"""
Main entry point for the Todo CLI application.
Full support: Basic + Intermediate + Advanced (Due Dates, Recurring Tasks, Reminders)
"""
import sys
from datetime import datetime as dt

from todo import TodoManager
from ui import (
    display_task_table,
    get_validated_input,
    validate_priority,
    validate_tags,
    display_search_results,
    display_filtered_tasks,
    display_sorted_tasks,
)


def print_help():
    """Print updated help with Advanced feature examples."""
    help_text = """
Evolution of Todo – Full Advanced CLI Help
==========================================
Commands:
  add "<title>" "<description>" [priority] [tags] [due_date] [recurrence]
      → priority: high | medium | low (default: medium)
      → tags: comma-separated (e.g. work,health)
      → due_date: YYYY-MM-DD or YYYY-MM-DD HH:MM (optional)
      → recurrence: daily | weekly | monthly | none (optional)

  list                  → Shows reminders first, then full sorted task list
  update <id> [title] [desc] [priority] [tags] [due_date] [recurrence]
  delete <id>
  complete <id>         → Recurring tasks auto-create next instance!
  incomplete <id>
  search <keyword>
  filter <type> <value> → type: status | priority | tag
  sort <type>           → type: priority | title | status
  help                  → Show this help
  exit                  → Quit

Examples:
  add "Team Meeting" "Weekly sync" high work "2026-01-09 10:00" weekly
  add "Gym" "Evening workout" medium health "2026-01-05 18:00" daily
  add "Pay rent" "Monthly bill" high finance "2026-02-01" monthly
  complete 1
  update 3 "" "" "" "" "2026-01-16 10:00" weekly
"""
    print(help_text)


def parse_command(user_input: str):
    """Robust parser that handles quoted strings properly."""
    if not user_input.strip():
        return "", []

    parts = user_input.strip().split()
    command = parts[0].lower()
    rest = user_input[len(parts[0]):].strip()

    args = []
    current = ""
    in_quotes = False
    quote_char = None

    for char in rest:
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
            if current:
                args.append(current)
            current = ""
        elif char == " " and not in_quotes:
            if current:
                args.append(current)
            current = ""
        else:
            current += char

    if current:
        args.append(current)

    return command, args


def main():
    """Main REPL loop – now with full Advanced support."""
    print("🚀 Welcome to Evolution of Todo – Full Advanced Version! 🚀")
    print("Type 'help' for commands • 'exit' to quit\n")

    todo_manager = TodoManager()

    while True:
        try:
            user_input = input("\ntodo> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command in ["exit", "quit"]:
                print("\nGoodbye! See you next time 👋")
                sys.exit(0)

            elif command == "help":
                print_help()

            elif command == "add":
                if len(args) < 2:
                    print("Usage: add \"<title>\" \"<description>\" [priority] [tags] [due_date] [recurrence]")
                    continue

                title = args[0]
                description = args[1]
                priority = (args[2].lower() if len(args) > 2 else "medium")
                tags_str = args[3] if len(args) > 3 else ""
                due_str = args[4] if len(args) > 4 else None
                recurrence = (args[5].lower() if len(args) > 5 else "none")

                if priority not in ["high", "medium", "low"]:
                    print("Invalid priority → defaulting to 'medium'")
                    priority = "medium"

                tags = validate_tags(tags_str)

                due_date = None
                if due_str and due_str.strip():
                    try:
                        if " " in due_str.strip():
                            due_date = dt.strptime(due_str.strip(), "%Y-%m-%d %H:%M")
                        else:
                            due_date = dt.strptime(due_str.strip(), "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format → due date ignored")
                        due_date = None

                if recurrence not in ["daily", "weekly", "monthly", "none"]:
                    print("Invalid recurrence → using 'none'")
                    recurrence = "none"

                task = todo_manager.add_task(
                    title=title,
                    description=description,
                    priority=priority,
                    tags=tags,
                    due_date=due_date,
                    recurrence=recurrence,
                )

                due_msg = due_date.strftime("%Y-%m-%d %H:%M") if due_date else "-"
                recur_msg = f" 🔁 {recurrence.capitalize()}" if recurrence != "none" else ""
                print(f"✅ Added task #{task.id}: {title} | Due: {due_msg}{recur_msg}")

            elif command == "list":
                reminders = todo_manager.get_reminders()
                if reminders:
                    print("\n🔥 === SMART REMINDERS === 🔥")
                    for line in reminders:
                        print(line)
                    print()

                tasks = todo_manager.list_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    display_task_table(tasks)

            elif command == "update":
                if len(args) < 1:
                    print("Usage: update <id> [title] [description] [priority] [tags] [due_date] [recurrence]")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                task = todo_manager.get_task_by_id(task_id)
                if not task:
                    print(f"Task with ID {task_id} not found.")
                    continue

                title = args[1] if len(args) > 1 and args[1] else task.title
                description = args[2] if len(args) > 2 and args[2] else task.description
                priority = args[3].lower() if len(args) > 3 and args[3] else task.priority
                tags_str = args[4] if len(args) > 4 else ""
                due_str = args[5] if len(args) > 5 else None
                recurrence = args[6].lower() if len(args) > 6 else task.recurrence

                if priority not in ["high", "medium", "low"]:
                    priority = task.priority

                tags = validate_tags(tags_str) if tags_str else task.tags

                due_date = task.due_date
                if due_str is not None:
                    if due_str.strip():
                        try:
                            if " " in due_str:
                                due_date = dt.strptime(due_str.strip(), "%Y-%m-%d %H:%M")
                            else:
                                due_date = dt.strptime(due_str.strip(), "%Y-%m-%d")
                        except ValueError:
                            print("Invalid date → keeping current")
                            due_date = task.due_date
                    else:
                        due_date = None

                if recurrence not in ["daily", "weekly", "monthly", "none"]:
                    recurrence = task.recurrence

                if todo_manager.update_task(task_id, title, description, priority, tags, due_date, recurrence):
                    print(f"Updated task #{task_id}")
                else:
                    print(f"Task with ID {task_id} not found.")

            elif command == "delete":
                if len(args) != 1:
                    print("Usage: delete <id>")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                if todo_manager.delete_task(task_id):
                    print(f"Deleted task #{task_id}")
                else:
                    print(f"Task with ID {task_id} not found.")

            elif command == "complete":
                if len(args) != 1:
                    print("Usage: complete <id>")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                result = todo_manager.mark_task_complete(task_id)
                if result is False:
                    print(f"Task with ID {task_id} not found.")
                elif result is True or result is None:
                    print(f"Marked task #{task_id} as complete ✅")
                else:
                    new_task = result
                    due_str = new_task.due_date.strftime("%Y-%m-%d %H:%M") if new_task.due_date else "N/A"
                    print(f"Marked task #{task_id} as complete ✅")
                    print(f"🔁 New recurring instance #{new_task.id} created → Due: {due_str}")

            elif command == "incomplete":
                if len(args) != 1:
                    print("Usage: incomplete <id>")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                if todo_manager.mark_task_incomplete(task_id):
                    print(f"Marked task #{task_id} as incomplete")
                else:
                    print(f"Task with ID {task_id} not found.")

            elif command == "search":
                if len(args) < 1:
                    print("Usage: search <keyword>")
                    continue

                keyword = " ".join(args)
                tasks = todo_manager.search_tasks(keyword)
                if not tasks:
                    print(f"No tasks found matching '{keyword}'.")
                else:
                    display_search_results(tasks, keyword)

            elif command == "filter":
                if len(args) < 2:
                    print("Usage: filter <type> <value>")
                    print("Types: status, priority, tag")
                    continue

                filter_type = args[0].lower()
                filter_value = args[1].lower()

                if filter_type not in ["status", "priority", "tag"]:
                    print("Filter type must be 'status', 'priority', or 'tag'.")
                    continue

                tasks = todo_manager.filter_tasks(filter_type, filter_value)
                if not tasks:
                    print(f"No tasks found matching filter: {filter_type} = {filter_value}.")
                else:
                    display_filtered_tasks(tasks, filter_type, filter_value)

            elif command == "sort":
                if len(args) < 1:
                    print("Usage: sort <type>")
                    print("Types: priority, title, status")
                    continue

                sort_type = args[0].lower()

                if sort_type not in ["priority", "title", "status"]:
                    print("Sort type must be 'priority', 'title', or 'status'.")
                    continue

                tasks = todo_manager.sort_tasks(sort_type)
                if not tasks:
                    print("No tasks to sort.")
                else:
                    display_sorted_tasks(tasks, sort_type)

            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except EOFError:
            print("\n\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
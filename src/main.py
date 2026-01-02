"""
Main entry point for the Todo CLI application.
Implements an interactive REPL loop for managing tasks.
"""
import sys
from todo import TodoManager
from ui import display_task_table, get_validated_input, validate_priority, validate_tags


def print_help():
    """Print help information showing all available commands."""
    help_text = """
Todo Application Help
=====================
Available commands:
  add <title> <description> [priority] [tags] - Add a new task with priority and tags
  list                        - List all tasks in enhanced format
  update <id> [title] [desc] [priority] [tags] - Update a task (optional fields)
  delete <id>                 - Delete a task
  complete <id>               - Mark task as complete
  incomplete <id>             - Mark task as incomplete
  search <keyword>            - Search tasks by keyword
  filter <type> <value>       - Filter tasks (type: status, priority, tag)
  sort <type>                 - Sort tasks (type: priority, title, status)
  help                        - Show this help message
  exit                        - Exit the application

Examples:
  add "Buy groceries" "Milk, bread, eggs" high "shopping,urgent"
  list
  update 1 "Buy groceries" "Milk, bread, eggs, fruits" medium "shopping"
  complete 1
  delete 2
  search "groceries"
  filter priority high
  sort title
"""
    print(help_text)


def parse_command(user_input: str) -> tuple:
    """
    Parse user input into command and arguments.
    
    Args:
        user_input: Raw user input string
        
    Returns:
        Tuple of (command, args_list)
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    
    command = parts[0].lower()
    args = parts[1:]
    
    # Handle quoted arguments
    if '"' in user_input or "'" in user_input:
        args = []
        current_arg = ""
        in_quotes = False
        quote_char = None
        
        i = 0
        while i < len(user_input):
            char = user_input[i]
            
            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
                args.append(current_arg)
                current_arg = ""
            elif char == " " and not in_quotes and current_arg:
                args.append(current_arg)
                current_arg = ""
            elif not (char == " " and not current_arg):
                current_arg += char
            
            i += 1
        
        if current_arg:
            args.append(current_arg)
        
        # Remove the command from args if it was parsed as part of the quoted string
        if args and args[0].lower() == command:
            args = args[1:]
    
    return command, args


def main():
    """Main application loop."""
    print("Welcome to the Enhanced Todo Application!")
    print("Type 'help' for available commands or 'exit' to quit.")

    todo_manager = TodoManager()

    while True:
        try:
            user_input = input("\ntodo> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command in ["exit", "quit"]:
                print("Goodbye!")
                sys.exit(0)

            elif command == "help":
                print_help()

            elif command == "add":
                if len(args) < 2:
                    print("Usage: add <title> <description> [priority] [tags]")
                    continue

                title = args[0]
                description = args[1] if len(args) > 1 else ""

                # Get priority if provided, otherwise use default
                priority = args[2] if len(args) > 2 else "Medium"
                if not validate_priority(priority):
                    print("Priority must be 'high', 'medium', or 'low'. Using default 'Medium'.")
                    priority = "Medium"

                # Get tags if provided
                tags_str = args[3] if len(args) > 3 else ""
                tags = validate_tags(tags_str)

                task = todo_manager.add_task(title, description, priority, tags)
                print(f"Added task #{task.id}: {task.title} (Priority: {task.priority}, Tags: {', '.join(task.tags) if task.tags else '-'})")

            elif command == "list":
                tasks = todo_manager.list_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    display_task_table(tasks)

            elif command == "update":
                if len(args) < 1:
                    print("Usage: update <id> [title] [description] [priority] [tags]")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                # Get current task to use existing values if not provided
                task = todo_manager.get_task_by_id(task_id)
                if not task:
                    print(f"Task with ID {task_id} not found.")
                    continue

                # Use provided values or keep existing ones
                title = args[1] if len(args) > 1 else task.title
                description = args[2] if len(args) > 2 else task.description
                priority = args[3] if len(args) > 3 else task.priority
                tags_str = args[4] if len(args) > 4 else ""

                # Validate priority
                if priority and not validate_priority(priority):
                    print("Priority must be 'high', 'medium', or 'low'. Keeping current value.")
                    priority = task.priority

                # Validate tags
                tags = validate_tags(tags_str) if tags_str else task.tags

                if todo_manager.update_task(task_id, title, description, priority, tags):
                    print(f"Updated task #{task_id}: {title} (Priority: {priority}, Tags: {', '.join(tags) if tags else '-'})")
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

            elif command in ["complete", "incomplete"]:
                if len(args) != 1:
                    print(f"Usage: {command} <id>")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                if command == "complete":
                    if todo_manager.mark_task_complete(task_id):
                        print(f"Marked task #{task_id} as complete")
                    else:
                        print(f"Task with ID {task_id} not found.")
                else:  # incomplete
                    if todo_manager.mark_task_incomplete(task_id):
                        print(f"Marked task #{task_id} as incomplete")
                    else:
                        print(f"Task with ID {task_id} not found.")

            elif command == "search":
                if len(args) < 1:
                    print("Usage: search <keyword>")
                    continue

                keyword = args[0]
                tasks = todo_manager.search_tasks(keyword)
                if not tasks:
                    print(f"No tasks found matching '{keyword}'.")
                else:
                    from ui import display_search_results
                    display_search_results(tasks, keyword)

            elif command == "filter":
                if len(args) < 2:
                    print("Usage: filter <type> <value>")
                    print("Types: status, priority, tag")
                    print("Values for status: completed, incomplete")
                    print("Values for priority: high, medium, low")
                    continue

                filter_type = args[0].lower()
                filter_value = args[1].lower()

                # Validate filter type
                if filter_type not in ["status", "priority", "tag"]:
                    print("Filter type must be 'status', 'priority', or 'tag'.")
                    continue

                # Validate filter value based on type
                if filter_type == "status" and filter_value not in ["completed", "incomplete"]:
                    print("Status filter value must be 'completed' or 'incomplete'.")
                    continue
                elif filter_type == "priority" and filter_value not in ["high", "medium", "low"]:
                    print("Priority filter value must be 'high', 'medium', or 'low'.")
                    continue

                tasks = todo_manager.filter_tasks(filter_type, filter_value)
                if not tasks:
                    print(f"No tasks found matching filter: {filter_type} = {filter_value}.")
                else:
                    from ui import display_filtered_tasks
                    display_filtered_tasks(tasks, filter_type, filter_value)

            elif command == "sort":
                if len(args) < 1:
                    print("Usage: sort <type>")
                    print("Types: priority, title, status")
                    continue

                sort_type = args[0].lower()

                # Validate sort type
                if sort_type not in ["priority", "title", "status"]:
                    print("Sort type must be 'priority', 'title', or 'status'.")
                    continue

                tasks = todo_manager.sort_tasks(sort_type)
                if not tasks:
                    print("No tasks to sort.")
                else:
                    from ui import display_sorted_tasks
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
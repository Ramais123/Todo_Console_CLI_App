import sys
from datetime import datetime
from typing import List, Optional

# Import the necessary modules
import os
import sys

# Add the src directory to the path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.todo import Task
from services.todo_service import TodoService
from lib.date_utils import is_overdue, is_due_today, is_upcoming


def show_reminders(todo_service: TodoService):
    """
    Display reminder section at startup and after key actions showing:
    - Today's due tasks
    - Overdue tasks
    - Upcoming tasks in the next 3 days
    """
    current_time = datetime.now()
    all_tasks = todo_service.get_all_tasks()

    overdue_tasks = []
    due_today_tasks = []
    upcoming_tasks = []

    for task in all_tasks:
        if not task.completed and task.due_date:
            if is_overdue(task.due_date, current_time):
                overdue_tasks.append(task)
            elif is_due_today(task.due_date, current_time):
                due_today_tasks.append(task)
            elif is_upcoming(task.due_date, current_time):
                upcoming_tasks.append(task)

    # Display reminders
    if overdue_tasks:
        print(f"\n🔥 OVERDUE TASKS ({len(overdue_tasks)}):")
        for task in overdue_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")

    if due_today_tasks:
        print(f"\n⏰ DUE TODAY ({len(due_today_tasks)}):")
        for task in due_today_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")

    if upcoming_tasks:
        print(f"\n📅 UPCOMING ({len(upcoming_tasks)}):")
        for task in upcoming_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("TODO APP - ADVANCED FEATURES")
    print("="*40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")
    print("="*40)


def get_user_choice() -> str:
    """Get user's menu choice"""
    choice = input("Enter your choice (1-6): ").strip()
    return choice


def add_task(todo_service: TodoService):
    """Add a new task with due date and recurrence options"""
    print("\n--- ADD TASK ---")
    
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    
    description = input("Enter task description (optional, press Enter to skip): ").strip()
    
    priority = input("Enter priority (High/Medium/Low, default: Medium): ").strip().title()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"
    
    tags_input = input("Enter tags (comma-separated, press Enter to skip): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
    
    # Prompt for due date
    due_date_input = input("Enter due date (YYYY-MM-DD HH:MM) or press Enter for none: ").strip()
    due_date = None
    if due_date_input:
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Task will be created without due date.")
    
    # Prompt for recurrence
    recurrence = input("Enter recurrence (none/daily/weekly/monthly, default: none): ").strip().lower()
    if recurrence not in ["none", "daily", "weekly", "monthly"]:
        recurrence = "none"
    
    try:
        new_task = todo_service.add_task(
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence=recurrence
        )
        print(f"Task '{new_task.title}' added successfully with ID {new_task.id}")
    except ValueError as e:
        print(f"Error adding task: {e}")


def view_tasks(todo_service: TodoService):
    """View all tasks with enhanced display"""
    print("\n--- VIEW TASKS ---")
    tasks = todo_service.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    # Sort tasks by due date (soonest first), then by priority
    sorted_tasks = todo_service.get_sorted_tasks()
    
    print(f"{'ID':<3} | {'Priority':<8} | {'Title':<20} | {'Tags':<15} | {'Due':<16} | {'Status':<8} | {'Description'}")
    print("-" * 100)
    
    for task in sorted_tasks:
        due_str = task.due_date.strftime('%Y-%m-%d %H:%M') if task.due_date else "-"
        status_str = "✅" if task.completed else "🔁" if task.recurrence != "none" else "⏳"
        
        # Add visual indicators for overdue tasks
        if task.due_date and is_overdue(task.due_date, datetime.now()):
            status_str = "🔥 OVERDUE"
        
        tags_str = ", ".join(task.tags[:2])  # Show first 2 tags
        if len(task.tags) > 2:
            tags_str += f" (+{len(task.tags)-2})"
        
        print(f"{task.id:<3} | {task.priority:<8} | {task.title[:20]:<20} | {tags_str:<15} | {due_str:<16} | {status_str:<8} | {task.description}")


def update_task(todo_service: TodoService):
    """Update an existing task"""
    print("\n--- UPDATE TASK ---")
    
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    task = todo_service.get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    print(f"Updating task: {task.title}")
    
    # Ask for updates
    new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep): ").strip()
    new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep): ").strip()
    new_priority = input(f"Enter new priority (High/Medium/Low, current: '{task.priority}', press Enter to keep): ").strip().title()
    
    tags_input = input(f"Enter new tags (comma-separated, current: {task.tags}, press Enter to keep): ").strip()
    new_tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else None
    
    # Due date update
    due_date_input = input(f"Enter new due date (YYYY-MM-DD HH:MM, current: {task.due_date}, press Enter to keep): ").strip()
    new_due_date = None
    if due_date_input:
        try:
            new_due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Due date will not be changed.")
            new_due_date = None
    elif due_date_input == "":
        new_due_date = task.due_date  # Keep existing due date
    
    # Recurrence update
    new_recurrence = input(f"Enter new recurrence (none/daily/weekly/monthly, current: '{task.recurrence}', press Enter to keep): ").strip().lower()
    if new_recurrence and new_recurrence not in ["none", "daily", "weekly", "monthly"]:
        print("Invalid recurrence value. Recurrence will not be changed.")
        new_recurrence = task.recurrence
    elif not new_recurrence:
        new_recurrence = task.recurrence  # Keep existing recurrence
    
    # Update the task
    updated_task = todo_service.update_task(
        task_id=task_id,
        title=new_title if new_title else None,
        description=new_description if new_description else None,
        priority=new_priority if new_priority in ["High", "Medium", "Low"] else None,
        tags=new_tags,
        due_date=new_due_date,
        recurrence=new_recurrence
    )
    
    if updated_task:
        print(f"Task '{updated_task.title}' updated successfully.")
    else:
        print("Failed to update task.")


def complete_task(todo_service: TodoService):
    """Mark a task as complete"""
    print("\n--- COMPLETE TASK ---")
    
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    completed_task = todo_service.complete_task(task_id)
    if completed_task:
        print(f"Task '{completed_task.title}' marked as complete.")
        
        # If it was a recurring task, inform about the new instance
        if completed_task.recurrence != "none":
            print(f"A new instance of this recurring task has been created with the next due date.")
    else:
        print(f"Task with ID {task_id} not found or already completed.")


def delete_task(todo_service: TodoService):
    """Delete a task"""
    print("\n--- DELETE TASK ---")
    
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    deleted_task = todo_service.delete_task(task_id)
    if deleted_task:
        print(f"Task '{deleted_task.title}' deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")


def main():
    """Main application loop"""
    print("Welcome to the Advanced Todo App!")
    print("This app includes recurring tasks and due date reminders.")
    
    # Initialize the todo service
    todo_service = TodoService()
    
    # Show initial reminders
    show_reminders(todo_service)
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            add_task(todo_service)
            show_reminders(todo_service)  # Show reminders after adding a task
        elif choice == "2":
            view_tasks(todo_service)
        elif choice == "3":
            update_task(todo_service)
            show_reminders(todo_service)  # Show reminders after updating a task
        elif choice == "4":
            complete_task(todo_service)
            show_reminders(todo_service)  # Show reminders after completing a task
        elif choice == "5":
            delete_task(todo_service)
            show_reminders(todo_service)  # Show reminders after deleting a task
        elif choice == "6":
            print("Thank you for using the Advanced Todo App!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
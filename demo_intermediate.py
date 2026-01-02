#!/usr/bin/env python3
"""
Demo script showing all Basic + Intermediate capabilities of the Todo app.
This script demonstrates the end-to-end functionality of the enhanced todo app.
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import TodoManager
from ui import display_task_table


def demo_basic_features():
    """Demonstrate basic todo functionality."""
    print("=== DEMO: Basic Features ===")
    
    # Create a todo manager
    tm = TodoManager()
    
    # Add some tasks
    print("\n1. Adding tasks:")
    task1 = tm.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"   Added task #{task1.id}: {task1.title}")
    
    task2 = tm.add_task("Finish report", "Complete the quarterly report for work")
    print(f"   Added task #{task2.id}: {task2.title}")
    
    # List all tasks
    print("\n2. Listing all tasks:")
    tasks = tm.list_tasks()
    display_task_table(tasks)
    
    # Update a task
    print("\n3. Updating a task:")
    tm.update_task(task1.id, title="Buy groceries", description="Milk, bread, eggs, fruits, vegetables")
    print(f"   Updated task #{task1.id}")
    
    # Mark a task as complete
    print("\n4. Marking a task as complete:")
    tm.mark_task_complete(task1.id)
    print(f"   Marked task #{task1.id} as complete")
    
    # List tasks again to see changes
    print("\n5. Listing tasks after updates:")
    tasks = tm.list_tasks()
    display_task_table(tasks)
    
    return tm


def demo_intermediate_features():
    """Demonstrate intermediate todo functionality."""
    print("\n\n=== DEMO: Intermediate Features ===")
    
    # Create a todo manager
    tm = TodoManager()
    
    # Add tasks with priorities and tags
    print("\n1. Adding tasks with priorities and tags:")
    task1 = tm.add_task("Fix critical bug", "Fix the login bug that's blocking users", "High", ["work", "urgent", "bug"])
    print(f"   Added task #{task1.id}: {task1.title} (Priority: {task1.priority}, Tags: {task1.tags})")
    
    task2 = tm.add_task("Plan vacation", "Plan summer vacation with family", "Medium", ["personal", "vacation"])
    print(f"   Added task #{task2.id}: {task2.title} (Priority: {task2.priority}, Tags: {task2.tags})")
    
    task3 = tm.add_task("Organize desk", "Clean and organize the workspace", "Low", ["work", "organization"])
    print(f"   Added task #{task3.id}: {task3.title} (Priority: {task3.priority}, Tags: {task3.tags})")
    
    task4 = tm.add_task("Call plumber", "Fix the leaking kitchen tap", "High", ["home", "urgent"])
    print(f"   Added task #{task4.id}: {task4.title} (Priority: {task4.priority}, Tags: {task4.tags})")
    
    # List all tasks with enhanced view
    print("\n2. Listing all tasks with enhanced view:")
    tasks = tm.list_tasks()
    display_task_table(tasks)
    
    # Search tasks
    print("\n3. Searching for tasks containing 'fix':")
    search_results = tm.search_tasks("fix")
    display_task_table(search_results)
    
    # Filter tasks by priority
    print("\n4. Filtering tasks by priority (High):")
    high_priority_tasks = tm.filter_tasks("priority", "high")
    display_task_table(high_priority_tasks)
    
    # Filter tasks by tag
    print("\n5. Filtering tasks by tag (work):")
    work_tasks = tm.filter_tasks("tag", "work")
    display_task_table(work_tasks)
    
    # Sort tasks by priority
    print("\n6. Sorting tasks by priority:")
    sorted_tasks = tm.sort_tasks("priority")
    display_task_table(sorted_tasks)
    
    # Sort tasks by title
    print("\n7. Sorting tasks alphabetically by title:")
    sorted_tasks = tm.sort_tasks("title")
    display_task_table(sorted_tasks)
    
    # Sort tasks by status
    print("\n8. Marking a task as complete and sorting by status:")
    tm.mark_task_complete(task2.id)
    sorted_tasks = tm.sort_tasks("status")  # Incomplete first
    display_task_table(sorted_tasks)
    
    return tm


def demo_end_to_end_flow():
    """Demonstrate an end-to-end flow as described in the requirements."""
    print("\n\n=== DEMO: End-to-End Flow ===")
    print("Following the flow: add tasks with priority/tags -> search -> filter by tag -> sort by priority -> update tags")
    
    tm = TodoManager()
    
    # Add tasks with priority and tags
    print("\n1. Adding tasks with priorities and tags:")
    tm.add_task("Implement login", "Create user login functionality", "High", ["work", "feature"])
    tm.add_task("Write tests", "Write unit tests for new features", "Medium", ["work", "testing"])
    tm.add_task("Buy groceries", "Milk, bread, eggs", "Medium", ["personal", "shopping"])
    tm.add_task("Fix bug", "Fix critical security bug", "High", ["work", "bug", "urgent"])
    tm.add_task("Plan meeting", "Schedule team meeting", "Low", ["work", "meeting"])
    
    print("   Added 5 tasks with various priorities and tags")
    
    # View all tasks
    print("\n2. All tasks:")
    display_task_table(tm.list_tasks())
    
    # Search for tasks
    print("\n3. Searching for 'fix':")
    results = tm.search_tasks("fix")
    display_task_table(results)
    
    # Filter by tag
    print("\n4. Filtering by 'work' tag:")
    work_tasks = tm.filter_tasks("tag", "work")
    display_task_table(work_tasks)
    
    # Sort by priority
    print("\n5. Sorting all tasks by priority:")
    sorted_tasks = tm.sort_tasks("priority")
    display_task_table(sorted_tasks)
    
    # Update tags
    print("\n6. Updating tags for task #1 (adding 'security' tag):")
    first_task = tm.list_tasks()[0]  # Get the first task
    new_tags = first_task.tags + ["security"]
    tm.update_task(first_task.id, tags=new_tags)
    print(f"   Updated task #{first_task.id} tags to: {new_tags}")
    
    # Final view
    print("\n7. Final view of all tasks:")
    display_task_table(tm.list_tasks())
    
    print("\nEnd-to-end demo completed successfully!")


if __name__ == "__main__":
    print("Todo App Intermediate Features Demo")
    print("===================================")
    
    # Run basic features demo
    basic_tm = demo_basic_features()
    
    # Run intermediate features demo
    intermediate_tm = demo_intermediate_features()
    
    # Run end-to-end flow demo
    demo_end_to_end_flow()
    
    print("\n\nAll demos completed! The Todo app with Intermediate features is working correctly.")
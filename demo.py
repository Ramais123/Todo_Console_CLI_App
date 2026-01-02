"""
Demo script to showcase the todo application functionality.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import TodoManager


def demo():
    """Demonstrate the todo application functionality."""
    print("Todo Application Demo")
    print("=====================")
    
    # Create a new todo manager
    tm = TodoManager()
    
    print("\n1. Adding tasks:")
    task1 = tm.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added: {task1}")
    
    task2 = tm.add_task("Walk the dog", "Take Fido to the park")
    print(f"   Added: {task2}")
    
    task3 = tm.add_task("Read a book", "Finish reading the Python cookbook")
    print(f"   Added: {task3}")
    
    print(f"\n2. Listing all tasks:")
    tasks = tm.list_tasks()
    print("   ID  Status  Title")
    print("   --  ------  -----")
    for task in tasks:
        status = "x" if task.completed else " "
        print(f"   {task.id:<3} [{status}]     {task.title}")
    
    print(f"\n3. Updating a task:")
    success = tm.update_task(1, "Buy weekly groceries", "Milk, bread, eggs, fruits, vegetables")
    if success:
        updated_task = tm.get_task_by_id(1)
        print(f"   Updated task #{updated_task.id}: {updated_task.title}")
    
    print(f"\n4. Marking a task as complete:")
    success = tm.mark_task_complete(2)
    if success:
        completed_task = tm.get_task_by_id(2)
        print(f"   Marked task #{completed_task.id} as complete: {completed_task.title}")
    
    print(f"\n5. Listing tasks after updates:")
    tasks = tm.list_tasks()
    print("   ID  Status  Title")
    print("   --  ------  -----")
    for task in tasks:
        status = "x" if task.completed else " "
        print(f"   {task.id:<3} [{status}]     {task.title}")
    
    print(f"\n6. Deleting a task:")
    success = tm.delete_task(3)
    if success:
        print(f"   Deleted task #3")
    
    print(f"\n7. Final task list:")
    tasks = tm.list_tasks()
    if not tasks:
        print("   No tasks remaining.")
    else:
        print("   ID  Status  Title")
        print("   --  ------  -----")
        for task in tasks:
            status = "x" if task.completed else " "
            print(f"   {task.id:<3} [{status}]     {task.title}")
    
    print(f"\n8. Testing error handling:")
    success = tm.delete_task(999)
    if not success:
        print("   Attempted to delete non-existent task #999 - handled gracefully")
    
    task = tm.get_task_by_id(999)
    if task is None:
        print("   Attempted to get non-existent task #999 - handled gracefully")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    demo()
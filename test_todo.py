"""
Simple test script to verify the todo application functionality.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import TodoManager, Task


def test_todo_functionality():
    """Test all functionality of the TodoManager."""
    print("Testing TodoManager functionality...")
    
    # Create a new todo manager
    tm = TodoManager()
    
    # Test adding tasks
    print("\n1. Testing add_task functionality")
    task1 = tm.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"Added task: {task1}")
    
    task2 = tm.add_task("Walk the dog", "Take Fido to the park")
    print(f"Added task: {task2}")
    
    # Verify auto-incrementing IDs
    assert task1.id == 1, f"Expected ID 1, got {task1.id}"
    assert task2.id == 2, f"Expected ID 2, got {task2.id}"
    print("PASS: Auto-incrementing IDs working correctly")
    
    # Test listing tasks
    print("\n2. Testing list_tasks functionality")
    tasks = tm.list_tasks()
    print(f"Number of tasks: {len(tasks)}")
    for task in tasks:
        print(f"  - {task}")
    assert len(tasks) == 2, f"Expected 2 tasks, got {len(tasks)}"
    print("PASS: Task listing working correctly")
    
    # Test getting task by ID
    print("\n3. Testing get_task_by_id functionality")
    retrieved_task = tm.get_task_by_id(1)
    assert retrieved_task is not None, "Task with ID 1 should exist"
    assert retrieved_task.id == 1, f"Expected ID 1, got {retrieved_task.id}"
    assert retrieved_task.title == "Buy groceries", f"Expected 'Buy groceries', got {retrieved_task.title}"
    print(f"Retrieved task: {retrieved_task}")
    print("PASS: Get task by ID working correctly")
    
    # Test updating task
    print("\n4. Testing update_task functionality")
    success = tm.update_task(1, "Buy weekly groceries", "Milk, bread, eggs, fruits, vegetables")
    assert success, "Update should succeed for existing task"
    
    updated_task = tm.get_task_by_id(1)
    assert updated_task.title == "Buy weekly groceries", f"Expected 'Buy weekly groceries', got {updated_task.title}"
    assert updated_task.description == "Milk, bread, eggs, fruits, vegetables", f"Expected updated description, got {updated_task.description}"
    print(f"Updated task: {updated_task}")
    print("PASS: Task update working correctly")
    
    # Test marking as complete/incomplete
    print("\n5. Testing mark_task_complete/mark_task_incomplete functionality")
    assert not updated_task.completed, "Task should initially be incomplete"
    
    success = tm.mark_task_complete(1)
    assert success, "Mark complete should succeed for existing task"
    assert updated_task.completed, "Task should now be complete"
    print(f"Marked task as complete: {updated_task}")
    
    success = tm.mark_task_incomplete(1)
    assert success, "Mark incomplete should succeed for existing task"
    assert not updated_task.completed, "Task should now be incomplete"
    print(f"Marked task as incomplete: {updated_task}")
    print("PASS: Mark complete/incomplete working correctly")
    
    # Test deleting task
    print("\n6. Testing delete_task functionality")
    assert len(tm.list_tasks()) == 2, f"Expected 2 tasks before deletion, got {len(tm.list_tasks())}"
    
    success = tm.delete_task(1)
    assert success, "Delete should succeed for existing task"
    assert len(tm.list_tasks()) == 1, f"Expected 1 task after deletion, got {len(tm.list_tasks())}"
    
    retrieved_task = tm.get_task_by_id(1)
    assert retrieved_task is None, "Task with ID 1 should no longer exist"
    print("PASS: Task deletion working correctly")
    
    # Test error handling for non-existent tasks
    print("\n7. Testing error handling for non-existent tasks")
    non_existent = tm.get_task_by_id(999)
    assert non_existent is None, "Should return None for non-existent task"
    
    update_success = tm.update_task(999, "New title", "New description")
    assert not update_success, "Update should fail for non-existent task"
    
    delete_success = tm.delete_task(999)
    assert not delete_success, "Delete should fail for non-existent task"
    
    complete_success = tm.mark_task_complete(999)
    assert not complete_success, "Mark complete should fail for non-existent task"
    
    incomplete_success = tm.mark_task_incomplete(999)
    assert not incomplete_success, "Mark incomplete should fail for non-existent task"
    
    print("PASS: Error handling for non-existent tasks working correctly")
    
    print("\nPASS: All tests passed! TodoManager functionality verified.")


if __name__ == "__main__":
    test_todo_functionality()
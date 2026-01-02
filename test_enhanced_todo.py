"""
Simple test to verify the enhanced todo app functionality.
"""
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import TodoManager
from ui import display_task_table


def test_basic_functionality():
    """Test basic todo functionality still works."""
    print("Testing basic functionality...")
    tm = TodoManager()
    
    # Add a task
    task = tm.add_task("Test task", "This is a test")
    assert task.title == "Test task"
    assert task.description == "This is a test"
    assert task.completed == False
    assert task.priority == "Medium"  # Default priority
    assert task.tags == []  # Default tags
    
    # List tasks
    tasks = tm.list_tasks()
    assert len(tasks) == 1
    
    # Update task
    tm.update_task(task.id, title="Updated test task")
    updated_task = tm.get_task_by_id(task.id)
    assert updated_task.title == "Updated test task"
    
    # Mark complete
    tm.mark_task_complete(task.id)
    completed_task = tm.get_task_by_id(task.id)
    assert completed_task.completed == True
    
    # Delete task
    tm.delete_task(task.id)
    tasks = tm.list_tasks()
    assert len(tasks) == 0
    
    print("PASS: Basic functionality test passed")


def test_intermediate_features():
    """Test intermediate features."""
    print("Testing intermediate features...")
    tm = TodoManager()
    
    # Add task with priority and tags
    task = tm.add_task("High priority task", "Description", "High", ["work", "urgent"])
    assert task.priority == "High"
    assert "work" in task.tags
    assert "urgent" in task.tags
    
    # Add another task with different priority
    task2 = tm.add_task("Low priority task", "Another description", "Low", ["personal"])
    assert task2.priority == "Low"
    assert "personal" in task2.tags
    
    # Test search
    results = tm.search_tasks("high")
    assert len(results) == 1
    assert results[0].id == task.id
    
    # Test filter by priority
    high_priority_tasks = tm.filter_tasks("priority", "high")
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0].priority.lower() == "high"
    
    # Test filter by tag
    work_tasks = tm.filter_tasks("tag", "work")
    assert len(work_tasks) == 1
    assert "work" in work_tasks[0].tags
    
    # Test sort by priority
    all_tasks = tm.list_tasks()
    assert len(all_tasks) == 2
    
    sorted_tasks = tm.sort_tasks("priority")  # Should put high priority first
    assert sorted_tasks[0].priority == "High"
    assert sorted_tasks[1].priority == "Low"
    
    # Test sort by title
    sorted_by_title = tm.sort_tasks("title")
    # Should be sorted alphabetically: "High priority task", "Low priority task"
    assert sorted_by_title[0].title == "High priority task"
    assert sorted_by_title[1].title == "Low priority task"
    
    # Test sort by status
    tm.mark_task_complete(task.id)  # Mark first task as complete
    sorted_by_status = tm.sort_tasks("status")  # Should put incomplete first
    assert sorted_by_status[0].completed == False  # Second task is incomplete
    assert sorted_by_status[1].completed == True   # First task is complete
    
    print("PASS: Intermediate features test passed")


def test_edge_cases():
    """Test edge cases."""
    print("Testing edge cases...")
    tm = TodoManager()
    
    # Add task with empty tags
    task = tm.add_task("Test", "Description", "Medium", [])
    assert task.tags == []
    
    # Add task with priority in different case
    task2 = tm.add_task("Test2", "Description2", "HIGH", ["TAG1", "tag2"])
    assert task2.priority == "HIGH"  # Priority should maintain case
    assert "tag1" in [tag.lower() for tag in task2.tags]  # Tags should be case-insensitive for filtering
    assert "tag2" in [tag.lower() for tag in task2.tags]
    
    # Search with case-insensitivity
    results = tm.search_tasks("test")  # lowercase
    assert len(results) == 2  # Should find both tasks
    
    results = tm.search_tasks("DESCRIPTION")  # uppercase
    assert len(results) == 2  # Should find both tasks
    
    print("PASS: Edge cases test passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for enhanced todo app...")
    print()
    
    test_basic_functionality()
    test_intermediate_features()
    test_edge_cases()
    
    print()
    print("SUCCESS: All tests passed! The enhanced todo app is working correctly.")


if __name__ == "__main__":
    run_all_tests()
"""
Unit tests for the Todo application.
Tests the core functionality of Task dataclass and TodoManager class.
"""
import unittest
from src.todo import Task, TodoManager


class TestTask(unittest.TestCase):
    """Test cases for the Task dataclass."""
    
    def test_task_creation(self):
        """Test creating a Task with required fields."""
        task = Task(id=1, title="Test Task", description="Test Description")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
    
    def test_task_completion(self):
        """Test toggling the completion status of a Task."""
        task = Task(id=1, title="Test Task", description="Test Description")
        
        # Initially should be incomplete
        self.assertFalse(task.completed)
        
        # Mark as complete
        task.completed = True
        self.assertTrue(task.completed)
        
        # Mark as incomplete again
        task.completed = False
        self.assertFalse(task.completed)
    
    def test_task_string_representation(self):
        """Test the string representation of a Task."""
        task = Task(id=1, title="Test Task", description="Test Description")
        
        # Test incomplete task representation
        expected_incomplete = "[ ] 1 - Test Task - Test Description"
        self.assertEqual(str(task)[:len(expected_incomplete)], expected_incomplete)
        
        # Test complete task representation
        task.completed = True
        expected_complete = "[x] 1 - Test Task - Test Description"
        self.assertEqual(str(task)[:len(expected_complete)], expected_complete)


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""
    
    def setUp(self):
        """Set up a fresh TodoManager for each test."""
        self.manager = TodoManager()
    
    def test_add_task(self):
        """Test adding a task to the TodoManager."""
        task = self.manager.add_task("Test Title", "Test Description")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        
        # Verify the task is in the list
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task)
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with auto-incrementing IDs."""
        task1 = self.manager.add_task("Task 1", "Description 1")
        task2 = self.manager.add_task("Task 2", "Description 2")
        task3 = self.manager.add_task("Task 3", "Description 3")
        
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)
    
    def test_list_tasks(self):
        """Test listing all tasks."""
        # Initially should be empty
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 0)
        
        # Add tasks and verify they appear
        task1 = self.manager.add_task("Task 1", "Description 1")
        task2 = self.manager.add_task("Task 2", "Description 2")
        
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)
    
    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        task = self.manager.add_task("Test Task", "Test Description")
        
        # Retrieve existing task
        retrieved_task = self.manager.get_task_by_id(1)
        self.assertEqual(retrieved_task, task)
        
        # Try to retrieve non-existent task
        non_existent = self.manager.get_task_by_id(999)
        self.assertIsNone(non_existent)
    
    def test_update_task(self):
        """Test updating a task's title and description."""
        task = self.manager.add_task("Original Title", "Original Description")
        
        # Update both title and description
        success = self.manager.update_task(1, "New Title", "New Description")
        self.assertTrue(success)
        
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
        
        # Update only title
        success = self.manager.update_task(1, "Updated Title")
        self.assertTrue(success)
        
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "New Description")  # Should remain unchanged
        
        # Update only description
        success = self.manager.update_task(1, description="Updated Description")
        self.assertTrue(success)
        
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "Updated Title")  # Should remain unchanged
        self.assertEqual(updated_task.description, "Updated Description")
        
        # Try to update non-existent task
        success = self.manager.update_task(999, "New Title", "New Description")
        self.assertFalse(success)
    
    def test_delete_task(self):
        """Test deleting a task by its ID."""
        task = self.manager.add_task("Test Task", "Test Description")
        
        # Verify task exists
        self.assertIsNotNone(self.manager.get_task_by_id(1))
        
        # Delete the task
        success = self.manager.delete_task(1)
        self.assertTrue(success)
        
        # Verify task no longer exists
        self.assertIsNone(self.manager.get_task_by_id(1))
        
        # Try to delete non-existent task
        success = self.manager.delete_task(999)
        self.assertFalse(success)
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.manager.add_task("Test Task", "Test Description")
        
        # Initially should be incomplete
        self.assertFalse(task.completed)
        
        # Mark as complete
        success = self.manager.mark_task_complete(1)
        self.assertTrue(success)
        self.assertTrue(task.completed)
        
        # Try to mark non-existent task as complete
        success = self.manager.mark_task_complete(999)
        self.assertFalse(success)
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.manager.add_task("Test Task", "Test Description")
        
        # Mark as complete first
        self.manager.mark_task_complete(1)
        self.assertTrue(task.completed)
        
        # Mark as incomplete
        success = self.manager.mark_task_incomplete(1)
        self.assertTrue(success)
        self.assertFalse(task.completed)
        
        # Try to mark non-existent task as incomplete
        success = self.manager.mark_task_incomplete(999)
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()
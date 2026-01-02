import pytest
from datetime import datetime, timedelta
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestAdditionalUnitTests:
    """
    Additional unit tests for the todo application
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_add_task_with_all_properties(self):
        """Test adding a task with all properties set"""
        due_date = datetime.now() + timedelta(days=5)
        task = self.service.add_task(
            title="Complete project",
            description="Finish the project documentation",
            completed=False,
            priority="High",
            tags=["work", "important"],
            due_date=due_date,
            recurrence="none"
        )
        
        assert task.title == "Complete project"
        assert task.description == "Finish the project documentation"
        assert task.completed is False
        assert task.priority == "High"
        assert task.tags == ["work", "important"]
        assert task.due_date == due_date
        assert task.recurrence == "none"
        assert task.created_at is not None
        assert task.updated_at is not None
    
    def test_update_task_completely(self):
        """Test updating all properties of a task"""
        original_task = self.service.add_task(
            title="Original task",
            description="Original description",
            priority="Low",
            tags=["old"],
            due_date=datetime.now() + timedelta(days=1),
            recurrence="none"
        )
        
        new_due_date = datetime.now() + timedelta(days=10)
        updated_task = self.service.update_task(
            task_id=original_task.id,
            title="Updated task",
            description="Updated description",
            completed=True,
            priority="High",
            tags=["new", "updated"],
            due_date=new_due_date,
            recurrence="weekly"
        )
        
        assert updated_task.title == "Updated task"
        assert updated_task.description == "Updated description"
        assert updated_task.completed is True
        assert updated_task.priority == "High"
        assert updated_task.tags == ["new", "updated"]
        assert updated_task.due_date == new_due_date
        assert updated_task.recurrence == "weekly"
    
    def test_delete_task(self):
        """Test deleting a task"""
        task = self.service.add_task(title="Task to delete")
        assert len(self.service.get_all_tasks()) == 1
        
        deleted_task = self.service.delete_task(task.id)
        assert deleted_task.title == "Task to delete"
        assert len(self.service.get_all_tasks()) == 0
        
        # Verify the task is really gone
        assert self.service.get_task_by_id(task.id) is None
    
    def test_get_task_by_id(self):
        """Test retrieving a task by its ID"""
        task = self.service.add_task(title="Find me by ID")
        retrieved_task = self.service.get_task_by_id(task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        assert retrieved_task.title == "Find me by ID"
    
    def test_get_task_by_id_nonexistent(self):
        """Test retrieving a non-existent task by ID"""
        retrieved_task = self.service.get_task_by_id(999)
        
        assert retrieved_task is None
    
    def test_task_id_uniqueness(self):
        """Test that task IDs are unique"""
        task1 = self.service.add_task(title="First task")
        task2 = self.service.add_task(title="Second task")
        task3 = self.service.add_task(title="Third task")
        
        # All IDs should be different
        ids = [task1.id, task2.id, task3.id]
        assert len(ids) == len(set(ids))  # Check that all IDs are unique
    
    def test_task_post_init_defaults(self):
        """Test that Task's __post_init__ sets defaults correctly"""
        task = Task(id=1, title="Test task")
        
        # Check that defaults were set
        assert task.description == ""
        assert task.completed is False
        assert task.priority == "Medium"
        assert task.tags == []
        assert task.due_date is None
        assert task.recurrence == "none"
        assert task.created_at is not None
        assert task.updated_at is not None
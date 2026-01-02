import pytest
from datetime import datetime
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestSecurityAndInputValidation:
    """
    Tests for security hardening and input validation
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_task_title_validation(self):
        """Test that task titles are properly validated"""
        # Test empty title
        with pytest.raises(ValueError, match="Title must not be empty"):
            self.service.add_task(title="")
        
        # Test valid title
        task = self.service.add_task(title="Valid task")
        assert task.title == "Valid task"
    
    def test_task_priority_validation(self):
        """Test that task priorities are properly validated"""
        # Test invalid priority
        with pytest.raises(ValueError, match="Priority must be one of"):
            self.service.add_task(title="Test task", priority="InvalidPriority")
        
        # Test valid priorities
        high_task = self.service.add_task(title="High priority", priority="High")
        medium_task = self.service.add_task(title="Medium priority", priority="Medium")
        low_task = self.service.add_task(title="Low priority", priority="Low")
        
        assert high_task.priority == "High"
        assert medium_task.priority == "Medium"
        assert low_task.priority == "Low"
    
    def test_task_recurrence_validation(self):
        """Test that task recurrence values are properly validated"""
        # Test invalid recurrence
        with pytest.raises(ValueError, match="Recurrence must be one of"):
            self.service.add_task(title="Test task", recurrence="invalid")
        
        # Test valid recurrences
        none_task = self.service.add_task(title="No recurrence", recurrence="none")
        daily_task = self.service.add_task(title="Daily recurrence", recurrence="daily", due_date=datetime.now())
        weekly_task = self.service.add_task(title="Weekly recurrence", recurrence="weekly", due_date=datetime.now())
        monthly_task = self.service.add_task(title="Monthly recurrence", recurrence="monthly", due_date=datetime.now())
        
        assert none_task.recurrence == "none"
        assert daily_task.recurrence == "daily"
        assert weekly_task.recurrence == "weekly"
        assert monthly_task.recurrence == "monthly"
    
    def test_recurring_task_must_have_due_date(self):
        """Test that recurring tasks must have a due date"""
        # Test that creating a recurring task without a due date raises an error
        with pytest.raises(ValueError, match="Recurring tasks must have a due date"):
            self.service.add_task(title="Recurring task without due date", recurrence="daily")
    
    def test_task_update_validation(self):
        """Test that task updates are properly validated"""
        task = self.service.add_task(title="Original task", priority="Medium")
        
        # Test updating with invalid priority
        result = self.service.update_task(task.id, priority="InvalidPriority")
        # The update should fail and return None, keeping the original priority
        assert result is None
        # Get the task again to verify it wasn't changed
        updated_task = self.service.get_task_by_id(task.id)
        assert updated_task.priority == "Medium"
    
    def test_task_tags_validation(self):
        """Test that task tags are properly validated"""
        # Test that tags must be a list
        with pytest.raises(ValueError, match="Tags must be a list of strings"):
            task = Task(
                id=1,
                title="Test task",
                tags="not a list"  # This should cause validation to fail
            )
            task.validate()
        
        # Test that tags must be a list of strings
        with pytest.raises(ValueError, match="Tags must be a list of strings"):
            task = Task(
                id=1,
                title="Test task",
                tags=[1, 2, 3]  # This should cause validation to fail
            )
            task.validate()
        
        # Test valid tags
        task = self.service.add_task(title="Task with tags", tags=["tag1", "tag2"])
        assert task.tags == ["tag1", "tag2"]
import pytest
from datetime import datetime, timedelta
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestRecurringTasks:
    """
    Acceptance tests for recurring task scenarios
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_create_daily_recurring_task(self):
        """Test creating a daily recurring task"""
        task = self.service.add_task(
            title="Daily workout",
            description="Exercise for 30 minutes",
            due_date=datetime.now() + timedelta(days=1),
            recurrence="daily"
        )
        
        assert task.title == "Daily workout"
        assert task.recurrence == "daily"
        assert task.due_date is not None
    
    def test_create_weekly_recurring_task(self):
        """Test creating a weekly recurring task"""
        task = self.service.add_task(
            title="Weekly team meeting",
            description="Team sync meeting",
            due_date=datetime.now() + timedelta(days=7),
            recurrence="weekly"
        )
        
        assert task.title == "Weekly team meeting"
        assert task.recurrence == "weekly"
        assert task.due_date is not None
    
    def test_create_monthly_recurring_task(self):
        """Test creating a monthly recurring task"""
        task = self.service.add_task(
            title="Monthly report",
            description="Submit monthly status report",
            due_date=datetime.now() + timedelta(days=30),
            recurrence="monthly"
        )
        
        assert task.title == "Monthly report"
        assert task.recurrence == "monthly"
        assert task.due_date is not None
    
    def test_complete_recurring_task_creates_new_instance_daily(self):
        """Test that completing a daily recurring task creates a new instance with next due date"""
        original_due_date = datetime.now() + timedelta(days=1)
        task = self.service.add_task(
            title="Daily habit",
            due_date=original_due_date,
            recurrence="daily"
        )
        
        # Complete the task
        new_task = self.service.complete_task(task.id)
        
        # Verify the original task is marked as complete
        assert task.completed is True
        
        # Verify a new task was created
        assert new_task is not None
        assert new_task.title == "Daily habit"
        assert new_task.recurrence == "daily"
        assert new_task.due_date == original_due_date + timedelta(days=1)
        assert new_task.completed is False
    
    def test_complete_recurring_task_creates_new_instance_weekly(self):
        """Test that completing a weekly recurring task creates a new instance with next due date"""
        original_due_date = datetime.now() + timedelta(days=7)
        task = self.service.add_task(
            title="Weekly meeting",
            due_date=original_due_date,
            recurrence="weekly"
        )
        
        # Complete the task
        new_task = self.service.complete_task(task.id)
        
        # Verify the original task is marked as complete
        assert task.completed is True
        
        # Verify a new task was created
        assert new_task is not None
        assert new_task.title == "Weekly meeting"
        assert new_task.recurrence == "weekly"
        assert new_task.due_date == original_due_date + timedelta(weeks=1)
        assert new_task.completed is False
    
    def test_complete_recurring_task_creates_new_instance_monthly(self):
        """Test that completing a monthly recurring task creates a new instance with next due date"""
        original_due_date = datetime.now() + timedelta(days=30)
        task = self.service.add_task(
            title="Monthly review",
            due_date=original_due_date,
            recurrence="monthly"
        )
        
        # Complete the task
        new_task = self.service.complete_task(task.id)
        
        # Verify the original task is marked as complete
        assert task.completed is True
        
        # Verify a new task was created
        assert new_task is not None
        assert new_task.title == "Monthly review"
        assert new_task.recurrence == "monthly"
        assert new_task.due_date == original_due_date + timedelta(days=30)
        assert new_task.completed is False
    
    def test_complete_non_recurring_task_does_not_create_new_instance(self):
        """Test that completing a non-recurring task does not create a new instance"""
        task = self.service.add_task(
            title="One-time task",
            due_date=datetime.now() + timedelta(days=1),
            recurrence="none"
        )
        
        # Complete the task
        result_task = self.service.complete_task(task.id)
        
        # Verify the task is marked as complete but no new task is created
        assert task.completed is True
        assert result_task == task  # The same task is returned, not a new one
        assert len(self.service.get_all_tasks()) == 1  # Only the original task exists
    
    def test_recurring_task_must_have_due_date(self):
        """Test that creating a recurring task without a due date raises an error"""
        with pytest.raises(ValueError, match="Recurring tasks must have a due date"):
            self.service.add_task(
                title="Recurring task without due date",
                recurrence="daily"
            )
    
    def test_recurring_task_indicator_in_list(self):
        """Test that recurring tasks show the recurring indicator in the list"""
        # Add a recurring task
        recurring_task = self.service.add_task(
            title="Recurring task",
            recurrence="weekly"
        )
        
        # Add a non-recurring task
        non_recurring_task = self.service.add_task(
            title="Non-recurring task",
            recurrence="none"
        )
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify both tasks exist
        assert len(sorted_tasks) == 2
import pytest
from datetime import datetime, timedelta
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestReminderScenarios:
    """
    Acceptance tests for reminder scenarios
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_overdue_task_reminder(self):
        """Test that overdue tasks are included in reminders"""
        # Create an overdue task
        past_date = datetime.now() - timedelta(days=2)
        overdue_task = self.service.add_task(
            title="Overdue task",
            due_date=past_date
        )
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify the overdue task is in the overdue reminders
        assert len(reminders["overdue"]) == 1
        assert reminders["overdue"][0].id == overdue_task.id
        assert len(reminders["due_today"]) == 0
        assert len(reminders["upcoming"]) == 0
    
    def test_due_today_task_reminder(self):
        """Test that tasks due today are included in reminders"""
        # Create a task due today
        today_date = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        today_task = self.service.add_task(
            title="Due today task",
            due_date=today_date
        )
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify the due today task is in the due today reminders
        assert len(reminders["due_today"]) == 1
        assert reminders["due_today"][0].id == today_task.id
        assert len(reminders["overdue"]) == 0
        assert len(reminders["upcoming"]) == 0
    
    def test_upcoming_task_reminder(self):
        """Test that upcoming tasks are included in reminders"""
        # Create a task due in 2 days
        future_date = datetime.now() + timedelta(days=2)
        upcoming_task = self.service.add_task(
            title="Upcoming task",
            due_date=future_date
        )
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify the upcoming task is in the upcoming reminders
        assert len(reminders["upcoming"]) == 1
        assert reminders["upcoming"][0].id == upcoming_task.id
        assert len(reminders["overdue"]) == 0
        assert len(reminders["due_today"]) == 0
    
    def test_mixed_reminder_types(self):
        """Test that all reminder types appear together"""
        # Create tasks for each reminder type
        past_date = datetime.now() - timedelta(days=1)
        today_date = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        future_date = datetime.now() + timedelta(days=2)
        
        overdue_task = self.service.add_task(title="Overdue task", due_date=past_date)
        today_task = self.service.add_task(title="Due today task", due_date=today_date)
        upcoming_task = self.service.add_task(title="Upcoming task", due_date=future_date)
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify all reminder types have the correct tasks
        assert len(reminders["overdue"]) == 1
        assert reminders["overdue"][0].id == overdue_task.id
        
        assert len(reminders["due_today"]) == 1
        assert reminders["due_today"][0].id == today_task.id
        
        assert len(reminders["upcoming"]) == 1
        assert reminders["upcoming"][0].id == upcoming_task.id
    
    def test_completed_tasks_not_in_reminders(self):
        """Test that completed tasks are not included in reminders"""
        # Create and complete an overdue task
        past_date = datetime.now() - timedelta(days=2)
        task = self.service.add_task(title="Completed task", due_date=past_date)
        self.service.complete_task(task.id)
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify the completed task is not in any reminders
        assert len(reminders["overdue"]) == 0
        assert len(reminders["due_today"]) == 0
        assert len(reminders["upcoming"]) == 0
    
    def test_task_without_due_date_not_in_reminders(self):
        """Test that tasks without due dates are not included in reminders"""
        # Create a task without a due date
        no_due_task = self.service.add_task(title="No due date task")
        
        # Get reminders
        reminders = self.service.get_reminders()
        
        # Verify the task without due date is not in any reminders
        assert len(reminders["overdue"]) == 0
        assert len(reminders["due_today"]) == 0
        assert len(reminders["upcoming"]) == 0
    
    def test_create_reminder_object(self):
        """Test creating a Reminder object"""
        future_date = datetime.now() + timedelta(days=2)
        task = self.service.add_task(title="Test task", due_date=future_date)
        
        # Create a reminder
        reminder = self.service.create_reminder(task, "upcoming")
        
        # Verify the reminder properties
        assert reminder.task.id == task.id
        assert reminder.reminder_type == "upcoming"
        assert reminder.time_until_due is not None
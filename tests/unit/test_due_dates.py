import pytest
from datetime import datetime, timedelta
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestDueDateScenarios:
    """
    Acceptance tests for due date scenarios
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_add_task_with_due_date(self):
        """Test adding a task with a due date"""
        future_date = datetime.now() + timedelta(days=5)
        task = self.service.add_task(
            title="Task with due date",
            due_date=future_date
        )
        
        assert task.title == "Task with due date"
        assert task.due_date == future_date
    
    def test_add_task_without_due_date(self):
        """Test adding a task without a due date"""
        task = self.service.add_task(
            title="Task without due date"
        )
        
        assert task.title == "Task without due date"
        assert task.due_date is None
    
    def test_task_sorting_by_due_date(self):
        """Test that tasks are sorted by due date (soonest first)"""
        # Add tasks with different due dates
        far_future_date = datetime.now() + timedelta(days=30)
        near_future_date = datetime.now() + timedelta(days=5)
        today_date = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        
        task3 = self.service.add_task(title="Far future task", due_date=far_future_date)
        task1 = self.service.add_task(title="Today task", due_date=today_date)
        task2 = self.service.add_task(title="Near future task", due_date=near_future_date)
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify the order: today, near future, far future
        assert sorted_tasks[0].id == task1.id  # Today's task first
        assert sorted_tasks[1].id == task2.id  # Near future task second
        assert sorted_tasks[2].id == task3.id  # Far future task third
    
    def test_task_sorting_with_mixed_due_dates(self):
        """Test that tasks without due dates come after tasks with due dates"""
        future_date = datetime.now() + timedelta(days=5)
        
        task_with_date = self.service.add_task(title="Task with due date", due_date=future_date)
        task_without_date = self.service.add_task(title="Task without due date")
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify the order: task with due date first, task without due date second
        assert sorted_tasks[0].id == task_with_date.id
        assert sorted_tasks[1].id == task_without_date.id
    
    def test_overdue_task_detection(self):
        """Test that overdue tasks are properly identified"""
        past_date = datetime.now() - timedelta(days=2)
        future_date = datetime.now() + timedelta(days=2)
        
        overdue_task = self.service.add_task(title="Overdue task", due_date=past_date)
        future_task = self.service.add_task(title="Future task", due_date=future_date)
        
        # Get overdue tasks
        overdue_tasks = self.service.get_overdue_tasks()
        
        # Verify only the overdue task is detected
        assert len(overdue_tasks) == 1
        assert overdue_tasks[0].id == overdue_task.id
    
    def test_due_today_task_detection(self):
        """Test that tasks due today are properly identified"""
        today_date = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        yesterday_date = datetime.now() - timedelta(days=1)
        tomorrow_date = datetime.now() + timedelta(days=1)
        
        today_task = self.service.add_task(title="Today task", due_date=today_date)
        yesterday_task = self.service.add_task(title="Yesterday task", due_date=yesterday_date)
        tomorrow_task = self.service.add_task(title="Tomorrow task", due_date=tomorrow_date)
        
        # Get tasks due today
        due_today_tasks = self.service.get_due_today_tasks()
        
        # Verify only the today task is detected
        assert len(due_today_tasks) == 1
        assert due_today_tasks[0].id == today_task.id
    
    def test_upcoming_task_detection(self):
        """Test that upcoming tasks are properly identified"""
        today = datetime.now()
        in_2_days = today + timedelta(days=2)
        in_4_days = today + timedelta(days=4)  # Beyond the default 3-day window
        
        upcoming_task = self.service.add_task(title="Upcoming task", due_date=in_2_days)
        future_task = self.service.add_task(title="Future task", due_date=in_4_days)
        
        # Get upcoming tasks (default is 3 days)
        upcoming_tasks = self.service.get_upcoming_tasks()
        
        # Verify only the task within 3 days is detected
        assert len(upcoming_tasks) == 1
        assert upcoming_tasks[0].id == upcoming_task.id
    
    def test_completed_tasks_not_shown_as_overdue(self):
        """Test that completed tasks are not shown as overdue"""
        past_date = datetime.now() - timedelta(days=2)
        
        # Add and complete an overdue task
        task = self.service.add_task(title="Completed overdue task", due_date=past_date)
        self.service.complete_task(task.id)
        
        # Get overdue tasks
        overdue_tasks = self.service.get_overdue_tasks()
        
        # Verify the completed task is not in the overdue list
        assert len(overdue_tasks) == 0
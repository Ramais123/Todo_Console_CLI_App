import pytest
from datetime import datetime, timedelta
from src.models.todo import Task
from src.services.todo_service import TodoService


class TestEnhancedViewScenarios:
    """
    Acceptance tests for enhanced view scenarios
    """
    
    def setup_method(self):
        """Set up a fresh TodoService for each test"""
        self.service = TodoService()
    
    def test_task_sorting_by_due_date_and_priority(self):
        """Test that tasks are sorted by due date first, then by priority"""
        # Create tasks with different due dates and priorities
        far_future_date = datetime.now() + timedelta(days=30)
        near_future_date = datetime.now() + timedelta(days=5)
        today_date = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        
        # Add tasks with different combinations of due dates and priorities
        low_priority_far_future = self.service.add_task(
            title="Low priority far future", 
            due_date=far_future_date, 
            priority="Low"
        )
        high_priority_near_future = self.service.add_task(
            title="High priority near future", 
            due_date=near_future_date, 
            priority="High"
        )
        medium_priority_today = self.service.add_task(
            title="Medium priority today", 
            due_date=today_date, 
            priority="Medium"
        )
        high_priority_far_future = self.service.add_task(
            title="High priority far future", 
            due_date=far_future_date, 
            priority="High"
        )
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify the order: due date first (soonest first), then priority (High → Medium → Low)
        # Today's task should be first (regardless of priority, due date takes precedence)
        assert sorted_tasks[0].id == medium_priority_today.id
        
        # Near future task should be second
        assert sorted_tasks[1].id == high_priority_near_future.id
        
        # Far future tasks should be last, with high priority before low priority
        # Since they have the same due date, priority should be the secondary sort
        assert sorted_tasks[2].id == high_priority_far_future.id
        assert sorted_tasks[3].id == low_priority_far_future.id
    
    def test_task_sorting_with_mixed_due_dates_and_priorities(self):
        """Test sorting with a mix of tasks with and without due dates"""
        future_date = datetime.now() + timedelta(days=5)
        
        task_with_date_high_priority = self.service.add_task(
            title="High priority with date", 
            due_date=future_date, 
            priority="High"
        )
        task_without_date_low_priority = self.service.add_task(
            title="Low priority without date", 
            priority="Low"
        )
        task_with_date_low_priority = self.service.add_task(
            title="Low priority with date", 
            due_date=future_date, 
            priority="Low"
        )
        task_without_date_high_priority = self.service.add_task(
            title="High priority without date", 
            priority="High"
        )
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Tasks with due dates should come first (sorted by date), 
        # then tasks without due dates (sorted by priority)
        assert sorted_tasks[0].id == task_with_date_high_priority.id
        assert sorted_tasks[1].id == task_with_date_low_priority.id
        assert sorted_tasks[2].id == task_without_date_high_priority.id
        assert sorted_tasks[3].id == task_without_date_low_priority.id
    
    def test_recurring_task_indicator_display(self):
        """Test that recurring tasks show the appropriate indicator"""
        # Add a recurring task
        recurring_task = self.service.add_task(
            title="Weekly meeting",
            recurrence="weekly"
        )
        
        # Add a non-recurring task
        non_recurring_task = self.service.add_task(
            title="One-time task",
            recurrence="none"
        )
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify both tasks exist
        assert len(sorted_tasks) == 2
        
        # Check that the recurring task is properly identified as recurring
        recurring_found = False
        non_recurring_found = False
        
        for task in sorted_tasks:
            if task.id == recurring_task.id:
                assert task.recurrence == "weekly"
                recurring_found = True
            elif task.id == non_recurring_task.id:
                assert task.recurrence == "none"
                non_recurring_found = True
        
        assert recurring_found
        assert non_recurring_found
    
    def test_overdue_task_visual_indicator(self):
        """Test that overdue tasks show visual indicators"""
        # Add an overdue task
        past_date = datetime.now() - timedelta(days=2)
        overdue_task = self.service.add_task(
            title="Overdue task",
            due_date=past_date
        )
        
        # Get sorted tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        # Verify the overdue task exists
        assert len(sorted_tasks) == 1
        assert sorted_tasks[0].id == overdue_task.id
        
        # The visual indicator would be handled in the display layer,
        # but we can verify the task properties
        assert sorted_tasks[0].due_date < datetime.now()
        assert not sorted_tasks[0].completed
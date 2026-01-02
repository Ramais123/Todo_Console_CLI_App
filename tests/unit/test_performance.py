import time
import pytest
from datetime import datetime, timedelta
from src.services.todo_service import TodoService


class TestPerformance:
    """
    Performance tests for task sorting and filtering
    """
    
    def setup_method(self):
        """Set up a TodoService with many tasks for performance testing"""
        self.service = TodoService()
        
        # Add many tasks to test performance
        for i in range(1000):
            due_date = datetime.now() + timedelta(days=i % 30)  # Cycle through 30 days
            self.service.add_task(
                title=f"Task {i}",
                description=f"Description for task {i}",
                priority="Medium" if i % 3 else "High",  # Every 3rd task is high priority
                due_date=due_date if i % 4 != 0 else None,  # Every 4th task has no due date
                recurrence="none"
            )
    
    def test_task_sorting_performance(self):
        """Test that task sorting performs well with many tasks"""
        start_time = time.time()
        
        # Sort the tasks
        sorted_tasks = self.service.get_sorted_tasks()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Verify that sorting completed in a reasonable time (less than 1 second)
        assert duration < 1.0, f"Task sorting took too long: {duration:.4f} seconds"
        
        # Verify that all tasks were returned
        assert len(sorted_tasks) == 1000
    
    def test_get_overdue_tasks_performance(self):
        """Test that getting overdue tasks performs well"""
        start_time = time.time()
        
        # Get overdue tasks (there shouldn't be any since all due dates are in the future)
        overdue_tasks = self.service.get_overdue_tasks()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Verify that the operation completed in a reasonable time
        assert duration < 0.5, f"Getting overdue tasks took too long: {duration:.4f} seconds"
        
        # Verify that no tasks were returned (since all due dates are in the future)
        assert len(overdue_tasks) == 0
    
    def test_get_due_today_tasks_performance(self):
        """Test that getting tasks due today performs well"""
        start_time = time.time()
        
        # Get tasks due today
        due_today_tasks = self.service.get_due_today_tasks()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Verify that the operation completed in a reasonable time
        assert duration < 0.5, f"Getting tasks due today took too long: {duration:.4f} seconds"
    
    def test_get_upcoming_tasks_performance(self):
        """Test that getting upcoming tasks performs well"""
        start_time = time.time()
        
        # Get upcoming tasks
        upcoming_tasks = self.service.get_upcoming_tasks()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Verify that the operation completed in a reasonable time
        assert duration < 0.5, f"Getting upcoming tasks took too long: {duration:.4f} seconds"
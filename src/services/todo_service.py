from datetime import datetime, timedelta
from typing import List, Optional

# Import with relative path
import sys
import os
# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.todo import Task, Reminder
from lib.date_utils import calculate_next_due_date


class TodoService:
    """
    Business logic layer for todo operations
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def get_next_id(self) -> int:
        """Get the next available ID for a task"""
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def add_task(
        self,
        title: str,
        description: str = "",
        completed: bool = False,
        priority: str = "Medium",
        tags: List[str] = None,
        due_date: Optional[datetime] = None,
        recurrence: str = "none"
    ) -> Task:
        """
        Add a new task with the specified properties
        """
        task = Task(
            id=self.get_next_id(),
            title=title,
            description=description,
            completed=completed,
            priority=priority,
            tags=tags or [],
            due_date=due_date,
            recurrence=recurrence
        )

        # Validate the task before adding
        task.validate()

        self.tasks.append(task)
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks
        """
        return self.tasks.copy()

    def get_sorted_tasks(self) -> List[Task]:
        """
        Get all tasks sorted by due date (soonest first), then by priority (High → Medium → Low)
        """
        def sort_key(task):
            # Tasks without due dates come last
            due_order = task.due_date if task.due_date else datetime.max
            priority_order = {"High": 1, "Medium": 2, "Low": 3}[task.priority]
            return (due_order, priority_order)

        return sorted(self.tasks, key=sort_key)

    def update_task(
        self,
        task_id: int,
        title: str = None,
        description: str = None,
        completed: bool = None,
        priority: str = None,
        tags: List[str] = None,
        due_date: Optional[datetime] = None,
        recurrence: str = None
    ) -> Optional[Task]:
        """
        Update an existing task with the specified properties
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Update fields if provided
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        if priority is not None and priority in ["High", "Medium", "Low"]:
            task.priority = priority
        if tags is not None:
            task.tags = tags
        if due_date is not None:
            task.due_date = due_date
        if recurrence is not None and recurrence in ["none", "daily", "weekly", "monthly"]:
            task.recurrence = recurrence

        # Update the updated_at timestamp
        task.updated_at = datetime.now()

        # Re-validate the task after updates
        task.validate()

        return task

    def complete_task(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete
        For recurring tasks, create a new instance with the next due date
        """
        task = self.get_task_by_id(task_id)
        if not task or task.completed:
            return task

        # Mark the original task as completed
        task.completed = True
        task.updated_at = datetime.now()

        # Handle recurring tasks
        if task.recurrence != "none" and task.due_date:
            # Create new instance with next due date
            next_due_date = calculate_next_due_date(task.due_date, task.recurrence)
            new_task = Task(
                id=self.get_next_id(),
                title=task.title,
                description=task.description,
                priority=task.priority,
                tags=task.tags,
                due_date=next_due_date,
                recurrence=task.recurrence
            )
            self.tasks.append(new_task)
            return new_task  # Return the new task that was created

        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        """
        Delete a task by its ID
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return task
        return None

    def get_overdue_tasks(self, current_time: datetime = None) -> List[Task]:
        """
        Get all overdue tasks
        """
        if current_time is None:
            current_time = datetime.now()

        from src.lib.date_utils import is_overdue

        overdue_tasks = []
        for task in self.tasks:
            if not task.completed and task.due_date and is_overdue(task.due_date, current_time):
                overdue_tasks.append(task)

        return overdue_tasks

    def get_due_today_tasks(self, current_time: datetime = None) -> List[Task]:
        """
        Get all tasks due today
        """
        if current_time is None:
            current_time = datetime.now()

        from src.lib.date_utils import is_due_today

        due_today_tasks = []
        for task in self.tasks:
            if not task.completed and task.due_date and is_due_today(task.due_date, current_time):
                due_today_tasks.append(task)

        return due_today_tasks

    def get_upcoming_tasks(self, days: int = 3, current_time: datetime = None) -> List[Task]:
        """
        Get all tasks due in the next specified number of days
        """
        if current_time is None:
            current_time = datetime.now()

        from src.lib.date_utils import is_upcoming

        upcoming_tasks = []
        for task in self.tasks:
            if not task.completed and task.due_date and is_upcoming(task.due_date, current_time, days):
                upcoming_tasks.append(task)

        return upcoming_tasks

    def get_reminders(self, current_time: datetime = None) -> dict:
        """
        Get all reminders grouped by type: overdue, due today, upcoming
        """
        if current_time is None:
            current_time = datetime.now()

        from src.lib.date_utils import is_overdue, is_due_today, is_upcoming

        reminders = {
            "overdue": [],
            "due_today": [],
            "upcoming": []
        }

        for task in self.tasks:
            if not task.completed and task.due_date:
                if is_overdue(task.due_date, current_time):
                    reminders["overdue"].append(task)
                elif is_due_today(task.due_date, current_time):
                    reminders["due_today"].append(task)
                elif is_upcoming(task.due_date, current_time):
                    reminders["upcoming"].append(task)

        return reminders

    def create_reminder(self, task: Task, reminder_type: str, current_time: datetime = None) -> Reminder:
        """
        Create a Reminder object for a task
        """
        if current_time is None:
            current_time = datetime.now()

        time_until_due = None
        if task.due_date:
            time_until_due = task.due_date - current_time

        reminder = Reminder(
            task=task,
            reminder_type=reminder_type,
            time_until_due=time_until_due
        )

        # Validate the reminder
        reminder.validate()

        return reminder
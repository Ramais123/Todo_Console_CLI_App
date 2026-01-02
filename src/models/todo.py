from datetime import datetime, timedelta
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Task:
    """
    Represents a single task with properties including ID, title, description,
    completion status, due date, priority, recurring interval, created_at, and updated_at
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "Medium"  # "High", "Medium", "Low"
    tags: List[str] = None
    due_date: Optional[datetime] = None  # Optional due date/time for the task
    recurrence: str = "none"  # "none", "daily", "weekly", "monthly"
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def validate(self):
        """
        Validates the task properties according to the business rules
        """
        if not self.title:
            raise ValueError("Title must not be empty")

        if self.priority not in ["High", "Medium", "Low"]:
            raise ValueError(f"Priority must be one of 'High', 'Medium', or 'Low', got '{self.priority}'")

        if not isinstance(self.tags, list) or not all(isinstance(tag, str) for tag in self.tags):
            raise ValueError("Tags must be a list of strings")

        if self.due_date is not None and not isinstance(self.due_date, datetime):
            raise ValueError("Due date must be a valid datetime if provided")

        if self.recurrence not in ["none", "daily", "weekly", "monthly"]:
            raise ValueError(f"Recurrence must be one of 'none', 'daily', 'weekly', or 'monthly', got '{self.recurrence}'")

        # Additional validation: if recurrence is not none, due_date must be provided
        if self.recurrence != "none" and self.due_date is None:
            raise ValueError("Recurring tasks must have a due date")


@dataclass
class Reminder:
    """
    Represents a reminder for a task that needs to be highlighted
    """
    task: Task
    reminder_type: str  # "overdue", "due_today", "upcoming"
    time_until_due: Optional[timedelta] = None  # Time difference from current time to due date

    def validate(self):
        """
        Validates the reminder properties according to the business rules
        """
        if self.reminder_type not in ["overdue", "due_today", "upcoming"]:
            raise ValueError(f"Reminder type must be one of 'overdue', 'due_today', or 'upcoming', got '{self.reminder_type}'")

        if not isinstance(self.task, Task):
            raise ValueError("Task must be a valid Task entity")
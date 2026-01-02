"""
Todo application module containing Task dataclass and TodoManager class.
Full support: Basic + Intermediate + Advanced features (Due Dates, Recurring Tasks, Reminders)
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo task with all advanced fields.
    """
    id: int
    title: str
    description: str
    completed: bool = False
    priority: str = "Medium"
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None          # New: Due date/time
    recurrence: str = "none"                     # New: none/daily/weekly/monthly

    def __post_init__(self):
        self.priority = self.priority.lower()
        self.recurrence = self.recurrence.lower()
        if self.tags is None:
            self.tags = []


class TodoManager:
    """
    Manages a collection of tasks in memory with full advanced functionality.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = "Medium",
        tags: List[str] = None,
        due_date: Optional[datetime] = None,
        recurrence: str = "none"
    ) -> Task:
        """
        Add a new task with full advanced options.
        """
        if tags is None:
            tags = []

        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence=recurrence
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> List[Task]:
        """
        Return tasks sorted by due_date (soonest first), then priority.
        """
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(
            self.tasks,
            key=lambda t: (
                t.due_date if t.due_date else datetime.max,
                priority_order.get(t.priority, 3),
                t.id
            )
        )

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[str] = None,
        tags: Optional[List[str]] = None,
        due_date: Optional[datetime] = None,
        recurrence: Optional[str] = None
    ) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if priority is not None:
            task.priority = priority.lower()
        if tags is not None:
            task.tags = tags
        if due_date is not None:
            task.due_date = due_date
        if recurrence is not None:
            task.recurrence = recurrence.lower()

        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int):
        """
        Mark task complete. If recurring and has due_date, create next instance.
        Returns: True (normal complete), or new Task object (recurring instance created), or False (not found)
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.completed = True

        if task.recurrence != "none" and task.due_date:
            # Calculate next due date
            next_due = task.due_date
            if task.recurrence == "daily":
                next_due += timedelta(days=1)
            elif task.recurrence == "weekly":
                next_due += timedelta(days=7)
            elif task.recurrence == "monthly":
                # Approximate: add ~30 days
                try:
                    next_due = next_due.replace(month=next_due.month % 12 + 1)
                    if next_due.month == 1:
                        next_due = next_due.replace(year=next_due.year + 1)
                except ValueError:
                    next_due += timedelta(days=30)

            # Create new recurring instance
            new_task = self.add_task(
                title=task.title,
                description=task.description,
                priority=task.priority,
                tags=task.tags.copy(),
                due_date=next_due,
                recurrence=task.recurrence
            )
            return new_task

        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Task]:
        keyword = keyword.lower()
        return [
            t for t in self.tasks
            if keyword in t.title.lower() or keyword in t.description.lower()
        ]

    def filter_tasks(self, filter_type: str, filter_value: str) -> List[Task]:
        filtered = []
        for task in self.tasks:
            if filter_type.lower() == "status":
                if (filter_value.lower() == "completed" and task.completed) or \
                   (filter_value.lower() == "incomplete" and not task.completed):
                    filtered.append(task)
            elif filter_type.lower() == "priority":
                if task.priority == filter_value.lower():
                    filtered.append(task)
            elif filter_type.lower() == "tag":
                if filter_value.lower() in [tag.lower() for tag in task.tags]:
                    filtered.append(task)
        return filtered

    def sort_tasks(self, sort_type: str) -> List[Task]:
        priority_order = {"high": 0, "medium": 1, "low": 2}
        if sort_type.lower() == "priority":
            return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 3))
        elif sort_type.lower() == "title":
            return sorted(self.tasks, key=lambda t: t.title.lower())
        elif sort_type.lower() == "status":
            return sorted(self.tasks, key=lambda t: (t.completed, t.id))
        return self.tasks.copy()

    def get_reminders(self) -> List[str]:
        """
        Generate smart reminder messages for overdue, today, and upcoming tasks.
        """
        now = datetime.now()
        reminders = []

        overdue = [t for t in self.tasks if not t.completed and t.due_date and t.due_date < now]
        today = [t for t in self.tasks if not t.completed and t.due_date and t.due_date.date() == now.date()]
        upcoming = [t for t in self.tasks if not t.completed and t.due_date and now < t.due_date <= now + timedelta(days=3)]

        if overdue:
            reminders.append("🔥 OVERDUE TASKS 🔥")
            for t in overdue:
                due_str = t.due_date.strftime("%Y-%m-%d %H:%M") if t.due_date else ""
                reminders.append(f"   #{t.id} {t.title} (Due: {due_str})")

        if today:
            reminders.append("⏰ DUE TODAY ⏰")
            for t in today:
                reminders.append(f"   #{t.id} {t.title}")

        if upcoming:
            reminders.append(" Upcoming (next 3 days)")
            for t in upcoming:
                reminders.append(f"   #{t.id} {t.title} (Due: {t.due_date.strftime('%Y-%m-%d')})")

        return reminders if reminders else ["No reminders — you're all caught up! "]
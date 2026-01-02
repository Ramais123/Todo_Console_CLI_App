"""
Todo application module containing Task dataclass and TodoManager class.
Implements all required functionality for managing tasks in memory.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, completion status, and creation timestamp.
    """
    id: int
    title: str
    description: str
    completed: bool = False
    priority: str = "Medium"  # Added priority field with default "Medium"
    tags: List[str] = None  # Added tags field
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.tags is None:
            self.tags = []

    def __str__(self) -> str:
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id} - {self.title} - {self.description[:50]}{'...' if len(self.description) > 50 else ''}"


class TodoManager:
    """
    Manages a collection of tasks in memory with CRUD operations.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str, priority: str = "Medium", tags: List[str] = None) -> Task:
        """
        Add a new task with the given title, description, priority, and tags.

        Args:
            title: The task title
            description: The task description
            priority: The task priority (default: "Medium")
            tags: List of tags for the task (default: empty list)

        Returns:
            The created Task object
        """
        if tags is None:
            tags = []
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all tasks
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None, priority: str = None, tags: List[str] = None) -> bool:
        """
        Update a task's title, description, priority, and/or tags.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)
            tags: New list of tags (optional)

        Returns:
            True if task was updated, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            if tags is not None:
                task.tags = tags
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark complete
            
        Returns:
            True if task was marked complete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description (case-insensitive).

        Args:
            keyword: The keyword to search for

        Returns:
            List of matching Task objects
        """
        keyword = keyword.lower()
        matching_tasks = []
        for task in self.tasks:
            if keyword in task.title.lower() or keyword in task.description.lower():
                matching_tasks.append(task)
        return matching_tasks

    def filter_tasks(self, filter_type: str, filter_value: str) -> List[Task]:
        """
        Filter tasks by specified criteria.

        Args:
            filter_type: Type of filter ("status", "priority", "tag")
            filter_value: Value to filter by

        Returns:
            List of matching Task objects
        """
        filtered_tasks = []
        for task in self.tasks:
            if filter_type.lower() == "status":
                if filter_value.lower() == "completed" and task.completed:
                    filtered_tasks.append(task)
                elif filter_value.lower() == "incomplete" and not task.completed:
                    filtered_tasks.append(task)
            elif filter_type.lower() == "priority":
                if task.priority.lower() == filter_value.lower():
                    filtered_tasks.append(task)
            elif filter_type.lower() == "tag":
                if filter_value.lower() in [tag.lower() for tag in task.tags]:
                    filtered_tasks.append(task)
        return filtered_tasks

    def sort_tasks(self, sort_type: str) -> List[Task]:
        """
        Sort tasks by specified criteria.

        Args:
            sort_type: Type of sort ("priority", "title", "status")

        Returns:
            List of sorted Task objects
        """
        if sort_type.lower() == "priority":
            # Sort by priority: High -> Medium -> Low
            priority_order = {"high": 1, "medium": 2, "low": 3}
            return sorted(self.tasks, key=lambda task: priority_order.get(task.priority.lower(), 4))
        elif sort_type.lower() == "title":
            # Sort alphabetically by title
            return sorted(self.tasks, key=lambda task: task.title.lower())
        elif sort_type.lower() == "status":
            # Sort by status: Incomplete first
            return sorted(self.tasks, key=lambda task: task.completed)
        else:
            # Return unsorted if invalid sort type
            return self.tasks
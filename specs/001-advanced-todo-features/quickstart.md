# Quickstart Guide: Advanced Todo Features

## Overview
This guide explains how to implement and use the advanced features: recurring tasks and due date reminders.

## Prerequisites
- Python 3.13+
- UV package manager (optional, for dependency management)
- Basic knowledge of the existing CLI todo app

## Implementation Steps

### 1. Enhance the Task Model
Update the Task class to include due_date and recurrence properties:

```python
from datetime import datetime
from typing import Optional, List

class Task:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False, 
                 priority: str = "Medium", tags: List[str] = None, due_date: Optional[datetime] = None,
                 recurrence: str = "none"):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority
        self.tags = tags or []
        self.due_date = due_date
        self.recurrence = recurrence  # "none", "daily", "weekly", "monthly"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
```

### 2. Implement Date Utilities
Create a date utility module for handling recurrence calculations:

```python
from datetime import datetime, timedelta

def calculate_next_due_date(last_due_date: datetime, recurrence: str) -> datetime:
    if recurrence == "daily":
        return last_due_date + timedelta(days=1)
    elif recurrence == "weekly":
        return last_due_date + timedelta(weeks=1)
    elif recurrence == "monthly":
        # Simple approach: add ~30 days
        # For more accurate month handling, consider edge cases like Jan 31 -> Feb
        return last_due_date + timedelta(days=30)
    else:
        raise ValueError(f"Invalid recurrence type: {recurrence}")

def is_overdue(task_due_date: datetime, current_time: datetime) -> bool:
    return task_due_date < current_time and task_due_date.date() < current_time.date()

def is_due_today(task_due_date: datetime, current_time: datetime) -> bool:
    return task_due_date.date() == current_time.date()
```

### 3. Update CLI Flows
Modify the add_task and update_task functions to include due date and recurrence prompts:

```python
def add_task():
    # ... existing code ...
    
    # Prompt for due date
    due_date_input = input("Enter due date (YYYY-MM-DD HH:MM) or press Enter for none: ")
    if due_date_input.strip():
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Task will be created without due date.")
            due_date = None
    else:
        due_date = None
    
    # Prompt for recurrence
    recurrence = input("Enter recurrence (none/daily/weekly/monthly) or press Enter for none: ").lower()
    if recurrence not in ["none", "daily", "weekly", "monthly"]:
        recurrence = "none"
    
    # ... create task with new properties ...
```

### 4. Implement Recurring Task Logic
When marking a recurring task as complete, create a new instance:

```python
def complete_task(task_id: int):
    task = get_task_by_id(task_id)
    if task and not task.completed:
        task.completed = True
        task.updated_at = datetime.now()
        
        # Handle recurring tasks
        if task.recurrence != "none" and task.due_date:
            # Create new instance with next due date
            next_due_date = calculate_next_due_date(task.due_date, task.recurrence)
            new_task = Task(
                id=get_next_id(),
                title=task.title,
                description=task.description,
                priority=task.priority,
                tags=task.tags,
                due_date=next_due_date,
                recurrence=task.recurrence
            )
            add_task(new_task)
            print(f"Created next instance of recurring task '{task.title}' due on {next_due_date}")
```

### 5. Implement Reminder System
Create a function to generate reminders at startup and after key actions:

```python
from datetime import datetime, timedelta

def show_reminders():
    current_time = datetime.now()
    overdue_tasks = []
    due_today_tasks = []
    upcoming_tasks = []
    
    for task in get_all_tasks():
        if not task.completed and task.due_date:
            if task.due_date < current_time and task.due_date.date() < current_time.date():
                overdue_tasks.append(task)
            elif task.due_date.date() == current_time.date():
                due_today_tasks.append(task)
            elif task.due_date <= current_time + timedelta(days=3):
                upcoming_tasks.append(task)
    
    # Display reminders
    if overdue_tasks:
        print(f"\n🔥 OVERDUE TASKS ({len(overdue_tasks)}):")
        for task in overdue_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")
    
    if due_today_tasks:
        print(f"\n⏰ DUE TODAY ({len(due_today_tasks)}):")
        for task in due_today_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")
    
    if upcoming_tasks:
        print(f"\n📅 UPCOMING ({len(upcoming_tasks)}):")
        for task in upcoming_tasks:
            print(f"  - {task.id}: {task.title} (due: {task.due_date.strftime('%Y-%m-%d %H:%M')})")
```

### 6. Update Task Display
Modify the list_tasks function to sort by due date and priority, and show indicators:

```python
def list_tasks():
    tasks = get_all_tasks()
    
    # Sort by due date (soonest first), then by priority
    def sort_key(task):
        # Tasks without due dates come last
        due_order = task.due_date if task.due_date else datetime.max
        priority_order = {"High": 1, "Medium": 2, "Low": 3}[task.priority]
        return (due_order, priority_order)
    
    tasks.sort(key=sort_key)
    
    # Display tasks with due date and recurrence indicators
    for task in tasks:
        due_str = task.due_date.strftime('%Y-%m-%d %H:%M') if task.due_date else "-"
        status_str = "✅" if task.completed else "🔁" if task.recurrence != "none" else "⏳"
        
        print(f"{task.id} | {task.priority} | {task.title} | {task.tags} | {due_str} | {status_str} | {task.description}")
```

## Running the Application
1. Ensure all dependencies are installed (only standard library needed)
2. Run the main CLI application
3. Use the enhanced features as described in the user stories

## Testing
Run the existing test suite to ensure no regression, then add tests for the new features:

```bash
# Run existing tests
python -m pytest tests/

# Add new tests for recurring tasks and due dates
python -m pytest tests/test_recurring_tasks.py
```
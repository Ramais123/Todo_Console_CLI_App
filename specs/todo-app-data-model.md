# Data Model: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Date**: 2026-01-02

## Entities

### Task
Represents a single todo item with the following attributes:

- **id** (int): Unique identifier for the task, auto-incremented
- **title** (str): Title of the task
- **description** (str): Detailed description of the task
- **completed** (bool): Status indicator for completion (default: False)
- **created_at** (datetime): Timestamp when the task was created (optional)

**Validation rules**:
- id must be a positive integer
- title must be a non-empty string
- completed must be a boolean value

**State transitions**:
- Default state: completed = False
- Can transition to: completed = True (via complete operation)
- Can transition from: completed = True to completed = False (via incomplete operation)

### TodoManager
Manages the collection of tasks with the following responsibilities:

- Maintains a list of Task objects
- Provides CRUD operations for tasks
- Manages auto-incrementing ID assignment
- Handles business logic for task operations

**Operations**:
- add_task(title: str, description: str) -> Task
- list_tasks() -> List[Task]
- get_task_by_id(task_id: int) -> Optional[Task]
- update_task(task_id: int, title: str = None, description: str = None) -> bool
- delete_task(task_id: int) -> bool
- mark_task_complete(task_id: int) -> bool
- mark_task_incomplete(task_id: int) -> bool
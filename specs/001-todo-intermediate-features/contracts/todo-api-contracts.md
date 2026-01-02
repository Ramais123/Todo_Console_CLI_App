# API Contracts: Todo App Intermediate Features

## Core Task Operations

### Add Task
- **Endpoint**: `add_task(title: str, description: str, priority: str = "Medium", tags: list[str] = []) -> Task`
- **Description**: Creates a new task with specified properties
- **Parameters**:
  - title (required): Task title
  - description (optional): Task description
  - priority (optional): Priority level ("High", "Medium", "Low"), defaults to "Medium"
  - tags (optional): List of tags, defaults to empty list
- **Returns**: Task object with all properties
- **Errors**: Invalid priority value, empty title

### Update Task
- **Endpoint**: `update_task(id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None) -> Task`
- **Description**: Updates an existing task with specified properties
- **Parameters**:
  - id (required): Task identifier
  - title (optional): New task title
  - description (optional): New task description
  - priority (optional): New priority level
  - tags (optional): New list of tags
- **Returns**: Updated Task object
- **Errors**: Task not found, invalid priority value

### Delete Task
- **Endpoint**: `delete_task(id: int) -> bool`
- **Description**: Deletes a task by ID
- **Parameters**:
  - id (required): Task identifier
- **Returns**: True if successful, False if task not found
- **Errors**: Task not found

### Mark Complete
- **Endpoint**: `mark_complete(id: int) -> Task`
- **Description**: Marks a task as complete
- **Parameters**:
  - id (required): Task identifier
- **Returns**: Updated Task object
- **Errors**: Task not found

### Mark Incomplete
- **Endpoint**: `mark_incomplete(id: int) -> Task`
- **Description**: Marks a task as incomplete
- **Parameters**:
  - id (required): Task identifier
- **Returns**: Updated Task object
- **Errors**: Task not found

## Intermediate Operations

### Search Tasks
- **Endpoint**: `search_tasks(keyword: str) -> list[Task]`
- **Description**: Finds tasks containing the keyword in title or description
- **Parameters**:
  - keyword (required): Search term
- **Returns**: List of matching Task objects
- **Errors**: None (returns empty list if no matches)

### Filter Tasks
- **Endpoint**: `filter_tasks(filter_type: str, filter_value: str) -> list[Task]`
- **Description**: Filters tasks by specified criteria
- **Parameters**:
  - filter_type (required): Type of filter ("status", "priority", "tag")
  - filter_value (required): Value to filter by
- **Returns**: List of matching Task objects
- **Errors**: Invalid filter type, invalid filter value

### Sort Tasks
- **Endpoint**: `sort_tasks(sort_type: str) -> list[Task]`
- **Description**: Sorts tasks by specified criteria
- **Parameters**:
  - sort_type (required): Type of sort ("priority", "title", "status")
- **Returns**: List of sorted Task objects
- **Errors**: Invalid sort type

### Display Tasks Enhanced
- **Endpoint**: `display_tasks_enhanced(tasks: list[Task]) -> None`
- **Description**: Displays tasks in enhanced table format
- **Parameters**:
  - tasks (required): List of Task objects to display
- **Returns**: None (displays to console)
- **Errors**: None
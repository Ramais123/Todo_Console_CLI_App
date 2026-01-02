# Quickstart Guide: Todo App with Intermediate Features

## Getting Started

This guide will help you get up and running with the enhanced Todo app that includes priorities, tags, search, filter, and sort functionality.

## Prerequisites

- Python 3.13+
- UV package manager (optional, for dependency management)

## Installation

1. Clone or download the project repository
2. Navigate to the project directory
3. The application is ready to run (no external dependencies required)

## Running the Application

```bash
python demo.py
```

Or if you're using the main entry point:
```bash
python src/main.py
```

## Basic Usage

### Adding a Task
1. Select "Add Task" from the main menu
2. Enter the task title
3. Enter the task description (optional)
4. Select priority level (High, Medium, Low)
5. Add tags (comma-separated, optional)

### Viewing Tasks
1. Select "View Tasks" from the main menu
2. Tasks will be displayed in an enhanced table format with:
   - ID
   - Priority indicator (🔥, ⚡, ➖)
   - Title
   - Tags (comma-separated or "-")
   - Status (✅/❌)
   - Description (truncated)

### Updating a Task
1. Select "Update Task" from the main menu
2. Enter the task ID
3. Choose which fields to update (title, description, priority, tags)
4. Enter new values

### Marking Tasks Complete/Incomplete
1. Select "Mark Complete" or "Mark Incomplete" from the menu
2. Enter the task ID

### New Intermediate Features

#### Search Tasks
1. Select "Search Tasks" from the main menu
2. Enter a keyword to search in titles and descriptions
3. Matching tasks will be displayed in the enhanced format

#### Filter Tasks
1. Select "Filter Tasks" from the main menu
2. Choose filter type (by status, priority, or tag)
3. Enter the filter value
4. Filtered tasks will be displayed

#### Sort Tasks
1. Select "Sort Tasks" from the main menu
2. Choose sort option (by priority, title, or status)
3. Tasks will be displayed in the selected order

## Example Workflow

1. Add several tasks with different priorities and tags
2. Use "View Tasks" to see all tasks in enhanced format
3. Use "Search Tasks" to find specific tasks by keyword
4. Use "Filter Tasks" to see only high priority tasks
5. Use "Sort Tasks" to order tasks by priority
6. Update tasks as needed
7. Mark completed tasks

## Error Handling

- Invalid task IDs will show an appropriate error message
- Invalid priority values will prompt for a valid selection
- Empty search results will show "No tasks found"
- Invalid inputs will show helpful error messages

## Tips

- Use descriptive tags to organize your tasks effectively
- Set appropriate priorities to focus on important tasks
- Use search to quickly find tasks when you have many
- Combine filter and sort for powerful task organization
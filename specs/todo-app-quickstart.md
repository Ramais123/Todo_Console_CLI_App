# Quickstart Guide: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Date**: 2026-01-02

## Getting Started

### Prerequisites
- Python 3.13 or higher

### Setup
1. Clone or download the project
2. Navigate to the project directory

### Running the Application
```bash
python src/main.py
```

## Usage

Once the application is running, you'll see the prompt:
```
todo> 
```

### Available Commands

**Add a task:**
```
add "Title of the task" "Description of the task"
```

**List all tasks:**
```
list
```

**Update a task:**
```
update <task_id> "New title" "New description"
```

**Delete a task:**
```
delete <task_id>
```

**Mark task as complete:**
```
complete <task_id>
```

**Mark task as incomplete:**
```
incomplete <task_id>
```

**Get help:**
```
help
```

**Exit the application:**
```
exit
```

## Example Session

```
todo> add "Buy groceries" "Milk, bread, eggs"
Added task #1: Buy groceries

todo> add "Walk the dog" "Take Fido to the park"
Added task #2: Walk the dog

todo> list
ID  Status  Title
--  ------  -----
1   [ ]     Buy groceries
2   [ ]     Walk the dog

todo> complete 1
Marked task #1 as complete

todo> list
ID  Status  Title
--  ------  -----
1   [x]     Buy groceries
2   [ ]     Walk the dog

todo> exit
Goodbye!
```

## Notes
- All data is stored in memory only and will be lost when the application exits
- Task IDs are auto-incremented starting from 1
- The application handles invalid inputs gracefully
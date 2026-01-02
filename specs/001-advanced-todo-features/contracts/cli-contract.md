# CLI Interface Contract for Advanced Todo Features

## Overview
This document defines the contract for the CLI interface of the advanced todo application, including the new features for recurring tasks and due date reminders.

## Command Structure
The CLI follows the existing structure with enhancements to support new features.

### Main Menu Options
1. Add Task
2. View Tasks
3. Update Task
4. Complete Task
5. Delete Task
6. Exit

## Enhanced Functionality

### 1. Add Task
**Input Flow:**
- Prompt for title
- Prompt for description (optional)
- Prompt for priority (High/Medium/Low)
- Prompt for tags (comma-separated)
- **NEW:** Prompt for due date (format: YYYY-MM-DD HH:MM, optional)
- **NEW:** Prompt for recurrence (none/daily/weekly/monthly)

**Output:**
- Success message with task ID
- Error message for invalid inputs

**Validations:**
- Title is required
- Due date format must be valid
- Recurrence must be one of the allowed values

### 2. View Tasks
**Output Format:**
- ID | Priority | Title | Tags | Due (or "-") | Status/Recur | Description

**Sorting:**
- First by due date (soonest first, None last)
- Second by priority (High → Medium → Low)

**Visual Indicators:**
- 🔁 for recurring tasks
- ⏰ for tasks due today
- 🔥 OVERDUE for overdue tasks

### 3. Update Task
**Input Flow:**
- Prompt for task ID
- Offer options to update:
  - Title
  - Description
  - Priority
  - Tags
  - **NEW:** Due date
  - **NEW:** Recurrence

**Validations:**
- Task ID must exist
- Due date format must be valid
- Recurrence must be one of the allowed values

### 4. Complete Task
**Behavior:**
- Mark task as completed
- **NEW:** If task is recurring, create new instance with next due date
- **NEW:** Display message about new instance creation for recurring tasks

### 5. Delete Task
**Behavior:**
- Delete task by ID
- No change from existing functionality

### 6. Exit
**Behavior:**
- Exit the application
- No change from existing functionality

## Reminder System
**Trigger Points:**
- Application startup
- After each major action (add/update/complete/delete)

**Display Format:**
- Overdue tasks: "🔥 OVERDUE TASKS (count):" followed by list
- Due today: "⏰ DUE TODAY (count):" followed by list
- Upcoming: "📅 UPCOMING (count):" followed by list

## Error Handling
- Invalid date format: "Invalid date format. Please use YYYY-MM-DD HH:MM"
- Invalid recurrence: "Invalid recurrence. Please choose none, daily, weekly, or monthly"
- Task not found: "Task with ID X not found"
- Other errors: Appropriate error message with guidance

## Data Model Contract
The underlying Task model includes these properties:
- id: int
- title: str
- description: str
- completed: bool
- priority: str (High/Medium/Low)
- tags: list[str]
- due_date: Optional[datetime]
- recurrence: str (none/daily/weekly/monthly)
- created_at: datetime
- updated_at: datetime
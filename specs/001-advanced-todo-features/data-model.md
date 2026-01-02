# Data Model for Advanced Todo Features

## Task Entity

The enhanced Task entity includes all original properties plus new fields for due dates and recurrence.

### Fields
- **id**: `int` - Unique identifier for the task (auto-incrementing)
- **title**: `str` - The task title/description
- **description**: `str` - Detailed description of the task (optional)
- **completed**: `bool` - Whether the task is completed (default: False)
- **priority**: `str` - Priority level ("High", "Medium", "Low") (default: "Medium")
- **tags**: `list[str]` - List of tags associated with the task (default: [])
- **due_date**: `Optional[datetime.datetime]` - Optional due date/time for the task (default: None)
- **recurrence**: `str` - Recurrence interval ("none", "daily", "weekly", "monthly") (default: "none")
- **created_at**: `datetime.datetime` - Timestamp when the task was created
- **updated_at**: `datetime.datetime` - Timestamp when the task was last updated

### Validation Rules
- `id` must be unique within the system
- `title` must not be empty
- `priority` must be one of "High", "Medium", or "Low"
- `tags` must be a list of strings
- `due_date` must be a valid datetime if provided
- `recurrence` must be one of "none", "daily", "weekly", or "monthly"

### State Transitions
- When a recurring task is marked as complete:
  1. The original task's `completed` status is set to True
  2. A new Task instance is created with the same properties except:
     - New `id` (next available)
     - New `due_date` calculated based on recurrence interval
     - `completed` set to False
     - `created_at` and `updated_at` set to current time

## RecurringTask Entity

A RecurringTask is a special case of a Task where the `recurrence` field is not "none".

### Properties
- Inherits all properties from Task entity
- `recurrence` is one of "daily", "weekly", or "monthly"
- When completed, triggers creation of a new Task instance with updated due date

### Validation Rules
- Must have a valid `due_date` when `recurrence` is not "none"
- `recurrence` interval must be one of the supported values

## Reminder Entity

The Reminder entity represents tasks that need to be highlighted in the reminder section.

### Properties
- **task**: `Task` - The associated task
- **reminder_type**: `str` - Type of reminder ("overdue", "due_today", "upcoming")
- **time_until_due**: `timedelta` - Time difference from current time to due date

### Validation Rules
- `reminder_type` must be one of "overdue", "due_today", or "upcoming"
- `task` must be a valid Task entity
# Data Model: Todo App Intermediate Features

## Task Entity

### Fields
- **id**: int (unique identifier, auto-incrementing)
- **title**: str (task title/description)
- **description**: str (detailed task description)
- **completed**: bool (completion status, default: False)
- **priority**: str (priority level: "High", "Medium", "Low"; default: "Medium")
- **tags**: list[str] (list of tags associated with the task; default: empty list)

### Relationships
- No direct relationships with other entities

### Validation Rules
- id: Must be a positive integer
- title: Required, non-empty string
- description: Optional, can be empty string
- completed: Boolean value only
- priority: Must be one of "High", "Medium", "Low"; defaults to "Medium" if not specified
- tags: List of strings, each tag should be non-empty after stripping whitespace

### State Transitions
- completed: Can transition from False to True (mark_complete) or True to False (mark_incomplete)

## Priority Entity

### Values
- **High**: Highest priority tasks, indicated visually with 🔥
- **Medium**: Medium priority tasks, indicated visually with ⚡
- **Low**: Low priority tasks, indicated visually with ➖
- **Default**: Medium priority when not explicitly set

## Tag Entity

### Characteristics
- String values that categorize tasks
- Multiple tags per task allowed
- Examples: "work", "personal", "health", "shopping"
- Stored as a list of strings in the Task entity

### Validation Rules
- Each tag must be a non-empty string after stripping whitespace
- Duplicates should be removed from the tag list
- Tags should be converted to lowercase for consistency

## Filter Entity

### Characteristics
- Represents criteria for filtering tasks
- Used by the filter functionality

### Types
- **By Status**: Filter by completed/incomplete
- **By Priority**: Filter by High/Medium/Low
- **By Tag**: Filter by exact tag match

## SortOption Entity

### Characteristics
- Represents criteria for sorting tasks
- Used by the sort functionality

### Types
- **By Priority**: Sort by priority (High → Medium → Low)
- **By Title**: Sort alphabetically by title (A-Z)
- **By Status**: Sort by status (Incomplete first)
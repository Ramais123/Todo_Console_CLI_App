# CLI Contracts: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Date**: 2026-01-02

## Command Interface Specification

### Command Format
```
command [arguments...]
```

### Available Commands

#### `add`
**Description**: Add a new task
**Arguments**: 
- title (string): Task title
- description (string): Task description
**Response**: Confirmation message with assigned task ID
**Example**: `add "Buy groceries" "Milk, bread, eggs"`

#### `list`
**Description**: List all tasks
**Arguments**: None
**Response**: Formatted table of all tasks with ID, status, title
**Example**: `list`

#### `update`
**Description**: Update an existing task
**Arguments**: 
- id (integer): Task ID
- title (string, optional): New task title
- description (string, optional): New task description
**Response**: Confirmation message or error if task not found
**Example**: `update 1 "Buy weekly groceries" "Milk, bread, eggs, fruits"`

#### `delete`
**Description**: Delete a task
**Arguments**: 
- id (integer): Task ID
**Response**: Confirmation message or error if task not found
**Example**: `delete 1`

#### `complete`
**Description**: Mark a task as complete
**Arguments**: 
- id (integer): Task ID
**Response**: Confirmation message or error if task not found
**Example**: `complete 1`

#### `incomplete`
**Description**: Mark a task as incomplete
**Arguments**: 
- id (integer): Task ID
**Response**: Confirmation message or error if task not found
**Example**: `incomplete 1`

#### `help`
**Description**: Show help information
**Arguments**: None
**Response**: Help text with all available commands
**Example**: `help`

#### `exit` or `quit`
**Description**: Exit the application
**Arguments**: None
**Response**: Goodbye message and application termination
**Example**: `exit`
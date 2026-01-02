# Research: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Date**: 2026-01-02

## Decision Log

### Decision: Use dataclass for Task model
**Rationale**: Dataclasses provide a clean, readable way to define simple data containers with type hints. They automatically generate common methods like __init__, __repr__, and __eq__.

**Alternatives considered**: 
- Regular class: More verbose, requires manual implementation of __init__ and other methods
- NamedTuple: Immutable, which might be limiting for future updates to tasks

### Decision: Use list for in-memory storage
**Rationale**: A simple list provides the necessary functionality for storing tasks in memory. It allows for easy iteration, appending, and removal operations.

**Alternatives considered**:
- Dictionary with ID as key: More complex for this simple use case
- Set: Doesn't maintain order and doesn't allow duplicates (not an issue here)

### Decision: Implement CLI with input loop
**Rationale**: An interactive command-line interface with a continuous input loop provides the best user experience for this type of application. Users can enter commands repeatedly without restarting the application.

**Alternatives considered**:
- Single command execution: Would require restarting the app for each operation
- Menu-based interface: More complex than necessary for this use case

### Decision: Use simple string parsing for commands
**Rationale**: For this application, simple string splitting and parsing is sufficient to handle commands. It avoids dependencies on external libraries like argparse for the CLI parsing.

**Alternatives considered**:
- argparse: Would require restructuring to single-command execution rather than interactive loop
- click: External dependency, which violates the constraint of no external dependencies

### Decision: Implement error handling with try-catch and validation
**Rationale**: Proper error handling prevents the application from crashing when users enter invalid inputs or attempt operations on non-existent tasks.

**Alternatives considered**:
- No error handling: Would lead to crashes and poor user experience
- Assertions: Not appropriate for user input validation
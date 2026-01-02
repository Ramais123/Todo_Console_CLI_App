# Implementation Plan: Todo App Intermediate Features

**Feature**: Todo In-Memory Python Console App – Intermediate Level Extension
**Branch**: 001-todo-intermediate-features
**Created**: 2026-01-02
**Status**: Draft

## Technical Context

The todo app is a CLI-based application with in-memory storage. The Basic Level functionality is already implemented with the following features:
- Add task (title + description)
- View all tasks with status
- Update task
- Delete by ID
- Mark complete/incomplete
- Tasks have: id (int), title (str), description (str), completed (bool)
- In-memory storage uses a list of Task objects
- CLI has a main loop with menu options

The Intermediate Level Extension will add:
- Priority levels (High, Medium, Low) with visual indicators
- Tags/Categories support (multiple tags per task)
- Search functionality (keyword search in title/description)
- Filter functionality (by status, priority, tag)
- Sort functionality (by priority, title, status)
- Enhanced view with rich table display

**Technology Stack**:
- Python 3.13+
- UV for package management
- In-memory storage only (no external dependencies)
- Standard library for CLI implementation

**NEEDS CLARIFICATION**: 
- What is the exact structure of the existing Basic Level codebase? (files, classes, functions)
- Are there any existing tests for the Basic Level functionality that need to be preserved?
- What is the current UI/UX flow for the Basic Level app?

## Constitution Check

This plan adheres to the project constitution:
- ✅ Spec-Driven Development: Based on the provided feature specification
- ✅ No Manual Boilerplate: Will generate complete, functional code
- ✅ Agentic Workflow: Following the Step 1 (plan), Step 2 (tasks), Step 3 (implementation) workflow
- ✅ Technology Constraints: Using Python 3.13+, UV, in-memory storage only
- ✅ Code Quality: Will include proper structure, error handling, and documentation

## Gates

### Gate 1: Architecture Feasibility
- [x] Basic Level functionality is complete and working
- [x] In-memory storage approach confirmed
- [x] CLI interface approach confirmed
- [x] Extension approach (modifying existing code vs. rewriting) confirmed

### Gate 2: Technical Requirements
- [x] Python 3.13+ available
- [x] UV package manager available
- [x] No external dependencies required
- [x] Existing Basic Level codebase accessible

### Gate 3: Implementation Constraints
- [x] No breaking changes to Basic Level functionality
- [x] All changes will be AI-generated
- [x] No manual code modifications
- [x] Clean, modular code structure maintained

## Phase 0: Research

### Research Tasks

1. **Codebase Structure Research**
   - Task: "Research existing Basic Level codebase structure"
   - Rationale: Need to understand current implementation to extend properly
   - Outcome: Understanding of existing classes, functions, and file structure

2. **Task Model Enhancement Research**
   - Task: "Research best practices for extending data models in Python"
   - Rationale: Need to add priority and tags fields to existing Task model
   - Outcome: Clear approach for extending the Task class/dataclass

3. **CLI Enhancement Research**
   - Task: "Research best practices for extending CLI menus in Python"
   - Rationale: Need to add new menu options for search, filter, sort
   - Outcome: Clear approach for extending the existing CLI interface

4. **Table Display Research**
   - Task: "Research best practices for table display in Python CLI without external libraries"
   - Rationale: Need to implement enhanced view with fixed-width columns
   - Outcome: Clear approach for formatting table output

## Phase 1: Design & Contracts

### Data Model: data-model.md

**Task Entity Enhancement**:
- Current fields: id (int), title (str), description (str), completed (bool)
- New fields: priority (str, values: "High", "Medium", "Low", default: "Medium"), tags (list[str], default: empty list)
- Visual indicators: 🔥 (High), ⚡ (Medium), ➖ (Low)

**Priority Entity**:
- Enumeration with three values: "High", "Medium", "Low"
- Default value: "Medium"
- Visual indicators: 🔥 (High), ⚡ (Medium), ➖ (Low)

**Tag Entity**:
- String values (e.g., "work", "personal", "health", "shopping")
- Multiple tags per task allowed
- Stored as list of strings

### API Contracts

**Core Task Operations**:
- `add_task(title: str, description: str, priority: str = "Medium", tags: list[str] = []) -> Task`
- `update_task(id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None) -> Task`
- `delete_task(id: int) -> bool`
- `mark_complete(id: int) -> Task`
- `mark_incomplete(id: int) -> Task`

**New Intermediate Operations**:
- `search_tasks(keyword: str) -> list[Task]`
- `filter_tasks(filter_type: str, filter_value: str) -> list[Task]`
- `sort_tasks(sort_type: str) -> list[Task]`
- `display_tasks_enhanced(tasks: list[Task]) -> None`

### Quickstart Guide

1. Run the application: `python main.py`
2. Use the menu to add tasks with priority and tags
3. View tasks in enhanced table format
4. Use search, filter, and sort options to organize tasks
5. Update or delete tasks as needed

## Phase 2: Implementation Approach

### File Structure
```
src/
├── main.py          # Entry point with CLI loop
├── todo.py          # Task model and core operations
├── ui.py            # User interface functions (display, input handling)
└── storage.py       # In-memory storage operations
```

### Implementation Steps
1. Extend Task model with priority and tags fields
2. Update add_task and update_task functions to handle new fields
3. Implement search, filter, and sort functions
4. Create enhanced display function with table formatting
5. Update CLI menu with new options
6. Ensure all Basic Level functionality remains intact
7. Add input validation and error handling

## Re-evaluation of Constitution Check (Post-Design)

- ✅ All design decisions align with project constitution
- ✅ No external dependencies introduced
- ✅ In-memory storage maintained
- ✅ Clean, modular code structure planned
- ✅ All Basic Level functionality preserved
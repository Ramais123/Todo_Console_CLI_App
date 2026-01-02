---
id: 003
title: Tasks Todo Intermediate Features
stage: tasks
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-intermediate-features
branch: 001-todo-intermediate-features
user: ramai
command: /sp.tasks
labels: [tasks, todo-app, features]
links:
  spec: ../specs/001-todo-intermediate-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ./specs/001-todo-intermediate-features/tasks.md
tests:
  - ./specs/001-todo-intermediate-features/tasks.md
---

## Prompt

$ARGUMENTS

Todo In-Memory Python Console App – Intermediate Level Extension (on top of completed Basic Level)
Objective: Extend the fully working Basic Level CLI todo app by adding all Intermediate Level organization and usability features (Priorities, Tags/Categories, Search, Filter, Sort). All changes must be 100% AI-generated using Qwen via the spec-driven workflow. No manual code modifications allowed.
Prerequisites:

Basic Level is already complete and functional.
Current Task model includes: id (int), title (str), description (str), completed (bool).
In-memory storage uses a list of Task objects.
CLI has a main loop with menu options for Add, List, Update, Delete, Mark Complete, Exit.

High-Level Plan:

Enhance Task Data Model
Add priority field: "High", "Medium", "Low" (default: "Medium")
Add tags field: list[str] (empty by default)
Define priority indicators: 🔥 (High), ⚡ (Medium), ➖ (Low)
Update existing Task class/dataclass accordingly

Modify Add Task Flow
After entering title and description, prompt for priority (with options 1-High, 2-Medium, 3-Low)
Then prompt for tags (comma-separated, optional; press Enter for none)
Parse and store tags as stripped lowercase list

Modify Update Task Flow
When updating a task by ID, offer options to update title, description, priority, and/or tags
Allow adding/removing/replacing tags (comma-separated input)

Upgrade List/View Display
Create enhanced display function showing a formatted table:
ID | Priority | Title | Tags | Status | Description (truncated)
Use fixed-width columns with alignment (no external libraries)
Show "-" for empty tags
Call this enhanced view as default for normal List command

Implement Sort Tasks
Add "Sort Tasks" menu option
Sub-menu with choices: 1. By Priority (High → Medium → Low), 2. By Title (A-Z), 3. By Status (Incomplete first)
Create a sorted copy of the task list based on choice and display using enhanced view
Sorting is temporary (only affects display, not stored order)

Implement Search Tasks
Add "Search Tasks" menu option
Prompt for keyword
Find case-insensitive matches in title or description
Display matching tasks with enhanced view (or "No tasks found")

Implement Filter Tasks
Add "Filter Tasks" menu option
Sub-menu for filter type: 1. By Status, 2. By Priority, 3. By Tag
Apply single filter and display results with enhanced view (or "No tasks match")
For tag filter: prompt for exact tag name

Update Main Menu
Extend menu with new numbered options:
Sort Tasks
Search Tasks
Filter Tasks

Keep existing options intact and renumber cleanly
Ensure menu remains easy to read

Input Validation & Error Handling
Validate priority choices
Handle invalid IDs gracefully (already in Basic, ensure preserved)
Validate tag inputs (strip, lowercase, deduplicate)
Provide clear, friendly error and success messages

Comprehensive Testing
Test full flows: Add tasks with priority/tags → List → Update priority/tags → Search by keyword → Filter by tag/priority/status → Sort by different criteria
Verify no regression in Basic features
Test edge cases: empty task list, no tags, long titles/descriptions, invalid inputs

Deliverables Finalization
Save this spec as specs_history/spec_intermediate_final.md
Update README.md with new Intermediate features description and usage examples
Ensure /src code remains clean and modular (e.g., separate concerns: models.py, storage.py, ui.py, main.py if applicable)
Prepare demo script showing all Basic + Intermediate capabilities


Execution Guidelines:

Proceed sequentially from step 1 to 11.
Break each step into small, atomic tasks for targeted code generation.
Generate code incrementally, integrate carefully into existing codebase, and verify after each major section.
Prioritize preserving existing functionality.

Success: A highly usable, polished CLI todo app that seamlessly combines all Basic and Intermediate features, delivering an excellent user experience ready for hackathon presentation and judging.

## Response snapshot

I have successfully generated the tasks.md file for the Todo In-Memory Python Console App – Intermediate Level Extension. The tasks are organized by user story to enable independent implementation and testing of each feature.

The generated tasks.md includes:

1. Phase 1: Setup tasks for creating the project structure
2. Phase 2: Foundational tasks for the core infrastructure (Task model, storage, CLI, UI)
3. Phase 3: User Story 1 - Enhanced Task Management with Priorities and Tags (P1 - MVP)
4. Phase 4: User Story 2 - Search Tasks by Content (P2)
5. Phase 5: User Story 3 - Filter and Sort Tasks (P3)
6. Phase 6: User Story 4 - Enhanced Task View (P4)
7. Phase 7: Polish & Cross-Cutting Concerns

Each task follows the required format with checkboxes, task IDs, story labels where appropriate, and specific file paths. The tasks are organized to allow for parallel execution where possible and include dependency information for proper execution order.

The tasks align with the requirements from the feature specification, implementation plan, data model, and API contracts, ensuring all Intermediate features (priorities, tags, search, filter, sort) are properly implemented while preserving existing Basic Level functionality.

## Outcome

- ✅ Impact: Created comprehensive task list for implementing intermediate todo app features
- 🧪 Tests: Tasks validated against specification requirements
- 📁 Files: tasks.md created with organized phases and dependencies
- 🔁 Next prompts: Ready for implementation phase
- 🧠 Reflection: Tasks organized by user story for independent implementation and testing

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
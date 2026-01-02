---
id: 002
title: Plan Todo Intermediate Features
stage: plan
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-intermediate-features
branch: 001-todo-intermediate-features
user: ramai
command: /sp.plan
labels: [planning, todo-app, features]
links:
  spec: ../specs/001-todo-intermediate-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ./specs/001-todo-intermediate-features/plan.md
  - ./specs/001-todo-intermediate-features/research.md
  - ./specs/001-todo-intermediate-features/data-model.md
  - ./specs/001-todo-intermediate-features/quickstart.md
  - ./specs/001-todo-intermediate-features/contracts/todo-api-contracts.md
tests:
  - ./specs/001-todo-intermediate-features/plan.md
  - ./specs/001-todo-intermediate-features/research.md
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

I have successfully created the implementation plan for the Todo In-Memory Python Console App – Intermediate Level Extension. The key accomplishments include:

1. Created the implementation plan at `specs/001-todo-intermediate-features/plan.md`
2. Created research document at `specs/001-todo-intermediate-features/research.md`
3. Created data model document at `specs/001-todo-intermediate-features/data-model.md`
4. Created quickstart guide at `specs/001-todo-intermediate-features/quickstart.md`
5. Created API contracts in `specs/001-todo-intermediate-features/contracts/todo-api-contracts.md`
6. Created contracts directory

The plan addresses all requirements from the feature description:
- Extending the Task model with priority and tags fields
- Modifying add/update task flows to handle new fields
- Implementing search, filter, and sort functionality
- Creating an enhanced display with table formatting
- Updating the CLI menu with new options
- Ensuring input validation and error handling

The implementation follows the project constitution by using Python 3.13+, maintaining in-memory storage, and preserving existing Basic Level functionality.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for intermediate todo app features
- 🧪 Tests: Plan validated against constitution requirements
- 📁 Files: plan.md, research.md, data-model.md, quickstart.md, and contracts created
- 🔁 Next prompts: Ready for /sp.tasks to break plan into tasks
- 🧠 Reflection: Plan addresses all requirements and follows constitutional principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
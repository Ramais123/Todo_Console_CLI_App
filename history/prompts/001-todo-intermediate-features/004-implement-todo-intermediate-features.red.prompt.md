---
id: 004
title: Implement Todo Intermediate Features
stage: red
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-intermediate-features
branch: 001-todo-intermediate-features
user: ramai
command: /sp.implement
labels: [implementation, todo-app, features]
links:
  spec: ../specs/001-todo-intermediate-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ./src/todo.py
  - ./src/main.py
  - ./src/ui.py
  - ./demo_intermediate.py
  - ./test_enhanced_todo.py
  - ./README.md
  - ./requirements.txt
  - ./specs/001-todo-intermediate-features/tasks.md
tests:
  - ./test_enhanced_todo.py
  - ./demo_intermediate.py
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

I have successfully implemented the Todo In-Memory Python Console App – Intermediate Level Extension. The implementation includes all requested features:

1. Enhanced Task Data Model:
   - Added priority field with values "High", "Medium", "Low" (default: "Medium")
   - Added tags field as a list of strings (default: empty list)
   - Updated the Task class with these new fields

2. Modified Add Task Flow:
   - Updated add_task function to accept priority and tags
   - Added input validation for priority and tags
   - Implemented parsing of comma-separated tags

3. Modified Update Task Flow:
   - Updated update_task function to modify priority and tags
   - Added validation for priority and tags during updates

4. Upgraded List/View Display:
   - Created enhanced display function with formatted table
   - Implemented fixed-width columns with alignment
   - Added visual indicators for priority levels
   - Added truncation for long descriptions
   - Show "-" for empty tags

5. Implemented Sort Tasks:
   - Created sort_tasks function with options for priority, title, and status
   - Implemented proper sorting logic (High → Medium → Low, alphabetical, incomplete first)

6. Implemented Search Tasks:
   - Created search_tasks function with case-insensitive matching
   - Implemented search in both title and description

7. Implemented Filter Tasks:
   - Created filter_tasks function with options for status, priority, and tag
   - Implemented proper filtering logic for each type

8. Updated Main Menu:
   - Added new commands for search, filter, and sort
   - Updated help text to include new functionality
   - Maintained all existing Basic Level functionality

9. Input Validation & Error Handling:
   - Added validation functions for priority and tags
   - Implemented proper error handling throughout
   - Preserved all existing error handling

10. Comprehensive Testing:
    - Created test_enhanced_todo.py with tests for all functionality
    - Created demo_intermediate.py showing all features in action
    - Verified no regression in Basic features
    - Tested end-to-end flows

11. Deliverables Finalization:
    - Updated README.md with new Intermediate features description and usage examples
    - Created requirements.txt file
    - Ensured modular code structure (models in todo.py, UI in ui.py, main logic in main.py)
    - Prepared demo script showing all Basic + Intermediate capabilities

All tasks from the tasks.md file have been completed and marked as [X] in the file. The implementation maintains backward compatibility with existing Basic Level functionality while adding all requested Intermediate Level features.

## Outcome

- ✅ Impact: Successfully implemented all Intermediate Level features for the Todo app
- 🧪 Tests: All functionality tested with test_enhanced_todo.py and demo_intermediate.py
- 📁 Files: Multiple files updated/created including todo.py, main.py, ui.py, README.md
- 🔁 Next prompts: Ready for further enhancements or deployment
- 🧠 Reflection: Implementation follows clean architecture principles and maintains backward compatibility

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
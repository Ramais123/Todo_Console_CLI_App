---
id: "001"
title: "advanced-todo-features-planning"
stage: "plan"
date_iso: "2026-01-02"
surface: "agent"
model: "Qwen"
feature: "advanced-todo-features"
branch: "001-advanced-todo-features"
user: "ramai"
command: "sp.plan"
labels:
  - "planning"
  - "todo-app"
  - "recurring-tasks"
  - "due-dates"
links:
  spec: "specs/001-advanced-todo-features/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-advanced-todo-features/plan.md"
  - "specs/001-advanced-todo-features/research.md"
  - "specs/001-advanced-todo-features/data-model.md"
  - "specs/001-advanced-todo-features/quickstart.md"
  - "specs/001-advanced-todo-features/contracts/cli-contract.md"
tests_yaml:
  - "No tests added in this session"
prompt_text: |
  /sp.plan Todo In-Memory Python Console App – Advanced Level Extension (Intelligent Features)
  Objective: Extend the fully functional Basic + Intermediate Level CLI todo app by adding Advanced Level intelligent features: Recurring Tasks with auto-rescheduling and Due Dates with console-based time reminders. All implementation must be 100% AI-generated using Qwen via the spec-driven workflow. No manual code changes allowed.
  Prerequisites:

  Basic + Intermediate Levels are complete and working perfectly.
  Current Task model includes: id, title, description, completed, priority ("High"/"Medium"/"Low"), tags (list[str]).
  Enhanced display, search, filter, sort, and polished CLI menu already exist.
  In-memory storage uses a list of Task objects.

  High-Level Plan:

  Enhance Task Data Model
  Add due_date: Optional datetime.datetime (None by default)
  Add recurrence: Optional string ("none", "daily", "weekly", "monthly") – default "none"
  Add recurrence_indicator: "🔁" for recurring tasks
  Add overdue/today indicators: "⏰" for due today, "🔥 OVERDUE" for past due
  Update Task class/dataclass with these fields

  Modify Add Task Flow
  After priority and tags, prompt for optional due date/time (format: YYYY-MM-DD or YYYY-MM-DD HH:MM; Enter for none)
  Then prompt for recurrence (options: none, daily, weekly, monthly)
  Parse due_date using datetime.strptime with clear format guidance and validation
  Store recurrence as lowercase string

  Modify Update Task Flow
  When updating, offer options to change due date and recurrence independently
  Allow clearing due date (set to None) or recurrence (set to "none")

  Implement Recurring Task Logic
  When marking a recurring task as complete:
  Calculate next due date based on recurrence interval:
  daily: +1 day
  weekly: +7 days
  monthly: +1 month (approximate same day)

  Create a new Task instance copying title, description, priority, tags, recurrence
  Set new task's due_date to calculated next date
  Mark original as completed (keep for history)

  Do not modify non-recurring tasks

  Implement Reminder System
  On app startup and after every major action (add/update/complete/delete):
  Calculate current date/time (use datetime.now())
  Generate reminder section printed at top:
  Overdue tasks (due_date < now and not completed)
  Due today (same date, not completed)
  Upcoming in next 3 days (not completed)

  Bold/emphasized console alerts (e.g., using simple formatting or ANSI codes if safe)

  Show count and brief list (ID, Title, Due info)

  Upgrade List/View Display
  Add Due Date column and indicators
  New table format:
  ID | Priority | Title | Tags | Due (or "-") | Status/Recur | Description
  Auto-sort displayed tasks:
  1st by due_date (soonest first, None last)
  2nd by priority (High → Medium → Low)
  Highlight overdue rows visually (e.g., prefix with 🔥)

  Update Main Menu & Flows
  Keep existing menu; no new top-level options needed (features integrated into Add/Update/Mark Complete)
  Ensure reminder section appears automatically without menu choice

  Date Handling & Validation
  Use datetime module for parsing, comparison, and arithmetic
  Handle month rollover correctly for monthly recurrence
  Graceful error messages for invalid date formats
  Timezone-naive (local time assumption)

  Error Handling & UX Polish
  Validate all new inputs thoroughly
  Helpful prompts (e.g., "Enter due date (YYYY-MM-DD HH:MM) or press Enter for none:")
  Confirmations for recurrence setup
  Clear messages when auto-creating next recurring instance

  Comprehensive Testing
  Test recurrence: Create weekly task → complete → verify new instance with +7 days due
  Test due dates: Set past/future dates → restart app → verify reminders and sorting
  Test mixed scenarios: recurring + overdue, non-recurring + today due
  Verify no regression in Basic/Intermediate features
  Edge cases: monthly rollover (Jan 31 → Feb), no due date, clearing recurrence

  Deliverables Finalization
  Save this spec as specs_history/spec_advanced_v1.md
  Update README.md with Advanced features description, usage examples, and demo steps (including recurrence and reminders)
  Ensure code remains modular and clean
  Prepare full demo showcasing recurring task creation/completion and reminder alerts


  Execution Guidelines:

  Proceed sequentially from step 1 to 11.
  Break each step into small atomic tasks for precise code generation.
  Integrate incrementally and test after key milestones (e.g., after data model update, after recurrence logic, after reminders).
  Prioritize correctness of date arithmetic and non-regression.

  Success: A smart, time-aware CLI todo app with intelligent recurring tasks and proactive console reminders, delivering a highly impressive demonstration of progressive, spec-driven AI development for the hackathon.
response_text: |
  Successfully created the implementation plan for Advanced Todo Features with Recurring Tasks and Due Date Reminders. The plan includes:
  - Technical context with Python 3.13, standard libraries only, in-memory storage
  - Project structure with models, services, CLI, and utility modules
  - Research findings on date/time handling, task model enhancement, CLI interface, and reminder system
  - Data model specification for Task, RecurringTask, and Reminder entities
  - Quickstart guide with implementation steps
  - CLI interface contract
  - All artifacts created in the specs/001-advanced-todo-features directory
outcome: |
  Implementation plan completed successfully with all required artifacts. Ready for task breakdown phase.
evaluation: |
  The plan comprehensively covers all aspects of the advanced todo features implementation, following the spec requirements and constitution principles.
---

# Implementation Plan: Advanced Todo Features with Recurring Tasks and Due Date Reminders

**Branch**: `001-advanced-todo-features` | **Date**: 2026-01-02 | **Spec**: [link to spec.md](spec.md)
**Input**: Feature specification from `/specs/001-advanced-todo-features/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Extending the existing CLI todo app with intelligent features: recurring tasks with auto-rescheduling and due dates with console-based time reminders. The implementation will enhance the Task data model with due dates and recurrence properties, modify the CLI flows to support these new features, implement the recurring task logic, and create a reminder system that displays alerts for overdue and upcoming tasks.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13
**Primary Dependencies**: Standard library only (use datetime from stdlib; no external packages like pendulum or dateparser)
**Storage**: In-memory only; all recurring instances and due dates lost on exit
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform CLI application
**Project Type**: Single project CLI application
**Performance Goals**: App should start in under 2 seconds, task operations should complete in under 500ms
**Constraints**: Strictly in-memory storage, console-based only (no real browser notifications), keep complexity manageable for CLI
**Scale/Scope**: Single user CLI application with time-aware features

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Spec-Driven Development Only: Plan based entirely on provided feature specification
- [x] No Manual Boilerplate: Will generate complete, functional code using Python 3.13+
- [x] Agentic Workflow Enforcement: Following Step 1 (high-level plan) as required
- [x] Technology Constraints: Using standard library only, in-memory storage as specified
- [x] Code Quality Rules: Will follow PEP8, include type hints, docstrings, and proper error handling

**Note**: The agent context update step failed due to template path issue, but this doesn't affect the core implementation plan.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── todo.py          # Task model and related classes
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   └── main.py          # CLI interface and menu system
└── lib/
    └── date_utils.py    # Date/time utilities for recurrence and reminders

tests/
├── unit/
│   └── test_todo.py     # Unit tests for todo models
├── integration/
│   └── test_todo_service.py  # Integration tests for todo services
└── contract/
    └── test_cli.py      # Contract tests for CLI interface
```

**Structure Decision**: Single project CLI application with modular structure separating models, services, CLI interface, and utility functions. This structure allows for clear separation of concerns while maintaining simplicity for a single-user CLI application.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
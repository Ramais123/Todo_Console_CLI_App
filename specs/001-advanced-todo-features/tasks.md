# Tasks: Advanced Todo Features with Recurring Tasks and Due Date Reminders

**Input**: Design documents from `/specs/001-advanced-todo-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/, tests/
- [ ] T002 Initialize Python 3.13 project with basic dependencies
- [x] T003 [P] Create directory structure: src/models/, src/services/, src/cli/, src/lib/, tests/unit/, tests/integration/, tests/contract/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Enhance Task model with due_date and recurrence properties in src/models/todo.py
- [x] T005 [P] Create date utilities module for recurrence calculations in src/lib/date_utils.py
- [x] T006 [P] Create base CLI structure in src/cli/main.py
- [x] T007 Create TaskService for business logic in src/services/todo_service.py
- [x] T008 Configure error handling and validation utilities
- [x] T009 Update existing CLI menu to support new features in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and Manage Recurring Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create recurring tasks with daily, weekly, or monthly intervals that automatically create new instances when completed

**Independent Test**: Can be fully tested by creating a recurring task, marking it as complete, and verifying that a new instance is automatically created with the next due date.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for recurring task creation in tests/contract/test_cli.py
- [ ] T011 [P] [US1] Integration test for recurring task completion flow in tests/integration/test_recurring_tasks.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Update Task model with recurrence validation in src/models/todo.py
- [x] T013 [US1] Implement recurring task logic in TaskService in src/services/todo_service.py
- [x] T014 [US1] Update complete_task function to handle recurring tasks in src/services/todo_service.py
- [x] T015 [US1] Add recurring task indicator to task display in src/cli/main.py
- [x] T016 [US1] Add acceptance tests for recurring task scenarios in tests/unit/test_recurring_tasks.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Set and View Due Dates (Priority: P1)

**Goal**: Allow users to set optional due dates and times for tasks and sort tasks by due date with the soonest first

**Independent Test**: Can be fully tested by adding a task with a due date, viewing the task list, and verifying that tasks are sorted by due date with the soonest first.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T017 [P] [US2] Contract test for due date functionality in tests/contract/test_cli.py
- [ ] T018 [P] [US2] Integration test for due date sorting in tests/integration/test_due_dates.py

### Implementation for User Story 2

- [x] T019 [P] [US2] Update Task model with due date validation in src/models/todo.py
- [x] T020 [US2] Implement due date parsing and validation in src/lib/date_utils.py
- [x] T021 [US2] Update task display to show due dates and sort by due date in src/cli/main.py
- [x] T022 [US2] Update add_task flow to include due date prompt in src/cli/main.py
- [x] T023 [US2] Add visual indicators for overdue tasks in src/cli/main.py
- [x] T024 [US2] Add acceptance tests for due date scenarios in tests/unit/test_due_dates.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Receive Time-Based Reminders (Priority: P2)

**Goal**: Display reminder section at startup and after key actions showing today's due tasks, overdue tasks, and upcoming tasks in the next 3 days

**Independent Test**: Can be fully tested by starting the app and verifying that the reminder section displays today's due tasks, overdue tasks, and upcoming tasks in the next 3 days.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US3] Contract test for reminder system in tests/contract/test_cli.py
- [ ] T026 [P] [US3] Integration test for reminder display in tests/integration/test_reminders.py

### Implementation for User Story 3

- [x] T027 [P] [US3] Create Reminder model/entity in src/models/todo.py
- [x] T028 [US3] Implement reminder logic in TaskService in src/services/todo_service.py
- [x] T029 [US3] Create reminder display function in src/cli/main.py
- [x] T030 [US3] Integrate reminder display at app startup and after key actions in src/cli/main.py
- [x] T031 [US3] Add acceptance tests for reminder scenarios in tests/unit/test_reminders.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Enhanced Task View with Prioritization (Priority: P2)

**Goal**: Sort task list by due date and priority to help users identify the most urgent tasks

**Independent Test**: Can be fully tested by creating tasks with various due dates and priorities, then viewing the list to verify the sorting order.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T032 [P] [US4] Contract test for enhanced task view in tests/contract/test_cli.py
- [ ] T033 [P] [US4] Integration test for task sorting logic in tests/integration/test_task_sorting.py

### Implementation for User Story 4

- [x] T034 [P] [US4] Update task sorting algorithm in src/services/todo_service.py
- [x] T035 [US4] Enhance task display format in src/cli/main.py
- [x] T036 [US4] Add recurring task indicators to enhanced view in src/cli/main.py
- [x] T037 [US4] Add acceptance tests for enhanced view scenarios in tests/unit/test_task_view.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T038 [P] Documentation updates in README.md
- [x] T039 Code cleanup and refactoring across all modules
- [x] T040 Performance optimization for task sorting and filtering
- [x] T041 [P] Additional unit tests in tests/unit/
- [x] T042 Security hardening and input validation
- [x] T043 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for recurring task creation in tests/contract/test_cli.py"
Task: "Integration test for recurring task completion flow in tests/integration/test_recurring_tasks.py"

# Launch all models for User Story 1 together:
Task: "Update Task model with recurrence validation in src/models/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
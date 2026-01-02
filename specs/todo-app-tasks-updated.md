---

description: "Task list for Todo In-Memory Python Console App - Updated"
---

# Tasks: Todo In-Memory Python Console App - Updated

**Input**: Design documents from `/specs/todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Initialize Python project with proper directory structure
- [x] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create Task dataclass in src/todo.py with id, title, description, completed fields
- [x] T005 [P] Create TodoManager class in src/todo.py with in-memory storage
- [x] T006 Create basic CLI structure in src/main.py
- [x] T007 Implement auto-incrementing ID functionality in TodoManager

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with title and description

**Independent Test**: Can be fully tested by adding a task and verifying it appears in the list

### Implementation for User Story 1

- [x] T008 [US1] Implement add_task method in TodoManager class
- [x] T009 [US1] Add CLI command parsing for 'add' command in main.py
- [x] T010 [US1] Implement user input handling for add command
- [x] T011 [US1] Add confirmation message after task is added

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with ID, status indicator, title, and description

**Independent Test**: Can be fully tested by adding tasks and then listing them to verify they appear correctly

### Implementation for User Story 2

- [x] T012 [US2] Implement list_tasks method in TodoManager class
- [x] T013 [US2] Add CLI command parsing for 'list' command in main.py
- [x] T014 [US2] Implement formatted display of tasks with status indicators
- [x] T015 [US2] Handle case when no tasks exist

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark tasks as complete or incomplete

**Independent Test**: Can be fully tested by adding a task, marking it complete, and verifying the status changes

### Implementation for User Story 3

- [x] T016 [US3] Implement mark_task_complete method in TodoManager class
- [x] T017 [US3] Implement mark_task_incomplete method in TodoManager class
- [x] T018 [US3] Add CLI command parsing for 'complete' command in main.py
- [x] T019 [US3] Add CLI command parsing for 'incomplete' command in main.py
- [x] T020 [US3] Implement user feedback for status change operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Enable users to update task details

**Independent Test**: Can be fully tested by adding a task, updating it, and verifying the changes

### Implementation for User Story 4

- [x] T021 [US4] Implement update_task method in TodoManager class
- [x] T022 [US4] Add CLI command parsing for 'update' command in main.py
- [x] T023 [US4] Implement user input handling for update command
- [x] T024 [US4] Add confirmation message after task is updated

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Enable users to delete tasks by ID

**Independent Test**: Can be fully tested by adding a task, deleting it, and verifying it no longer appears in the list

### Implementation for User Story 5

- [x] T025 [US5] Implement delete_task method in TodoManager class
- [x] T026 [US5] Add CLI command parsing for 'delete' command in main.py
- [x] T027 [US5] Implement user feedback for deletion operations

---

## Phase 8: User Story 6 - Interactive CLI (Priority: P1)

**Goal**: Provide an interactive command-line interface

**Independent Test**: Can be fully tested by running the application and verifying all commands work as expected

### Implementation for User Story 6

- [x] T028 [US6] Implement main REPL loop in main.py
- [x] T029 [US6] Add 'help' command implementation
- [x] T030 [US6] Add 'exit' command implementation
- [x] T031 [US6] Implement error handling for invalid commands

---

## Phase 9: Error Handling and User Experience (Priority: P1)

**Goal**: Add robust error handling and improve user experience

- [x] T032 Implement error handling for invalid task IDs
- [x] T033 Implement error handling for invalid command formats
- [x] T034 Add helpful feedback messages for all operations
- [x] T035 Ensure app remains responsive and doesn't crash

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 [P] Documentation updates in README.md
- [x] T037 Code cleanup and refactoring
- [x] T038 Performance optimization across all stories
- [x] T039 [P] Additional unit tests (if requested) in tests/unit/
- [x] T040 Security hardening
- [x] T041 Run quickstart.md validation

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
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - Critical for all other stories to be usable

### Within Each User Story

- Core implementation before UI integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Stories 1, 2, and 6 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (List Tasks)
5. Complete Phase 8: User Story 6 (Interactive CLI)
6. **STOP and VALIDATE**: Test basic functionality independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 6 → Test independently → Deploy/Demo (Interactive app!)
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Add User Story 5 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 6
   - Developer D: User Stories 3, 4, 5
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
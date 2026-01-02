---

description: "Task list for Todo App Intermediate Features implementation"
---

# Tasks: Todo App Intermediate Features

**Input**: Design documents from `/specs/001-todo-intermediate-features/`
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

- [X] T001 Create src directory structure (main.py, todo.py, ui.py, storage.py)
- [X] T002 [P] Create requirements.txt with Python 3.13+ requirement
- [X] T003 [P] Create basic project files based on plan.md structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 [P] Create Task model with id, title, description, completed fields in src/todo.py
- [X] T005 [P] Create in-memory storage implementation in src/storage.py
- [X] T006 [P] Create basic CLI menu structure in src/main.py
- [X] T007 [P] Create basic UI functions in src/ui.py
- [X] T008 [P] Create input validation functions in src/ui.py
- [X] T009 [P] Create error handling functions in src/ui.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Enhanced Task Management with Priorities and Tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (High, Medium, Low) and tags to tasks, with visual indicators in the enhanced list view

**Independent Test**: Can be fully tested by adding tasks with different priority levels and tags, then viewing them in the enhanced list format to verify visual indicators are displayed correctly.

### Implementation for User Story 1

- [X] T010 [P] [US1] Extend Task model with priority and tags fields in src/todo.py
- [X] T011 [P] [US1] Update add_task function to accept priority and tags in src/todo.py
- [X] T012 [P] [US1] Update update_task function to modify priority and tags in src/todo.py
- [X] T013 [US1] Create enhanced display function with table formatting in src/ui.py
- [X] T014 [US1] Update CLI menu to prompt for priority during task creation in src/main.py
- [X] T015 [US1] Update CLI menu to prompt for tags during task creation in src/main.py
- [X] T016 [US1] Update CLI menu to allow priority/tag updates in src/main.py
- [X] T017 [US1] Implement visual indicators for priority levels (🔥, ⚡, ➖) in src/ui.py
- [X] T018 [US1] Implement tag display in enhanced view in src/ui.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search Tasks by Content (Priority: P2)

**Goal**: Enable users to search for specific tasks by keyword in title or description

**Independent Test**: Can be fully tested by adding multiple tasks with different content, then using the search functionality to find specific tasks by keywords in title or description.

### Implementation for User Story 2

- [X] T019 [P] [US2] Create search_tasks function in src/todo.py
- [X] T020 [US2] Implement case-insensitive keyword matching in src/todo.py
- [X] T021 [US2] Add search menu option to CLI in src/main.py
- [X] T022 [US2] Create search UI functions in src/ui.py
- [X] T023 [US2] Integrate search results with enhanced display from US1

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Filter and Sort Tasks (Priority: P3)

**Goal**: Enable users to filter tasks by status, priority, or tag, and sort them in different ways

**Independent Test**: Can be fully tested by filtering and sorting tasks in various combinations to verify that the displayed results match the selected criteria.

### Implementation for User Story 3

- [X] T024 [P] [US3] Create filter_tasks function in src/todo.py
- [X] T025 [P] [US3] Create sort_tasks function in src/todo.py
- [X] T026 [US3] Add filter menu option to CLI in src/main.py
- [X] T027 [US3] Add sort menu option to CLI in src/main.py
- [X] T028 [US3] Create filter UI functions in src/ui.py
- [X] T029 [US3] Create sort UI functions in src/ui.py
- [X] T030 [US3] Integrate filter/sort results with enhanced display from US1

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Enhanced Task View (Priority: P4)

**Goal**: Display tasks in a rich table format with all relevant information

**Independent Test**: Can be fully tested by adding tasks with various properties and verifying that the enhanced view displays all required information in a well-organized table format.

### Implementation for User Story 4

- [X] T031 [P] [US4] Enhance table formatting with fixed-width columns in src/ui.py
- [X] T032 [P] [US4] Implement description truncation for table display in src/ui.py
- [X] T033 [US4] Update all display functions to use enhanced view as default in src/main.py
- [X] T034 [US4] Ensure all existing functionality uses enhanced display in src/todo.py

**Checkpoint**: All user stories should now be integrated and working together

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T035 [P] Update README.md with new Intermediate features description and usage examples
- [X] T036 [P] Add input validation for all new features (priority, tags) in src/ui.py
- [X] T037 [P] Add error handling for edge cases in src/ui.py
- [X] T038 [P] Create demo script showing all Basic + Intermediate capabilities
- [X] T039 [P] Run quickstart.md validation to ensure all features work as described
- [X] T040 [P] Code cleanup and refactoring across all modules
- [X] T041 [P] Performance optimization for search, filter, and sort operations
- [X] T042 [P] Documentation updates in docstrings across all modules

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Depends on US1 (enhanced display) - builds upon US1's functionality

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
Task: "Extend Task model with priority and tags fields in src/todo.py"
Task: "Update add_task function to accept priority and tags in src/todo.py"
Task: "Update update_task function to modify priority and tags in src/todo.py"
Task: "Create enhanced display function with table formatting in src/ui.py"
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
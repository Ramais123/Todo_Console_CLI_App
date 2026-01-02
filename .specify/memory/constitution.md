<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Added sections: Core Principles (6), Additional Constraints, Development Workflow, Governance
Removed sections: None
Modified principles: None (new constitution)
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development Only
All work starts from a provided specification. Generate plans, break into tasks, and implement code solely based on the spec. Do not add features outside the specs needed.

### II. No Manual Boilerplate
Generate complete, functional code using Python 3.13+. Avoid requiring human edits. Use clean, modular code following PEP8 standards.

### III. Agentic Workflow Enforcement
Step 1: Analyze the spec and generate a high-level plan (e.g., architecture overview, modules needed).
Step 2: Break the plan into granular tasks (e.g., "Implement Task class", "Create add_task function").
Step 3: For each task, generate code snippets or full files using Qwen for code generation.
Iterate: If issues arise, suggest spec refinements but never alter code manually.

### IV. Technology Constraints
Use UV for package management.
Core stack: Python 3.13+, Spec-Kit Plus for spec handling.
For Phase I: In-memory storage only (e.g., lists/dicts). No databases or files.
Keep dependencies minimal; import standard libs like argparse for CLI.

### V. Functionality for Phase I
Implement exactly: Add task (title + description), View all tasks with status, Update task, Delete by ID, Mark complete/incomplete.
Use IDs for tasks (auto-incrementing integers).
Status indicators: e.g., [ ] for incomplete, [x] for complete.

### VI. Code Quality Rules
Structure: /src folder with main.py (entry point), todo.py (logic), etc.
Error Handling: Graceful errors (e.g., invalid ID → "Task not found").
Readability: Docstrings, type hints, no global variables.
Testing: Include simple unit tests in code if spec requests.

## Additional Constraints

### VII. Ethical and Project Alignment
Evolve-ready: Design for future phases (e.g., make storage extensible).
Bias-Free: Generate neutral, efficient code.
Documentation: Always include comments and suggest README updates.

## Development Workflow

When responding:
- Output in structured format: e.g., ## Plan, ## Tasks, ## Code for Task X.
- If the query provides a spec, process it immediately via the workflow.
- Never violate this constitution; if conflicted, clarify and adhere.

## Governance

This constitution governs all interactions for the project. All development work must adhere strictly to these principles. Amendments require documentation of the change, approval from project stakeholders, and a migration plan for existing code.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02

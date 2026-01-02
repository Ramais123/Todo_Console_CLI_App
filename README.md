# Evolution of Todo – Todo In-Memory Python Console App (Full Version)

**Hackathon Project**  
**Theme**: From CLI to Distributed Cloud-Native AI Systems  
**Current Phase**: Complete – Basic + Intermediate + Advanced Levels Implemented  

This repository contains a fully featured command-line Todo application built **entirely through spec-driven, AI-assisted development** using Spec-Kit Plus and Qwen — **zero manual coding**. The project demonstrates the progressive evolution of a simple script into a smart, intelligent CLI tool.

## Features

### Basic Level (Core MVP)
- Add tasks with title and description
- List all tasks with ID and status (✅/❌)
- Update task details
- Delete task by ID
- Mark as complete/incomplete

### Intermediate Level (Organization & Usability)
- Priorities: High (🔥), Medium (⚡), Low (➖)
- Multiple tags/categories per task (e.g., work, personal, health)
- Search tasks by keyword (title/description)
- Filter by status, priority, or tag
- Sort by priority, title, or status
- Rich, formatted table view

### Advanced Level (Intelligent Features)
- Due dates & time support (YYYY-MM-DD or YYYY-MM-DD HH:MM)
- Console-based reminders on startup:
  - 🔥 Overdue tasks
  - ⏰ Due today
  - Upcoming tasks (next 3 days)
- Recurring tasks (daily, weekly, monthly) with 🔁 indicator
- Auto-rescheduling: completing a recurring task creates a new instance with the next due date
- Auto-sorting by due date (soonest first), then priority

All data is stored **in-memory only** (lost on exit) as per Phase I requirements.

## Demo Screenshot Example
=== REMINDERS ===
🔥 OVERDUE: #3 Pay bills (Due: 2026-01-01)
⏰ DUE TODAY: #5 Team standup (Due: 2026-01-02 09:00)
ID | Priority | Title                | Tags            | Due          | Status/Recur | Description
1  | 🔥 High   | Finish report        | work, urgent    | 2026-01-05   | ❌           | Final Q4 summary
2  | ⚡ Medium | Gym                  | health          | 2026-01-03   | ❌ 🔁        | Weekly workout
...
text## Project Structure
.
├── constitution.md                  # AI agent constitution & progression rules
├── README.md                        # This file
├── pyproject.toml                   # UV configuration (optional)
├── specs_history/                   # All spec versions
│   ├── spec_basic.md
│   ├── spec_intermediate.md
│   ├── spec_advanced.md
│   └── ...
├── src/
│   ├── main.py                      # Entry point & CLI loop
│   ├── models.py                    # Task dataclass
│   ├── storage.py                   # In-memory manager
│   ├── ui.py                        # Display & input helpers
│   └── utils.py                     # Date handling & formatting
└── ...
text## Setup & Run

### Requirements
- Python 3.13+
- UV (recommended): https://docs.astral.sh/uv/

### Quick Start
```bash
git clone https://github.com/your-username/evolution-of-todo.git
cd evolution-of-todo

uv venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

python -m src.main
Explore the menu to experience all features — try creating recurring tasks and setting due dates to see auto-reminders and rescheduling!
Development Process

100% Spec-Driven: Every feature began with /sp.specify → /sp.plan → atomic tasks → AI code generation
No Manual Code: Entire codebase generated iteratively via Qwen
Clean & Modular: Type hints, docstrings, error handling, PEP 8 compliance

Future Evolution (Planned)

Persistent storage
Web/API interface
Cloud-native distributed system (Kubernetes)
Full AI-powered intelligence

Built for Hackathon II: Spec-Driven Development
Complete process (constitution, specs history, iterations) included for judging.

Made with ❤️ using AI as Product Architect

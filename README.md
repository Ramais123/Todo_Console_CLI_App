# Advanced Todo App

This is an advanced CLI-based todo application with intelligent features including recurring tasks and due date reminders.

## Features

- **Add Tasks**: Add new tasks with titles, descriptions, priorities, tags, due dates, and recurrence settings
- **View Tasks**: View all tasks with sorting by due date and priority
- **Update Tasks**: Update existing tasks with new information
- **Complete Tasks**: Mark tasks as complete; recurring tasks automatically generate new instances
- **Delete Tasks**: Remove tasks from the list
- **Due Date Reminders**: Tasks can have optional due dates with visual indicators for overdue tasks
- **Recurring Tasks**: Tasks can be set to recur daily, weekly, or monthly
- **Reminder System**: Displays overdue, due today, and upcoming tasks at startup and after key actions

## Getting Started

1. Run the application:
   ```bash
   python src/cli/main.py
   ```

2. Use the menu system to interact with your tasks

## Task Properties

- **ID**: Unique identifier for each task
- **Title**: The task title (required)
- **Description**: Optional detailed description
- **Priority**: High, Medium, or Low (default: Medium)
- **Tags**: Optional list of tags for categorization
- **Due Date**: Optional due date in YYYY-MM-DD HH:MM format
- **Recurrence**: none, daily, weekly, or monthly (default: none)
- **Status**: Completed (✅) or incomplete (⏳), with recurring indicator (🔁)

## Recurring Tasks

When you mark a recurring task as complete, the application automatically creates a new instance of the task with the next due date based on the recurrence interval:
- Daily: +1 day
- Weekly: +7 days
- Monthly: +30 days

## Due Date Reminders

The application provides visual reminders:
- 🔥 OVERDUE: Tasks past their due date
- ⏰ DUE TODAY: Tasks due today
- 📅 UPCOMING: Tasks due in the next 3 days

These reminders are displayed at application startup and after key actions (add, update, complete, delete).

## Technical Details

- Built with Python 3.13
- Uses only standard library modules
- In-memory storage (tasks are lost on exit)
- Modular architecture with separate models, services, and CLI layers
"""
User interface functions for the Todo application.
Handles input validation, display formatting, and user interaction.
"""
from typing import List, Optional
from todo import Task


def get_validated_input(prompt: str, validation_fn=None, error_msg: str = "Invalid input. Please try again."):
    """
    Get input from user with validation.

    Args:
        prompt: The input prompt to display
        validation_fn: Optional function to validate input
        error_msg: Error message to display for invalid input

    Returns:
        Validated user input
    """
    while True:
        user_input = input(prompt).strip()
        if validation_fn is None or validation_fn(user_input):
            return user_input
        else:
            print(error_msg)


def validate_priority(priority: str) -> bool:
    """
    Validate that the priority is one of the allowed values.

    Args:
        priority: The priority value to validate

    Returns:
        True if valid, False otherwise
    """
    return priority.lower() in ["high", "medium", "low"]


def validate_tags(tags_input: str) -> List[str]:
    """
    Validate and process tags input.

    Args:
        tags_input: Comma-separated tags string

    Returns:
        List of validated tags
    """
    if not tags_input.strip():
        return []
    
    tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]
    # Remove duplicates while preserving order
    unique_tags = []
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)
    return unique_tags


def display_task_table(tasks: List[Task]):
    """
    Display tasks in an enhanced table format with all relevant information.

    Args:
        tasks: List of tasks to display
    """
    if not tasks:
        print("No tasks found.")
        return

    # Define column widths
    id_width = 4
    priority_width = 10
    title_width = 20
    tags_width = 20
    status_width = 8
    description_width = 30

    # Print header
    print(f"{'ID':<{id_width}} {'Priority':<{priority_width}} {'Title':<{title_width}} {'Tags':<{tags_width}} {'Status':<{status_width}} {'Description':<{description_width}}")
    print("-" * (id_width + priority_width + title_width + tags_width + status_width + description_width + 5))

    # Print each task
    for task in tasks:
        # Get priority indicator
        priority_indicator = get_priority_indicator(task.priority)
        
        # Format tags
        tags_str = ", ".join(task.tags) if task.tags else "-"
        
        # Format status
        status_str = "[X]" if task.completed else "[ ]"
        
        # Truncate description if too long
        description = task.description[:description_width-3] + "..." if len(task.description) > description_width else task.description
        
        print(f"{task.id:<{id_width}} {priority_indicator:<{priority_width}} {task.title[:title_width]:<{title_width}} {tags_str:<{tags_width}} {status_str:<{status_width}} {description:<{description_width}}")


def get_priority_indicator(priority: str) -> str:
    """
    Get the visual indicator for a priority level.

    Args:
        priority: The priority level ("high", "medium", "low")

    Returns:
        Visual indicator for the priority
    """
    priority = priority.lower()
    if priority == "high":
        return "[H] High"
    elif priority == "medium":
        return "[M] Medium"
    elif priority == "low":
        return "[L] Low"
    else:
        return "[M] Medium"  # Default to medium


def display_search_results(tasks: List[Task], keyword: str):
    """
    Display search results in enhanced format.

    Args:
        tasks: List of matching tasks
        keyword: The search keyword
    """
    print(f"\nSearch results for '{keyword}':")
    display_task_table(tasks)


def display_filtered_tasks(tasks: List[Task], filter_type: str, filter_value: str):
    """
    Display filtered tasks in enhanced format.

    Args:
        tasks: List of filtered tasks
        filter_type: The type of filter applied
        filter_value: The value used for filtering
    """
    print(f"\nFiltered tasks by {filter_type} = {filter_value}:")
    display_task_table(tasks)


def display_sorted_tasks(tasks: List[Task], sort_type: str):
    """
    Display sorted tasks in enhanced format.

    Args:
        tasks: List of sorted tasks
        sort_type: The type of sorting applied
    """
    print(f"\nTasks sorted by {sort_type}:")
    display_task_table(tasks)


def truncate_text(text: str, max_length: int) -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: The text to truncate
        max_length: Maximum length of the text

    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."
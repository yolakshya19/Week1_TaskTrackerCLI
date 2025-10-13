from typing import List, Dict, Optional
from core.utils import load_tasks, save_tasks, now_iso, TASKS_FILE


# -- CRUD operations (business logic) --
def add_task(description: str, filename: str = TASKS_FILE) -> Dict:
    """
    Add a new task with `description`.
    - Loads tasks from file, appends new task, saves file.
    - New task fields:
        - description (str)
        - created_at (ISO timestamp)
        - completed (False)
        - completed_at (None)
    - Returns the created task dict.
    - Validate: description must be non-empty; otherwise raise ValueError.
    """
    if not description:
        return "Description can not be empty"
    tasks = load_tasks(filename)

    task = {
        "description": description,
        "created_at": now_iso(),
        "completed": False,
        "completed_at": None,
    }
    tasks.append(task)
    save_tasks(tasks, TASKS_FILE)
    return task


def list_tasks(filename: str = TASKS_FILE) -> List[Dict]:
    """
    Return the current list of tasks (loaded from file).
    - Should not mutate file.
    - Useful to return list so CLI/other logic handles presentation.
    """
    tasks = load_tasks(TASKS_FILE)
    return tasks


def mark_complete(task_index: int, filename: str = TASKS_FILE) -> Dict:
    """
    Mark the task at 1-based `task_index` as completed.
    - Loads tasks, validate index in range (1..len(tasks)): if invalid, raise IndexError.
    - If already completed, leave `completed_at` unchanged (or update — document choice).
    - Set `completed` True and `completed_at` to current ISO timestamp.
    - Save tasks and return the updated task dict.
    """
    tasks = load_tasks(filename)
    if task_index < 1 or task_index > len(tasks):
        return "IndexError"
    if tasks[task_index - 1]["completed"] == True:
        return "Task already completed"

    tasks[task_index - 1]["completed"] = True
    tasks[task_index - 1]["completed_at"] = now_iso()

    save_tasks(tasks, filename)

    return tasks[task_index - 1]


def delete_task(task_index: int, filename: str = TASKS_FILE) -> Dict:
    """
    Delete the task at 1-based `task_index`.
    - Loads tasks, validate index; if invalid, raise IndexError.
    - Remove the task from list, save tasks.
    - Return the deleted task dict (so caller can show confirmation).
    """
    tasks = load_tasks(filename)
    if task_index < 1 or task_index > len(tasks):
        return "IndexError"

    deleted_task = tasks[task_index - 1]

    tasks.pop(task_index - 1)

    save_tasks(tasks, TASKS_FILE)

    return deleted_task


# -- Optional / convenience utilities --
def update_task_description(
    task_index: int, new_description: str, filename: str = TASKS_FILE
) -> Dict:
    """
    Update the description of a task.
    - Validate description is non-empty.
    - Validate index.
    - Save and return updated task.
    """
    if not new_description:
        return "Description can not be empty"
    tasks = load_tasks(TASKS_FILE)
    if task_index < 1 or task_index > len(tasks):
        return "IndexError"

    tasks[task_index - 1]["description"] = new_description

    save_tasks(tasks, TASKS_FILE)
    return "Updated successfully"


def clear_completed(filename: str = TASKS_FILE) -> int:
    """
    Remove all tasks with completed == True.
    - Return the number of removed tasks.
    - Save tasks after deletion.
    """


def reorder_tasks(old_index: int, new_index: int, filename: str = TASKS_FILE) -> None:
    """
    Move task from old 1-based index to new 1-based index.
    - Validate indices (both within range).
    - Save tasks after reordering.
    """

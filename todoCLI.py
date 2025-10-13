from datetime import datetime
import json
from typing import List, Dict, Optional

# -- Config / helper (interface) --
TASKS_FILE: str = "tasks.json"


def now_iso() -> str:
    """
    Return the current timestamp as an ISO-formatted string.
    Used when creating/completing tasks.
    """
    return datetime.now().isoformat(timespec="seconds")


# -- Persistence API --
def load_tasks(filename: str = TASKS_FILE) -> List[Dict]:
    """
    Load and return the list of tasks from `filename`.
    - If file does not exist, return an empty list.
    - If file exists but JSON is invalid, raise a ValueError or return [] (choose and document).
    - Each task should be a dict with at least:
        {
          "description": str,
          "created_at": str,   # ISO timestamp
          "completed": bool,
          "completed_at": Optional[str]  # ISO timestamp or None
        }
    """
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Error in opening file - {e}")
        return []


def save_tasks(tasks: List[Dict], filename: str = TASKS_FILE) -> None:
    """
    Persist `tasks` to `filename` atomically if possible.
    - Should write JSON with indentation (human-readable).
    - Should raise IOError on unrecoverable write errors.
    """
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)


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


# -- CLI hook (thin wrapper) --
def run_cli(filename: str = TASKS_FILE) -> None:
    """
    Run a simple read-eval-print loop using the functions above.
    - Accept commands: add, list, done, del, exit (or similar).
    - The CLI should call list_tasks() and the other functions; it should not directly read/write files.
    - Keep CLI responsibilities: parsing, user prompts, printing success/failure.
    """
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

        choice = input("Enter your choice (1-5):")

        match choice:
            case "1":
                description = input("Enter the task description: ")
                print(add_task(description, TASKS_FILE))
            case "2":
                tasks = list_tasks(TASKS_FILE)
                if not tasks:
                    print("No tasks yet.")
                else:
                    for i, t in enumerate(tasks, start=1):
                        status = "✅" if t["completed"] else "❌"
                        print(
                            f"{i}. {t['description']} ({status})  -  Created: {t['created_at']}"
                        )

            case "3":
                tasks = list_tasks(TASKS_FILE)
                if not tasks:
                    print("No tasks yet.")
                else:
                    for i, t in enumerate(tasks, start=1):
                        status = "✅" if t["completed"] else "❌"
                        print(
                            f"{i}. {t['description']} ({status})  -  Created: {t['created_at']}"
                        )
                index = int(input("Enter the completed task index: "))
                print(mark_complete(index, TASKS_FILE))
            case "4":
                tasks = list_tasks(TASKS_FILE)
                if not tasks:
                    print("No tasks yet.")
                else:
                    for i, t in enumerate(tasks, start=1):
                        status = "✅" if t["completed"] else "❌"
                        print(
                            f"{i}. {t['description']} ({status})  -  Created: {t['created_at']}"
                        )
                index = int(input("Enter the task index to be deleted: "))
                print(delete_task(index, TASKS_FILE))
            case "5":
                tasks = list_tasks(TASKS_FILE)
                if not tasks:
                    print("No tasks yet.")
                else:
                    for i, t in enumerate(tasks, start=1):
                        status = "✅" if t["completed"] else "❌"
                        print(
                            f"{i}. {t['description']} ({status})  -  Created: {t['created_at']}"
                        )
                index = int(input("Enter the task index to be updated: "))
                newDescp = input("Enter the new description: ")
                print(update_task_description(index, newDescp, TASKS_FILE))
            case "6":
                break


run_cli()

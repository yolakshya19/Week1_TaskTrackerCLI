from typing import List, Dict, Optional
import json
from datetime import datetime
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "..", "tasks.json")


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

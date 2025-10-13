from core.tasks import (
    add_task,
    list_tasks,
    mark_complete,
    delete_task,
    update_task_description,
)
from core.utils import TASKS_FILE


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

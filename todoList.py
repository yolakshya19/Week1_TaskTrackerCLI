tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice (1-4):")

    match choice:
        case "1":
            task = input("Enter the task: ")
            if task in tasks:
                print(f"{task} : is already present in the to-do")
            else:
                tasks.append(task)
        case "2":
            if len(tasks) == 0:
                print("No tasks yet")
            else:
                c = 1
                for task in tasks:
                    print(f"{c}. {task}")
                    c += 1
        case "3":
            c = 1
            for task in tasks:
                print(f"{c}. {task}")
                c += 1
            task = input("enter the completed task: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print(f'{task} : is not in the to-do')
        case "4":
            print("Let's Conquer The Day")
            break

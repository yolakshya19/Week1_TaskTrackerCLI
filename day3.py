def sum2(a, b):
    return a + b


# print(sum2(10,2))


def sumMany(*nums):
    result = 0
    for num in nums:
        result += num

    return result


# print(sumMany(2,5,78))


def fullName(first_name: str, last_name: str, uppercase=False):
    if uppercase == True:
        last_name = last_name.upper()
        first_name = first_name.upper()
    return f"{last_name},{first_name}"


# print(fullName("Lakshya", "Dhawan", True))

# Task Manager
tasks = []


def add_tasks(tasks: list, task):
    tasks.append(task)
    # return tasks


def list_tasks(tasks: list):
    if len(tasks) == 0:
        print("No Tasks Added Yet, Start Working!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def remove_tasks(tasks: list, index):
    # for task, i in enumerate(tasks, 1):
    #     print(f"{i}. {task}")
    # index = input("Which task to delete, enter the number: ")
    tasks.pop(index - 1)
    list_tasks(tasks)


# add_tasks(tasks, "Learn Python")
# add_tasks(tasks, "Do Office")
# add_tasks(tasks, "Go Gym")
# add_tasks(tasks, "Read Book")
# list_tasks(tasks)
# remove_tasks(tasks, 3)


def write_note(note: str):
    with open("notes.txt", "a") as f:
        f.write(note)


def read_notes():
    with open("notes.txt", "r") as f:
        print(f.read())


# write_note("\nHi, this is the 1st note!")
# write_note("\nHi, this is the 2nd note!")
# write_note("\nHi, this is the 3rd note!")
# read_notes()
import json

profile = {
    "name": "Lakshya",
    "age": 22,
    "interests": ["cricket", "f1", "neuroscience"],
}

with open("profile.json", "w") as file:
    json.dump(profile, file)


def load_profile(filename):
    # returns Python dict from JSON
    with open(filename, "r") as f:
        profile = json.load(f)
    print(profile)


load_profile("profile.json")


def update_profile(filename, key, value):
    # modifies JSON file
    with open(filename, "r") as f:
        profile = json.load(f)

    profile[key] = value

    with open(filename, "w") as f:
        json.dump(profile, f)


update_profile("profile.json", "age", 43)
load_profile("profile.json")
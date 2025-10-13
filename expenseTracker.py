expenses = {}

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add/Update Expense")
    print("2. View Category-wise Expenses")
    print("3. Delete Expense")
    print("4. Calculate Total Expense")
    print("5. Exit")
    print("6. View all expenses")

    choice = input("Choose an option (1-6): ")

    match choice:
        case "1":
            category = input("Enter expense category (e.g., Food, Transport): ")
            amount = float(input("Enter expense amount: "))
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
        case "2":
            category = input("Enter the category: ")
            if category in expenses:
                print(expenses[category])
            else:
                print("Category does not exist")
        case "3":
            category = input("Enter expense category (e.g., Food, Transport): ")
            if category in expenses:
                amount = float(input("Enter expense amount: "))
                expenses[category] -= amount
                if expenses[category] <= 0:
                    del expenses[category]
            else:
                print("Category does not exist")
        case "4":
            total = 0
            for x in expenses.values():
                total += x
            print("Total expenses:", total)
        case "5":
            break
        case "6":
            for cat, amt in expenses.items():
                print(f'{cat}: {amt}')
        case _:
            print("Choose from the available options:")

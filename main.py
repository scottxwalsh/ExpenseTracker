while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add Expense
        pass
    elif choice == "2":
        # View Expenses
        pass
    elif choice == "3":
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please try again.")

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description")
    date = input("Enter date (YYYY-MM-DD): ")
    expense = {'amount': amount, 'category': category, 'description': description, 'date': date}
    expenses.append(expense)

def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']} - {expense['description']} - {expense['amount']}")

expenses = []
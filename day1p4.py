import os

def get_total(expenses):
    return sum(expenses)


def get_average(expenses):
    return sum(expenses) / len(expenses)


def get_max(expenses):
    return max(expenses)

filename = "expenses.txt"
expenses = []

if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                expenses.append(float(line))
            except ValueError:
                print(f"Skipping invalid line in {filename}: {line}")
    print(f"Loaded {len(expenses)} existing expense(s) from {filename}.")

new_expenses = []
while True:
    expense = input("Enter an expense (or 'done' to finish): ")
    if expense.lower() == 'done':
        break
    try:
        new_expenses.append(float(expense))
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

if new_expenses:
    with open(filename, "a") as file:
        for expense in new_expenses:
            file.write(f"{expense}\n")
    expenses.extend(new_expenses)
    print(f"Saved {len(new_expenses)} new expense(s) to {filename}.")
else:
    print("No new expenses entered.")

print("\nExpenses read from file:")
with open(filename, "r") as file:
    for line in file:
        print(f"${float(line.strip()):.2f}")




if not expenses:
    print("No expenses entered.")
else:
    print("========= Expenses Summary =========")
    print(f"Total Expenses: ${get_total(expenses):.2f}")
    print(f"Average Expense: ${get_average(expenses):.2f}")
    print(f"Maximum Expense: ${get_max(expenses):.2f}")
    print("====================================")
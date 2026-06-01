#practice number 4
expenses = []

while True:
    expense = input("Enter an expense (or 'done' to finish): ")
    if expense.lower() == 'done':
        break
    try:
        expenses.append(float(expense))
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

def get_total(expenses):
    return sum(expenses)

def get_average(expenses):
    return sum(expenses) / len(expenses)

def get_max(expenses):
    return max(expenses)

print("========= Expenses Summary =========")
print(f"Total Expenses: ${get_total(expenses):.2f}")
print(f"Average Expense: ${get_average(expenses):.2f}")
print(f"Maximum Expense: ${get_max(expenses):.2f}")
print("====================================")

# # 

# import os

# # Expense Tracker Class
# class ExpenseTracker:
#     def _init_(self):
#         self.expenses = []

#     # Add an expense
#     def add_expense(self, date, category, amount, description):
#         expense = {
#             "Date": date,
#             "Category": category,
#             "Amount": amount,
#             "Description": description
#         }
#         self.expenses.append(expense)
#         print("Expense added successfully.")

#     # View all expenses
#     def view_expenses(self):
#         if not self.expenses:
#             print("No expenses recorded yet.")
#             return
        
#         print("\n--- All Expenses ---")
#         for i, expense in enumerate(self.expenses, start=1):
#             print(f"{i}. Date: {expense['Date']}, Category: {expense['Category']}, "
#                   f"Amount: ${expense['Amount']}, Description: {expense['Description']}")

#     # Write expenses to a file
#     def write_to_file(self, filename="expenses.txt"):
#         if not self.expenses:
#             print("No expenses to write to file.")
#             return

#         with open(filename, "w") as file:
#             for expense in self.expenses:
#                 file.write(f"Date: {expense['Date']}, Category: {expense['Category']}, "
#                            f"Amount: ${expense['Amount']}, Description: {expense['Description']}\n")
#         print(f"Expenses written to file '{filename}' successfully.")


# # Main Program
# def main():
#     tracker = ExpenseTracker()

#     while True:
#         print("\n--- Expense Tracker ---")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Write Expenses to File")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             date = input("Enter date (YYYY-MM-DD): ")
#             category = input("Enter category (e.g., Food, Transport, etc.): ")
#             amount = float(input("Enter amount: "))
#             description = input("Enter description: ")
#             tracker.add_expense(date, category, amount, description)
#         elif choice == "2":
#             tracker.view_expenses()
#         elif choice == "3":
#             filename = input("Enter filename to save expenses (default: expenses.txt): ")
#             if not filename:
#                 filename = "expenses.txt"
#             tracker.write_to_file(filename)
#         elif choice == "4":
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Run the program
# if __name__ == "_main_":
#     main()

# def expense_tracker():
#     expenses = {}

#     while True:
#         category = input ("enter expense category(type 'quit'to exit):").lower()
#         if category == "quit":
#             break
#         amount = float(input("enter expense amount:"))
#         if category in expenses:
#             expenses[category] += amount
#         else:
#             expenses[category == amount]
#     print("expenses:")
#     for category , amount in expenses.items():
#         print(f'{category.capitalize()}:${amount:.2f}')

# expense_tracker()


import os

# File where expenses will be saved
FILE_NAME = "expenses.txt"

# Function to add a new expense
def add_expense():
    print("Add a new expense")
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category of the expense (e.g., Food, Transport): ")

    # Create a formatted expense record
    expense_record = f"Description: {description}, Amount: ${amount:.2f}, Category: {category}\n"

    # Write the expense to the file
    with open(FILE_NAME, "a") as file:
        file.write(expense_record)

    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if os.path.exists(FILE_NAME):
        print("Current Expenses:")
        with open(FILE_NAME, "r") as file:
            content = file.readlines()
            if content:
                for line in content:
                    print(line.strip())
            else:
                print("No expenses recorded yet.")
    else:
        print("No expense records found.")

    print()

# Function to write expenses to the file (This would typically be used for saving or exporting)
def write_expenses_to_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            content = file.readlines()
            if content:
                with open("backup_expenses.txt", "w") as backup_file:
                    backup_file.writelines(content)
                print("Expenses have been backed up to 'backup_expenses.txt'.")
            else:
                print("No expenses to back up.")
    else:
        print("No expense records found to write.")

# Function to display the menu
def display_menu():
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Write Expenses to File")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            write_expenses_to_file()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

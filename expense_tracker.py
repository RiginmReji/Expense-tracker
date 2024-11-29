

import os


FILE_NAME = "expenses.txt"


def add_expense():
    print("Add a new expense")
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category of the expense (e.g., Food, Transport): ")


    expense_record = f"Description: {description}, Amount: ${amount:.2f}, Category: {category}\n"

  
    with open(FILE_NAME, "a") as file:
        file.write(expense_record)

    print("Expense added successfully!\n")


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

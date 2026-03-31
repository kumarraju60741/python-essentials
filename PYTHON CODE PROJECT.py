import sys

def main():
    print("--- Python Essentials: Expense Tracker ---")
    
    try:
        budget = float(input("Enter your monthly budget: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    expenses = []
    
    while True:
        print("\n1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            item = input("Enter item name: ")
            amount = float(input(f"Enter amount for {item}: "))
            expenses.append({"item": item, "amount": amount})
            print(f"Added {item} successfully.")

        elif choice == '2':
            total = sum(e['amount'] for e in expenses)
            print("\n--- Expense Summary ---")
            for e in expenses:
                print(f"- {e['item']}: ${e['amount']}")
            print(f"Total Spent: ${total}")
            print(f"Budget Remaining: ${budget - total}")
            
            if total > budget:
                print(" WARNING: You have exceeded your budget!")
            else:
                print("You are within your budget.")

        elif choice == '3':
            print("Exiting tracker. Stay financially literate!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
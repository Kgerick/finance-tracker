transactions = []

def add_transaction():
    print("\n==== Add Transaction ====")
    date = input("Date (YYYY-DD-MM): ")
    category = input("Category (e.g. Groceries, Rent, Gas)")

    while True:
        amount_str = input("Amount (e.g. 123.43, 25.66, 12.99)")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("That isnt a valid number.")

    description = input("Short Description: ")

    transaction = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }

    transactions.append(transaction)

    print("\n Transaction added!")

def show_menu():
    print("\n==== Finance Tracker ====")
    print("1) Add transaction")
    print("2) View all transactions")
    print("3) View Summary")
    print("4) Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            print("You chose: View all transactions")
        elif choice == "3":
            print("You chose: View Summary")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    main()

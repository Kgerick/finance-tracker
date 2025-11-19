import json
import os

transactions = []

def save_transactions():
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

def load_transactions():
    if not os.path.exists("transactions.json"):
        return

    with open("transactions.json", "r") as f:
        data = json.load(f)

    transactions.extend(data)



def show_menu():
    print("\n==== Finance Tracker ====")
    print("1) Add transaction")
    print("2) View all transactions")
    print("3) View Summary")
    print("4) Exit")

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


def list_transactions():
    print("\n==== All Transactions ====")

    if not transactions:
        print("No transactions yet.")
        return
    
    for index, tx in enumerate(transactions, start=1):
        print(f"{index}. {tx['date']} | {tx['category']} | ${tx['amount']:.2f} | {tx['description']}")


def show_summary():
    print("\n==== Summary ====")

    if not transactions:
        print("No transactions yet")
        return
    
    total = 0
    for tx in transactions:
        total += tx["amount"]

    count = len(transactions)
    average = total / count

    print(f"Number of transactions: {count}")
    print(f"Total spent: ${total:.2f}")
    print(f"Average transaction: ${average:.2f}")


def main():
    load_transactions()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            save_transactions()
            print("Saved. Goodbye.")
            break
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    main()

from dataclasses import dataclass

@dataclass
class Transaction:
    date: str
    category: str
    amount: float
    description: str

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

    transaction = Transaction(
        date=date,
        category=category,
        amount=amount,
        description=description
    )

    transactions.append(transaction)

    print("\n Transaction added!")


def list_transactions():
    print("\n==== All Transactions ====")

    if not transactions:
        print("No transactions yet.")
        return
    
    for index, tx in enumerate(transactions, start=1):
        print(f"{index}. {tx.date} | {tx.category} | ${tx.amount:.2f} | {tx.description}")


def show_summary():
    print("\n==== Summary ====")

    if not transactions:
        print("No transactions yet")
        return
    
    total = 0
    for tx in transactions:
        total += tx.amount

    count = len(transactions)
    average = total / count

    print(f"Number of transactions: {count}")
    print(f"Total spent: ${total:.2f}")
    print(f"Average transaction: ${average:.2f}")
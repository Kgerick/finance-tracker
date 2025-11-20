import json
import os
from transactions import transactions, Transaction

def save_transactions():
    data = [tx.__dict__ for tx in transactions]

    with open("transactions.json", "w") as f:
        json.dump(data, f, indent=4)

def load_transactions():
    if not os.path.exists("transactions.json"):
        return

    try:
        with open("transactions.json", "r") as f:
            data = json.load(f)

        for item in data:
            tx = Transaction(
                date=item["date"],
                category=item["category"],
                amount=item["amount"],
                description=item["description"]
            )

        transactions.append(tx)

    except Exception as e:
        print("Could not load saved transactions")
        print("Reason: ", e)
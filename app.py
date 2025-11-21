from flask import Flask, jsonify, request
from transactions import (
    Transaction, 
    transactions,
    get_transaction_count,
    delete_transaction_by_index,
    update_transaction_by_index
)
from storage import load_transactions, save_transactions

app = Flask(__name__)

load_transactions()

@app.get("/transactions")
def get_transactions():
    data = [tx.__dict__ for tx in transactions]
    return jsonify(data)

@app.post("/transactions")
def create_transaction():
    body = request.get_json()

    required_fields = ["date", "category", "amount", "description"]
    for field in required_fields:
        if field not in body:
            return jsonify({"error": f"Missing field: {field}"})
        
    tx = Transaction(
        date=body["date"],
        category=body["category"],
        amount=float(body["amount"]),
        description=body["description"]
    )

    transactions.append(tx)
    save_transactions()

    return jsonify({"status": "ok"}), 201

@app.get("/summary")
def get_summary():
    if not transactions:
        return jsonify({
            "count": 0,
            "total": 0.0,
            "average": 0.0
        })
    
    total = sum(tx.amount for tx in transactions)
    count = len(transactions)
    average = total / count

    return jsonify({
        "count": count,
        "total": total,
        "average": average
    })

if __name__ == "__main__":
    app.run(debug=True)

@app.delete("/transactions/<int:index>")
def delete_transaction(index: int):
    deleted = delete_transaction_by_index(index)

    if not deleted:
        return jsonify({"error": "Transaction not found"}), 404
    
    save_transactions()
    return jsonify({"status": "deleted"}), 200

@app.patch("/transactions/<int:index>")
def update_transactions(index: int):
    body = request.get_json() or {}

    date = body.get("date")
    category = body.get("category")
    amount = body.get("amount")
    description = body.get("description")

    if amount is not None:
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"error": "Invalid amount"}), 400
        
    updated = update_transaction_by_index(
        index = index,
        date = date,
        category = category,
        amount = amount,
        description = description
    )

    if not updated:
        return jsonify({"error": "Transaction not found"}), 404
    
    save_transactions()
    return jsonify({"status": "updated"}), 200

@app.get("/summary/by-category")
def summary_by_category():
    if not transactions:
        return jsonify({})
    
    totals: dict[str, float] = {}

    for tx in transactions:
        totals[tx.category] = totals.get(tx.category, 0.0) + tx.amount

    return jsonify(totals)
# health check route to check if the app is running
from flask import Blueprint, jsonify, request
from database import get_connection



expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    amount = data.get("amount")
    category = data.get("category")
    description = data.get("description", "")
    date = data.get("date")

    if not amount or not category or not date:
        return jsonify({"error": "amount, category and date are required"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, date)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Expense added", "id": new_id}), 201
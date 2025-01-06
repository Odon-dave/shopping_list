from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "shopping_list.db"



def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 1
            )
        """)
        conn.commit()

@app.route("/items", methods=["GET"])
def get_items():
    """Retrieve all items in the shopping list."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shopping_list")
        items = cursor.fetchall()
        return jsonify(items)


@app.route("/items", methods=["POST"])
def create_item():
    """Add a new item to the shopping list."""
    data = request.json
    item_name = data.get("item_name")
    quantity = data.get("quantity", 1)

    if not item_name:
        return jsonify({"error": "Item name is required"}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO shopping_list (item_name, quantity) VALUES (?, ?)",
            (item_name, quantity),
        )
        conn.commit()
        return jsonify({"message": "Item added successfully"}), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """Update an item in the shopping list."""
    data = request.json
    item_name = data.get("item_name")
    quantity = data.get("quantity")

    if not item_name and quantity is None:
        return jsonify({"error": "No fields to update"}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        if item_name:
            cursor.execute(
                "UPDATE shopping_list SET item_name = ? WHERE id = ?", (item_name, item_id)
            )
        if quantity is not None:
            cursor.execute(
                "UPDATE shopping_list SET quantity = ? WHERE id = ?", (quantity, item_id)
            )
        conn.commit()
        return jsonify({"message": "Item updated successfully"})


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete an item from the shopping list."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM shopping_list WHERE id = ?", (item_id,))
        conn.commit()
        return jsonify({"message": "Item deleted successfully"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

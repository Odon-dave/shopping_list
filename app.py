from flask import Flask, request, jsonify
import sqlite3

# Configuration
DATABASE = "shopping_list.db"
DEBUG_MODE = True

app = Flask(__name__)
app.config["DEBUG"] = DEBUG_MODE


def get_db_connection():
    """Creates and returns a new database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enables dict-like cursor behavior
    return conn


def init_db():
    """Initialize the SQLite database."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 1
            )
        """)
        conn.commit()


@app.errorhandler(404)
def not_found_error(e):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


@app.route("/items", methods=["GET"])
def get_items():
    """Retrieve all items in the shopping list."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM shopping_list")
            items = cursor.fetchall()
            return jsonify([dict(item) for item in items])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/items", methods=["POST"])
def create_item():
    """Add a new item to the shopping list."""
    try:
        data = request.get_json()
        item_name = data.get("item_name")
        quantity = data.get("quantity", 1)

        if not item_name:
            return jsonify({"error": "Item name is required"}), 400

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO shopping_list (item_name, quantity) VALUES (?, ?)",
                (item_name, quantity),
            )
            conn.commit()
            return jsonify({"message": "Item added successfully", "id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """Update an item in the shopping list."""
    try:
        data = request.get_json()
        item_name = data.get("item_name")
        quantity = data.get("quantity")

        if not item_name and quantity is None:
            return jsonify({"error": "No fields to update"}), 400

        with get_db_connection() as conn:
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

            if cursor.rowcount == 0:
                return jsonify({"error": "Item not found"}), 404

            return jsonify({"message": "Item updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete an item from the shopping list."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM shopping_list WHERE id = ?", (item_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Item not found"}), 404

            return jsonify({"message": "Item deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/items/<int:item_id>", methods=["GET"])
def get_single_item(item_id):
    """Retrieve a single item by ID."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM shopping_list WHERE id = ?", (item_id,))
            item = cursor.fetchone()

            if not item:
                return jsonify({"error": "Item not found"}), 404

            return jsonify(dict(item))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    init_db()
    app.run()

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

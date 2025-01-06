from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "shopping_list.db"
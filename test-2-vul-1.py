import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    # 🚨 Vulnerable: unsanitized input in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)  # CodeQL will flag this
    result = cursor.fetchall()

    return {"result": result}

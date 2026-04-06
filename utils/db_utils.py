import os
import sqlite3

DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "bank.db")


def init_db():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT
    )
    """)

    conn.commit()
    conn.close()


# ✅ ADD THIS FUNCTION
def add_admin(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO admins (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()


# ✅ ADD THIS FUNCTION
def login_admin(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM admins WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()

    return result


# ✅ ADD THIS FUNCTION
def save_question(question):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO questions (question) VALUES (?)",
        (question,)
    )

    conn.commit()
    conn.close()
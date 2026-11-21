from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent / "history.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS calc_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expressions TEXT NOT NULL,
                result TEXT
            )
            """
        )
        conn.commit()


def save_history(expressions, result):
    expr_text = str(expressions).strip()
    if not expr_text or result is None or str(result) == "Error":
        return

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO calc_history (expressions, result) VALUES (?, ?)",
            (expr_text, str(result)),
        )
        conn.commit()



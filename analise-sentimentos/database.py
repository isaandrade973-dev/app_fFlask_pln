import sqlite3
from typing import List, Tuple

DB_NAME = "comments.db"

def init_db():
    """Inicializa a tabela de comentários se não existir."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                sentiment TEXT NOT NULL,
                score REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_comment(text: str, sentiment: str, score: float):
    """Insere um novo comentário e seu resultado analisado no banco."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO comments (text, sentiment, score) VALUES (?, ?, ?)",
            (text, sentiment, score)
        )
        conn.commit()

def get_all_comments() -> List[Tuple]:
    """Recupera todos os comentários salvos, ordenados do mais recente para o mais antigo."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, text, sentiment, score, created_at FROM comments ORDER BY created_at DESC"
        )
        return cursor.fetchall()
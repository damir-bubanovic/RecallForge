from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "recallforge.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subfolders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
                UNIQUE(subject_id, name)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subfolder_id INTEGER NOT NULL,
                question_text TEXT NOT NULL,
                answer_text TEXT NOT NULL,
                question_image_path TEXT,
                answer_image_path TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (subfolder_id) REFERENCES subfolders(id) ON DELETE CASCADE
            )
        """)

        connection.commit()



def create_subject(name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subject name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO subjects (name)
            VALUES (?)
            """,
            (cleaned_name,)
        )
        connection.commit()

        return cursor.lastrowid


def get_subjects():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id, name, created_at, updated_at
            FROM subjects
            ORDER BY name ASC
            """
        )

        return cursor.fetchall()


def update_subject(subject_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subject name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE subjects
            SET name = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (cleaned_name, subject_id)
        )
        connection.commit()

        return cursor.rowcount


def delete_subject(subject_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (subject_id,)
        )
        connection.commit()

        return cursor.rowcount
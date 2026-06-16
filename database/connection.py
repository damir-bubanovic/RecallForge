from pathlib import Path
import sqlite3


APP_NAME = "RecallForge"
DATA_DIR = Path.home() / ".local" / "share" / APP_NAME
DB_PATH = DATA_DIR / "recallforge.db"


def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection
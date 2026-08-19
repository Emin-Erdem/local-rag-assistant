import sqlite3
from contextlib import contextmanager
from typing import Generator
from config.settings import DATABASE_PATH


@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """SQLite veritabanı bağlantısı oluşturan ve yöneten context manager."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Kolonlara isimleriyle erişebilmek için
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
from database.connection import get_db_connection

CREATE_DOCUMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS document_chunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_INDEX_SOURCE = """
CREATE INDEX IF NOT EXISTS idx_source_file ON document_chunks(source_file);
"""


def init_db() -> None:
    """Gerekli tabloları ve indeksleri başlatır."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_DOCUMENTS_TABLE)
        cursor.execute(CREATE_INDEX_SOURCE)
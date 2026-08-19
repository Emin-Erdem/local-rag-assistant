import json
from typing import Any, Dict, List
from database.connection import get_db_connection


class DocumentStore:
    """Doküman parçalarını ve embedding'leri yöneten veri tabanı deposu."""

    @staticmethod
    def insert_chunk(
        source_file: str,
        chunk_index: int,
        content: str,
        embedding: List[float],
    ) -> int:
        """Tek bir chunk ve embedding'ini kaydeder."""
        embedding_json = json.dumps(embedding)
        query = """
        INSERT INTO document_chunks (source_file, chunk_index, content, embedding)
        VALUES (?, ?, ?, ?);
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                query, (source_file, chunk_index, content, embedding_json)
            )
            return cursor.lastrowid

    @staticmethod
    def get_all_chunks() -> List[Dict[str, Any]]:
        """Tüm kayıtlı chunk'ları ve embedding vektörlerini getirir."""
        query = "SELECT id, source_file, chunk_index, content, embedding FROM document_chunks;"
        with get_db_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(query).fetchall()
            return [
                {
                    "id": row["id"],
                    "source_file": row["source_file"],
                    "chunk_index": row["chunk_index"],
                    "content": row["content"],
                    "embedding": json.loads(row["embedding"]),
                }
                for row in rows
            ]

    @staticmethod
    def clear_all() -> None:
        """Tüm doküman tablosunu sıfırlar."""
        with get_db_connection() as conn:
            conn.cursor().execute("DELETE FROM document_chunks;")
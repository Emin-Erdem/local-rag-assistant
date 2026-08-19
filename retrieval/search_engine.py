from typing import Any, Dict, List
from config.model_config import model_settings
from core.embedding_service import EmbeddingService
from database.document_store import DocumentStore
from retrieval.vector_math import cosine_similarity


class VectorSearchEngine:
    """Veritabanı üzerinde semantik benzerlik araması yapan motor."""

    def __init__(self, embedding_service: EmbeddingService = None):
        self.embedding_service = embedding_service or EmbeddingService()

    def search(
        self,
        query: str,
        top_k: int = model_settings.TOP_K_RESULTS,
        threshold: float = model_settings.SIMILARITY_THRESHOLD,
    ) -> List[Dict[str, Any]]:
        """Kullanıcı sorgusuna en yakın doküman parçalarını döndürür."""
        query_vector = self.embedding_service.get_embedding(query)
        if not query_vector:
            return []

        all_chunks = DocumentStore.get_all_chunks()
        scored_chunks = []

        for chunk in all_chunks:
            score = cosine_similarity(query_vector, chunk["embedding"])
            if score >= threshold:
                scored_chunks.append({
                    "id": chunk["id"],
                    "source_file": chunk["source_file"],
                    "chunk_index": chunk["chunk_index"],
                    "content": chunk["content"],
                    "score": round(score, 4),
                })

        # Skora göre büyükten küçüğe sırala ve top_k kadarını al
        scored_chunks.sort(key=lambda item: item["score"], reverse=True)
        return scored_chunks[:top_k]
from typing import Dict
from core.embedding_service import EmbeddingService
from database.document_store import DocumentStore
from database.schema import init_db
from ingestion.chunker import TextChunker
from ingestion.file_loader import FileLoader


class IngestionPipeline:
    """Doküman yükleme, parçalama ve veritabanına indeksleme akışı."""

    def __init__(self):
        self.loader = FileLoader()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        init_db()

    def run(self, reset_existing: bool = True) -> Dict[str, int]:
        """Ingestion sürecini başlatır."""
        if reset_existing:
            DocumentStore.clear_all()

        docs = self.loader.load_documents()
        total_chunks = 0

        for doc in docs:
            filename = doc["filename"]
            chunks = self.chunker.chunk_text(doc["content"])
            
            for idx, chunk in enumerate(chunks):
                embedding = self.embedding_service.get_embedding(chunk)
                DocumentStore.insert_chunk(
                    source_file=filename,
                    chunk_index=idx,
                    content=chunk,
                    embedding=embedding,
                )
                total_chunks += 1

        return {
            "processed_documents": len(docs),
            "created_chunks": total_chunks
        }
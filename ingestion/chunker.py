from typing import List
from config.settings import CHUNK_OVERLAP, CHUNK_SIZE


class TextChunker:
    """Metinleri parçalara (chunks) ayıran sınıf."""

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP
    ) -> List[str]:
        """Metni örtüşmeli pencereler halinde parçalara böler."""
        if not text:
            return []

        if len(text) <= chunk_size:
            return [text]

        chunks = []
        start = 0
        text_len = len(text)
        step = chunk_size - overlap

        while start < text_len:
            end = min(start + chunk_size, text_len)
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end >= text_len:
                break
            start += step

        return chunks
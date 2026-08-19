from typing import List
from config.model_config import model_settings
from core.client import FoundryClientManager


class EmbeddingService:
    """Metinleri vektör temsiline dönüştüren servis."""

    def __init__(self, model_name: str = model_settings.EMBEDDING_MODEL):
        self.model_name = model_name
        self.client = FoundryClientManager.get_client()

    def get_embedding(self, text: str) -> List[float]:
        """Tek bir metin parçasının embedding vektörünü döndürür."""
        clean_text = text.strip()
        if not clean_text:
            return []

        response = self.client.embeddings.create(
            model=self.model_name,
            input=clean_text,
        )
        return response.data[0].embedding

    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Birden çok metnin embedding vektörlerini toplu olarak döndürür."""
        cleaned_texts = [t.strip() for t in texts if t.strip()]
        if not cleaned_texts:
            return []

        response = self.client.embeddings.create(
            model=self.model_name,
            input=cleaned_texts,
        )
        return [item.embedding for item in response.data]
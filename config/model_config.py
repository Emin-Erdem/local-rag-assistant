from dataclasses import dataclass

@dataclass(frozen=True)
class ModelSettings:
    # Model Tanımları
    EMBEDDING_MODEL: str = "qwen3-embedding-0.6b"
    LLM_MODEL: str = "phi-3.5-mini"

    # LLM Çıktı Parametreleri
    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 512
    TOP_P: float = 0.9

    # Retrieval Ayarları
    TOP_K_RESULTS: int = 3
    SIMILARITY_THRESHOLD: float = 0.3

# Varsayılan ayar nesnesi
model_settings = ModelSettings()
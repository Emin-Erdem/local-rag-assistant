from pathlib import Path

# Proje Kök Dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# Veri Dizinleri
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"
STORAGE_DIR = DATA_DIR / "storage"

# SQLite Veritabanı Yolu
DATABASE_PATH = STORAGE_DIR / "knowledge_base.db"

# Chunking Parametreleri
CHUNK_SIZE = 500  # Karakter sayısı bazlı varsayılan uzunluk
CHUNK_OVERLAP = 50  # Parçalar arası örtüşme miktarı

# Dizinlerin varlığını garanti altına al
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
STORAGE_DIR.mkdir(parents=True, exist_ok=True)
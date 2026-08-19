from pathlib import Path
from typing import Dict, List
from config.settings import DOCUMENTS_DIR


class FileLoader:
    """Belirtilen dizindeki metin dosyalarını yükleyen modül."""

    SUPPORTED_EXTENSIONS = {".txt", ".md"}

    @classmethod
    def load_documents(cls, directory: Path = DOCUMENTS_DIR) -> List[Dict[str, str]]:
        """Dizindeki desteklenen tüm dosyaları okur ve liste olarak döndürür."""
        documents = []
        if not directory.exists():
            return documents

        for file_path in directory.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in cls.SUPPORTED_EXTENSIONS:
                try:
                    content = file_path.read_text(encoding="utf-8").strip()
                    if content:
                        documents.append({
                            "filename": file_path.name,
                            "content": content
                        })
                except Exception as exc:
                    print(f"Hata: {file_path.name} okunamadı: {exc}")

        return documents
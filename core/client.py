from typing import Optional
import foundry_local


class FoundryClientManager:
    """Microsoft Foundry Local SDK istemci yöneticisi."""

    _instance: Optional[foundry_local.FoundryLocalClient] = None

    @classmethod
    def get_client(cls) -> foundry_local.FoundryLocalClient:
        """Foundry Local istemcisini tekil örnek olarak başlatır ve döndürür."""
        if cls._instance is None:
            cls._instance = foundry_local.FoundryLocalClient()
        return cls._instance
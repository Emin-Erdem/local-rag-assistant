from typing import List
import numpy as np


def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """İki vektör arasındaki kosinüs benzerliğini hesaplar (-1.0 ile 1.0 arası)."""
    if not vec_a or not vec_b:
        return 0.0

    a = np.array(vec_a, dtype=np.float32)
    b = np.array(vec_b, dtype=np.float32)

    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return float(dot_product / (norm_a * norm_b))
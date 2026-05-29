import json
import hashlib
from pathlib import Path
from pydoc import text

CACHE_FILE = Path("cache/embeddings.json")


def load_cache():

    if not CACHE_FILE.exists():
        return {}

    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(cache):

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def compute_hash(text: str):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()

from app.core.embeddings import (
    get_embedding
)

import numpy as np
def get_or_create_embedding(doc):

    cache = load_cache()

    table = doc["table"]
    text = doc["text"]

    doc_hash = compute_hash(text)

    if table in cache:

        cached = cache[table]

        if cached["hash"] == doc_hash:

            print(f"[CACHE HIT] {table}")

            return np.array(
                cached["embedding"]
            )

    print(f"[EMBEDDING CREATED] {table}")

    embedding = get_embedding(text)

    cache[table] = {
        "hash": doc_hash,
        "embedding": embedding.tolist()
    }

    save_cache(cache)

    return embedding
import requests
import numpy as np


OLLAMA_URL = "http://127.0.0.1:11434/api/embeddings"
MODEL = "nomic-embed-text"


def get_embedding(text: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": text
        }
    )

    data = response.json()

    return np.array(data["embedding"])

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_intent_bonus(query, table_name):
    query = query.lower()

    bonus = 0

    if "product" in query:
        if table_name == "products":
            bonus += 0.20

        if table_name == "categories":
            bonus += 0.10

        if table_name == "order_items":
            bonus += 0.05

    if "customer" in query or "user" in query:
        if table_name == "users":
            bonus += 0.20

        if table_name == "orders":
            bonus += 0.10

    if "order" in query:
        if table_name == "orders":
            bonus += 0.20

    return bonus
from app.core.embeddings import (
    get_embedding,
    cosine_similarity
)

a = get_embedding("users")
b = get_embedding("customers")
c = get_embedding("airplane")

print("users ↔ customers:",
      cosine_similarity(a, b))

print("users ↔ airplane:",
      cosine_similarity(a, c))
def extract_relevant_tables(query, graph):
    query = query.lower()
    matched = []

    for table in graph:
        if table in query:
            matched.append(table)

    return matched

def build_table_documents(schema):
    docs = []

    semantic_hints = {
        "users": "Stores customer and user account information.",
        "orders": "Stores purchase orders made by users.",
        "order_items": "Stores products included in orders.",
        "products": "Stores product catalog and inventory items.",
        "categories": "Stores product category classifications."
    }

    for table in schema["tables"]:
        columns = [
            col["name"]
            for col in table["columns"]
        ]

        description = semantic_hints.get(
            table["name"],
            ""
        )

        text = f"""
        Table {table['name']}.
        {description}
        Columns: {", ".join(columns)}.
        """

        docs.append({
            "table": table["name"],
            "text": text.strip()
        })

    return docs

from app.core.embeddings import (
    get_embedding,
    cosine_similarity,
    get_intent_bonus
)



def semantic_table_search(
    query,
    table_embeddings,
    top_k=5
):
    query_embedding = get_embedding(query)

    query_lower = query.lower()

    scores = []

    for item in table_embeddings:
        semantic_score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        keyword_bonus = 0

        if item["table"] in query_lower:
            keyword_bonus += 0.15

        intent_bonus = get_intent_bonus(query, item["table"])

        final_score = semantic_score + keyword_bonus + intent_bonus

        scores.append({
            "table": item["table"],
            "semantic_score": float(semantic_score),
            "keyword_bonus": keyword_bonus,
            "intent_bonus": intent_bonus,
            "final_score": float(final_score)
        })

    scores.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )
    


    return scores[:top_k]
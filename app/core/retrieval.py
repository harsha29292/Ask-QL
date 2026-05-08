def extract_relevant_tables(query, graph):
    query = query.lower()
    matched = []

    for table in graph:
        if table in query:
            matched.append(table)

    return matched

def build_table_documents(schema):
    docs = []

    for table in schema["tables"]:
        columns = [col["name"] for col in table["columns"]]

        text = f"""
        Table {table['name']}
        Columns: {", ".join(columns)}
        """

        docs.append({
            "table": table["name"],
            "text": text.strip()
        })

    return docs
from app.core.embeddings import get_embedding, cosine_similarity


def semantic_table_search(query, table_embeddings, top_k=2):
    query_embedding = get_embedding(query)

    scores = []

    for item in table_embeddings:
        score = cosine_similarity(query_embedding, item["embedding"])

        scores.append({
            "table": item["table"],
            "score": float(score)
        })

    scores.sort(key=lambda x: x["score"], reverse=True)

    return scores[:top_k]
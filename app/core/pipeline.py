from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph, find_join_path
from app.core.retrieval import extract_relevant_tables
from app.core.embeddings import get_embedding
from app.core.retrieval import build_table_documents

# cache schema + graph (important for performance)
_schema = None
_graph = None

_table_embeddings = []

def initialize():
    global _schema, _graph, _table_embeddings

    _schema = extract_schema()
    _graph = build_schema_graph(_schema)

    docs = build_table_documents(_schema)

    for doc in docs:
        embedding = get_embedding(doc["text"])

        _table_embeddings.append({
            "table": doc["table"],
            "embedding": embedding
        })



def run_pipeline(query: str):
    tables = extract_relevant_tables(query, _graph)

    if len(tables) < 2:
        return {"tables": tables, "path": None}

    # enforce stable ordering
    start, end = sorted(tables)

    path = find_join_path(_graph, start, end)

    return {
        "tables": tables,
        "path": path
    }

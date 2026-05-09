from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph, connect_tables, find_join_path
from app.core.retrieval import extract_relevant_tables
from app.core.embeddings import get_embedding
from app.core.retrieval import (
    build_table_documents,
    semantic_table_search
)

# cache schema + graph (important for performance)
_schema = None
_graph = None

_table_embeddings = []

def initialize():
    global _schema, _graph, _table_embeddings

    _schema = extract_schema()
    _graph = build_schema_graph(_schema)

    docs = build_table_documents(_schema)

    _table_embeddings = []

    for doc in docs:
        embedding = get_embedding(doc["text"])

        _table_embeddings.append({
            "table": doc["table"],
            "embedding": embedding
        })



def run_pipeline(query: str):
    results = semantic_table_search(
        query,
        _table_embeddings
    )

    tables = [r["table"] for r in results]

    if len(tables) < 2:
        return {
            "tables": tables,
            "scores": results,
            "path": None
        }

    start, end = tables[0], tables[1]

    path = connect_tables(
    _graph,
    tables
)
    return {
        "tables": tables,
        "scores": results,
        "path": path
    }
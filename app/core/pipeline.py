from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph, connect_tables, find_join_path,connect_tables_as_edges
from app.core.retrieval import extract_relevant_tables
from app.core.embeddings import get_embedding
from app.core.retrieval import (
    build_table_documents,
    semantic_table_search
)
from app.core.intent_parser import parse_intent
from app.core.sql_planner import build_join_clause


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
            "join_edges": None
        }

    start, end = tables[0], tables[1]

    join_edges = connect_tables_as_edges(
    _graph,
    tables
)

    join_clause = build_join_clause(join_edges, _graph)
    intent = parse_intent(query)
    return {
        "tables": tables,
        "scores": results,
        "join_edges": join_edges,
        "intent": intent,
        "join_clause": join_clause
    }
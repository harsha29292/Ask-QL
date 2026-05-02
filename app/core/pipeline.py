from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph, find_join_path
from app.core.retrieval import extract_relevant_tables

# cache schema + graph (important for performance)
_schema = None
_graph = None


def initialize():
    global _schema, _graph
    _schema = extract_schema()
    _graph = build_schema_graph(_schema)


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
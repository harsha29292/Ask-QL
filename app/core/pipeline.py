from warnings import filters

from app.core.reranker import rerank_tables
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
from app.core.select_planner import (
    build_select_clause
)
from app.db.execute import execute_sql
from app.core.answer_generator import (
    generate_answer
)
from app.core.filter_planner import (
    extract_filters,
    build_where_clause
)

from app.core.rewriter import (
    rewrite_query
)

from app.core.embeddings_cache import (
    get_or_create_embedding
)

from app.core.sql_validator import (
    validate_sql
)


from app.core.reranker import (
    rerank_tables
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

        embedding = get_or_create_embedding(
            doc
        )

        _table_embeddings.append({
        "table": doc["table"],
        "embedding": embedding
        })


def run_pipeline(query: str):
    rewritten_query = rewrite_query(query)

    results = semantic_table_search(
    rewritten_query,
    _table_embeddings
    )
    print("\nRAW RESULTS")
    print("COUNT:", len(results))
    print(
        [r["table"] for r in results]
            )

    intent = parse_intent(query)

    filters = extract_filters(query)

# NEW
    results = rerank_tables(
        query,
        results,
        intent,
        filters
            )
    TOP_K=3
    tables = [r["table"] for r in results[:TOP_K]]
    print("FINAL TABLES:")
    print(tables)


    filter_tables = []

    for f in filters:
        table = f.get("table")

        if table and table not in filter_tables:
            filter_tables.append(table)

    for table in filter_tables:
        if table not in tables:
            tables.append(table)

    join_edges = connect_tables_as_edges(
        _graph,
        tables
                )


  


               

    where_clause = build_where_clause(filters)
    join_clause = build_join_clause(join_edges, _graph)
    select_plan = build_select_clause(
    intent,
    tables)

    sql = (
    select_plan["select_clause"]
    + "\n"
    + join_clause
                )
    if where_clause:
        sql += "\n" + where_clause
    if select_plan["group_by"]:
        sql += (
            "\nGROUP BY "
            + select_plan["group_by"]

                )
        
    if select_plan["order_by"]:
        sql += (
            "\nORDER BY "
            + select_plan["order_by"]
                        )
    validation = validate_sql(
    sql,
    _schema,
    join_edges,
    _graph)
      
    
    if validation["valid"]:

        execution = execute_sql(sql)

    else:

        execution = {
            "success": False,
            "errors": validation["errors"]
                    }

    answer = generate_answer(
    query,
    execution)
    
       

     
    return {
        "tables": tables,
        "scores": results,
        "join_edges": join_edges,
        "intent": intent,
        "join_clause": join_clause,
        "select_plan": select_plan,
        "sql": sql,
        "execution": execution,
        "answer": answer,
        "filters": filters,
        "rewritten_query": rewritten_query,
        "validation": validation
        }
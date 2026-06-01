from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph
from app.core.sql_validator import validate_sql

schema = extract_schema()

graph = build_schema_graph(
    schema
)

# valid path
valid_edges = [
    ("users", "orders"),
    ("orders", "order_items")
]

# invalid path
invalid_edges = [
    ("users", "categories")
]

sql = """
SELECT users.name
FROM users
"""

print("\n" + "=" * 60)
print("VALID JOIN TEST")

result = validate_sql(
    sql,
    schema,
    valid_edges,
    graph
)

print(result)

print("\n" + "=" * 60)
print("INVALID JOIN TEST")

result = validate_sql(
    sql,
    schema,
    invalid_edges,
    graph
)

print(result)
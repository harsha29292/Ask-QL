from pprint import pprint

from app.db.introspect import extract_schema
from app.core.graph import build_schema_graph

schema = extract_schema()

graph = build_schema_graph(schema)

print("TYPE:", type(graph))

pprint(graph)
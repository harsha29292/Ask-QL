from collections import deque


def build_schema_graph(schema):
    graph = {}

    # nodes
    for table in schema["tables"]:
        graph[table["name"]] = {
            "columns": set(col["name"] for col in table["columns"]),
            "primary_key": table["primary_key"],
            "relations": []
        }

    # edges (bidirectional)
    for table in schema["tables"]:
        table_name = table["name"]

        for fk in table["foreign_keys"]:
            to_table = fk["references"]["table"]

            graph[table_name]["relations"].append({
                "to": to_table,
                "from_column": fk["column"],
                "to_column": fk["references"]["column"]
            })

            graph[to_table]["relations"].append({
                "to": table_name,
                "from_column": fk["references"]["column"],
                "to_column": fk["column"]
            })

    return graph


def find_join_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        visited.add(current)

        for rel in graph[current]["relations"]:
            neighbor = rel["to"]

            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


def serialize_graph(graph):
    return {
        table: {
            "columns": list(data["columns"]),
            "primary_key": data["primary_key"],
            "relations": data["relations"]
        }
        for table, data in graph.items()
    }
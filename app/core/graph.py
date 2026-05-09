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

    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        for rel in graph[current]["relations"]:
            neighbor = rel["to"]

            if neighbor in visited:
                continue

            visited.add(neighbor)

            queue.append(
                (neighbor, path + [neighbor])
            )

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

def connect_tables(graph, tables):
    if not tables:
        return []

    # start with first table
    full_path = [tables[0]]

    covered = list(full_path)

    for target in tables[1:]:
        best_path = None
        best_cost = float("inf")

        for source in covered:

            path = find_join_path(
                graph,
                source,
                target
                )

            if not path:
                continue

            cost = len(path)

            if cost < best_cost:
                best_cost = cost
                best_path = path

        # try connecting from ANY covered table
        

        if not best_path:
            continue

        # merge path without duplicates
        for node in best_path:
            if node not in full_path:
                full_path.append(node)

            if node not in covered:
                covered.append(node)

        

    return full_path
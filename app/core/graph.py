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

        for source in reversed(full_path):

            path = find_join_path(
                graph,
                source,
                target
                )

            if not path:
                continue

            cost = len(path)
            print(
                f"\nSOURCE={source} "
                f"TARGET={target} "
                f"PATH={path} "
                f"COST={cost}"
                                )
            

            if cost < best_cost:
                best_cost = cost
                best_path = path
        print(f"BEST PATH CHOSEN: {best_path}")
        # try connecting from ANY covered table
        

        if not best_path:
            continue

        # merge path without duplicates
        overlap_index = None

        for i, node in enumerate(best_path):
            if node in full_path:
                overlap_index = i
                break


        if overlap_index is not None:
            tail=best_path
        else:
            tail=best_path[overlap_index+1:]
        for node in tail:
            if node not in full_path:
                full_path.append(node)
            if node not in covered:
                covered.append(node)            

        

    return full_path
def validate_edges(graph, edges):
    for left, right in edges:

        valid = False

        for rel in graph[left]["relations"]:
            if rel["to"] == right:
                valid = True
                break

        if not valid:
            return False

    return True

    return True
def connect_tables_as_edges(graph, tables):
    if not tables:
        return []

    connected = {tables[0]}

    edges = []

    remaining = set(tables[1:])

    while remaining:
        best_path = None
        best_cost = float("inf")

        for source in connected:
            for target in remaining:

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

        if not best_path:
            break

        # convert path into edges
        for i in range(len(best_path) - 1):
            left = best_path[i]
            right = best_path[i + 1]

            edge = (left, right)

            if edge not in edges:
                edges.append(edge)

        connected.update(best_path)

        remaining -= connected

    return edges
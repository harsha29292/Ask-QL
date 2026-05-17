def build_join_clause(edges, graph):
    if not edges:
        return ""

    used_tables = set()

    first_left, _ = edges[0]

    sql = f"FROM {first_left}\n"

    used_tables.add(first_left)

    for left, right in edges:

        relation = None

        for rel in graph[left]["relations"]:
            if rel["to"] == right:
                relation = rel
                break

        if not relation:
            continue

        left_col = relation["from_column"]
        right_col = relation["to_column"]

        if right not in used_tables:
            sql += (
                f"JOIN {right}\n"
                f"ON {left}.{left_col} = "
                f"{right}.{right_col}\n"
            )

            used_tables.add(right)

    return sql
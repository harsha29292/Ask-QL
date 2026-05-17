def build_join_clause(path, graph):
    if not path or len(path) < 2:
        return ""

    sql = f"FROM {path[0]}\n"

    for i in range(len(path) - 1):
        left = path[i]
        right = path[i + 1]

        relation = None

        # find matching edge
        for rel in graph[left]["relations"]:
            if rel["to"] == right:
                relation = rel
                break

        if not relation:
            continue

        left_col = relation["from_column"]
        right_col = relation["to_column"]

        sql += (
            f"JOIN {right}\n"
            f"ON {left}.{left_col} = "
            f"{right}.{right_col}\n"
        )

    return sql
def generate_answer(query, execution):
    if not execution["success"]:
        return f"Failed to execute query: {execution['error']}"

    rows = execution["rows"]

    if not rows:
        return "No results found."

    query_lower = query.lower()

    # count-style queries
    if "count" in query_lower or "how many" in query_lower:
        if len(rows) == 1:
            return str(rows[0])

        lines = []

        for row in rows:
            values = [str(v) for v in row.values()]
            lines.append(" - ".join(values))

        return "\n".join(lines)

    # average queries
    if "average" in query_lower or "avg" in query_lower:
        first_row = rows[0]

        for value in first_row.values():
            return f"Average value is {value}"

    # ranking queries
    if "top" in query_lower or "lowest" in query_lower:

        lines = []

        for i, row in enumerate(rows, start=1):

            name = row.get("name")

            count = (
                row.get("total_count")
                or row.get("count")
            )

            if count is not None:
                lines.append(
                    f"{i}. {name} ({count})"
                )
            else:
                lines.append(
                    f"{i}. {name}"
                )

        return "\n".join(lines)

    # generic fallback
    return str(rows)
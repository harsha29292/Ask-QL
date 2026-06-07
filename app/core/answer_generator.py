def generate_answer(query, execution):

    if not execution["success"]:
        return (
            f"Failed to execute query: "
            f"{execution['error']}"
        )

    rows = execution["rows"]

    if not rows:
        return "No results found."

    query_lower = query.lower()

    # count-style queries
    if (
        "count" in query_lower
        or "how many" in query_lower
    ):

        if len(rows) == 1:
            return str(rows[0])

        lines = []

        for row in rows:
            values = [
                str(v)
                for v in row.values()
            ]

            lines.append(
                " - ".join(values)
            )

        return "\n".join(lines)

    # average queries
    if (
        "average" in query_lower
        or "avg" in query_lower
        or "mean" in query_lower
    ):

        first_row = rows[0]

        for value in first_row.values():

            return (
                f"Average value is "
                f"{float(value):,.2f}"
            )

    # sum / revenue queries
    if (
        "revenue" in query_lower
        or "total" in query_lower
        or "sum" in query_lower
    ):

        if len(rows) == 1:

            first_row = rows[0]

            if "total_value" in first_row:

                return (
                    f"Total value: "
                    f"${float(first_row['total_value']):,.2f}"
                )

    # ranking queries
    if (
        "top" in query_lower
        or "lowest" in query_lower
        or "highest" in query_lower
        or "most" in query_lower
        or "best" in query_lower
    ):

        lines = []

        for i, row in enumerate(
            rows,
            start=1
        ):

            name = row.get("name")

            total_count = (
                row.get("total_count")
                or row.get("count")
            )

            total_value = row.get(
                "total_value"
            )

            if total_value is not None:

                lines.append(
                    f"{i}. {name} "
                    f"(${float(total_value):,.2f})"
                )

            elif total_count is not None:

                lines.append(
                    f"{i}. {name} "
                    f"({total_count})"
                )

            else:

                lines.append(
                    f"{i}. {name}"
                )

        return "\n".join(lines)

    # generic table formatter
    if len(rows) <= 20:

        lines = []

        for i, row in enumerate(
            rows,
            start=1
        ):

            values = [
                str(v)
                for v in row.values()
            ]

            lines.append(
                f"{i}. "
                + " - ".join(values)
            )

        return "\n".join(lines)

    # fallback
    return str(rows)
def prune_tables(
    tables,
    intent,
    filters
):
    required = set()

    # tables referenced by filters
    for f in filters:
        required.add(
            f["table"]
        )

    # group by entity
    if intent["group_by"]:
        required.add(
            intent["group_by"]
        )

    # aggregation hints
    if intent["aggregation"] == "sum":

        if "payments" in tables:
            required.add(
                "payments"
            )

        elif "invoices" in tables:
            required.add(
                "invoices"
            )

    return [
        table
        for table in tables
        if (
            table in required
            or table not in [
                "users",
                "organizations",
                "team_members",
                "ticket_comments"
            ]
        )
    ]
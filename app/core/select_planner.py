def build_select_clause(
    intent,
    tables,
    query
):
    select_parts = []
    group_by = None
    order_by = None

    query_lower = query.lower()

    # -------------------------
    # BUSINESS INTENT OVERRIDES
    # -------------------------

    if (
        "paying" in query_lower
        or "revenue" in query_lower
    ):
        intent["aggregation"] = "sum"

    # -------------------------
    # GROUPING ENTITY
    # -------------------------

    if intent["group_by"] == "products":

        select_parts.append(
            "products.name"
        )

        group_by = "products.name"

    elif intent["group_by"] == "users":

        select_parts.append(
            "users.name"
        )

        group_by = "users.name"

    elif intent["group_by"] == "categories":

        select_parts.append(
            "categories.name"
        )

        group_by = "categories.name"

    # SaaS support

    elif (
        "customers" in tables
        and "customer" in query_lower
    ):

        select_parts.append(
            "customers.name"
        )

        group_by = "customers.name"

    elif (
        "organizations" in tables
        and "organization" in query_lower
    ):

        select_parts.append(
            "organizations.name"
        )

        group_by = "organizations.name"

    elif (
        "plans" in tables
        and "plan" in query_lower
    ):

        select_parts.append(
            "plans.name"
        )

        group_by = "plans.name"

    # -------------------------
    # AGGREGATION
    # -------------------------

    aggregation = intent["aggregation"]

    if aggregation == "count":

        if "order_items" in tables:

            select_parts.append(
                "COUNT(order_items.id) AS total_count"
            )

        else:

            select_parts.append(
                "COUNT(*) AS total_count"
            )

    elif aggregation == "avg":

        if "orders" in tables:

            select_parts.append(
                "AVG(orders.total_amount) AS average_value"
            )

        elif "invoices" in tables:

            select_parts.append(
                "AVG(invoices.amount) AS average_value"
            )

    elif aggregation == "sum":

        if "payments" in tables:

            select_parts.append(
                "SUM(payments.amount) AS total_value"
            )

        elif "invoices" in tables:

            select_parts.append(
                "SUM(invoices.amount) AS total_value"
            )

        elif "orders" in tables:

            select_parts.append(
                "SUM(orders.total_amount) AS total_value"
            )

    # -------------------------
    # RANKING
    # -------------------------

    if intent["ranking"] == "desc":

        if aggregation == "count":

            order_by = "total_count DESC"

        elif aggregation == "sum":

            order_by = "total_value DESC"

    elif intent["ranking"] == "asc":

        if aggregation == "count":

            order_by = "total_count ASC"

        elif aggregation == "sum":

            order_by = "total_value ASC"

    # -------------------------
    # FALLBACK
    # -------------------------

    if not select_parts:

        select_parts.append("*")

    return {
        "select_clause":
            "SELECT "
            + ", ".join(select_parts),

        "group_by":
            group_by,

        "order_by":
            order_by,
        "limit":
            intent["limit"]
    }
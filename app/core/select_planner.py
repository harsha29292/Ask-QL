def build_select_clause(intent, tables):
    select_parts = []
    group_by = None
    order_by = None

    # grouping entity
    if intent["group_by"] == "products":
        select_parts.append("products.name")

        group_by = "products.name"

    elif intent["group_by"] == "users":
        select_parts.append("users.name")

        group_by = "users.name"

    elif intent["group_by"] == "categories":
        select_parts.append("categories.name")

        group_by = "categories.name"

    # aggregation logic
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

    elif aggregation == "sum":

        if "orders" in tables:
            select_parts.append(
                "SUM(orders.total_amount) AS total_value"
            )

    # ranking logic
    if intent["ranking"] == "desc":

        if aggregation == "count":
            order_by = "total_count DESC"

    elif intent["ranking"] == "asc":

        if aggregation == "count":
            order_by = "total_count ASC"

    # fallback
    if not select_parts:
        select_parts.append("*")

    return {
        "select_clause": (
            "SELECT " +
            ", ".join(select_parts)
        ),
        "group_by": group_by,
        "order_by": order_by
    }
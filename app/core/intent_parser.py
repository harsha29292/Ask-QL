def parse_intent(query: str):

    query = query.lower()

    intent = {
        "aggregation": None,
        "ranking": None,
        "filters": [],
        "group_by": None
    }

    # -------------------------
    # Aggregation Detection
    # -------------------------

    if any(word in query for word in [
        "count",
        "how many",
        "number of"
    ]):
        intent["aggregation"] = "count"

    elif any(word in query for word in [
        "average",
        "avg",
        "mean"
    ]):
        intent["aggregation"] = "avg"

    elif any(word in query for word in [
        "sum",
        "total",
        "revenue",
        "paying",
        "payment",
        "payments"
    ]):
        intent["aggregation"] = "sum"

    # -------------------------
    # Ranking
    # -------------------------

    if any(word in query for word in [
        "top",
        "highest",
        "best",
        "most"
    ]):
        intent["ranking"] = "desc"

    elif any(word in query for word in [
        "lowest",
        "least"
    ]):
        intent["ranking"] = "asc"

    # -------------------------
    # Fallback Aggregation
    # -------------------------

    if (
        intent["ranking"] is not None
        and intent["aggregation"] is None
    ):
        intent["aggregation"] = "count"

    # -------------------------
    # Group By Detection
    # -------------------------

    if "products" in query or "product" in query:
        intent["group_by"] = "products"

    elif "categories" in query or "category" in query:
        intent["group_by"] = "categories"

    elif "customers" in query or "customer" in query:
        intent["group_by"] = "customers"

    elif "organizations" in query or "organization" in query:
        intent["group_by"] = "organizations"

    elif "plans" in query or "plan" in query:
        intent["group_by"] = "plans"

    elif "users" in query or "user" in query:
        intent["group_by"] = "users"

    return intent
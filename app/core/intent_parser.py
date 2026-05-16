def parse_intent(query: str):
    query = query.lower()

    intent = {
        "aggregation": None,
        "ranking": None,
        "filters": [],
        "group_by": None
    }

    # aggregation detection
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
        "total"
    ]):
        intent["aggregation"] = "sum"

    # ranking intent
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

    # group by hints
    if "products" in query or "product" in query:
        intent["group_by"] = "products"

    elif "users" in query or "customers" in query:
        intent["group_by"] = "users"

    elif "categories" in query:
        intent["group_by"] = "categories"

    return intent
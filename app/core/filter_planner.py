import re


CATEGORY_MAP = {
    "electronics": "Electronics",
    "books": "Books",
    "clothing": "Clothing"
}


def extract_filters(query: str):
    query_lower = query.lower()

    filters = []

    # category filters
    for keyword, value in CATEGORY_MAP.items():

        if keyword in query_lower:

            filters.append({
                "column": "categories.name",
                "operator": "=",
                "value": value,
                "table": "categories"
            })

    # above 500
    matches = re.findall(
        r"(?:above|greater than)\s+(\d+)",
        query_lower
    )

    for amount in matches:

        filters.append({
            "column": "orders.total_amount",
            "operator": ">",
            "value": int(amount),
            "table": "orders"
        })

    # below 1000
    matches = re.findall(
        r"(?:below|less than)\s+(\d+)",
        query_lower
    )

    for amount in matches:

        filters.append({
            "column": "orders.total_amount",
            "operator": "<",
            "value": int(amount),
            "table": "orders"
        })

    return filters


def build_where_clause(filters):
    if not filters:
        return ""

    conditions = []

    for f in filters:

        value = f["value"]

        if isinstance(value, str):
            value = f"'{value}'"

        conditions.append(
            f"{f['column']} "
            f"{f['operator']} "
            f"{value}"
        )

    return "WHERE " + " AND ".join(conditions)
import re

from datetime import datetime

CATEGORY_MAP = {
    "electronics": "Electronics",
    "books": "Books",
    "clothing": "Clothing"
}

STATUS_FILTERS = {

    "active": {
        "table": "subscriptions",
        "column": "subscriptions.status",
        "value": "active"
    },

    "trial": {
        "table": "subscriptions",
        "column": "subscriptions.status",
        "value": "trial"
    },

    "cancelled": {
        "table": "subscriptions",
        "column": "subscriptions.status",
        "value": "cancelled"
    },

    "paid": {
        "table": "invoices",
        "column": "invoices.status",
        "value": "paid"
    },

    "pending": {
        "table": "invoices",
        "column": "invoices.status",
        "value": "pending"
    },

    "overdue": {
        "table": "invoices",
        "column": "invoices.status",
        "value": "overdue"
    }
}
def extract_filters(query: str):
    query_lower = query.lower()

    filters = []

    # category filters
    # status filters

    for keyword, config in STATUS_FILTERS.items():

        if keyword in query_lower:

            filters.append({

                "column": config["column"],

                "operator": "=",

                "value": config["value"],

                "table": config["table"]
                })
    current_year = datetime.now().year

    if "this year" in query_lower:

        filters.append({
        "column": "invoices.issued_at",
        "operator": ">=",
        "value": f"{current_year}-01-01",
        "table": "invoices"
        })

        filters.append({
        "column": "invoices.issued_at",
        "operator": "<=",
        "value": f"{current_year}-12-31",
        "table": "invoices"
        })

    elif "last year" in query_lower:

        year = current_year - 1

        filters.append({
        "column": "invoices.issued_at",
        "operator": ">=",
        "value": f"{year}-01-01",
        "table": "invoices"
        })

        filters.append({
        "column": "invoices.issued_at",
        "operator": "<=",
        "value": f"{year}-12-31",
        "table": "invoices"
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

from app.core.filter_planner import (
    extract_filters
)

queries = [

    "customers with active subscriptions",

    "customers with overdue invoices",

    "paid invoices",

    "cancelled subscriptions",

    "trial subscriptions"
]

for query in queries:

    print("\n" + "=" * 60)

    print(query)

    print(
        extract_filters(query)
    )
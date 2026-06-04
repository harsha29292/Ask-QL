from app.core.filter_planner import (
    extract_filters
)

queries = [
    "revenue this year",
    "revenue last year",
    "invoices this year",
    "customers with invoices this year"
]

for query in queries:

    print("\n" + "=" * 60)

    print(query)

    print(
        extract_filters(query)
    )
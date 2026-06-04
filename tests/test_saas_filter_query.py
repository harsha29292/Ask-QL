from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "customers with active subscriptions",
    "customers with overdue invoices",
    "paid invoices"
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nFILTERS:")
    print(result["filters"])

    print("\nSQL:")
    print(result["sql"])

    print("\nVALIDATION:")
    print(result["validation"])
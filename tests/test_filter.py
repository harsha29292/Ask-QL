from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "customers who bought electronics",
    "orders above 500",
    "orders above 500 and below 1000",
    "books purchases"
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)
    print("QUERY:", query)

    print("\nFILTERS:")
    print(result["filters"])

    print("\nSQL:")
    print(result["sql"])
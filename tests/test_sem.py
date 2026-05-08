from app.core.pipeline import (
    initialize,
    run_pipeline
)

# initialize schema + graph + embeddings
initialize()

queries = [
    "top products bought by users",
    "customers purchasing items",
    "people buying products",
    "product categories",
    "orders made by customers"
]

for query in queries:
    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nTABLES:")
    print(result["tables"])

    print("\nSIMILARITY SCORES:")
    for item in result["scores"]:
        print(
            f"{item['table']} -> "
            f"{round(item['score'], 4)}"
        )

    print("\nJOIN PATH:")
    print(result["path"])
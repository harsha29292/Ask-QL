from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "buyers of electronics",
    "purchasers of books",
    "sales by category",
    "users ordering products",
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nREWRITTEN:")
    print(result["rewritten_query"])

    print("\nTABLES:")
    print(result["tables"])

    print("\nTOP SCORES:")
    for item in result["scores"]:
        print(
            f"{item['table']} -> "
            f"{round(item['final_score'], 4)}"
        )
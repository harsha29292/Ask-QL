from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "average order value",
    "top products bought by users",
    "customers who bought electronics"
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nTOP TABLES:")

    for item in result["scores"]:

        print(
            item["table"],
            round(
                item.get(
                    "rerank_score",
                    item["final_score"]
                ),
                4
            )
        )
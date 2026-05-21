from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "count customers who bought electronics",
    "average order value",
    "top products bought by users",
    "lowest selling categories"
]

for query in queries:

    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nSQL:")
    print(result["sql"])
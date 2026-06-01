from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "top products bought by users",
    "lowest selling categories",
    "average order value"
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nVALIDATION:")
    print(result["validation"])

    print("\nSQL:")
    print(result["sql"])
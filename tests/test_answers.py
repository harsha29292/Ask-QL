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

    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nANSWER:")
    print(result["answer"])
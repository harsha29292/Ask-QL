from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "top subscription plans"
]

for query in queries:

    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nANSWER:")
    print(result["answer"])
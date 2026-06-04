from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "revenue this year",
    "revenue last year",
    "highest revenue customers this year"
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

    print("\nANSWER:")
    print(result["answer"])
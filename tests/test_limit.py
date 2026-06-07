from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

queries = [
    "top 5 paying customers",
    "top 3 subscription plans",
    "highest revenue customers"
]

for query in queries:

    result = run_pipeline(query)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nINTENT:")
    print(result["intent"])

    print("\nSQL:")
    print(result["sql"])

    print("\nANSWER:")
    print(result["answer"])
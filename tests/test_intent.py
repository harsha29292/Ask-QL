from app.core.pipeline import initialize, run_pipeline

initialize()

queries = [
    "top products bought by users",
    "average order value",
    "count customers who bought electronics",
    "lowest selling categories"
]

for query in queries:
    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nINTENT:")
    print(result["intent"])

    print("\nTABLES:")
    print(result["tables"])

    print("\nJOIN PATH:")
    print(result["path"])
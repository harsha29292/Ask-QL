from app.core.pipeline import initialize, run_pipeline

initialize()

queries = [
    "top products bought by users",
    "orders made by customers",
    "product categories"
]

for query in queries:
    print("\n" + "=" * 60)
    print("QUERY:", query)

    result = run_pipeline(query)

    print("\nPATH:")
    print(result["path"])

    print("\nJOIN CLAUSE:")
    print(result["join_clause"])
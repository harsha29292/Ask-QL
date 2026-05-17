
from app.core import pipeline
from app.core.pipeline import (
    initialize,
    run_pipeline
)


from app.core.graph import validate_edges

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
    print(result["join_edges"])

    print("\nJOIN CLAUSE:")
    print(result["join_clause"])
    print("\nVALID PATH:")
    print(validate_edges(
        pipeline._graph,
        result["join_edges"]
                        ))
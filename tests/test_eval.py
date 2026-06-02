from app.core.pipeline import (
    initialize,
    run_pipeline
)

from tests.eval_queries import (
    EVAL_SET
)

initialize()

total_precision = 0
total_recall = 0

table_hit_rate = 0
valid_sql = 0

for item in EVAL_SET:

    result = run_pipeline(
        item["query"]
    )

    predicted = set(
        result["tables"]
    )

    expected = set(
        item["expected_tables"]
    )

    correct = predicted.intersection(
        expected
    )

    precision = (
        len(correct)
        / len(predicted)
    )

    recall = (
        len(correct)
        / len(expected)
    )

    total_precision += precision
    total_recall += recall

    # table hit rate
    hit = expected.issubset(predicted)

    if not hit:

        print("\nFAILED RETRIEVAL")

        print("QUERY:")
        print(item["query"])

        print("\nSCORES:")

        for score in result["scores"]:

            print(
                score["table"],
                round(
                    score.get(
                     "rerank_score",
                        score["final_score"]
                    ),
                    4
                )
            )

    if hit:
        table_hit_rate += 1

    # sql validity
    if result["validation"]["valid"]:
        valid_sql += 1

    print("\n" + "=" * 60)

    print("QUERY:")
    print(item["query"])

    print("EXPECTED:")
    print(expected)

    print("PREDICTED:")
    print(predicted)

    print(
        f"PRECISION: {precision:.2f}"
    )

    print(
        f"RECALL: {recall:.2f}"
    )

    print(
        f"HIT: {hit}"
    )

    print(
        f"SQL VALID: {result['validation']['valid']}"
    )

print("\n" + "=" * 60)

print(
    "AVG PRECISION:",
    round(
        total_precision / len(EVAL_SET),
        2
    )
)

print(
    "AVG RECALL:",
    round(
        total_recall / len(EVAL_SET),
        2
    )
)

print(
    "TABLE HIT RATE:",
    round(
        table_hit_rate / len(EVAL_SET),
        2
    )
)

print(
    "SQL VALIDITY:",
    round(
        valid_sql / len(EVAL_SET),
        2
    )
)
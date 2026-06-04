from app.core.pipeline import initialize, run_pipeline
from tests.saas_eval_queries import SAAS_EVAL

initialize()

total_precision = 0
total_recall = 0
hit_rate = 0

for item in SAAS_EVAL:

    result = run_pipeline(item["query"])

    predicted = set(result["tables"])
    expected = set(item["expected_tables"])

    correct = predicted.intersection(expected)

    precision = len(correct) / len(predicted)
    recall = len(correct) / len(expected)

    hit = expected.issubset(predicted)

    total_precision += precision
    total_recall += recall
    hit_rate += int(hit)

    print("\n" + "=" * 60)
    print("QUERY:", item["query"])
    print("EXPECTED:", expected)
    print("PREDICTED:", predicted)
    print(f"PRECISION: {precision:.2f}")
    print(f"RECALL: {recall:.2f}")

print("\n" + "=" * 60)

print(
    "AVG PRECISION:",
    round(total_precision / len(SAAS_EVAL), 2)
)

print(
    "AVG RECALL:",
    round(total_recall / len(SAAS_EVAL), 2)
)

print(
    "TABLE HIT RATE:",
    round(hit_rate / len(SAAS_EVAL), 2)
)
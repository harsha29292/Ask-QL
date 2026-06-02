from app.core.pipeline import (
    initialize,
    run_pipeline
)

from tests.eval_answers import (
    EVAL_SET
)

initialize()

correct = 0

for item in EVAL_SET:

    result = run_pipeline(
        item["query"]
    )

    answer = result["answer"]

    passed = True

    for expected in item[
        "expected_answer_contains"
    ]:

        if expected not in answer:
            passed = False

    if passed:
        correct += 1

    print("\n" + "=" * 60)

    print("QUERY:")
    print(item["query"])

    print("\nANSWER:")
    print(answer)

    print(
        "\nPASSED:",
        passed
    )

print("\n" + "=" * 60)

print(
    "ANSWER ACCURACY:",
    round(
        correct / len(EVAL_SET),
        2
    )
)
from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

result = run_pipeline(
    "active customers with overdue invoices this year"
)

print("\nTABLES:")
print(result["tables"])

print("\nSQL:")
print(result["sql"])

print("\nVALIDATION:")
print(result["validation"])

print("\nANSWER:")
print(result["answer"])
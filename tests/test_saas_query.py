from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

query = "top paying customers"

result = run_pipeline(query)

print("\nTABLES:")
print(result["tables"])

print("\nSQL:")
print(result["sql"])

print("\nVALIDATION:")
print(result["validation"])

print("\nANSWER:")
print(result["answer"])
from app.core.pipeline import (
    initialize,
    run_pipeline
)

initialize()

result = run_pipeline(
    "organizations with most users"
)

print("\nTABLES:")
print(result["tables"])

print("\nSQL:")
print(result["sql"])

print("\nVALIDATION:")
print(result["validation"])

print("\nANSWER:")
print(result["answer"])
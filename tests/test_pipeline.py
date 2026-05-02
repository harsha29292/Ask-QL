from app.core.pipeline import initialize, run_pipeline

initialize()

query = "top products bought by users"

result = run_pipeline(query)

print("RESULT:", result)
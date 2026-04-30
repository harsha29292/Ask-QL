import requests
import time

def generate(prompt):
    start_time = time.time()

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    end_time = time.time()

    return {
        "output": response.json()["response"],
        "latency": end_time - start_time
    }
result = generate("""You are a PostgreSQL expert.

Schema:
users(id, name, email)

Task:
Generate a SQL query for the question below.

Rules:
- Output ONLY a valid PostgreSQL query
- Do NOT include explanations
- Do NOT include multiple versions
- Do NOT mention other SQL dialects
Question:
Get all users""")
print(f"Generated Text: {result['output']}")
print(f"Latency: {result['latency']} seconds")
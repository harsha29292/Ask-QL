import requests
import json
import time

def stream_generate(prompt):
    start_time = time.time()
    first_token_time = None

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            if first_token_time is None:
                first_token_time = time.time()

            data = json.loads(line)
            print(data.get("response", ""), end="", flush=True)

    end_time = time.time()

    print("\n")
    print("TTFT:", first_token_time - start_time)
    print("Total Latency:", end_time - start_time)
result = stream_generate("Explain how drones work in detail in 200 words")
print(result)    
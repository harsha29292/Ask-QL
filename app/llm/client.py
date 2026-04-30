import requests
import time
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

import time

def stream_generate_sse(prompt: str):
    import requests
    import json

    start_time = time.time()
    first_token_time = None

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    buffer = ""
    chunk_size = 40

    for line in response.iter_lines():
        if line:
            if first_token_time is None:
                first_token_time = time.time()

            data = json.loads(line)
            token = data.get("response", "")

            buffer += token

            if len(buffer) >= chunk_size or token.endswith((".", "?", "!", "\n")):
                yield f"data: {buffer}\n\n"
                buffer = ""

    if buffer:
        yield f"data: {buffer}\n\n"

    end_time = time.time()

    # send metadata
    yield f"event: metrics\ndata: {{\"ttft\": {first_token_time - start_time}, \"total\": {end_time - start_time}}}\n\n"

    yield "event: done\ndata: end\n\n"
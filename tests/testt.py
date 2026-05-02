import requests

response = requests.post(
    "http://127.0.0.1:8000/generate-stream",
    json={"prompt": "Explain AI in simple terms"},
    stream=True
)

for line in response.iter_lines():
    if line:
        print(line.decode())
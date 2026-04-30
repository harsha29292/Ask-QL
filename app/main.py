from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.llm.client import stream_generate_sse

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-stream")
def generate_stream(request: PromptRequest):
    generator = stream_generate_sse(request.prompt)

    return StreamingResponse(
        generator,
        media_type="text/event-stream"
    )
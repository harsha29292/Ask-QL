from fastapi import FastAPI
from pydantic import BaseModel

from app.core.pipeline import (
    initialize,
    run_pipeline
)

app = FastAPI(
    title="AskQL"
)

initialize()


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/query")
def query(
    request: QueryRequest
):

    result = run_pipeline(
        request.query
    )

    return {
        "query": request.query,
        "tables": result["tables"],
        "sql": result["sql"],
        "answer": result["answer"]
    }
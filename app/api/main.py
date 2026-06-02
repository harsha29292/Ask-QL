from fastapi import FastAPI


from app.core.pipeline import initialize, run_pipeline


app=FastAPI()

initialize()   


@app.post("/query")

def query(payload: dict):

    result=run_pipeline(
        payload["query"]
    )

    return{
        "query": payload["query"],
        "sql": result["sql"],
        "answer": result["answer"]
    }
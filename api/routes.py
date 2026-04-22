from fastapi import FastAPI
from app.main import run_pipeline

app = FastAPI()

@app.get("/run")
def start():
    run_pipeline("data/sample.mp4")
    return {"status": "running"}
from fastapi import FastAPI
from scoring import score

app = FastAPI(title="MLOPS API")

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}

@app.get("/health")
def health():
    return {"health": "green"}

@app.get("/score")
def score_endpoint(x: float):
    return score(x)

from fastapi import FastAPI

app = FastAPI(title="MLOPS API")

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}

@app.get("/health")
def health():
    return {"health": "green"}

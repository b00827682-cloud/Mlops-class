from fastapi import FastAPI

app = FastAPI(title="Surface API")

@app.get("/surface{surface}")
def surface(surface: int):
    api = 1 if surface <= 50 else 2
    return {"surface": surface, "api": api}




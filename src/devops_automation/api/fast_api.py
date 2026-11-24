from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def home() -> dict:
    return {"message": "DevOps automation running"}


@app.get("/health")
def health() -> dict:
    return {"status": "healthy"}

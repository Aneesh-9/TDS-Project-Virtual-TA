from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TDS Virtual TA is live!"}

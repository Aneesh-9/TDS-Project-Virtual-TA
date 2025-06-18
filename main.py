# main.py
import os
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Virtual TA is up and running!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway sets this PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)

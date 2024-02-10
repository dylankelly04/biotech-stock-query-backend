from fastapi import FastAPI
from gpt import generate

app = FastAPI()

@app.get("/")
def health_check() -> dict[str, list[str]]:
    return {"messages": ["Server healthy."]}

@app.get("/{symbol}")
def read_item(symbol: str) -> dict[str, list[str]]:
    return {"messages": generate(symbol)}
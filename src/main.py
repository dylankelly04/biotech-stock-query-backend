from fastapi import FastAPI
from gpt import generate
from seeking_alpha import get_titles

app = FastAPI()

@app.get("/api")
def health_check() -> dict[str, list[str]]:
    return {"messages": ["Server healthy."]}

@app.get("/api/{symbol}")
def generate_response(symbol: str, query: str) -> dict[str, list[str]]:
    return {"messages": generate(symbol, query)}
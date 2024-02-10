from fastapi import FastAPI

from gpt import generate
from stock import get_data

app = FastAPI()

@app.get("/api")
def health_check() -> dict[str, list[str]]:
    return {"messages": ["Server healthy."]}

@app.get("/api/{symbol}")
def generate_response(symbol: str, query: str) -> dict[str, list[str]]:
    return {"messages": generate(symbol, query)}

@app.get("/data")
def graph_data(ticker: str, time: str):
    return get_data(ticker, time)

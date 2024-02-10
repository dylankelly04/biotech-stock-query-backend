from fastapi import FastAPI
from gpt import generate
from stock import get_data
import requests

app = FastAPI()


@app.get("/")
def health_check() -> dict[str, list[str]]:
    return {"messages": ["Server healthy."]}


@app.get("/{symbol}")
def read_item(symbol: str) -> dict[str, list[str]]:
    return {"messages": generate(symbol)}


@app.get("/data")
def graph_data():
    ticker = requests.args.get('ticker')
    time = requests.args.get('time')
    return get_data(ticker, time)

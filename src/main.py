from typing import Union
from fastapi import FastAPI, Response

from gpt import generate
from similar_stocks import get_recommended_symbols
from stock import get_data

app = FastAPI()

@app.get("/api")
def health_check() -> dict[str, list[str]]:
    return {"messages": ["Server healthy."]}

@app.get("/api/{symbol}")
def generate_response(symbol: str, query: str) -> dict[str, list[str]]:
    return {"messages": generate(symbol, query)}

@app.get("/api/similar/{symbol}")
def get_similar(symbol: str, res: Response) -> Union[dict[str, list[str]], str]:
    try:
        similars = get_recommended_symbols(symbol)
        return {"similar": similars}
    except:
        res.status_code = 500
        return "Failed to fetch similar stocks (500)"

@app.get("/data")
def graph_data(ticker: str, time: str):
    return get_data(ticker, time)

from typing import Union
from fastapi import FastAPI, Response

from gpt import generate
from similar_stocks import get_recommended_symbols
from stock import get_graph_data
from fastapi.middleware.cors import CORSMiddleware

from yahoo_finance import fetch_raw_data, get_data, preprocess_data
app = FastAPI()
allowed_origins = [
    "http://localhost:3000",
    "https://biotech-stock-query.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    # Allow specific origins (or ["*"] for all origins)
    allow_origins=allowed_origins,
    allow_credentials=True,  # Allow cookies to be included in cross-origin requests
    allow_methods=["*"],  # Allow all methods (or specify like ["GET", "POST"])
    # Allow all headers (or specify like ["X-Custom-Header"])
    allow_headers=["*"],
)


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
    return get_graph_data(ticker, time)

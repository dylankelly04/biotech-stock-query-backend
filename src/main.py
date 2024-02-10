from fastapi import FastAPI

from gpt import generate
from stock import get_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
allowed_origins = [
    "http://localhost:3000"
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


@app.get("/data")
def graph_data(ticker: str, time: str):
    return get_data(ticker, time)

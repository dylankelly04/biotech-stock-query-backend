import yfinance as yf


def get_graph_data(ticker, time):
    res = yf.Ticker(ticker)
    hist = res.history(period=time)
    return hist.to_json()

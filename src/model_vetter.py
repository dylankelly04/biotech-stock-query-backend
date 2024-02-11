import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import *
from keras.layers import *
import yfinance as yf


def generate_rating(symbol: str, model):
    res = yf.Ticker(symbol)
    hist = res.history(period='1mo').loc[:, 'Close'].to_numpy()
    cols = ['Ordinary Shares Number', 'Total Debt', 'Working Capital', 'Total Assets',
            'Total Liabilities Net Minority Interest', 'Inventory', 'Cash And Cash Equivalents']

    bal = res.balance_sheet
    ind = []
    for col in cols:
        if (col not in bal.index):
            ind.append(0)
        else:
            ind.append(bal.loc[col].iloc[0])

    ind = np.array(ind)

    ind = ind / ind[3].reshape(-1, 1)
    hist = (hist - hist.min().reshape(-1, 1)) / \
        ((hist.max() - hist.min()).reshape(-1, 1))

    preds = model.predict([hist.reshape(1, -1), ind.reshape(1, -1)]).tolist()
    print(preds)
    return {"Very Strong Potential": preds[0][0], "Strong Potential": preds[0][1], "Neutral": preds[0][2], "Low Potential": preds[0][3], "Little/No Potential": preds[0][4]}

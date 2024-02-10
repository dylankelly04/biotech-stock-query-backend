import requests
import bs4

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' }

# People also watch
def get_paw_endpoint(symbol: str) -> str:
  return f"https://query1.finance.yahoo.com/v6/finance/recommendationsbysymbol/{symbol}"

def get_recommended_symbols(symbol: str) -> list[str]:
  response = requests.get(get_paw_endpoint(symbol), headers=headers)

  if (response.status_code != 200):
    raise Exception("Failed to fetch recommended symbols.")

  json = response.json()

  try:
    recommendations = json["finance"]["result"][0]["recommendedSymbols"]
    return [rec["symbol"] for rec in recommendations]
  except:
    raise Exception("Failed to fetch recommended symbols.")
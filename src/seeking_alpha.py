import bs4 as bs
import requests

def get_endpoint(symbol: str) -> str:
  return f"https://seekingalpha.com/api/sa/combined/{symbol}.xml"

def fetch_rss(symbol: str) -> str:
  response = requests.get(get_endpoint(symbol))

  if (response.status_code != 200):
    raise Exception("Failed to fetch RSS feed.")

  return response.text;

def parse_rss(rss: str) -> list[str]:
  soup = bs.BeautifulSoup(rss, "xml")
  items = soup.find_all("item")

  return [item.title.text for item in items]

def get_titles(symbol: str) -> list[str]:
  print(f"Fetching titles for {symbol}")
  rss = fetch_rss(symbol)
  return parse_rss(rss)
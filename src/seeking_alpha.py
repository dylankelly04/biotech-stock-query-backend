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
  titles = [item.title.text for item in items]
  dates = [item.pubDate.text[item.pubDate.text.find(", ")+2:item.pubDate.text.find(", ")+13] for item in items]
  return [titles[i] + " " + dates[i] for i in range(len(titles))]

def get_titles(symbol: str) -> list[str]:
  print(f"Fetching titles and dates for {symbol}")
  rss = fetch_rss(symbol)
  return parse_rss(rss)
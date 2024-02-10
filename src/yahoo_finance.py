import requests

def fetch_raw_data(symbol):
    url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=" + symbol + "&region=US&lang=en-US"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    return result.content.decode()

def get_data(raw_file_str, info_type):
    start_indices = []
    end_indices = []
    start_idx = 0
    while raw_file_str.find(info_type, start_idx) != -1:
      start_indices.append(raw_file_str.find(info_type, start_idx) + len(info_type))
      end_indices.append(raw_file_str.find("</" + info_type[1:], start_idx))
      start_idx = end_indices[-1] + 1
    
    data_lst = []
    for i in range(1, len(start_indices)): # first instance is not needed
      data_lst.append(raw_file_str[start_indices[i]:end_indices[i]])
    return data_lst
  
def preprocess_data(descriptions, titles):
  """ 

  """
  return descriptions, titles
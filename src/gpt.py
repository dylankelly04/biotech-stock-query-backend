from yahoo_finance import *
from seeking_alpha import *
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(symbol: str, query: str):
  input_data = ".\n".join(get_data(symbol)) + ".\n".join(get_titles(symbol))
  prompt = """
  You are to assume the role of a financial analyst.
  Using the given news article titles and descriptions, answer the following question in a brief list. "
  """ + query
  output = prompt_model(input_data, prompt)
  return output

def prompt_model(input_data, prompt):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": prompt},
      {"role": "user", "content": input_data},
    ]
  )
  return response.choices[0].message.content
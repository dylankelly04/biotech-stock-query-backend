from openai import OpenAI
client = OpenAI(api_key="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")

def generate(symbol: str, query: str) -> list[str]:
  data = fetch_raw_data(symbol)
  descriptions = get_data(data, "<description>")
  titles = get_data(data, "<title>")[:-1]
  descriptions, titles = preprocess_data(descriptions, titles)
  input_data = ".\n".join([titles[i] + ": " + descriptions[i] for i in range(len(titles))])
  input_data += ".\n".join(get_titles(symbol))
  prompt = """
  You are to assume the role of a financial analyst. 
  Using the given news article titles and descriptions, answer the following question. "
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
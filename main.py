from ast import Try
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPEN_AI_SK")

url = "https://api.openai.com/v1/chat/completions"
header = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {
            "role": "user",
            "content": "What you think are the most important inventions of the 21st century?",
        },
    ],
    "temperature": 0.7,
}

response = requests.post(url, headers=header, json=data)

try:
    response.raise_for_status()
    reply = response.json()["choices"][0]["message"]["content"]
    print(f"Assistant:  {reply}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as e:
    print(f"An unexpectend error occurred: {e}")

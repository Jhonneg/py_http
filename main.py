import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPEN_AI_SK")

url = "https://api.openai.com/vi/chat/completions"
header = {"Authorization": f"Bearer:{api_key}", "Content-Type": "application/json"}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {
            "role",
            "user",
            "content",
            "What you think are the most important inventions of the 21st century",
        },
    ],
}

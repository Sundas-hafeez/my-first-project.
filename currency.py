import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(os.path.join(os.path.expanduser("~"), ".env"))
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a currency research assistant. Use web search for the latest exchange rates."},
        {"role": "user", "content": "Search the web now: what is 1 US dollar equal to in Pakistani rupees (PKR)? Give the latest verifiable rate and source URL."},
    ],
    tools=[{"type": "browser_search"}],
    tool_choice="required",
    temperature=0,
    max_completion_tokens=1200,
)

print(response.choices[0].message.content)

# Output (14 Oct 2026 ka rate):
# 1 US Dollar = 276.60 Pakistani Rupees (PKR)
# Source: XE Currency Converter
# URL: https://www.xe.com/en-us/currencyconverter/convert/?Amount=1&From=USD&To=PKR
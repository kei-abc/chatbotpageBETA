# mexc_solusdt_price.py
# pip install requests

import os
import requests

BASE_URL = "https://api.mexc.com"
SYMBOL = "SOLUSDT"

def get_solusdt_price(api_key: str | None = None) -> float:
    url = f"{BASE_URL}/api/v3/ticker/price"
    params = {"symbol": SYMBOL}

    headers = {}
    # API key is NOT required for this endpoint, but you can include it if you want.
    if api_key:
        headers["X-MEXC-APIKEY"] = api_key

    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    # Expected shape: {"symbol": "SOLUSDT", "price": "123.45"}
    return float(data["price"])

if __name__ == "__main__":
    # Set your key in environment variable (recommended):
    # Windows PowerShell:  $env:MEXC_API_KEY="your_key_here"
    # macOS/Linux bash:    export MEXC_API_KEY="your_key_here"
    api_key = os.getenv("MEXC_API_KEY")

    try:
        price = get_solusdt_price(api_key=api_key)
        print(f"SOL/USDT price: {price}")
    except requests.HTTPError as e:
        print("HTTP error:", e)
        if e.response is not None:
            print("Response:", e.response.text)
    except Exception as e:
        print("Error:", e)
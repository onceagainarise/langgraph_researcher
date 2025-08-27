from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus

load_dotenv()
api_key = os.getenv("BRIGHTDATA_API_KEY")

def _make_api_request(url, method="GET", **kwargs):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, **kwargs)
        else:
            response = requests.get(url, headers=headers, **kwargs)

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def serp_search(query, engine="google"):
    if engine == "google":
        base_url = "https://www.google.com/search"
    elif engine == "bing":
        base_url = "https://www.bing.com/search"
    else:
        raise ValueError(f"Unsupported search engine: {engine}")

    url = "https://api.brightdata.com/request"
    payload = {
        "zone": "ai_agent",
        "url": f"{base_url}?q={quote_plus(query)}&brd_json=1",
        "format": "raw"   # usually json not raw
    }

    full_response = _make_api_request(url, method="POST", json=payload)
    if not full_response:
        return None

    # adjust depending on actual API response schema
    extracted_data = {
        "knowledge": full_response.get("knowledge", {}),
        "organic": full_response.get("organic", []),
    }
    return extracted_data

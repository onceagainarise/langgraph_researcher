from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus
from snapshot_operations import poll_snapshot_status, download_snapshot

load_dotenv()
dataset_id="gd_lvz8ah06191smkebj4"
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
def _make_api_request_reddit(url, **kwargs):
    api_key = os.getenv("BRIGHTDATA_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
    except Exception as e:
        print(f"Unknown error: {e}")
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
        "format": "raw"   
    }

    full_response = _make_api_request(url, method="POST", json=payload)
    if not full_response:
        return None


    extracted_data = {
        "knowledge": full_response.get("knowledge", {}),
        "organic": full_response.get("organic", []),
    }
    return extracted_data

def _trigger_and_download_snapshot(trigger_url, params, data, operation_name="operation"):
    trigger_result = _make_api_request_reddit(trigger_url, params=params, json=data)
    if not trigger_result:
        return None

    snapshot_id = trigger_result.get("snapshot_id")
    if not snapshot_id:
        return None

    if not poll_snapshot_status(snapshot_id):
        return None

    raw_data = download_snapshot(snapshot_id)
    return raw_data
def _trigger_and_download_snapshot_retrieve(trigger_url, params, data, operation_name="operation"):
    trigger_result = _make_api_request(trigger_url, params=params, json=data)
    if not trigger_result:
        return None

    snapshot_id = trigger_result.get("snapshot_id")
    if not snapshot_id:
        return None

    if not poll_snapshot_status(snapshot_id):
        return None

    raw_data = download_snapshot(snapshot_id)
    return raw_data

def reddit_search_api(keyword, date="All time", sort_by="Hot", num_of_posts=5):
    trigger_url = "https://api.brightdata.com/datasets/v3/trigger"

    params = {
        "dataset_id": "gd_lvz8ah06191smkebj4",
        "include_errors": "true",
        "type": "discover_new",
        "discover_by": "keyword",
    }

    data = [
        {
            "keyword": keyword,
            "date": date,
            "sort_by": sort_by,
            "num_of_posts": num_of_posts,
        }
    ]

    raw_data = _trigger_and_download_snapshot(
        trigger_url, params, data, operation_name="reddit"
    )

    if not raw_data:
        return None

    parsed_data = []
    for post in raw_data:
        parsed_post = {
            "title": post.get("title"),
            "url": post.get("url")
        }
        parsed_data.append(parsed_post)

    return {"parsed_posts": parsed_data, "total_found": len(parsed_data)}

def reddit_post_retrieval(urls,days_back=10, load_all_replies=False,commit_limit=""):
    if not urls:
        return None
    trigger_url = "https://api.brightdata.com/datasets/v3/trigger"
    params = {
        "dataset_id": "gd_lvzdpsdlw09j6t702",
        "include_errors": "true",
    }
    data = [{"url": url, "days_back": days_back, "load_all_replies": load_all_replies, "commit_limit": commit_limit} for url in urls]
    raw_data = _trigger_and_download_snapshot_retrieve(
        trigger_url, params, data, operation_name="reddit comments"
    )
    if not raw_data:
        return None 
    parsed_comments =[]
    for comment in raw_data:
        parsed_comment={
            "comment_id": comment.get("comment_id"),
            "content": comment.get("comment"),
            "date": comment.get("date_posted"),            
        }
        parsed_comments.append(parsed_comment)
    return {"comments": parsed_comments, "total_retrieved": len(parsed_comments)} 

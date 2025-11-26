import requests
from src.crawler.stealth import stealth_delay, stealth_headers

def get_request(url):
    stealth_delay()
    return requests.get(url, headers=stealth_headers(), timeout=5)
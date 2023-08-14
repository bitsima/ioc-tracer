import requests

from typing import Optional

from ..config import google_lookup_api_key
from ..utils import logging_config


logger = logging_config.setup_logging()


def send_request(threat_entry: dict) -> Optional[bool]:
    """Sends a POST request to the Google's Lookup Api for malicious urls and fetches the response data.

    Args:
        threat_entry (dict): either {"url": "www.example.com"} or {"hash": "_sha256_digest_"}

    """
    url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={google_lookup_api_key}"
    payload = {
        "client": {"clientId": "ioc_tracer", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [threat_entry],
        },
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if len(data) != 0:
            return True
        else:
            return False

    else:
        return None


threat_entry = {"url": "https://infoamazonprime.com/"}
send_request(threat_entry)

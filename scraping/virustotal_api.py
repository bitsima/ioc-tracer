import requests

from typing import Union, Dict, Any, Optional

from ..config import virustotal_api_key
from ..utils import logging_config

logger = logging_config.setup_logging()


def check_file_hash(file_hash: str) -> Optional[Union[str, Dict[str, Any]]]:
    base_url = "https://www.virustotal.com/api/v3/files/"
    headers = {"x-apikey": virustotal_api_key}
    url = f"{base_url}{file_hash}"

    response = requests.get(url, headers=headers)

    logger.info(
        f"Sent a request to VirusTotal for file hash '{file_hash}', response status code: {response.status_code}"
    )
    if response.status_code == 200:
        return response.json()
    elif response.status_code != 404:
        logger.error(
            f"Error occurred while receiving the request from VirusTotal, status code: {response.status_code}"
        )

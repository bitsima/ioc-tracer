import requests

from typing import Union, Dict, Any, Optional, Tuple
from enum import Enum

from ..config import virustotal_api_key
from ..utils import logging_config


logger = logging_config.setup_logging()


class RequestType(Enum):
    DOMAIN = "domain"
    IP = "ip address"
    URL = "url address"
    HASH = "file hash"
    ANALYSIS = "analysis result"


function_mapping = {
    RequestType.DOMAIN: lambda *args: check_domain(*args),
    RequestType.IP: lambda *args: check_ip(*args),
    RequestType.URL: lambda *args: check_url(*args),
    RequestType.HASH: lambda *args: check_file_hash(*args),
    RequestType.ANALYSIS: lambda *args: get_analysis_results(*args),
}


# so we don't have to write request checks and logs in each function
def handle_request(
    request_type: RequestType, url: str, param: str
) -> Optional[Union[str, Dict[str, Any]]]:
    headers = {"x-apikey": virustotal_api_key}

    response = requests.get(url, headers=headers)

    logger.info(
        f"Sent a request to VirusTotal for '{request_type}' '{param}', response status code: {response.status_code}"
    )
    if response.status_code == 200:
        return response.json()
    elif response.status_code != 404:
        logger.error(
            f"Error occurred while receiving the response from VirusTotal from the '{request_type}' request, status code: {response.status_code}"
        )
        return None
    else:
        logger.warning(
            f"The requested '{request_type}' could not be found on VirusTotal, status code: 404"
        )
        return None


def get_analysis_results(id: str) -> Optional[Union[str, Dict[str, Any]]]:
    url = f"https://www.virustotal.com/api/v3/analyses/{id}"
    return handle_request(RequestType.ANALYSIS, url, id)["stats"]


def check_domain(domain: str) -> Optional[Tuple[str, str]]:
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    response = handle_request(RequestType.DOMAIN, url, domain)
    if response is not None:
        last_analysis_stats = response["data"]["attributes"]["last_analysis_stats"]
        return last_analysis_stats["malicious"], last_analysis_stats["harmless"]


def check_ip(ip_addr: str) -> Optional[Tuple[str, str]]:
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_addr}"
    response = handle_request(RequestType.IP, url, ip_addr)
    if response is not None:
        last_analysis_stats = response["data"]["attributes"]["last_analysis_stats"]
        return last_analysis_stats["malicious"], last_analysis_stats["harmless"]


def check_url(url_addr: str) -> Optional[Tuple[str, str]]:
    url = f"https://www.virustotal.com/api/v3/urls"
    response = handle_request(RequestType.URL, url, url_addr)
    if response is not None:
        analysis_id = response["data"]["id"]
        analysis_results = get_analysis_results(analysis_id)
        return analysis_results["malicious"], analysis_results["harmless"]


def check_file_hash(file_hash: str) -> Optional[Tuple[str, str]]:
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    response = handle_request(RequestType.HASH, url, file_hash)
    if response is not None:
        total_votes = response["data"]["total_votes"]
        return total_votes["malicious"], total_votes["harmless"]


selected = RequestType.HASH
parameter = "40041c3240eaa39da781a68f6a60f93577f1b0bbdaee5a0297d7fe329c073baa"
print(
    function_mapping[selected](parameter)
)  # if none an error occurred check logs uyarısını unutma

pass

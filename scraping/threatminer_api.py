import requests

from typing import Optional


def check_domain(domain: str) -> Optional[list[dict]]:
    passive_dns_url = f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=2"

    passive_dns_response = requests.get(passive_dns_url)
    if passive_dns_response.status_code == 200:
        data = passive_dns_response.json()
        return data["results"]

    else:
        return None


def check_ip(ip: str):
    passive_dns_url = f"https://api.threatminer.org/v2/host.php?q={ip}&rt=2"

    passive_dns_response = requests.get(passive_dns_url)
    if passive_dns_response.status_code == 200:
        data = passive_dns_response.json()
        return data["results"]

    else:
        return None

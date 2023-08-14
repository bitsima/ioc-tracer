import socket
from typing import Optional

from ..config import project_honeypot_bl_access_key


def bl_check(ip_address) -> Optional[dict]:
    query = (
        f"{project_honeypot_bl_access_key}.{reverse_ip(ip_address)}.dnsbl.httpbl.org"
    )

    try:
        response = socket.gethostbyname(query)
        # The format of the response is: "{127}.{days}.{threat_score}.{visitor_type}"
        response = response.split(".")
        match response[-1]:
            case "0":
                visitor = "search engine (0)"
            case "1":
                visitor = "suspicious (1)"
            case "2":
                visitor = "harvester (2)"
            case "3":
                visitor = "suspicious & harvester (3)"
            case "4":
                visitor = "comment spammer (4)"
            case "5":
                visitor = "suspicious & comment spammer (5)"
            case "6":
                visitor = "harvester & comment spammer (6)"
            case "7":
                visitor = "suspicious & harvester & comment spammer (7)"
            case default:
                return None

        return {
            "days_last_seen": response[1],
            "threat_score": response[2],
            "visitor_type": visitor,
        }

    except socket.gaierror:
        # If the DNS query fails, the IP is not blacklisted.
        return None


def reverse_ip(ip_address: str) -> str:
    octets = ip_address.split(".")
    reversed_octets = octets[::-1]
    reversed_ip = ".".join(reversed_octets)
    return reversed_ip

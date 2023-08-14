from urllib.parse import urlparse


with open("..data/whitelist.txt") as file:
    domains = file.readlines()


def in_whitelist(data) -> bool:
    if data in domains:
        return True
    parsed_url = urlparse(data)
    extracted_domain = parsed_url.netloc

    for domain in domains:
        if extracted_domain == domain:
            # subdomain check
            if parsed_url.hostname != domain:
                return False
            return True

from celery import Celery

from typing import Optional

from ..scraping import google_lookup_api
from ..scraping import virustotal_api
from ..scraping import threatminer_api
from ..scraping import alienvault_api
from ..scraping import project_honeypot_bl

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def get_result_google(data) -> dict:
    result = google_lookup_api.send_request(data)
    return {"google": result}


@app.task
def get_result_virustotal(data, type) -> Optional[dict]:
    match type:
        case "domain":
            result = virustotal_api.check_domain(data)
        case "ip":
            result = virustotal_api.check_ip(data)
        case "url":
            result = virustotal_api.check_url(data)
        case "file_hash":
            result = virustotal_api.check_file_hash(data)
        case default:
            return None
    return {"virustotal": result}


@app.task
def get_result_threatminer(data, type) -> Optional[dict]:
    match type:
        case "domain":
            result = threatminer_api.check_domain(data)
        case "ip":
            result = threatminer_api.check_ip(data)
        case default:
            return None
    return {"threatminer": result}


@app.task
def get_result_alienvault(data, type) -> Optional[dict]:
    match type:
        case "domain":
            result = alienvault_api.check_hostname(data)
        case "ip":
            result = alienvault_api.check_ip(data)
        case "url":
            result = alienvault_api.check_url(data)
        case "hash":
            result = alienvault_api.check_file_hash(data)
        case default:
            return None
    return {"alienvault": result}


@app.task
def get_result_project_honeypot(data) -> Optional[dict]:
    return project_honeypot_bl.bl_check(data)

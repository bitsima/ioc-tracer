import os
import re
import json

from . import git_utils
from ..config import db_init_repo
from ..config import cloned_repo_path
from ..config import processed_data_path
from ..config import processed_data_filename


cloned_repo_path = os.path.abspath(cloned_repo_path)
processed_data_path = (
    os.path.abspath(processed_data_path) + "/" + processed_data_filename
)

repo_abs_path = (
    cloned_repo_path + "/" + git_utils.clone_repository(db_init_repo, cloned_repo_path)
)

regex_patterns = {
    "hash": [r"^[0-9a-f]{32}$", r"^[0-9a-f]{40}$", r"^[0-9a-f]{64}$"],
    "ip": [
        r"^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.|\[\.\])){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?::[1-9][0-9]*)?$"
    ],
    "domain": [r"^[a-zA-Z0-9\-]+(?:\[[^\]]*\])?(?:\.[a-zA-Z0-9\-]+(?:\[[^\]]*\])?)+$"],
    "url": [
        r"^(?:(?:h(?:tt|xx)p[s]?|ftp)\[?:\]?\/)+\/?(?:[^:\/\s]+)(?:(?:\/\w+)*\/)(?:[\w\-\.]+[^#?\s]+)(?:.*)?(?:#[\w\-]+)?$"
    ],
}

processed_data = {"hash": [], "ip": [], "domain": [], "url": []}


def process_text_file(file_path: str):
    with open(file_path) as f:
        content = f.read()

    for ioc_type in regex_patterns:
        for pattern in regex_patterns[ioc_type]:
            matches = re.findall(pattern, content, re.MULTILINE)
            if matches:
                processed_data[ioc_type] += matches


for filename in os.scandir(repo_abs_path):
    if filename.is_dir():
        continue
    process_text_file(filename.path)

with open(processed_data_path, "w") as output_file:
    json.dump(processed_data, output_file)

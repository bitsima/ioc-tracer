import shutil
import os
import re
import json
import subprocess
from typing import Optional


db_init_repo = "https://github.com/BRANDEFENSE/IoC.git"


def clone_repository(repo_url: str, target_dir: str) -> Optional[str]:
    try:
        temp_list = os.listdir(cloned_repo_path)
        subprocess.call()
        subprocess.run(["git", "clone", repo_url, target_dir])

        return os.path.abspath(target_dir)
    except Exception as e:
        return None


# from ..utils import git_utils
# from ..config import db_init_repo


regex_patterns = {
    "hash": [r"^[0-9a-f]{32}$", r"^[0-9a-f]{40}$", r"^[0-9a-f]{64}$"],
    "ip": [
        r"^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.|\[\.\])){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?::[1-9][0-9]*)?$"
    ],
    "domain": [r"^[a-zA-Z0-9\-]+(?:\[[^\]]*\])?(?:\.[a-zA-Z0-9\-]+(?:\[[^\]]*\])?)+$"],
    "url": [
        r"/(?:https?|hxxp):(?:\[?\]?)\/\/(?:[\w-]+(?:\.[\w-]+)+|(?:(?:\d{1,3}\.){3}\d{1,3}))(?:\/\S*)?/i"
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


cloned_repo_path = "../data/raw_data/"
processed_data_path = "../data/processed_data.json"

clone_repository(db_init_repo, cloned_repo_path)

for root, dirs, files in os.walk(cloned_repo_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        process_text_file(file_path)

with open(processed_data_path, "w") as output_file:
    json.dump(processed_data, output_file)


"#YARA and Sigma Rules"
"#YARA"  # ```jsx ```
"#YARA Rules"  # rule blabla

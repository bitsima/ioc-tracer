import os
from typing import Optional

import logging_config

logger = logging_config.setup_logging()


def clone_repository(repo_url: str, target_dir: str) -> Optional[str]:
    repo_name = repo_url.rsplit("/", 1)[1].split(".")[0]
    if os.path.exists(target_dir + "/" + repo_name):
        os.system(
            f"git config --global --add safe.directory {target_dir + '/' + repo_name}"
        )
        os.system(f"cd {target_dir + '/' + repo_name} && git pull")
        return repo_name
    try:
        os.system(f"git clone {repo_url} {target_dir + '/' + repo_name}")
        return repo_name
    except Exception as e:
        logger.error(f"Failed to clone the repository: {str(e)}")
        return None

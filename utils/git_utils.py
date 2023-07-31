import subprocess
import os
from typing import Optional

import logging_config

logger = logging_config.setup_logging()


def clone_repository(repo_url: str, target_dir: str) -> Optional[str]:
    try:
        subprocess.run(["git", "clone", repo_url, target_dir])
        return os.path.abspath(target_dir)
    except Exception as e:
        logger.error(f"Failed to clone the repository: {str(e)}")
        return None

import subprocess
import os
from typing import Optional


def clone_repository(repo_url: str, target_dir: str) -> Optional[str]:
    try:
        subprocess.run(["git", "clone", repo_url, target_dir])
        return os.path.abspath(target_dir)
    except Exception as e:
        print(f"Failed to clone the repository: {str(e)}")
        return None

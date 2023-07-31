import hashlib


def hash_with_MD5(path_to_file: str) -> str:
    with open(path_to_file, "rb") as file:
        data = file.read()
        md5_returned = hashlib.md5(data).hexdigest()
    return md5_returned


def hash_with_SHA1(path_to_file: str) -> str:
    with open(path_to_file, "rb") as file:
        data = file.read()
        sha1_returned = hashlib.sha1(data).hexdigest()
    return sha1_returned


def hash_with_SHA256(path_to_file: str) -> str:
    with open(path_to_file, "rb") as file:
        data = file.read()
        sha256_returned = hashlib.sha256(data).hexdigest()
    return sha256_returned

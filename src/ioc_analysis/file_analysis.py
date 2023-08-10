from PyPDF2 import PdfReader
from exiftool import ExifToolHelper
import magic

from typing import Dict, Any

from ..helpers import file_hashing
from ...scraping import virustotal_api


async def analyze_file_type(path_to_file: str) -> str:
    file_type = magic.from_file(path_to_file)
    return file_type


async def get_media_exif_data(path_to_file: str) -> dict[str, dict[str]]:
    with ExifToolHelper() as et:
        meta_data = et.get_metadata(path_to_file)

    return meta_data


async def get_pdf_meta_data(path_to_file: str) -> dict[str, str]:
    meta_data = vars(PdfReader(path_to_file).metadata)
    return meta_data


async def check_hash(path_to_file: str) -> Dict[str, Any]:
    sha256_hash = file_hashing.hash_with_SHA256(path_to_file)
    sha256_response = virustotal_api.check_file_hash(sha256_hash)

    if sha256_response is not None:
        return sha256_response

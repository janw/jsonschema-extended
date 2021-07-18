from urllib.parse import urlparse
from uuid import UUID

from .europeanisms import is_blz  # noqa: F401
from .europeanisms import is_iban  # noqa: F401


def is_https_url(url_string):
    parsed = urlparse(url_string)
    return parsed.scheme == "https" and parsed.netloc


def is_http_url(url_string):
    parsed = urlparse(url_string)
    return parsed.scheme in {"http", "https"} and parsed.netloc


def is_uuid(uuid_string):
    UUID(uuid_string)

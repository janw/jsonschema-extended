import re
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
    return UUID(uuid_string)


# RFC3339 Duration regex licensed under Artistic License 2.0 from
# https://github.com/jhthorsen/json-validator
# /blob/49de68974b18f89091624b3a169898f60b8fe74a/lib/JSON/Validator/Formats.pm#L50
re_num = r"\d+(?:[,.]\d+)?"
re_sec = rf"{re_num}S"
re_min = rf"{re_num}M(?:{re_sec})?"
re_hour = rf"{re_num}H(?:{re_min})?"
re_day = rf"{re_num}D(?:{re_hour})?"
re_mon = rf"{re_num}M(?:{re_day})?"
re_year = rf"{re_num}Y(?:{re_mon})?"
re_week = rf"{re_num}W"
re_time = rf"T({re_hour}|{re_min}|{re_sec})"
re_date = rf"(?:{re_day}|{re_mon}|{re_year})(?:{re_time})?"
re_duration = re.compile(rf"^P(?:{re_date}|{re_time}|{re_week})$")


def is_rfc3339_duration(dur_string):
    return re_duration.match(dur_string) is not None

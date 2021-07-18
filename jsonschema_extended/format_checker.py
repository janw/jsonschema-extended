import re
import socket
import struct
from dataclasses import dataclass
from typing import Callable
from typing import Dict
from typing import Set
from typing import Tuple
from typing import Union

import idna
import jsonpointer
from jsonschema import _format
from jsonschema import FormatChecker

from . import checkers


@dataclass
class Check:
    func: Callable
    raises: Union[Exception, Tuple[Exception, ...]] = ()
    source: str = "custom"


AVAILABLE_CHECKS: Dict[str, Check] = {
    "idn-email": Check(
        _format.is_email,
        source="jsonschema",
    ),
    "email": Check(
        _format.is_email,
        source="jsonschema",
    ),
    "ipv4": Check(
        _format.is_ipv4,
        source="jsonschema",
    ),
    "ipv6": Check(
        _format.is_ipv6,
        (
            socket.error,
            struct.error,
            ValueError,
        ),
        source="jsonschema",
    ),
    "hostname": Check(
        _format.is_host_name,
        source="jsonschema",
    ),
    "idn-hostname": Check(
        _format.is_host_name,
        idna.IDNAError,
        source="jsonschema",
    ),
    "uri": Check(
        _format.is_uri,
        source="jsonschema",
    ),
    "uri-reference": Check(
        _format.is_uri_reference,
        ValueError,
        source="jsonschema",
    ),
    "date": Check(
        _format.is_date,
        ValueError,
        source="jsonschema",
    ),
    "date-time": Check(
        _format.is_datetime,
        source="jsonschema",
    ),
    "time": Check(
        _format.is_time,
        source="jsonschema",
    ),
    "regex": Check(
        _format.is_regex,
        re.error,
        source="jsonschema",
    ),
    "color": Check(
        _format.is_css21_color,
        (ValueError, TypeError),
        source="jsonschema",
    ),
    "json-pointer": Check(
        _format.is_json_pointer,
        jsonpointer.JsonPointerException,
        source="jsonschema",
    ),
    "relative-json-pointer": Check(
        _format.is_relative_json_pointer,
        jsonpointer.JsonPointerException,
        source="jsonschema",
    ),
    #
    #
    # Custom definitions
    "color3": Check(
        _format.is_css3_color,
        (ValueError, TypeError),
        source="jsonschema",
    ),
    "uuid": Check(
        checkers.is_uuid,
        ValueError,
        source="jsonschema_extended",
    ),
    "iban": Check(
        checkers.is_iban,
        source="jsonschema_extended",
    ),
    "de_blz": Check(
        checkers.is_blz,
        source="jsonschema_extended",
    ),
    "https": Check(
        checkers.is_https_url,
        source="jsonschema_extended",
    ),
    "http": Check(
        checkers.is_http_url,
        source="jsonschema_extended",
    ),
}

AVAILABLE_FORMATS = set(AVAILABLE_CHECKS)
AVAILABLE_SOURCES = {c.source for c in AVAILABLE_CHECKS.values()}

assert "custom" not in AVAILABLE_SOURCES


def create_format_checker(
    formats: Set[str] = AVAILABLE_FORMATS, sources: Set[str] = AVAILABLE_SOURCES
):
    checker = FormatChecker()
    for format, check in AVAILABLE_CHECKS.items():
        if format in formats and check.source in sources:
            checker.checks(format, raises=check.raises)(check.func)


extended_format_checker = create_format_checker()

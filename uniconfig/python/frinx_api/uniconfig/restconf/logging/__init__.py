# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from enum import Enum


class HttpMethod(Enum):
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    TRACE = 'TRACE'
    OPTIONS = 'OPTIONS'
    CONNECT = 'CONNECT'
    PATCH = 'PATCH'
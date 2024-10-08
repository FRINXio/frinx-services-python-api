# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hidden_http_headers: Optional[list[str]] = Field(None, alias='hidden-http-headers')
    """
    List of HTTP headers (names of the headers) which content is hidden in the logs.
    Names of the HTTP headers are not case-sensitive.
    """

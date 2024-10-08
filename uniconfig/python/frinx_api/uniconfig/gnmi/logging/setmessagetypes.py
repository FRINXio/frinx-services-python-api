# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from . import GnmiMessageType


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    message_types: Optional[list[GnmiMessageType]] = Field(None, alias='message-types')
    """
    List of gNMI message types, based on which the broker will log the message content.
    Names of the gNMI message types are not case-sensitive.
    """

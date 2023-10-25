# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from . import RpcStatus


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    device_list: Optional[list[str]] = Field(None, alias='device-list')
    """
    List of devices.
    """
    broker_identifier: str = Field(..., alias='broker-identifier')
    """
    Logging broker identifier.
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    message: Optional[str] = None
    """
    Information message about state of operation.
    """
    status: RpcStatus

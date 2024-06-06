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
    wait_for_output_timer: Optional[int] = Field(
        None, alias='wait-for-output-timer', ge=0, le=65535
    )
    """
    If no output is received during this time, then execute next command.
    Commands are sent without waiting for their echo.
    """
    error_check: Optional[bool] = Field(None, alias='error-check')
    """
    Flag for determine whether error handling will be enabled or not
    """
    command: str
    """
    Input configuration snippet (one or multiple commands separated by newline).
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: str
    """
    Status of the executed RPC.
    """

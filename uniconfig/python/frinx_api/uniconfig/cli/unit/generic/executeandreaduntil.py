# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

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
    last_output: str = Field(..., alias='last-output')
    """
    Expected last output of the last command - it is usually name of the prompt in the
    specific configuration mode.
    """
    command: str
    """
    Input configuration snippet (one or multiple commands separated by newline).
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    output: str
    """
    Output that is composed from the inputs/prompts/outputs of executed commands.
    """

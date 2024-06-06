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
    encryption_enabled: bool = Field(..., alias='encryption-enabled')
    """
    Is encryption enabled.
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    encryption_enabled_actual_status: Optional[bool] = Field(
        None, alias='encryption-enabled-actual-status'
    )
    """
    Actual encryption enabled status (true or false).
    """

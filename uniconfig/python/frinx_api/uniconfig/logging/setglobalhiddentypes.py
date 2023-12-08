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
    hidden_types: Optional[list[str]] = Field(None, alias='hidden-types')
    """
    Types filtered and hidden at logger ouptut.
    """

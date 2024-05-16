# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    key_id: Optional[list[str]] = Field(None, alias='key-id')

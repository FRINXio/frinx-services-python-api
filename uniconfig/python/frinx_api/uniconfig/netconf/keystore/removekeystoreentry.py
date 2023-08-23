# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    key_id: Optional[list[str]] = Field(None, alias='key-id')

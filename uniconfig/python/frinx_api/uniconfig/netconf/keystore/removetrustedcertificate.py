# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: Optional[list[str]] = None

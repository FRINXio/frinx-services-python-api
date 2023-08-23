# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from . import RepositoryCreationStatus


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    repository_name: Optional[str] = Field(None, alias='repository-name')
    """
    Name of the schema repository / directory that is used for persistence of YANG artifacts.
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    The cause of the failure.
    """
    status: RepositoryCreationStatus
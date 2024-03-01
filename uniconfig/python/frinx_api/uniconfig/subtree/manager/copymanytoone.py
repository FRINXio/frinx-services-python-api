# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from . import Datastore
from . import Operation


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    source_paths: Optional[list[str]] = Field(None, alias='source-paths')
    """
    Source paths to data which is put/merged under target nodes.
    """
    source_datastore: Optional[Datastore] = Field(None, alias='source-datastore')
    target_datastore: Optional[Datastore] = Field(None, alias='target-datastore')
    target_path: Optional[str] = Field(None, alias='target-path')
    """
    Target path under which data from source paths is put/merged.
    """
    operation: Optional[Operation] = None

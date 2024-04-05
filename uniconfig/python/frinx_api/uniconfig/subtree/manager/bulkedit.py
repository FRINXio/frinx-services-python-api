# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ...frinx import types


class EditItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    path: Optional[str] = None
    """
    Path to modified subtree. Path must be complaint to RFC-8040 and relative
    to parent top-level node 'configuration' container.
    """
    data: str
    """
    JSON-formatted subtree representing applied subtree configuration.
    """
    operation: types.DataTreeOperation


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: Optional[list[str]] = Field(None, alias='node-id')
    """
    List of nodes representing target nodes for list of modifications.
    """
    topology_id: str = Field(..., alias='topology-id')
    """
    Identifier of the topology which contains target nodes.
    """
    edit: Optional[list[EditItem]] = None
    """
    List of intended modifications.
    """

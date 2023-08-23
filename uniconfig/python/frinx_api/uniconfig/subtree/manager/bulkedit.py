# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types


class EditItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

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
    class Config:
        allow_population_by_field_name = True

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


class NodeResultItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node_id: Optional[str] = Field(None, alias='node-id')
    error_type: Optional[types.ErrorType] = Field(None, alias='error-type')
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message describing cause of error.
    """
    status: types.OperationResultType


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    List of target nodes with results.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')
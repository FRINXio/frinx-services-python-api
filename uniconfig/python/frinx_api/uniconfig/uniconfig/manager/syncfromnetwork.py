# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types


class TargetNodes(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node: Optional[list[str]] = None


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    check_timestamp: Optional[bool] = Field(None, alias='check-timestamp')
    """
    Perform timestamp comparison(last known to Uniconfig vs current timestamp on device)
    before loading all configuration from a device.
    """
    target_nodes: Optional[TargetNodes] = Field(
        None,
        alias='target-nodes',
        title='uniconfig.manager.targetuniconfignodesfields.TargetNodes',
    )


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


class NodeResults(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    Result of synchronization of configuration from network element
    to actual uniconfig node.
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_results: Optional[NodeResults] = Field(
        None,
        alias='node-results',
        title='uniconfig.manager.syncfromnetworkoutputfields.NodeResults',
    )
    """
    Individual result of sync for given nodes.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')

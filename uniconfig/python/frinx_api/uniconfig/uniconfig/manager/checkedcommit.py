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

    do_rollback: Optional[bool] = Field(None, alias='do-rollback')
    """
    Controls whether to roll back successfully configured devices in case of failure.
    Applies when configuring multiple devices within a single COMMIT RPC.
    By default, if N devices succeed, but the N+1 device fails,
    those N devices will be rolled back unless this option is set to false.
    The N+1 device will always be rolled back regardless of this option.
    """
    target_nodes: Optional[TargetNodes] = Field(
        None,
        alias='target-nodes',
        title='uniconfig.manager.targetuniconfigunistorenodesfields.TargetNodes',
    )


class NodeResultItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    configuration_status: Optional[types.OperationResultType] = Field(
        None, alias='configuration-status'
    )
    node_id: Optional[str] = Field(None, alias='node-id')
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message describing cause of error.
    """
    configuration: Optional[str] = None
    """
    Cli commands or netconf RPCs that needs to be executed
    on node to reach intended configuration state
    """
    rollback_status: Optional[types.OperationResultType] = Field(
        None, alias='rollback-status'
    )
    error_type: Optional[types.ErrorType] = Field(None, alias='error-type')


class NodeResults(BaseModel):
    """
    Result of configuration and rollback on each configured network element.
    """

    class Config:
        allow_population_by_field_name = True

    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    Result of configuration and rollback on the given node.
    Rollback status is empty if rollback was not executed.
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
        title='uniconfig.manager.commitoutputfields.NodeResults',
    )
    """
    Result of configuration and rollback on each configured network element.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')

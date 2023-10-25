# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ...frinx import types


class TargetNodes(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node: Optional[list[str]] = None


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    check_timestamp: Optional[bool] = Field(None, alias='check-timestamp')
    """
    Perform timestamp comparison(last known to Uniconfig vs current timestamp on device)
    before loading all configuration from a device.
    """
    skip_unreachable_nodes: Optional[bool] = Field(None, alias='skip-unreachable-nodes')
    """
    Option to skip nodes, that are unreachable at the time of commit. Other nodes will be committed
    """
    do_validate: Optional[bool] = Field(None, alias='do-validate')
    """
    Option to enable/disable validation at commit. Default value is true - validate
    """
    do_confirmed_commit: Optional[bool] = Field(None, alias='do-confirmed-commit')
    """
    Option to enable/disable confirmed-commit at commit. Default value is true - confirmed-commit
    """
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
        title='uniconfig.manager.targetuniconfignodesfields.TargetNodes',
    )


class NodeResultItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: Optional[str] = Field(None, alias='node-id')
    error_type: Optional[types.ErrorType] = Field(None, alias='error-type')
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message describing cause of error.
    """
    status: types.OperationResultType


class NodeResults(BaseModel):
    """
    Individual result of sync for given nodes.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    Result of synchronization of configuration to network element
    from actual uniconfig node.
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_results: Optional[NodeResults] = Field(
        None,
        alias='node-results',
        title='uniconfig.manager.synctonetworkoutputfields.NodeResults',
    )
    """
    Individual result of sync for given nodes.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')

# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
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
    skip_unreachable_nodes: Optional[bool] = Field(None, alias='skip-unreachable-nodes')
    """
    Option to skip nodes, that are unreachable at the time of commit. Other nodes will be commited
    """
    do_validate: Optional[bool] = Field(None, alias='do-validate')
    """
    Option to enable/disable validation at commit. Default value is true - validate
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    unreachable_nodes: Optional[list[str]] = Field(None, alias='unreachable-nodes')
    """
    List of unreachable node identifiers.
    """

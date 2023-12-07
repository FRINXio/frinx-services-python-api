# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ...frinx import types
from . import AdminState


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: str = Field(..., alias='node-id')
    """
    Node identifier of CLI/NETCONF/GNMI node.
    """
    admin_state: Optional[AdminState] = Field(None, alias='admin-state')


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Message that described occurred error during invocation of operation.
    """
    status: types.OperationResultType

# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from . import ConnectionType


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: str = Field(..., alias='node-id')
    """
    Node identifier of CLI/NETCONF/GNMI node.
    """
    connection_type: Optional[ConnectionType] = Field(None, alias='connection-type')

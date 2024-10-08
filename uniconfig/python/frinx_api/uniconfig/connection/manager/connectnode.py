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
    between_attempts_timeout: Optional[int] = Field(
        None, alias='between-attempts-timeout', ge=0, le=65535
    )
    """
    Initial timeout in seconds to wait between connection attempts.
    Will be multiplied by reconenction-attempts-multiplier with every additional attempt.
    Only supported for NETCONF nodes.
    """
    node_id: str = Field(..., alias='node-id')
    """
    Node identifier of CLI/NETCONF/GNMI node.
    """
    stream_name: Optional[str] = Field(None, alias='stream-name')
    """
    Name of a stream.
    """
    max_connection_attempts: Optional[int] = Field(
        None, alias='max-connection-attempts', ge=0, le=4294967295
    )
    """
    Maximum number of connection retries. Non positive value or null is interpreted as infinity.
    Only supported for NETCONF and CLI nodes.
    """

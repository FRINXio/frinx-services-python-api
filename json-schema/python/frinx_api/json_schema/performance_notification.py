# generated by datamodel-codegen

from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PerformanceMonitoringNotification(BaseModel):
    """
    Schema for performance monitoring notifications
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    nodeId: str
    """
    The name of the node.
    """
    identifier: str
    """
    The Identifier/path to data.
    """
    eventTime: str = Field(
        ...,
        pattern='^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{5}-\\d{2}:\\d{2}$',
    )
    """
    The timestamp when notification arrived.
    """
    body: dict[str, Any]
    """
    The data.
    """
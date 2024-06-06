# generated by datamodel-codegen

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    subscription_id: str = Field(..., alias='subscription-id')
    """
    Unique identifier of the subscription.
    """

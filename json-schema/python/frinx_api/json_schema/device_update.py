# generated by datamodel-codegen

from __future__ import annotations

from typing import Any
from typing import Optional

from pydantic import ConfigDict

from .device_parent import DeviceParentSchema


class DeviceUpdate(DeviceParentSchema):
    """
    Device update schema using merge behavior
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    device_size: Optional[str] = None
    device_type: Optional[str] = None
    device_address: Optional[str] = None
    device_port: Optional[int] = None
    service_state: Optional[str] = None
    mount_parameters: Optional[dict[str, Any]] = None
    vendor: Optional[str] = None
    model: Optional[str] = None
    blueprint_id: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    version: Optional[str] = None
    label_ids: Optional[list[Any]] = None
    device_name: str
    """
    The name of the device.
    """

# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class DeviceSize(Enum):
    """
    The size of the device.
    """

    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'


class ServiceState(Enum):
    """
    The state the device is in.
    """

    IN_SERVICE = 'IN_SERVICE'
    OUT_OF_SERVICE = 'OUT_OF_SERVICE'
    PLANNING = 'PLANNING'


class DeviceRegistration(BaseModel):
    """
    Device registration schema
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    device_name: str
    """
    The name of the device.
    """
    device_size: Optional[DeviceSize] = None
    """
    The size of the device.
    """
    device_type: Optional[str] = None
    """
    The type of the device.
    """
    device_address: Optional[str] = None
    """
    The address of the device.
    """
    device_port: Optional[int] = None
    """
    The port of the device.
    """
    zone_id: str
    """
    The zone ID of the device.
    """
    service_state: Optional[ServiceState] = None
    """
    The state the device is in.
    """
    mount_parameters: Optional[str] = None
    """
    Mount parameters.
    """
    vendor: Optional[str] = None
    """
    The device vendor.
    """
    model: Optional[str] = None
    """
    The model of the device.
    """
    blueprint_id: Optional[str] = None
    """
    The blueprint ID of the device.
    """
    username: Optional[str] = None
    """
    Device username.
    """
    password: Optional[str] = None
    """
    Device password
    """
    version: Optional[str] = None
    """
    The version of the device.
    """
    label_ids: Optional[list[str]] = None
    """
    Array of label IDs assigned to the device.
    """

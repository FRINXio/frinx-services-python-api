# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import RootModel


class TcpPortItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    end_port: Optional[int] = Field(None, alias='end-port', ge=0, le=65535)
    port: Optional[int] = Field(None, ge=0, le=65535)
    start_port: Optional[int] = Field(None, alias='start-port', ge=0, le=65535)


class Addres(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    end_ipv6_address: Optional[str] = Field(None, alias='end-ipv6-address')
    ip_address: Optional[str] = Field(None, alias='ip-address')
    """
    IP address in either IPv4 or IPv6 format, the syntax
    then determines which version is used
    """
    hostname: Optional[str] = None
    """
    Domain name
    """
    end_ipv4_address: Optional[str] = Field(None, alias='end-ipv4-address')
    start_ipv4_address: Optional[str] = Field(None, alias='start-ipv4-address')
    start_ipv6_address: Optional[str] = Field(None, alias='start-ipv6-address')
    network: Optional[str] = None
    """
    IP address with a subnet mask either in IPv4 or IPv6 format,
    the syntax then determines which version is used
    """


class UdpPortItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    end_port: Optional[int] = Field(None, alias='end-port', ge=0, le=65535)
    port: Optional[int] = Field(None, ge=0, le=65535)
    start_port: Optional[int] = Field(None, alias='start-port', ge=0, le=65535)


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    verify_host_reachability: Optional[bool] = Field(
        None, alias='verify-host-reachability'
    )
    """
    Check whether the host is reachable or not using ICMP protocol
    """
    tcp_port: Optional[list[TcpPortItem]] = Field(None, alias='tcp-port')
    address: Optional[list[Addres]] = None
    udp_port: Optional[list[UdpPortItem]] = Field(None, alias='udp-port')


class AvailableUdpPort(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: int = Field(..., ge=0, le=65535)


class UnavailableTcpPort(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: int = Field(..., ge=0, le=65535)


class AvailableTcpPort(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: int = Field(..., ge=0, le=65535)


class UnavailableUdpPort(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: int = Field(..., ge=0, le=65535)


class DeviceItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    is_host_reachable: Optional[bool] = Field(None, alias='is-host-reachable')
    """
    If the host is reachable or not using ICMP protocol
    """
    available_udp_ports: Optional[list[AvailableUdpPort]] = Field(
        None, alias='available-udp-ports'
    )
    """
    All the available UDP ports
    """
    host: Optional[str] = None
    """
    Host address either in IP (IPv4 or IPv6) format or in domain-name format
    """
    unavailable_tcp_ports: Optional[list[UnavailableTcpPort]] = Field(
        None, alias='unavailable-tcp-ports'
    )
    """
    TCP ports that are unreachable
    """
    available_tcp_ports: Optional[list[AvailableTcpPort]] = Field(
        None, alias='available-tcp-ports'
    )
    """
    All the available TCP ports
    """
    unavailable_udp_ports: Optional[list[UnavailableUdpPort]] = Field(
        None, alias='unavailable-udp-ports'
    )
    """
    UDP ports that are unreachable
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    device: Optional[list[DeviceItem]] = None

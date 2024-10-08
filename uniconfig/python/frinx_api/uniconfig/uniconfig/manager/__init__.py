# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum


class ConnectionType(Enum):
    """
    Type of the mountpoint that is awaited:
    a. cli - CLI mountpoint,
    b. netconf - NETCONF mountpoint,
    c. uniconfig-preferred-connection - Unified mounpoint (type of the southbound protocol
    is read from database).
    d. gnmi - gNMI mountpoint,
    e. snmp - snmp mountpoin

    """

    cli = 'cli'
    netconf = 'netconf'
    uniconfig_preferred_connection = 'uniconfig-preferred-connection'
    gnmi = 'gnmi'
    snmp = 'snmp'


class ContentType(Enum):
    """
    Content-type used only for mount-point read

    """

    config = 'config'
    state = 'state'
    operational = 'operational'
    all = 'all'

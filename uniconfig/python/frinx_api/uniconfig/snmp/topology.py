# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum


class AuthenticationProtocolEnumeration(Enum):
    """
    The authentication protocol that will be used when the security
    model is set to authNoPriv or authPriv.

    """

    MD5 = 'MD5'
    SHA_1 = 'SHA-1'
    SHA_224 = 'SHA-224'
    SHA_256 = 'SHA-256'
    SHA_384 = 'SHA-384'
    SHA_512 = 'SHA-512'


class PrivacyProtocolEnumeration(Enum):
    """
    The privacy protocol that will be used when the security model is set to authPriv

    """

    DES = 'DES'
    field_3DES = '3DES'
    AES_128 = 'AES-128'
    AES_192 = 'AES-192'
    AES_256 = 'AES-256'
    AES_192_3DESkeyext = 'AES-192-3DESkeyext'
    AES_256_3DESkeyext = 'AES-256-3DESkeyext'


class SnmpVersionEnumeration(Enum):
    """
    The SNMP version.

    """

    v1 = 'v1'
    v2c = 'v2c'
    v3 = 'v3'


class TransportTypeEnumeration(Enum):
    """
    The transport mapping.

    """

    udp = 'udp'
    tcp = 'tcp'

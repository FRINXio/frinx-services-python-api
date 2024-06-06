# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum


class AdminState(Enum):
    """
    Specifies the state when the device is installed.
    * locked - When a device is administratively locked, it is not possible
    to modify its configuration, and no changes are ever pushed
    to the device
    * unlocked - Device is assumed to be operational. All changes are attempted
    to be sent southbound. This is the default when a new device is created.
    * southbound_locked - It is possible to configure the device, but no changes are sent
    to the device. Useful admin mode when pre provisioning devices.

    """

    locked = 'locked'
    unlocked = 'unlocked'
    southbound_locked = 'southbound_locked'


class PublicKeyCipherType(Enum):
    """
    Algorithm used for generation of key-pair which public part is specified
    by 'public-key-path' leaf'.

    """

    RSA = 'RSA'
    CURVE25519 = 'CURVE25519'
    ECDSA = 'ECDSA'

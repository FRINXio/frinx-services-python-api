# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum


class NewEncryptionCipherType(Enum):
    """
    New algorithm that will be used to generation of public key.

    """

    RSA = 'RSA'
    CURVE25519 = 'CURVE25519'
    ECDSA = 'ECDSA'

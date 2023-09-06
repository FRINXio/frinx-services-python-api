# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from . import NewEncryptionCipherType


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    need_rotation_of_encryption_certificate: bool = Field(
        ..., alias='need-rotation-of-encryption-certificate'
    )
    """
    Requiring the rotation of the encryption certificate after changing encryption keys (true or false).
    """


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    new_decryption_private_key: Optional[str] = Field(
        None, alias='new-decryption-private-key'
    )
    """
    New private key that will be used to decryption of confidential data stored in database.
    """
    new_encryption_cipher_type: Optional[NewEncryptionCipherType] = Field(
        None, alias='new-encryption-cipher-type'
    )
    new_encryption_public_key: Optional[str] = Field(
        None, alias='new-encryption-public-key'
    )
    """
    New public key that will be used to encryption of selected leaves in configuration.
    """

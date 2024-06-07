# generated by datamodel-codegen

from __future__ import annotations

from enum import Enum


class RepositoryCreationStatus(Enum):
    """
    Status of the repository registration.
    * success - Repository has been successfully created and verified by building of schema context.
    * failed - Repository cannot be created due to the error (schema context cannot be build).

    """

    success = 'success'
    failed = 'failed'

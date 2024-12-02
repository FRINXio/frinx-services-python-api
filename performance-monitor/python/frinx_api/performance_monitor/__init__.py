# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2024-11-29T13:27:01+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional, TypeAlias

from pydantic import BaseModel, Field

Boolean: TypeAlias = bool
"""
The `Boolean` scalar type represents `true` or `false`.
"""


Datetime: TypeAlias = str
"""
Represents a datetime value.
"""


Float: TypeAlias = float
"""
The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).
"""


Int: TypeAlias = int
"""
The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.
"""


String: TypeAlias = str
"""
The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.
"""


class BucketUnit(Enum):
    """
    Bucket width unit types.
    """

    centuries = 'centuries'
    days = 'days'
    hours = 'hours'
    microseconds = 'microseconds'
    milliseconds = 'milliseconds'
    minutes = 'minutes'
    months = 'months'
    seconds = 'seconds'
    weeks = 'weeks'
    years = 'years'


class MetricsInterface(BaseModel):
    """
    Interface representing device metrics.
    """

    cpu: Optional[Float] = Field(
        None, description='The CPU utilization represented as a percentage.'
    )
    memory: Optional[Float] = Field(
        None, description='The memory utilization represented as a percentage.'
    )
    typename__: Optional[Literal['MetricsInterface']] = Field(
        'MetricsInterface', alias='__typename'
    )


class BulkUtilizationConnection(BaseModel):
    """
    Represents a paginated connection of utilization data for multiple devices.
    """

    metrics: List[MetricsEdge] = Field(
        ...,
        description='A list of metrics for multiple devices, each with associated cursor information.',
    )
    pageInfo: PageInfo = Field(
        ..., description='Information about the current page of results.'
    )
    typename__: Optional[Literal['BulkUtilizationConnection']] = Field(
        'BulkUtilizationConnection', alias='__typename'
    )


class CurrentUtilization(BaseModel):
    """
    Represents the current sources utilization of a single device.
    """

    device: String = Field(..., description='The unique identifier for the device.')
    deviceMetrics: MetricsNode = Field(..., description='The device metrics.')
    typename__: Optional[Literal['CurrentUtilization']] = Field(
        'CurrentUtilization', alias='__typename'
    )


class MetricsEdge(BaseModel):
    """
    Represents an edge in a paginated list of device metrics.
    """

    cursor: String = Field(..., description='A cursor for pagination.')
    deviceMetrics: List[MetricsWithDeviceNode] = Field(
        ..., description='A list of device metrics associated with a specific device.'
    )
    typename__: Optional[Literal['MetricsEdge']] = Field(
        'MetricsEdge', alias='__typename'
    )


class MetricsNode(MetricsInterface):
    """
    Base node type for metrics.
    """

    cpu: Optional[Float] = None
    memory: Optional[Float] = None
    typename__: Optional[Literal['MetricsNode']] = Field(
        'MetricsNode', alias='__typename'
    ) # type: ignore


class MetricsWithCursorNode(MetricsInterface):
    """
    Node type for metrics including a cursor.
    """

    cpu: Optional[Float] = None
    cursor: Optional[String] = Field(
        None, description='The cursor used for pagination.'
    )
    memory: Optional[Float] = None
    typename__: Optional[Literal['MetricsWithCursorNode']] = Field(
        'MetricsWithCursorNode', alias='__typename'
    ) # type: ignore


class MetricsWithDeviceNode(MetricsInterface):
    """
    Node type for metrics a device.
    """

    cpu: Optional[Float] = None
    device: String = Field(..., description='The device identifier.')
    memory: Optional[Float] = None
    typename__: Optional[Literal['MetricsWithDeviceNode']] = Field(
        'MetricsWithDeviceNode', alias='__typename'
    ) # type: ignore


class PageInfo(BaseModel):
    """
    Pagination metadata that is usually coupled to a returned list of objects.
    """

    endCursor: Optional[String] = Field(
        None, description='Pointer to the last object in the list.'
    )
    hasNextPage: Boolean = Field(
        ..., description='Indicates if there is a next object in the list.'
    )
    typename__: Optional[Literal['PageInfo']] = Field('PageInfo', alias='__typename')


class UtilizationConnection(BaseModel):
    """
    Represents a paginated connection of utilization data for a single device.
    """

    device: String = Field(..., description='The unique identifier for the device.')
    deviceMetrics: List[MetricsWithCursorNode] = Field(
        ..., description='A list of device metrics with associated cursor information.'
    )
    pageInfo: PageInfo = Field(
        ..., description='Information about the current page of results.'
    )
    typename__: Optional[Literal['UtilizationConnection']] = Field(
        'UtilizationConnection', alias='__typename'
    )


class BucketWidth(BaseModel):
    """
    Bucket width input type that wraps unit and value.
    These two values will be join to create 'bucket_width' parameter for TimescaleDB time_bucket function.
    """

    unit: BucketUnit
    value: Float
    typename__: Optional[Literal['BucketWidth']] = Field(
        'BucketWidth', alias='__typename'
    )

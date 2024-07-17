from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

Datetime: typing.TypeAlias = typing.Any
String: typing.TypeAlias = str
Float: typing.TypeAlias = float
Boolean: typing.TypeAlias = bool
Int: typing.TypeAlias = int


class BucketUnit(ENUM):
    MICROSECONDS = 'microseconds'
    MILLISECONDS = 'milliseconds'
    SECONDS = 'seconds'
    MINUTES = 'minutes'
    HOURS = 'hours'
    DAYS = 'days'
    WEEKS = 'weeks'
    MONTHS = 'months'
    YEARS = 'years'
    CENTURIES = 'centuries'


class BucketWidth(Input):
    unit: BucketUnit
    value: Float


class Percentage(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    usage: typing.Optional[Boolean] = Field(default=False)


class PercentagePayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    usage: typing.Optional[typing.Optional[Float]] = Field(default=None)


class PercentageInTimeSeries(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    usages: typing.Optional[PercentageInTime] = Field(default=None)


class PercentageInTimeSeriesPayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    usages: typing.Optional[typing.Optional[list[PercentageInTimePayload]]] = Field(default=None)


class PercentageInTime(Payload):
    time: typing.Optional[Boolean] = Field(default=False)
    usage: typing.Optional[Boolean] = Field(default=False)


class PercentageInTimePayload(BaseModel):
    time: typing.Optional[typing.Optional[Datetime]] = Field(default=None)
    usage: typing.Optional[typing.Optional[Float]] = Field(default=None)


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')


class PageInfoPayload(BaseModel):
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')


class CpuUsageConnections(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[CpuUsageEdges] = Field(default=None)


class CpuUsageConnectionsPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[CpuUsageEdgesPayload]]] = Field(default=None)


class CpuUsageConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    device: typing.Optional[Boolean] = Field(default=False)
    edges: typing.Optional[CpuUsageEdge] = Field(default=None)


class CpuUsageConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    edges: typing.Optional[typing.Optional[list[CpuUsageEdgePayload]]] = Field(default=None)


class CpuUsageEdges(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[CpuUsageNode] = Field(default=None)


class CpuUsageEdgesPayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[typing.Optional[list[CpuUsageNodePayload]]] = Field(default=None)


class CpuUsageEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[Boolean] = Field(default=False)


class CpuUsageEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[typing.Optional[Float]] = Field(default=None)


class CpuUsageNode(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    usage: typing.Optional[Boolean] = Field(default=False)


class CpuUsageNodePayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    usage: typing.Optional[typing.Optional[Float]] = Field(default=None)


class CurrentCpuUsageQuery(Query):
    _name: str = PrivateAttr('currentCpuUsage')
    device: String = Field(json_schema_extra={'type': 'String!'})
    payload: Percentage


class CurrentCpuUsagesQuery(Query):
    _name: str = PrivateAttr('currentCpuUsages')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    payload: Percentage


class CurrentMemoryUsageQuery(Query):
    _name: str = PrivateAttr('currentMemoryUsage')
    device: String = Field(json_schema_extra={'type': 'String!'})
    payload: Percentage


class CurrentMemoryUsagesQuery(Query):
    _name: str = PrivateAttr('currentMemoryUsages')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    payload: Percentage


class CpuUsageQuery(Query):
    _name: str = PrivateAttr('cpuUsage')
    device: String = Field(json_schema_extra={'type': 'String!'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: CpuUsageConnection


class CpuUsagesQuery(Query):
    _name: str = PrivateAttr('cpuUsages')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: CpuUsageConnections


class MemoryUsageQuery(Query):
    _name: str = PrivateAttr('memoryUsage')
    device: String = Field(json_schema_extra={'type': 'String!'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: MemoryUsageConnection


class MemoryUsagesQuery(Query):
    _name: str = PrivateAttr('memoryUsages')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: MemoryUsageConnections


class CurrentCpuUsageQueryResponse(BaseModel):
    data: typing.Optional[CurrentCpuUsageData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CurrentCpuUsageData(BaseModel):
    current_cpu_usage: PercentagePayload = Field(alias='currentCpuUsage')


class CurrentCpuUsagesQueryResponse(BaseModel):
    data: typing.Optional[CurrentCpuUsagesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CurrentCpuUsagesData(BaseModel):
    current_cpu_usages: typing.Optional[list[PercentagePayload]] = Field(alias='currentCpuUsages')


class CurrentMemoryUsageQueryResponse(BaseModel):
    data: typing.Optional[CurrentMemoryUsageData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CurrentMemoryUsageData(BaseModel):
    current_memory_usage: PercentagePayload = Field(alias='currentMemoryUsage')


class CurrentMemoryUsagesQueryResponse(BaseModel):
    data: typing.Optional[CurrentMemoryUsagesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CurrentMemoryUsagesData(BaseModel):
    current_memory_usages: typing.Optional[list[PercentagePayload]] = Field(alias='currentMemoryUsages')


class CpuUsageQueryResponse(BaseModel):
    data: typing.Optional[CpuUsageData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CpuUsageData(BaseModel):
    cpu_usage: CpuUsageConnectionPayload = Field(alias='cpuUsage')


class CpuUsagesQueryResponse(BaseModel):
    data: typing.Optional[CpuUsagesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CpuUsagesData(BaseModel):
    cpu_usages: CpuUsageConnectionsPayload = Field(alias='cpuUsages')


class MemoryUsageQueryResponse(BaseModel):
    data: typing.Optional[MemoryUsageData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class MemoryUsageData(BaseModel):
    memory_usage: MemoryUsageConnectionPayload = Field(alias='memoryUsage')


class MemoryUsagesQueryResponse(BaseModel):
    data: typing.Optional[MemoryUsagesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class MemoryUsagesData(BaseModel):
    memory_usages: MemoryUsageConnectionsPayload = Field(alias='memoryUsages')


class MemoryUsageConnections(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[MemoryUsageEdges] = Field(default=None)


class MemoryUsageConnectionsPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[MemoryUsageEdgesPayload]]] = Field(default=None)


class MemoryUsageConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    device: typing.Optional[Boolean] = Field(default=False)
    edges: typing.Optional[MemoryUsageEdge] = Field(default=None)


class MemoryUsageConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    edges: typing.Optional[typing.Optional[list[MemoryUsageEdgePayload]]] = Field(default=None)


class MemoryUsageEdges(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[MemoryUsageNode] = Field(default=None)


class MemoryUsageEdgesPayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[typing.Optional[list[MemoryUsageNodePayload]]] = Field(default=None)


class MemoryUsageEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[Boolean] = Field(default=False)


class MemoryUsageEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[typing.Optional[Float]] = Field(default=None)


class MemoryUsageNode(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    usage: typing.Optional[Boolean] = Field(default=False)


class MemoryUsageNodePayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    usage: typing.Optional[typing.Optional[Float]] = Field(default=None)


BucketWidth.model_rebuild()
Percentage.model_rebuild()
PercentagePayload.model_rebuild()
PercentageInTimeSeries.model_rebuild()
PercentageInTimeSeriesPayload.model_rebuild()
PercentageInTime.model_rebuild()
PercentageInTimePayload.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
CpuUsageConnections.model_rebuild()
CpuUsageConnectionsPayload.model_rebuild()
CpuUsageConnection.model_rebuild()
CpuUsageConnectionPayload.model_rebuild()
CpuUsageEdges.model_rebuild()
CpuUsageEdgesPayload.model_rebuild()
CpuUsageEdge.model_rebuild()
CpuUsageEdgePayload.model_rebuild()
CpuUsageNode.model_rebuild()
CpuUsageNodePayload.model_rebuild()
CurrentCpuUsageQuery.model_rebuild()
CurrentCpuUsagesQuery.model_rebuild()
CurrentMemoryUsageQuery.model_rebuild()
CurrentMemoryUsagesQuery.model_rebuild()
CpuUsageQuery.model_rebuild()
CpuUsagesQuery.model_rebuild()
MemoryUsageQuery.model_rebuild()
MemoryUsagesQuery.model_rebuild()
CurrentCpuUsageQueryResponse.model_rebuild()
CurrentCpuUsageData.model_rebuild()
CurrentCpuUsagesQueryResponse.model_rebuild()
CurrentCpuUsagesData.model_rebuild()
CurrentMemoryUsageQueryResponse.model_rebuild()
CurrentMemoryUsageData.model_rebuild()
CurrentMemoryUsagesQueryResponse.model_rebuild()
CurrentMemoryUsagesData.model_rebuild()
CpuUsageQueryResponse.model_rebuild()
CpuUsageData.model_rebuild()
CpuUsagesQueryResponse.model_rebuild()
CpuUsagesData.model_rebuild()
MemoryUsageQueryResponse.model_rebuild()
MemoryUsageData.model_rebuild()
MemoryUsagesQueryResponse.model_rebuild()
MemoryUsagesData.model_rebuild()
MemoryUsageConnections.model_rebuild()
MemoryUsageConnectionsPayload.model_rebuild()
MemoryUsageConnection.model_rebuild()
MemoryUsageConnectionPayload.model_rebuild()
MemoryUsageEdges.model_rebuild()
MemoryUsageEdgesPayload.model_rebuild()
MemoryUsageEdge.model_rebuild()
MemoryUsageEdgePayload.model_rebuild()
MemoryUsageNode.model_rebuild()
MemoryUsageNodePayload.model_rebuild()

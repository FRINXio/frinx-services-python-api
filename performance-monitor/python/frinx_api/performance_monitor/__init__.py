from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

Datetime: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
Boolean: typing.TypeAlias = bool
String: typing.TypeAlias = str
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


class MetricsInterface(Interface):
    cpu: typing.Optional[Boolean] = Field(default=None)
    memory: typing.Optional[Boolean] = Field(default=None)


class BucketWidth(Input):
    unit: BucketUnit
    value: Float


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')


class PageInfoPayload(BaseModel):
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')


class CurrentUtilizationQuery(Query):
    _name: str = PrivateAttr('currentUtilization')
    device: String = Field(json_schema_extra={'type': 'String!'})
    payload: CurrentUtilization


class BulkCurrentUtilizationQuery(Query):
    _name: str = PrivateAttr('bulkCurrentUtilization')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    payload: CurrentUtilization


class UtilizationQuery(Query):
    _name: str = PrivateAttr('utilization')
    device: String = Field(json_schema_extra={'type': 'String!'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: UtilizationConnection


class BulkUtilizationQuery(Query):
    _name: str = PrivateAttr('bulkUtilization')
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    bucket_width: typing.Optional[BucketWidth] = Field(default=None, json_schema_extra={'type': 'BucketWidth'})
    start_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    end_time: typing.Optional[Datetime] = Field(default=None, json_schema_extra={'type': 'Datetime'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: BulkUtilizationConnection


class CurrentUtilizationQueryResponse(BaseModel):
    data: typing.Optional[CurrentUtilizationData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CurrentUtilizationData(BaseModel):
    current_utilization: CurrentUtilizationPayload = Field(alias='currentUtilization')


class BulkCurrentUtilizationQueryResponse(BaseModel):
    data: typing.Optional[BulkCurrentUtilizationData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class BulkCurrentUtilizationData(BaseModel):
    bulk_current_utilization: typing.Optional[list[CurrentUtilizationPayload]] = Field(alias='bulkCurrentUtilization')


class UtilizationQueryResponse(BaseModel):
    data: typing.Optional[UtilizationData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UtilizationData(BaseModel):
    utilization: UtilizationConnectionPayload


class BulkUtilizationQueryResponse(BaseModel):
    data: typing.Optional[BulkUtilizationData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class BulkUtilizationData(BaseModel):
    bulk_utilization: BulkUtilizationConnectionPayload = Field(alias='bulkUtilization')


class MetricsNode(Payload):
    cpu: typing.Optional[Boolean] = Field(default=False)
    memory: typing.Optional[Boolean] = Field(default=False)


class MetricsNodePayload(BaseModel):
    cpu: typing.Optional[typing.Optional[Float]] = Field(default=None)
    memory: typing.Optional[typing.Optional[Float]] = Field(default=None)


class MetricsWithCursorNode(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    cpu: typing.Optional[Boolean] = Field(default=False)
    memory: typing.Optional[Boolean] = Field(default=False)


class MetricsWithCursorNodePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    cpu: typing.Optional[typing.Optional[Float]] = Field(default=None)
    memory: typing.Optional[typing.Optional[Float]] = Field(default=None)


class MetricsWithDeviceNode(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    cpu: typing.Optional[Boolean] = Field(default=False)
    memory: typing.Optional[Boolean] = Field(default=False)


class MetricsWithDeviceNodePayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    cpu: typing.Optional[typing.Optional[Float]] = Field(default=None)
    memory: typing.Optional[typing.Optional[Float]] = Field(default=None)


class CurrentUtilization(Payload):
    device: typing.Optional[Boolean] = Field(default=False)
    device_metrics: typing.Optional[MetricsNode] = Field(default=None, alias='deviceMetrics')


class CurrentUtilizationPayload(BaseModel):
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    device_metrics: typing.Optional[MetricsNodePayload] = Field(default=None, alias='deviceMetrics')


class UtilizationConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    device: typing.Optional[Boolean] = Field(default=False)
    device_metrics: typing.Optional[MetricsWithCursorNode] = Field(default=None, alias='deviceMetrics')


class UtilizationConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    device: typing.Optional[typing.Optional[String]] = Field(default=None)
    device_metrics: typing.Optional[typing.Optional[list[MetricsWithCursorNodePayload]]] = Field(default=None, alias='deviceMetrics')


class BulkUtilizationConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    metrics: typing.Optional[MetricsEdge] = Field(default=None)


class BulkUtilizationConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    metrics: typing.Optional[typing.Optional[list[MetricsEdgePayload]]] = Field(default=None)


class MetricsEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    device_metrics: typing.Optional[MetricsWithDeviceNode] = Field(default=None, alias='deviceMetrics')


class MetricsEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    device_metrics: typing.Optional[typing.Optional[list[MetricsWithDeviceNodePayload]]] = Field(default=None, alias='deviceMetrics')


MetricsInterface.model_rebuild()
BucketWidth.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
CurrentUtilizationQuery.model_rebuild()
BulkCurrentUtilizationQuery.model_rebuild()
UtilizationQuery.model_rebuild()
BulkUtilizationQuery.model_rebuild()
CurrentUtilizationQueryResponse.model_rebuild()
CurrentUtilizationData.model_rebuild()
BulkCurrentUtilizationQueryResponse.model_rebuild()
BulkCurrentUtilizationData.model_rebuild()
UtilizationQueryResponse.model_rebuild()
UtilizationData.model_rebuild()
BulkUtilizationQueryResponse.model_rebuild()
BulkUtilizationData.model_rebuild()
MetricsNode.model_rebuild()
MetricsNodePayload.model_rebuild()
MetricsWithCursorNode.model_rebuild()
MetricsWithCursorNodePayload.model_rebuild()
MetricsWithDeviceNode.model_rebuild()
MetricsWithDeviceNodePayload.model_rebuild()
CurrentUtilization.model_rebuild()
CurrentUtilizationPayload.model_rebuild()
UtilizationConnection.model_rebuild()
UtilizationConnectionPayload.model_rebuild()
BulkUtilizationConnection.model_rebuild()
BulkUtilizationConnectionPayload.model_rebuild()
MetricsEdge.model_rebuild()
MetricsEdgePayload.model_rebuild()

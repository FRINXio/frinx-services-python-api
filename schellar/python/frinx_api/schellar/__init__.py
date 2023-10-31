from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

Boolean: typing.TypeAlias = bool
DateTime: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
JSON: typing.TypeAlias = typing.Any
String: typing.TypeAlias = str


class Status(ENUM):
    UNKNOWN = 'UNKNOWN'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    PAUSED = 'PAUSED'
    RUNNING = 'RUNNING'
    TERMINATED = 'TERMINATED'
    TIMED_OUT = 'TIMED_OUT'


class CreateScheduleInput(Input):
    name: String
    workflow_name: String = Field(alias='workflowName')
    workflow_version: String = Field(alias='workflowVersion')
    cron_string: String = Field(alias='cronString')
    enabled: typing.Optional[Boolean] = Field(default=None)
    parallel_runs: typing.Optional[Boolean] = Field(default=None, alias='parallelRuns')
    workflow_context: typing.Optional[String] = Field(default=None, alias='workflowContext')
    from_date: typing.Optional[DateTime] = Field(default=None, alias='fromDate')
    to_date: typing.Optional[DateTime] = Field(default=None, alias='toDate')


class SchedulesFilterInput(Input):
    workflow_name: String = Field(alias='workflowName')
    workflow_version: String = Field(alias='workflowVersion')


class UpdateScheduleInput(Input):
    workflow_name: typing.Optional[String] = Field(default=None, alias='workflowName')
    workflow_version: typing.Optional[String] = Field(default=None, alias='workflowVersion')
    cron_string: typing.Optional[String] = Field(default=None, alias='cronString')
    enabled: typing.Optional[Boolean] = Field(default=None)
    parallel_runs: typing.Optional[Boolean] = Field(default=None, alias='parallelRuns')
    workflow_context: typing.Optional[String] = Field(default=None, alias='workflowContext')
    from_date: typing.Optional[DateTime] = Field(default=None, alias='fromDate')
    to_date: typing.Optional[DateTime] = Field(default=None, alias='toDate')


class CreateScheduleMutation(Mutation):
    _name: str = PrivateAttr('createSchedule')
    input: CreateScheduleInput = Field(json_schema_extra={'type': 'CreateScheduleInput!'})
    payload: Schedule


class UpdateScheduleMutation(Mutation):
    _name: str = PrivateAttr('updateSchedule')
    name: String = Field(json_schema_extra={'type': 'String!'})
    input: UpdateScheduleInput = Field(json_schema_extra={'type': 'UpdateScheduleInput!'})
    payload: Schedule


class DeleteScheduleMutation(Mutation):
    _name: str = PrivateAttr('deleteSchedule')
    name: String = Field(json_schema_extra={'type': 'String!'})
    payload: Boolean


class CreateScheduleMutationResponse(BaseModel):
    data: typing.Optional[CreateScheduleData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateScheduleData(BaseModel):
    create_schedule: SchedulePayload = Field(alias='createSchedule')


class UpdateScheduleMutationResponse(BaseModel):
    data: typing.Optional[UpdateScheduleData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateScheduleData(BaseModel):
    update_schedule: SchedulePayload = Field(alias='updateSchedule')


class DeleteScheduleMutationResponse(BaseModel):
    data: typing.Optional[DeleteScheduleData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteScheduleData(BaseModel):
    delete_schedule: typing.Optional[Boolean] = Field(alias='deleteSchedule')


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    has_previous_page: typing.Optional[Boolean] = Field(default=False, alias='hasPreviousPage')
    start_cursor: typing.Optional[Boolean] = Field(default=False, alias='startCursor')
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')


class PageInfoPayload(BaseModel):
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasPreviousPage')
    start_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='startCursor')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')


class ScheduleQuery(Query):
    _name: str = PrivateAttr('schedule')
    name: String = Field(json_schema_extra={'type': 'String!'})
    payload: Schedule


class SchedulesQuery(Query):
    _name: str = PrivateAttr('schedules')
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    filter: typing.Optional[SchedulesFilterInput] = Field(default=None, json_schema_extra={'type': 'SchedulesFilterInput'})
    payload: ScheduleConnection


class ScheduleQueryResponse(BaseModel):
    data: typing.Optional[ScheduleData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ScheduleData(BaseModel):
    schedule: typing.Optional[SchedulePayload]


class SchedulesQueryResponse(BaseModel):
    data: typing.Optional[SchedulesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SchedulesData(BaseModel):
    schedules: typing.Optional[ScheduleConnectionPayload]


class Schedule(Payload):
    name: typing.Optional[Boolean] = Field(default=False)
    enabled: typing.Optional[Boolean] = Field(default=False)
    parallel_runs: typing.Optional[Boolean] = Field(default=False, alias='parallelRuns')
    workflow_name: typing.Optional[Boolean] = Field(default=False, alias='workflowName')
    workflow_version: typing.Optional[Boolean] = Field(default=False, alias='workflowVersion')
    cron_string: typing.Optional[Boolean] = Field(default=False, alias='cronString')
    workflow_context: typing.Optional[Boolean] = Field(default=False, alias='workflowContext')
    from_date: typing.Optional[Boolean] = Field(default=False, alias='fromDate')
    to_date: typing.Optional[Boolean] = Field(default=False, alias='toDate')
    status: typing.Optional[Boolean] = Field(default=False)


class SchedulePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    enabled: typing.Optional[typing.Optional[Boolean]] = Field(default=None)
    parallel_runs: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='parallelRuns')
    workflow_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='workflowName')
    workflow_version: typing.Optional[typing.Optional[String]] = Field(default=None, alias='workflowVersion')
    cron_string: typing.Optional[typing.Optional[String]] = Field(default=None, alias='cronString')
    workflow_context: typing.Optional[typing.Optional[String]] = Field(default=None, alias='workflowContext')
    from_date: typing.Optional[typing.Optional[DateTime]] = Field(default=None, alias='fromDate')
    to_date: typing.Optional[typing.Optional[DateTime]] = Field(default=None, alias='toDate')
    status: typing.Optional[typing.Optional[Status]] = Field(default=None)


class ScheduleConnection(Payload):
    edges: typing.Optional[ScheduleEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class ScheduleConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ScheduleEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class ScheduleEdge(Payload):
    node: typing.Optional[Schedule] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class ScheduleEdgePayload(BaseModel):
    node: typing.Optional[SchedulePayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


CreateScheduleInput.model_rebuild()
SchedulesFilterInput.model_rebuild()
UpdateScheduleInput.model_rebuild()
CreateScheduleMutation.model_rebuild()
UpdateScheduleMutation.model_rebuild()
DeleteScheduleMutation.model_rebuild()
CreateScheduleMutationResponse.model_rebuild()
CreateScheduleData.model_rebuild()
UpdateScheduleMutationResponse.model_rebuild()
UpdateScheduleData.model_rebuild()
DeleteScheduleMutationResponse.model_rebuild()
DeleteScheduleData.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
ScheduleQuery.model_rebuild()
SchedulesQuery.model_rebuild()
ScheduleQueryResponse.model_rebuild()
ScheduleData.model_rebuild()
SchedulesQueryResponse.model_rebuild()
SchedulesData.model_rebuild()
Schedule.model_rebuild()
SchedulePayload.model_rebuild()
ScheduleConnection.model_rebuild()
ScheduleConnectionPayload.model_rebuild()
ScheduleEdge.model_rebuild()
ScheduleEdgePayload.model_rebuild()

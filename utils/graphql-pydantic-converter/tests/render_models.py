import typing

from pydantic import Field
from pydantic import PrivateAttr

from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query

Boolean: typing.TypeAlias = bool
Cursor: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Map: typing.TypeAlias = dict[str, typing.Any]
String: typing.TypeAlias = str


class TagAnd(Input):
    matches_all: typing.Optional[list[String]] = Field(default=None, alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(default=None, alias='matchesAny')


class OutputCursor(Payload):
    id: typing.Optional[Boolean] = Field(alias='ID', default=False)


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[Boolean] = Field(alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='startCursor')


class AllocationStrategy(Payload):
    description: typing.Optional[Boolean] = Field(alias='Description', default=False)
    lang: typing.Optional[Boolean] = Field(alias='Lang', default=False)
    name: typing.Optional[Boolean] = Field(alias='Name', default=False)
    script: typing.Optional[Boolean] = Field(alias='Script', default=False)
    id: typing.Optional[Boolean] = Field(default=False)


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(default=None,
                                                                     alias='AllocationStrategy')
    name: typing.Optional[Boolean] = Field(alias='Name', default=False)
    pool_properties: typing.Optional[Boolean] = Field(alias='PoolProperties', default=False)
    pool_type: typing.Optional[Boolean] = Field(alias='PoolType', default=False)
    id: typing.Optional[Boolean] = Field(default=False)


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(default=None)
    node: typing.Optional[ResourcePool] = Field(default=None)


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount',)


class SearchPoolsByTagsQuery(Query):
    _name: str = PrivateAttr('SearchPoolsByTags')
    tags: typing.Optional[TagOr] = Field(default=None, json_schema_extra={'type': 'TagOr'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    payload: ResourcePoolConnection


class SchedulesFilterInput(Input):
    workflow_name: String = Field(alias='workflowName')
    workflow_version: String = Field(alias='workflowVersion')


class PageInfoSchedule(Payload):
    has_next_page: typing.Optional[Boolean] = Field(alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[Boolean] = Field(alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[Boolean] = Field(alias='startCursor', default=False)
    end_cursor: typing.Optional[Boolean] = Field(alias='endCursor', default=False)


class Schedule(Payload):
    name: typing.Optional[Boolean] = Field(default=False)
    enabled: typing.Optional[Boolean] = Field(default=False)
    parallel_runs: typing.Optional[Boolean] = Field(alias='parallelRuns', default=False)
    workflow_name: typing.Optional[Boolean] = Field(alias='workflowName', default=False)
    workflow_version: typing.Optional[Boolean] = Field(alias='workflowVersion', default=False)
    cron_string: typing.Optional[Boolean] = Field(alias='cronString', default=False)
    workflow_context: typing.Optional[Boolean] = Field(alias='workflowContext', default=False)
    from_date: typing.Optional[Boolean] = Field(alias='fromDate', default=False)
    to_date: typing.Optional[Boolean] = Field(alias='toDate', default=False)
    status: typing.Optional[Boolean] = Field(default=False)


class ScheduleEdge(Payload):
    node: typing.Optional[Schedule] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class ScheduleConnection(Payload):
    edges: typing.Optional[ScheduleEdge] = Field(default=None)
    page_info: typing.Optional[PageInfoSchedule] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(alias='totalCount', default=False)


class SchedulesQuery(Query):
    _name: str = PrivateAttr('schedules')
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    filter: typing.Optional[SchedulesFilterInput] = Field(
        default=None, json_schema_extra={'type': 'SchedulesFilterInput'}
    )
    payload: ScheduleConnection


class Resource(Payload):
    description: typing.Optional[Boolean] = Field(default=False, alias='Description')
    nested_pool: typing.Optional[ResourcePool] = Field(default=None, alias='NestedPool')
    parent_pool: typing.Optional[ResourcePool] = Field(default=None, alias='ParentPool')
    properties: typing.Optional[Boolean] = Field(default=False, alias='Properties')
    alternative_id: typing.Optional[Boolean] = Field(default=False, alias='AlternativeId')
    id: typing.Optional[Boolean] = Field(default=False)


class ClaimResourceMutation(Mutation):
    _name: str = PrivateAttr('ClaimResource')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    description: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    user_input: Map = Field(alias='userInput', json_schema_extra={'type': 'Map!'})
    payload: Resource


class CreateScheduleInput(Input):
    name: String
    workflow_name: String = Field(alias='workflowName')
    workflow_version: String = Field(alias='workflowVersion')
    cron_string: String = Field(alias='cronString')
    enabled: typing.Optional[Boolean] = Field(default=None)
    parallel_runs: typing.Optional[Boolean] = Field(default=None, alias='parallelRuns')
    workflow_context: typing.Optional[String] = Field(default=None, alias='workflowContext')
    from_date: typing.Optional[typing.Any] = Field(default=None, alias='fromDate')
    to_date: typing.Optional[typing.Any] = Field(default=None, alias='toDate')


class CreateScheduleMutation(Mutation):
    _name: str = PrivateAttr('createSchedule')
    input: CreateScheduleInput = Field(json_schema_extra={'type': 'CreateScheduleInput!'})
    payload: Schedule

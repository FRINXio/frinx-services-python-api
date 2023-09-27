import typing

from pydantic import Field

from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query


class TagAnd(Input):
    matches_all: typing.Optional[list[str]] = Field(alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(alias='matchesAny')


class OutputCursor(Payload):
    id: typing.Optional[bool] = Field(response='str', alias='ID', default=True)


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='endCursor')
    has_next_page: typing.Optional[bool] = Field(response='bool', alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[bool] = Field(response='bool', alias='hasPreviousPage',
                                                     default=True)
    start_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='startCursor')


class AllocationStrategy(Payload):
    description: typing.Optional[bool] = Field(response='str', alias='Description', default=True)
    lang: typing.Optional[bool] = Field(response='AllocationStrategyLang', alias='Lang', default=True)
    name: typing.Optional[bool] = Field(response='str', alias='Name', default=True)
    script: typing.Optional[bool] = Field(response='str', alias='Script', default=True)
    id: typing.Optional[bool] = Field(response='ID', default=True)


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy',
                                                                     alias='AllocationStrategy')
    name: typing.Optional[bool] = Field(response='str', alias='Name', default=True)
    pool_properties: typing.Optional[bool] = Field(response='Map', alias='PoolProperties', default=True)
    pool_type: typing.Optional[bool] = Field(response='PoolType', alias='PoolType', default=True)
    id: typing.Optional[bool] = Field(response='ID', default=True)


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor')
    node: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(response='ResourcePoolEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[bool] = Field(response='Int', alias='totalCount', default=True)


class SearchPoolsByTagsQuery(Query):
    _name: str = Field('SearchPoolsByTags', const=True)
    tags: typing.Optional[TagOr]
    first: typing.Optional[int]
    last: typing.Optional[int]
    before: typing.Optional[typing.Any]
    after: typing.Optional[typing.Any]
    payload: ResourcePoolConnection


class SchedulesFilterInput(Input):
    workflow_name: str = Field(alias='workflowName')
    workflow_version: str = Field(alias='workflowVersion')


class PageInfoSchedule(Payload):
    has_next_page: typing.Optional[bool] = Field(response='bool', alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[bool] = Field(response='bool', alias='hasPreviousPage', default=True)
    start_cursor: typing.Optional[bool] = Field(response='String', alias='startCursor', default=True)
    end_cursor: typing.Optional[bool] = Field(response='String', alias='endCursor', default=True)


class Schedule(Payload):
    name: typing.Optional[bool] = Field(response='String', default=True)
    enabled: typing.Optional[bool] = Field(response='bool', default=True)
    parallel_runs: typing.Optional[bool] = Field(response='bool', alias='parallelRuns', default=True)
    workflow_name: typing.Optional[bool] = Field(response='String', alias='workflowName', default=True)
    workflow_version: typing.Optional[bool] = Field(response='String', alias='workflowVersion', default=True)
    cron_string: typing.Optional[bool] = Field(response='String', alias='cronString', default=True)
    workflow_context: typing.Optional[bool] = Field(response='String', alias='workflowContext', default=True)
    from_date: typing.Optional[bool] = Field(response='DateTime', alias='fromDate', default=True)
    to_date: typing.Optional[bool] = Field(response='DateTime', alias='toDate', default=True)
    status: typing.Optional[bool] = Field(response='Status', default=True)


class ScheduleEdge(Payload):
    node: typing.Optional[Schedule] = Field(response='Schedule')
    cursor: typing.Optional[bool] = Field(response='String', default=True)


class ScheduleConnection(Payload):
    edges: typing.Optional[ScheduleEdge] = Field(response='ScheduleEdge')
    page_info: typing.Optional[PageInfoSchedule] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[bool] = Field(response='Int', alias='totalCount', default=True)


class SchedulesQuery(Query):
    _name: str = Field('schedules', const=True)
    after: typing.Optional[str]
    before: typing.Optional[str]
    first: typing.Optional[int]
    last: typing.Optional[int]
    filter: typing.Optional[SchedulesFilterInput]
    payload: ScheduleConnection

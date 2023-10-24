import typing

from pydantic import Field
from pydantic import PrivateAttr

from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query


class TagAnd(Input):
    matches_all: typing.Optional[list[str]] = Field(default=None, alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(default=None, alias='matchesAny')


class OutputCursor(Payload):
    id: typing.Optional[bool] = Field(alias='ID', default=False)


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[bool] = Field(alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[bool] = Field(alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='startCursor')


class AllocationStrategy(Payload):
    description: typing.Optional[bool] = Field(alias='Description', default=False)
    lang: typing.Optional[bool] = Field(alias='Lang', default=False)
    name: typing.Optional[bool] = Field(alias='Name', default=False)
    script: typing.Optional[bool] = Field(alias='Script', default=False)
    id: typing.Optional[bool] = Field(default=False)


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(default=None,
                                                                     alias='AllocationStrategy')
    name: typing.Optional[bool] = Field(alias='Name', default=False)
    pool_properties: typing.Optional[bool] = Field(alias='PoolProperties', default=False)
    pool_type: typing.Optional[bool] = Field(alias='PoolType', default=False)
    id: typing.Optional[bool] = Field(default=False)


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(default=None)
    node: typing.Optional[ResourcePool] = Field(default=None)


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[bool] = Field(default=False, alias='totalCount',)


class SearchPoolsByTagsQuery(Query):
    _name: str = PrivateAttr('SearchPoolsByTags')
    tags: typing.Optional[TagOr] = Field(default=None)
    first: typing.Optional[int] = Field(default=None)
    last: typing.Optional[int] = Field(default=None)
    before: typing.Optional[typing.Any] = Field(default=None)
    after: typing.Optional[typing.Any] = Field(default=None)
    payload: ResourcePoolConnection


class SchedulesFilterInput(Input):
    workflow_name: str = Field(alias='workflowName')
    workflow_version: str = Field(alias='workflowVersion')


class PageInfoSchedule(Payload):
    has_next_page: typing.Optional[bool] = Field(alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[bool] = Field(alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[bool] = Field(alias='startCursor', default=False)
    end_cursor: typing.Optional[bool] = Field(alias='endCursor', default=False)


class Schedule(Payload):
    name: typing.Optional[bool] = Field(default=False)
    enabled: typing.Optional[bool] = Field(default=False)
    parallel_runs: typing.Optional[bool] = Field(alias='parallelRuns', default=False)
    workflow_name: typing.Optional[bool] = Field(alias='workflowName', default=False)
    workflow_version: typing.Optional[bool] = Field(alias='workflowVersion', default=False)
    cron_string: typing.Optional[bool] = Field(alias='cronString', default=False)
    workflow_context: typing.Optional[bool] = Field(alias='workflowContext', default=False)
    from_date: typing.Optional[bool] = Field(alias='fromDate', default=False)
    to_date: typing.Optional[bool] = Field(alias='toDate', default=False)
    status: typing.Optional[bool] = Field(default=False)


class ScheduleEdge(Payload):
    node: typing.Optional[Schedule] = Field(default=None)
    cursor: typing.Optional[bool] = Field(default=False)


class ScheduleConnection(Payload):
    edges: typing.Optional[ScheduleEdge] = Field(default=None)
    page_info: typing.Optional[PageInfoSchedule] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[bool] = Field(alias='totalCount', default=False)


class SchedulesQuery(Query):
    _name: str = PrivateAttr('schedules')
    after: typing.Optional[str] = Field(default=None)
    before: typing.Optional[str] = Field(default=None)
    first: typing.Optional[int] = Field(default=None)
    last: typing.Optional[int] = Field(default=None)
    filter: typing.Optional[SchedulesFilterInput] = Field(default=None)
    payload: ScheduleConnection

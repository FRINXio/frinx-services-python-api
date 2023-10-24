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
    id: typing.Optional[bool] = Field(alias='ID', default=True)


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[bool] = Field(alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[bool] = Field(alias='hasPreviousPage', default=True)
    start_cursor: typing.Optional[OutputCursor] = Field(default=None, alias='startCursor')


class AllocationStrategy(Payload):
    description: typing.Optional[bool] = Field(alias='Description', default=True)
    lang: typing.Optional[bool] = Field(alias='Lang', default=True)
    name: typing.Optional[bool] = Field(alias='Name', default=True)
    script: typing.Optional[bool] = Field(alias='Script', default=True)
    id: typing.Optional[bool] = Field(default=True)


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(default=None,
                                                                     alias='AllocationStrategy')
    name: typing.Optional[bool] = Field(alias='Name', default=True)
    pool_properties: typing.Optional[bool] = Field(alias='PoolProperties', default=True)
    pool_type: typing.Optional[bool] = Field(alias='PoolType', default=True)
    id: typing.Optional[bool] = Field(default=True)


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(default=None)
    node: typing.Optional[ResourcePool] = Field(default=None)


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[bool] = Field(default=True, alias='totalCount',)


class SearchPoolsByTagsQuery(Query):
    _name: str = PrivateAttr('SearchPoolsByTags')
    tags: typing.Optional[TagOr] = Field(default=None)
    first: typing.Optional[int] = Field(default=None)
    last: typing.Optional[int] = Field(default=None)
    before: typing.Optional[typing.Any] = Field(default=None)
    after: typing.Optional[typing.Any] = Field(default=None)
    payload: ResourcePoolConnection = Field(default=None)


class SchedulesFilterInput(Input):
    workflow_name: str = Field(default=None, alias='workflowName')
    workflow_version: str = Field(default=None, alias='workflowVersion')


class PageInfoSchedule(Payload):
    has_next_page: typing.Optional[bool] = Field(alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[bool] = Field(alias='hasPreviousPage', default=True)
    start_cursor: typing.Optional[bool] = Field(alias='startCursor', default=True)
    end_cursor: typing.Optional[bool] = Field(alias='endCursor', default=True)


class Schedule(Payload):
    name: typing.Optional[bool] = Field(default=True)
    enabled: typing.Optional[bool] = Field(default=True)
    parallel_runs: typing.Optional[bool] = Field(alias='parallelRuns', default=True)
    workflow_name: typing.Optional[bool] = Field(alias='workflowName', default=True)
    workflow_version: typing.Optional[bool] = Field(alias='workflowVersion', default=True)
    cron_string: typing.Optional[bool] = Field(alias='cronString', default=True)
    workflow_context: typing.Optional[bool] = Field(alias='workflowContext', default=True)
    from_date: typing.Optional[bool] = Field(alias='fromDate', default=True)
    to_date: typing.Optional[bool] = Field(alias='toDate', default=True)
    status: typing.Optional[bool] = Field(default=True)


class ScheduleEdge(Payload):
    node: typing.Optional[Schedule] = Field(default=None)
    cursor: typing.Optional[bool] = Field(default=True)


class ScheduleConnection(Payload):
    edges: typing.Optional[ScheduleEdge] = Field(default=None)
    page_info: typing.Optional[PageInfoSchedule] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[bool] = Field(alias='totalCount', default=True)


class SchedulesQuery(Query):
    _name: str = PrivateAttr('schedules')
    after: typing.Optional[str] = Field(default=None)
    before: typing.Optional[str] = Field(default=None)
    first: typing.Optional[int] = Field(default=None)
    last: typing.Optional[int] = Field(default=None)
    filter: typing.Optional[SchedulesFilterInput] = Field(default=None)
    payload: ScheduleConnection = Field(default=None)

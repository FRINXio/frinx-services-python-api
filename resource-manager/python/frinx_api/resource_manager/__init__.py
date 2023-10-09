from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from pydantic import BaseModel
from pydantic import Field

Boolean: typing.TypeAlias = bool
Cursor: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Map: typing.TypeAlias = typing.Any
String: typing.TypeAlias = str


class AllocationStrategyLang(ENUM):
    js = 'js'
    py = 'py'


class PoolType(ENUM):
    allocating = 'allocating'
    set = 'set'
    singleton = 'singleton'


class Node(Interface):
    id: typing.Optional[Boolean]


class CreateAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String]
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_properties: Map = Field(alias='poolProperties')
    pool_property_types: Map = Field(alias='poolPropertyTypes')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateAllocationStrategyInput(Input):
    name: String
    description: typing.Optional[String]
    script: String
    lang: AllocationStrategyLang
    expected_pool_property_types: typing.Optional[Map] = Field(alias='expectedPoolPropertyTypes')


class CreateNestedAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateNestedSetPoolInput(Input):
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateNestedSingletonPoolInput(Input):
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateResourceTypeInput(Input):
    resource_name: String = Field(alias='resourceName')
    resource_properties: Map = Field(alias='resourceProperties')


class CreateSetPoolInput(Input):
    description: typing.Optional[String]
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateSingletonPoolInput(Input):
    description: typing.Optional[String]
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateTagInput(Input):
    tag_text: String = Field(alias='tagText')


class DeleteAllocationStrategyInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')


class DeleteResourcePoolInput(Input):
    resource_pool_id: ID = Field(alias='resourcePoolId')


class DeleteResourceTypeInput(Input):
    resource_type_id: ID = Field(alias='resourceTypeId')


class DeleteTagInput(Input):
    tag_id: ID = Field(alias='tagId')


class ResourceInput(Input):
    properties: Map = Field(alias='Properties')
    status: String = Field(alias='Status')
    updated_at: String = Field(alias='UpdatedAt')


class ResourcePoolInput(Input):
    resource_pool_id: ID = Field(alias='ResourcePoolID')
    resource_pool_name: String = Field(alias='ResourcePoolName')
    pool_properties: Map = Field(alias='poolProperties')


class TagAnd(Input):
    matches_all: typing.Optional[list[String]] = Field(alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(alias='matchesAny')


class TagPoolInput(Input):
    tag_id: ID = Field(alias='tagId')
    pool_id: ID = Field(alias='poolId')


class UntagPoolInput(Input):
    tag_id: ID = Field(alias='tagId')
    pool_id: ID = Field(alias='poolId')


class UpdateResourceTypeNameInput(Input):
    resource_type_id: ID = Field(alias='resourceTypeId')
    resource_name: String = Field(alias='resourceName')


class UpdateTagInput(Input):
    tag_id: ID = Field(alias='tagId')
    tag_text: String = Field(alias='tagText')


class AllocationStrategy(Payload):
    description: typing.Optional[Boolean] = Field(response='String', alias='Description', default=False)
    lang: typing.Optional[Boolean] = Field(response='AllocationStrategyLang', alias='Lang', default=False)
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=False)
    script: typing.Optional[Boolean] = Field(response='String', alias='Script', default=False)
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class AllocationStrategyPayload(BaseModel):
    description: typing.Optional[typing.Optional[String]] = Field(alias='Description')
    lang: typing.Optional[typing.Optional[AllocationStrategyLang]] = Field(alias='Lang')
    name: typing.Optional[typing.Optional[String]] = Field(alias='Name')
    script: typing.Optional[typing.Optional[String]] = Field(alias='Script')
    id: typing.Optional[typing.Optional[ID]]


class CreateAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateAllocatingPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy')


class CreateAllocationStrategyPayloadPayload(BaseModel):
    strategy: typing.Optional[AllocationStrategyPayload]


class CreateNestedAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateNestedAllocatingPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateNestedSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateNestedSetPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateNestedSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateNestedSingletonPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateResourceTypePayload(Payload):
    resource_type: typing.Optional[ResourceType] = Field(response='ResourceType', alias='resourceType')


class CreateResourceTypePayloadPayload(BaseModel):
    resource_type: typing.Optional[ResourceTypePayload] = Field(alias='resourceType')


class CreateSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateSetPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateSingletonPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload]


class CreateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class CreateTagPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload]


class DeleteAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy')


class DeleteAllocationStrategyPayloadPayload(BaseModel):
    strategy: typing.Optional[AllocationStrategyPayload]


class DeleteResourcePoolPayload(Payload):
    resource_pool_id: typing.Optional[Boolean] = Field(response='ID', alias='resourcePoolId', default=False)


class DeleteResourcePoolPayloadPayload(BaseModel):
    resource_pool_id: typing.Optional[typing.Optional[ID]] = Field(alias='resourcePoolId')


class DeleteResourceTypePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(response='ID', alias='resourceTypeId', default=False)


class DeleteResourceTypePayloadPayload(BaseModel):
    resource_type_id: typing.Optional[typing.Optional[ID]] = Field(alias='resourceTypeId')


class DeleteTagPayload(Payload):
    tag_id: typing.Optional[Boolean] = Field(response='ID', alias='tagId', default=False)


class DeleteTagPayloadPayload(BaseModel):
    tag_id: typing.Optional[typing.Optional[ID]] = Field(alias='tagId')


class CreateTagMutation(Mutation):
    _name: str = Field('CreateTag', const=True)
    input: CreateTagInput
    payload: CreateTagPayload


class UpdateTagMutation(Mutation):
    _name: str = Field('UpdateTag', const=True)
    input: UpdateTagInput
    payload: UpdateTagPayload


class DeleteTagMutation(Mutation):
    _name: str = Field('DeleteTag', const=True)
    input: DeleteTagInput
    payload: DeleteTagPayload


class TagPoolMutation(Mutation):
    _name: str = Field('TagPool', const=True)
    input: TagPoolInput
    payload: TagPoolPayload


class UntagPoolMutation(Mutation):
    _name: str = Field('UntagPool', const=True)
    input: UntagPoolInput
    payload: UntagPoolPayload


class CreateAllocationStrategyMutation(Mutation):
    _name: str = Field('CreateAllocationStrategy', const=True)
    input: typing.Optional[CreateAllocationStrategyInput]
    payload: CreateAllocationStrategyPayload


class DeleteAllocationStrategyMutation(Mutation):
    _name: str = Field('DeleteAllocationStrategy', const=True)
    input: typing.Optional[DeleteAllocationStrategyInput]
    payload: DeleteAllocationStrategyPayload


class TestAllocationStrategyMutation(Mutation):
    _name: str = Field('TestAllocationStrategy', const=True)
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    resource_pool: ResourcePoolInput = Field(alias='resourcePool')
    current_resources: typing.Optional[list[ResourceInput]] = Field(alias='currentResources')
    user_input: Map = Field(alias='userInput')
    payload: Boolean


class ClaimResourceMutation(Mutation):
    _name: str = Field('ClaimResource', const=True)
    pool_id: ID = Field(alias='poolId')
    description: typing.Optional[String]
    user_input: Map = Field(alias='userInput')
    payload: Resource


class ClaimResourceWithAltIdMutation(Mutation):
    _name: str = Field('ClaimResourceWithAltId', const=True)
    pool_id: ID = Field(alias='poolId')
    description: typing.Optional[String]
    user_input: Map = Field(alias='userInput')
    alternative_id: Map = Field(alias='alternativeId')
    payload: Resource


class FreeResourceMutation(Mutation):
    _name: str = Field('FreeResource', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    payload: Boolean


class CreateSetPoolMutation(Mutation):
    _name: str = Field('CreateSetPool', const=True)
    input: CreateSetPoolInput
    payload: CreateSetPoolPayload


class CreateNestedSetPoolMutation(Mutation):
    _name: str = Field('CreateNestedSetPool', const=True)
    input: CreateNestedSetPoolInput
    payload: CreateNestedSetPoolPayload


class CreateSingletonPoolMutation(Mutation):
    _name: str = Field('CreateSingletonPool', const=True)
    input: typing.Optional[CreateSingletonPoolInput]
    payload: CreateSingletonPoolPayload


class CreateNestedSingletonPoolMutation(Mutation):
    _name: str = Field('CreateNestedSingletonPool', const=True)
    input: CreateNestedSingletonPoolInput
    payload: CreateNestedSingletonPoolPayload


class CreateAllocatingPoolMutation(Mutation):
    _name: str = Field('CreateAllocatingPool', const=True)
    input: typing.Optional[CreateAllocatingPoolInput]
    payload: CreateAllocatingPoolPayload


class CreateNestedAllocatingPoolMutation(Mutation):
    _name: str = Field('CreateNestedAllocatingPool', const=True)
    input: CreateNestedAllocatingPoolInput
    payload: CreateNestedAllocatingPoolPayload


class DeleteResourcePoolMutation(Mutation):
    _name: str = Field('DeleteResourcePool', const=True)
    input: DeleteResourcePoolInput
    payload: DeleteResourcePoolPayload


class CreateResourceTypeMutation(Mutation):
    _name: str = Field('CreateResourceType', const=True)
    input: CreateResourceTypeInput
    payload: CreateResourceTypePayload


class DeleteResourceTypeMutation(Mutation):
    _name: str = Field('DeleteResourceType', const=True)
    input: DeleteResourceTypeInput
    payload: DeleteResourceTypePayload


class UpdateResourceTypeNameMutation(Mutation):
    _name: str = Field('UpdateResourceTypeName', const=True)
    input: UpdateResourceTypeNameInput
    payload: UpdateResourceTypeNamePayload


class UpdateResourceAltIdMutation(Mutation):
    _name: str = Field('UpdateResourceAltId', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    alternative_id: Map = Field(alias='alternativeId')
    payload: Resource


class CreateTagMutationResponse(BaseModel):
    data: typing.Optional[CreateTagData]
    errors: typing.Optional[typing.Any]


class CreateTagData(BaseModel):
    create_tag: CreateTagPayloadPayload = Field(alias='CreateTag')


class UpdateTagMutationResponse(BaseModel):
    data: typing.Optional[UpdateTagData]
    errors: typing.Optional[typing.Any]


class UpdateTagData(BaseModel):
    update_tag: UpdateTagPayloadPayload = Field(alias='UpdateTag')


class DeleteTagMutationResponse(BaseModel):
    data: typing.Optional[DeleteTagData]
    errors: typing.Optional[typing.Any]


class DeleteTagData(BaseModel):
    delete_tag: DeleteTagPayloadPayload = Field(alias='DeleteTag')


class TagPoolMutationResponse(BaseModel):
    data: typing.Optional[TagPoolData]
    errors: typing.Optional[typing.Any]


class TagPoolData(BaseModel):
    tag_pool: TagPoolPayloadPayload = Field(alias='TagPool')


class UntagPoolMutationResponse(BaseModel):
    data: typing.Optional[UntagPoolData]
    errors: typing.Optional[typing.Any]


class UntagPoolData(BaseModel):
    untag_pool: UntagPoolPayloadPayload = Field(alias='UntagPool')


class CreateAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[CreateAllocationStrategyData]
    errors: typing.Optional[typing.Any]


class CreateAllocationStrategyData(BaseModel):
    create_allocation_strategy: CreateAllocationStrategyPayloadPayload = Field(alias='CreateAllocationStrategy')


class DeleteAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[DeleteAllocationStrategyData]
    errors: typing.Optional[typing.Any]


class DeleteAllocationStrategyData(BaseModel):
    delete_allocation_strategy: DeleteAllocationStrategyPayloadPayload = Field(alias='DeleteAllocationStrategy')


class TestAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[TestAllocationStrategyData]
    errors: typing.Optional[typing.Any]


class TestAllocationStrategyData(BaseModel):
    test_allocation_strategy: typing.Optional[Map] = Field(alias='TestAllocationStrategy')


class ClaimResourceMutationResponse(BaseModel):
    data: typing.Optional[ClaimResourceData]
    errors: typing.Optional[typing.Any]


class ClaimResourceData(BaseModel):
    claim_resource: ResourcePayload = Field(alias='ClaimResource')


class ClaimResourceWithAltIdMutationResponse(BaseModel):
    data: typing.Optional[ClaimResourceWithAltIdData]
    errors: typing.Optional[typing.Any]


class ClaimResourceWithAltIdData(BaseModel):
    claim_resource_with_alt_id: ResourcePayload = Field(alias='ClaimResourceWithAltId')


class FreeResourceMutationResponse(BaseModel):
    data: typing.Optional[FreeResourceData]
    errors: typing.Optional[typing.Any]


class FreeResourceData(BaseModel):
    free_resource: typing.Optional[String] = Field(alias='FreeResource')


class CreateSetPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateSetPoolData]
    errors: typing.Optional[typing.Any]


class CreateSetPoolData(BaseModel):
    create_set_pool: CreateSetPoolPayloadPayload = Field(alias='CreateSetPool')


class CreateNestedSetPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedSetPoolData]
    errors: typing.Optional[typing.Any]


class CreateNestedSetPoolData(BaseModel):
    create_nested_set_pool: CreateNestedSetPoolPayloadPayload = Field(alias='CreateNestedSetPool')


class CreateSingletonPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateSingletonPoolData]
    errors: typing.Optional[typing.Any]


class CreateSingletonPoolData(BaseModel):
    create_singleton_pool: CreateSingletonPoolPayloadPayload = Field(alias='CreateSingletonPool')


class CreateNestedSingletonPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedSingletonPoolData]
    errors: typing.Optional[typing.Any]


class CreateNestedSingletonPoolData(BaseModel):
    create_nested_singleton_pool: CreateNestedSingletonPoolPayloadPayload = Field(alias='CreateNestedSingletonPool')


class CreateAllocatingPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateAllocatingPoolData]
    errors: typing.Optional[typing.Any]


class CreateAllocatingPoolData(BaseModel):
    create_allocating_pool: CreateAllocatingPoolPayloadPayload = Field(alias='CreateAllocatingPool')


class CreateNestedAllocatingPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedAllocatingPoolData]
    errors: typing.Optional[typing.Any]


class CreateNestedAllocatingPoolData(BaseModel):
    create_nested_allocating_pool: CreateNestedAllocatingPoolPayloadPayload = Field(alias='CreateNestedAllocatingPool')


class DeleteResourcePoolMutationResponse(BaseModel):
    data: typing.Optional[DeleteResourcePoolData]
    errors: typing.Optional[typing.Any]


class DeleteResourcePoolData(BaseModel):
    delete_resource_pool: DeleteResourcePoolPayloadPayload = Field(alias='DeleteResourcePool')


class CreateResourceTypeMutationResponse(BaseModel):
    data: typing.Optional[CreateResourceTypeData]
    errors: typing.Optional[typing.Any]


class CreateResourceTypeData(BaseModel):
    create_resource_type: CreateResourceTypePayloadPayload = Field(alias='CreateResourceType')


class DeleteResourceTypeMutationResponse(BaseModel):
    data: typing.Optional[DeleteResourceTypeData]
    errors: typing.Optional[typing.Any]


class DeleteResourceTypeData(BaseModel):
    delete_resource_type: DeleteResourceTypePayloadPayload = Field(alias='DeleteResourceType')


class UpdateResourceTypeNameMutationResponse(BaseModel):
    data: typing.Optional[UpdateResourceTypeNameData]
    errors: typing.Optional[typing.Any]


class UpdateResourceTypeNameData(BaseModel):
    update_resource_type_name: UpdateResourceTypeNamePayloadPayload = Field(alias='UpdateResourceTypeName')


class UpdateResourceAltIdMutationResponse(BaseModel):
    data: typing.Optional[UpdateResourceAltIdData]
    errors: typing.Optional[typing.Any]


class UpdateResourceAltIdData(BaseModel):
    update_resource_alt_id: ResourcePayload = Field(alias='UpdateResourceAltId')


class OutputCursor(Payload):
    id: typing.Optional[Boolean] = Field(response='String', alias='ID', default=False)


class OutputCursorPayload(BaseModel):
    id: typing.Optional[typing.Optional[String]] = Field(alias='ID')


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='startCursor')


class PageInfoPayload(BaseModel):
    end_cursor: typing.Optional[OutputCursorPayload] = Field(alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(alias='hasPreviousPage')
    start_cursor: typing.Optional[OutputCursorPayload] = Field(alias='startCursor')


class PoolCapacityPayload(Payload):
    free_capacity: typing.Optional[Boolean] = Field(response='String', alias='freeCapacity', default=False)
    utilized_capacity: typing.Optional[Boolean] = Field(response='String', alias='utilizedCapacity', default=False)


class PoolCapacityPayloadPayload(BaseModel):
    free_capacity: typing.Optional[typing.Optional[String]] = Field(alias='freeCapacity')
    utilized_capacity: typing.Optional[typing.Optional[String]] = Field(alias='utilizedCapacity')


class PropertyType(Payload):
    float_val: typing.Optional[Boolean] = Field(response='Float', alias='FloatVal', default=False)
    int_val: typing.Optional[Boolean] = Field(response='Int', alias='IntVal', default=False)
    mandatory: typing.Optional[Boolean] = Field(response='Boolean', alias='Mandatory', default=False)
    string_val: typing.Optional[Boolean] = Field(response='String', alias='StringVal', default=False)
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=False)
    type: typing.Optional[Boolean] = Field(response='String', alias='Type', default=False)
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class PropertyTypePayload(BaseModel):
    float_val: typing.Optional[typing.Optional[Float]] = Field(alias='FloatVal')
    int_val: typing.Optional[typing.Optional[Int]] = Field(alias='IntVal')
    mandatory: typing.Optional[typing.Optional[Boolean]] = Field(alias='Mandatory')
    string_val: typing.Optional[typing.Optional[String]] = Field(alias='StringVal')
    name: typing.Optional[typing.Optional[String]] = Field(alias='Name')
    type: typing.Optional[typing.Optional[String]] = Field(alias='Type')
    id: typing.Optional[typing.Optional[ID]]


class QueryPoolCapacityQuery(Query):
    _name: str = Field('QueryPoolCapacity', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: PoolCapacityPayload


class QueryPoolTypesQuery(Query):
    _name: str = Field('QueryPoolTypes', const=True)


class QueryResourceQuery(Query):
    _name: str = Field('QueryResource', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    payload: Resource


class QueryResourcesQuery(Query):
    _name: str = Field('QueryResources', const=True)
    pool_id: ID = Field(alias='poolId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryResourcesByAltIdQuery(Query):
    _name: str = Field('QueryResourcesByAltId', const=True)
    input: Map
    pool_id: typing.Optional[ID] = Field(alias='poolId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryAllocationStrategyQuery(Query):
    _name: str = Field('QueryAllocationStrategy', const=True)
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    payload: AllocationStrategy


class QueryAllocationStrategiesQuery(Query):
    _name: str = Field('QueryAllocationStrategies', const=True)
    by_name: typing.Optional[String] = Field(alias='byName')
    payload: AllocationStrategy


class QueryResourceTypesQuery(Query):
    _name: str = Field('QueryResourceTypes', const=True)
    by_name: typing.Optional[String] = Field(alias='byName')
    payload: ResourceType


class QueryRequiredPoolPropertiesQuery(Query):
    _name: str = Field('QueryRequiredPoolProperties', const=True)
    allocation_strategy_name: String = Field(alias='allocationStrategyName')
    payload: PropertyType


class QueryResourcePoolQuery(Query):
    _name: str = Field('QueryResourcePool', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: ResourcePool


class QueryEmptyResourcePoolsQuery(Query):
    _name: str = Field('QueryEmptyResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    payload: ResourcePoolConnection


class QueryResourcePoolsQuery(Query):
    _name: str = Field('QueryResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class QueryRecentlyActiveResourcesQuery(Query):
    _name: str = Field('QueryRecentlyActiveResources', const=True)
    from_datetime: String = Field(alias='fromDatetime')
    to_datetime: typing.Optional[String] = Field(alias='toDatetime')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryResourcePoolHierarchyPathQuery(Query):
    _name: str = Field('QueryResourcePoolHierarchyPath', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: ResourcePool


class QueryRootResourcePoolsQuery(Query):
    _name: str = Field('QueryRootResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class QueryLeafResourcePoolsQuery(Query):
    _name: str = Field('QueryLeafResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class SearchPoolsByTagsQuery(Query):
    _name: str = Field('SearchPoolsByTags', const=True)
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    payload: ResourcePoolConnection


class QueryTagsQuery(Query):
    _name: str = Field('QueryTags', const=True)


class NodeQuery(Query):
    _name: str = Field('node', const=True)
    id: ID
    payload: Node


class QueryPoolCapacityQueryResponse(BaseModel):
    data: typing.Optional[QueryPoolCapacityData]
    errors: typing.Optional[typing.Any]


class QueryPoolCapacityData(BaseModel):
    query_pool_capacity: PoolCapacityPayloadPayload = Field(alias='QueryPoolCapacity')


class QueryResourceQueryResponse(BaseModel):
    data: typing.Optional[QueryResourceData]
    errors: typing.Optional[typing.Any]


class QueryResourceData(BaseModel):
    query_resource: ResourcePayload = Field(alias='QueryResource')


class QueryResourcesQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcesData]
    errors: typing.Optional[typing.Any]


class QueryResourcesData(BaseModel):
    query_resources: ResourceConnectionPayload = Field(alias='QueryResources')


class QueryResourcesByAltIdQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcesByAltIdData]
    errors: typing.Optional[typing.Any]


class QueryResourcesByAltIdData(BaseModel):
    query_resources_by_alt_id: ResourceConnectionPayload = Field(alias='QueryResourcesByAltId')


class QueryAllocationStrategyQueryResponse(BaseModel):
    data: typing.Optional[QueryAllocationStrategyData]
    errors: typing.Optional[typing.Any]


class QueryAllocationStrategyData(BaseModel):
    query_allocation_strategy: AllocationStrategyPayload = Field(alias='QueryAllocationStrategy')


class QueryAllocationStrategiesQueryResponse(BaseModel):
    data: typing.Optional[QueryAllocationStrategiesData]
    errors: typing.Optional[typing.Any]


class QueryAllocationStrategiesData(BaseModel):
    query_allocation_strategies: typing.Optional[list[AllocationStrategyPayload]] = Field(alias='QueryAllocationStrategies')


class QueryResourceTypesQueryResponse(BaseModel):
    data: typing.Optional[QueryResourceTypesData]
    errors: typing.Optional[typing.Any]


class QueryResourceTypesData(BaseModel):
    query_resource_types: typing.Optional[list[ResourceTypePayload]] = Field(alias='QueryResourceTypes')


class QueryRequiredPoolPropertiesQueryResponse(BaseModel):
    data: typing.Optional[QueryRequiredPoolPropertiesData]
    errors: typing.Optional[typing.Any]


class QueryRequiredPoolPropertiesData(BaseModel):
    query_required_pool_properties: typing.Optional[list[PropertyTypePayload]] = Field(alias='QueryRequiredPoolProperties')


class QueryResourcePoolQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolData]
    errors: typing.Optional[typing.Any]


class QueryResourcePoolData(BaseModel):
    query_resource_pool: ResourcePoolPayload = Field(alias='QueryResourcePool')


class QueryEmptyResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryEmptyResourcePoolsData]
    errors: typing.Optional[typing.Any]


class QueryEmptyResourcePoolsData(BaseModel):
    query_empty_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryEmptyResourcePools')


class QueryResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolsData]
    errors: typing.Optional[typing.Any]


class QueryResourcePoolsData(BaseModel):
    query_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryResourcePools')


class QueryRecentlyActiveResourcesQueryResponse(BaseModel):
    data: typing.Optional[QueryRecentlyActiveResourcesData]
    errors: typing.Optional[typing.Any]


class QueryRecentlyActiveResourcesData(BaseModel):
    query_recently_active_resources: ResourceConnectionPayload = Field(alias='QueryRecentlyActiveResources')


class QueryResourcePoolHierarchyPathQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolHierarchyPathData]
    errors: typing.Optional[typing.Any]


class QueryResourcePoolHierarchyPathData(BaseModel):
    query_resource_pool_hierarchy_path: typing.Optional[list[ResourcePoolPayload]] = Field(alias='QueryResourcePoolHierarchyPath')


class QueryRootResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryRootResourcePoolsData]
    errors: typing.Optional[typing.Any]


class QueryRootResourcePoolsData(BaseModel):
    query_root_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryRootResourcePools')


class QueryLeafResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryLeafResourcePoolsData]
    errors: typing.Optional[typing.Any]


class QueryLeafResourcePoolsData(BaseModel):
    query_leaf_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryLeafResourcePools')


class SearchPoolsByTagsQueryResponse(BaseModel):
    data: typing.Optional[SearchPoolsByTagsData]
    errors: typing.Optional[typing.Any]


class SearchPoolsByTagsData(BaseModel):
    search_pools_by_tags: ResourcePoolConnectionPayload = Field(alias='SearchPoolsByTags')


class NodeQueryResponse(BaseModel):
    data: typing.Optional[Node]
    errors: typing.Optional[typing.Any]


class Resource(Payload):
    description: typing.Optional[Boolean] = Field(response='String', alias='Description', default=False)
    nested_pool: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='NestedPool')
    parent_pool: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='ParentPool')
    properties: typing.Optional[Boolean] = Field(response='Map', alias='Properties', default=False)
    alternative_id: typing.Optional[Boolean] = Field(response='Map', alias='AlternativeId', default=False)
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class ResourcePayload(BaseModel):
    description: typing.Optional[typing.Optional[String]] = Field(alias='Description')
    nested_pool: typing.Optional[ResourcePoolPayload] = Field(alias='NestedPool')
    parent_pool: typing.Optional[ResourcePoolPayload] = Field(alias='ParentPool')
    properties: typing.Optional[typing.Optional[Map]] = Field(alias='Properties')
    alternative_id: typing.Optional[typing.Optional[Map]] = Field(alias='AlternativeId')
    id: typing.Optional[typing.Optional[ID]]


class ResourceConnection(Payload):
    edges: typing.Optional[ResourceEdge] = Field(response='ResourceEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=False)


class ResourceConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ResourceEdgePayload]]]
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(alias='totalCount')


class ResourceEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor')
    node: typing.Optional[Resource] = Field(response='Resource')


class ResourceEdgePayload(BaseModel):
    cursor: typing.Optional[OutputCursorPayload]
    node: typing.Optional[ResourcePayload]


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy', alias='AllocationStrategy')
    capacity: typing.Optional[PoolCapacityPayload] = Field(response='PoolCapacityPayload', alias='Capacity')
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=False)
    parent_resource: typing.Optional[Resource] = Field(response='Resource', alias='ParentResource')
    pool_properties: typing.Optional[Boolean] = Field(response='Map', alias='PoolProperties', default=False)
    pool_type: typing.Optional[Boolean] = Field(response='PoolType', alias='PoolType', default=False)
    resource_type: typing.Optional[ResourceType] = Field(response='ResourceType', alias='ResourceType')
    resources: typing.Optional[Resource] = Field(response='Resource', alias='Resources')
    tags: typing.Optional[Tag] = Field(response='Tag', alias='Tags')
    allocated_resources: typing.Optional[ResourceConnection] = Field(response='ResourceConnection', alias='allocatedResources')
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class ResourcePoolPayload(BaseModel):
    allocation_strategy: typing.Optional[AllocationStrategyPayload] = Field(alias='AllocationStrategy')
    capacity: typing.Optional[PoolCapacityPayloadPayload] = Field(alias='Capacity')
    name: typing.Optional[typing.Optional[String]] = Field(alias='Name')
    parent_resource: typing.Optional[ResourcePayload] = Field(alias='ParentResource')
    pool_properties: typing.Optional[typing.Optional[Map]] = Field(alias='PoolProperties')
    pool_type: typing.Optional[typing.Optional[PoolType]] = Field(alias='PoolType')
    resource_type: typing.Optional[ResourceTypePayload] = Field(alias='ResourceType')
    resources: typing.Optional[typing.Optional[list[ResourcePayload]]] = Field(alias='Resources')
    tags: typing.Optional[typing.Optional[list[TagPayload]]] = Field(alias='Tags')
    allocated_resources: typing.Optional[ResourceConnectionPayload] = Field(alias='allocatedResources')
    id: typing.Optional[typing.Optional[ID]]


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(response='ResourcePoolEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=False)


class ResourcePoolConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ResourcePoolEdgePayload]]]
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(alias='totalCount')


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor')
    node: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class ResourcePoolEdgePayload(BaseModel):
    cursor: typing.Optional[OutputCursorPayload]
    node: typing.Optional[ResourcePoolPayload]


class ResourceType(Payload):
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=False)
    pools: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='Pools')
    property_types: typing.Optional[PropertyType] = Field(response='PropertyType', alias='PropertyTypes')
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class ResourceTypePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]] = Field(alias='Name')
    pools: typing.Optional[typing.Optional[list[ResourcePoolPayload]]] = Field(alias='Pools')
    property_types: typing.Optional[typing.Optional[list[PropertyTypePayload]]] = Field(alias='PropertyTypes')
    id: typing.Optional[typing.Optional[ID]]


class Tag(Payload):
    pools: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='Pools')
    tag: typing.Optional[Boolean] = Field(response='String', alias='Tag', default=False)
    id: typing.Optional[Boolean] = Field(response='ID', default=False)


class TagPayload(BaseModel):
    pools: typing.Optional[typing.Optional[list[ResourcePoolPayload]]] = Field(alias='Pools')
    tag: typing.Optional[typing.Optional[String]] = Field(alias='Tag')
    id: typing.Optional[typing.Optional[ID]]


class TagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class TagPoolPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload]


class UntagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class UntagPoolPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload]


class UpdateResourceTypeNamePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(response='ID', alias='resourceTypeId', default=False)


class UpdateResourceTypeNamePayloadPayload(BaseModel):
    resource_type_id: typing.Optional[typing.Optional[ID]] = Field(alias='resourceTypeId')


class UpdateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class UpdateTagPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload]


Node.update_forward_refs()
CreateAllocatingPoolInput.update_forward_refs()
CreateAllocationStrategyInput.update_forward_refs()
CreateNestedAllocatingPoolInput.update_forward_refs()
CreateNestedSetPoolInput.update_forward_refs()
CreateNestedSingletonPoolInput.update_forward_refs()
CreateResourceTypeInput.update_forward_refs()
CreateSetPoolInput.update_forward_refs()
CreateSingletonPoolInput.update_forward_refs()
CreateTagInput.update_forward_refs()
DeleteAllocationStrategyInput.update_forward_refs()
DeleteResourcePoolInput.update_forward_refs()
DeleteResourceTypeInput.update_forward_refs()
DeleteTagInput.update_forward_refs()
ResourceInput.update_forward_refs()
ResourcePoolInput.update_forward_refs()
TagAnd.update_forward_refs()
TagOr.update_forward_refs()
TagPoolInput.update_forward_refs()
UntagPoolInput.update_forward_refs()
UpdateResourceTypeNameInput.update_forward_refs()
UpdateTagInput.update_forward_refs()
AllocationStrategy.update_forward_refs()
AllocationStrategyPayload.update_forward_refs()
CreateAllocatingPoolPayload.update_forward_refs()
CreateAllocatingPoolPayloadPayload.update_forward_refs()
CreateAllocationStrategyPayload.update_forward_refs()
CreateAllocationStrategyPayloadPayload.update_forward_refs()
CreateNestedAllocatingPoolPayload.update_forward_refs()
CreateNestedAllocatingPoolPayloadPayload.update_forward_refs()
CreateNestedSetPoolPayload.update_forward_refs()
CreateNestedSetPoolPayloadPayload.update_forward_refs()
CreateNestedSingletonPoolPayload.update_forward_refs()
CreateNestedSingletonPoolPayloadPayload.update_forward_refs()
CreateResourceTypePayload.update_forward_refs()
CreateResourceTypePayloadPayload.update_forward_refs()
CreateSetPoolPayload.update_forward_refs()
CreateSetPoolPayloadPayload.update_forward_refs()
CreateSingletonPoolPayload.update_forward_refs()
CreateSingletonPoolPayloadPayload.update_forward_refs()
CreateTagPayload.update_forward_refs()
CreateTagPayloadPayload.update_forward_refs()
DeleteAllocationStrategyPayload.update_forward_refs()
DeleteAllocationStrategyPayloadPayload.update_forward_refs()
DeleteResourcePoolPayload.update_forward_refs()
DeleteResourcePoolPayloadPayload.update_forward_refs()
DeleteResourceTypePayload.update_forward_refs()
DeleteResourceTypePayloadPayload.update_forward_refs()
DeleteTagPayload.update_forward_refs()
DeleteTagPayloadPayload.update_forward_refs()
CreateTagMutation.update_forward_refs()
UpdateTagMutation.update_forward_refs()
DeleteTagMutation.update_forward_refs()
TagPoolMutation.update_forward_refs()
UntagPoolMutation.update_forward_refs()
CreateAllocationStrategyMutation.update_forward_refs()
DeleteAllocationStrategyMutation.update_forward_refs()
TestAllocationStrategyMutation.update_forward_refs()
ClaimResourceMutation.update_forward_refs()
ClaimResourceWithAltIdMutation.update_forward_refs()
FreeResourceMutation.update_forward_refs()
CreateSetPoolMutation.update_forward_refs()
CreateNestedSetPoolMutation.update_forward_refs()
CreateSingletonPoolMutation.update_forward_refs()
CreateNestedSingletonPoolMutation.update_forward_refs()
CreateAllocatingPoolMutation.update_forward_refs()
CreateNestedAllocatingPoolMutation.update_forward_refs()
DeleteResourcePoolMutation.update_forward_refs()
CreateResourceTypeMutation.update_forward_refs()
DeleteResourceTypeMutation.update_forward_refs()
UpdateResourceTypeNameMutation.update_forward_refs()
UpdateResourceAltIdMutation.update_forward_refs()
CreateTagMutationResponse.update_forward_refs()
CreateTagData.update_forward_refs()
UpdateTagMutationResponse.update_forward_refs()
UpdateTagData.update_forward_refs()
DeleteTagMutationResponse.update_forward_refs()
DeleteTagData.update_forward_refs()
TagPoolMutationResponse.update_forward_refs()
TagPoolData.update_forward_refs()
UntagPoolMutationResponse.update_forward_refs()
UntagPoolData.update_forward_refs()
CreateAllocationStrategyMutationResponse.update_forward_refs()
CreateAllocationStrategyData.update_forward_refs()
DeleteAllocationStrategyMutationResponse.update_forward_refs()
DeleteAllocationStrategyData.update_forward_refs()
TestAllocationStrategyMutationResponse.update_forward_refs()
TestAllocationStrategyData.update_forward_refs()
ClaimResourceMutationResponse.update_forward_refs()
ClaimResourceData.update_forward_refs()
ClaimResourceWithAltIdMutationResponse.update_forward_refs()
ClaimResourceWithAltIdData.update_forward_refs()
FreeResourceMutationResponse.update_forward_refs()
FreeResourceData.update_forward_refs()
CreateSetPoolMutationResponse.update_forward_refs()
CreateSetPoolData.update_forward_refs()
CreateNestedSetPoolMutationResponse.update_forward_refs()
CreateNestedSetPoolData.update_forward_refs()
CreateSingletonPoolMutationResponse.update_forward_refs()
CreateSingletonPoolData.update_forward_refs()
CreateNestedSingletonPoolMutationResponse.update_forward_refs()
CreateNestedSingletonPoolData.update_forward_refs()
CreateAllocatingPoolMutationResponse.update_forward_refs()
CreateAllocatingPoolData.update_forward_refs()
CreateNestedAllocatingPoolMutationResponse.update_forward_refs()
CreateNestedAllocatingPoolData.update_forward_refs()
DeleteResourcePoolMutationResponse.update_forward_refs()
DeleteResourcePoolData.update_forward_refs()
CreateResourceTypeMutationResponse.update_forward_refs()
CreateResourceTypeData.update_forward_refs()
DeleteResourceTypeMutationResponse.update_forward_refs()
DeleteResourceTypeData.update_forward_refs()
UpdateResourceTypeNameMutationResponse.update_forward_refs()
UpdateResourceTypeNameData.update_forward_refs()
UpdateResourceAltIdMutationResponse.update_forward_refs()
UpdateResourceAltIdData.update_forward_refs()
OutputCursor.update_forward_refs()
OutputCursorPayload.update_forward_refs()
PageInfo.update_forward_refs()
PageInfoPayload.update_forward_refs()
PoolCapacityPayload.update_forward_refs()
PoolCapacityPayloadPayload.update_forward_refs()
PropertyType.update_forward_refs()
PropertyTypePayload.update_forward_refs()
QueryPoolCapacityQuery.update_forward_refs()
QueryPoolTypesQuery.update_forward_refs()
QueryResourceQuery.update_forward_refs()
QueryResourcesQuery.update_forward_refs()
QueryResourcesByAltIdQuery.update_forward_refs()
QueryAllocationStrategyQuery.update_forward_refs()
QueryAllocationStrategiesQuery.update_forward_refs()
QueryResourceTypesQuery.update_forward_refs()
QueryRequiredPoolPropertiesQuery.update_forward_refs()
QueryResourcePoolQuery.update_forward_refs()
QueryEmptyResourcePoolsQuery.update_forward_refs()
QueryResourcePoolsQuery.update_forward_refs()
QueryRecentlyActiveResourcesQuery.update_forward_refs()
QueryResourcePoolHierarchyPathQuery.update_forward_refs()
QueryRootResourcePoolsQuery.update_forward_refs()
QueryLeafResourcePoolsQuery.update_forward_refs()
SearchPoolsByTagsQuery.update_forward_refs()
QueryTagsQuery.update_forward_refs()
NodeQuery.update_forward_refs()
QueryPoolCapacityQueryResponse.update_forward_refs()
QueryPoolCapacityData.update_forward_refs()
QueryResourceQueryResponse.update_forward_refs()
QueryResourceData.update_forward_refs()
QueryResourcesQueryResponse.update_forward_refs()
QueryResourcesData.update_forward_refs()
QueryResourcesByAltIdQueryResponse.update_forward_refs()
QueryResourcesByAltIdData.update_forward_refs()
QueryAllocationStrategyQueryResponse.update_forward_refs()
QueryAllocationStrategyData.update_forward_refs()
QueryAllocationStrategiesQueryResponse.update_forward_refs()
QueryAllocationStrategiesData.update_forward_refs()
QueryResourceTypesQueryResponse.update_forward_refs()
QueryResourceTypesData.update_forward_refs()
QueryRequiredPoolPropertiesQueryResponse.update_forward_refs()
QueryRequiredPoolPropertiesData.update_forward_refs()
QueryResourcePoolQueryResponse.update_forward_refs()
QueryResourcePoolData.update_forward_refs()
QueryEmptyResourcePoolsQueryResponse.update_forward_refs()
QueryEmptyResourcePoolsData.update_forward_refs()
QueryResourcePoolsQueryResponse.update_forward_refs()
QueryResourcePoolsData.update_forward_refs()
QueryRecentlyActiveResourcesQueryResponse.update_forward_refs()
QueryRecentlyActiveResourcesData.update_forward_refs()
QueryResourcePoolHierarchyPathQueryResponse.update_forward_refs()
QueryResourcePoolHierarchyPathData.update_forward_refs()
QueryRootResourcePoolsQueryResponse.update_forward_refs()
QueryRootResourcePoolsData.update_forward_refs()
QueryLeafResourcePoolsQueryResponse.update_forward_refs()
QueryLeafResourcePoolsData.update_forward_refs()
SearchPoolsByTagsQueryResponse.update_forward_refs()
SearchPoolsByTagsData.update_forward_refs()
NodeQueryResponse.update_forward_refs()
Resource.update_forward_refs()
ResourcePayload.update_forward_refs()
ResourceConnection.update_forward_refs()
ResourceConnectionPayload.update_forward_refs()
ResourceEdge.update_forward_refs()
ResourceEdgePayload.update_forward_refs()
ResourcePool.update_forward_refs()
ResourcePoolPayload.update_forward_refs()
ResourcePoolConnection.update_forward_refs()
ResourcePoolConnectionPayload.update_forward_refs()
ResourcePoolEdge.update_forward_refs()
ResourcePoolEdgePayload.update_forward_refs()
ResourceType.update_forward_refs()
ResourceTypePayload.update_forward_refs()
Tag.update_forward_refs()
TagPayload.update_forward_refs()
TagPoolPayload.update_forward_refs()
TagPoolPayloadPayload.update_forward_refs()
UntagPoolPayload.update_forward_refs()
UntagPoolPayloadPayload.update_forward_refs()
UpdateResourceTypeNamePayload.update_forward_refs()
UpdateResourceTypeNamePayloadPayload.update_forward_refs()
UpdateTagPayload.update_forward_refs()
UpdateTagPayloadPayload.update_forward_refs()

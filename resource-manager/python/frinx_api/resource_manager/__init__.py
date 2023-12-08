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
from pydantic import PrivateAttr

Boolean: typing.TypeAlias = bool
Cursor: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Map: typing.TypeAlias = dict[str, typing.Any]
String: typing.TypeAlias = str


class AllocationStrategyLang(ENUM):
    JS = 'js'
    PY = 'py'


class OrderDirection(ENUM):
    ASC = 'ASC'
    DESC = 'DESC'


class PoolType(ENUM):
    ALLOCATING = 'allocating'
    SET = 'set'
    SINGLETON = 'singleton'


class ResourcePoolOrderField(ENUM):
    NAME = 'name'
    DEALOCATIONSAFETYPERIOD = 'dealocationSafetyPeriod'


class Node(Interface):
    id: typing.Optional[Boolean] = Field(default=None)


class CreateAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String] = Field(default=None)
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_properties: Map = Field(alias='poolProperties')
    pool_property_types: Map = Field(alias='poolPropertyTypes')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


class CreateAllocationStrategyInput(Input):
    name: String
    description: typing.Optional[String] = Field(default=None)
    script: String
    lang: AllocationStrategyLang
    expected_pool_property_types: typing.Optional[Map] = Field(default=None, alias='expectedPoolPropertyTypes')


class CreateNestedAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String] = Field(default=None)
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


class CreateNestedSetPoolInput(Input):
    description: typing.Optional[String] = Field(default=None)
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(default=None, alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


class CreateNestedSingletonPoolInput(Input):
    description: typing.Optional[String] = Field(default=None)
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(default=None, alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


class CreateResourceTypeInput(Input):
    resource_name: String = Field(alias='resourceName')
    resource_properties: Map = Field(alias='resourceProperties')


class CreateSetPoolInput(Input):
    description: typing.Optional[String] = Field(default=None)
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(default=None, alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


class CreateSingletonPoolInput(Input):
    description: typing.Optional[String] = Field(default=None)
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(default=None, alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]] = Field(default=None)


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


class SortResourcePoolsInput(Input):
    direction: OrderDirection
    field: typing.Optional[ResourcePoolOrderField] = Field(default=None)


class TagAnd(Input):
    matches_all: typing.Optional[list[String]] = Field(default=None, alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(default=None, alias='matchesAny')


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
    description: typing.Optional[Boolean] = Field(default=False, alias='Description')
    lang: typing.Optional[Boolean] = Field(default=False, alias='Lang')
    name: typing.Optional[Boolean] = Field(default=False, alias='Name')
    script: typing.Optional[Boolean] = Field(default=False, alias='Script')
    id: typing.Optional[Boolean] = Field(default=False)


class AllocationStrategyPayload(BaseModel):
    description: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Description')
    lang: typing.Optional[typing.Optional[AllocationStrategyLang]] = Field(default=None, alias='Lang')
    name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Name')
    script: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Script')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class CreateAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateAllocatingPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(default=None)


class CreateAllocationStrategyPayloadPayload(BaseModel):
    strategy: typing.Optional[AllocationStrategyPayload] = Field(default=None)


class CreateNestedAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateNestedAllocatingPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateNestedSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateNestedSetPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateNestedSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateNestedSingletonPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateResourceTypePayload(Payload):
    resource_type: typing.Optional[ResourceType] = Field(default=None, alias='resourceType')


class CreateResourceTypePayloadPayload(BaseModel):
    resource_type: typing.Optional[ResourceTypePayload] = Field(default=None, alias='resourceType')


class CreateSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateSetPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(default=None)


class CreateSingletonPoolPayloadPayload(BaseModel):
    pool: typing.Optional[ResourcePoolPayload] = Field(default=None)


class CreateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(default=None)


class CreateTagPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload] = Field(default=None)


class DeleteAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(default=None)


class DeleteAllocationStrategyPayloadPayload(BaseModel):
    strategy: typing.Optional[AllocationStrategyPayload] = Field(default=None)


class DeleteResourcePoolPayload(Payload):
    resource_pool_id: typing.Optional[Boolean] = Field(default=False, alias='resourcePoolId')


class DeleteResourcePoolPayloadPayload(BaseModel):
    resource_pool_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='resourcePoolId')


class DeleteResourceTypePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(default=False, alias='resourceTypeId')


class DeleteResourceTypePayloadPayload(BaseModel):
    resource_type_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='resourceTypeId')


class DeleteTagPayload(Payload):
    tag_id: typing.Optional[Boolean] = Field(default=False, alias='tagId')


class DeleteTagPayloadPayload(BaseModel):
    tag_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='tagId')


class CreateTagMutation(Mutation):
    _name: str = PrivateAttr('CreateTag')
    input: CreateTagInput = Field(json_schema_extra={'type': 'CreateTagInput!'})
    payload: CreateTagPayload


class UpdateTagMutation(Mutation):
    _name: str = PrivateAttr('UpdateTag')
    input: UpdateTagInput = Field(json_schema_extra={'type': 'UpdateTagInput!'})
    payload: UpdateTagPayload


class DeleteTagMutation(Mutation):
    _name: str = PrivateAttr('DeleteTag')
    input: DeleteTagInput = Field(json_schema_extra={'type': 'DeleteTagInput!'})
    payload: DeleteTagPayload


class TagPoolMutation(Mutation):
    _name: str = PrivateAttr('TagPool')
    input: TagPoolInput = Field(json_schema_extra={'type': 'TagPoolInput!'})
    payload: TagPoolPayload


class UntagPoolMutation(Mutation):
    _name: str = PrivateAttr('UntagPool')
    input: UntagPoolInput = Field(json_schema_extra={'type': 'UntagPoolInput!'})
    payload: UntagPoolPayload


class CreateAllocationStrategyMutation(Mutation):
    _name: str = PrivateAttr('CreateAllocationStrategy')
    input: typing.Optional[CreateAllocationStrategyInput] = Field(default=None, json_schema_extra={'type': 'CreateAllocationStrategyInput'})
    payload: CreateAllocationStrategyPayload


class DeleteAllocationStrategyMutation(Mutation):
    _name: str = PrivateAttr('DeleteAllocationStrategy')
    input: typing.Optional[DeleteAllocationStrategyInput] = Field(default=None, json_schema_extra={'type': 'DeleteAllocationStrategyInput'})
    payload: DeleteAllocationStrategyPayload


class TestAllocationStrategyMutation(Mutation):
    _name: str = PrivateAttr('TestAllocationStrategy')
    allocation_strategy_id: ID = Field(alias='allocationStrategyId', json_schema_extra={'type': 'ID!'})
    resource_pool: ResourcePoolInput = Field(alias='resourcePool', json_schema_extra={'type': 'ResourcePoolInput!'})
    current_resources: typing.Optional[list[ResourceInput]] = Field(default=None, alias='currentResources', json_schema_extra={'type': '[ResourceInput!]!'})
    user_input: Map = Field(alias='userInput', json_schema_extra={'type': 'Map!'})
    payload: Boolean


class ClaimResourceMutation(Mutation):
    _name: str = PrivateAttr('ClaimResource')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    description: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    user_input: Map = Field(alias='userInput', json_schema_extra={'type': 'Map!'})
    payload: Resource


class ClaimResourceWithAltIdMutation(Mutation):
    _name: str = PrivateAttr('ClaimResourceWithAltId')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    description: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    user_input: Map = Field(alias='userInput', json_schema_extra={'type': 'Map!'})
    alternative_id: Map = Field(alias='alternativeId', json_schema_extra={'type': 'Map!'})
    payload: Resource


class FreeResourceMutation(Mutation):
    _name: str = PrivateAttr('FreeResource')
    input: Map = Field(json_schema_extra={'type': 'Map!'})
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    payload: Boolean


class CreateSetPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateSetPool')
    input: CreateSetPoolInput = Field(json_schema_extra={'type': 'CreateSetPoolInput!'})
    payload: CreateSetPoolPayload


class CreateNestedSetPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateNestedSetPool')
    input: CreateNestedSetPoolInput = Field(json_schema_extra={'type': 'CreateNestedSetPoolInput!'})
    payload: CreateNestedSetPoolPayload


class CreateSingletonPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateSingletonPool')
    input: typing.Optional[CreateSingletonPoolInput] = Field(default=None, json_schema_extra={'type': 'CreateSingletonPoolInput'})
    payload: CreateSingletonPoolPayload


class CreateNestedSingletonPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateNestedSingletonPool')
    input: CreateNestedSingletonPoolInput = Field(json_schema_extra={'type': 'CreateNestedSingletonPoolInput!'})
    payload: CreateNestedSingletonPoolPayload


class CreateAllocatingPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateAllocatingPool')
    input: typing.Optional[CreateAllocatingPoolInput] = Field(default=None, json_schema_extra={'type': 'CreateAllocatingPoolInput'})
    payload: CreateAllocatingPoolPayload


class CreateNestedAllocatingPoolMutation(Mutation):
    _name: str = PrivateAttr('CreateNestedAllocatingPool')
    input: CreateNestedAllocatingPoolInput = Field(json_schema_extra={'type': 'CreateNestedAllocatingPoolInput!'})
    payload: CreateNestedAllocatingPoolPayload


class DeleteResourcePoolMutation(Mutation):
    _name: str = PrivateAttr('DeleteResourcePool')
    input: DeleteResourcePoolInput = Field(json_schema_extra={'type': 'DeleteResourcePoolInput!'})
    payload: DeleteResourcePoolPayload


class CreateResourceTypeMutation(Mutation):
    _name: str = PrivateAttr('CreateResourceType')
    input: CreateResourceTypeInput = Field(json_schema_extra={'type': 'CreateResourceTypeInput!'})
    payload: CreateResourceTypePayload


class DeleteResourceTypeMutation(Mutation):
    _name: str = PrivateAttr('DeleteResourceType')
    input: DeleteResourceTypeInput = Field(json_schema_extra={'type': 'DeleteResourceTypeInput!'})
    payload: DeleteResourceTypePayload


class UpdateResourceTypeNameMutation(Mutation):
    _name: str = PrivateAttr('UpdateResourceTypeName')
    input: UpdateResourceTypeNameInput = Field(json_schema_extra={'type': 'UpdateResourceTypeNameInput!'})
    payload: UpdateResourceTypeNamePayload


class UpdateResourceAltIdMutation(Mutation):
    _name: str = PrivateAttr('UpdateResourceAltId')
    input: Map = Field(json_schema_extra={'type': 'Map!'})
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    alternative_id: Map = Field(alias='alternativeId', json_schema_extra={'type': 'Map!'})
    payload: Resource


class CreateTagMutationResponse(BaseModel):
    data: typing.Optional[CreateTagData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateTagData(BaseModel):
    create_tag: CreateTagPayloadPayload = Field(alias='CreateTag')


class UpdateTagMutationResponse(BaseModel):
    data: typing.Optional[UpdateTagData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateTagData(BaseModel):
    update_tag: UpdateTagPayloadPayload = Field(alias='UpdateTag')


class DeleteTagMutationResponse(BaseModel):
    data: typing.Optional[DeleteTagData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteTagData(BaseModel):
    delete_tag: DeleteTagPayloadPayload = Field(alias='DeleteTag')


class TagPoolMutationResponse(BaseModel):
    data: typing.Optional[TagPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TagPoolData(BaseModel):
    tag_pool: TagPoolPayloadPayload = Field(alias='TagPool')


class UntagPoolMutationResponse(BaseModel):
    data: typing.Optional[UntagPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UntagPoolData(BaseModel):
    untag_pool: UntagPoolPayloadPayload = Field(alias='UntagPool')


class CreateAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[CreateAllocationStrategyData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateAllocationStrategyData(BaseModel):
    create_allocation_strategy: CreateAllocationStrategyPayloadPayload = Field(alias='CreateAllocationStrategy')


class DeleteAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[DeleteAllocationStrategyData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteAllocationStrategyData(BaseModel):
    delete_allocation_strategy: DeleteAllocationStrategyPayloadPayload = Field(alias='DeleteAllocationStrategy')


class TestAllocationStrategyMutationResponse(BaseModel):
    data: typing.Optional[TestAllocationStrategyData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TestAllocationStrategyData(BaseModel):
    test_allocation_strategy: typing.Optional[Map] = Field(alias='TestAllocationStrategy')


class ClaimResourceMutationResponse(BaseModel):
    data: typing.Optional[ClaimResourceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ClaimResourceData(BaseModel):
    claim_resource: ResourcePayload = Field(alias='ClaimResource')


class ClaimResourceWithAltIdMutationResponse(BaseModel):
    data: typing.Optional[ClaimResourceWithAltIdData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ClaimResourceWithAltIdData(BaseModel):
    claim_resource_with_alt_id: ResourcePayload = Field(alias='ClaimResourceWithAltId')


class FreeResourceMutationResponse(BaseModel):
    data: typing.Optional[FreeResourceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class FreeResourceData(BaseModel):
    free_resource: typing.Optional[String] = Field(alias='FreeResource')


class CreateSetPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateSetPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateSetPoolData(BaseModel):
    create_set_pool: CreateSetPoolPayloadPayload = Field(alias='CreateSetPool')


class CreateNestedSetPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedSetPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateNestedSetPoolData(BaseModel):
    create_nested_set_pool: CreateNestedSetPoolPayloadPayload = Field(alias='CreateNestedSetPool')


class CreateSingletonPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateSingletonPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateSingletonPoolData(BaseModel):
    create_singleton_pool: CreateSingletonPoolPayloadPayload = Field(alias='CreateSingletonPool')


class CreateNestedSingletonPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedSingletonPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateNestedSingletonPoolData(BaseModel):
    create_nested_singleton_pool: CreateNestedSingletonPoolPayloadPayload = Field(alias='CreateNestedSingletonPool')


class CreateAllocatingPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateAllocatingPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateAllocatingPoolData(BaseModel):
    create_allocating_pool: CreateAllocatingPoolPayloadPayload = Field(alias='CreateAllocatingPool')


class CreateNestedAllocatingPoolMutationResponse(BaseModel):
    data: typing.Optional[CreateNestedAllocatingPoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateNestedAllocatingPoolData(BaseModel):
    create_nested_allocating_pool: CreateNestedAllocatingPoolPayloadPayload = Field(alias='CreateNestedAllocatingPool')


class DeleteResourcePoolMutationResponse(BaseModel):
    data: typing.Optional[DeleteResourcePoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteResourcePoolData(BaseModel):
    delete_resource_pool: DeleteResourcePoolPayloadPayload = Field(alias='DeleteResourcePool')


class CreateResourceTypeMutationResponse(BaseModel):
    data: typing.Optional[CreateResourceTypeData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateResourceTypeData(BaseModel):
    create_resource_type: CreateResourceTypePayloadPayload = Field(alias='CreateResourceType')


class DeleteResourceTypeMutationResponse(BaseModel):
    data: typing.Optional[DeleteResourceTypeData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteResourceTypeData(BaseModel):
    delete_resource_type: DeleteResourceTypePayloadPayload = Field(alias='DeleteResourceType')


class UpdateResourceTypeNameMutationResponse(BaseModel):
    data: typing.Optional[UpdateResourceTypeNameData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateResourceTypeNameData(BaseModel):
    update_resource_type_name: UpdateResourceTypeNamePayloadPayload = Field(alias='UpdateResourceTypeName')


class UpdateResourceAltIdMutationResponse(BaseModel):
    data: typing.Optional[UpdateResourceAltIdData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateResourceAltIdData(BaseModel):
    update_resource_alt_id: ResourcePayload = Field(alias='UpdateResourceAltId')


class PageInfo(Payload):
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    has_previous_page: typing.Optional[Boolean] = Field(default=False, alias='hasPreviousPage')
    start_cursor: typing.Optional[Boolean] = Field(default=False, alias='startCursor')


class PageInfoPayload(BaseModel):
    end_cursor: typing.Optional[typing.Optional[Cursor]] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasPreviousPage')
    start_cursor: typing.Optional[typing.Optional[Cursor]] = Field(default=None, alias='startCursor')


class PoolCapacityPayload(Payload):
    free_capacity: typing.Optional[Boolean] = Field(default=False, alias='freeCapacity')
    utilized_capacity: typing.Optional[Boolean] = Field(default=False, alias='utilizedCapacity')


class PoolCapacityPayloadPayload(BaseModel):
    free_capacity: typing.Optional[typing.Optional[String]] = Field(default=None, alias='freeCapacity')
    utilized_capacity: typing.Optional[typing.Optional[String]] = Field(default=None, alias='utilizedCapacity')


class PropertyType(Payload):
    float_val: typing.Optional[Boolean] = Field(default=False, alias='FloatVal')
    int_val: typing.Optional[Boolean] = Field(default=False, alias='IntVal')
    mandatory: typing.Optional[Boolean] = Field(default=False, alias='Mandatory')
    string_val: typing.Optional[Boolean] = Field(default=False, alias='StringVal')
    name: typing.Optional[Boolean] = Field(default=False, alias='Name')
    type: typing.Optional[Boolean] = Field(default=False, alias='Type')
    id: typing.Optional[Boolean] = Field(default=False)


class PropertyTypePayload(BaseModel):
    float_val: typing.Optional[typing.Optional[Float]] = Field(default=None, alias='FloatVal')
    int_val: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='IntVal')
    mandatory: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='Mandatory')
    string_val: typing.Optional[typing.Optional[String]] = Field(default=None, alias='StringVal')
    name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Name')
    type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Type')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class QueryPoolCapacityQuery(Query):
    _name: str = PrivateAttr('QueryPoolCapacity')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    payload: PoolCapacityPayload


class QueryPoolTypesQuery(Query):
    _name: str = PrivateAttr('QueryPoolTypes')


class QueryResourceQuery(Query):
    _name: str = PrivateAttr('QueryResource')
    input: Map = Field(json_schema_extra={'type': 'Map!'})
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    payload: Resource


class QueryResourcesQuery(Query):
    _name: str = PrivateAttr('QueryResources')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    payload: ResourceConnection


class QueryResourcesByAltIdQuery(Query):
    _name: str = PrivateAttr('QueryResourcesByAltId')
    input: Map = Field(json_schema_extra={'type': 'Map!'})
    pool_id: typing.Optional[ID] = Field(default=None, alias='poolId', json_schema_extra={'type': 'ID'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    payload: ResourceConnection


class QueryAllocationStrategyQuery(Query):
    _name: str = PrivateAttr('QueryAllocationStrategy')
    allocation_strategy_id: ID = Field(alias='allocationStrategyId', json_schema_extra={'type': 'ID!'})
    payload: AllocationStrategy


class QueryAllocationStrategiesQuery(Query):
    _name: str = PrivateAttr('QueryAllocationStrategies')
    by_name: typing.Optional[String] = Field(default=None, alias='byName', json_schema_extra={'type': 'String'})
    payload: AllocationStrategy


class QueryResourceTypesQuery(Query):
    _name: str = PrivateAttr('QueryResourceTypes')
    by_name: typing.Optional[String] = Field(default=None, alias='byName', json_schema_extra={'type': 'String'})
    payload: ResourceType


class QueryRequiredPoolPropertiesQuery(Query):
    _name: str = PrivateAttr('QueryRequiredPoolProperties')
    allocation_strategy_name: String = Field(alias='allocationStrategyName', json_schema_extra={'type': 'String!'})
    payload: PropertyType


class QueryResourcePoolQuery(Query):
    _name: str = PrivateAttr('QueryResourcePool')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    payload: ResourcePool


class QueryEmptyResourcePoolsQuery(Query):
    _name: str = PrivateAttr('QueryEmptyResourcePools')
    resource_type_id: typing.Optional[ID] = Field(default=None, alias='resourceTypeId', json_schema_extra={'type': 'ID'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    sort_by: typing.Optional[SortResourcePoolsInput] = Field(default=None, alias='sortBy', json_schema_extra={'type': 'SortResourcePoolsInput'})
    payload: ResourcePoolConnection


class QueryResourcePoolsQuery(Query):
    _name: str = PrivateAttr('QueryResourcePools')
    resource_type_id: typing.Optional[ID] = Field(default=None, alias='resourceTypeId', json_schema_extra={'type': 'ID'})
    tags: typing.Optional[TagOr] = Field(default=None, json_schema_extra={'type': 'TagOr'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    filter_by_resources: typing.Optional[Map] = Field(default=None, alias='filterByResources', json_schema_extra={'type': 'Map'})
    sort_by: typing.Optional[SortResourcePoolsInput] = Field(default=None, alias='sortBy', json_schema_extra={'type': 'SortResourcePoolsInput'})
    payload: ResourcePoolConnection


class QueryRecentlyActiveResourcesQuery(Query):
    _name: str = PrivateAttr('QueryRecentlyActiveResources')
    from_datetime: String = Field(alias='fromDatetime', json_schema_extra={'type': 'String!'})
    to_datetime: typing.Optional[String] = Field(default=None, alias='toDatetime', json_schema_extra={'type': 'String'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: ResourceConnection


class QueryResourcePoolHierarchyPathQuery(Query):
    _name: str = PrivateAttr('QueryResourcePoolHierarchyPath')
    pool_id: ID = Field(alias='poolId', json_schema_extra={'type': 'ID!'})
    payload: ResourcePool


class QueryRootResourcePoolsQuery(Query):
    _name: str = PrivateAttr('QueryRootResourcePools')
    resource_type_id: typing.Optional[ID] = Field(default=None, alias='resourceTypeId', json_schema_extra={'type': 'ID'})
    tags: typing.Optional[TagOr] = Field(default=None, json_schema_extra={'type': 'TagOr'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    filter_by_resources: typing.Optional[Map] = Field(default=None, alias='filterByResources', json_schema_extra={'type': 'Map'})
    sort_by: typing.Optional[SortResourcePoolsInput] = Field(default=None, alias='sortBy', json_schema_extra={'type': 'SortResourcePoolsInput'})
    payload: ResourcePoolConnection


class QueryLeafResourcePoolsQuery(Query):
    _name: str = PrivateAttr('QueryLeafResourcePools')
    resource_type_id: typing.Optional[ID] = Field(default=None, alias='resourceTypeId', json_schema_extra={'type': 'ID'})
    tags: typing.Optional[TagOr] = Field(default=None, json_schema_extra={'type': 'TagOr'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    filter_by_resources: typing.Optional[Map] = Field(default=None, alias='filterByResources', json_schema_extra={'type': 'Map'})
    sort_by: typing.Optional[SortResourcePoolsInput] = Field(default=None, alias='sortBy', json_schema_extra={'type': 'SortResourcePoolsInput'})
    payload: ResourcePoolConnection


class SearchPoolsByTagsQuery(Query):
    _name: str = PrivateAttr('SearchPoolsByTags')
    tags: typing.Optional[TagOr] = Field(default=None, json_schema_extra={'type': 'TagOr'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    after: typing.Optional[Cursor] = Field(default=None, json_schema_extra={'type': 'Cursor'})
    payload: ResourcePoolConnection


class QueryTagsQuery(Query):
    _name: str = PrivateAttr('QueryTags')


class NodeQuery(Query):
    _name: str = PrivateAttr('node')
    id: ID = Field(json_schema_extra={'type': 'ID!'})
    payload: Node


class QueryPoolCapacityQueryResponse(BaseModel):
    data: typing.Optional[QueryPoolCapacityData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryPoolCapacityData(BaseModel):
    query_pool_capacity: PoolCapacityPayloadPayload = Field(alias='QueryPoolCapacity')


class QueryResourceQueryResponse(BaseModel):
    data: typing.Optional[QueryResourceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourceData(BaseModel):
    query_resource: ResourcePayload = Field(alias='QueryResource')


class QueryResourcesQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourcesData(BaseModel):
    query_resources: ResourceConnectionPayload = Field(alias='QueryResources')


class QueryResourcesByAltIdQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcesByAltIdData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourcesByAltIdData(BaseModel):
    query_resources_by_alt_id: ResourceConnectionPayload = Field(alias='QueryResourcesByAltId')


class QueryAllocationStrategyQueryResponse(BaseModel):
    data: typing.Optional[QueryAllocationStrategyData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryAllocationStrategyData(BaseModel):
    query_allocation_strategy: AllocationStrategyPayload = Field(alias='QueryAllocationStrategy')


class QueryAllocationStrategiesQueryResponse(BaseModel):
    data: typing.Optional[QueryAllocationStrategiesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryAllocationStrategiesData(BaseModel):
    query_allocation_strategies: typing.Optional[list[AllocationStrategyPayload]] = Field(alias='QueryAllocationStrategies')


class QueryResourceTypesQueryResponse(BaseModel):
    data: typing.Optional[QueryResourceTypesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourceTypesData(BaseModel):
    query_resource_types: typing.Optional[list[ResourceTypePayload]] = Field(alias='QueryResourceTypes')


class QueryRequiredPoolPropertiesQueryResponse(BaseModel):
    data: typing.Optional[QueryRequiredPoolPropertiesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryRequiredPoolPropertiesData(BaseModel):
    query_required_pool_properties: typing.Optional[list[PropertyTypePayload]] = Field(alias='QueryRequiredPoolProperties')


class QueryResourcePoolQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourcePoolData(BaseModel):
    query_resource_pool: ResourcePoolPayload = Field(alias='QueryResourcePool')


class QueryEmptyResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryEmptyResourcePoolsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryEmptyResourcePoolsData(BaseModel):
    query_empty_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryEmptyResourcePools')


class QueryResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourcePoolsData(BaseModel):
    query_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryResourcePools')


class QueryRecentlyActiveResourcesQueryResponse(BaseModel):
    data: typing.Optional[QueryRecentlyActiveResourcesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryRecentlyActiveResourcesData(BaseModel):
    query_recently_active_resources: ResourceConnectionPayload = Field(alias='QueryRecentlyActiveResources')


class QueryResourcePoolHierarchyPathQueryResponse(BaseModel):
    data: typing.Optional[QueryResourcePoolHierarchyPathData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryResourcePoolHierarchyPathData(BaseModel):
    query_resource_pool_hierarchy_path: typing.Optional[list[ResourcePoolPayload]] = Field(alias='QueryResourcePoolHierarchyPath')


class QueryRootResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryRootResourcePoolsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryRootResourcePoolsData(BaseModel):
    query_root_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryRootResourcePools')


class QueryLeafResourcePoolsQueryResponse(BaseModel):
    data: typing.Optional[QueryLeafResourcePoolsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class QueryLeafResourcePoolsData(BaseModel):
    query_leaf_resource_pools: ResourcePoolConnectionPayload = Field(alias='QueryLeafResourcePools')


class SearchPoolsByTagsQueryResponse(BaseModel):
    data: typing.Optional[SearchPoolsByTagsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SearchPoolsByTagsData(BaseModel):
    search_pools_by_tags: ResourcePoolConnectionPayload = Field(alias='SearchPoolsByTags')


class NodeQueryResponse(BaseModel):
    data: typing.Optional[Node] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class Resource(Payload):
    description: typing.Optional[Boolean] = Field(default=False, alias='Description')
    nested_pool: typing.Optional[ResourcePool] = Field(default=None, alias='NestedPool')
    parent_pool: typing.Optional[ResourcePool] = Field(default=None, alias='ParentPool')
    properties: typing.Optional[Boolean] = Field(default=False, alias='Properties')
    alternative_id: typing.Optional[Boolean] = Field(default=False, alias='AlternativeId')
    id: typing.Optional[Boolean] = Field(default=False)


class ResourcePayload(BaseModel):
    description: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Description')
    nested_pool: typing.Optional[ResourcePoolPayload] = Field(default=None, alias='NestedPool')
    parent_pool: typing.Optional[ResourcePoolPayload] = Field(default=None, alias='ParentPool')
    properties: typing.Optional[typing.Optional[Map]] = Field(default=None, alias='Properties')
    alternative_id: typing.Optional[typing.Optional[Map]] = Field(default=None, alias='AlternativeId')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class ResourceConnection(Payload):
    edges: typing.Optional[ResourceEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class ResourceConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ResourceEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class ResourceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[Resource] = Field(default=None)


class ResourceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[Cursor]] = Field(default=None)
    node: typing.Optional[ResourcePayload] = Field(default=None)


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(default=None, alias='AllocationStrategy')
    capacity: typing.Optional[PoolCapacityPayload] = Field(default=None, alias='Capacity')
    name: typing.Optional[Boolean] = Field(default=False, alias='Name')
    parent_resource: typing.Optional[Resource] = Field(default=None, alias='ParentResource')
    pool_properties: typing.Optional[Boolean] = Field(default=False, alias='PoolProperties')
    pool_type: typing.Optional[Boolean] = Field(default=False, alias='PoolType')
    resource_type: typing.Optional[ResourceType] = Field(default=None, alias='ResourceType')
    resources: typing.Optional[Resource] = Field(default=None, alias='Resources')
    dealocation_safety_period: typing.Optional[Boolean] = Field(default=False, alias='DealocationSafetyPeriod')
    tags: typing.Optional[Tag] = Field(default=None, alias='Tags')
    allocated_resources: typing.Optional[ResourceConnection] = Field(default=None, alias='allocatedResources')
    id: typing.Optional[Boolean] = Field(default=False)


class ResourcePoolPayload(BaseModel):
    allocation_strategy: typing.Optional[AllocationStrategyPayload] = Field(default=None, alias='AllocationStrategy')
    capacity: typing.Optional[PoolCapacityPayloadPayload] = Field(default=None, alias='Capacity')
    name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Name')
    parent_resource: typing.Optional[ResourcePayload] = Field(default=None, alias='ParentResource')
    pool_properties: typing.Optional[typing.Optional[Map]] = Field(default=None, alias='PoolProperties')
    pool_type: typing.Optional[typing.Optional[PoolType]] = Field(default=None, alias='PoolType')
    resource_type: typing.Optional[ResourceTypePayload] = Field(default=None, alias='ResourceType')
    resources: typing.Optional[typing.Optional[list[ResourcePayload]]] = Field(default=None, alias='Resources')
    dealocation_safety_period: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='DealocationSafetyPeriod')
    tags: typing.Optional[typing.Optional[list[TagPayload]]] = Field(default=None, alias='Tags')
    allocated_resources: typing.Optional[ResourceConnectionPayload] = Field(default=None, alias='allocatedResources')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class ResourcePoolConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ResourcePoolEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[ResourcePool] = Field(default=None)


class ResourcePoolEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[Cursor]] = Field(default=None)
    node: typing.Optional[ResourcePoolPayload] = Field(default=None)


class ResourceType(Payload):
    name: typing.Optional[Boolean] = Field(default=False, alias='Name')
    pools: typing.Optional[ResourcePool] = Field(default=None, alias='Pools')
    property_types: typing.Optional[PropertyType] = Field(default=None, alias='PropertyTypes')
    id: typing.Optional[Boolean] = Field(default=False)


class ResourceTypePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Name')
    pools: typing.Optional[typing.Optional[list[ResourcePoolPayload]]] = Field(default=None, alias='Pools')
    property_types: typing.Optional[typing.Optional[list[PropertyTypePayload]]] = Field(default=None, alias='PropertyTypes')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class Tag(Payload):
    pools: typing.Optional[ResourcePool] = Field(default=None, alias='Pools')
    tag: typing.Optional[Boolean] = Field(default=False, alias='Tag')
    id: typing.Optional[Boolean] = Field(default=False)


class TagPayload(BaseModel):
    pools: typing.Optional[typing.Optional[list[ResourcePoolPayload]]] = Field(default=None, alias='Pools')
    tag: typing.Optional[typing.Optional[String]] = Field(default=None, alias='Tag')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)


class TagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(default=None)


class TagPoolPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload] = Field(default=None)


class UntagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(default=None)


class UntagPoolPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload] = Field(default=None)


class UpdateResourceTypeNamePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(default=False, alias='resourceTypeId')


class UpdateResourceTypeNamePayloadPayload(BaseModel):
    resource_type_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='resourceTypeId')


class UpdateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(default=None)


class UpdateTagPayloadPayload(BaseModel):
    tag: typing.Optional[TagPayload] = Field(default=None)


Node.model_rebuild()
CreateAllocatingPoolInput.model_rebuild()
CreateAllocationStrategyInput.model_rebuild()
CreateNestedAllocatingPoolInput.model_rebuild()
CreateNestedSetPoolInput.model_rebuild()
CreateNestedSingletonPoolInput.model_rebuild()
CreateResourceTypeInput.model_rebuild()
CreateSetPoolInput.model_rebuild()
CreateSingletonPoolInput.model_rebuild()
CreateTagInput.model_rebuild()
DeleteAllocationStrategyInput.model_rebuild()
DeleteResourcePoolInput.model_rebuild()
DeleteResourceTypeInput.model_rebuild()
DeleteTagInput.model_rebuild()
ResourceInput.model_rebuild()
ResourcePoolInput.model_rebuild()
SortResourcePoolsInput.model_rebuild()
TagAnd.model_rebuild()
TagOr.model_rebuild()
TagPoolInput.model_rebuild()
UntagPoolInput.model_rebuild()
UpdateResourceTypeNameInput.model_rebuild()
UpdateTagInput.model_rebuild()
AllocationStrategy.model_rebuild()
AllocationStrategyPayload.model_rebuild()
CreateAllocatingPoolPayload.model_rebuild()
CreateAllocatingPoolPayloadPayload.model_rebuild()
CreateAllocationStrategyPayload.model_rebuild()
CreateAllocationStrategyPayloadPayload.model_rebuild()
CreateNestedAllocatingPoolPayload.model_rebuild()
CreateNestedAllocatingPoolPayloadPayload.model_rebuild()
CreateNestedSetPoolPayload.model_rebuild()
CreateNestedSetPoolPayloadPayload.model_rebuild()
CreateNestedSingletonPoolPayload.model_rebuild()
CreateNestedSingletonPoolPayloadPayload.model_rebuild()
CreateResourceTypePayload.model_rebuild()
CreateResourceTypePayloadPayload.model_rebuild()
CreateSetPoolPayload.model_rebuild()
CreateSetPoolPayloadPayload.model_rebuild()
CreateSingletonPoolPayload.model_rebuild()
CreateSingletonPoolPayloadPayload.model_rebuild()
CreateTagPayload.model_rebuild()
CreateTagPayloadPayload.model_rebuild()
DeleteAllocationStrategyPayload.model_rebuild()
DeleteAllocationStrategyPayloadPayload.model_rebuild()
DeleteResourcePoolPayload.model_rebuild()
DeleteResourcePoolPayloadPayload.model_rebuild()
DeleteResourceTypePayload.model_rebuild()
DeleteResourceTypePayloadPayload.model_rebuild()
DeleteTagPayload.model_rebuild()
DeleteTagPayloadPayload.model_rebuild()
CreateTagMutation.model_rebuild()
UpdateTagMutation.model_rebuild()
DeleteTagMutation.model_rebuild()
TagPoolMutation.model_rebuild()
UntagPoolMutation.model_rebuild()
CreateAllocationStrategyMutation.model_rebuild()
DeleteAllocationStrategyMutation.model_rebuild()
TestAllocationStrategyMutation.model_rebuild()
ClaimResourceMutation.model_rebuild()
ClaimResourceWithAltIdMutation.model_rebuild()
FreeResourceMutation.model_rebuild()
CreateSetPoolMutation.model_rebuild()
CreateNestedSetPoolMutation.model_rebuild()
CreateSingletonPoolMutation.model_rebuild()
CreateNestedSingletonPoolMutation.model_rebuild()
CreateAllocatingPoolMutation.model_rebuild()
CreateNestedAllocatingPoolMutation.model_rebuild()
DeleteResourcePoolMutation.model_rebuild()
CreateResourceTypeMutation.model_rebuild()
DeleteResourceTypeMutation.model_rebuild()
UpdateResourceTypeNameMutation.model_rebuild()
UpdateResourceAltIdMutation.model_rebuild()
CreateTagMutationResponse.model_rebuild()
CreateTagData.model_rebuild()
UpdateTagMutationResponse.model_rebuild()
UpdateTagData.model_rebuild()
DeleteTagMutationResponse.model_rebuild()
DeleteTagData.model_rebuild()
TagPoolMutationResponse.model_rebuild()
TagPoolData.model_rebuild()
UntagPoolMutationResponse.model_rebuild()
UntagPoolData.model_rebuild()
CreateAllocationStrategyMutationResponse.model_rebuild()
CreateAllocationStrategyData.model_rebuild()
DeleteAllocationStrategyMutationResponse.model_rebuild()
DeleteAllocationStrategyData.model_rebuild()
TestAllocationStrategyMutationResponse.model_rebuild()
TestAllocationStrategyData.model_rebuild()
ClaimResourceMutationResponse.model_rebuild()
ClaimResourceData.model_rebuild()
ClaimResourceWithAltIdMutationResponse.model_rebuild()
ClaimResourceWithAltIdData.model_rebuild()
FreeResourceMutationResponse.model_rebuild()
FreeResourceData.model_rebuild()
CreateSetPoolMutationResponse.model_rebuild()
CreateSetPoolData.model_rebuild()
CreateNestedSetPoolMutationResponse.model_rebuild()
CreateNestedSetPoolData.model_rebuild()
CreateSingletonPoolMutationResponse.model_rebuild()
CreateSingletonPoolData.model_rebuild()
CreateNestedSingletonPoolMutationResponse.model_rebuild()
CreateNestedSingletonPoolData.model_rebuild()
CreateAllocatingPoolMutationResponse.model_rebuild()
CreateAllocatingPoolData.model_rebuild()
CreateNestedAllocatingPoolMutationResponse.model_rebuild()
CreateNestedAllocatingPoolData.model_rebuild()
DeleteResourcePoolMutationResponse.model_rebuild()
DeleteResourcePoolData.model_rebuild()
CreateResourceTypeMutationResponse.model_rebuild()
CreateResourceTypeData.model_rebuild()
DeleteResourceTypeMutationResponse.model_rebuild()
DeleteResourceTypeData.model_rebuild()
UpdateResourceTypeNameMutationResponse.model_rebuild()
UpdateResourceTypeNameData.model_rebuild()
UpdateResourceAltIdMutationResponse.model_rebuild()
UpdateResourceAltIdData.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
PoolCapacityPayload.model_rebuild()
PoolCapacityPayloadPayload.model_rebuild()
PropertyType.model_rebuild()
PropertyTypePayload.model_rebuild()
QueryPoolCapacityQuery.model_rebuild()
QueryPoolTypesQuery.model_rebuild()
QueryResourceQuery.model_rebuild()
QueryResourcesQuery.model_rebuild()
QueryResourcesByAltIdQuery.model_rebuild()
QueryAllocationStrategyQuery.model_rebuild()
QueryAllocationStrategiesQuery.model_rebuild()
QueryResourceTypesQuery.model_rebuild()
QueryRequiredPoolPropertiesQuery.model_rebuild()
QueryResourcePoolQuery.model_rebuild()
QueryEmptyResourcePoolsQuery.model_rebuild()
QueryResourcePoolsQuery.model_rebuild()
QueryRecentlyActiveResourcesQuery.model_rebuild()
QueryResourcePoolHierarchyPathQuery.model_rebuild()
QueryRootResourcePoolsQuery.model_rebuild()
QueryLeafResourcePoolsQuery.model_rebuild()
SearchPoolsByTagsQuery.model_rebuild()
QueryTagsQuery.model_rebuild()
NodeQuery.model_rebuild()
QueryPoolCapacityQueryResponse.model_rebuild()
QueryPoolCapacityData.model_rebuild()
QueryResourceQueryResponse.model_rebuild()
QueryResourceData.model_rebuild()
QueryResourcesQueryResponse.model_rebuild()
QueryResourcesData.model_rebuild()
QueryResourcesByAltIdQueryResponse.model_rebuild()
QueryResourcesByAltIdData.model_rebuild()
QueryAllocationStrategyQueryResponse.model_rebuild()
QueryAllocationStrategyData.model_rebuild()
QueryAllocationStrategiesQueryResponse.model_rebuild()
QueryAllocationStrategiesData.model_rebuild()
QueryResourceTypesQueryResponse.model_rebuild()
QueryResourceTypesData.model_rebuild()
QueryRequiredPoolPropertiesQueryResponse.model_rebuild()
QueryRequiredPoolPropertiesData.model_rebuild()
QueryResourcePoolQueryResponse.model_rebuild()
QueryResourcePoolData.model_rebuild()
QueryEmptyResourcePoolsQueryResponse.model_rebuild()
QueryEmptyResourcePoolsData.model_rebuild()
QueryResourcePoolsQueryResponse.model_rebuild()
QueryResourcePoolsData.model_rebuild()
QueryRecentlyActiveResourcesQueryResponse.model_rebuild()
QueryRecentlyActiveResourcesData.model_rebuild()
QueryResourcePoolHierarchyPathQueryResponse.model_rebuild()
QueryResourcePoolHierarchyPathData.model_rebuild()
QueryRootResourcePoolsQueryResponse.model_rebuild()
QueryRootResourcePoolsData.model_rebuild()
QueryLeafResourcePoolsQueryResponse.model_rebuild()
QueryLeafResourcePoolsData.model_rebuild()
SearchPoolsByTagsQueryResponse.model_rebuild()
SearchPoolsByTagsData.model_rebuild()
NodeQueryResponse.model_rebuild()
Resource.model_rebuild()
ResourcePayload.model_rebuild()
ResourceConnection.model_rebuild()
ResourceConnectionPayload.model_rebuild()
ResourceEdge.model_rebuild()
ResourceEdgePayload.model_rebuild()
ResourcePool.model_rebuild()
ResourcePoolPayload.model_rebuild()
ResourcePoolConnection.model_rebuild()
ResourcePoolConnectionPayload.model_rebuild()
ResourcePoolEdge.model_rebuild()
ResourcePoolEdgePayload.model_rebuild()
ResourceType.model_rebuild()
ResourceTypePayload.model_rebuild()
Tag.model_rebuild()
TagPayload.model_rebuild()
TagPoolPayload.model_rebuild()
TagPoolPayloadPayload.model_rebuild()
UntagPoolPayload.model_rebuild()
UntagPoolPayloadPayload.model_rebuild()
UpdateResourceTypeNamePayload.model_rebuild()
UpdateResourceTypeNamePayloadPayload.model_rebuild()
UpdateTagPayload.model_rebuild()
UpdateTagPayloadPayload.model_rebuild()

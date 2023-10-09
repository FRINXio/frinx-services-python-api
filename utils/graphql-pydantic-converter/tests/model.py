from __future__ import annotations

import typing

from pydantic import BaseModel
from pydantic import Field

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from graphql_pydantic_converter.graphql_types import Subscription

String: typing.TypeAlias = str
Int: typing.TypeAlias = int
Boolean: typing.TypeAlias = bool
ID: typing.TypeAlias = str
Float: typing.TypeAlias = float


class DeviceServiceState(ENUM):
    IN_SERVICE = 'IN_SERVICE'
    OUT_OF_SERVICE = 'OUT_OF_SERVICE'
    PLANNING = 'PLANNING'


class DeviceSize(ENUM):
    LARGE = 'LARGE'
    MEDIUM = 'MEDIUM'
    SMALL = 'SMALL'


class GraphEdgeStatus(ENUM):
    ok = 'ok'
    unknown = 'unknown'


class BaseGraphNode(Interface):
    coordinates: typing.Optional[GraphNodeCoordinates]
    device_type: typing.Optional[Boolean] = Field(alias='deviceType')
    id: typing.Optional[Boolean]
    interfaces: typing.Optional[GraphNodeInterface]
    software_version: typing.Optional[Boolean] = Field(alias='softwareVersion')


class Node(Interface):
    id: typing.Optional[Boolean]


class AddBlueprintInput(Input):
    name: String
    template: String


class AddDeviceInput(Input):
    address: typing.Optional[String]
    blueprint_id: typing.Optional[String] = Field(alias='blueprintId')
    device_size: typing.Optional[DeviceSize] = Field(alias='deviceSize')
    device_type: typing.Optional[String] = Field(alias='deviceType')
    label_ids: typing.Optional[list[String]] = Field(alias='labelIds')
    model: typing.Optional[String]
    mount_parameters: typing.Optional[String] = Field(alias='mountParameters')
    name: String
    password: typing.Optional[String]
    port: typing.Optional[Int]
    service_state: typing.Optional[DeviceServiceState] = Field(alias='serviceState')
    username: typing.Optional[String]
    vendor: typing.Optional[String]
    version: typing.Optional[String]
    zone_id: String = Field(alias='zoneId')


class GraphNodeCoordinatesInput(Input):
    device_name: String = Field(alias='deviceName')
    x: Float
    y: Float


class UpdateBlueprintInput(Input):
    name: typing.Optional[String]
    template: typing.Optional[String]


class AddBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class AddBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload]


class Blueprint(Payload):
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=False)
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    template: typing.Optional[Boolean] = Field(response='String', default=False)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=False)


class BlueprintPayload(BaseModel):
    created_at: typing.Optional[typing.Optional[String]] = Field(alias='createdAt')
    id: typing.Optional[typing.Optional[ID]]
    name: typing.Optional[typing.Optional[String]]
    template: typing.Optional[typing.Optional[String]]
    updated_at: typing.Optional[typing.Optional[String]] = Field(alias='updatedAt')


class BlueprintConnection(Payload):
    edges: typing.Optional[BlueprintEdge] = Field(response='BlueprintEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=False)


class BlueprintConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[BlueprintEdgePayload]]]
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(alias='totalCount')


class BlueprintEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[Blueprint] = Field(response='Blueprint')


class BlueprintEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[BlueprintPayload]


class DeleteBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class DeleteBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload]


class GraphNodeCoordinates(Payload):
    x: typing.Optional[Boolean] = Field(response='Float', default=False)
    y: typing.Optional[Boolean] = Field(response='Float', default=False)


class GraphNodeCoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]]
    y: typing.Optional[typing.Optional[Float]]


class AddBlueprintMutation(Mutation):
    _name: str = Field('addBlueprint', const=True)
    input: AddBlueprintInput
    payload: AddBlueprintPayload


class DeleteBlueprintMutation(Mutation):
    _name: str = Field('deleteBlueprint', const=True)
    id: String
    payload: DeleteBlueprintPayload


class UpdateBlueprintMutation(Mutation):
    _name: str = Field('updateBlueprint', const=True)
    id: String
    input: UpdateBlueprintInput
    payload: UpdateBlueprintPayload


class AddBlueprintMutationResponse(BaseModel):
    data: typing.Optional[AddBlueprintData]
    errors: typing.Optional[typing.Any]


class AddBlueprintData(BaseModel):
    add_blueprint: AddBlueprintPayloadPayload = Field(alias='addBlueprint')


class DeleteBlueprintMutationResponse(BaseModel):
    data: typing.Optional[DeleteBlueprintData]
    errors: typing.Optional[typing.Any]


class DeleteBlueprintData(BaseModel):
    delete_blueprint: DeleteBlueprintPayloadPayload = Field(alias='deleteBlueprint')


class UpdateBlueprintMutationResponse(BaseModel):
    data: typing.Optional[UpdateBlueprintData]
    errors: typing.Optional[typing.Any]


class UpdateBlueprintData(BaseModel):
    update_blueprint: UpdateBlueprintPayloadPayload = Field(alias='updateBlueprint')


class GraphNodeInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='String', default=False)
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    status: typing.Optional[Boolean] = Field(response='GraphEdgeStatus', default=False)


class GraphNodeInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[String]]
    name: typing.Optional[typing.Optional[String]]
    status: typing.Optional[typing.Optional[GraphEdgeStatus]]


class PageInfo(Payload):
    end_cursor: typing.Optional[Boolean] = Field(response='String', alias='endCursor', default=False)
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=False)
    has_previous_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasPreviousPage', default=False)
    start_cursor: typing.Optional[Boolean] = Field(response='String', alias='startCursor', default=False)


class PageInfoPayload(BaseModel):
    end_cursor: typing.Optional[typing.Optional[String]] = Field(alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(alias='hasPreviousPage')
    start_cursor: typing.Optional[typing.Optional[String]] = Field(alias='startCursor')


class BlueprintsQuery(Query):
    _name: str = Field('blueprints', const=True)
    after: typing.Optional[String]
    before: typing.Optional[String]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    payload: BlueprintConnection


class BlueprintsQueryResponse(BaseModel):
    data: typing.Optional[BlueprintsData]
    errors: typing.Optional[typing.Any]


class BlueprintsData(BaseModel):
    blueprints: BlueprintConnectionPayload


class UniconfigShellSubscription(Subscription):
    _name: str = Field('uniconfigShell', const=True)
    input: typing.Optional[String]
    session_id: String = Field(alias='sessionId')
    trigger: typing.Optional[Int]
    payload: Boolean


class UniconfigShellSubscriptionResponse(BaseModel):
    data: typing.Optional[UniconfigShellData]
    errors: typing.Optional[typing.Any]


class UniconfigShellData(BaseModel):
    uniconfig_shell: typing.Optional[typing.Optional[String]] = Field(alias='uniconfigShell')


class UpdateBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class UpdateBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload]


BaseGraphNode.update_forward_refs()
Node.update_forward_refs()
AddBlueprintInput.update_forward_refs()
AddDeviceInput.update_forward_refs()
GraphNodeCoordinatesInput.update_forward_refs()
UpdateBlueprintInput.update_forward_refs()
AddBlueprintPayload.update_forward_refs()
AddBlueprintPayloadPayload.update_forward_refs()
Blueprint.update_forward_refs()
BlueprintPayload.update_forward_refs()
BlueprintConnection.update_forward_refs()
BlueprintConnectionPayload.update_forward_refs()
BlueprintEdge.update_forward_refs()
BlueprintEdgePayload.update_forward_refs()
DeleteBlueprintPayload.update_forward_refs()
DeleteBlueprintPayloadPayload.update_forward_refs()
GraphNodeCoordinates.update_forward_refs()
GraphNodeCoordinatesPayload.update_forward_refs()
AddBlueprintMutation.update_forward_refs()
DeleteBlueprintMutation.update_forward_refs()
UpdateBlueprintMutation.update_forward_refs()
AddBlueprintMutationResponse.update_forward_refs()
AddBlueprintData.update_forward_refs()
DeleteBlueprintMutationResponse.update_forward_refs()
DeleteBlueprintData.update_forward_refs()
UpdateBlueprintMutationResponse.update_forward_refs()
UpdateBlueprintData.update_forward_refs()
GraphNodeInterface.update_forward_refs()
GraphNodeInterfacePayload.update_forward_refs()
PageInfo.update_forward_refs()
PageInfoPayload.update_forward_refs()
BlueprintsQuery.update_forward_refs()
BlueprintsQueryResponse.update_forward_refs()
BlueprintsData.update_forward_refs()
UniconfigShellSubscription.update_forward_refs()
UniconfigShellSubscriptionResponse.update_forward_refs()
UniconfigShellData.update_forward_refs()
UpdateBlueprintPayload.update_forward_refs()
UpdateBlueprintPayloadPayload.update_forward_refs()

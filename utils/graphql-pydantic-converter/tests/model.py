from __future__ import annotations

import typing

from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

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
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)
    device_type: typing.Optional[Boolean] = Field(default=None, alias='deviceType')
    id: typing.Optional[Boolean] = Field(default=None)
    interfaces: typing.Optional[GraphNodeInterface] = Field(default=None)
    software_version: typing.Optional[Boolean] = Field(default=None, alias='softwareVersion')


class Node(Interface):
    id: typing.Optional[Boolean] = Field(default=None)


class AddBlueprintInput(Input):
    name: String
    template: String


class AddDeviceInput(Input):
    address: typing.Optional[String] = Field(default=None)
    blueprint_id: typing.Optional[String] = Field(default=None, alias='blueprintId')
    device_size: typing.Optional[DeviceSize] = Field(default=None, alias='deviceSize')
    device_type: typing.Optional[String] = Field(default=None, alias='deviceType')
    label_ids: typing.Optional[list[String]] = Field(default=None, alias='labelIds')
    model: typing.Optional[String] = Field(default=None)
    mount_parameters: typing.Optional[String] = Field(default=None, alias='mountParameters')
    name: String
    password: typing.Optional[String] = Field(default=None)
    port: typing.Optional[Int] = Field(default=None)
    service_state: typing.Optional[DeviceServiceState] = Field(default=None, alias='serviceState')
    username: typing.Optional[String] = Field(default=None)
    vendor: typing.Optional[String] = Field(default=None)
    version: typing.Optional[String] = Field(default=None)
    zone_id: String = Field(alias='zoneId')


class GraphNodeCoordinatesInput(Input):
    device_name: String = Field(alias='deviceName')
    x: Float
    y: Float


class UpdateBlueprintInput(Input):
    name: typing.Optional[String] = Field(default=None)
    template: typing.Optional[String] = Field(default=None)


class AddBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class AddBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class Blueprint(Payload):
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    template: typing.Optional[Boolean] = Field(default=False)
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')


class BlueprintPayload(BaseModel):
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    template: typing.Optional[typing.Optional[String]] = Field(default=None)
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')


class BlueprintConnection(Payload):
    edges: typing.Optional[BlueprintEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class BlueprintConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[BlueprintEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class BlueprintEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[Blueprint] = Field(default=None)


class BlueprintEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[BlueprintPayload] = Field(default=None)


class DeleteBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class DeleteBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class GraphNodeCoordinates(Payload):
    x: typing.Optional[Boolean] = Field(default=False)
    y: typing.Optional[Boolean] = Field(default=False)


class GraphNodeCoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]] = Field(default=None)
    y: typing.Optional[typing.Optional[Float]] = Field(default=None)


class AddBlueprintMutation(Mutation):
    _name: str = PrivateAttr('addBlueprint')
    input: AddBlueprintInput
    payload: AddBlueprintPayload


class DeleteBlueprintMutation(Mutation):
    _name: str = PrivateAttr('deleteBlueprint')
    id: String
    payload: DeleteBlueprintPayload


class UpdateBlueprintMutation(Mutation):
    _name: str = PrivateAttr('updateBlueprint')
    id: String
    input: UpdateBlueprintInput
    payload: UpdateBlueprintPayload


class AddBlueprintMutationResponse(BaseModel):
    data: typing.Optional[AddBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddBlueprintData(BaseModel):
    add_blueprint: AddBlueprintPayloadPayload = Field(alias='addBlueprint')


class DeleteBlueprintMutationResponse(BaseModel):
    data: typing.Optional[DeleteBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteBlueprintData(BaseModel):
    delete_blueprint: DeleteBlueprintPayloadPayload = Field(alias='deleteBlueprint')


class UpdateBlueprintMutationResponse(BaseModel):
    data: typing.Optional[UpdateBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateBlueprintData(BaseModel):
    update_blueprint: UpdateBlueprintPayloadPayload = Field(alias='updateBlueprint')


class GraphNodeInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)


class GraphNodeInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[String]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[GraphEdgeStatus]] = Field(default=None)


class PageInfo(Payload):
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    has_previous_page: typing.Optional[Boolean] = Field(default=False, alias='hasPreviousPage')
    start_cursor: typing.Optional[Boolean] = Field(default=False, alias='startCursor')


class PageInfoPayload(BaseModel):
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasPreviousPage')
    start_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='startCursor')


class BlueprintsQuery(Query):
    _name: str = PrivateAttr('blueprints')
    after: typing.Optional[String] = Field(default=None)
    before: typing.Optional[String] = Field(default=None)
    first: typing.Optional[Int] = Field(default=None)
    last: typing.Optional[Int] = Field(default=None)
    payload: BlueprintConnection


class BlueprintsQueryResponse(BaseModel):
    data: typing.Optional[BlueprintsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class BlueprintsData(BaseModel):
    blueprints: BlueprintConnectionPayload


class UniconfigShellSubscription(Subscription):
    _name: str = PrivateAttr('uniconfigShell')
    input: typing.Optional[String] = Field(default=None)
    session_id: String = Field(alias='sessionId')
    trigger: typing.Optional[Int] = Field(default=None)
    payload: Boolean


class UniconfigShellSubscriptionResponse(BaseModel):
    data: typing.Optional[UniconfigShellData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UniconfigShellData(BaseModel):
    uniconfig_shell: typing.Optional[typing.Optional[String]] = Field(alias='uniconfigShell')


class UpdateBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class UpdateBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


BaseGraphNode.model_rebuild()
Node.model_rebuild()
AddBlueprintInput.model_rebuild()
AddDeviceInput.model_rebuild()
GraphNodeCoordinatesInput.model_rebuild()
UpdateBlueprintInput.model_rebuild()
AddBlueprintPayload.model_rebuild()
AddBlueprintPayloadPayload.model_rebuild()
Blueprint.model_rebuild()
BlueprintPayload.model_rebuild()
BlueprintConnection.model_rebuild()
BlueprintConnectionPayload.model_rebuild()
BlueprintEdge.model_rebuild()
BlueprintEdgePayload.model_rebuild()
DeleteBlueprintPayload.model_rebuild()
DeleteBlueprintPayloadPayload.model_rebuild()
GraphNodeCoordinates.model_rebuild()
GraphNodeCoordinatesPayload.model_rebuild()
AddBlueprintMutation.model_rebuild()
DeleteBlueprintMutation.model_rebuild()
UpdateBlueprintMutation.model_rebuild()
AddBlueprintMutationResponse.model_rebuild()
AddBlueprintData.model_rebuild()
DeleteBlueprintMutationResponse.model_rebuild()
DeleteBlueprintData.model_rebuild()
UpdateBlueprintMutationResponse.model_rebuild()
UpdateBlueprintData.model_rebuild()
GraphNodeInterface.model_rebuild()
GraphNodeInterfacePayload.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
BlueprintsQuery.model_rebuild()
BlueprintsQueryResponse.model_rebuild()
BlueprintsData.model_rebuild()
UniconfigShellSubscription.model_rebuild()
UniconfigShellSubscriptionResponse.model_rebuild()
UniconfigShellData.model_rebuild()
UpdateBlueprintPayload.model_rebuild()
UpdateBlueprintPayloadPayload.model_rebuild()

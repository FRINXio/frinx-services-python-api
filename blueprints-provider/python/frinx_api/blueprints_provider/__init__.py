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
DateTime: typing.TypeAlias = typing.Any
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
JSON: typing.TypeAlias = typing.Any
String: typing.TypeAlias = str


class BlueprintType(ENUM):
    INSTALL = 'INSTALL'
    STREAM = 'STREAM'
    TOPOLOGY_LLDP = 'TOPOLOGY_LLDP'
    TOPOLOGY_PTP = 'TOPOLOGY_PTP'
    TOPOLOGY_SYNCE = 'TOPOLOGY_SYNCE'
    TOPOLOGY_MPLS = 'TOPOLOGY_MPLS'
    PERFORMANCE = 'PERFORMANCE'


class ConnectionType(ENUM):
    NETCONF = 'NETCONF'
    GNMI = 'GNMI'
    CLI = 'CLI'
    SNMP = 'SNMP'


class Connection(Interface):
    edges: typing.Optional[Edge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')


class Edge(Interface):
    cursor: typing.Optional[Boolean] = Field(default=None)
    node: typing.Optional[Node] = Field(default=None)


class Node(Interface):
    name: typing.Optional[Boolean] = Field(default=None)


class BlueprintNodeInput(Input):
    blueprint_type: BlueprintType = Field(alias='blueprintType')
    connection_type: ConnectionType = Field(alias='connectionType')
    model_pattern: typing.Optional[String] = Field(default=None, alias='modelPattern')
    name: String
    template: String
    vendor_pattern: typing.Optional[String] = Field(default=None, alias='vendorPattern')
    version_pattern: typing.Optional[String] = Field(default=None, alias='versionPattern')


class BlueprintConnection(Payload):
    edges: typing.Optional[BlueprintEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')


class BlueprintConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[BlueprintEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')


class BlueprintEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[BlueprintNode] = Field(default=None)


class BlueprintEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[BlueprintNodePayload] = Field(default=None)


class BlueprintMetadata(Payload):
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')


class BlueprintMetadataPayload(BaseModel):
    created_at: typing.Optional[typing.Optional[DateTime]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[DateTime]] = Field(default=None, alias='updatedAt')


class BlueprintNode(Payload):
    blueprint_type: typing.Optional[Boolean] = Field(default=False, alias='blueprintType')
    connection_type: typing.Optional[Boolean] = Field(default=False, alias='connectionType')
    model_pattern: typing.Optional[Boolean] = Field(default=False, alias='modelPattern')
    name: typing.Optional[Boolean] = Field(default=False)
    template: typing.Optional[Boolean] = Field(default=False)
    vendor_pattern: typing.Optional[Boolean] = Field(default=False, alias='vendorPattern')
    version_pattern: typing.Optional[Boolean] = Field(default=False, alias='versionPattern')


class BlueprintNodePayload(BaseModel):
    blueprint_type: typing.Optional[typing.Optional[BlueprintType]] = Field(default=None, alias='blueprintType')
    connection_type: typing.Optional[typing.Optional[ConnectionType]] = Field(default=None, alias='connectionType')
    model_pattern: typing.Optional[typing.Optional[String]] = Field(default=None, alias='modelPattern')
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    template: typing.Optional[typing.Optional[String]] = Field(default=None)
    vendor_pattern: typing.Optional[typing.Optional[String]] = Field(default=None, alias='vendorPattern')
    version_pattern: typing.Optional[typing.Optional[String]] = Field(default=None, alias='versionPattern')


class BlueprintOutput(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    metadata: typing.Optional[BlueprintMetadata] = Field(default=None)
    node: typing.Optional[BlueprintNode] = Field(default=None)


class BlueprintOutputPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    metadata: typing.Optional[BlueprintMetadataPayload] = Field(default=None)
    node: typing.Optional[BlueprintNodePayload] = Field(default=None)


class CreateBlueprintMutation(Mutation):
    _name: str = PrivateAttr('createBlueprint')
    node: BlueprintNodeInput = Field(json_schema_extra={'type': 'BlueprintNodeInput!'})
    payload: BlueprintOutput


class DeleteBlueprintMutation(Mutation):
    _name: str = PrivateAttr('deleteBlueprint')
    id: ID = Field(json_schema_extra={'type': 'ID!'})
    payload: BlueprintOutput


class UpdateBlueprintMutation(Mutation):
    _name: str = PrivateAttr('updateBlueprint')
    id: ID = Field(json_schema_extra={'type': 'ID!'})
    node: BlueprintNodeInput = Field(json_schema_extra={'type': 'BlueprintNodeInput!'})
    payload: BlueprintOutput


class CreateBlueprintMutationResponse(BaseModel):
    data: typing.Optional[CreateBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateBlueprintData(BaseModel):
    create_blueprint: BlueprintOutputPayload = Field(alias='createBlueprint')


class DeleteBlueprintMutationResponse(BaseModel):
    data: typing.Optional[DeleteBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteBlueprintData(BaseModel):
    delete_blueprint: BlueprintOutputPayload = Field(alias='deleteBlueprint')


class UpdateBlueprintMutationResponse(BaseModel):
    data: typing.Optional[UpdateBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateBlueprintData(BaseModel):
    update_blueprint: BlueprintOutputPayload = Field(alias='updateBlueprint')


class PageInfo(Payload):
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')


class PageInfoPayload(BaseModel):
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')


class BlueprintsQuery(Query):
    _name: str = PrivateAttr('blueprints')
    connection_type: typing.Optional[ConnectionType] = Field(default=None, alias='connectionType', json_schema_extra={'type': 'ConnectionType'})
    blueprint_type: typing.Optional[BlueprintType] = Field(default=None, alias='blueprintType', json_schema_extra={'type': 'BlueprintType'})
    vendor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    model: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    version: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    template_variables: typing.Optional[JSON] = Field(default=None, alias='templateVariables', json_schema_extra={'type': 'JSON'})
    payload: BlueprintConnection


class BlueprintsQueryResponse(BaseModel):
    data: typing.Optional[BlueprintsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class BlueprintsData(BaseModel):
    blueprints: BlueprintConnectionPayload


Connection.model_rebuild()
Edge.model_rebuild()
Node.model_rebuild()
BlueprintNodeInput.model_rebuild()
BlueprintConnection.model_rebuild()
BlueprintConnectionPayload.model_rebuild()
BlueprintEdge.model_rebuild()
BlueprintEdgePayload.model_rebuild()
BlueprintMetadata.model_rebuild()
BlueprintMetadataPayload.model_rebuild()
BlueprintNode.model_rebuild()
BlueprintNodePayload.model_rebuild()
BlueprintOutput.model_rebuild()
BlueprintOutputPayload.model_rebuild()
CreateBlueprintMutation.model_rebuild()
DeleteBlueprintMutation.model_rebuild()
UpdateBlueprintMutation.model_rebuild()
CreateBlueprintMutationResponse.model_rebuild()
CreateBlueprintData.model_rebuild()
DeleteBlueprintMutationResponse.model_rebuild()
DeleteBlueprintData.model_rebuild()
UpdateBlueprintMutationResponse.model_rebuild()
UpdateBlueprintData.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
BlueprintsQuery.model_rebuild()
BlueprintsQueryResponse.model_rebuild()
BlueprintsData.model_rebuild()

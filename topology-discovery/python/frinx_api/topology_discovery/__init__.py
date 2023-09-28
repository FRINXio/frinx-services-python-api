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

String: typing.TypeAlias = str
Float: typing.TypeAlias = float
JSON: typing.TypeAlias = typing.Any
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Boolean: typing.TypeAlias = bool


class CoordinatesNodeType(ENUM):
    device = 'device'
    network = 'network'


class TopologyDiffCollectionTypes(ENUM):
    net = 'net'
    phy = 'phy'


class NodeStatus(ENUM):
    ok = 'ok'
    unknown = 'unknown'


class NetRoutingPathOutputCollections(ENUM):
    NetDevice = 'NetDevice'
    NetInterface = 'NetInterface'


class __TypeKind(ENUM):
    SCALAR = 'SCALAR'
    OBJECT = 'OBJECT'
    INTERFACE = 'INTERFACE'
    UNION = 'UNION'
    ENUM = 'ENUM'
    INPUT_OBJECT = 'INPUT_OBJECT'
    LIST = 'LIST'
    NON_NULL = 'NON_NULL'


class __DirectiveLocation(ENUM):
    QUERY = 'QUERY'
    MUTATION = 'MUTATION'
    SUBSCRIPTION = 'SUBSCRIPTION'
    FIELD = 'FIELD'
    FRAGMENT_DEFINITION = 'FRAGMENT_DEFINITION'
    FRAGMENT_SPREAD = 'FRAGMENT_SPREAD'
    INLINE_FRAGMENT = 'INLINE_FRAGMENT'
    VARIABLE_DEFINITION = 'VARIABLE_DEFINITION'
    SCHEMA = 'SCHEMA'
    SCALAR = 'SCALAR'
    OBJECT = 'OBJECT'
    FIELD_DEFINITION = 'FIELD_DEFINITION'
    ARGUMENT_DEFINITION = 'ARGUMENT_DEFINITION'
    INTERFACE = 'INTERFACE'
    UNION = 'UNION'
    ENUM = 'ENUM'
    ENUM_VALUE = 'ENUM_VALUE'
    INPUT_OBJECT = 'INPUT_OBJECT'
    INPUT_FIELD_DEFINITION = 'INPUT_FIELD_DEFINITION'


class Node(Interface):
    id: typing.Optional[Boolean]


class CoordinatesInput(Input):
    node_type: CoordinatesNodeType
    node_name: String
    x: Float
    y: Float


class NetDeviceFilter(Input):
    ospf_area_id: typing.Optional[String] = Field(alias='ospfAreaId')
    router_id: typing.Optional[String] = Field(alias='routerId')


class NetInterfaceFilter(Input):
    ip_address: typing.Optional[String] = Field(alias='ipAddress')


class NetNetworkFilter(Input):
    subnet: typing.Optional[String]
    ospf_route_type: typing.Optional[Int] = Field(alias='ospfRouteType')


class PhyDeviceFilter(Input):
    label: typing.Optional[String]
    name: typing.Optional[String]


class PhyInterfaceFilter(Input):
    status: typing.Optional[String]
    name: typing.Optional[String]


class CreateBackupResponse(Payload):
    db_name: typing.Optional[Boolean] = Field(response='String', default=False)


class CreateBackupResponsePayload(BaseModel):
    db_name: typing.Optional[typing.Optional[String]]


class DeleteBackupsResponse(Payload):
    deleted_backups: typing.Optional[Boolean] = Field(response='String', default=False)


class DeleteBackupsResponsePayload(BaseModel):
    deleted_backups: typing.Optional[typing.Optional[list[typing.Optional[String]]]]


class CoordinatesResponse(Payload):
    not_updated: typing.Optional[Boolean] = Field(response='String', default=False)
    updated: typing.Optional[Boolean] = Field(response='String', default=False)


class CoordinatesResponsePayload(BaseModel):
    not_updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]]
    updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]]


class TopologyResponse(Payload):
    diff_data: typing.Optional[Boolean] = Field(response='JSON', default=False)


class TopologyResponsePayload(BaseModel):
    diff_data: typing.Optional[typing.Optional[JSON]]


class CommonNodesResponse(Payload):
    common_nodes: typing.Optional[Boolean] = Field(response='String', default=False)


class CommonNodesResponsePayload(BaseModel):
    common_nodes: typing.Optional[typing.Optional[list[typing.Optional[String]]]]


class ProviderResponse(Payload):
    supported_devices: typing.Optional[Boolean] = Field(response='String', default=False)


class ProviderResponsePayload(BaseModel):
    supported_devices: typing.Optional[typing.Optional[list[typing.Optional[String]]]]


class SyncResponse(Payload):
    labels: typing.Optional[Boolean] = Field(response='String', default=False)
    loaded_devices: typing.Optional[Boolean] = Field(response='JSON', default=False)


class SyncResponsePayload(BaseModel):
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]]
    loaded_devices: typing.Optional[typing.Optional[JSON]]


class NodeQuery(Query):
    _name: str = Field('node', const=True)
    id: ID
    payload: Node


class PhyDevicesQuery(Query):
    _name: str = Field('phyDevices', const=True)
    filters: typing.Optional[PhyDeviceFilter]
    first: typing.Optional[Int]
    cursor: typing.Optional[String]
    payload: PhyDeviceConnection


class NetDevicesQuery(Query):
    _name: str = Field('netDevices', const=True)
    filters: typing.Optional[NetDeviceFilter]
    first: typing.Optional[Int]
    cursor: typing.Optional[String]
    payload: NetDeviceConnection


class NetRoutingPathsQuery(Query):
    _name: str = Field('netRoutingPaths', const=True)
    device_from: ID = Field(alias='deviceFrom')
    device_to: ID = Field(alias='deviceTo')
    output_collection: typing.Optional[NetRoutingPathOutputCollections] = Field(alias='outputCollection')
    payload: NetRoutingPathConnection


class BackupsQuery(Query):
    _name: str = Field('backups', const=True)


class TopologyDiffQuery(Query):
    _name: str = Field('topologyDiff', const=True)
    new_db: typing.Optional[String]
    old_db: typing.Optional[String]
    collection_type: TopologyDiffCollectionTypes
    payload: TopologyResponse


class PhyHasAndInterfacesQuery(Query):
    _name: str = Field('phyHasAndInterfaces', const=True)


class PhyLinksAndDevicesQuery(Query):
    _name: str = Field('phyLinksAndDevices', const=True)


class CommonNodesQuery(Query):
    _name: str = Field('commonNodes', const=True)
    selected_nodes: typing.Optional[list[String]]
    db_name: typing.Optional[String]
    payload: CommonNodesResponse


class ProvidersQuery(Query):
    _name: str = Field('providers', const=True)


class ProviderQuery(Query):
    _name: str = Field('provider', const=True)
    name: String
    payload: ProviderResponse


class NodeResponse(BaseModel):
    data: typing.Optional[NodeData]
    errors: typing.Optional[typing.Any]


class PhyDevicesResponse(BaseModel):
    data: typing.Optional[PhyDevicesData]
    errors: typing.Optional[typing.Any]


class PhyDevicesData(BaseModel):
    phy_devices: PhyDeviceConnectionPayload = Field(alias='phyDevices')


class NetDevicesResponse(BaseModel):
    data: typing.Optional[NetDevicesData]
    errors: typing.Optional[typing.Any]


class NetDevicesData(BaseModel):
    net_devices: NetDeviceConnectionPayload = Field(alias='netDevices')


class NetRoutingPathsResponse(BaseModel):
    data: typing.Optional[NetRoutingPathsData]
    errors: typing.Optional[typing.Any]


class NetRoutingPathsData(BaseModel):
    net_routing_paths: typing.Optional[NetRoutingPathConnectionPayload] = Field(alias='netRoutingPaths')


class TopologyDiffResponse(BaseModel):
    data: typing.Optional[TopologyDiffData]
    errors: typing.Optional[typing.Any]


class TopologyDiffData(BaseModel):
    topology_diff: TopologyResponsePayload = Field(alias='topologyDiff')


class CommonNodesResponse(BaseModel):
    data: typing.Optional[CommonNodesData]
    errors: typing.Optional[typing.Any]


class CommonNodesData(BaseModel):
    common_nodes: CommonNodesResponsePayload = Field(alias='commonNodes')


class ProviderResponse(BaseModel):
    data: typing.Optional[ProviderData]
    errors: typing.Optional[typing.Any]


class ProviderData(BaseModel):
    provider: ProviderResponsePayload


class CreateBackupMutation(Mutation):
    _name: str = Field('createBackup', const=True)


class DeleteBackupsMutation(Mutation):
    _name: str = Field('deleteBackups', const=True)
    delete_age: typing.Optional[Int]
    payload: DeleteBackupsResponse


class UpdateCoordinatesMutation(Mutation):
    _name: str = Field('updateCoordinates', const=True)
    coordinates_list: typing.Optional[list[CoordinatesInput]]
    payload: CoordinatesResponse


class UpdateNodeStatusMutation(Mutation):
    _name: str = Field('updateNodeStatus', const=True)
    device_name: String
    status: String
    interface_name: typing.Optional[String]
    payload: Boolean


class SyncMutation(Mutation):
    _name: str = Field('sync', const=True)
    provider_name: String
    devices: typing.Optional[list[String]]
    labels: typing.Optional[list[String]]
    payload: SyncResponse


class DeleteBackupsResponse(BaseModel):
    data: typing.Optional[DeleteBackupsData]
    errors: typing.Optional[typing.Any]


class DeleteBackupsData(BaseModel):
    delete_backups: DeleteBackupsResponsePayload = Field(alias='deleteBackups')


class UpdateCoordinatesResponse(BaseModel):
    data: typing.Optional[UpdateCoordinatesData]
    errors: typing.Optional[typing.Any]


class UpdateCoordinatesData(BaseModel):
    update_coordinates: CoordinatesResponsePayload = Field(alias='updateCoordinates')


class UpdateNodeStatusResponse(BaseModel):
    data: typing.Optional[UpdateNodeStatusData]
    errors: typing.Optional[typing.Any]


class UpdateNodeStatusData(BaseModel):
    update_node_status: typing.Optional[JSON] = Field(alias='updateNodeStatus')


class SyncResponse(BaseModel):
    data: typing.Optional[SyncData]
    errors: typing.Optional[typing.Any]


class SyncData(BaseModel):
    sync: SyncResponsePayload


class Coordinates(Payload):
    x: typing.Optional[Boolean] = Field(response='Float', default=False)
    y: typing.Optional[Boolean] = Field(response='Float', default=False)


class CoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]]
    y: typing.Optional[typing.Optional[Float]]


class NetDevice(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    router_id: typing.Optional[Boolean] = Field(response='String', alias='routerId', default=False)
    ospf_area_id: typing.Optional[Boolean] = Field(response='String', alias='ospfAreaId', default=False)
    phy_device: typing.Optional[PhyDevice] = Field(response='PhyDevice', alias='phyDevice')
    net_networks: typing.Optional[NetNetworkConnection] = Field(response='NetNetworkConnection', alias='netNetworks')
    net_interfaces: typing.Optional[NetInterfaceConnection] = Field(response='NetInterfaceConnection', alias='netInterfaces')


class NetDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]]
    router_id: typing.Optional[typing.Optional[String]] = Field(alias='routerId')
    ospf_area_id: typing.Optional[typing.Optional[String]] = Field(alias='ospfAreaId')
    phy_device: typing.Optional[PhyDevicePayload] = Field(alias='phyDevice')
    net_networks: typing.Optional[NetNetworkConnectionPayload] = Field(alias='netNetworks')
    net_interfaces: typing.Optional[NetInterfaceConnectionPayload] = Field(alias='netInterfaces')


class NetDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[NetDevice] = Field(response='NetDevice')


class NetDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[NetDevicePayload]


class NetDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetDeviceEdge] = Field(response='NetDeviceEdge')


class NetDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetDeviceEdgePayload]]]


class NetInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    ip_address: typing.Optional[Boolean] = Field(response='String', alias='ipAddress', default=False)
    net_device: typing.Optional[NetDevice] = Field(response='NetDevice', alias='netDevice')
    igp_metric: typing.Optional[Boolean] = Field(response='Int', default=False)
    net_link: typing.Optional[NetInterface] = Field(response='NetInterface', alias='netLink')


class NetInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]]
    ip_address: typing.Optional[typing.Optional[String]] = Field(alias='ipAddress')
    net_device: typing.Optional[NetDevicePayload] = Field(alias='netDevice')
    igp_metric: typing.Optional[typing.Optional[Int]]
    net_link: typing.Optional[NetInterfacePayload] = Field(alias='netLink')


class NetInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[NetInterface] = Field(response='NetInterface')


class NetInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[NetInterfacePayload]


class NetInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetInterfaceEdge] = Field(response='NetInterfaceEdge')


class NetInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetInterfaceEdgePayload]]]


class NetNetwork(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    subnet: typing.Optional[Boolean] = Field(response='String', default=False)
    ospf_route_type: typing.Optional[Boolean] = Field(response='Int', alias='ospfRouteType', default=False)
    coordinates: typing.Optional[Coordinates] = Field(response='Coordinates')


class NetNetworkPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]]
    subnet: typing.Optional[typing.Optional[String]]
    ospf_route_type: typing.Optional[typing.Optional[Int]] = Field(alias='ospfRouteType')
    coordinates: typing.Optional[CoordinatesPayload]


class NetNetworkEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[NetNetwork] = Field(response='NetNetwork')


class NetNetworkEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[NetNetworkPayload]


class NetNetworkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetNetworkEdge] = Field(response='NetNetworkEdge')


class NetNetworkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetNetworkEdgePayload]]]


class NodeInfo(Payload):
    node: typing.Optional[Boolean] = Field(response='ID', default=False)
    weight: typing.Optional[Boolean] = Field(response='Int', default=False)


class NodeInfoPayload(BaseModel):
    node: typing.Optional[typing.Optional[ID]]
    weight: typing.Optional[typing.Optional[Int]]


class RoutingPath(Payload):
    nodes: typing.Optional[NodeInfo] = Field(response='NodeInfo')
    weight: typing.Optional[Boolean] = Field(response='Int', default=False)


class RoutingPathPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[NodeInfoPayload]]]
    weight: typing.Optional[typing.Optional[Int]]


class NetRoutingPathConnection(Payload):
    edges: typing.Optional[RoutingPath] = Field(response='RoutingPath')


class NetRoutingPathConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[RoutingPathPayload]]]


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=False)
    end_cursor: typing.Optional[Boolean] = Field(response='String', alias='endCursor', default=False)


class PageInfoPayload(BaseModel):
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(alias='hasNextPage')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(alias='endCursor')


class PhyDevice(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    router_id: typing.Optional[Boolean] = Field(response='String', alias='routerId', default=False)
    coordinates: typing.Optional[Coordinates] = Field(response='Coordinates')
    details: typing.Optional[PhyDeviceDetails] = Field(response='PhyDeviceDetails')
    status: typing.Optional[Boolean] = Field(response='NodeStatus', default=False)
    labels: typing.Optional[Boolean] = Field(response='String', default=False)
    phy_interfaces: typing.Optional[PhyInterfaceConnection] = Field(response='PhyInterfaceConnection', alias='phyInterfaces')
    net_device: typing.Optional[NetDevice] = Field(response='NetDevice', alias='netDevice')


class PhyDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]]
    name: typing.Optional[typing.Optional[String]]
    router_id: typing.Optional[typing.Optional[String]] = Field(alias='routerId')
    coordinates: typing.Optional[CoordinatesPayload]
    details: typing.Optional[PhyDeviceDetailsPayload]
    status: typing.Optional[typing.Optional[NodeStatus]]
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]]
    phy_interfaces: typing.Optional[PhyInterfaceConnectionPayload] = Field(alias='phyInterfaces')
    net_device: typing.Optional[NetDevicePayload] = Field(alias='netDevice')


class PhyDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[PhyDevice] = Field(response='PhyDevice')


class PhyDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[PhyDevicePayload]


class PhyDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[PhyDeviceEdge] = Field(response='PhyDeviceEdge')


class PhyDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PhyDeviceEdgePayload]]]


class PhyDeviceDetails(Payload):
    device_type: typing.Optional[Boolean] = Field(response='String', default=False)
    sw_version: typing.Optional[Boolean] = Field(response='String', default=False)


class PhyDeviceDetailsPayload(BaseModel):
    device_type: typing.Optional[typing.Optional[String]]
    sw_version: typing.Optional[typing.Optional[String]]


class PhyHasAndInterfacesResponse(Payload):
    phy_has_and_interfaces_data: typing.Optional[Boolean] = Field(response='JSON', default=False)


class PhyHasAndInterfacesResponsePayload(BaseModel):
    phy_has_and_interfaces_data: typing.Optional[typing.Optional[JSON]]


class PhyLinksAndDevicesResponse(Payload):
    phy_links_and_devices_data: typing.Optional[Boolean] = Field(response='JSON', default=False)


class PhyLinksAndDevicesResponsePayload(BaseModel):
    phy_links_and_devices_data: typing.Optional[typing.Optional[JSON]]


class PhyInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=False)
    id_link: typing.Optional[Boolean] = Field(response='ID', alias='idLink', default=False)
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    status: typing.Optional[Boolean] = Field(response='String', default=False)
    phy_device: typing.Optional[PhyDevice] = Field(response='PhyDevice', alias='phyDevice')
    phy_link: typing.Optional[PhyInterface] = Field(response='PhyInterface', alias='phyLink')


class PhyInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]]
    id_link: typing.Optional[typing.Optional[ID]] = Field(alias='idLink')
    name: typing.Optional[typing.Optional[String]]
    status: typing.Optional[typing.Optional[String]]
    phy_device: typing.Optional[PhyDevicePayload] = Field(alias='phyDevice')
    phy_link: typing.Optional[PhyInterfacePayload] = Field(alias='phyLink')


class PhyInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=False)
    node: typing.Optional[PhyInterface] = Field(response='PhyInterface')


class PhyInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]]
    node: typing.Optional[PhyInterfacePayload]


class PhyInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[PhyInterfaceEdge] = Field(response='PhyInterfaceEdge')


class PhyInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PhyInterfaceEdgePayload]]]


class __Schema(Payload):
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    types: typing.Optional[__Type] = Field(response='__Type')
    query_type: typing.Optional[__Type] = Field(response='__Type', alias='queryType')
    mutation_type: typing.Optional[__Type] = Field(response='__Type', alias='mutationType')
    subscription_type: typing.Optional[__Type] = Field(response='__Type', alias='subscriptionType')
    directives: typing.Optional[__Directive] = Field(response='__Directive')


class __SchemaPayload(BaseModel):
    description: typing.Optional[typing.Optional[String]]
    types: typing.Optional[typing.Optional[list[__TypePayload]]]
    query_type: typing.Optional[__TypePayload] = Field(alias='queryType')
    mutation_type: typing.Optional[__TypePayload] = Field(alias='mutationType')
    subscription_type: typing.Optional[__TypePayload] = Field(alias='subscriptionType')
    directives: typing.Optional[typing.Optional[list[__DirectivePayload]]]


class __Type(Payload):
    kind: typing.Optional[Boolean] = Field(response='__TypeKind', default=False)
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    specified_by_url: typing.Optional[Boolean] = Field(response='String', alias='specifiedByURL', default=False)
    fields: typing.Optional[__Field] = Field(response='__Field')
    interfaces: typing.Optional[__Type] = Field(response='__Type')
    possible_types: typing.Optional[__Type] = Field(response='__Type', alias='possibleTypes')
    enum_values: typing.Optional[__EnumValue] = Field(response='__EnumValue', alias='enumValues')
    input_fields: typing.Optional[__InputValue] = Field(response='__InputValue', alias='inputFields')
    of_type: typing.Optional[__Type] = Field(response='__Type', alias='ofType')


class __TypePayload(BaseModel):
    kind: typing.Optional[typing.Optional[__TypeKind]]
    name: typing.Optional[typing.Optional[String]]
    description: typing.Optional[typing.Optional[String]]
    specified_by_url: typing.Optional[typing.Optional[String]] = Field(alias='specifiedByURL')
    fields: typing.Optional[typing.Optional[list[__FieldPayload]]]
    interfaces: typing.Optional[typing.Optional[list[__TypePayload]]]
    possible_types: typing.Optional[typing.Optional[list[__TypePayload]]] = Field(alias='possibleTypes')
    enum_values: typing.Optional[typing.Optional[list[__EnumValuePayload]]] = Field(alias='enumValues')
    input_fields: typing.Optional[typing.Optional[list[__InputValuePayload]]] = Field(alias='inputFields')
    of_type: typing.Optional[__TypePayload] = Field(alias='ofType')


class __Field(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    args: typing.Optional[__InputValue] = Field(response='__InputValue')
    type: typing.Optional[__Type] = Field(response='__Type')
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=False)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=False)


class __FieldPayload(BaseModel):
    name: typing.Optional[typing.Optional[String]]
    description: typing.Optional[typing.Optional[String]]
    args: typing.Optional[typing.Optional[list[__InputValuePayload]]]
    type: typing.Optional[__TypePayload]
    is_deprecated: typing.Optional[typing.Optional[Boolean]] = Field(alias='isDeprecated')
    deprecation_reason: typing.Optional[typing.Optional[String]] = Field(alias='deprecationReason')


class __InputValue(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    type: typing.Optional[__Type] = Field(response='__Type')
    default_value: typing.Optional[Boolean] = Field(response='String', alias='defaultValue', default=False)
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=False)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=False)


class __InputValuePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]]
    description: typing.Optional[typing.Optional[String]]
    type: typing.Optional[__TypePayload]
    default_value: typing.Optional[typing.Optional[String]] = Field(alias='defaultValue')
    is_deprecated: typing.Optional[typing.Optional[Boolean]] = Field(alias='isDeprecated')
    deprecation_reason: typing.Optional[typing.Optional[String]] = Field(alias='deprecationReason')


class __EnumValue(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=False)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=False)


class __EnumValuePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]]
    description: typing.Optional[typing.Optional[String]]
    is_deprecated: typing.Optional[typing.Optional[Boolean]] = Field(alias='isDeprecated')
    deprecation_reason: typing.Optional[typing.Optional[String]] = Field(alias='deprecationReason')


class __Directive(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=False)
    description: typing.Optional[Boolean] = Field(response='String', default=False)
    is_repeatable: typing.Optional[Boolean] = Field(response='Boolean', alias='isRepeatable', default=False)
    locations: typing.Optional[Boolean] = Field(response='__DirectiveLocation', default=False)
    args: typing.Optional[__InputValue] = Field(response='__InputValue')


class __DirectivePayload(BaseModel):
    name: typing.Optional[typing.Optional[String]]
    description: typing.Optional[typing.Optional[String]]
    is_repeatable: typing.Optional[typing.Optional[Boolean]] = Field(alias='isRepeatable')
    locations: typing.Optional[typing.Optional[list[typing.Optional[__DirectiveLocation]]]]
    args: typing.Optional[typing.Optional[list[__InputValuePayload]]]


Node.update_forward_refs()
CoordinatesInput.update_forward_refs()
NetDeviceFilter.update_forward_refs()
NetInterfaceFilter.update_forward_refs()
NetNetworkFilter.update_forward_refs()
PhyDeviceFilter.update_forward_refs()
PhyInterfaceFilter.update_forward_refs()
CreateBackupResponse.update_forward_refs()
CreateBackupResponsePayload.update_forward_refs()
DeleteBackupsResponse.update_forward_refs()
DeleteBackupsResponsePayload.update_forward_refs()
CoordinatesResponse.update_forward_refs()
CoordinatesResponsePayload.update_forward_refs()
TopologyResponse.update_forward_refs()
TopologyResponsePayload.update_forward_refs()
CommonNodesResponse.update_forward_refs()
CommonNodesResponsePayload.update_forward_refs()
ProviderResponse.update_forward_refs()
ProviderResponsePayload.update_forward_refs()
SyncResponse.update_forward_refs()
SyncResponsePayload.update_forward_refs()
NodeQuery.update_forward_refs()
PhyDevicesQuery.update_forward_refs()
NetDevicesQuery.update_forward_refs()
NetRoutingPathsQuery.update_forward_refs()
BackupsQuery.update_forward_refs()
TopologyDiffQuery.update_forward_refs()
PhyHasAndInterfacesQuery.update_forward_refs()
PhyLinksAndDevicesQuery.update_forward_refs()
CommonNodesQuery.update_forward_refs()
ProvidersQuery.update_forward_refs()
ProviderQuery.update_forward_refs()
NodeResponse.update_forward_refs()
PhyDevicesResponse.update_forward_refs()
PhyDevicesData.update_forward_refs()
NetDevicesResponse.update_forward_refs()
NetDevicesData.update_forward_refs()
NetRoutingPathsResponse.update_forward_refs()
NetRoutingPathsData.update_forward_refs()
TopologyDiffResponse.update_forward_refs()
TopologyDiffData.update_forward_refs()
CommonNodesResponse.update_forward_refs()
CommonNodesData.update_forward_refs()
ProviderResponse.update_forward_refs()
ProviderData.update_forward_refs()
CreateBackupMutation.update_forward_refs()
DeleteBackupsMutation.update_forward_refs()
UpdateCoordinatesMutation.update_forward_refs()
UpdateNodeStatusMutation.update_forward_refs()
SyncMutation.update_forward_refs()
DeleteBackupsResponse.update_forward_refs()
DeleteBackupsData.update_forward_refs()
UpdateCoordinatesResponse.update_forward_refs()
UpdateCoordinatesData.update_forward_refs()
UpdateNodeStatusResponse.update_forward_refs()
UpdateNodeStatusData.update_forward_refs()
SyncResponse.update_forward_refs()
SyncData.update_forward_refs()
Coordinates.update_forward_refs()
CoordinatesPayload.update_forward_refs()
NetDevice.update_forward_refs()
NetDevicePayload.update_forward_refs()
NetDeviceEdge.update_forward_refs()
NetDeviceEdgePayload.update_forward_refs()
NetDeviceConnection.update_forward_refs()
NetDeviceConnectionPayload.update_forward_refs()
NetInterface.update_forward_refs()
NetInterfacePayload.update_forward_refs()
NetInterfaceEdge.update_forward_refs()
NetInterfaceEdgePayload.update_forward_refs()
NetInterfaceConnection.update_forward_refs()
NetInterfaceConnectionPayload.update_forward_refs()
NetNetwork.update_forward_refs()
NetNetworkPayload.update_forward_refs()
NetNetworkEdge.update_forward_refs()
NetNetworkEdgePayload.update_forward_refs()
NetNetworkConnection.update_forward_refs()
NetNetworkConnectionPayload.update_forward_refs()
NodeInfo.update_forward_refs()
NodeInfoPayload.update_forward_refs()
RoutingPath.update_forward_refs()
RoutingPathPayload.update_forward_refs()
NetRoutingPathConnection.update_forward_refs()
NetRoutingPathConnectionPayload.update_forward_refs()
PageInfo.update_forward_refs()
PageInfoPayload.update_forward_refs()
PhyDevice.update_forward_refs()
PhyDevicePayload.update_forward_refs()
PhyDeviceEdge.update_forward_refs()
PhyDeviceEdgePayload.update_forward_refs()
PhyDeviceConnection.update_forward_refs()
PhyDeviceConnectionPayload.update_forward_refs()
PhyDeviceDetails.update_forward_refs()
PhyDeviceDetailsPayload.update_forward_refs()
PhyHasAndInterfacesResponse.update_forward_refs()
PhyHasAndInterfacesResponsePayload.update_forward_refs()
PhyLinksAndDevicesResponse.update_forward_refs()
PhyLinksAndDevicesResponsePayload.update_forward_refs()
PhyInterface.update_forward_refs()
PhyInterfacePayload.update_forward_refs()
PhyInterfaceEdge.update_forward_refs()
PhyInterfaceEdgePayload.update_forward_refs()
PhyInterfaceConnection.update_forward_refs()
PhyInterfaceConnectionPayload.update_forward_refs()
__Schema.update_forward_refs()
__SchemaPayload.update_forward_refs()
__Type.update_forward_refs()
__TypePayload.update_forward_refs()
__Field.update_forward_refs()
__FieldPayload.update_forward_refs()
__InputValue.update_forward_refs()
__InputValuePayload.update_forward_refs()
__EnumValue.update_forward_refs()
__EnumValuePayload.update_forward_refs()
__Directive.update_forward_refs()
__DirectivePayload.update_forward_refs()

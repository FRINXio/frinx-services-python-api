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


class Node(Interface):
    id: typing.Optional[Boolean] = Field(default=None)


class CoordinatesInput(Input):
    node_type: CoordinatesNodeType
    node_name: String
    x: Float
    y: Float


class NetDeviceFilter(Input):
    ospf_area_id: typing.Optional[String] = Field(default=None, alias='ospfAreaId')
    router_id: typing.Optional[String] = Field(default=None, alias='routerId')


class NetInterfaceFilter(Input):
    ip_address: typing.Optional[String] = Field(default=None, alias='ipAddress')


class NetNetworkFilter(Input):
    subnet: typing.Optional[String] = Field(default=None)
    ospf_route_type: typing.Optional[Int] = Field(default=None, alias='ospfRouteType')


class PhyDeviceFilter(Input):
    label: typing.Optional[String] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)


class PhyInterfaceFilter(Input):
    status: typing.Optional[String] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)


class CreateBackupResponse(Payload):
    db_name: typing.Optional[Boolean] = Field(default=False)


class CreateBackupResponsePayload(BaseModel):
    db_name: typing.Optional[typing.Optional[String]] = Field(default=None)


class DeleteBackupsResponse(Payload):
    deleted_backups: typing.Optional[Boolean] = Field(default=False)


class DeleteBackupsResponsePayload(BaseModel):
    deleted_backups: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)


class CoordinatesResponse(Payload):
    not_updated: typing.Optional[Boolean] = Field(default=False)
    updated: typing.Optional[Boolean] = Field(default=False)


class CoordinatesResponsePayload(BaseModel):
    not_updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)


class TopologyResponse(Payload):
    diff_data: typing.Optional[Boolean] = Field(default=False)


class TopologyResponsePayload(BaseModel):
    diff_data: typing.Optional[typing.Optional[JSON]] = Field(default=None)


class CommonNodesResponse(Payload):
    common_nodes: typing.Optional[Boolean] = Field(default=False)


class CommonNodesResponsePayload(BaseModel):
    common_nodes: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)


class ProviderResponse(Payload):
    supported_devices: typing.Optional[Boolean] = Field(default=False)


class ProviderResponsePayload(BaseModel):
    supported_devices: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)


class SyncResponse(Payload):
    labels: typing.Optional[Boolean] = Field(default=False)
    loaded_devices: typing.Optional[Boolean] = Field(default=False)


class SyncResponsePayload(BaseModel):
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    loaded_devices: typing.Optional[typing.Optional[JSON]] = Field(default=None)


class NodeQuery(Query):
    _name: str = PrivateAttr('node')
    id: ID = Field(json_schema_extra={'type': 'ID!'})
    payload: Node


class PhyDevicesQuery(Query):
    _name: str = PrivateAttr('phyDevices')
    filters: typing.Optional[PhyDeviceFilter] = Field(default=None, json_schema_extra={'type': 'PhyDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: PhyDeviceConnection


class NetDevicesQuery(Query):
    _name: str = PrivateAttr('netDevices')
    filters: typing.Optional[NetDeviceFilter] = Field(default=None, json_schema_extra={'type': 'NetDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: NetDeviceConnection


class NetRoutingPathsQuery(Query):
    _name: str = PrivateAttr('netRoutingPaths')
    device_from: ID = Field(alias='deviceFrom', json_schema_extra={'type': 'ID!'})
    device_to: ID = Field(alias='deviceTo', json_schema_extra={'type': 'ID!'})
    output_collection: typing.Optional[NetRoutingPathOutputCollections] = Field(default=None, alias='outputCollection', json_schema_extra={'type': 'NetRoutingPathOutputCollections'})
    payload: NetRoutingPathConnection


class BackupsQuery(Query):
    _name: str = PrivateAttr('backups')


class TopologyDiffQuery(Query):
    _name: str = PrivateAttr('topologyDiff')
    new_db: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    old_db: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    collection_type: TopologyDiffCollectionTypes = Field(json_schema_extra={'type': 'TopologyDiffCollectionTypes!'})
    payload: TopologyResponse


class PhyHasAndInterfacesQuery(Query):
    _name: str = PrivateAttr('phyHasAndInterfaces')


class PhyLinksAndDevicesQuery(Query):
    _name: str = PrivateAttr('phyLinksAndDevices')


class CommonNodesQuery(Query):
    _name: str = PrivateAttr('commonNodes')
    selected_nodes: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    db_name: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: CommonNodesResponse


class ProvidersQuery(Query):
    _name: str = PrivateAttr('providers')


class ProviderQuery(Query):
    _name: str = PrivateAttr('provider')
    name: String = Field(json_schema_extra={'type': 'String!'})
    payload: ProviderResponse


class NodeQueryResponse(BaseModel):
    data: typing.Optional[Node] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PhyDevicesQueryResponse(BaseModel):
    data: typing.Optional[PhyDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PhyDevicesData(BaseModel):
    phy_devices: PhyDeviceConnectionPayload = Field(alias='phyDevices')


class NetDevicesQueryResponse(BaseModel):
    data: typing.Optional[NetDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class NetDevicesData(BaseModel):
    net_devices: NetDeviceConnectionPayload = Field(alias='netDevices')


class NetRoutingPathsQueryResponse(BaseModel):
    data: typing.Optional[NetRoutingPathsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class NetRoutingPathsData(BaseModel):
    net_routing_paths: typing.Optional[NetRoutingPathConnectionPayload] = Field(alias='netRoutingPaths')


class TopologyDiffQueryResponse(BaseModel):
    data: typing.Optional[TopologyDiffData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TopologyDiffData(BaseModel):
    topology_diff: TopologyResponsePayload = Field(alias='topologyDiff')


class CommonNodesQueryResponse(BaseModel):
    data: typing.Optional[CommonNodesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CommonNodesData(BaseModel):
    common_nodes: CommonNodesResponsePayload = Field(alias='commonNodes')


class ProviderQueryResponse(BaseModel):
    data: typing.Optional[ProviderData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ProviderData(BaseModel):
    provider: ProviderResponsePayload


class CreateBackupMutation(Mutation):
    _name: str = PrivateAttr('createBackup')


class DeleteBackupsMutation(Mutation):
    _name: str = PrivateAttr('deleteBackups')
    delete_age: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    payload: DeleteBackupsResponse


class UpdateCoordinatesMutation(Mutation):
    _name: str = PrivateAttr('updateCoordinates')
    coordinates_list: typing.Optional[list[CoordinatesInput]] = Field(default=None, json_schema_extra={'type': '[CoordinatesInput!]!'})
    payload: CoordinatesResponse


class UpdateNodeStatusMutation(Mutation):
    _name: str = PrivateAttr('updateNodeStatus')
    device_name: String = Field(json_schema_extra={'type': 'String!'})
    status: String = Field(json_schema_extra={'type': 'String!'})
    interface_name: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: Boolean


class SyncMutation(Mutation):
    _name: str = PrivateAttr('sync')
    provider_name: String = Field(json_schema_extra={'type': 'String!'})
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String]'})
    labels: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String]'})
    payload: SyncResponse


class DeleteBackupsMutationResponse(BaseModel):
    data: typing.Optional[DeleteBackupsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteBackupsData(BaseModel):
    delete_backups: DeleteBackupsResponsePayload = Field(alias='deleteBackups')


class UpdateCoordinatesMutationResponse(BaseModel):
    data: typing.Optional[UpdateCoordinatesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateCoordinatesData(BaseModel):
    update_coordinates: CoordinatesResponsePayload = Field(alias='updateCoordinates')


class UpdateNodeStatusMutationResponse(BaseModel):
    data: typing.Optional[UpdateNodeStatusData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateNodeStatusData(BaseModel):
    update_node_status: typing.Optional[JSON] = Field(alias='updateNodeStatus')


class SyncMutationResponse(BaseModel):
    data: typing.Optional[SyncData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SyncData(BaseModel):
    sync: SyncResponsePayload


class Coordinates(Payload):
    x: typing.Optional[Boolean] = Field(default=False)
    y: typing.Optional[Boolean] = Field(default=False)


class CoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]] = Field(default=None)
    y: typing.Optional[typing.Optional[Float]] = Field(default=None)


class NetDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    router_id: typing.Optional[Boolean] = Field(default=False, alias='routerId')
    ospf_area_id: typing.Optional[Boolean] = Field(default=False, alias='ospfAreaId')
    phy_device: typing.Optional[PhyDevice] = Field(default=None, alias='phyDevice')
    net_networks: typing.Optional[NetNetworkConnection] = Field(default=None, alias='netNetworks')
    net_interfaces: typing.Optional[NetInterfaceConnection] = Field(default=None, alias='netInterfaces')


class NetDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    router_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='routerId')
    ospf_area_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ospfAreaId')
    phy_device: typing.Optional[PhyDevicePayload] = Field(default=None, alias='phyDevice')
    net_networks: typing.Optional[NetNetworkConnectionPayload] = Field(default=None, alias='netNetworks')
    net_interfaces: typing.Optional[NetInterfaceConnectionPayload] = Field(default=None, alias='netInterfaces')


class NetDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[NetDevice] = Field(default=None)


class NetDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[NetDevicePayload] = Field(default=None)


class NetDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[NetDeviceEdge] = Field(default=None)


class NetDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetDeviceEdgePayload]]] = Field(default=None)


class NetInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    ip_address: typing.Optional[Boolean] = Field(default=False, alias='ipAddress')
    net_device: typing.Optional[NetDevice] = Field(default=None, alias='netDevice')
    igp_metric: typing.Optional[Boolean] = Field(default=False)
    net_link: typing.Optional[NetInterface] = Field(default=None, alias='netLink')


class NetInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    ip_address: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ipAddress')
    net_device: typing.Optional[NetDevicePayload] = Field(default=None, alias='netDevice')
    igp_metric: typing.Optional[typing.Optional[Int]] = Field(default=None)
    net_link: typing.Optional[NetInterfacePayload] = Field(default=None, alias='netLink')


class NetInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[NetInterface] = Field(default=None)


class NetInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[NetInterfacePayload] = Field(default=None)


class NetInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[NetInterfaceEdge] = Field(default=None)


class NetInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetInterfaceEdgePayload]]] = Field(default=None)


class NetNetwork(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    subnet: typing.Optional[Boolean] = Field(default=False)
    ospf_route_type: typing.Optional[Boolean] = Field(default=False, alias='ospfRouteType')
    coordinates: typing.Optional[Coordinates] = Field(default=None)


class NetNetworkPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    subnet: typing.Optional[typing.Optional[String]] = Field(default=None)
    ospf_route_type: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='ospfRouteType')
    coordinates: typing.Optional[CoordinatesPayload] = Field(default=None)


class NetNetworkEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[NetNetwork] = Field(default=None)


class NetNetworkEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[NetNetworkPayload] = Field(default=None)


class NetNetworkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[NetNetworkEdge] = Field(default=None)


class NetNetworkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetNetworkEdgePayload]]] = Field(default=None)


class NodeInfo(Payload):
    node: typing.Optional[Boolean] = Field(default=False)
    weight: typing.Optional[Boolean] = Field(default=False)


class NodeInfoPayload(BaseModel):
    node: typing.Optional[typing.Optional[ID]] = Field(default=None)
    weight: typing.Optional[typing.Optional[Int]] = Field(default=None)


class RoutingPath(Payload):
    nodes: typing.Optional[NodeInfo] = Field(default=None)
    weight: typing.Optional[Boolean] = Field(default=False)


class RoutingPathPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[NodeInfoPayload]]] = Field(default=None)
    weight: typing.Optional[typing.Optional[Int]] = Field(default=None)


class NetRoutingPathConnection(Payload):
    edges: typing.Optional[RoutingPath] = Field(default=None)


class NetRoutingPathConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[RoutingPathPayload]]] = Field(default=None)


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')


class PageInfoPayload(BaseModel):
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')


class PhyDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    router_id: typing.Optional[Boolean] = Field(default=False, alias='routerId')
    coordinates: typing.Optional[Coordinates] = Field(default=None)
    details: typing.Optional[PhyDeviceDetails] = Field(default=None)
    status: typing.Optional[Boolean] = Field(default=False)
    labels: typing.Optional[Boolean] = Field(default=False)
    phy_interfaces: typing.Optional[PhyInterfaceConnection] = Field(default=None, alias='phyInterfaces')
    net_device: typing.Optional[NetDevice] = Field(default=None, alias='netDevice')


class PhyDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    router_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='routerId')
    coordinates: typing.Optional[CoordinatesPayload] = Field(default=None)
    details: typing.Optional[PhyDeviceDetailsPayload] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    phy_interfaces: typing.Optional[PhyInterfaceConnectionPayload] = Field(default=None, alias='phyInterfaces')
    net_device: typing.Optional[NetDevicePayload] = Field(default=None, alias='netDevice')


class PhyDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PhyDevice] = Field(default=None)


class PhyDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PhyDevicePayload] = Field(default=None)


class PhyDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PhyDeviceEdge] = Field(default=None)


class PhyDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PhyDeviceEdgePayload]]] = Field(default=None)


class PhyDeviceDetails(Payload):
    device_type: typing.Optional[Boolean] = Field(default=False)
    sw_version: typing.Optional[Boolean] = Field(default=False)


class PhyDeviceDetailsPayload(BaseModel):
    device_type: typing.Optional[typing.Optional[String]] = Field(default=None)
    sw_version: typing.Optional[typing.Optional[String]] = Field(default=None)


class PhyHasAndInterfacesResponse(Payload):
    phy_has_and_interfaces_data: typing.Optional[Boolean] = Field(default=False)


class PhyHasAndInterfacesResponsePayload(BaseModel):
    phy_has_and_interfaces_data: typing.Optional[typing.Optional[JSON]] = Field(default=None)


class PhyLinksAndDevicesResponse(Payload):
    phy_links_and_devices_data: typing.Optional[Boolean] = Field(default=False)


class PhyLinksAndDevicesResponsePayload(BaseModel):
    phy_links_and_devices_data: typing.Optional[typing.Optional[JSON]] = Field(default=None)


class PhyInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    id_link: typing.Optional[Boolean] = Field(default=False, alias='idLink')
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    phy_device: typing.Optional[PhyDevice] = Field(default=None, alias='phyDevice')
    phy_link: typing.Optional[PhyInterface] = Field(default=None, alias='phyLink')


class PhyInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    id_link: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='idLink')
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[String]] = Field(default=None)
    phy_device: typing.Optional[PhyDevicePayload] = Field(default=None, alias='phyDevice')
    phy_link: typing.Optional[PhyInterfacePayload] = Field(default=None, alias='phyLink')


class PhyInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PhyInterface] = Field(default=None)


class PhyInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PhyInterfacePayload] = Field(default=None)


class PhyInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PhyInterfaceEdge] = Field(default=None)


class PhyInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PhyInterfaceEdgePayload]]] = Field(default=None)


Node.model_rebuild()
CoordinatesInput.model_rebuild()
NetDeviceFilter.model_rebuild()
NetInterfaceFilter.model_rebuild()
NetNetworkFilter.model_rebuild()
PhyDeviceFilter.model_rebuild()
PhyInterfaceFilter.model_rebuild()
CreateBackupResponse.model_rebuild()
CreateBackupResponsePayload.model_rebuild()
DeleteBackupsResponse.model_rebuild()
DeleteBackupsResponsePayload.model_rebuild()
CoordinatesResponse.model_rebuild()
CoordinatesResponsePayload.model_rebuild()
TopologyResponse.model_rebuild()
TopologyResponsePayload.model_rebuild()
CommonNodesResponse.model_rebuild()
CommonNodesResponsePayload.model_rebuild()
ProviderResponse.model_rebuild()
ProviderResponsePayload.model_rebuild()
SyncResponse.model_rebuild()
SyncResponsePayload.model_rebuild()
NodeQuery.model_rebuild()
PhyDevicesQuery.model_rebuild()
NetDevicesQuery.model_rebuild()
NetRoutingPathsQuery.model_rebuild()
BackupsQuery.model_rebuild()
TopologyDiffQuery.model_rebuild()
PhyHasAndInterfacesQuery.model_rebuild()
PhyLinksAndDevicesQuery.model_rebuild()
CommonNodesQuery.model_rebuild()
ProvidersQuery.model_rebuild()
ProviderQuery.model_rebuild()
NodeQueryResponse.model_rebuild()
PhyDevicesQueryResponse.model_rebuild()
PhyDevicesData.model_rebuild()
NetDevicesQueryResponse.model_rebuild()
NetDevicesData.model_rebuild()
NetRoutingPathsQueryResponse.model_rebuild()
NetRoutingPathsData.model_rebuild()
TopologyDiffQueryResponse.model_rebuild()
TopologyDiffData.model_rebuild()
CommonNodesQueryResponse.model_rebuild()
CommonNodesData.model_rebuild()
ProviderQueryResponse.model_rebuild()
ProviderData.model_rebuild()
CreateBackupMutation.model_rebuild()
DeleteBackupsMutation.model_rebuild()
UpdateCoordinatesMutation.model_rebuild()
UpdateNodeStatusMutation.model_rebuild()
SyncMutation.model_rebuild()
DeleteBackupsMutationResponse.model_rebuild()
DeleteBackupsData.model_rebuild()
UpdateCoordinatesMutationResponse.model_rebuild()
UpdateCoordinatesData.model_rebuild()
UpdateNodeStatusMutationResponse.model_rebuild()
UpdateNodeStatusData.model_rebuild()
SyncMutationResponse.model_rebuild()
SyncData.model_rebuild()
Coordinates.model_rebuild()
CoordinatesPayload.model_rebuild()
NetDevice.model_rebuild()
NetDevicePayload.model_rebuild()
NetDeviceEdge.model_rebuild()
NetDeviceEdgePayload.model_rebuild()
NetDeviceConnection.model_rebuild()
NetDeviceConnectionPayload.model_rebuild()
NetInterface.model_rebuild()
NetInterfacePayload.model_rebuild()
NetInterfaceEdge.model_rebuild()
NetInterfaceEdgePayload.model_rebuild()
NetInterfaceConnection.model_rebuild()
NetInterfaceConnectionPayload.model_rebuild()
NetNetwork.model_rebuild()
NetNetworkPayload.model_rebuild()
NetNetworkEdge.model_rebuild()
NetNetworkEdgePayload.model_rebuild()
NetNetworkConnection.model_rebuild()
NetNetworkConnectionPayload.model_rebuild()
NodeInfo.model_rebuild()
NodeInfoPayload.model_rebuild()
RoutingPath.model_rebuild()
RoutingPathPayload.model_rebuild()
NetRoutingPathConnection.model_rebuild()
NetRoutingPathConnectionPayload.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
PhyDevice.model_rebuild()
PhyDevicePayload.model_rebuild()
PhyDeviceEdge.model_rebuild()
PhyDeviceEdgePayload.model_rebuild()
PhyDeviceConnection.model_rebuild()
PhyDeviceConnectionPayload.model_rebuild()
PhyDeviceDetails.model_rebuild()
PhyDeviceDetailsPayload.model_rebuild()
PhyHasAndInterfacesResponse.model_rebuild()
PhyHasAndInterfacesResponsePayload.model_rebuild()
PhyLinksAndDevicesResponse.model_rebuild()
PhyLinksAndDevicesResponsePayload.model_rebuild()
PhyInterface.model_rebuild()
PhyInterfacePayload.model_rebuild()
PhyInterfaceEdge.model_rebuild()
PhyInterfaceEdgePayload.model_rebuild()
PhyInterfaceConnection.model_rebuild()
PhyInterfaceConnectionPayload.model_rebuild()

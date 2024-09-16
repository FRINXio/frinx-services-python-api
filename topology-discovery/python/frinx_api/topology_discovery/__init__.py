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
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Boolean: typing.TypeAlias = bool
JSON: typing.TypeAlias = typing.Any


class CoordinatesNodeType(ENUM):
    DEVICE = 'DEVICE'
    NETWORK = 'NETWORK'


class TopologyType(ENUM):
    PHYSICAL_TOPOLOGY = 'PHYSICAL_TOPOLOGY'
    PTP_TOPOLOGY = 'PTP_TOPOLOGY'
    ETH_TOPOLOGY = 'ETH_TOPOLOGY'
    NETWORK_TOPOLOGY = 'NETWORK_TOPOLOGY'
    MPLS_TOPOLOGY = 'MPLS_TOPOLOGY'


class GeometryType(ENUM):
    POINT = 'POINT'


class Signalisation(ENUM):
    RSVP = 'RSVP'
    LDP = 'LDP'


class MplsOperation(ENUM):
    SWAP = 'SWAP'
    PUSH = 'PUSH'
    POP = 'POP'
    NOOP = 'NOOP'


class NetRoutingPathOutputCollections(ENUM):
    NET_DEVICE = 'NET_DEVICE'
    NET_INTERFACE = 'NET_INTERFACE'


class NodeStatus(ENUM):
    OK = 'OK'
    UNKNOWN = 'UNKNOWN'


class PtpPathOutputCollections(ENUM):
    PTP_DEVICE = 'PTP_DEVICE'
    PTP_INTERFACE = 'PTP_INTERFACE'


class SyncePathOutputCollections(ENUM):
    SYNCE_DEVICE = 'SYNCE_DEVICE'
    SYNCE_INTERFACE = 'SYNCE_INTERFACE'


class Node(Interface):
    id: typing.Optional[Boolean] = Field(default=None)


class CoordinatesInput(Input):
    node_type: CoordinatesNodeType = Field(alias='nodeType')
    node_name: String = Field(alias='nodeName')
    x: Float
    y: Float


class DeviceMetadataFilter(Input):
    device_name: typing.Optional[String] = Field(default=None, alias='deviceName')
    topology_type: typing.Optional[TopologyType] = Field(default=None, alias='topologyType')
    polygon: typing.Optional[list[list[None]]] = Field(default=None)


class MplsDeviceFilter(Input):
    label: typing.Optional[String] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)


class MplsInterfaceFilter(Input):
    status: typing.Optional[NodeStatus] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)


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


class PtpDeviceFilter(Input):
    label: typing.Optional[String] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)
    clock_type: typing.Optional[String] = Field(default=None, alias='clockType')
    domain: typing.Optional[Int] = Field(default=None)
    ptp_profile: typing.Optional[String] = Field(default=None, alias='ptpProfile')
    clock_id: typing.Optional[String] = Field(default=None, alias='clockId')
    clock_class: typing.Optional[Int] = Field(default=None, alias='clockClass')
    clock_accuracy: typing.Optional[String] = Field(default=None, alias='clockAccuracy')
    clock_variance: typing.Optional[String] = Field(default=None, alias='clockVariance')
    time_recovery_status: typing.Optional[String] = Field(default=None, alias='timeRecoveryStatus')


class PtpInterfaceFilter(Input):
    status: typing.Optional[NodeStatus] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)
    ptp_status: typing.Optional[String] = Field(default=None, alias='ptpStatus')
    admin_oper_status: typing.Optional[String] = Field(default=None, alias='adminOperStatus')
    ptsf_unusable: typing.Optional[String] = Field(default=None, alias='ptsfUnusable')


class SynceDeviceFilter(Input):
    label: typing.Optional[String] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)
    selected_for_use: typing.Optional[String] = Field(default=None, alias='selectedForUse')


class SynceInterfaceFilter(Input):
    status: typing.Optional[NodeStatus] = Field(default=None)
    name: typing.Optional[String] = Field(default=None)
    synce_enabled: typing.Optional[Boolean] = Field(default=None, alias='synceEnabled')
    rx_quality_level: typing.Optional[String] = Field(default=None, alias='rxQualityLevel')
    qualified_for_use: typing.Optional[String] = Field(default=None, alias='qualifiedForUse')
    not_qualified_due_to: typing.Optional[String] = Field(default=None, alias='notQualifiedDueTo')
    not_selected_due_to: typing.Optional[String] = Field(default=None, alias='notSelectedDueTo')


class TopologyOverlayDeviceFilter(Input):
    name: typing.Optional[String] = Field(default=None)


class TopologyOverlayInterfaceFilter(Input):
    name: typing.Optional[String] = Field(default=None)


class CreateBackupResponse(Payload):
    db_name: typing.Optional[Boolean] = Field(default=False, alias='dbName')


class CreateBackupResponsePayload(BaseModel):
    db_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='dbName')


class DeleteBackupsResponse(Payload):
    deleted_backups: typing.Optional[Boolean] = Field(default=False, alias='deletedBackups')


class DeleteBackupsResponsePayload(BaseModel):
    deleted_backups: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='deletedBackups')


class CoordinatesResponse(Payload):
    not_installed: typing.Optional[Boolean] = Field(default=False, alias='notInstalled')
    installed: typing.Optional[InstalledDevices] = Field(default=None)


class CoordinatesResponsePayload(BaseModel):
    not_installed: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='notInstalled')
    installed: typing.Optional[InstalledDevicesPayload] = Field(default=None)


class InstalledDevices(Payload):
    not_updated: typing.Optional[Boolean] = Field(default=False, alias='notUpdated')
    updated: typing.Optional[Boolean] = Field(default=False)


class InstalledDevicesPayload(BaseModel):
    not_updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='notUpdated')
    updated: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)


class TopologyResponse(Payload):
    diff_data: typing.Optional[Boolean] = Field(default=False, alias='diffData')


class TopologyResponsePayload(BaseModel):
    diff_data: typing.Optional[typing.Optional[JSON]] = Field(default=None, alias='diffData')


class CommonNodesResponse(Payload):
    common_nodes: typing.Optional[Boolean] = Field(default=False, alias='commonNodes')


class CommonNodesResponsePayload(BaseModel):
    common_nodes: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='commonNodes')


class ProviderResponse(Payload):
    supported_devices: typing.Optional[Boolean] = Field(default=False, alias='supportedDevices')


class ProviderResponsePayload(BaseModel):
    supported_devices: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='supportedDevices')


class SyncResponse(Payload):
    labels: typing.Optional[Boolean] = Field(default=False)
    loaded_devices: typing.Optional[Boolean] = Field(default=False, alias='loadedDevices')
    devices_missing_in_inventory: typing.Optional[Boolean] = Field(default=False, alias='devicesMissingInInventory')
    devices_missing_in_uniconfig: typing.Optional[Boolean] = Field(default=False, alias='devicesMissingInUniconfig')


class SyncResponsePayload(BaseModel):
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    loaded_devices: typing.Optional[typing.Optional[JSON]] = Field(default=None, alias='loadedDevices')
    devices_missing_in_inventory: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='devicesMissingInInventory')
    devices_missing_in_uniconfig: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='devicesMissingInUniconfig')


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


class PtpDevicesQuery(Query):
    _name: str = PrivateAttr('ptpDevices')
    filters: typing.Optional[PtpDeviceFilter] = Field(default=None, json_schema_extra={'type': 'PtpDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: PtpDeviceConnection


class NetDevicesQuery(Query):
    _name: str = PrivateAttr('netDevices')
    filters: typing.Optional[NetDeviceFilter] = Field(default=None, json_schema_extra={'type': 'NetDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: NetDeviceConnection


class SynceDevicesQuery(Query):
    _name: str = PrivateAttr('synceDevices')
    filters: typing.Optional[SynceDeviceFilter] = Field(default=None, json_schema_extra={'type': 'SynceDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: SynceDeviceConnection


class MplsDevicesQuery(Query):
    _name: str = PrivateAttr('mplsDevices')
    filters: typing.Optional[MplsDeviceFilter] = Field(default=None, json_schema_extra={'type': 'MplsDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: MplsDeviceConnection


class NetRoutingPathsQuery(Query):
    _name: str = PrivateAttr('netRoutingPaths')
    device_from: ID = Field(alias='deviceFrom', json_schema_extra={'type': 'ID!'})
    device_to: ID = Field(alias='deviceTo', json_schema_extra={'type': 'ID!'})
    output_collection: typing.Optional[NetRoutingPathOutputCollections] = Field(default=None, alias='outputCollection', json_schema_extra={'type': 'NetRoutingPathOutputCollections'})
    payload: NetRoutingPathConnection


class PtpPathToGmClockQuery(Query):
    _name: str = PrivateAttr('ptpPathToGmClock')
    device_from: ID = Field(alias='deviceFrom', json_schema_extra={'type': 'ID!'})
    output_collection: typing.Optional[PtpPathOutputCollections] = Field(default=None, alias='outputCollection', json_schema_extra={'type': 'PtpPathOutputCollections'})
    payload: PtpPath


class SyncePathToGmQuery(Query):
    _name: str = PrivateAttr('syncePathToGm')
    device_from: ID = Field(alias='deviceFrom', json_schema_extra={'type': 'ID!'})
    output_collection: typing.Optional[SyncePathOutputCollections] = Field(default=None, alias='outputCollection', json_schema_extra={'type': 'SyncePathOutputCollections'})
    payload: SyncePath


class PtpDiffSynceQuery(Query):
    _name: str = PrivateAttr('ptpDiffSynce')
    filters: typing.Optional[PtpDeviceFilter] = Field(default=None, json_schema_extra={'type': 'PtpDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: PtpDiffSynceConnection


class BackupsQuery(Query):
    _name: str = PrivateAttr('backups')


class TopologyDiffQuery(Query):
    _name: str = PrivateAttr('topologyDiff')
    new_db: String = Field(alias='newDb', json_schema_extra={'type': 'String!'})
    old_db: String = Field(alias='oldDb', json_schema_extra={'type': 'String!'})
    collection_type: TopologyType = Field(alias='collectionType', json_schema_extra={'type': 'TopologyType!'})
    payload: TopologyResponse


class CommonNodesQuery(Query):
    _name: str = PrivateAttr('commonNodes')
    selected_nodes: typing.Optional[list[String]] = Field(default=None, alias='selectedNodes', json_schema_extra={'type': '[String!]!'})
    db_name: typing.Optional[String] = Field(default=None, alias='dbName', json_schema_extra={'type': 'String'})
    topology_type: typing.Optional[TopologyType] = Field(default=None, alias='topologyType', json_schema_extra={'type': 'TopologyType'})
    payload: CommonNodesResponse


class ProvidersQuery(Query):
    _name: str = PrivateAttr('providers')


class ProviderQuery(Query):
    _name: str = PrivateAttr('provider')
    topology_type: TopologyType = Field(alias='topologyType', json_schema_extra={'type': 'TopologyType!'})
    payload: ProviderResponse


class DeviceMetadataQuery(Query):
    _name: str = PrivateAttr('deviceMetadata')
    filters: typing.Optional[DeviceMetadataFilter] = Field(default=None, json_schema_extra={'type': 'DeviceMetadataFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: MetadataConnection


class MplsLspCountQuery(Query):
    _name: str = PrivateAttr('mplsLspCount')
    device_id: ID = Field(alias='deviceId', json_schema_extra={'type': 'ID!'})
    payload: MplsTotalLsps


class MplsLspPathQuery(Query):
    _name: str = PrivateAttr('mplsLspPath')
    device_id: ID = Field(alias='deviceId', json_schema_extra={'type': 'ID!'})
    lsp_id: ID = Field(alias='lspId', json_schema_extra={'type': 'ID!'})
    payload: MplsLspPath


class TopologyOverlayQuery(Query):
    _name: str = PrivateAttr('topologyOverlay')
    first_topology: TopologyType = Field(alias='firstTopology', json_schema_extra={'type': 'TopologyType!'})
    second_topology: TopologyType = Field(alias='secondTopology', json_schema_extra={'type': 'TopologyType!'})
    filters: typing.Optional[TopologyOverlayDeviceFilter] = Field(default=None, json_schema_extra={'type': 'TopologyOverlayDeviceFilter'})
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    cursor: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: TopologyOverlayDeviceConnection


class NeighborsQuery(Query):
    _name: str = PrivateAttr('neighbors')
    device_name: String = Field(alias='deviceName', json_schema_extra={'type': 'String!'})
    topology_type: TopologyType = Field(alias='topologyType', json_schema_extra={'type': 'TopologyType!'})
    payload: Neighbor


class NodeQueryResponse(BaseModel):
    data: typing.Optional[Node] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PhyDevicesQueryResponse(BaseModel):
    data: typing.Optional[PhyDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PhyDevicesData(BaseModel):
    phy_devices: PhyDeviceConnectionPayload = Field(alias='phyDevices')


class PtpDevicesQueryResponse(BaseModel):
    data: typing.Optional[PtpDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PtpDevicesData(BaseModel):
    ptp_devices: PtpDeviceConnectionPayload = Field(alias='ptpDevices')


class NetDevicesQueryResponse(BaseModel):
    data: typing.Optional[NetDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class NetDevicesData(BaseModel):
    net_devices: NetDeviceConnectionPayload = Field(alias='netDevices')


class SynceDevicesQueryResponse(BaseModel):
    data: typing.Optional[SynceDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SynceDevicesData(BaseModel):
    synce_devices: SynceDeviceConnectionPayload = Field(alias='synceDevices')


class MplsDevicesQueryResponse(BaseModel):
    data: typing.Optional[MplsDevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class MplsDevicesData(BaseModel):
    mpls_devices: MplsDeviceConnectionPayload = Field(alias='mplsDevices')


class NetRoutingPathsQueryResponse(BaseModel):
    data: typing.Optional[NetRoutingPathsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class NetRoutingPathsData(BaseModel):
    net_routing_paths: typing.Optional[NetRoutingPathConnectionPayload] = Field(alias='netRoutingPaths')


class PtpPathToGmClockQueryResponse(BaseModel):
    data: typing.Optional[PtpPathToGmClockData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PtpPathToGmClockData(BaseModel):
    ptp_path_to_gm_clock: PtpPathPayload = Field(alias='ptpPathToGmClock')


class SyncePathToGmQueryResponse(BaseModel):
    data: typing.Optional[SyncePathToGmData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SyncePathToGmData(BaseModel):
    synce_path_to_gm: SyncePathPayload = Field(alias='syncePathToGm')


class PtpDiffSynceQueryResponse(BaseModel):
    data: typing.Optional[PtpDiffSynceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class PtpDiffSynceData(BaseModel):
    ptp_diff_synce: PtpDiffSynceConnectionPayload = Field(alias='ptpDiffSynce')


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


class DeviceMetadataQueryResponse(BaseModel):
    data: typing.Optional[DeviceMetadataData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeviceMetadataData(BaseModel):
    device_metadata: MetadataConnectionPayload = Field(alias='deviceMetadata')


class MplsLspCountQueryResponse(BaseModel):
    data: typing.Optional[MplsLspCountData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class MplsLspCountData(BaseModel):
    mpls_lsp_count: typing.Optional[list[MplsTotalLspsPayload]] = Field(alias='mplsLspCount')


class MplsLspPathQueryResponse(BaseModel):
    data: typing.Optional[MplsLspPathData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class MplsLspPathData(BaseModel):
    mpls_lsp_path: MplsLspPathPayload = Field(alias='mplsLspPath')


class TopologyOverlayQueryResponse(BaseModel):
    data: typing.Optional[TopologyOverlayData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TopologyOverlayData(BaseModel):
    topology_overlay: TopologyOverlayDeviceConnectionPayload = Field(alias='topologyOverlay')


class NeighborsQueryResponse(BaseModel):
    data: typing.Optional[NeighborsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class NeighborsData(BaseModel):
    neighbors: typing.Optional[list[NeighborPayload]]


class CreateBackupMutation(Mutation):
    _name: str = PrivateAttr('createBackup')


class DeleteBackupsMutation(Mutation):
    _name: str = PrivateAttr('deleteBackups')
    delete_age: typing.Optional[Int] = Field(default=None, alias='deleteAge', json_schema_extra={'type': 'Int'})
    payload: DeleteBackupsResponse


class UpdateCoordinatesMutation(Mutation):
    _name: str = PrivateAttr('updateCoordinates')
    coordinates_list: typing.Optional[list[CoordinatesInput]] = Field(default=None, alias='coordinatesList', json_schema_extra={'type': '[CoordinatesInput!]!'})
    topology_type: typing.Optional[TopologyType] = Field(default=None, alias='topologyType', json_schema_extra={'type': 'TopologyType'})
    payload: CoordinatesResponse


class UpdateNodeStatusMutation(Mutation):
    _name: str = PrivateAttr('updateNodeStatus')
    device_name: String = Field(alias='deviceName', json_schema_extra={'type': 'String!'})
    status: NodeStatus = Field(json_schema_extra={'type': 'NodeStatus!'})
    interface_name: typing.Optional[String] = Field(default=None, alias='interfaceName', json_schema_extra={'type': 'String'})
    topology_type: typing.Optional[TopologyType] = Field(default=None, alias='topologyType', json_schema_extra={'type': 'TopologyType'})
    payload: Boolean


class SyncMutation(Mutation):
    _name: str = PrivateAttr('sync')
    topology_type: TopologyType = Field(alias='topologyType', json_schema_extra={'type': 'TopologyType!'})
    devices: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String]'})
    labels: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String]'})
    payload: SyncResponse


class EnableRemoteDebugSessionMutation(Mutation):
    _name: str = PrivateAttr('enableRemoteDebugSession')
    host: String = Field(json_schema_extra={'type': 'String!'})
    port: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    stdout_to_server: typing.Optional[Boolean] = Field(default=None, alias='stdoutToServer', json_schema_extra={'type': 'Boolean'})
    stderr_to_server: typing.Optional[Boolean] = Field(default=None, alias='stderrToServer', json_schema_extra={'type': 'Boolean'})
    payload: Boolean


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


class EnableRemoteDebugSessionMutationResponse(BaseModel):
    data: typing.Optional[EnableRemoteDebugSessionData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class EnableRemoteDebugSessionData(BaseModel):
    enable_remote_debug_session: typing.Optional[String] = Field(alias='enableRemoteDebugSession')


class Coordinates(Payload):
    x: typing.Optional[Boolean] = Field(default=False)
    y: typing.Optional[Boolean] = Field(default=False)


class CoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]] = Field(default=None)
    y: typing.Optional[typing.Optional[Float]] = Field(default=None)


class DeviceMetadata(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    device_name: typing.Optional[Boolean] = Field(default=False, alias='deviceName')
    device_type: typing.Optional[Boolean] = Field(default=False, alias='deviceType')
    vendor: typing.Optional[Boolean] = Field(default=False)
    model: typing.Optional[Boolean] = Field(default=False)
    version: typing.Optional[Boolean] = Field(default=False)
    protocol_type: typing.Optional[Boolean] = Field(default=False, alias='protocolType')
    geo_location: typing.Optional[DeviceGeoLocation] = Field(default=None, alias='geoLocation')


class DeviceMetadataPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    device_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceName')
    device_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceType')
    vendor: typing.Optional[typing.Optional[String]] = Field(default=None)
    model: typing.Optional[typing.Optional[String]] = Field(default=None)
    version: typing.Optional[typing.Optional[String]] = Field(default=None)
    protocol_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='protocolType')
    geo_location: typing.Optional[DeviceGeoLocationPayload] = Field(default=None, alias='geoLocation')


class DeviceMetadataEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[DeviceMetadata] = Field(default=None)


class DeviceMetadataEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[DeviceMetadataPayload] = Field(default=None)


class MetadataConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[DeviceMetadataEdge] = Field(default=None)


class MetadataConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[DeviceMetadataEdgePayload]]] = Field(default=None)


class DeviceGeoLocation(Payload):
    type: typing.Optional[Boolean] = Field(default=False)
    coordinates: typing.Optional[Boolean] = Field(default=False)
    bbox: typing.Optional[Boolean] = Field(default=False)


class DeviceGeoLocationPayload(BaseModel):
    type: typing.Optional[typing.Optional[GeometryType]] = Field(default=None)
    coordinates: typing.Optional[typing.Optional[list[typing.Optional[Float]]]] = Field(default=None)
    bbox: typing.Optional[typing.Optional[list[typing.Optional[Float]]]] = Field(default=None)


class MplsDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    coordinates: typing.Optional[Coordinates] = Field(default=None)
    details: typing.Optional[MplsDeviceDetails] = Field(default=None)
    status: typing.Optional[Boolean] = Field(default=False)
    labels: typing.Optional[Boolean] = Field(default=False)
    mpls_interfaces: typing.Optional[MplsInterfaceConnection] = Field(default=None, alias='mplsInterfaces')


class MplsDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    coordinates: typing.Optional[CoordinatesPayload] = Field(default=None)
    details: typing.Optional[MplsDeviceDetailsPayload] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    mpls_interfaces: typing.Optional[MplsInterfaceConnectionPayload] = Field(default=None, alias='mplsInterfaces')


class MplsDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[MplsDevice] = Field(default=None)


class MplsDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[MplsDevicePayload] = Field(default=None)


class MplsDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[MplsDeviceEdge] = Field(default=None)


class MplsDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[MplsDeviceEdgePayload]]] = Field(default=None)


class MplsDeviceDetails(Payload):
    mpls_data: typing.Optional[MplsData] = Field(default=None, alias='mplsData')
    lsp_tunnels: typing.Optional[LspTunnel] = Field(default=None, alias='lspTunnels')
    router_id: typing.Optional[Boolean] = Field(default=False, alias='routerId')


class MplsDeviceDetailsPayload(BaseModel):
    mpls_data: typing.Optional[typing.Optional[list[MplsDataPayload]]] = Field(default=None, alias='mplsData')
    lsp_tunnels: typing.Optional[typing.Optional[list[LspTunnelPayload]]] = Field(default=None, alias='lspTunnels')
    router_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='routerId')


class MplsData(Payload):
    lsp_id: typing.Optional[Boolean] = Field(default=False, alias='lspId')
    oper_state: typing.Optional[Boolean] = Field(default=False, alias='operState')
    in_label: typing.Optional[Boolean] = Field(default=False, alias='inLabel')
    in_interface: typing.Optional[Boolean] = Field(default=False, alias='inInterface')
    out_label: typing.Optional[Boolean] = Field(default=False, alias='outLabel')
    out_interface: typing.Optional[Boolean] = Field(default=False, alias='outInterface')
    mpls_operation: typing.Optional[Boolean] = Field(default=False, alias='mplsOperation')
    signalisation: typing.Optional[Boolean] = Field(default=False)


class MplsDataPayload(BaseModel):
    lsp_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='lspId')
    oper_state: typing.Optional[typing.Optional[String]] = Field(default=None, alias='operState')
    in_label: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='inLabel')
    in_interface: typing.Optional[typing.Optional[String]] = Field(default=None, alias='inInterface')
    out_label: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='outLabel')
    out_interface: typing.Optional[typing.Optional[String]] = Field(default=None, alias='outInterface')
    mpls_operation: typing.Optional[typing.Optional[MplsOperation]] = Field(default=None, alias='mplsOperation')
    signalisation: typing.Optional[typing.Optional[Signalisation]] = Field(default=None)


class LspTunnel(Payload):
    lsp_id: typing.Optional[Boolean] = Field(default=False, alias='lspId')
    signalisation: typing.Optional[Boolean] = Field(default=False)
    from_device: typing.Optional[Boolean] = Field(default=False, alias='fromDevice')
    to_device: typing.Optional[Boolean] = Field(default=False, alias='toDevice')
    uptime: typing.Optional[Boolean] = Field(default=False)


class LspTunnelPayload(BaseModel):
    lsp_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='lspId')
    signalisation: typing.Optional[typing.Optional[Signalisation]] = Field(default=None)
    from_device: typing.Optional[typing.Optional[String]] = Field(default=None, alias='fromDevice')
    to_device: typing.Optional[typing.Optional[String]] = Field(default=None, alias='toDevice')
    uptime: typing.Optional[typing.Optional[Int]] = Field(default=None)


class MplsInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    mpls_device: typing.Optional[MplsDevice] = Field(default=None, alias='mplsDevice')
    mpls_links: typing.Optional[MplsLinkConnection] = Field(default=None, alias='mplsLinks')


class MplsInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    mpls_device: typing.Optional[MplsDevicePayload] = Field(default=None, alias='mplsDevice')
    mpls_links: typing.Optional[MplsLinkConnectionPayload] = Field(default=None, alias='mplsLinks')


class MplsLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[MplsLinkEdge] = Field(default=None)


class MplsLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[MplsLinkEdgePayload]]] = Field(default=None)


class MplsLinkEdge(Payload):
    link: typing.Optional[Boolean] = Field(default=False)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[MplsInterface] = Field(default=None)


class MplsLinkEdgePayload(BaseModel):
    link: typing.Optional[typing.Optional[ID]] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[MplsInterfacePayload] = Field(default=None)


class MplsInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[MplsInterface] = Field(default=None)


class MplsInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[MplsInterfacePayload] = Field(default=None)


class MplsInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[MplsInterfaceEdge] = Field(default=None)


class MplsInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[MplsInterfaceEdgePayload]]] = Field(default=None)


class MplsTotalLsps(Payload):
    to_device: typing.Optional[Boolean] = Field(default=False, alias='toDevice')
    outcoming_lsps: typing.Optional[Boolean] = Field(default=False, alias='outcomingLsps')
    incoming_lsps: typing.Optional[Boolean] = Field(default=False, alias='incomingLsps')


class MplsTotalLspsPayload(BaseModel):
    to_device: typing.Optional[typing.Optional[String]] = Field(default=None, alias='toDevice')
    outcoming_lsps: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='outcomingLsps')
    incoming_lsps: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='incomingLsps')


class MplsLspMetadata(Payload):
    signalisation: typing.Optional[Boolean] = Field(default=False)
    from_device: typing.Optional[Boolean] = Field(default=False, alias='fromDevice')
    to_device: typing.Optional[Boolean] = Field(default=False, alias='toDevice')
    uptime: typing.Optional[Boolean] = Field(default=False)


class MplsLspMetadataPayload(BaseModel):
    signalisation: typing.Optional[typing.Optional[String]] = Field(default=None)
    from_device: typing.Optional[typing.Optional[String]] = Field(default=None, alias='fromDevice')
    to_device: typing.Optional[typing.Optional[String]] = Field(default=None, alias='toDevice')
    uptime: typing.Optional[typing.Optional[Int]] = Field(default=None)


class MplsLspPath(Payload):
    path: typing.Optional[Boolean] = Field(default=False)
    lsp_metadata: typing.Optional[MplsLspMetadata] = Field(default=None, alias='lspMetadata')


class MplsLspPathPayload(BaseModel):
    path: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    lsp_metadata: typing.Optional[MplsLspMetadataPayload] = Field(default=None, alias='lspMetadata')


class Neighbor(Payload):
    device_id: typing.Optional[Boolean] = Field(default=False, alias='deviceId')
    device_name: typing.Optional[Boolean] = Field(default=False, alias='deviceName')


class NeighborPayload(BaseModel):
    device_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceId')
    device_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceName')


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
    net_links: typing.Optional[NetLinkConnection] = Field(default=None, alias='netLinks')


class NetInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    ip_address: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ipAddress')
    net_device: typing.Optional[NetDevicePayload] = Field(default=None, alias='netDevice')
    igp_metric: typing.Optional[typing.Optional[Int]] = Field(default=None)
    net_links: typing.Optional[NetLinkConnectionPayload] = Field(default=None, alias='netLinks')


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


class NetLinkEdge(Payload):
    link: typing.Optional[Boolean] = Field(default=False)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[NetInterface] = Field(default=None)


class NetLinkEdgePayload(BaseModel):
    link: typing.Optional[typing.Optional[ID]] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[NetInterfacePayload] = Field(default=None)


class NetLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[NetLinkEdge] = Field(default=None)


class NetLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[NetLinkEdgePayload]]] = Field(default=None)


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
    device_type: typing.Optional[Boolean] = Field(default=False, alias='deviceType')
    sw_version: typing.Optional[Boolean] = Field(default=False, alias='swVersion')


class PhyDeviceDetailsPayload(BaseModel):
    device_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceType')
    sw_version: typing.Optional[typing.Optional[String]] = Field(default=None, alias='swVersion')


class PhyInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    phy_device: typing.Optional[PhyDevice] = Field(default=None, alias='phyDevice')
    details: typing.Optional[PhyInterfaceDetails] = Field(default=None)
    phy_links: typing.Optional[PhyLinkConnection] = Field(default=None, alias='phyLinks')


class PhyInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    phy_device: typing.Optional[PhyDevicePayload] = Field(default=None, alias='phyDevice')
    details: typing.Optional[PhyInterfaceDetailsPayload] = Field(default=None)
    phy_links: typing.Optional[PhyLinkConnectionPayload] = Field(default=None, alias='phyLinks')


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


class PhyInterfaceDetails(Payload):
    max_speed: typing.Optional[Boolean] = Field(default=False, alias='maxSpeed')


class PhyInterfaceDetailsPayload(BaseModel):
    max_speed: typing.Optional[typing.Optional[Float]] = Field(default=None, alias='maxSpeed')


class PhyLinkEdge(Payload):
    link: typing.Optional[Boolean] = Field(default=False)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PhyInterface] = Field(default=None)


class PhyLinkEdgePayload(BaseModel):
    link: typing.Optional[typing.Optional[ID]] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PhyInterfacePayload] = Field(default=None)


class PhyLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PhyLinkEdge] = Field(default=None)


class PhyLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PhyLinkEdgePayload]]] = Field(default=None)


class PtpDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    coordinates: typing.Optional[Coordinates] = Field(default=None)
    details: typing.Optional[PtpDeviceDetails] = Field(default=None)
    status: typing.Optional[Boolean] = Field(default=False)
    labels: typing.Optional[Boolean] = Field(default=False)
    ptp_interfaces: typing.Optional[PtpInterfaceConnection] = Field(default=None, alias='ptpInterfaces')


class PtpDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    coordinates: typing.Optional[CoordinatesPayload] = Field(default=None)
    details: typing.Optional[PtpDeviceDetailsPayload] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    ptp_interfaces: typing.Optional[PtpInterfaceConnectionPayload] = Field(default=None, alias='ptpInterfaces')


class PtpDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PtpDevice] = Field(default=None)


class PtpDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PtpDevicePayload] = Field(default=None)


class PtpDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PtpDeviceEdge] = Field(default=None)


class PtpDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PtpDeviceEdgePayload]]] = Field(default=None)


class PtpDeviceDetails(Payload):
    clock_type: typing.Optional[Boolean] = Field(default=False, alias='clockType')
    domain: typing.Optional[Boolean] = Field(default=False)
    ptp_profile: typing.Optional[Boolean] = Field(default=False, alias='ptpProfile')
    clock_id: typing.Optional[Boolean] = Field(default=False, alias='clockId')
    parent_clock_id: typing.Optional[Boolean] = Field(default=False, alias='parentClockId')
    gm_clock_id: typing.Optional[Boolean] = Field(default=False, alias='gmClockId')
    clock_class: typing.Optional[Boolean] = Field(default=False, alias='clockClass')
    clock_accuracy: typing.Optional[Boolean] = Field(default=False, alias='clockAccuracy')
    clock_variance: typing.Optional[Boolean] = Field(default=False, alias='clockVariance')
    time_recovery_status: typing.Optional[Boolean] = Field(default=False, alias='timeRecoveryStatus')
    global_priority: typing.Optional[Boolean] = Field(default=False, alias='globalPriority')
    user_priority: typing.Optional[Boolean] = Field(default=False, alias='userPriority')
    ptp_port_state: typing.Optional[Boolean] = Field(default=False, alias='ptpPortState')


class PtpDeviceDetailsPayload(BaseModel):
    clock_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='clockType')
    domain: typing.Optional[typing.Optional[Int]] = Field(default=None)
    ptp_profile: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptpProfile')
    clock_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='clockId')
    parent_clock_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='parentClockId')
    gm_clock_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='gmClockId')
    clock_class: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='clockClass')
    clock_accuracy: typing.Optional[typing.Optional[String]] = Field(default=None, alias='clockAccuracy')
    clock_variance: typing.Optional[typing.Optional[String]] = Field(default=None, alias='clockVariance')
    time_recovery_status: typing.Optional[typing.Optional[String]] = Field(default=None, alias='timeRecoveryStatus')
    global_priority: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='globalPriority')
    user_priority: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='userPriority')
    ptp_port_state: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptpPortState')


class PtpInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    details: typing.Optional[PtpInterfaceDetails] = Field(default=None)
    ptp_device: typing.Optional[PtpDevice] = Field(default=None, alias='ptpDevice')
    ptp_links: typing.Optional[PtpLinkConnection] = Field(default=None, alias='ptpLinks')


class PtpInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    details: typing.Optional[PtpInterfaceDetailsPayload] = Field(default=None)
    ptp_device: typing.Optional[PtpDevicePayload] = Field(default=None, alias='ptpDevice')
    ptp_links: typing.Optional[PtpLinkConnectionPayload] = Field(default=None, alias='ptpLinks')


class PtpInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PtpInterface] = Field(default=None)


class PtpInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PtpInterfacePayload] = Field(default=None)


class PtpInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PtpInterfaceEdge] = Field(default=None)


class PtpInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PtpInterfaceEdgePayload]]] = Field(default=None)


class PtpLinkEdge(Payload):
    link: typing.Optional[Boolean] = Field(default=False)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PtpInterface] = Field(default=None)


class PtpLinkEdgePayload(BaseModel):
    link: typing.Optional[typing.Optional[ID]] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PtpInterfacePayload] = Field(default=None)


class PtpLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PtpLinkEdge] = Field(default=None)


class PtpLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PtpLinkEdgePayload]]] = Field(default=None)


class PtpInterfaceDetails(Payload):
    ptp_status: typing.Optional[Boolean] = Field(default=False, alias='ptpStatus')
    ptsf_unusable: typing.Optional[Boolean] = Field(default=False, alias='ptsfUnusable')
    admin_oper_status: typing.Optional[Boolean] = Field(default=False, alias='adminOperStatus')


class PtpInterfaceDetailsPayload(BaseModel):
    ptp_status: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptpStatus')
    ptsf_unusable: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptsfUnusable')
    admin_oper_status: typing.Optional[typing.Optional[String]] = Field(default=None, alias='adminOperStatus')


class PtpPath(Payload):
    nodes: typing.Optional[Boolean] = Field(default=False)
    complete: typing.Optional[Boolean] = Field(default=False)


class PtpPathPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[typing.Optional[ID]]]] = Field(default=None)
    complete: typing.Optional[typing.Optional[Boolean]] = Field(default=None)


class PtpDiffSynce(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    ptp_upstream_interface: typing.Optional[Boolean] = Field(default=False, alias='ptpUpstreamInterface')
    ptp_upstream_interface_name: typing.Optional[Boolean] = Field(default=False, alias='ptpUpstreamInterfaceName')
    ptp_upstream_interface_status: typing.Optional[Boolean] = Field(default=False, alias='ptpUpstreamInterfaceStatus')
    synce_id: typing.Optional[Boolean] = Field(default=False, alias='synceId')
    synce_upstream_interface_name: typing.Optional[Boolean] = Field(default=False, alias='synceUpstreamInterfaceName')


class PtpDiffSyncePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    ptp_upstream_interface: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='ptpUpstreamInterface')
    ptp_upstream_interface_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptpUpstreamInterfaceName')
    ptp_upstream_interface_status: typing.Optional[typing.Optional[String]] = Field(default=None, alias='ptpUpstreamInterfaceStatus')
    synce_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='synceId')
    synce_upstream_interface_name: typing.Optional[typing.Optional[String]] = Field(default=None, alias='synceUpstreamInterfaceName')


class PtpDiffSynceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[PtpDiffSynce] = Field(default=None)


class PtpDiffSynceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[PtpDiffSyncePayload] = Field(default=None)


class PtpDiffSynceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[PtpDiffSynceEdge] = Field(default=None)


class PtpDiffSynceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[PtpDiffSynceEdgePayload]]] = Field(default=None)


class SynceDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    coordinates: typing.Optional[Coordinates] = Field(default=None)
    details: typing.Optional[SynceDeviceDetails] = Field(default=None)
    status: typing.Optional[Boolean] = Field(default=False)
    labels: typing.Optional[Boolean] = Field(default=False)
    synce_interfaces: typing.Optional[SynceInterfaceConnection] = Field(default=None, alias='synceInterfaces')


class SynceDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    coordinates: typing.Optional[CoordinatesPayload] = Field(default=None)
    details: typing.Optional[SynceDeviceDetailsPayload] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    labels: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None)
    synce_interfaces: typing.Optional[SynceInterfaceConnectionPayload] = Field(default=None, alias='synceInterfaces')


class SynceDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[SynceDevice] = Field(default=None)


class SynceDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[SynceDevicePayload] = Field(default=None)


class SynceDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[SynceDeviceEdge] = Field(default=None)


class SynceDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[SynceDeviceEdgePayload]]] = Field(default=None)


class SynceDeviceDetails(Payload):
    selected_for_use: typing.Optional[Boolean] = Field(default=False, alias='selectedForUse')


class SynceDeviceDetailsPayload(BaseModel):
    selected_for_use: typing.Optional[typing.Optional[String]] = Field(default=None, alias='selectedForUse')


class SynceInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    synce_device: typing.Optional[SynceDevice] = Field(default=None, alias='synceDevice')
    synce_links: typing.Optional[SynceLinkConnection] = Field(default=None, alias='synceLinks')
    details: typing.Optional[SynceInterfaceDetails] = Field(default=None)


class SynceInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[NodeStatus]] = Field(default=None)
    synce_device: typing.Optional[SynceDevicePayload] = Field(default=None, alias='synceDevice')
    synce_links: typing.Optional[SynceLinkConnectionPayload] = Field(default=None, alias='synceLinks')
    details: typing.Optional[SynceInterfaceDetailsPayload] = Field(default=None)


class SynceLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[SynceLinkEdge] = Field(default=None)


class SynceLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[SynceLinkEdgePayload]]] = Field(default=None)


class SynceLinkEdge(Payload):
    link: typing.Optional[Boolean] = Field(default=False)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[SynceInterface] = Field(default=None)


class SynceLinkEdgePayload(BaseModel):
    link: typing.Optional[typing.Optional[ID]] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[SynceInterfacePayload] = Field(default=None)


class SynceInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[SynceInterface] = Field(default=None)


class SynceInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[SynceInterfacePayload] = Field(default=None)


class SynceInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[SynceInterfaceEdge] = Field(default=None)


class SynceInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[SynceInterfaceEdgePayload]]] = Field(default=None)


class SynceInterfaceDetails(Payload):
    synce_enabled: typing.Optional[Boolean] = Field(default=False, alias='synceEnabled')
    rx_quality_level: typing.Optional[Boolean] = Field(default=False, alias='rxQualityLevel')
    qualified_for_use: typing.Optional[Boolean] = Field(default=False, alias='qualifiedForUse')
    not_qualified_due_to: typing.Optional[Boolean] = Field(default=False, alias='notQualifiedDueTo')
    not_selected_due_to: typing.Optional[Boolean] = Field(default=False, alias='notSelectedDueTo')


class SynceInterfaceDetailsPayload(BaseModel):
    synce_enabled: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='synceEnabled')
    rx_quality_level: typing.Optional[typing.Optional[String]] = Field(default=None, alias='rxQualityLevel')
    qualified_for_use: typing.Optional[typing.Optional[String]] = Field(default=None, alias='qualifiedForUse')
    not_qualified_due_to: typing.Optional[typing.Optional[String]] = Field(default=None, alias='notQualifiedDueTo')
    not_selected_due_to: typing.Optional[typing.Optional[String]] = Field(default=None, alias='notSelectedDueTo')


class SyncePath(Payload):
    nodes: typing.Optional[Boolean] = Field(default=False)
    complete: typing.Optional[Boolean] = Field(default=False)


class SyncePathPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[typing.Optional[ID]]]] = Field(default=None)
    complete: typing.Optional[typing.Optional[Boolean]] = Field(default=None)


class TopologyOverlayDevice(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    second_topology_id: typing.Optional[Boolean] = Field(default=False, alias='secondTopologyId')
    topology_overlay_interfaces: typing.Optional[TopologyOverlayInterfaceConnection] = Field(default=None, alias='topologyOverlayInterfaces')


class TopologyOverlayDevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    second_topology_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='secondTopologyId')
    topology_overlay_interfaces: typing.Optional[TopologyOverlayInterfaceConnectionPayload] = Field(default=None, alias='topologyOverlayInterfaces')


class TopologyOverlayDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[TopologyOverlayDeviceEdge] = Field(default=None)


class TopologyOverlayDeviceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[TopologyOverlayDeviceEdgePayload]]] = Field(default=None)


class TopologyOverlayDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[TopologyOverlayDevice] = Field(default=None)


class TopologyOverlayDeviceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[TopologyOverlayDevicePayload] = Field(default=None)


class TopologyOverlayInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    second_topology_id: typing.Optional[Boolean] = Field(default=False, alias='secondTopologyId')
    topology_overlay_device: typing.Optional[TopologyOverlayDevice] = Field(default=None, alias='topologyOverlayDevice')
    topology_overlay_links: typing.Optional[TopologyOverlayLinkConnection] = Field(default=None, alias='topologyOverlayLinks')


class TopologyOverlayInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    second_topology_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='secondTopologyId')
    topology_overlay_device: typing.Optional[TopologyOverlayDevicePayload] = Field(default=None, alias='topologyOverlayDevice')
    topology_overlay_links: typing.Optional[TopologyOverlayLinkConnectionPayload] = Field(default=None, alias='topologyOverlayLinks')


class TopologyOverlayInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[TopologyOverlayInterfaceEdge] = Field(default=None)


class TopologyOverlayInterfaceConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[TopologyOverlayInterfaceEdgePayload]]] = Field(default=None)


class TopologyOverlayInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[TopologyOverlayInterface] = Field(default=None)


class TopologyOverlayInterfaceEdgePayload(BaseModel):
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[TopologyOverlayInterfacePayload] = Field(default=None)


class TopologyOverlayLinkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[TopologyOverlayLinkEdge] = Field(default=None)


class TopologyOverlayLinkConnectionPayload(BaseModel):
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    edges: typing.Optional[typing.Optional[list[TopologyOverlayLinkEdgePayload]]] = Field(default=None)


class TopologyOverlayLinkEdge(Payload):
    link: typing.Optional[TopologyOverlayLinkIds] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)
    node: typing.Optional[TopologyOverlayInterface] = Field(default=None)


class TopologyOverlayLinkEdgePayload(BaseModel):
    link: typing.Optional[TopologyOverlayLinkIdsPayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)
    node: typing.Optional[TopologyOverlayInterfacePayload] = Field(default=None)


class TopologyOverlayLinkIds(Payload):
    first_topology_link_id: typing.Optional[Boolean] = Field(default=False, alias='firstTopologyLinkId')
    second_topology_link_id: typing.Optional[Boolean] = Field(default=False, alias='secondTopologyLinkId')


class TopologyOverlayLinkIdsPayload(BaseModel):
    first_topology_link_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='firstTopologyLinkId')
    second_topology_link_id: typing.Optional[typing.Optional[ID]] = Field(default=None, alias='secondTopologyLinkId')


Node.model_rebuild()
CoordinatesInput.model_rebuild()
DeviceMetadataFilter.model_rebuild()
MplsDeviceFilter.model_rebuild()
MplsInterfaceFilter.model_rebuild()
NetDeviceFilter.model_rebuild()
NetInterfaceFilter.model_rebuild()
NetNetworkFilter.model_rebuild()
PhyDeviceFilter.model_rebuild()
PhyInterfaceFilter.model_rebuild()
PtpDeviceFilter.model_rebuild()
PtpInterfaceFilter.model_rebuild()
SynceDeviceFilter.model_rebuild()
SynceInterfaceFilter.model_rebuild()
TopologyOverlayDeviceFilter.model_rebuild()
TopologyOverlayInterfaceFilter.model_rebuild()
CreateBackupResponse.model_rebuild()
CreateBackupResponsePayload.model_rebuild()
DeleteBackupsResponse.model_rebuild()
DeleteBackupsResponsePayload.model_rebuild()
CoordinatesResponse.model_rebuild()
CoordinatesResponsePayload.model_rebuild()
InstalledDevices.model_rebuild()
InstalledDevicesPayload.model_rebuild()
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
PtpDevicesQuery.model_rebuild()
NetDevicesQuery.model_rebuild()
SynceDevicesQuery.model_rebuild()
MplsDevicesQuery.model_rebuild()
NetRoutingPathsQuery.model_rebuild()
PtpPathToGmClockQuery.model_rebuild()
SyncePathToGmQuery.model_rebuild()
PtpDiffSynceQuery.model_rebuild()
BackupsQuery.model_rebuild()
TopologyDiffQuery.model_rebuild()
CommonNodesQuery.model_rebuild()
ProvidersQuery.model_rebuild()
ProviderQuery.model_rebuild()
DeviceMetadataQuery.model_rebuild()
MplsLspCountQuery.model_rebuild()
MplsLspPathQuery.model_rebuild()
TopologyOverlayQuery.model_rebuild()
NeighborsQuery.model_rebuild()
NodeQueryResponse.model_rebuild()
PhyDevicesQueryResponse.model_rebuild()
PhyDevicesData.model_rebuild()
PtpDevicesQueryResponse.model_rebuild()
PtpDevicesData.model_rebuild()
NetDevicesQueryResponse.model_rebuild()
NetDevicesData.model_rebuild()
SynceDevicesQueryResponse.model_rebuild()
SynceDevicesData.model_rebuild()
MplsDevicesQueryResponse.model_rebuild()
MplsDevicesData.model_rebuild()
NetRoutingPathsQueryResponse.model_rebuild()
NetRoutingPathsData.model_rebuild()
PtpPathToGmClockQueryResponse.model_rebuild()
PtpPathToGmClockData.model_rebuild()
SyncePathToGmQueryResponse.model_rebuild()
SyncePathToGmData.model_rebuild()
PtpDiffSynceQueryResponse.model_rebuild()
PtpDiffSynceData.model_rebuild()
TopologyDiffQueryResponse.model_rebuild()
TopologyDiffData.model_rebuild()
CommonNodesQueryResponse.model_rebuild()
CommonNodesData.model_rebuild()
ProviderQueryResponse.model_rebuild()
ProviderData.model_rebuild()
DeviceMetadataQueryResponse.model_rebuild()
DeviceMetadataData.model_rebuild()
MplsLspCountQueryResponse.model_rebuild()
MplsLspCountData.model_rebuild()
MplsLspPathQueryResponse.model_rebuild()
MplsLspPathData.model_rebuild()
TopologyOverlayQueryResponse.model_rebuild()
TopologyOverlayData.model_rebuild()
NeighborsQueryResponse.model_rebuild()
NeighborsData.model_rebuild()
CreateBackupMutation.model_rebuild()
DeleteBackupsMutation.model_rebuild()
UpdateCoordinatesMutation.model_rebuild()
UpdateNodeStatusMutation.model_rebuild()
SyncMutation.model_rebuild()
EnableRemoteDebugSessionMutation.model_rebuild()
DeleteBackupsMutationResponse.model_rebuild()
DeleteBackupsData.model_rebuild()
UpdateCoordinatesMutationResponse.model_rebuild()
UpdateCoordinatesData.model_rebuild()
UpdateNodeStatusMutationResponse.model_rebuild()
UpdateNodeStatusData.model_rebuild()
SyncMutationResponse.model_rebuild()
SyncData.model_rebuild()
EnableRemoteDebugSessionMutationResponse.model_rebuild()
EnableRemoteDebugSessionData.model_rebuild()
Coordinates.model_rebuild()
CoordinatesPayload.model_rebuild()
DeviceMetadata.model_rebuild()
DeviceMetadataPayload.model_rebuild()
DeviceMetadataEdge.model_rebuild()
DeviceMetadataEdgePayload.model_rebuild()
MetadataConnection.model_rebuild()
MetadataConnectionPayload.model_rebuild()
DeviceGeoLocation.model_rebuild()
DeviceGeoLocationPayload.model_rebuild()
MplsDevice.model_rebuild()
MplsDevicePayload.model_rebuild()
MplsDeviceEdge.model_rebuild()
MplsDeviceEdgePayload.model_rebuild()
MplsDeviceConnection.model_rebuild()
MplsDeviceConnectionPayload.model_rebuild()
MplsDeviceDetails.model_rebuild()
MplsDeviceDetailsPayload.model_rebuild()
MplsData.model_rebuild()
MplsDataPayload.model_rebuild()
LspTunnel.model_rebuild()
LspTunnelPayload.model_rebuild()
MplsInterface.model_rebuild()
MplsInterfacePayload.model_rebuild()
MplsLinkConnection.model_rebuild()
MplsLinkConnectionPayload.model_rebuild()
MplsLinkEdge.model_rebuild()
MplsLinkEdgePayload.model_rebuild()
MplsInterfaceEdge.model_rebuild()
MplsInterfaceEdgePayload.model_rebuild()
MplsInterfaceConnection.model_rebuild()
MplsInterfaceConnectionPayload.model_rebuild()
MplsTotalLsps.model_rebuild()
MplsTotalLspsPayload.model_rebuild()
MplsLspMetadata.model_rebuild()
MplsLspMetadataPayload.model_rebuild()
MplsLspPath.model_rebuild()
MplsLspPathPayload.model_rebuild()
Neighbor.model_rebuild()
NeighborPayload.model_rebuild()
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
NetLinkEdge.model_rebuild()
NetLinkEdgePayload.model_rebuild()
NetLinkConnection.model_rebuild()
NetLinkConnectionPayload.model_rebuild()
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
PhyInterface.model_rebuild()
PhyInterfacePayload.model_rebuild()
PhyInterfaceEdge.model_rebuild()
PhyInterfaceEdgePayload.model_rebuild()
PhyInterfaceConnection.model_rebuild()
PhyInterfaceConnectionPayload.model_rebuild()
PhyInterfaceDetails.model_rebuild()
PhyInterfaceDetailsPayload.model_rebuild()
PhyLinkEdge.model_rebuild()
PhyLinkEdgePayload.model_rebuild()
PhyLinkConnection.model_rebuild()
PhyLinkConnectionPayload.model_rebuild()
PtpDevice.model_rebuild()
PtpDevicePayload.model_rebuild()
PtpDeviceEdge.model_rebuild()
PtpDeviceEdgePayload.model_rebuild()
PtpDeviceConnection.model_rebuild()
PtpDeviceConnectionPayload.model_rebuild()
PtpDeviceDetails.model_rebuild()
PtpDeviceDetailsPayload.model_rebuild()
PtpInterface.model_rebuild()
PtpInterfacePayload.model_rebuild()
PtpInterfaceEdge.model_rebuild()
PtpInterfaceEdgePayload.model_rebuild()
PtpInterfaceConnection.model_rebuild()
PtpInterfaceConnectionPayload.model_rebuild()
PtpLinkEdge.model_rebuild()
PtpLinkEdgePayload.model_rebuild()
PtpLinkConnection.model_rebuild()
PtpLinkConnectionPayload.model_rebuild()
PtpInterfaceDetails.model_rebuild()
PtpInterfaceDetailsPayload.model_rebuild()
PtpPath.model_rebuild()
PtpPathPayload.model_rebuild()
PtpDiffSynce.model_rebuild()
PtpDiffSyncePayload.model_rebuild()
PtpDiffSynceEdge.model_rebuild()
PtpDiffSynceEdgePayload.model_rebuild()
PtpDiffSynceConnection.model_rebuild()
PtpDiffSynceConnectionPayload.model_rebuild()
SynceDevice.model_rebuild()
SynceDevicePayload.model_rebuild()
SynceDeviceEdge.model_rebuild()
SynceDeviceEdgePayload.model_rebuild()
SynceDeviceConnection.model_rebuild()
SynceDeviceConnectionPayload.model_rebuild()
SynceDeviceDetails.model_rebuild()
SynceDeviceDetailsPayload.model_rebuild()
SynceInterface.model_rebuild()
SynceInterfacePayload.model_rebuild()
SynceLinkConnection.model_rebuild()
SynceLinkConnectionPayload.model_rebuild()
SynceLinkEdge.model_rebuild()
SynceLinkEdgePayload.model_rebuild()
SynceInterfaceEdge.model_rebuild()
SynceInterfaceEdgePayload.model_rebuild()
SynceInterfaceConnection.model_rebuild()
SynceInterfaceConnectionPayload.model_rebuild()
SynceInterfaceDetails.model_rebuild()
SynceInterfaceDetailsPayload.model_rebuild()
SyncePath.model_rebuild()
SyncePathPayload.model_rebuild()
TopologyOverlayDevice.model_rebuild()
TopologyOverlayDevicePayload.model_rebuild()
TopologyOverlayDeviceConnection.model_rebuild()
TopologyOverlayDeviceConnectionPayload.model_rebuild()
TopologyOverlayDeviceEdge.model_rebuild()
TopologyOverlayDeviceEdgePayload.model_rebuild()
TopologyOverlayInterface.model_rebuild()
TopologyOverlayInterfacePayload.model_rebuild()
TopologyOverlayInterfaceConnection.model_rebuild()
TopologyOverlayInterfaceConnectionPayload.model_rebuild()
TopologyOverlayInterfaceEdge.model_rebuild()
TopologyOverlayInterfaceEdgePayload.model_rebuild()
TopologyOverlayLinkConnection.model_rebuild()
TopologyOverlayLinkConnectionPayload.model_rebuild()
TopologyOverlayLinkEdge.model_rebuild()
TopologyOverlayLinkEdgePayload.model_rebuild()
TopologyOverlayLinkIds.model_rebuild()
TopologyOverlayLinkIdsPayload.model_rebuild()

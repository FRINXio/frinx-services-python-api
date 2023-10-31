from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from graphql_pydantic_converter.graphql_types import Subscription
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

ID: typing.TypeAlias = str
String: typing.TypeAlias = str
Boolean: typing.TypeAlias = bool
Int: typing.TypeAlias = int
Upload: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float


class DeviceServiceState(ENUM):
    PLANNING = 'PLANNING'
    IN_SERVICE = 'IN_SERVICE'
    OUT_OF_SERVICE = 'OUT_OF_SERVICE'


class DeviceSource(ENUM):
    MANUAL = 'MANUAL'
    DISCOVERED = 'DISCOVERED'
    IMPORTED = 'IMPORTED'


class DeviceSize(ENUM):
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'


class SortDeviceBy(ENUM):
    NAME = 'NAME'
    CREATED_AT = 'CREATED_AT'


class SortDirection(ENUM):
    ASC = 'ASC'
    DESC = 'DESC'


class GraphEdgeStatus(ENUM):
    ok = 'ok'
    unknown = 'unknown'


class Node(Interface):
    id: typing.Optional[Boolean] = Field(default=None)


class BaseGraphNode(Interface):
    id: typing.Optional[Boolean] = Field(default=None)
    interfaces: typing.Optional[GraphNodeInterface] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)
    device_type: typing.Optional[Boolean] = Field(default=None, alias='deviceType')
    software_version: typing.Optional[Boolean] = Field(default=None, alias='softwareVersion')


class FilterDevicesInput(Input):
    labels: typing.Optional[list[String]] = Field(default=None)
    device_name: typing.Optional[String] = Field(default=None, alias='deviceName')


class DeviceOrderByInput(Input):
    sort_key: SortDeviceBy = Field(alias='sortKey')
    direction: SortDirection


class AddDeviceInput(Input):
    name: String
    zone_id: String = Field(alias='zoneId')
    label_ids: typing.Optional[list[String]] = Field(default=None, alias='labelIds')
    device_size: typing.Optional[DeviceSize] = Field(default=None, alias='deviceSize')
    service_state: typing.Optional[DeviceServiceState] = Field(default=None, alias='serviceState')
    mount_parameters: typing.Optional[String] = Field(default=None, alias='mountParameters')
    blueprint_id: typing.Optional[String] = Field(default=None, alias='blueprintId')
    model: typing.Optional[String] = Field(default=None)
    vendor: typing.Optional[String] = Field(default=None)
    address: typing.Optional[String] = Field(default=None)
    username: typing.Optional[String] = Field(default=None)
    password: typing.Optional[String] = Field(default=None)
    port: typing.Optional[Int] = Field(default=None)
    device_type: typing.Optional[String] = Field(default=None, alias='deviceType')
    version: typing.Optional[String] = Field(default=None)


class UpdateDeviceInput(Input):
    mount_parameters: typing.Optional[String] = Field(default=None, alias='mountParameters')
    blueprint_id: typing.Optional[String] = Field(default=None, alias='blueprintId')
    model: typing.Optional[String] = Field(default=None)
    vendor: typing.Optional[String] = Field(default=None)
    address: typing.Optional[String] = Field(default=None)
    username: typing.Optional[String] = Field(default=None)
    password: typing.Optional[String] = Field(default=None)
    port: typing.Optional[Int] = Field(default=None)
    device_type: typing.Optional[String] = Field(default=None, alias='deviceType')
    device_size: typing.Optional[DeviceSize] = Field(default=None, alias='deviceSize')
    version: typing.Optional[String] = Field(default=None)
    label_ids: typing.Optional[list[String]] = Field(default=None, alias='labelIds')
    service_state: typing.Optional[DeviceServiceState] = Field(default=None, alias='serviceState')
    location_id: typing.Optional[String] = Field(default=None, alias='locationId')


class CSVImportInput(Input):
    zone_id: String = Field(alias='zoneId')
    file: Upload


class AddZoneInput(Input):
    name: String


class UpdateDataStoreInput(Input):
    config: String


class CommitConfigInput(Input):
    device_id: String = Field(alias='deviceId')
    should_dry_run: typing.Optional[Boolean] = Field(default=None, alias='shouldDryRun')


class AddSnapshotInput(Input):
    name: String
    device_id: String = Field(alias='deviceId')


class DeleteSnapshotInput(Input):
    device_id: String = Field(alias='deviceId')
    name: String
    transaction_id: String = Field(alias='transactionId')


class ApplySnapshotInput(Input):
    device_id: String = Field(alias='deviceId')
    name: String


class AddLocationInput(Input):
    name: String
    country_id: String = Field(alias='countryId')


class AddBlueprintInput(Input):
    name: String
    template: String


class UpdateBlueprintInput(Input):
    name: typing.Optional[String] = Field(default=None)
    template: typing.Optional[String] = Field(default=None)


class FilterTopologyInput(Input):
    labels: typing.Optional[list[String]] = Field(default=None)


class GraphNodeCoordinatesInput(Input):
    device_name: String = Field(alias='deviceName')
    x: Float
    y: Float


class CreateLabelInput(Input):
    name: String


class PageInfo(Payload):
    start_cursor: typing.Optional[Boolean] = Field(default=False, alias='startCursor')
    end_cursor: typing.Optional[Boolean] = Field(default=False, alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(default=False, alias='hasNextPage')
    has_previous_page: typing.Optional[Boolean] = Field(default=False, alias='hasPreviousPage')


class PageInfoPayload(BaseModel):
    start_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='startCursor')
    end_cursor: typing.Optional[typing.Optional[String]] = Field(default=None, alias='endCursor')
    has_next_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasNextPage')
    has_previous_page: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='hasPreviousPage')


class Device(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')
    model: typing.Optional[Boolean] = Field(default=False)
    vendor: typing.Optional[Boolean] = Field(default=False)
    port: typing.Optional[Boolean] = Field(default=False)
    address: typing.Optional[Boolean] = Field(default=False)
    mount_parameters: typing.Optional[Boolean] = Field(default=False, alias='mountParameters')
    source: typing.Optional[Boolean] = Field(default=False)
    service_state: typing.Optional[Boolean] = Field(default=False, alias='serviceState')
    is_installed: typing.Optional[Boolean] = Field(default=False, alias='isInstalled')
    zone: typing.Optional[Zone] = Field(default=None)
    labels: typing.Optional[LabelConnection] = Field(default=None)
    location: typing.Optional[Location] = Field(default=None)
    device_size: typing.Optional[Boolean] = Field(default=False, alias='deviceSize')
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class DevicePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')
    model: typing.Optional[typing.Optional[String]] = Field(default=None)
    vendor: typing.Optional[typing.Optional[String]] = Field(default=None)
    port: typing.Optional[typing.Optional[Int]] = Field(default=None)
    address: typing.Optional[typing.Optional[String]] = Field(default=None)
    mount_parameters: typing.Optional[typing.Optional[String]] = Field(default=None, alias='mountParameters')
    source: typing.Optional[typing.Optional[DeviceSource]] = Field(default=None)
    service_state: typing.Optional[typing.Optional[DeviceServiceState]] = Field(default=None, alias='serviceState')
    is_installed: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='isInstalled')
    zone: typing.Optional[ZonePayload] = Field(default=None)
    labels: typing.Optional[LabelConnectionPayload] = Field(default=None)
    location: typing.Optional[LocationPayload] = Field(default=None)
    device_size: typing.Optional[typing.Optional[DeviceSize]] = Field(default=None, alias='deviceSize')
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class DeviceEdge(Payload):
    node: typing.Optional[Device] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class DeviceEdgePayload(BaseModel):
    node: typing.Optional[DevicePayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class DeviceConnection(Payload):
    edges: typing.Optional[DeviceEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class DeviceConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[DeviceEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class AddDevicePayload(Payload):
    device: typing.Optional[Device] = Field(default=None)


class AddDevicePayloadPayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)


class UpdateDevicePayload(Payload):
    device: typing.Optional[Device] = Field(default=None)


class UpdateDevicePayloadPayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)


class UpdateDeviceMetadataPayload(Payload):
    devices: typing.Optional[Device] = Field(default=None)


class UpdateDeviceMetadataPayloadPayload(BaseModel):
    devices: typing.Optional[typing.Optional[list[DevicePayload]]] = Field(default=None)


class DeleteDevicePayload(Payload):
    device: typing.Optional[Device] = Field(default=None)


class DeleteDevicePayloadPayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)


class InstallDevicePayload(Payload):
    device: typing.Optional[Device] = Field(default=None)


class InstallDevicePayloadPayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)


class UninstallDevicePayload(Payload):
    device: typing.Optional[Device] = Field(default=None)


class UninstallDevicePayloadPayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)


class CSVImport(Payload):
    is_ok: typing.Optional[Boolean] = Field(default=False, alias='isOk')


class CSVImportPayload(BaseModel):
    is_ok: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='isOk')


class Zone(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')


class ZonePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')


class ZoneEdge(Payload):
    node: typing.Optional[Zone] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class ZoneEdgePayload(BaseModel):
    node: typing.Optional[ZonePayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class ZonesConnection(Payload):
    edges: typing.Optional[ZoneEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class ZonesConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[ZoneEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class AddZonePayload(Payload):
    zone: typing.Optional[Zone] = Field(default=None)


class AddZonePayloadPayload(BaseModel):
    zone: typing.Optional[ZonePayload] = Field(default=None)


class Snapshot(Payload):
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')


class SnapshotPayload(BaseModel):
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')


class DataStore(Payload):
    config: typing.Optional[Boolean] = Field(default=False)
    operational: typing.Optional[Boolean] = Field(default=False)
    snapshots: typing.Optional[Snapshot] = Field(default=None)


class DataStorePayload(BaseModel):
    config: typing.Optional[typing.Optional[String]] = Field(default=None)
    operational: typing.Optional[typing.Optional[String]] = Field(default=None)
    snapshots: typing.Optional[typing.Optional[list[SnapshotPayload]]] = Field(default=None)


class UpdateDataStorePayload(Payload):
    data_store: typing.Optional[DataStore] = Field(default=None, alias='dataStore')


class UpdateDataStorePayloadPayload(BaseModel):
    data_store: typing.Optional[DataStorePayload] = Field(default=None, alias='dataStore')


class CommitConfigOutput(Payload):
    device_id: typing.Optional[Boolean] = Field(default=False, alias='deviceId')
    message: typing.Optional[Boolean] = Field(default=False)
    configuration: typing.Optional[Boolean] = Field(default=False)


class CommitConfigOutputPayload(BaseModel):
    device_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceId')
    message: typing.Optional[typing.Optional[String]] = Field(default=None)
    configuration: typing.Optional[typing.Optional[String]] = Field(default=None)


class CommitConfigPayload(Payload):
    output: typing.Optional[CommitConfigOutput] = Field(default=None)


class CommitConfigPayloadPayload(BaseModel):
    output: typing.Optional[CommitConfigOutputPayload] = Field(default=None)


class ResetConfigPayload(Payload):
    data_store: typing.Optional[DataStore] = Field(default=None, alias='dataStore')


class ResetConfigPayloadPayload(BaseModel):
    data_store: typing.Optional[DataStorePayload] = Field(default=None, alias='dataStore')


class AddSnapshotPayload(Payload):
    snapshot: typing.Optional[Snapshot] = Field(default=None)


class AddSnapshotPayloadPayload(BaseModel):
    snapshot: typing.Optional[SnapshotPayload] = Field(default=None)


class DeleteSnapshotPayload(Payload):
    snapshot: typing.Optional[Snapshot] = Field(default=None)


class DeleteSnapshotPayloadPayload(BaseModel):
    snapshot: typing.Optional[SnapshotPayload] = Field(default=None)


class ApplySnapshotPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(default=False, alias='isOk')
    output: typing.Optional[Boolean] = Field(default=False)


class ApplySnapshotPayloadPayload(BaseModel):
    is_ok: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='isOk')
    output: typing.Optional[typing.Optional[String]] = Field(default=None)


class DiffData(Payload):
    path: typing.Optional[Boolean] = Field(default=False)
    data: typing.Optional[Boolean] = Field(default=False)


class DiffDataPayload(BaseModel):
    path: typing.Optional[typing.Optional[String]] = Field(default=None)
    data: typing.Optional[typing.Optional[String]] = Field(default=None)


class CalculatedUpdateDiffData(Payload):
    path: typing.Optional[Boolean] = Field(default=False)
    intended_data: typing.Optional[Boolean] = Field(default=False, alias='intendedData')
    actual_data: typing.Optional[Boolean] = Field(default=False, alias='actualData')


class CalculatedUpdateDiffDataPayload(BaseModel):
    path: typing.Optional[typing.Optional[String]] = Field(default=None)
    intended_data: typing.Optional[typing.Optional[String]] = Field(default=None, alias='intendedData')
    actual_data: typing.Optional[typing.Optional[String]] = Field(default=None, alias='actualData')


class CalculatedDiffResult(Payload):
    created_data: typing.Optional[DiffData] = Field(default=None, alias='createdData')
    deleted_data: typing.Optional[DiffData] = Field(default=None, alias='deletedData')
    updated_data: typing.Optional[CalculatedUpdateDiffData] = Field(default=None, alias='updatedData')


class CalculatedDiffResultPayload(BaseModel):
    created_data: typing.Optional[typing.Optional[list[DiffDataPayload]]] = Field(default=None, alias='createdData')
    deleted_data: typing.Optional[typing.Optional[list[DiffDataPayload]]] = Field(default=None, alias='deletedData')
    updated_data: typing.Optional[typing.Optional[list[CalculatedUpdateDiffDataPayload]]] = Field(default=None, alias='updatedData')


class CalculatedDiffPayload(Payload):
    result: typing.Optional[CalculatedDiffResult] = Field(default=None)


class CalculatedDiffPayloadPayload(BaseModel):
    result: typing.Optional[CalculatedDiffResultPayload] = Field(default=None)


class SyncFromNetworkPayload(Payload):
    data_store: typing.Optional[DataStore] = Field(default=None, alias='dataStore')


class SyncFromNetworkPayloadPayload(BaseModel):
    data_store: typing.Optional[DataStorePayload] = Field(default=None, alias='dataStore')


class Label(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')


class LabelPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')


class LabelEdge(Payload):
    node: typing.Optional[Label] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class LabelEdgePayload(BaseModel):
    node: typing.Optional[LabelPayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class LabelConnection(Payload):
    edges: typing.Optional[LabelEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class LabelConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[LabelEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class CreateLabelPayload(Payload):
    label: typing.Optional[Label] = Field(default=None)


class CreateLabelPayloadPayload(BaseModel):
    label: typing.Optional[LabelPayload] = Field(default=None)


class DeleteLabelPayload(Payload):
    label: typing.Optional[Label] = Field(default=None)


class DeleteLabelPayloadPayload(BaseModel):
    label: typing.Optional[LabelPayload] = Field(default=None)


class Location(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')
    country: typing.Optional[Boolean] = Field(default=False)


class LocationPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')
    country: typing.Optional[typing.Optional[String]] = Field(default=None)


class Country(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    code: typing.Optional[Boolean] = Field(default=False)


class CountryPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    code: typing.Optional[typing.Optional[String]] = Field(default=None)


class CountryEdge(Payload):
    node: typing.Optional[Country] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class CountryEdgePayload(BaseModel):
    node: typing.Optional[CountryPayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class CountryConnection(Payload):
    edges: typing.Optional[CountryEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class CountryConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[CountryEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class LocationEdge(Payload):
    node: typing.Optional[Location] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class LocationEdgePayload(BaseModel):
    node: typing.Optional[LocationPayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class LocationConnection(Payload):
    edges: typing.Optional[LocationEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class LocationConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[LocationEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class AddLocationPayload(Payload):
    location: typing.Optional[Location] = Field(default=None)


class AddLocationPayloadPayload(BaseModel):
    location: typing.Optional[LocationPayload] = Field(default=None)


class Blueprint(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    created_at: typing.Optional[Boolean] = Field(default=False, alias='createdAt')
    updated_at: typing.Optional[Boolean] = Field(default=False, alias='updatedAt')
    template: typing.Optional[Boolean] = Field(default=False)


class BlueprintPayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    created_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='createdAt')
    updated_at: typing.Optional[typing.Optional[String]] = Field(default=None, alias='updatedAt')
    template: typing.Optional[typing.Optional[String]] = Field(default=None)


class BlueprintEdge(Payload):
    node: typing.Optional[Blueprint] = Field(default=None)
    cursor: typing.Optional[Boolean] = Field(default=False)


class BlueprintEdgePayload(BaseModel):
    node: typing.Optional[BlueprintPayload] = Field(default=None)
    cursor: typing.Optional[typing.Optional[String]] = Field(default=None)


class BlueprintConnection(Payload):
    edges: typing.Optional[BlueprintEdge] = Field(default=None)
    page_info: typing.Optional[PageInfo] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(default=False, alias='totalCount')


class BlueprintConnectionPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[BlueprintEdgePayload]]] = Field(default=None)
    page_info: typing.Optional[PageInfoPayload] = Field(default=None, alias='pageInfo')
    total_count: typing.Optional[typing.Optional[Int]] = Field(default=None, alias='totalCount')


class AddBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class AddBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class UpdateBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class UpdateBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class DeleteBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(default=None)


class DeleteBlueprintPayloadPayload(BaseModel):
    blueprint: typing.Optional[BlueprintPayload] = Field(default=None)


class TransactionDiff(Payload):
    path: typing.Optional[Boolean] = Field(default=False)
    data_before: typing.Optional[Boolean] = Field(default=False, alias='dataBefore')
    data_after: typing.Optional[Boolean] = Field(default=False, alias='dataAfter')


class TransactionDiffPayload(BaseModel):
    path: typing.Optional[typing.Optional[String]] = Field(default=None)
    data_before: typing.Optional[typing.Optional[String]] = Field(default=None, alias='dataBefore')
    data_after: typing.Optional[typing.Optional[String]] = Field(default=None, alias='dataAfter')


class TransactionChange(Payload):
    device: typing.Optional[Device] = Field(default=None)
    diff: typing.Optional[TransactionDiff] = Field(default=None)


class TransactionChangePayload(BaseModel):
    device: typing.Optional[DevicePayload] = Field(default=None)
    diff: typing.Optional[typing.Optional[list[TransactionDiffPayload]]] = Field(default=None)


class Transaction(Payload):
    transaction_id: typing.Optional[Boolean] = Field(default=False, alias='transactionId')
    last_commit_time: typing.Optional[Boolean] = Field(default=False, alias='lastCommitTime')
    changes: typing.Optional[TransactionChange] = Field(default=None)


class TransactionPayload(BaseModel):
    transaction_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='transactionId')
    last_commit_time: typing.Optional[typing.Optional[String]] = Field(default=None, alias='lastCommitTime')
    changes: typing.Optional[typing.Optional[list[TransactionChangePayload]]] = Field(default=None)


class CreateTransactionPayload(Payload):
    transaction_id: typing.Optional[Boolean] = Field(default=False, alias='transactionId')


class CreateTransactionPayloadPayload(BaseModel):
    transaction_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='transactionId')


class CloseTransactionPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(default=False, alias='isOk')


class CloseTransactionPayloadPayload(BaseModel):
    is_ok: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='isOk')


class RevertChangesPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(default=False, alias='isOk')


class RevertChangesPayloadPayload(BaseModel):
    is_ok: typing.Optional[typing.Optional[Boolean]] = Field(default=None, alias='isOk')


class GraphNodeInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    status: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)


class GraphNodeInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[String]] = Field(default=None)
    status: typing.Optional[typing.Optional[GraphEdgeStatus]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)


class GraphNodeCoordinates(Payload):
    x: typing.Optional[Boolean] = Field(default=False)
    y: typing.Optional[Boolean] = Field(default=False)


class GraphNodeCoordinatesPayload(BaseModel):
    x: typing.Optional[typing.Optional[Float]] = Field(default=None)
    y: typing.Optional[typing.Optional[Float]] = Field(default=None)


class GraphNode(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    interfaces: typing.Optional[GraphNodeInterface] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)
    device_type: typing.Optional[Boolean] = Field(default=False, alias='deviceType')
    software_version: typing.Optional[Boolean] = Field(default=False, alias='softwareVersion')
    device: typing.Optional[Device] = Field(default=None)


class GraphNodePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    interfaces: typing.Optional[typing.Optional[list[GraphNodeInterfacePayload]]] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinatesPayload] = Field(default=None)
    device_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceType')
    software_version: typing.Optional[typing.Optional[String]] = Field(default=None, alias='softwareVersion')
    device: typing.Optional[DevicePayload] = Field(default=None)


class EdgeSourceTarget(Payload):
    node_id: typing.Optional[Boolean] = Field(default=False, alias='nodeId')
    interface: typing.Optional[Boolean] = Field(default=False)


class EdgeSourceTargetPayload(BaseModel):
    node_id: typing.Optional[typing.Optional[String]] = Field(default=None, alias='nodeId')
    interface: typing.Optional[typing.Optional[String]] = Field(default=None)


class GraphEdge(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    source: typing.Optional[EdgeSourceTarget] = Field(default=None)
    target: typing.Optional[EdgeSourceTarget] = Field(default=None)


class GraphEdgePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    source: typing.Optional[EdgeSourceTargetPayload] = Field(default=None)
    target: typing.Optional[EdgeSourceTargetPayload] = Field(default=None)


class Topology(Payload):
    nodes: typing.Optional[GraphNode] = Field(default=None)
    edges: typing.Optional[GraphEdge] = Field(default=None)


class TopologyPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[GraphNodePayload]]] = Field(default=None)
    edges: typing.Optional[typing.Optional[list[GraphEdgePayload]]] = Field(default=None)


class GraphVersionEdge(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    source: typing.Optional[EdgeSourceTarget] = Field(default=None)
    target: typing.Optional[EdgeSourceTarget] = Field(default=None)


class GraphVersionEdgePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    source: typing.Optional[EdgeSourceTargetPayload] = Field(default=None)
    target: typing.Optional[EdgeSourceTargetPayload] = Field(default=None)


class TopologyVersionData(Payload):
    nodes: typing.Optional[GraphVersionNode] = Field(default=None)
    edges: typing.Optional[GraphVersionEdge] = Field(default=None)


class TopologyVersionDataPayload(BaseModel):
    nodes: typing.Optional[typing.Optional[list[GraphVersionNodePayload]]] = Field(default=None)
    edges: typing.Optional[typing.Optional[list[GraphVersionEdgePayload]]] = Field(default=None)


class TopologyCommonNodes(Payload):
    common_nodes: typing.Optional[Boolean] = Field(default=False, alias='commonNodes')


class TopologyCommonNodesPayload(BaseModel):
    common_nodes: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='commonNodes')


class UpdateGraphNodeCoordinatesPayload(Payload):
    device_names: typing.Optional[Boolean] = Field(default=False, alias='deviceNames')


class UpdateGraphNodeCoordinatesPayloadPayload(BaseModel):
    device_names: typing.Optional[typing.Optional[list[typing.Optional[String]]]] = Field(default=None, alias='deviceNames')


class NetInterface(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)


class NetInterfacePayload(BaseModel):
    id: typing.Optional[typing.Optional[String]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)


class NetNetwork(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    subnet: typing.Optional[Boolean] = Field(default=False)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)


class NetNetworkPayload(BaseModel):
    id: typing.Optional[typing.Optional[String]] = Field(default=None)
    subnet: typing.Optional[typing.Optional[String]] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinatesPayload] = Field(default=None)


class NetNode(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    name: typing.Optional[Boolean] = Field(default=False)
    interfaces: typing.Optional[NetInterface] = Field(default=None)
    networks: typing.Optional[NetNetwork] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)


class NetNodePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    name: typing.Optional[typing.Optional[String]] = Field(default=None)
    interfaces: typing.Optional[typing.Optional[list[NetInterfacePayload]]] = Field(default=None)
    networks: typing.Optional[typing.Optional[list[NetNetworkPayload]]] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinatesPayload] = Field(default=None)


class NetTopology(Payload):
    edges: typing.Optional[GraphEdge] = Field(default=None)
    nodes: typing.Optional[NetNode] = Field(default=None)


class NetTopologyPayload(BaseModel):
    edges: typing.Optional[typing.Optional[list[GraphEdgePayload]]] = Field(default=None)
    nodes: typing.Optional[typing.Optional[list[NetNodePayload]]] = Field(default=None)


class GraphVersionNode(Payload):
    id: typing.Optional[Boolean] = Field(default=False)
    interfaces: typing.Optional[GraphNodeInterface] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(default=None)
    device_type: typing.Optional[Boolean] = Field(default=False, alias='deviceType')
    software_version: typing.Optional[Boolean] = Field(default=False, alias='softwareVersion')
    name: typing.Optional[Boolean] = Field(default=False)


class GraphVersionNodePayload(BaseModel):
    id: typing.Optional[typing.Optional[ID]] = Field(default=None)
    interfaces: typing.Optional[typing.Optional[list[GraphNodeInterfacePayload]]] = Field(default=None)
    coordinates: typing.Optional[GraphNodeCoordinatesPayload] = Field(default=None)
    device_type: typing.Optional[typing.Optional[String]] = Field(default=None, alias='deviceType')
    software_version: typing.Optional[typing.Optional[String]] = Field(default=None, alias='softwareVersion')
    name: typing.Optional[typing.Optional[String]] = Field(default=None)


class NodeQuery(Query):
    _name: str = PrivateAttr('node')
    id: ID = Field(json_schema_extra={'type': 'ID!'})
    payload: Node


class DevicesQuery(Query):
    _name: str = PrivateAttr('devices')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    filter: typing.Optional[FilterDevicesInput] = Field(default=None, json_schema_extra={'type': 'FilterDevicesInput'})
    order_by: typing.Optional[DeviceOrderByInput] = Field(default=None, alias='orderBy', json_schema_extra={'type': 'DeviceOrderByInput'})
    payload: DeviceConnection


class UniconfigShellSessionQuery(Query):
    _name: str = PrivateAttr('uniconfigShellSession')


class ZonesQuery(Query):
    _name: str = PrivateAttr('zones')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: ZonesConnection


class DataStoreQuery(Query):
    _name: str = PrivateAttr('dataStore')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: DataStore


class CalculatedDiffQuery(Query):
    _name: str = PrivateAttr('calculatedDiff')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: CalculatedDiffPayload


class LabelsQuery(Query):
    _name: str = PrivateAttr('labels')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: LabelConnection


class CountriesQuery(Query):
    _name: str = PrivateAttr('countries')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: CountryConnection


class LocationsQuery(Query):
    _name: str = PrivateAttr('locations')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: LocationConnection


class BlueprintsQuery(Query):
    _name: str = PrivateAttr('blueprints')
    first: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    after: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    last: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    before: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    payload: BlueprintConnection


class TransactionsQuery(Query):
    _name: str = PrivateAttr('transactions')


class TopologyQuery(Query):
    _name: str = PrivateAttr('topology')
    filter: typing.Optional[FilterTopologyInput] = Field(default=None, json_schema_extra={'type': 'FilterTopologyInput'})
    payload: Topology


class TopologyVersionsQuery(Query):
    _name: str = PrivateAttr('topologyVersions')


class TopologyCommonNodesQuery(Query):
    _name: str = PrivateAttr('topologyCommonNodes')
    nodes: typing.Optional[list[String]] = Field(default=None, json_schema_extra={'type': '[String!]!'})
    payload: TopologyCommonNodes


class TopologyVersionDataQuery(Query):
    _name: str = PrivateAttr('topologyVersionData')
    version: String = Field(json_schema_extra={'type': 'String!'})
    payload: TopologyVersionData


class NetTopologyQuery(Query):
    _name: str = PrivateAttr('netTopology')


class NodeQueryResponse(BaseModel):
    data: typing.Optional[Node] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DevicesQueryResponse(BaseModel):
    data: typing.Optional[DevicesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DevicesData(BaseModel):
    devices: DeviceConnectionPayload


class ZonesQueryResponse(BaseModel):
    data: typing.Optional[ZonesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ZonesData(BaseModel):
    zones: ZonesConnectionPayload


class DataStoreQueryResponse(BaseModel):
    data: typing.Optional[DataStoreData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DataStoreData(BaseModel):
    data_store: typing.Optional[DataStorePayload] = Field(alias='dataStore')


class CalculatedDiffQueryResponse(BaseModel):
    data: typing.Optional[CalculatedDiffData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CalculatedDiffData(BaseModel):
    calculated_diff: CalculatedDiffPayloadPayload = Field(alias='calculatedDiff')


class LabelsQueryResponse(BaseModel):
    data: typing.Optional[LabelsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class LabelsData(BaseModel):
    labels: LabelConnectionPayload


class CountriesQueryResponse(BaseModel):
    data: typing.Optional[CountriesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CountriesData(BaseModel):
    countries: CountryConnectionPayload


class LocationsQueryResponse(BaseModel):
    data: typing.Optional[LocationsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class LocationsData(BaseModel):
    locations: LocationConnectionPayload


class BlueprintsQueryResponse(BaseModel):
    data: typing.Optional[BlueprintsData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class BlueprintsData(BaseModel):
    blueprints: BlueprintConnectionPayload


class TopologyQueryResponse(BaseModel):
    data: typing.Optional[TopologyData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TopologyData(BaseModel):
    topology: typing.Optional[TopologyPayload]


class TopologyCommonNodesQueryResponse(BaseModel):
    data: typing.Optional[TopologyCommonNodesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TopologyCommonNodesData(BaseModel):
    topology_common_nodes: typing.Optional[TopologyCommonNodesPayload] = Field(alias='topologyCommonNodes')


class TopologyVersionDataQueryResponse(BaseModel):
    data: typing.Optional[TopologyVersionDataData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class TopologyVersionDataData(BaseModel):
    topology_version_data: TopologyVersionDataPayload = Field(alias='topologyVersionData')


class AddDeviceMutation(Mutation):
    _name: str = PrivateAttr('addDevice')
    input: AddDeviceInput = Field(json_schema_extra={'type': 'AddDeviceInput!'})
    payload: AddDevicePayload


class UpdateDeviceMutation(Mutation):
    _name: str = PrivateAttr('updateDevice')
    id: String = Field(json_schema_extra={'type': 'String!'})
    input: UpdateDeviceInput = Field(json_schema_extra={'type': 'UpdateDeviceInput!'})
    payload: UpdateDevicePayload


class DeleteDeviceMutation(Mutation):
    _name: str = PrivateAttr('deleteDevice')
    id: String = Field(json_schema_extra={'type': 'String!'})
    payload: DeleteDevicePayload


class InstallDeviceMutation(Mutation):
    _name: str = PrivateAttr('installDevice')
    id: String = Field(json_schema_extra={'type': 'String!'})
    payload: InstallDevicePayload


class UninstallDeviceMutation(Mutation):
    _name: str = PrivateAttr('uninstallDevice')
    id: String = Field(json_schema_extra={'type': 'String!'})
    payload: UninstallDevicePayload


class ImportCSVMutation(Mutation):
    _name: str = PrivateAttr('importCSV')
    input: CSVImportInput = Field(json_schema_extra={'type': 'CSVImportInput!'})
    payload: CSVImport


class AddZoneMutation(Mutation):
    _name: str = PrivateAttr('addZone')
    input: AddZoneInput = Field(json_schema_extra={'type': 'AddZoneInput!'})
    payload: AddZonePayload


class UpdateDataStoreMutation(Mutation):
    _name: str = PrivateAttr('updateDataStore')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    input: UpdateDataStoreInput = Field(json_schema_extra={'type': 'UpdateDataStoreInput!'})
    payload: UpdateDataStorePayload


class CommitConfigMutation(Mutation):
    _name: str = PrivateAttr('commitConfig')
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    input: CommitConfigInput = Field(json_schema_extra={'type': 'CommitConfigInput!'})
    payload: CommitConfigPayload


class ResetConfigMutation(Mutation):
    _name: str = PrivateAttr('resetConfig')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: ResetConfigPayload


class AddSnapshotMutation(Mutation):
    _name: str = PrivateAttr('addSnapshot')
    input: AddSnapshotInput = Field(json_schema_extra={'type': 'AddSnapshotInput!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: AddSnapshotPayload


class DeleteSnapshotMutation(Mutation):
    _name: str = PrivateAttr('deleteSnapshot')
    input: DeleteSnapshotInput = Field(json_schema_extra={'type': 'DeleteSnapshotInput!'})
    payload: DeleteSnapshotPayload


class ApplySnapshotMutation(Mutation):
    _name: str = PrivateAttr('applySnapshot')
    input: ApplySnapshotInput = Field(json_schema_extra={'type': 'ApplySnapshotInput!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: ApplySnapshotPayload


class SyncFromNetworkMutation(Mutation):
    _name: str = PrivateAttr('syncFromNetwork')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: SyncFromNetworkPayload


class CreateLabelMutation(Mutation):
    _name: str = PrivateAttr('createLabel')
    input: CreateLabelInput = Field(json_schema_extra={'type': 'CreateLabelInput!'})
    payload: CreateLabelPayload


class DeleteLabelMutation(Mutation):
    _name: str = PrivateAttr('deleteLabel')
    id: String = Field(json_schema_extra={'type': 'String!'})
    payload: DeleteLabelPayload


class AddLocationMutation(Mutation):
    _name: str = PrivateAttr('addLocation')
    input: AddLocationInput = Field(json_schema_extra={'type': 'AddLocationInput!'})
    payload: AddLocationPayload


class AddBlueprintMutation(Mutation):
    _name: str = PrivateAttr('addBlueprint')
    input: AddBlueprintInput = Field(json_schema_extra={'type': 'AddBlueprintInput!'})
    payload: AddBlueprintPayload


class UpdateBlueprintMutation(Mutation):
    _name: str = PrivateAttr('updateBlueprint')
    id: String = Field(json_schema_extra={'type': 'String!'})
    input: UpdateBlueprintInput = Field(json_schema_extra={'type': 'UpdateBlueprintInput!'})
    payload: UpdateBlueprintPayload


class DeleteBlueprintMutation(Mutation):
    _name: str = PrivateAttr('deleteBlueprint')
    id: String = Field(json_schema_extra={'type': 'String!'})
    payload: DeleteBlueprintPayload


class CreateTransactionMutation(Mutation):
    _name: str = PrivateAttr('createTransaction')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    payload: CreateTransactionPayload


class CloseTransactionMutation(Mutation):
    _name: str = PrivateAttr('closeTransaction')
    device_id: String = Field(alias='deviceId', json_schema_extra={'type': 'String!'})
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: CloseTransactionPayload


class RevertChangesMutation(Mutation):
    _name: str = PrivateAttr('revertChanges')
    transaction_id: String = Field(alias='transactionId', json_schema_extra={'type': 'String!'})
    payload: RevertChangesPayload


class UpdateGraphNodeCoordinatesMutation(Mutation):
    _name: str = PrivateAttr('updateGraphNodeCoordinates')
    input: typing.Optional[list[GraphNodeCoordinatesInput]] = Field(default=None, json_schema_extra={'type': '[GraphNodeCoordinatesInput!]!'})
    payload: UpdateGraphNodeCoordinatesPayload


class AddDeviceMutationResponse(BaseModel):
    data: typing.Optional[AddDeviceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddDeviceData(BaseModel):
    add_device: AddDevicePayloadPayload = Field(alias='addDevice')


class UpdateDeviceMutationResponse(BaseModel):
    data: typing.Optional[UpdateDeviceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateDeviceData(BaseModel):
    update_device: UpdateDevicePayloadPayload = Field(alias='updateDevice')


class DeleteDeviceMutationResponse(BaseModel):
    data: typing.Optional[DeleteDeviceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteDeviceData(BaseModel):
    delete_device: DeleteDevicePayloadPayload = Field(alias='deleteDevice')


class InstallDeviceMutationResponse(BaseModel):
    data: typing.Optional[InstallDeviceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class InstallDeviceData(BaseModel):
    install_device: InstallDevicePayloadPayload = Field(alias='installDevice')


class UninstallDeviceMutationResponse(BaseModel):
    data: typing.Optional[UninstallDeviceData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UninstallDeviceData(BaseModel):
    uninstall_device: UninstallDevicePayloadPayload = Field(alias='uninstallDevice')


class ImportCSVMutationResponse(BaseModel):
    data: typing.Optional[ImportCSVData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ImportCSVData(BaseModel):
    import_csv: typing.Optional[CSVImportPayload] = Field(alias='importCSV')


class AddZoneMutationResponse(BaseModel):
    data: typing.Optional[AddZoneData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddZoneData(BaseModel):
    add_zone: AddZonePayloadPayload = Field(alias='addZone')


class UpdateDataStoreMutationResponse(BaseModel):
    data: typing.Optional[UpdateDataStoreData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateDataStoreData(BaseModel):
    update_data_store: UpdateDataStorePayloadPayload = Field(alias='updateDataStore')


class CommitConfigMutationResponse(BaseModel):
    data: typing.Optional[CommitConfigData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CommitConfigData(BaseModel):
    commit_config: CommitConfigPayloadPayload = Field(alias='commitConfig')


class ResetConfigMutationResponse(BaseModel):
    data: typing.Optional[ResetConfigData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ResetConfigData(BaseModel):
    reset_config: ResetConfigPayloadPayload = Field(alias='resetConfig')


class AddSnapshotMutationResponse(BaseModel):
    data: typing.Optional[AddSnapshotData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddSnapshotData(BaseModel):
    add_snapshot: typing.Optional[AddSnapshotPayloadPayload] = Field(alias='addSnapshot')


class DeleteSnapshotMutationResponse(BaseModel):
    data: typing.Optional[DeleteSnapshotData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteSnapshotData(BaseModel):
    delete_snapshot: typing.Optional[DeleteSnapshotPayloadPayload] = Field(alias='deleteSnapshot')


class ApplySnapshotMutationResponse(BaseModel):
    data: typing.Optional[ApplySnapshotData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class ApplySnapshotData(BaseModel):
    apply_snapshot: ApplySnapshotPayloadPayload = Field(alias='applySnapshot')


class SyncFromNetworkMutationResponse(BaseModel):
    data: typing.Optional[SyncFromNetworkData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class SyncFromNetworkData(BaseModel):
    sync_from_network: SyncFromNetworkPayloadPayload = Field(alias='syncFromNetwork')


class CreateLabelMutationResponse(BaseModel):
    data: typing.Optional[CreateLabelData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateLabelData(BaseModel):
    create_label: CreateLabelPayloadPayload = Field(alias='createLabel')


class DeleteLabelMutationResponse(BaseModel):
    data: typing.Optional[DeleteLabelData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteLabelData(BaseModel):
    delete_label: DeleteLabelPayloadPayload = Field(alias='deleteLabel')


class AddLocationMutationResponse(BaseModel):
    data: typing.Optional[AddLocationData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddLocationData(BaseModel):
    add_location: AddLocationPayloadPayload = Field(alias='addLocation')


class AddBlueprintMutationResponse(BaseModel):
    data: typing.Optional[AddBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class AddBlueprintData(BaseModel):
    add_blueprint: AddBlueprintPayloadPayload = Field(alias='addBlueprint')


class UpdateBlueprintMutationResponse(BaseModel):
    data: typing.Optional[UpdateBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateBlueprintData(BaseModel):
    update_blueprint: UpdateBlueprintPayloadPayload = Field(alias='updateBlueprint')


class DeleteBlueprintMutationResponse(BaseModel):
    data: typing.Optional[DeleteBlueprintData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class DeleteBlueprintData(BaseModel):
    delete_blueprint: DeleteBlueprintPayloadPayload = Field(alias='deleteBlueprint')


class CreateTransactionMutationResponse(BaseModel):
    data: typing.Optional[CreateTransactionData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CreateTransactionData(BaseModel):
    create_transaction: CreateTransactionPayloadPayload = Field(alias='createTransaction')


class CloseTransactionMutationResponse(BaseModel):
    data: typing.Optional[CloseTransactionData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class CloseTransactionData(BaseModel):
    close_transaction: CloseTransactionPayloadPayload = Field(alias='closeTransaction')


class RevertChangesMutationResponse(BaseModel):
    data: typing.Optional[RevertChangesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class RevertChangesData(BaseModel):
    revert_changes: RevertChangesPayloadPayload = Field(alias='revertChanges')


class UpdateGraphNodeCoordinatesMutationResponse(BaseModel):
    data: typing.Optional[UpdateGraphNodeCoordinatesData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UpdateGraphNodeCoordinatesData(BaseModel):
    update_graph_node_coordinates: UpdateGraphNodeCoordinatesPayloadPayload = Field(alias='updateGraphNodeCoordinates')


class UniconfigShellSubscription(Subscription):
    _name: str = PrivateAttr('uniconfigShell')
    input: typing.Optional[String] = Field(default=None, json_schema_extra={'type': 'String'})
    trigger: typing.Optional[Int] = Field(default=None, json_schema_extra={'type': 'Int'})
    session_id: String = Field(alias='sessionId', json_schema_extra={'type': 'String!'})
    payload: Boolean


class UniconfigShellSubscriptionResponse(BaseModel):
    data: typing.Optional[UniconfigShellData] = Field(default=None)
    errors: typing.Optional[typing.Any] = Field(default=None)


class UniconfigShellData(BaseModel):
    uniconfig_shell: typing.Optional[typing.Optional[String]] = Field(alias='uniconfigShell')


Node.model_rebuild()
BaseGraphNode.model_rebuild()
FilterDevicesInput.model_rebuild()
DeviceOrderByInput.model_rebuild()
AddDeviceInput.model_rebuild()
UpdateDeviceInput.model_rebuild()
CSVImportInput.model_rebuild()
AddZoneInput.model_rebuild()
UpdateDataStoreInput.model_rebuild()
CommitConfigInput.model_rebuild()
AddSnapshotInput.model_rebuild()
DeleteSnapshotInput.model_rebuild()
ApplySnapshotInput.model_rebuild()
AddLocationInput.model_rebuild()
AddBlueprintInput.model_rebuild()
UpdateBlueprintInput.model_rebuild()
FilterTopologyInput.model_rebuild()
GraphNodeCoordinatesInput.model_rebuild()
CreateLabelInput.model_rebuild()
PageInfo.model_rebuild()
PageInfoPayload.model_rebuild()
Device.model_rebuild()
DevicePayload.model_rebuild()
DeviceEdge.model_rebuild()
DeviceEdgePayload.model_rebuild()
DeviceConnection.model_rebuild()
DeviceConnectionPayload.model_rebuild()
AddDevicePayload.model_rebuild()
AddDevicePayloadPayload.model_rebuild()
UpdateDevicePayload.model_rebuild()
UpdateDevicePayloadPayload.model_rebuild()
UpdateDeviceMetadataPayload.model_rebuild()
UpdateDeviceMetadataPayloadPayload.model_rebuild()
DeleteDevicePayload.model_rebuild()
DeleteDevicePayloadPayload.model_rebuild()
InstallDevicePayload.model_rebuild()
InstallDevicePayloadPayload.model_rebuild()
UninstallDevicePayload.model_rebuild()
UninstallDevicePayloadPayload.model_rebuild()
CSVImport.model_rebuild()
CSVImportPayload.model_rebuild()
Zone.model_rebuild()
ZonePayload.model_rebuild()
ZoneEdge.model_rebuild()
ZoneEdgePayload.model_rebuild()
ZonesConnection.model_rebuild()
ZonesConnectionPayload.model_rebuild()
AddZonePayload.model_rebuild()
AddZonePayloadPayload.model_rebuild()
Snapshot.model_rebuild()
SnapshotPayload.model_rebuild()
DataStore.model_rebuild()
DataStorePayload.model_rebuild()
UpdateDataStorePayload.model_rebuild()
UpdateDataStorePayloadPayload.model_rebuild()
CommitConfigOutput.model_rebuild()
CommitConfigOutputPayload.model_rebuild()
CommitConfigPayload.model_rebuild()
CommitConfigPayloadPayload.model_rebuild()
ResetConfigPayload.model_rebuild()
ResetConfigPayloadPayload.model_rebuild()
AddSnapshotPayload.model_rebuild()
AddSnapshotPayloadPayload.model_rebuild()
DeleteSnapshotPayload.model_rebuild()
DeleteSnapshotPayloadPayload.model_rebuild()
ApplySnapshotPayload.model_rebuild()
ApplySnapshotPayloadPayload.model_rebuild()
DiffData.model_rebuild()
DiffDataPayload.model_rebuild()
CalculatedUpdateDiffData.model_rebuild()
CalculatedUpdateDiffDataPayload.model_rebuild()
CalculatedDiffResult.model_rebuild()
CalculatedDiffResultPayload.model_rebuild()
CalculatedDiffPayload.model_rebuild()
CalculatedDiffPayloadPayload.model_rebuild()
SyncFromNetworkPayload.model_rebuild()
SyncFromNetworkPayloadPayload.model_rebuild()
Label.model_rebuild()
LabelPayload.model_rebuild()
LabelEdge.model_rebuild()
LabelEdgePayload.model_rebuild()
LabelConnection.model_rebuild()
LabelConnectionPayload.model_rebuild()
CreateLabelPayload.model_rebuild()
CreateLabelPayloadPayload.model_rebuild()
DeleteLabelPayload.model_rebuild()
DeleteLabelPayloadPayload.model_rebuild()
Location.model_rebuild()
LocationPayload.model_rebuild()
Country.model_rebuild()
CountryPayload.model_rebuild()
CountryEdge.model_rebuild()
CountryEdgePayload.model_rebuild()
CountryConnection.model_rebuild()
CountryConnectionPayload.model_rebuild()
LocationEdge.model_rebuild()
LocationEdgePayload.model_rebuild()
LocationConnection.model_rebuild()
LocationConnectionPayload.model_rebuild()
AddLocationPayload.model_rebuild()
AddLocationPayloadPayload.model_rebuild()
Blueprint.model_rebuild()
BlueprintPayload.model_rebuild()
BlueprintEdge.model_rebuild()
BlueprintEdgePayload.model_rebuild()
BlueprintConnection.model_rebuild()
BlueprintConnectionPayload.model_rebuild()
AddBlueprintPayload.model_rebuild()
AddBlueprintPayloadPayload.model_rebuild()
UpdateBlueprintPayload.model_rebuild()
UpdateBlueprintPayloadPayload.model_rebuild()
DeleteBlueprintPayload.model_rebuild()
DeleteBlueprintPayloadPayload.model_rebuild()
TransactionDiff.model_rebuild()
TransactionDiffPayload.model_rebuild()
TransactionChange.model_rebuild()
TransactionChangePayload.model_rebuild()
Transaction.model_rebuild()
TransactionPayload.model_rebuild()
CreateTransactionPayload.model_rebuild()
CreateTransactionPayloadPayload.model_rebuild()
CloseTransactionPayload.model_rebuild()
CloseTransactionPayloadPayload.model_rebuild()
RevertChangesPayload.model_rebuild()
RevertChangesPayloadPayload.model_rebuild()
GraphNodeInterface.model_rebuild()
GraphNodeInterfacePayload.model_rebuild()
GraphNodeCoordinates.model_rebuild()
GraphNodeCoordinatesPayload.model_rebuild()
GraphNode.model_rebuild()
GraphNodePayload.model_rebuild()
EdgeSourceTarget.model_rebuild()
EdgeSourceTargetPayload.model_rebuild()
GraphEdge.model_rebuild()
GraphEdgePayload.model_rebuild()
Topology.model_rebuild()
TopologyPayload.model_rebuild()
GraphVersionEdge.model_rebuild()
GraphVersionEdgePayload.model_rebuild()
TopologyVersionData.model_rebuild()
TopologyVersionDataPayload.model_rebuild()
TopologyCommonNodes.model_rebuild()
TopologyCommonNodesPayload.model_rebuild()
UpdateGraphNodeCoordinatesPayload.model_rebuild()
UpdateGraphNodeCoordinatesPayloadPayload.model_rebuild()
NetInterface.model_rebuild()
NetInterfacePayload.model_rebuild()
NetNetwork.model_rebuild()
NetNetworkPayload.model_rebuild()
NetNode.model_rebuild()
NetNodePayload.model_rebuild()
NetTopology.model_rebuild()
NetTopologyPayload.model_rebuild()
GraphVersionNode.model_rebuild()
GraphVersionNodePayload.model_rebuild()
NodeQuery.model_rebuild()
DevicesQuery.model_rebuild()
UniconfigShellSessionQuery.model_rebuild()
ZonesQuery.model_rebuild()
DataStoreQuery.model_rebuild()
CalculatedDiffQuery.model_rebuild()
LabelsQuery.model_rebuild()
CountriesQuery.model_rebuild()
LocationsQuery.model_rebuild()
BlueprintsQuery.model_rebuild()
TransactionsQuery.model_rebuild()
TopologyQuery.model_rebuild()
TopologyVersionsQuery.model_rebuild()
TopologyCommonNodesQuery.model_rebuild()
TopologyVersionDataQuery.model_rebuild()
NetTopologyQuery.model_rebuild()
NodeQueryResponse.model_rebuild()
DevicesQueryResponse.model_rebuild()
DevicesData.model_rebuild()
ZonesQueryResponse.model_rebuild()
ZonesData.model_rebuild()
DataStoreQueryResponse.model_rebuild()
DataStoreData.model_rebuild()
CalculatedDiffQueryResponse.model_rebuild()
CalculatedDiffData.model_rebuild()
LabelsQueryResponse.model_rebuild()
LabelsData.model_rebuild()
CountriesQueryResponse.model_rebuild()
CountriesData.model_rebuild()
LocationsQueryResponse.model_rebuild()
LocationsData.model_rebuild()
BlueprintsQueryResponse.model_rebuild()
BlueprintsData.model_rebuild()
TopologyQueryResponse.model_rebuild()
TopologyData.model_rebuild()
TopologyCommonNodesQueryResponse.model_rebuild()
TopologyCommonNodesData.model_rebuild()
TopologyVersionDataQueryResponse.model_rebuild()
TopologyVersionDataData.model_rebuild()
AddDeviceMutation.model_rebuild()
UpdateDeviceMutation.model_rebuild()
DeleteDeviceMutation.model_rebuild()
InstallDeviceMutation.model_rebuild()
UninstallDeviceMutation.model_rebuild()
ImportCSVMutation.model_rebuild()
AddZoneMutation.model_rebuild()
UpdateDataStoreMutation.model_rebuild()
CommitConfigMutation.model_rebuild()
ResetConfigMutation.model_rebuild()
AddSnapshotMutation.model_rebuild()
DeleteSnapshotMutation.model_rebuild()
ApplySnapshotMutation.model_rebuild()
SyncFromNetworkMutation.model_rebuild()
CreateLabelMutation.model_rebuild()
DeleteLabelMutation.model_rebuild()
AddLocationMutation.model_rebuild()
AddBlueprintMutation.model_rebuild()
UpdateBlueprintMutation.model_rebuild()
DeleteBlueprintMutation.model_rebuild()
CreateTransactionMutation.model_rebuild()
CloseTransactionMutation.model_rebuild()
RevertChangesMutation.model_rebuild()
UpdateGraphNodeCoordinatesMutation.model_rebuild()
AddDeviceMutationResponse.model_rebuild()
AddDeviceData.model_rebuild()
UpdateDeviceMutationResponse.model_rebuild()
UpdateDeviceData.model_rebuild()
DeleteDeviceMutationResponse.model_rebuild()
DeleteDeviceData.model_rebuild()
InstallDeviceMutationResponse.model_rebuild()
InstallDeviceData.model_rebuild()
UninstallDeviceMutationResponse.model_rebuild()
UninstallDeviceData.model_rebuild()
ImportCSVMutationResponse.model_rebuild()
ImportCSVData.model_rebuild()
AddZoneMutationResponse.model_rebuild()
AddZoneData.model_rebuild()
UpdateDataStoreMutationResponse.model_rebuild()
UpdateDataStoreData.model_rebuild()
CommitConfigMutationResponse.model_rebuild()
CommitConfigData.model_rebuild()
ResetConfigMutationResponse.model_rebuild()
ResetConfigData.model_rebuild()
AddSnapshotMutationResponse.model_rebuild()
AddSnapshotData.model_rebuild()
DeleteSnapshotMutationResponse.model_rebuild()
DeleteSnapshotData.model_rebuild()
ApplySnapshotMutationResponse.model_rebuild()
ApplySnapshotData.model_rebuild()
SyncFromNetworkMutationResponse.model_rebuild()
SyncFromNetworkData.model_rebuild()
CreateLabelMutationResponse.model_rebuild()
CreateLabelData.model_rebuild()
DeleteLabelMutationResponse.model_rebuild()
DeleteLabelData.model_rebuild()
AddLocationMutationResponse.model_rebuild()
AddLocationData.model_rebuild()
AddBlueprintMutationResponse.model_rebuild()
AddBlueprintData.model_rebuild()
UpdateBlueprintMutationResponse.model_rebuild()
UpdateBlueprintData.model_rebuild()
DeleteBlueprintMutationResponse.model_rebuild()
DeleteBlueprintData.model_rebuild()
CreateTransactionMutationResponse.model_rebuild()
CreateTransactionData.model_rebuild()
CloseTransactionMutationResponse.model_rebuild()
CloseTransactionData.model_rebuild()
RevertChangesMutationResponse.model_rebuild()
RevertChangesData.model_rebuild()
UpdateGraphNodeCoordinatesMutationResponse.model_rebuild()
UpdateGraphNodeCoordinatesData.model_rebuild()
UniconfigShellSubscription.model_rebuild()
UniconfigShellSubscriptionResponse.model_rebuild()
UniconfigShellData.model_rebuild()

from __future__ import annotations

from typing import Any

from . import OperationsAddKeystoreEntryPostRequest
from . import OperationsAddPrivateKeyPostRequest
from . import OperationsAddTrustedCertificatePostRequest
from . import OperationsApplyTemplatePostRequest
from . import OperationsBulkEditPostRequest
from . import OperationsBulkGetPostRequest
from . import OperationsBulkGetPostResponse
from . import OperationsCalculateDiffPostRequest
from . import OperationsCalculateDiffPostResponse
from . import OperationsCalculateGitLikeDiffPostRequest
from . import OperationsCalculateGitLikeDiffPostResponse
from . import OperationsCalculateSubtreeDiffPostRequest
from . import OperationsCalculateSubtreeDiffPostResponse
from . import OperationsCalculateSubtreeGitLikeDiffPostRequest
from . import OperationsCalculateSubtreeGitLikeDiffPostResponse
from . import OperationsChangeAdminStatePostRequest
from . import OperationsChangeEncryptionKeysPostRequest
from . import OperationsChangeEncryptionKeysPostResponse
from . import OperationsChangeEncryptionStatusPostRequest
from . import OperationsChangeEncryptionStatusPostResponse
from . import OperationsCheckedCommitPostRequest
from . import OperationsCheckInstalledNodesPostRequest
from . import OperationsCheckInstalledNodesPostResponse
from . import OperationsCheckNodesConnectionPostRequest
from . import OperationsClearJournalPostRequest
from . import OperationsClearJournalPostResponse
from . import OperationsCloseTransactionPostRequest
from . import OperationsCommitPostRequest
from . import OperationsCommitPostResponse
from . import OperationsCompareConfigPostRequest
from . import OperationsCompareConfigPostResponse
from . import OperationsConnectNodePostRequest
from . import OperationsCopyManyToOnePostRequest
from . import OperationsCopyOneToManyPostRequest
from . import OperationsCopyOneToOnePostRequest
from . import OperationsCreateDataChangeSubscriptionPostRequest
from . import OperationsCreateDataChangeSubscriptionPostResponse
from . import OperationsCreateMultipleTemplatesPostRequest
from . import OperationsCreateSnapshotPostRequest
from . import OperationsCreateSubscriptionPostRequest
from . import OperationsCreateTransactionPostRequest
from . import OperationsDeleteDataChangeSubscriptionPostRequest
from . import OperationsDeleteSnapshotPostRequest
from . import OperationsDisableDefaultDeviceLoggingPostRequest
from . import OperationsDisableDeviceLoggingPostRequest
from . import OperationsDisableLoggingPostRequest
from . import OperationsDisconnectNodePostRequest
from . import OperationsDiscoverPostRequest
from . import OperationsDiscoverPostResponse
from . import OperationsDryrunCommitPostRequest
from . import OperationsDryrunCommitPostResponse
from . import OperationsDryrunMountNodePostRequest
from . import OperationsDryrunUnmountNodePostRequest
from . import OperationsEnableDefaultDeviceLoggingPostRequest
from . import OperationsEnableDeviceLoggingPostRequest
from . import OperationsEnableLoggingPostRequest
from . import OperationsGetInstalledNodesPostRequest
from . import OperationsGetInstalledNodesPostResponse
from . import OperationsGetTemplateInfoPostRequest
from . import OperationsGetTemplateInfoPostResponse
from . import OperationsGetTemplateNodesPostRequest
from . import OperationsGetTemplateNodesPostResponse
from . import OperationsHealthPostRequest
from . import OperationsHealthPostResponse
from . import OperationsInstallMultipleNodesPostRequest
from . import OperationsInstallNodePostRequest
from . import OperationsIsInSyncPostRequest
from . import OperationsIsInSyncPostResponse
from . import OperationsMountNodePostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostResponse
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostResponse
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostResponse
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostResponse
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostRequest
from . import OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostResponse
from . import OperationsQueryConfigPostRequest
from . import OperationsQueryConfigPostResponse
from . import OperationsReadJournalPostRequest
from . import OperationsReadJournalPostResponse
from . import OperationsReadPropertiesPostRequest
from . import OperationsReadPropertiesPostResponse
from . import OperationsRegisterRepositoryPostRequest
from . import OperationsRegisterRepositoryPostResponse
from . import OperationsRemoveKeystoreEntryPostRequest
from . import OperationsRemovePrivateKeyPostRequest
from . import OperationsRemoveTrustedCertificatePostRequest
from . import OperationsReplaceConfigWithOperationalPostRequest
from . import OperationsReplaceConfigWithSnapshotPostRequest
from . import OperationsRevertChangesPostRequest
from . import OperationsSetGlobalHiddenTypesPostRequest
from . import OperationsSetHiddenHttpHeadersPostRequest
from . import OperationsSetHiddenHttpMethodsPostRequest
from . import OperationsSetMessageTypesPostRequest
from . import OperationsShowSubscriptionDataPostRequest
from . import OperationsShowSubscriptionDataPostResponse
from . import OperationsSyncFromNetworkPostRequest
from . import OperationsSyncToNetworkPostRequest
from . import OperationsUninstallMultipleNodesPostRequest
from . import OperationsUninstallNodePostRequest
from . import OperationsUnmountNodePostRequest
from . import OperationsUpdatePropertiesPostRequest
from . import OperationsUpdatePropertiesPostResponse
from . import OperationsUpgradeTemplatePostRequest
from . import OperationsUploadYangModelPostRequest
from . import OperationsValidatePostRequest


class UniconfigRest:
    uri: str
    method: str
    request: Any | None
    response: Any | None


class CliDefaultParametersGet(UniconfigRest):
    uri = '/data/cli-default-parameters'
    method = 'GET'
    request = None
    response = None


class CliDefaultParametersPut(UniconfigRest):
    uri = '/data/cli-default-parameters'
    method = 'PUT'
    request = None
    response = None


class CliDefaultParametersPost(UniconfigRest):
    uri = '/data/cli-default-parameters'
    method = 'POST'
    request = None
    response = None


class CliDefaultParametersDelete(UniconfigRest):
    uri = '/data/cli-default-parameters'
    method = 'DELETE'
    request = None
    response = None


class DeviceId(UniconfigRest):
    uri = '/data/device-id'
    method = 'GET'
    request = None
    response = None


class AvailableCliDeviceTranslationsGet(UniconfigRest):
    uri = '/data/available-cli-device-translations'
    method = 'GET'
    request = None
    response = None


class AvailableCliDeviceTranslationsPut(UniconfigRest):
    uri = '/data/available-cli-device-translations'
    method = 'PUT'
    request = None
    response = None


class AvailableCliDeviceTranslationsPost(UniconfigRest):
    uri = '/data/available-cli-device-translations'
    method = 'POST'
    request = None
    response = None


class AvailableCliDeviceTranslationsDelete(UniconfigRest):
    uri = '/data/available-cli-device-translations'
    method = 'DELETE'
    request = None
    response = None


class AvailableCliDeviceTranslationGet(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation'
    method = 'GET'
    request = None
    response = None


class AvailableCliDeviceTranslationPut(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation'
    method = 'PUT'
    request = None
    response = None


class AvailableCliDeviceTranslationDelete(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation'
    method = 'DELETE'
    request = None
    response = None


class AvailableCliDeviceTranslationDeviceTypeGet(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation={device_type},{device_version}'
    method = 'GET'
    request = None
    response = None


class AvailableCliDeviceTranslationDeviceTypePut(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation={device_type},{device_version}'
    method = 'PUT'
    request = None
    response = None


class AvailableCliDeviceTranslationDeviceTypeDelete(UniconfigRest):
    uri = '/data/available-cli-device-translations/available-cli-device-translation={device_type},{device_version}'
    method = 'DELETE'
    request = None
    response = None


class ConfigCoverage(UniconfigRest):
    uri = '/operations/network-topology/topology={topology_id}/node={node_id}/yang-ext:mount/config-coverage'
    method = 'POST'
    request = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostRequest
    response = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostResponse


class Execute(UniconfigRest):
    uri = '/operations/network-topology/topology={topology_id}/node={node_id}/yang-ext:mount/execute'
    method = 'POST'
    request = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostRequest
    response = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostResponse


class ExecuteAndExpect(UniconfigRest):
    uri = '/operations/network-topology/topology={topology_id}/node={node_id}/yang-ext:mount/execute-and-expect'
    method = 'POST'
    request = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostRequest
    response = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostResponse


class ExecuteAndRead(UniconfigRest):
    uri = '/operations/network-topology/topology={topology_id}/node={node_id}/yang-ext:mount/execute-and-read'
    method = 'POST'
    request = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostRequest
    response = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostResponse


class ExecuteAndReadUntil(UniconfigRest):
    uri = '/operations/network-topology/topology={topology_id}/node={node_id}/yang-ext:mount/execute-and-read-until'
    method = 'POST'
    request = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostRequest
    response = OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostResponse


class DryrunMountNode(UniconfigRest):
    uri = '/operations/dryrun-mount-node'
    method = 'POST'
    request = OperationsDryrunMountNodePostRequest
    response = None


class CheckInstalledNodes(UniconfigRest):
    uri = '/operations/check-installed-nodes'
    method = 'POST'
    request = OperationsCheckInstalledNodesPostRequest
    response = OperationsCheckInstalledNodesPostResponse


class MountNode(UniconfigRest):
    uri = '/operations/mount-node'
    method = 'POST'
    request = OperationsMountNodePostRequest
    response = None


class InstallMultipleNodes(UniconfigRest):
    uri = '/operations/install-multiple-nodes'
    method = 'POST'
    request = OperationsInstallMultipleNodesPostRequest
    response = None


class UninstallMultipleNodes(UniconfigRest):
    uri = '/operations/uninstall-multiple-nodes'
    method = 'POST'
    request = OperationsUninstallMultipleNodesPostRequest
    response = None


class ConnectNode(UniconfigRest):
    uri = '/operations/connect-node'
    method = 'POST'
    request = OperationsConnectNodePostRequest
    response = None


class GetInstalledNodes(UniconfigRest):
    uri = '/operations/get-installed-nodes'
    method = 'POST'
    request = OperationsGetInstalledNodesPostRequest
    response = OperationsGetInstalledNodesPostResponse


class DisconnectNode(UniconfigRest):
    uri = '/operations/disconnect-node'
    method = 'POST'
    request = OperationsDisconnectNodePostRequest
    response = None


class DryrunUnmountNode(UniconfigRest):
    uri = '/operations/dryrun-unmount-node'
    method = 'POST'
    request = OperationsDryrunUnmountNodePostRequest
    response = None


class UnmountNode(UniconfigRest):
    uri = '/operations/unmount-node'
    method = 'POST'
    request = OperationsUnmountNodePostRequest
    response = None


class CheckNodesConnection(UniconfigRest):
    uri = '/operations/check-nodes-connection'
    method = 'POST'
    request = OperationsCheckNodesConnectionPostRequest
    response = None


class UninstallNode(UniconfigRest):
    uri = '/operations/uninstall-node'
    method = 'POST'
    request = OperationsUninstallNodePostRequest
    response = None


class InstallNode(UniconfigRest):
    uri = '/operations/install-node'
    method = 'POST'
    request = OperationsInstallNodePostRequest
    response = None


class ChangeAdminState(UniconfigRest):
    uri = '/operations/change-admin-state'
    method = 'POST'
    request = OperationsChangeAdminStatePostRequest
    response = None


class ChangeEncryptionStatus(UniconfigRest):
    uri = '/operations/change-encryption-status'
    method = 'POST'
    request = OperationsChangeEncryptionStatusPostRequest
    response = OperationsChangeEncryptionStatusPostResponse


class ChangeEncryptionKeys(UniconfigRest):
    uri = '/operations/change-encryption-keys'
    method = 'POST'
    request = OperationsChangeEncryptionKeysPostRequest
    response = OperationsChangeEncryptionKeysPostResponse


class DeleteDataChangeSubscription(UniconfigRest):
    uri = '/operations/delete-data-change-subscription'
    method = 'POST'
    request = OperationsDeleteDataChangeSubscriptionPostRequest
    response = None


class CreateDataChangeSubscription(UniconfigRest):
    uri = '/operations/create-data-change-subscription'
    method = 'POST'
    request = OperationsCreateDataChangeSubscriptionPostRequest
    response = OperationsCreateDataChangeSubscriptionPostResponse


class ShowSubscriptionData(UniconfigRest):
    uri = '/operations/show-subscription-data'
    method = 'POST'
    request = OperationsShowSubscriptionDataPostRequest
    response = OperationsShowSubscriptionDataPostResponse


class Discover(UniconfigRest):
    uri = '/operations/discover'
    method = 'POST'
    request = OperationsDiscoverPostRequest
    response = OperationsDiscoverPostResponse


class DryrunCommit(UniconfigRest):
    uri = '/operations/dryrun-commit'
    method = 'POST'
    request = OperationsDryrunCommitPostRequest
    response = OperationsDryrunCommitPostResponse


class SetMessageTypes(UniconfigRest):
    uri = '/operations/set-message-types'
    method = 'POST'
    request = OperationsSetMessageTypesPostRequest
    response = None


class GnmiDefaultParametersGet(UniconfigRest):
    uri = '/data/gnmi-default-parameters'
    method = 'GET'
    request = None
    response = None


class GnmiDefaultParametersPut(UniconfigRest):
    uri = '/data/gnmi-default-parameters'
    method = 'PUT'
    request = None
    response = None


class GnmiDefaultParametersPost(UniconfigRest):
    uri = '/data/gnmi-default-parameters'
    method = 'POST'
    request = None
    response = None


class GnmiDefaultParametersDelete(UniconfigRest):
    uri = '/data/gnmi-default-parameters'
    method = 'DELETE'
    request = None
    response = None


class SessionTimersGet(UniconfigRest):
    uri = '/data/gnmi-default-parameters/session-timers'
    method = 'GET'
    request = None
    response = None


class SessionTimersPut(UniconfigRest):
    uri = '/data/gnmi-default-parameters/session-timers'
    method = 'PUT'
    request = None
    response = None


class SessionTimersPost(UniconfigRest):
    uri = '/data/gnmi-default-parameters/session-timers'
    method = 'POST'
    request = None
    response = None


class SessionTimersDelete(UniconfigRest):
    uri = '/data/gnmi-default-parameters/session-timers'
    method = 'DELETE'
    request = None
    response = None


class FlagsGet(UniconfigRest):
    uri = '/data/gnmi-default-parameters/flags'
    method = 'GET'
    request = None
    response = None


class FlagsPut(UniconfigRest):
    uri = '/data/gnmi-default-parameters/flags'
    method = 'PUT'
    request = None
    response = None


class FlagsPost(UniconfigRest):
    uri = '/data/gnmi-default-parameters/flags'
    method = 'POST'
    request = None
    response = None


class FlagsDelete(UniconfigRest):
    uri = '/data/gnmi-default-parameters/flags'
    method = 'DELETE'
    request = None
    response = None


class OtherParametersGet(UniconfigRest):
    uri = '/data/gnmi-default-parameters/other-parameters'
    method = 'GET'
    request = None
    response = None


class OtherParametersPut(UniconfigRest):
    uri = '/data/gnmi-default-parameters/other-parameters'
    method = 'PUT'
    request = None
    response = None


class OtherParametersPost(UniconfigRest):
    uri = '/data/gnmi-default-parameters/other-parameters'
    method = 'POST'
    request = None
    response = None


class OtherParametersDelete(UniconfigRest):
    uri = '/data/gnmi-default-parameters/other-parameters'
    method = 'DELETE'
    request = None
    response = None


class UploadYangModel(UniconfigRest):
    uri = '/operations/upload-yang-model'
    method = 'POST'
    request = OperationsUploadYangModelPostRequest
    response = None


class ReadJournal(UniconfigRest):
    uri = '/operations/read-journal'
    method = 'POST'
    request = OperationsReadJournalPostRequest
    response = OperationsReadJournalPostResponse


class ClearJournal(UniconfigRest):
    uri = '/operations/clear-journal'
    method = 'POST'
    request = OperationsClearJournalPostRequest
    response = OperationsClearJournalPostResponse


class LoggingStatus(UniconfigRest):
    uri = '/data/logging-status'
    method = 'GET'
    request = None
    response = None


class Global(UniconfigRest):
    uri = '/data/logging-status/global'
    method = 'GET'
    request = None
    response = None


class Broker(UniconfigRest):
    uri = '/data/logging-status/broker'
    method = 'GET'
    request = None
    response = None


class BrokerBrokerIdentifier(UniconfigRest):
    uri = '/data/logging-status/broker={broker_identifier}'
    method = 'GET'
    request = None
    response = None


class EnableDefaultDeviceLogging(UniconfigRest):
    uri = '/operations/enable-default-device-logging'
    method = 'POST'
    request = OperationsEnableDefaultDeviceLoggingPostRequest
    response = None


class DisableLogging(UniconfigRest):
    uri = '/operations/disable-logging'
    method = 'POST'
    request = OperationsDisableLoggingPostRequest
    response = None


class SetGlobalHiddenTypes(UniconfigRest):
    uri = '/operations/set-global-hidden-types'
    method = 'POST'
    request = OperationsSetGlobalHiddenTypesPostRequest
    response = None


class DisableDeviceLogging(UniconfigRest):
    uri = '/operations/disable-device-logging'
    method = 'POST'
    request = OperationsDisableDeviceLoggingPostRequest
    response = None


class DisableDefaultDeviceLogging(UniconfigRest):
    uri = '/operations/disable-default-device-logging'
    method = 'POST'
    request = OperationsDisableDefaultDeviceLoggingPostRequest
    response = None


class EnableDeviceLogging(UniconfigRest):
    uri = '/operations/enable-device-logging'
    method = 'POST'
    request = OperationsEnableDeviceLoggingPostRequest
    response = None


class EnableLogging(UniconfigRest):
    uri = '/operations/enable-logging'
    method = 'POST'
    request = OperationsEnableLoggingPostRequest
    response = None


class AddTrustedCertificate(UniconfigRest):
    uri = '/operations/add-trusted-certificate'
    method = 'POST'
    request = OperationsAddTrustedCertificatePostRequest
    response = None


class RemoveKeystoreEntry(UniconfigRest):
    uri = '/operations/remove-keystore-entry'
    method = 'POST'
    request = OperationsRemoveKeystoreEntryPostRequest
    response = None


class AddKeystoreEntry(UniconfigRest):
    uri = '/operations/add-keystore-entry'
    method = 'POST'
    request = OperationsAddKeystoreEntryPostRequest
    response = None


class RemoveTrustedCertificate(UniconfigRest):
    uri = '/operations/remove-trusted-certificate'
    method = 'POST'
    request = OperationsRemoveTrustedCertificatePostRequest
    response = None


class AddPrivateKey(UniconfigRest):
    uri = '/operations/add-private-key'
    method = 'POST'
    request = OperationsAddPrivateKeyPostRequest
    response = None


class RemovePrivateKey(UniconfigRest):
    uri = '/operations/remove-private-key'
    method = 'POST'
    request = OperationsRemovePrivateKeyPostRequest
    response = None


class Notification(UniconfigRest):
    uri = '/data/notification'
    method = 'GET'
    request = None
    response = None


class CreateSubscription(UniconfigRest):
    uri = '/operations/create-subscription'
    method = 'POST'
    request = OperationsCreateSubscriptionPostRequest
    response = None


class SetHiddenHttpHeaders(UniconfigRest):
    uri = '/operations/set-hidden-http-headers'
    method = 'POST'
    request = OperationsSetHiddenHttpHeadersPostRequest
    response = None


class SetHiddenHttpMethods(UniconfigRest):
    uri = '/operations/set-hidden-http-methods'
    method = 'POST'
    request = OperationsSetHiddenHttpMethodsPostRequest
    response = None


class RegisterRepository(UniconfigRest):
    uri = '/operations/register-repository'
    method = 'POST'
    request = OperationsRegisterRepositoryPostRequest
    response = OperationsRegisterRepositoryPostResponse


class SnapshotsMetadataGet(UniconfigRest):
    uri = '/data/snapshots-metadata'
    method = 'GET'
    request = None
    response = None


class SnapshotsMetadataPut(UniconfigRest):
    uri = '/data/snapshots-metadata'
    method = 'PUT'
    request = None
    response = None


class SnapshotsMetadataPost(UniconfigRest):
    uri = '/data/snapshots-metadata'
    method = 'POST'
    request = None
    response = None


class SnapshotsMetadataDelete(UniconfigRest):
    uri = '/data/snapshots-metadata'
    method = 'DELETE'
    request = None
    response = None


class SnapshotGet(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot'
    method = 'GET'
    request = None
    response = None


class SnapshotPut(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot'
    method = 'PUT'
    request = None
    response = None


class SnapshotDelete(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot'
    method = 'DELETE'
    request = None
    response = None


class SnapshotNameGet(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot={name}'
    method = 'GET'
    request = None
    response = None


class SnapshotNamePut(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot={name}'
    method = 'PUT'
    request = None
    response = None


class SnapshotNameDelete(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot={name}'
    method = 'DELETE'
    request = None
    response = None


class DeleteSnapshot(UniconfigRest):
    uri = '/operations/delete-snapshot'
    method = 'POST'
    request = OperationsDeleteSnapshotPostRequest
    response = None


class CreateSnapshot(UniconfigRest):
    uri = '/operations/create-snapshot'
    method = 'POST'
    request = OperationsCreateSnapshotPostRequest
    response = None


class ReplaceConfigWithSnapshot(UniconfigRest):
    uri = '/operations/replace-config-with-snapshot'
    method = 'POST'
    request = OperationsReplaceConfigWithSnapshotPostRequest
    response = None


class Subscription(UniconfigRest):
    uri = '/data/subscription'
    method = 'GET'
    request = None
    response = None


class SubscriptionNodeId(UniconfigRest):
    uri = '/data/subscription={node_id},{stream_name}'
    method = 'GET'
    request = None
    response = None


class CopyOneToOne(UniconfigRest):
    uri = '/operations/copy-one-to-one'
    method = 'POST'
    request = OperationsCopyOneToOnePostRequest
    response = None


class CalculateSubtreeDiff(UniconfigRest):
    uri = '/operations/calculate-subtree-diff'
    method = 'POST'
    request = OperationsCalculateSubtreeDiffPostRequest
    response = OperationsCalculateSubtreeDiffPostResponse


class CalculateSubtreeGitLikeDiff(UniconfigRest):
    uri = '/operations/calculate-subtree-git-like-diff'
    method = 'POST'
    request = OperationsCalculateSubtreeGitLikeDiffPostRequest
    response = OperationsCalculateSubtreeGitLikeDiffPostResponse


class CopyOneToMany(UniconfigRest):
    uri = '/operations/copy-one-to-many'
    method = 'POST'
    request = OperationsCopyOneToManyPostRequest
    response = None


class CopyManyToOne(UniconfigRest):
    uri = '/operations/copy-many-to-one'
    method = 'POST'
    request = OperationsCopyManyToOnePostRequest
    response = None


class BulkEdit(UniconfigRest):
    uri = '/operations/bulk-edit'
    method = 'POST'
    request = OperationsBulkEditPostRequest
    response = None


class ApplyTemplate(UniconfigRest):
    uri = '/operations/apply-template'
    method = 'POST'
    request = OperationsApplyTemplatePostRequest
    response = None


class UpgradeTemplate(UniconfigRest):
    uri = '/operations/upgrade-template'
    method = 'POST'
    request = OperationsUpgradeTemplatePostRequest
    response = None


class GetTemplateInfo(UniconfigRest):
    uri = '/operations/get-template-info'
    method = 'POST'
    request = OperationsGetTemplateInfoPostRequest
    response = OperationsGetTemplateInfoPostResponse


class GetTemplateNodes(UniconfigRest):
    uri = '/operations/get-template-nodes'
    method = 'POST'
    request = OperationsGetTemplateNodesPostRequest
    response = OperationsGetTemplateNodesPostResponse


class CreateMultipleTemplates(UniconfigRest):
    uri = '/operations/create-multiple-templates'
    method = 'POST'
    request = OperationsCreateMultipleTemplatesPostRequest
    response = None


class TransactionsData(UniconfigRest):
    uri = '/data/transactions-data'
    method = 'GET'
    request = None
    response = None


class TransactionData(UniconfigRest):
    uri = '/data/transactions-data/transaction-data'
    method = 'GET'
    request = None
    response = None


class TransactionDataTransactionId(UniconfigRest):
    uri = '/data/transactions-data/transaction-data={transaction_id}'
    method = 'GET'
    request = None
    response = None


class TransactionsMetadata(UniconfigRest):
    uri = '/data/transactions-metadata'
    method = 'GET'
    request = None
    response = None


class TransactionMetadata(UniconfigRest):
    uri = '/data/transactions-metadata/transaction-metadata'
    method = 'GET'
    request = None
    response = None


class TransactionMetadataTransactionId(UniconfigRest):
    uri = '/data/transactions-metadata/transaction-metadata={transaction_id}'
    method = 'GET'
    request = None
    response = None


class RevertChanges(UniconfigRest):
    uri = '/operations/revert-changes'
    method = 'POST'
    request = OperationsRevertChangesPostRequest
    response = None


class SyncFromNetwork(UniconfigRest):
    uri = '/operations/sync-from-network'
    method = 'POST'
    request = OperationsSyncFromNetworkPostRequest
    response = None


class BulkGet(UniconfigRest):
    uri = '/operations/bulk-get'
    method = 'POST'
    request = OperationsBulkGetPostRequest
    response = OperationsBulkGetPostResponse


class CloseTransaction(UniconfigRest):
    uri = '/operations/close-transaction'
    method = 'POST'
    request = OperationsCloseTransactionPostRequest
    response = None


class CalculateGitLikeDiff(UniconfigRest):
    uri = '/operations/calculate-git-like-diff'
    method = 'POST'
    request = OperationsCalculateGitLikeDiffPostRequest
    response = OperationsCalculateGitLikeDiffPostResponse


class UpdateProperties(UniconfigRest):
    uri = '/operations/update-properties'
    method = 'POST'
    request = OperationsUpdatePropertiesPostRequest
    response = OperationsUpdatePropertiesPostResponse


class IsInSync(UniconfigRest):
    uri = '/operations/is-in-sync'
    method = 'POST'
    request = OperationsIsInSyncPostRequest
    response = OperationsIsInSyncPostResponse


class SyncToNetwork(UniconfigRest):
    uri = '/operations/sync-to-network'
    method = 'POST'
    request = OperationsSyncToNetworkPostRequest
    response = None


class CreateTransaction(UniconfigRest):
    uri = '/operations/create-transaction'
    method = 'POST'
    request = OperationsCreateTransactionPostRequest
    response = None


class ReadProperties(UniconfigRest):
    uri = '/operations/read-properties'
    method = 'POST'
    request = OperationsReadPropertiesPostRequest
    response = OperationsReadPropertiesPostResponse


class Health(UniconfigRest):
    uri = '/operations/health'
    method = 'POST'
    request = OperationsHealthPostRequest
    response = OperationsHealthPostResponse


class Validate(UniconfigRest):
    uri = '/operations/validate'
    method = 'POST'
    request = OperationsValidatePostRequest
    response = None


class ReplaceConfigWithOperational(UniconfigRest):
    uri = '/operations/replace-config-with-operational'
    method = 'POST'
    request = OperationsReplaceConfigWithOperationalPostRequest
    response = None


class Commit(UniconfigRest):
    uri = '/operations/commit'
    method = 'POST'
    request = OperationsCommitPostRequest
    response = OperationsCommitPostResponse


class CheckedCommit(UniconfigRest):
    uri = '/operations/checked-commit'
    method = 'POST'
    request = OperationsCheckedCommitPostRequest
    response = None


class CalculateDiff(UniconfigRest):
    uri = '/operations/calculate-diff'
    method = 'POST'
    request = OperationsCalculateDiffPostRequest
    response = OperationsCalculateDiffPostResponse


class CompareConfig(UniconfigRest):
    uri = '/operations/compare-config'
    method = 'POST'
    request = OperationsCompareConfigPostRequest
    response = OperationsCompareConfigPostResponse


class QueryConfig(UniconfigRest):
    uri = '/operations/query-config'
    method = 'POST'
    request = OperationsQueryConfigPostRequest
    response = OperationsQueryConfigPostResponse


class AvailableUnitopoDeviceTranslations(UniconfigRest):
    uri = '/data/available-unitopo-device-translations'
    method = 'GET'
    request = None
    response = None


class Unit(UniconfigRest):
    uri = '/data/available-unitopo-device-translations/unit'
    method = 'GET'
    request = None
    response = None


class UnitId(UniconfigRest):
    uri = '/data/available-unitopo-device-translations/unit={id}'
    method = 'GET'
    request = None
    response = None


class ReadStructuredData(UniconfigRest):
    uri = '/data/network-topology:network-topology/topology={topology_id}/node={node_id}/frinx-uniconfig-topology:configuration{uri}'
    method = 'GET'


class WriteStructuredData(UniconfigRest):
    uri = '/data/network-topology:network-topology/topology={topology_id}/node={node_id}/frinx-uniconfig-topology:configuration{uri}'
    method = 'PUT'


class DeleteStructuredData(UniconfigRest):
    uri = '/data/network-topology:network-topology/topology={topology_id}/node={node_id}/frinx-uniconfig-topology:configuration{uri}'
    method = 'DELETE'

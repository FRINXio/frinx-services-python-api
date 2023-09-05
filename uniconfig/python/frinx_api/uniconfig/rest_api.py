from __future__ import annotations

from pydantic import BaseModel

from . import OperationsAddKeystoreEntryPostRequest
from . import OperationsAddPrivateKeyPostRequest
from . import OperationsAddTrustedCertificatePostRequest
from . import OperationsApplyTemplatePostRequest
from . import OperationsApplyTemplatePostResponse
from . import OperationsBulkEditPostRequest
from . import OperationsBulkEditPostResponse
from . import OperationsCalculateDiffPostRequest
from . import OperationsCalculateDiffPostResponse
from . import OperationsCalculateGitLikeDiffPostRequest
from . import OperationsCalculateGitLikeDiffPostResponse
from . import OperationsCalculateSubtreeDiffPostRequest
from . import OperationsCalculateSubtreeDiffPostResponse
from . import OperationsCalculateSubtreeGitLikeDiffPostRequest
from . import OperationsCalculateSubtreeGitLikeDiffPostResponse
from . import OperationsChangeAdminStatePostRequest
from . import OperationsChangeAdminStatePostResponse
from . import OperationsChangeEncryptionStatusPostRequest
from . import OperationsChangeEncryptionStatusPostResponse
from . import OperationsCheckedCommitPostRequest
from . import OperationsCheckedCommitPostResponse
from . import OperationsCheckInstalledNodesPostRequest
from . import OperationsCheckInstalledNodesPostResponse
from . import OperationsClearJournalPostRequest
from . import OperationsClearJournalPostResponse
from . import OperationsCloseTransactionPostRequest
from . import OperationsCommitPostRequest
from . import OperationsCommitPostResponse
from . import OperationsCompareConfigPostRequest
from . import OperationsCompareConfigPostResponse
from . import OperationsCopyManyToOnePostRequest
from . import OperationsCopyManyToOnePostResponse
from . import OperationsCopyOneToManyPostRequest
from . import OperationsCopyOneToManyPostResponse
from . import OperationsCopyOneToOnePostRequest
from . import OperationsCopyOneToOnePostResponse
from . import OperationsCreateDataChangeSubscriptionPostRequest
from . import OperationsCreateDataChangeSubscriptionPostResponse
from . import OperationsCreateMultipleTemplatesPostRequest
from . import OperationsCreateMultipleTemplatesPostResponse
from . import OperationsCreateSnapshotPostRequest
from . import OperationsCreateSnapshotPostResponse
from . import OperationsCreateSubscriptionPostRequest
from . import OperationsCreateTransactionPostRequest
from . import OperationsDeleteDataChangeSubscriptionPostRequest
from . import OperationsDeleteSnapshotPostRequest
from . import OperationsDeleteSnapshotPostResponse
from . import OperationsDisableDefaultDeviceLoggingPostRequest
from . import OperationsDisableDefaultDeviceLoggingPostResponse
from . import OperationsDisableDeviceLoggingPostRequest
from . import OperationsDisableDeviceLoggingPostResponse
from . import OperationsDisableLoggingPostRequest
from . import OperationsDisableLoggingPostResponse
from . import OperationsDiscoverPostRequest
from . import OperationsDiscoverPostResponse
from . import OperationsDryrunCommitPostRequest
from . import OperationsDryrunCommitPostResponse
from . import OperationsDryrunMountNodePostRequest
from . import OperationsDryrunMountNodePostResponse
from . import OperationsDryrunUnmountNodePostRequest
from . import OperationsDryrunUnmountNodePostResponse
from . import OperationsEnableDefaultDeviceLoggingPostRequest
from . import OperationsEnableDefaultDeviceLoggingPostResponse
from . import OperationsEnableDeviceLoggingPostRequest
from . import OperationsEnableDeviceLoggingPostResponse
from . import OperationsEnableLoggingPostRequest
from . import OperationsEnableLoggingPostResponse
from . import OperationsGetInstalledNodesPostRequest
from . import OperationsGetInstalledNodesPostResponse
from . import OperationsGetTemplateInfoPostRequest
from . import OperationsGetTemplateInfoPostResponse
from . import OperationsGetTemplateNodesPostRequest
from . import OperationsGetTemplateNodesPostResponse
from . import OperationsHealthPostRequest
from . import OperationsHealthPostResponse
from . import OperationsInstallMultipleNodesPostRequest
from . import OperationsInstallMultipleNodesPostResponse
from . import OperationsInstallNodePostRequest
from . import OperationsInstallNodePostResponse
from . import OperationsIsInSyncPostRequest
from . import OperationsIsInSyncPostResponse
from . import OperationsMountNodePostRequest
from . import OperationsMountNodePostResponse
from . import OperationsQueryConfigPostRequest
from . import OperationsQueryConfigPostResponse
from . import OperationsReadJournalPostRequest
from . import OperationsReadJournalPostResponse
from . import OperationsRegisterRepositoryPostRequest
from . import OperationsRegisterRepositoryPostResponse
from . import OperationsRemoveKeystoreEntryPostRequest
from . import OperationsRemovePrivateKeyPostRequest
from . import OperationsRemoveTrustedCertificatePostRequest
from . import OperationsReplaceConfigWithOperationalPostRequest
from . import OperationsReplaceConfigWithOperationalPostResponse
from . import OperationsReplaceConfigWithSnapshotPostRequest
from . import OperationsReplaceConfigWithSnapshotPostResponse
from . import OperationsRevertChangesPostRequest
from . import OperationsRevertChangesPostResponse
from . import OperationsSetGlobalHiddenTypesPostRequest
from . import OperationsSetGlobalHiddenTypesPostResponse
from . import OperationsSetHiddenHttpHeadersPostRequest
from . import OperationsSetHiddenHttpHeadersPostResponse
from . import OperationsSetHiddenHttpMethodsPostRequest
from . import OperationsSetHiddenHttpMethodsPostResponse
from . import OperationsShowSubscriptionDataPostRequest
from . import OperationsShowSubscriptionDataPostResponse
from . import OperationsSyncFromNetworkPostRequest
from . import OperationsSyncFromNetworkPostResponse
from . import OperationsSyncToNetworkPostRequest
from . import OperationsSyncToNetworkPostResponse
from . import OperationsUninstallMultipleNodesPostRequest
from . import OperationsUninstallMultipleNodesPostResponse
from . import OperationsUninstallNodePostRequest
from . import OperationsUninstallNodePostResponse
from . import OperationsUnmountNodePostRequest
from . import OperationsUnmountNodePostResponse
from . import OperationsUpgradeTemplatePostRequest
from . import OperationsValidatePostRequest
from . import OperationsValidatePostResponse


class UniconfigRest:
    uri: str
    method: str
    request: BaseModel | None
    response: BaseModel | None


class ConfigCoverage(UniconfigRest):
    uri = '/operations/network-topology/topology={topology-id}/node={node-id}/yang-ext:mount/config-coverage'
    method = 'POST'
    request = None
    response = None


class Execute(UniconfigRest):
    uri = '/operations/network-topology/topology={topology-id}/node={node-id}/yang-ext:mount/execute'
    method = 'POST'
    request = None
    response = None


class ExecuteAndExpect(UniconfigRest):
    uri = '/operations/network-topology/topology={topology-id}/node={node-id}/yang-ext:mount/execute-and-expect'
    method = 'POST'
    request = None
    response = None


class ExecuteAndRead(UniconfigRest):
    uri = '/operations/network-topology/topology={topology-id}/node={node-id}/yang-ext:mount/execute-and-read'
    method = 'POST'
    request = None
    response = None


class ExecuteAndReadUntil(UniconfigRest):
    uri = '/operations/network-topology/topology={topology-id}/node={node-id}/yang-ext:mount/execute-and-read-until'
    method = 'POST'
    request = None
    response = None


class UninstallNode(UniconfigRest):
    uri = '/operations/uninstall-node'
    method = 'POST'
    request = OperationsUninstallNodePostRequest
    response = OperationsUninstallNodePostResponse


class UninstallMultipleNodes(UniconfigRest):
    uri = '/operations/uninstall-multiple-nodes'
    method = 'POST'
    request = OperationsUninstallMultipleNodesPostRequest
    response = OperationsUninstallMultipleNodesPostResponse


class GetInstalledNodes(UniconfigRest):
    uri = '/operations/get-installed-nodes'
    method = 'POST'
    request = OperationsGetInstalledNodesPostRequest
    response = OperationsGetInstalledNodesPostResponse


class InstallNode(UniconfigRest):
    uri = '/operations/install-node'
    method = 'POST'
    request = OperationsInstallNodePostRequest
    response = OperationsInstallNodePostResponse


class ChangeAdminState(UniconfigRest):
    uri = '/operations/change-admin-state'
    method = 'POST'
    request = OperationsChangeAdminStatePostRequest
    response = OperationsChangeAdminStatePostResponse


class UnmountNode(UniconfigRest):
    uri = '/operations/unmount-node'
    method = 'POST'
    request = OperationsUnmountNodePostRequest
    response = OperationsUnmountNodePostResponse


class DryrunUnmountNode(UniconfigRest):
    uri = '/operations/dryrun-unmount-node'
    method = 'POST'
    request = OperationsDryrunUnmountNodePostRequest
    response = OperationsDryrunUnmountNodePostResponse


class MountNode(UniconfigRest):
    uri = '/operations/mount-node'
    method = 'POST'
    request = OperationsMountNodePostRequest
    response = OperationsMountNodePostResponse


class InstallMultipleNodes(UniconfigRest):
    uri = '/operations/install-multiple-nodes'
    method = 'POST'
    request = OperationsInstallMultipleNodesPostRequest
    response = OperationsInstallMultipleNodesPostResponse


class CheckInstalledNodes(UniconfigRest):
    uri = '/operations/check-installed-nodes'
    method = 'POST'
    request = OperationsCheckInstalledNodesPostRequest
    response = OperationsCheckInstalledNodesPostResponse


class DryrunMountNode(UniconfigRest):
    uri = '/operations/dryrun-mount-node'
    method = 'POST'
    request = OperationsDryrunMountNodePostRequest
    response = OperationsDryrunMountNodePostResponse


class ChangeEncryptionStatus(UniconfigRest):
    uri = '/operations/change-encryption-status'
    method = 'POST'
    request = OperationsChangeEncryptionStatusPostRequest
    response = OperationsChangeEncryptionStatusPostResponse


class ShowSubscriptionData(UniconfigRest):
    uri = '/operations/show-subscription-data'
    method = 'POST'
    request = OperationsShowSubscriptionDataPostRequest
    response = OperationsShowSubscriptionDataPostResponse


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
    request = None
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


class EnableDefaultDeviceLogging(UniconfigRest):
    uri = '/operations/enable-default-device-logging'
    method = 'POST'
    request = OperationsEnableDefaultDeviceLoggingPostRequest
    response = OperationsEnableDefaultDeviceLoggingPostResponse


class DisableLogging(UniconfigRest):
    uri = '/operations/disable-logging'
    method = 'POST'
    request = OperationsDisableLoggingPostRequest
    response = OperationsDisableLoggingPostResponse


class SetGlobalHiddenTypes(UniconfigRest):
    uri = '/operations/set-global-hidden-types'
    method = 'POST'
    request = OperationsSetGlobalHiddenTypesPostRequest
    response = OperationsSetGlobalHiddenTypesPostResponse


class DisableDeviceLogging(UniconfigRest):
    uri = '/operations/disable-device-logging'
    method = 'POST'
    request = OperationsDisableDeviceLoggingPostRequest
    response = OperationsDisableDeviceLoggingPostResponse


class DisableDefaultDeviceLogging(UniconfigRest):
    uri = '/operations/disable-default-device-logging'
    method = 'POST'
    request = OperationsDisableDefaultDeviceLoggingPostRequest
    response = OperationsDisableDefaultDeviceLoggingPostResponse


class EnableDeviceLogging(UniconfigRest):
    uri = '/operations/enable-device-logging'
    method = 'POST'
    request = OperationsEnableDeviceLoggingPostRequest
    response = OperationsEnableDeviceLoggingPostResponse


class EnableLogging(UniconfigRest):
    uri = '/operations/enable-logging'
    method = 'POST'
    request = OperationsEnableLoggingPostRequest
    response = OperationsEnableLoggingPostResponse


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


class CreateSubscription(UniconfigRest):
    uri = '/operations/create-subscription'
    method = 'POST'
    request = OperationsCreateSubscriptionPostRequest
    response = None


class SetHiddenHttpHeaders(UniconfigRest):
    uri = '/operations/set-hidden-http-headers'
    method = 'POST'
    request = OperationsSetHiddenHttpHeadersPostRequest
    response = OperationsSetHiddenHttpHeadersPostResponse


class SetHiddenHttpMethods(UniconfigRest):
    uri = '/operations/set-hidden-http-methods'
    method = 'POST'
    request = OperationsSetHiddenHttpMethodsPostRequest
    response = OperationsSetHiddenHttpMethodsPostResponse


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


class SnapshotPost(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot'
    method = 'POST'
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


class SnapshotNamePost(UniconfigRest):
    uri = '/data/snapshots-metadata/snapshot={name}'
    method = 'POST'
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
    response = OperationsDeleteSnapshotPostResponse


class CreateSnapshot(UniconfigRest):
    uri = '/operations/create-snapshot'
    method = 'POST'
    request = OperationsCreateSnapshotPostRequest
    response = OperationsCreateSnapshotPostResponse


class ReplaceConfigWithSnapshot(UniconfigRest):
    uri = '/operations/replace-config-with-snapshot'
    method = 'POST'
    request = OperationsReplaceConfigWithSnapshotPostRequest
    response = OperationsReplaceConfigWithSnapshotPostResponse


class CopyOneToOne(UniconfigRest):
    uri = '/operations/copy-one-to-one'
    method = 'POST'
    request = OperationsCopyOneToOnePostRequest
    response = OperationsCopyOneToOnePostResponse


class CopyOneToMany(UniconfigRest):
    uri = '/operations/copy-one-to-many'
    method = 'POST'
    request = OperationsCopyOneToManyPostRequest
    response = OperationsCopyOneToManyPostResponse


class CalculateSubtreeDiff(UniconfigRest):
    uri = '/operations/calculate-subtree-diff'
    method = 'POST'
    request = OperationsCalculateSubtreeDiffPostRequest
    response = OperationsCalculateSubtreeDiffPostResponse


class CopyManyToOne(UniconfigRest):
    uri = '/operations/copy-many-to-one'
    method = 'POST'
    request = OperationsCopyManyToOnePostRequest
    response = OperationsCopyManyToOnePostResponse


class CalculateSubtreeGitLikeDiff(UniconfigRest):
    uri = '/operations/calculate-subtree-git-like-diff'
    method = 'POST'
    request = OperationsCalculateSubtreeGitLikeDiffPostRequest
    response = OperationsCalculateSubtreeGitLikeDiffPostResponse


class BulkEdit(UniconfigRest):
    uri = '/operations/bulk-edit'
    method = 'POST'
    request = OperationsBulkEditPostRequest
    response = OperationsBulkEditPostResponse


class ApplyTemplate(UniconfigRest):
    uri = '/operations/apply-template'
    method = 'POST'
    request = OperationsApplyTemplatePostRequest
    response = OperationsApplyTemplatePostResponse


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
    response = OperationsCreateMultipleTemplatesPostResponse


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
    uri = '/data/transactions-metadata/transaction-metadata={transaction-id}'
    method = 'GET'
    request = None
    response = None


class RevertChanges(UniconfigRest):
    uri = '/operations/revert-changes'
    method = 'POST'
    request = OperationsRevertChangesPostRequest
    response = OperationsRevertChangesPostResponse


class SyncToNetwork(UniconfigRest):
    uri = '/operations/sync-to-network'
    method = 'POST'
    request = OperationsSyncToNetworkPostRequest
    response = OperationsSyncToNetworkPostResponse


class CreateTransaction(UniconfigRest):
    uri = '/operations/create-transaction'
    method = 'POST'
    request = OperationsCreateTransactionPostRequest
    response = None


class Health(UniconfigRest):
    uri = '/operations/health'
    method = 'POST'
    request = OperationsHealthPostRequest
    response = OperationsHealthPostResponse


class ReplaceConfigWithOperational(UniconfigRest):
    uri = '/operations/replace-config-with-operational'
    method = 'POST'
    request = OperationsReplaceConfigWithOperationalPostRequest
    response = OperationsReplaceConfigWithOperationalPostResponse


class Validate(UniconfigRest):
    uri = '/operations/validate'
    method = 'POST'
    request = OperationsValidatePostRequest
    response = OperationsValidatePostResponse


class Commit(UniconfigRest):
    uri = '/operations/commit'
    method = 'POST'
    request = OperationsCommitPostRequest
    response = OperationsCommitPostResponse


class CheckedCommit(UniconfigRest):
    uri = '/operations/checked-commit'
    method = 'POST'
    request = OperationsCheckedCommitPostRequest
    response = OperationsCheckedCommitPostResponse


class CompareConfig(UniconfigRest):
    uri = '/operations/compare-config'
    method = 'POST'
    request = OperationsCompareConfigPostRequest
    response = OperationsCompareConfigPostResponse


class CalculateDiff(UniconfigRest):
    uri = '/operations/calculate-diff'
    method = 'POST'
    request = OperationsCalculateDiffPostRequest
    response = OperationsCalculateDiffPostResponse


class SyncFromNetwork(UniconfigRest):
    uri = '/operations/sync-from-network'
    method = 'POST'
    request = OperationsSyncFromNetworkPostRequest
    response = OperationsSyncFromNetworkPostResponse


class CalculateGitLikeDiff(UniconfigRest):
    uri = '/operations/calculate-git-like-diff'
    method = 'POST'
    request = OperationsCalculateGitLikeDiffPostRequest
    response = OperationsCalculateGitLikeDiffPostResponse


class CloseTransaction(UniconfigRest):
    uri = '/operations/close-transaction'
    method = 'POST'
    request = OperationsCloseTransactionPostRequest
    response = None


class IsInSync(UniconfigRest):
    uri = '/operations/is-in-sync'
    method = 'POST'
    request = OperationsIsInSyncPostRequest
    response = OperationsIsInSyncPostResponse


class QueryConfig(UniconfigRest):
    uri = '/operations/query-config'
    method = 'POST'
    request = OperationsQueryConfigPostRequest
    response = OperationsQueryConfigPostResponse

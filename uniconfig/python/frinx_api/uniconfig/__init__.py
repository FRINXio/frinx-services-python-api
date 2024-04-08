# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from .cli.unit.generic import configcoverage
from .cli.unit.generic import execute
from .cli.unit.generic import executeandexpect
from .cli.unit.generic import executeandread
from .cli.unit.generic import executeandreaduntil
from .connection.manager import changeadminstate
from .connection.manager import checkinstallednodes
from .connection.manager import connectnode
from .connection.manager import disconnectnode
from .connection.manager import dryrunmountnode
from .connection.manager import dryrununmountnode
from .connection.manager import getinstallednodes
from .connection.manager import installmultiplenodes
from .connection.manager import installnode
from .connection.manager import mountnode
from .connection.manager import uninstallmultiplenodes
from .connection.manager import uninstallnode
from .connection.manager import unmountnode
from .crypto import changeencryptionkeys
from .crypto import changeencryptionstatus
from .data.change.events import createdatachangesubscription
from .data.change.events import deletedatachangesubscription
from .data.change.events import showsubscriptiondata
from .device.discovery import discover
from .dryrun.manager import dryruncommit
from .gnmi.logging import setmessagetypes
from .gnmi.yang.storage import uploadyangmodel
from .journal import clearjournal
from .journal import readjournal
from .logging import disabledefaultdevicelogging
from .logging import disabledevicelogging
from .logging import disablelogging
from .logging import enabledefaultdevicelogging
from .logging import enabledevicelogging
from .logging import enablelogging
from .logging import setglobalhiddentypes
from .netconf.keystore import addkeystoreentry
from .netconf.keystore import addprivatekey
from .netconf.keystore import addtrustedcertificate
from .netconf.keystore import removekeystoreentry
from .netconf.keystore import removeprivatekey
from .netconf.keystore import removetrustedcertificate
from .notifications import createsubscription
from .restconf.logging import sethiddenhttpheaders
from .restconf.logging import sethiddenhttpmethods
from .schema.resources import registerrepository
from .snapshot.manager import createsnapshot
from .snapshot.manager import deletesnapshot
from .snapshot.manager import replaceconfigwithsnapshot
from .subtree.manager import bulkedit
from .subtree.manager import calculatesubtreediff
from .subtree.manager import calculatesubtreegitlikediff
from .subtree.manager import copymanytoone
from .subtree.manager import copyonetomany
from .subtree.manager import copyonetoone
from .template.manager import applytemplate
from .template.manager import createmultipletemplates
from .template.manager import gettemplateinfo
from .template.manager import gettemplatenodes
from .template.manager import upgradetemplate
from .transaction.log import revertchanges
from .uniconfig.manager import calculatediff
from .uniconfig.manager import calculategitlikediff
from .uniconfig.manager import checkedcommit
from .uniconfig.manager import commit
from .uniconfig.manager import compareconfig
from .uniconfig.manager import health
from .uniconfig.manager import isinsync
from .uniconfig.manager import readproperties
from .uniconfig.manager import replaceconfigwithoperational
from .uniconfig.manager import syncfromnetwork
from .uniconfig.manager import synctonetwork
from .uniconfig.manager import updateproperties
from .uniconfig.manager import validate
from .uniconfig.query import queryconfig


class OperationsReadJournalPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsClearJournalPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsGetTemplateNodesPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsCloseTransactionPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsCreateTransactionPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsHealthPostRequest(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
    )


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostRequest(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[configcoverage.Input] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountConfigCoveragePostResponse(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[configcoverage.Output] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostRequest(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[execute.Input] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecutePostResponse(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[execute.Output] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostRequest(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[executeandexpect.Input] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndExpectPostResponse(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[executeandexpect.Output] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostRequest(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[executeandread.Input] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadPostResponse(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[executeandread.Output] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostRequest(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[executeandreaduntil.Input] = None


class OperationsNetworkTopologyTopologyTopologyIdNodeNodeIdYangExtMountExecuteAndReadUntilPostResponse(
    BaseModel
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[executeandreaduntil.Output] = None


class OperationsCheckInstalledNodesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[checkinstallednodes.Input] = None


class OperationsCheckInstalledNodesPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[checkinstallednodes.Output] = None


class OperationsConnectNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[connectnode.Input] = None


class OperationsGetInstalledNodesPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[getinstallednodes.Output] = None


class OperationsDisconnectNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[disconnectnode.Input] = None


class OperationsChangeEncryptionStatusPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[changeencryptionstatus.Input] = None


class OperationsChangeEncryptionStatusPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[changeencryptionstatus.Output] = None


class OperationsChangeEncryptionKeysPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[changeencryptionkeys.Output] = None


class OperationsDeleteDataChangeSubscriptionPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[deletedatachangesubscription.Input] = None


class OperationsCreateDataChangeSubscriptionPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[createdatachangesubscription.Output] = None


class OperationsShowSubscriptionDataPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[showsubscriptiondata.Input] = None


class OperationsDiscoverPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[discover.Input] = None


class OperationsDiscoverPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[discover.Output] = None


class OperationsDryrunCommitPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[dryruncommit.Input] = None


class OperationsDryrunCommitPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[dryruncommit.Output] = None


class OperationsUploadYangModelPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[uploadyangmodel.Input] = None


class OperationsReadJournalPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[readjournal.Output] = None


class OperationsClearJournalPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[clearjournal.Output] = None


class OperationsEnableDefaultDeviceLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[enabledefaultdevicelogging.Input] = None


class OperationsDisableLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[disablelogging.Input] = None


class OperationsSetGlobalHiddenTypesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[setglobalhiddentypes.Input] = None


class OperationsDisableDeviceLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[disabledevicelogging.Input] = None


class OperationsDisableDefaultDeviceLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[disabledefaultdevicelogging.Input] = None


class OperationsEnableDeviceLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[enabledevicelogging.Input] = None


class OperationsEnableLoggingPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[enablelogging.Input] = None


class OperationsAddTrustedCertificatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[addtrustedcertificate.Input] = None


class OperationsRemoveKeystoreEntryPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[removekeystoreentry.Input] = None


class OperationsAddKeystoreEntryPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[addkeystoreentry.Input] = None


class OperationsRemoveTrustedCertificatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[removetrustedcertificate.Input] = None


class OperationsAddPrivateKeyPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[addprivatekey.Input] = None


class OperationsRemovePrivateKeyPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[removeprivatekey.Input] = None


class OperationsCreateSubscriptionPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[createsubscription.Input] = None


class OperationsSetHiddenHttpHeadersPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[sethiddenhttpheaders.Input] = None


class OperationsRegisterRepositoryPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[registerrepository.Input] = None


class OperationsDeleteSnapshotPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[deletesnapshot.Input] = None


class OperationsCreateSnapshotPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[createsnapshot.Input] = None


class OperationsReplaceConfigWithSnapshotPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[replaceconfigwithsnapshot.Input] = None


class OperationsCalculateSubtreeDiffPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[calculatesubtreediff.Output] = None


class OperationsCalculateSubtreeGitLikeDiffPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[calculatesubtreegitlikediff.Output] = None


class OperationsApplyTemplatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[applytemplate.Input] = None


class OperationsUpgradeTemplatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[upgradetemplate.Input] = None


class OperationsGetTemplateInfoPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[gettemplateinfo.Input] = None


class OperationsGetTemplateInfoPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[gettemplateinfo.Output] = None


class OperationsGetTemplateNodesPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[gettemplatenodes.Output] = None


class OperationsRevertChangesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[revertchanges.Input] = None


class OperationsSyncFromNetworkPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[syncfromnetwork.Input] = None


class OperationsCalculateGitLikeDiffPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[calculategitlikediff.Input] = None


class OperationsCalculateGitLikeDiffPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[calculategitlikediff.Output] = None


class OperationsUpdatePropertiesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[updateproperties.Input] = None


class OperationsUpdatePropertiesPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[updateproperties.Output] = None


class OperationsIsInSyncPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[isinsync.Input] = None


class OperationsIsInSyncPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[isinsync.Output] = None


class OperationsSyncToNetworkPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[synctonetwork.Input] = None


class OperationsReadPropertiesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[readproperties.Input] = None


class OperationsReadPropertiesPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[readproperties.Output] = None


class OperationsHealthPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[health.Output] = None


class OperationsValidatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[validate.Input] = None


class OperationsReplaceConfigWithOperationalPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[replaceconfigwithoperational.Input] = None


class OperationsCommitPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[commit.Input] = None


class OperationsCommitPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[commit.Output] = None


class OperationsCheckedCommitPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[checkedcommit.Input] = None


class OperationsCalculateDiffPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[calculatediff.Input] = None


class OperationsCalculateDiffPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[calculatediff.Output] = None


class OperationsCompareConfigPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[compareconfig.Input] = None


class OperationsCompareConfigPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[compareconfig.Output] = None


class OperationsQueryConfigPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[queryconfig.Input] = None


class OperationsQueryConfigPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[queryconfig.Output] = None


class OperationsDryrunMountNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[dryrunmountnode.Input] = None


class OperationsMountNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[mountnode.Input] = None


class OperationsInstallMultipleNodesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[installmultiplenodes.Input] = None


class OperationsUninstallMultipleNodesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[uninstallmultiplenodes.Input] = None


class OperationsGetInstalledNodesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[getinstallednodes.Input] = None


class OperationsDryrunUnmountNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[dryrununmountnode.Input] = None


class OperationsUnmountNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[unmountnode.Input] = None


class OperationsUninstallNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[uninstallnode.Input] = None


class OperationsInstallNodePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[installnode.Input] = None


class OperationsChangeAdminStatePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[changeadminstate.Input] = None


class OperationsChangeEncryptionKeysPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[changeencryptionkeys.Input] = None


class OperationsCreateDataChangeSubscriptionPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[createdatachangesubscription.Input] = None


class OperationsShowSubscriptionDataPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[showsubscriptiondata.Output] = None


class OperationsSetMessageTypesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[setmessagetypes.Input] = None


class OperationsSetHiddenHttpMethodsPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[sethiddenhttpmethods.Input] = None


class OperationsRegisterRepositoryPostResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    output: Optional[registerrepository.Output] = None


class OperationsCopyOneToOnePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[copyonetoone.Input] = None


class OperationsCalculateSubtreeDiffPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[calculatesubtreediff.Input] = None


class OperationsCalculateSubtreeGitLikeDiffPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[calculatesubtreegitlikediff.Input] = None


class OperationsCopyOneToManyPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[copyonetomany.Input] = None


class OperationsCopyManyToOnePostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[copymanytoone.Input] = None


class OperationsBulkEditPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[bulkedit.Input] = None


class OperationsCreateMultipleTemplatesPostRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: Optional[createmultipletemplates.Input] = None

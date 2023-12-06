# generated by datamodel-codegen

from __future__ import annotations

from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ...cli import topology
from ...frinx import types
from ...netconf.node import topology as topology_1
from ...uniconfig import config


class CliTopologyDefaultErrorPatterns(BaseModel):
    """
    Device specific list of error patterns. This list is the primary source
    of error checking on the device. This list can be overridden from the code.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    error_pattern: Optional[list[str]] = Field(None, alias='error-pattern')
    """
    Device specific error patterns.
    """


class Blacklist(BaseModel):
    """
    Reads which are not invoked for sync-from-network and initial config read.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    path: Optional[list[str]] = None
    """
    Only root schema nodes are supported. The path needs to be in URI format from RFC 8040.
    e.g. ietf-interfaces:interfaces where ietf-interfaces is YANG module name and interfaces is root
    container.
    """
    extension: Optional[list[str]] = None
    """
    List of extensions that mark top level containers/lists.
    Example value: ["common:hidden true"]
    """


class Whitelist(BaseModel):
    """
    Reads which are invoked for sync-from-network and initial config read.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    path: Optional[list[str]] = None
    """
    Only root schema nodes are supported. The path needs to be in URI format from RFC 8040.
    e.g. ietf-interfaces:interfaces where ietf-interfaces is YANG module name and interfaces is root
    container.
    """
    extension: Optional[list[str]] = None
    """
    List of extensions that mark top level containers/lists.
    Example value: ["common:hidden true"]
    """


class CliTopologyDefaultCommitErrorPatterns(BaseModel):
    """
    Device specific list of commit error patterns. The following list
    of patterns is checked in the input after 'commit' command is sent.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    commit_error_pattern: Optional[list[str]] = Field(
        None, alias='commit-error-pattern'
    )
    """
    Device specific commit error patterns.
    """


class NetconfNodeTopologyYangModuleCapabilities(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    capability: Optional[list[str]] = None
    """
    Set a list of capabilities to override capabilities provided in device's hello message.
    Can be used for devices that do not report any yang modules in their hello message
    """
    override: Optional[bool] = None
    """
    Whether to override or merge this list of capabilities with capabilities from device
    """


class Flags(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    streaming_session: Optional[bool] = Field(None, alias='streaming-session')
    """
    NETCONF session is created and optimized for receiving of NETCONF notifications
    from remote server.
    """
    enabled_notifications: Optional[bool] = Field(None, alias='enabled-notifications')
    """
    If it is set to 'true' and NETCONF device supports notifications, NETCONF mountpoint will
    expose NETCONF notification and subscription services.
    """
    reconnect_on_changed_schema: Optional[bool] = Field(
        None, alias='reconnect-on-changed-schema'
    )
    """
    If it is set to 'true', NETCONF notifications are supported by device, and NETCONF
    notifications are enabled ('enabled-notifications' flag), the connector would auto
    disconnect/reconnect when schemas are changed in the remote device. The connector subscribes
    (right after connect) to base netconf notifications and listens
    for netconf-capability-change notification
    """
    enabled_strict_parsing: Optional[bool] = Field(None, alias='enabled-strict-parsing')
    """
    If this parameter is set to 'false', then parser should ignore unknown elements and not throw
    exception during parsing.
    """


class NetconfNodeTopologyYangLibrary(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    password: Optional[str] = None
    yang_library_url: Optional[str] = Field(None, alias='yang-library-url')
    """
    Yang library to be plugged as additional source provider into the shared schema repository
    """
    username: Optional[str] = None


class NetconfNodeTopologyOdlHelloMessageCapabilities(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    capability: Optional[list[str]] = None
    """
    Certain devices are non-accepting of ODL's hello message.  This allows specification of
    a custom ODL hello message based on a list of supported capabilities.
    """


class NetconfSubscriptionsStreamItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    stop_time: Optional[str] = Field(None, alias='stop-time')
    """
    RFC5277: An optional parameter, <stopTime>, used with the optional replay feature to indicate the newest
    notifications of interest. If <stopTime> is not present, the notifications will continue until the
    subscription is terminated. Must be used with and be later than <startTime>. Values of <stopTime>
    in the future are valid.
    """
    start_time: Optional[str] = Field(None, alias='start-time')
    """
    RFC5277: A parameter, <startTime>, used to trigger the replay feature and indicate that the replay
    should start at the time specified. If <startTime> is not present, this is not a replay subscription.
    It is not valid to specify start times that are later than the current time. If the <startTime> specified
    is earlier than the log can support, the replay will begin with the earliest available notification.
    """
    stream_name: Optional[str] = Field(None, alias='stream-name')
    """
    Identifier of the notification stream.
    """


class NetconfNodeTopologyNonModuleCapabilities(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    capability: Optional[list[str]] = None
    """
    Set a list of non-module based capabilities to override or merge non-module capabilities
    provided in device's hello message. Can be used for devices that do not report or
    incorrectly report non-module based capabilities in their hello message
    """
    override: Optional[bool] = None
    """
    Whether to override or merge this list of non-module based capabilities with non-module
    based capabilities from device
    """


class KeyBased(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    key_id: Optional[str] = Field(None, alias='key-id')
    username: Optional[str] = None


class SessionTimers(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    keepalive_delay: Optional[float] = Field(
        None, alias='keepalive-delay', ge=0.0, le=4294967295.0
    )
    """
    Netconf connector sends keepalive RPCs while the session is idle, this delay specifies the delay between keepalive RPC in seconds
    If a value <1 is provided, no keepalives will be sent
    """
    max_reconnection_attempts: Optional[float] = Field(
        None, alias='max-reconnection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of reconnect retries. Non positive value or null is interpreted as infinity.
    This is an optional parameter. If set, max-connection-attempts will be used only once, for the first connection attempts
    and for any subsequent disconnect-connect cycles, max-reconnect-attempts will be used.
    This enables users using different amount of reconnects for initial attempts vs subsequent reconnects.
    """
    reconnenction_attempts_multiplier: Optional[int] = Field(
        None,
        alias='reconnenction-attempts-multiplier',
        ge=-922337203685477630,
        le=922337203685477630,
    )
    """
    After each reconnection attempt, the delay between reconnection attempts is
    multiplied by this factor. By default, it is set to 1.5. This means that the next
    delay between attempts will be 3000 ms, then it will be 4500 ms, etc.
    """
    confirm_commit_timeout: Optional[float] = Field(
        None, alias='confirm-commit-timeout', ge=0.0, le=4294967295.0
    )
    """
    Timeout period in seconds to issued commit after confirmed-commit
    """
    request_transaction_timeout: Optional[float] = Field(
        None, alias='request-transaction-timeout', ge=0.0, le=4294967295.0
    )
    """
    Timeout in seconds for blocking operations within transactions.
    """
    max_connection_attempts: Optional[float] = Field(
        None, alias='max-connection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of connection retries. Non positive value or null is interpreted as infinity.
    """
    initial_connection_timeout: Optional[float] = Field(
        None, alias='initial-connection-timeout', ge=0.0, le=4294967295.0
    )
    """
    Specifies timeout in seconds after which connection must be established.
    """
    between_attempts_timeout: Optional[int] = Field(
        None, alias='between-attempts-timeout', ge=0, le=65535
    )
    """
    Initial timeout in seconds to wait between connection attempts.
    Will be multiplied by reconenction-attempts-multiplier with every additional attempt
    """


class LoginPasswordUnencrypted(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    password: Optional[str] = None
    username: Optional[str] = None


class LoginPassword(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    password: Optional[str] = None
    username: Optional[str] = None


class UniconfigConfigCrypto(BaseModel):
    """
    Settings related to encryption of arbitrary leaves/leaf-list using public key that
    is read from device on specified path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    public_key_path: Optional[str] = Field(None, alias='public-key-path')
    """
    Path to leaf containing public key in Base64 binary format.
    """
    public_key_cipher_type: Optional[config.PublicKeyCipherType] = Field(
        None, alias='public-key-cipher-type'
    )


class Cli(BaseModel):
    """
    CLI node settings.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cli_topology_device_type: Optional[str] = Field(
        None, alias='cli-topology:device-type'
    )
    uniconfig_config_confirmed_commit_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:confirmed-commit-enabled'
    )
    """
    Specifies whether to send confirmed commit RPC between validate RPC and confirming commit.
    """
    uniconfig_config_replace_paths: Optional[list[str]] = Field(
        None, alias='uniconfig-config:replace-paths'
    )
    """
    Replace paths that point to config that should be handled as a one replace request
    """
    cli_topology_resend_command_delay: Optional[int] = Field(
        None, alias='cli-topology:resend-command-delay', ge=0, le=65535
    )
    """
    Delay between re-send commands.
    """
    secret: Optional[str] = None
    """
    Privileged EXEC mode password for Cisco IOS devices. If not set credentials
    password will be used
    """
    cli_topology_dry_run_journal_size: Optional[int] = Field(
        None, alias='cli-topology:dry-run-journal-size', ge=0, le=65535
    )
    """
    Size of the DRY RUN cli mountpoint jounral. DRY RUN journal captures commands that would be
    executed when reading/writing some configuration. However the commands are not actually sent
    to the device
    """
    keepalive_initial_delay: Optional[int] = Field(
        None, alias='keepalive-initial-delay', ge=0, le=65535
    )
    uniconfig_config_store_failed_installation: Optional[bool] = Field(
        None, alias='uniconfig-config:store-failed-installation'
    )
    """
    In case UniConfig fails to install the device, it will still populate the database.
    """
    password: Optional[str] = None
    keepalive_timeout: Optional[int] = Field(
        None, alias='keepalive-timeout', ge=0, le=65535
    )
    cli_topology_max_connection_attempts_install: Optional[float] = Field(
        None,
        alias='cli-topology:max-connection-attempts-install',
        ge=0.0,
        le=4294967295.0,
    )
    """
    Maximum number of connection attempts used during installation of device.
    Value 0 disables the limit
    """
    uniconfig_config_crypto: Optional[UniconfigConfigCrypto] = Field(
        None,
        alias='uniconfig-config:crypto',
        title='uniconfig.config.uniconfigconfignodefields.Crypto',
    )
    """
    Settings related to encryption of arbitrary leaves/leaf-list using public key that
    is read from device on specified path.
    """
    cli_topology_max_resend_command_attempt: Optional[float] = Field(
        None, alias='cli-topology:max-resend-command-attempt', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of re-send commands that are sent to device after first attempt.
    Value 0 disables resending.
    """
    cli_topology_max_reconnection_attempts: Optional[float] = Field(
        None, alias='cli-topology:max-reconnection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of reconnect retries. Non positive value or null is interpreted as infinity.
    This is an optional parameter. If set, max-connection-attempts will be used only once,
    for the first connection attempts and for any subsequent disconnect-connect cycles,
    max-reconnect-attempts will be used. This enables users using different amount of reconnects
    for initial attempts vs subsequent reconnects.
    """
    uniconfig_config_install_uniconfig_node_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:install-uniconfig-node-enabled'
    )
    connection_lazy_timeout: Optional[int] = Field(
        None, alias='connection-lazy-timeout', ge=0, le=65535
    )
    """
    Maximal time (in seconds) for connection to keep alive, if no activity was detected
    in the session and the timeout has been reached, connection will be stopped
    """
    cli_topology_device_version: Optional[str] = Field(
        None, alias='cli-topology:device-version'
    )
    cli_topology_max_connection_attempts: Optional[float] = Field(
        None, alias='cli-topology:max-connection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of connection attempts before connection initialization is marked as failed.
    Value 0 disables this limit.
    """
    connection_establish_timeout: Optional[int] = Field(
        None, alias='connection-establish-timeout', ge=0, le=65535
    )
    """
    Maximal time (in seconds) for connection establishment, if a connection attempt does
    not succeed in this time, the attempt is considered a failure
    """
    uniconfig_config_admin_state: Optional[config.AdminState] = Field(
        None, alias='uniconfig-config:admin-state'
    )
    cli_topology_pass_through: Optional[dict[str, Any]] = Field(
        None,
        alias='cli-topology:pass-through',
        title='cli.topology.clinodeconnectionstatus.PassThrough',
    )
    """
    When the underlying node is connected, its cli context
    is available verbatim under this container through the
    mount extension.
    """
    cli_topology_host: Optional[str] = Field(None, alias='cli-topology:host')
    cli_topology_default_error_patterns: Optional[
        CliTopologyDefaultErrorPatterns
    ] = Field(
        None,
        alias='cli-topology:default-error-patterns',
        title='cli.translate.registry.errorpatterns.DefaultErrorPatterns',
    )
    """
    Device specific list of error patterns. This list is the primary source
    of error checking on the device. This list can be overridden from the code.
    """
    cli_topology_transport_type: Optional[topology.TransportTypeEnumeration] = Field(
        None, alias='cli-topology:transport-type'
    )
    blacklist: Optional[Blacklist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.bl.Blacklist'
    )
    """
    Reads which are not invoked for sync-from-network and initial config read.
    """
    uniconfig_config_validation_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:validation-enabled'
    )
    """
    Specifies whether to send validate RPC before commit RPC.
    """
    whitelist: Optional[Whitelist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.wl.Whitelist'
    )
    """
    Reads which are invoked for sync-from-network and initial config read.
    """
    cli_topology_default_commit_error_patterns: Optional[
        CliTopologyDefaultCommitErrorPatterns
    ] = Field(
        None,
        alias='cli-topology:default-commit-error-patterns',
        title='cli.translate.registry.errorcommitpatterns.DefaultCommitErrorPatterns',
    )
    """
    Device specific list of commit error patterns. The following list
    of patterns is checked in the input after 'commit' command is sent.
    """
    cli_topology_journal_level: Optional[topology.JournalLevel] = Field(
        None, alias='cli-topology:journal-level'
    )
    uniconfig_config_sequence_read_active: Optional[bool] = Field(
        None, alias='uniconfig-config:sequence-read-active'
    )
    """
    Forces reading of data sequentially when mounting device.
    """
    keepalive_delay: Optional[int] = Field(
        None, alias='keepalive-delay', ge=0, le=65535
    )
    cli_topology_journal_size: Optional[int] = Field(
        None, alias='cli-topology:journal-size', ge=0, le=65535
    )
    """
    Size of the cli mountpoint jounral. Journal keeps track of executed commands and makes
    them available for users/apps for debugging purposes. Value 0 disables journaling
    """
    command_timeout: Optional[int] = Field(
        None, alias='command-timeout', ge=0, le=65535
    )
    """
    Maximal time (in seconds) for command execution, if a command cannot be executed on
    a device in this time, the execution is considered a failure
    """
    uniconfig_config_uniconfig_native_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:uniconfig-native-enabled'
    )
    cli_topology_port: Optional[int] = Field(
        None, alias='cli-topology:port', ge=0, le=65535
    )
    cli_topology_parsing_engine: Optional[topology.ParsingEngine] = Field(
        None, alias='cli-topology:parsing-engine'
    )
    username: Optional[str] = None


class OtherParameters(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    concurrent_rpc_limit: Optional[int] = Field(
        None, alias='concurrent-rpc-limit', ge=0, le=65535
    )
    """
    Limit of concurrent messages that can be send before reply messages are received.
    If value <1 is provided, no limit will be enforced
    """
    dry_run_journal_size: Optional[int] = Field(
        None, alias='dry-run-journal-size', ge=0, le=65535
    )
    """
    Size of the DRY RUN netconf mountpoint journal. DRY RUN journal captures netconf RPCs that
    would be executed when reading/writing some configuration. However the RPCs are not actually
    sent to the device
    """
    custom_connector_factory: Optional[str] = Field(
        None, alias='custom-connector-factory'
    )
    """
    Specification of the custom NETCONF connector factory. For example,
               if device doesn't support candidate data-store, this parameter
               should be set to 'netconf-customization-alu-ignore-candidate' string.
    """
    edit_config_test_option: Optional[topology_1.EditConfigTestOption] = Field(
        None, alias='edit-config-test-option'
    )


class Netconf(BaseModel):
    """
    NETCONF node settings.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    concurrent_rpc_limit: Optional[int] = Field(
        None, alias='concurrent-rpc-limit', ge=0, le=65535
    )
    """
    Limit of concurrent messages that can be send before reply messages are received.
    If value <1 is provided, no limit will be enforced
    """
    uniconfig_config_confirmed_commit_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:confirmed-commit-enabled'
    )
    """
    Specifies whether to send confirmed commit RPC between validate RPC and confirming commit.
    """
    uniconfig_config_replace_paths: Optional[list[str]] = Field(
        None, alias='uniconfig-config:replace-paths'
    )
    """
    Replace paths that point to config that should be handled as a one replace request
    """
    max_reconnection_attempts: Optional[float] = Field(
        None, alias='max-reconnection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of reconnect retries. Non positive value or null is interpreted as infinity.
    This is an optional parameter. If set, max-connection-attempts will be used only once, for the first connection attempts
    and for any subsequent disconnect-connect cycles, max-reconnect-attempts will be used.
    This enables users using different amount of reconnects for initial attempts vs subsequent reconnects.
    """
    netconf_node_topology_tcp_only: Optional[bool] = Field(
        None, alias='netconf-node-topology:tcp-only'
    )
    streaming_session: Optional[bool] = Field(None, alias='streaming-session')
    """
    NETCONF session is created and optimized for receiving of NETCONF notifications
    from remote server.
    """
    netconf_node_topology_yang_module_capabilities: Optional[
        NetconfNodeTopologyYangModuleCapabilities
    ] = Field(
        None,
        alias='netconf-node-topology:yang-module-capabilities',
        title='netconf.node.topology.netconfnodeconnectionparameters.YangModuleCapabilities',
    )
    max_connection_attempts: Optional[float] = Field(
        None, alias='max-connection-attempts', ge=0.0, le=4294967295.0
    )
    """
    Maximum number of connection retries. Non positive value or null is interpreted as infinity.
    """
    reconnect_on_changed_schema: Optional[bool] = Field(
        None, alias='reconnect-on-changed-schema'
    )
    """
    If it is set to 'true', NETCONF notifications are supported by device, and NETCONF
    notifications are enabled ('enabled-notifications' flag), the connector would auto
    disconnect/reconnect when schemas are changed in the remote device. The connector subscribes
    (right after connect) to base netconf notifications and listens
    for netconf-capability-change notification
    """
    dry_run_journal_size: Optional[int] = Field(
        None, alias='dry-run-journal-size', ge=0, le=65535
    )
    """
    Size of the DRY RUN netconf mountpoint journal. DRY RUN journal captures netconf RPCs that
    would be executed when reading/writing some configuration. However the RPCs are not actually
    sent to the device
    """
    flags: Optional[Flags] = Field(
        None, title='netconf.node.topology.netconfparametersgroups.Flags'
    )
    netconf_node_topology_port: Optional[int] = Field(
        None, alias='netconf-node-topology:port', ge=0, le=65535
    )
    netconf_node_topology_yang_library: Optional[
        NetconfNodeTopologyYangLibrary
    ] = Field(
        None,
        alias='netconf-node-topology:yang-library',
        title='netconf.node.topology.netconfschemastorage.YangLibrary',
    )
    netconf_node_topology_odl_hello_message_capabilities: Optional[
        NetconfNodeTopologyOdlHelloMessageCapabilities
    ] = Field(
        None,
        alias='netconf-node-topology:odl-hello-message-capabilities',
        title='netconf.node.topology.netconfnodeconnectionparameters.OdlHelloMessageCapabilities',
    )
    strict_parsing: Optional[bool] = Field(None, alias='strict-parsing')
    """
    If this parameter is set to 'false', then parser should ignore unknown elements and not throw
    exception during parsing.
    """
    uniconfig_config_store_failed_installation: Optional[bool] = Field(
        None, alias='uniconfig-config:store-failed-installation'
    )
    """
    In case UniConfig fails to install the device, it will still populate the database.
    """
    password: Optional[str] = None
    enabled_notifications: Optional[bool] = Field(None, alias='enabled-notifications')
    """
    If it is set to 'true' and NETCONF device supports notifications, NETCONF mountpoint will
    expose NETCONF notification and subscription services.
    """
    confirm_timeout: Optional[float] = Field(
        None, alias='confirm-timeout', ge=0.0, le=4294967295.0
    )
    """
    Timeout period in seconds to issued commit after confirmed-commit
    """
    sleep_factor: Optional[int] = Field(
        None, alias='sleep-factor', ge=-922337203685477630, le=922337203685477630
    )
    """
    After each reconnection attempt, the delay between reconnection attempts is
    multiplied by this factor. By default, it is set to 1.5. This means that the next
    delay between attempts will be 3000 ms, then it will be 4500 ms, etc.
    """
    uniconfig_config_crypto: Optional[UniconfigConfigCrypto] = Field(
        None,
        alias='uniconfig-config:crypto',
        title='uniconfig.config.uniconfigconfignodefields.Crypto',
    )
    """
    Settings related to encryption of arbitrary leaves/leaf-list using public key that
    is read from device on specified path.
    """
    other_parameters: Optional[OtherParameters] = Field(
        None,
        alias='other-parameters',
        title='netconf.node.topology.netconfparametersgroups.OtherParameters',
    )
    uniconfig_config_install_uniconfig_node_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:install-uniconfig-node-enabled'
    )
    netconf_node_topology_schema_cache_directory: Optional[str] = Field(
        None, alias='netconf-node-topology:schema-cache-directory'
    )
    """
    The destination schema repository for yang files relative to the cache directory.  This may be specified per netconf mount
    so that the loaded yang files are stored to a distinct directory to avoid potential conflict.
    """
    between_attempts_timeout_millis: Optional[int] = Field(
        None, alias='between-attempts-timeout-millis', ge=0, le=65535
    )
    """
    Initial timeout in milliseconds to wait between connection attempts. Will be multiplied by sleep-factor with every additional attempt
    """
    netconf_node_topology_pass_through: Optional[dict[str, Any]] = Field(
        None,
        alias='netconf-node-topology:pass-through',
        title='netconf.node.topology.netconfnodeconnectionstatus.PassThrough',
    )
    """
    When the underlying node is connected, its NETCONF context
    is available verbatim under this container through the
    mount extension.
    """
    netconf_subscriptions_stream: Optional[
        list[NetconfSubscriptionsStreamItem]
    ] = Field(None, alias='netconf-subscriptions:stream')
    """
    List of available streams to which subscription can be created.
    """
    netconf_node_topology_non_module_capabilities: Optional[
        NetconfNodeTopologyNonModuleCapabilities
    ] = Field(
        None,
        alias='netconf-node-topology:non-module-capabilities',
        title='netconf.node.topology.netconfnodeconnectionparameters.NonModuleCapabilities',
    )
    netconf_node_topology_schemaless: Optional[bool] = Field(
        None, alias='netconf-node-topology:schemaless'
    )
    edit_config_test_option: Optional[topology_1.EditConfigTestOption] = Field(
        None, alias='edit-config-test-option'
    )
    uniconfig_config_admin_state: Optional[config.AdminState] = Field(
        None, alias='uniconfig-config:admin-state'
    )
    key_based: Optional[KeyBased] = Field(
        None,
        alias='key-based',
        title='netconf.node.topology.netconfnodecredentials.credentials.keyauth.KeyBased',
    )
    blacklist: Optional[Blacklist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.bl.Blacklist'
    )
    """
    Reads which are not invoked for sync-from-network and initial config read.
    """
    uniconfig_config_validation_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:validation-enabled'
    )
    """
    Specifies whether to send validate RPC before commit RPC.
    """
    session_timers: Optional[SessionTimers] = Field(
        None,
        alias='session-timers',
        title='netconf.node.topology.netconfparametersgroups.SessionTimers',
    )
    whitelist: Optional[Whitelist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.wl.Whitelist'
    )
    """
    Reads which are invoked for sync-from-network and initial config read.
    """
    uniconfig_config_sequence_read_active: Optional[bool] = Field(
        None, alias='uniconfig-config:sequence-read-active'
    )
    """
    Forces reading of data sequentially when mounting device.
    """
    keepalive_delay: Optional[float] = Field(
        None, alias='keepalive-delay', ge=0.0, le=4294967295.0
    )
    """
    Netconf connector sends keepalive RPCs while the session is idle, this delay specifies the delay between keepalive RPC in seconds
    If a value <1 is provided, no keepalives will be sent
    """
    netconf_node_topology_host: Optional[str] = Field(
        None, alias='netconf-node-topology:host'
    )
    default_request_timeout_millis: Optional[float] = Field(
        None, alias='default-request-timeout-millis', ge=0.0, le=4294967295.0
    )
    """
    Timeout in milliseconds for blocking operations within transactions.
    """
    connection_timeout_millis: Optional[float] = Field(
        None, alias='connection-timeout-millis', ge=0.0, le=4294967295.0
    )
    """
    Specifies timeout in milliseconds after which connection must be established.
    """
    login_password_unencrypted: Optional[LoginPasswordUnencrypted] = Field(
        None,
        alias='login-password-unencrypted',
        title='netconf.node.topology.netconfnodecredentials.credentials.loginpwunencrypted.LoginPasswordUnencrypted',
    )
    customization_factory: Optional[str] = Field(None, alias='customization-factory')
    """
    Specification of the custom NETCONF connector factory. For example,
    if device doesn't support candidate data-store, this parameter
    should be set to 'netconf-customization-alu-ignore-candidate' string.
    """
    login_password: Optional[LoginPassword] = Field(
        None,
        alias='login-password',
        title='netconf.node.topology.netconfnodecredentials.credentials.loginpw.LoginPassword',
    )
    uniconfig_config_uniconfig_native_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:uniconfig-native-enabled'
    )
    username: Optional[str] = None


class Gnmi(BaseModel):
    """
    gNMI node settings.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    uniconfig_config_sequence_read_active: Optional[bool] = Field(
        None, alias='uniconfig-config:sequence-read-active'
    )
    """
    Forces reading of data sequentially when mounting device.
    """
    uniconfig_config_confirmed_commit_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:confirmed-commit-enabled'
    )
    """
    Specifies whether to send confirmed commit RPC between validate RPC and confirming commit.
    """
    uniconfig_config_replace_paths: Optional[list[str]] = Field(
        None, alias='uniconfig-config:replace-paths'
    )
    """
    Replace paths that point to config that should be handled as a one replace request
    """
    uniconfig_config_store_failed_installation: Optional[bool] = Field(
        None, alias='uniconfig-config:store-failed-installation'
    )
    """
    In case UniConfig fails to install the device, it will still populate the database.
    """
    uniconfig_config_admin_state: Optional[config.AdminState] = Field(
        None, alias='uniconfig-config:admin-state'
    )
    uniconfig_config_crypto: Optional[UniconfigConfigCrypto] = Field(
        None,
        alias='uniconfig-config:crypto',
        title='uniconfig.config.uniconfigconfignodefields.Crypto',
    )
    """
    Settings related to encryption of arbitrary leaves/leaf-list using public key that
    is read from device on specified path.
    """
    blacklist: Optional[Blacklist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.bl.Blacklist'
    )
    """
    Reads which are not invoked for sync-from-network and initial config read.
    """
    uniconfig_config_validation_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:validation-enabled'
    )
    """
    Specifies whether to send validate RPC before commit RPC.
    """
    uniconfig_config_uniconfig_native_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:uniconfig-native-enabled'
    )
    uniconfig_config_install_uniconfig_node_enabled: Optional[bool] = Field(
        None, alias='uniconfig-config:install-uniconfig-node-enabled'
    )
    whitelist: Optional[Whitelist] = Field(
        None, title='uniconfig.config.uniconfigconfignodefields.nodes.wl.Whitelist'
    )
    """
    Reads which are invoked for sync-from-network and initial config read.
    """


class Node(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: str = Field(..., alias='node-id')
    """
    Node identifier of CLI/NETCONF/GNMI node.
    """
    cli: Optional[Cli] = Field(
        None, title='connection.manager.installmultiplenodes.input.nodes.Cli'
    )
    """
    CLI node settings.
    """
    netconf: Optional[Netconf] = Field(
        None, title='connection.manager.installmultiplenodes.input.nodes.Netconf'
    )
    """
    NETCONF node settings.
    """
    gnmi: Optional[Gnmi] = Field(
        None, title='connection.manager.installmultiplenodes.input.nodes.Gnmi'
    )
    """
    gNMI node settings.
    """


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    nodes: Optional[list[Node]] = None


class NodeResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    node_id: str = Field(..., alias='node-id')
    """
    Node identifier of CLI/NETCONF/GNMI node.
    """
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Message that described occurred error during invocation of operation on a specific node.
    """
    status: types.OperationResultType


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_results: Optional[list[NodeResult]] = Field(None, alias='node-results')
    overall_status: types.OperationResultType = Field(..., alias='overall-status')

import logging

from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv

from pysnmp.proto.secmod.rfc3826.priv import aes
from pysnmp.proto.secmod.rfc3414.auth import hmacsha
from pysnmp.proto import rfc1902

from splunk_connect_for_snmp_traps.manager.hec_sender import HecSender
from splunk_connect_for_snmp_traps.manager.mib_server_client import get_translation
from splunk_connect_for_snmp_traps.manager.const import AuthProtocolMap, PrivProtocolMap
import socket
import os


# *TODO*: enable debug all only if end-user has set debug logging mode.
# debugging log for SNMPv3 trap
from pysnmp import debug

debug.setLogger(debug.Debug("all"))

logger = logging.getLogger(__name__)


class TrapServer:
    def __init__(self, args, server_config):
        self._args = args
        self._server_config = server_config
        self._snmp_engine = engine.SnmpEngine()
        self.configure_trap_server()
        self._hec_sender = HecSender(args, self._server_config)

    def configure_trap_server(self):
        self._snmp_engine.observer.registerObserver(
            self.request_observer,
            "rfc3412.receiveMessage:request",
            "rfc3412.returnResponsePdu",
        )
        snmp_config = self._server_config["snmp"]
        if self._args.ipv4:
            config.addTransport(
                self._snmp_engine,
                udp.domainName,
                udp.UdpTransport().openServerMode(("0.0.0.0", self._args.port)),
            )
        if self._args.ipv6:
            config.addTransport(
                self._snmp_engine,
                udp6.domainName,
                udp6.Udp6Transport().openServerMode(("::0", self._args.port)),
            )
        # SNMPv1/2c setup
        # SecurityName <-> CommunityName mapping
        """
        test snmptrap command:
        v1: 
        sudo snmptrap -v 1 -c public localhost:2162 '1.2.3.4.5.6' '192.193.194.195' 6 99 '55' 1.11.12.13.14.15  s "teststring"
        v2c:
        sudo snmptrap -v 2c -c public localhost:2162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s test2

        """
        for community in snmp_config["communities"].get("v1", None):
            logger.info(f"Configuring V1 {community}")
            config.addV1System(self._snmp_engine, community, community)

        for community in snmp_config["communities"].get("v2", None):
            logger.info(f"Configuring V1 {community}")
            config.addV1System(self._snmp_engine, community, community)

        # SNMPv3/USM setup
        """
        SNMPv3 params for addV3User(
            snmpEngine,
            userName,
            authProtocal: MD5(default),
            authKey,
            privProtocal: DES(default),
            engineID: snmptrap command should specify the same egienID by using option -e
        )

        test snmptrap command:
        user1: snmpv3test
        sudo snmptrap -v 3 -e 0x8000000004030201 -l noAuthNoPriv -u snmpv3test localhost:2162 123 1.3.6.1.6.3.1.1.5.1
        sudo snmptrap -v 3 -e 0x8000000004030201 -l authPriv -u snmpv3test -A AuthPass1 -X PrivPass2 localhost:2162 2 1.3.6.1.2.1.1.3.0
        sudo snmptrap -v 3 -e 0x8000000004030201 -l authPriv -u snmpv3test -a MD5 -A AuthPass1 -x DES -X PrivPass2 localhost:2162 ''  1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 i 60

        user2: snmpv3test2
        sudo snmptrap -v 3 -e 0x8000000004030202 -l noAuthNoPriv -u snmpv3test2 localhost:2162 123 1.3.6.1.6.3.1.1.5.1
        sudo snmptrap -v 3 -e 0x8000000004030202 -l authPriv -u snmpv3test2 -a SHA -A AuthPass11 -x AES -X PrivPass22 localhost:2162 ''  1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 i 120
        
        user3: snmpv3test3
        sudo snmptrap -e 0x8000000004030203 -v3 -l noAuthNoPriv -u snmpv3test3 localhost:2162 123 1.3.6.1.6.3.1.1.5.1
        """
        for user_config in snmp_config["communities"].get("v3", None):
            # user_config = snmp_config["communities"]["v3"].get(user)
            logger.info(f"Configuring V3 {user_config}")
            username = user_config.get("userName", None)
            authprotocol = AuthProtocolMap[
                user_config.get("authProtocol", "NONE").upper()
            ]
            authkey = user_config.get("authKey", None)
            # authProtocol default is NoAuth if authKey is None
            # authProtocol default is MD5 if authKey is given
            if user_config.get("authProtocol", None) is None and authkey is not None:
                authprotocol = AuthProtocolMap[
                    user_config.get("authProtocol", "MD5").upper()
                ]
            privprotocol = PrivProtocolMap[
                user_config.get("privProtocol", "NONE").upper()
            ]
            privkey = user_config.get("privKey", None)
            # privProtocol default is NoPriv if privKey is None
            # privProtocol default is DES if privKey is given
            if user_config.get("privProtocol", None) is None and privkey is not None:
                privprotocol = PrivProtocolMap[
                    user_config.get("privProtocol", "DES").upper()
                ]
            securityengineId = user_config.get("securityEngineId", None)
            if securityengineId:
                securityengineId = rfc1902.OctetString(hexValue=str(securityengineId))
            logger.info(
                f"V3 params: username: {username}, authprotocol: {user_config.get('authProtocol', None)}-{authprotocol}, authkey: {authkey}, privprotocol: {user_config.get('privProtocol', None)}-{privprotocol}, privkey: {privkey}, securityengineId: {securityengineId}"
            )
            config.addV3User(
                self._snmp_engine,
                username,
                authprotocol,
                authkey,
                privprotocol,
                privkey,
                securityengineId,
            )
        logger.debug(f"config: {config}")

        # Register SNMP Application at the SNMP engine
        ntfrcv.NotificationReceiver(self._snmp_engine, self.snmp_callback_function)

    # Register a callback to be invoked at specified execution point of
    # SNMP Engine and passed local variables at code point's local scope
    # noinspection PyUnusedLocal,PyUnusedLocal
    def request_observer(self, snmp_engine, execution_point, variables, callback_ctx):
        logger.debug(f'Raw data is "{variables}"')
        logger.debug("Execution point: %s" % execution_point)
        logger.debug(
            "* transportDomain: %s"
            % ".".join([str(x) for x in variables["transportDomain"]])
        )
        logger.debug(
            "* transportAddress: %s"
            % "@".join([str(x) for x in variables["transportAddress"]])
        )
        logger.debug("* securityModel: %s" % variables["securityModel"])
        logger.debug("* securityName: %s" % variables["securityName"])
        logger.debug("* securityLevel: %s" % variables["securityLevel"])
        logger.debug(
            "* contextEngineId: %s" % variables["contextEngineId"].prettyPrint()
        )
        logger.debug("* contextName: %s" % variables["contextName"].prettyPrint())
        logger.debug("* PDU: %s" % variables["pdu"].prettyPrint())

    # Callback function for receiving notifications
    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def snmp_callback_function(
        self,
        snmp_engine,
        state_reference,
        context_engine_id,
        context_name,
        var_binds,
        callback_ctx,
    ):
        logger.debug(
            'Notification from ContextEngineId "%s", ContextName "%s"'
            % (context_engine_id.prettyPrint(), context_name.prettyPrint())
        )
        # Get an execution context...
        execContext = snmp_engine.observer.getExecutionContext(
            "rfc3412.receiveMessage:request"
        )
        logger.debug(
            f'execContext["transportAddress"]: {execContext["transportAddress"]}'
        )
        logger.debug(
            'Notification from %s, ContextEngineId "%s", '
            'ContextName "%s"'
            % (
                "@".join([str(x) for x in execContext["transportAddress"]]),
                context_engine_id.prettyPrint(),
                context_name.prettyPrint(),
            )
        )
        logger.debug(
            f"state_reference: {snmp_engine.msgAndPduDsp.getTransportInfo(state_reference)}"
        )
        transportDomain, transportAddress = snmp_engine.msgAndPduDsp.getTransportInfo(
            state_reference
        )

        logger.debug(
            "Notification from %s, SNMP Engine %s, "
            "Context %s"
            % (
                transportAddress,
                context_engine_id.prettyPrint(),
                context_name.prettyPrint(),
            )
        )
        device_ip = snmp_engine.msgAndPduDsp.getTransportInfo(state_reference)[1][0]
        header = {}
        try:
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(device_ip)
            parts = str(hostname).split(".")
            name = parts[0]
            # print(name)
            if len(parts) > 1:
                header["Agent_Hostname"] = name
                logger.debug(f"host={header['Agent_Hostname']} device_ip={device_ip}")
            else:
                header["Agent_Hostname"] = device_ip
                logger.debug(f"device_ip={device_ip}")
        except:
            logger.debug(f"device_ip={device_ip}")
            header["Agent_Hostname"] = device_ip
            pass

        header["Agent_Address"] = device_ip

        # Send API call to SNMP MIB server to get var_binds translated
        # mib_server_url = self._server_config["snmp"]["mib-server"]["url"]
        mib_server_url = os.environ["MIBS_SERVER_URL"]
        trap_event_string = get_translation(var_binds, mib_server_url)

        self._hec_sender.post_data(device_ip, trap_event_string)

    def run_trap_server(self):
        self._snmp_engine.transportDispatcher.jobStarted(1)
        try:
            self._snmp_engine.transportDispatcher.runDispatcher()
        finally:
            self._snmp_engine.observer.unregisterObserver()
            self._snmp_engine.transportDispatcher.closeDispatcher()

import logging

from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv

from splunk_connect_for_snmp_traps.manager.hec_sender import HecSender
from splunk_connect_for_snmp_traps.manager.mib_server_client import get_translation
import socket
import os

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
        for community in snmp_config["communities"]["v1"]:
            logger.info(f"Configuring V1 {community}")
            config.addV1System(self._snmp_engine, community, community)
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
        mib_server_url = os.environ['MIBS_SERVER_URL']
        trap_event_string = get_translation(var_binds, mib_server_url)
        
        self._hec_sender.post_data(header["Agent_Hostname"], trap_event_string)

    def run_trap_server(self):
        self._snmp_engine.transportDispatcher.jobStarted(1)
        try:
            self._snmp_engine.transportDispatcher.runDispatcher()
        finally:
            self._snmp_engine.observer.unregisterObserver()
            self._snmp_engine.transportDispatcher.closeDispatcher()

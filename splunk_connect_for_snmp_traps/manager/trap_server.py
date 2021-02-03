import logging

from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv

from splunk_connect_for_snmp_traps.manager.hec_sender import HecSender
from splunk_connect_for_snmp_traps.manager.translator import Translator

from pysnmp.smi import builder, view, compiler, rfc1902
import os
import json
import csv

logger = logging.getLogger(__name__)


class TrapServer:
    def __init__(self, args, server_config):
        self._args = args
        self._server_config = server_config
        self._snmp_engine = engine.SnmpEngine()
        self.configure_trap_server()
        self._hec_sender = HecSender(args, self._server_config)
        self._translator = Translator(server_config)

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
        # Translate the var_binds to MIB objects
        trap_event_string = self._translator.format_trap_event(var_binds)
        self._hec_sender.post_data(trap_event_string)

    def run_trap_server(self):
        self._snmp_engine.transportDispatcher.jobStarted(1)
        try:
            self._snmp_engine.transportDispatcher.runDispatcher()
        finally:
            self._snmp_engine.observer.unregisterObserver()
            self._snmp_engine.transportDispatcher.closeDispatcher()

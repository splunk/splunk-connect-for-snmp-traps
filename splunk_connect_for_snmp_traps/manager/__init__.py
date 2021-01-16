import logging.config

from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity.rfc3413 import ntfrcv

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)


def trap_server(port, server_config):
    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher
    snmpEngine = engine.SnmpEngine()

    snmpEngine.observer.registerObserver(
        requestObserver, "rfc3412.receiveMessage:request", "rfc3412.returnResponsePdu"
    )

    # UDP over IPv4
    if server_config["ipv4"]:
        config.addTransport(
            snmpEngine,
            udp.domainName,
            udp.UdpTransport().openServerMode(("127.0.0.1", port)),
        )

    # UDP over IPv6
    if server_config["ipv6"]:
        config.addTransport(
            snmpEngine,
            udp6.domainName,
            udp6.Udp6Transport().openServerMode(("::1", port)),
        )

    # SNMPv1/2c setup

    # SecurityName <-> CommunityName mapping
    for community in server_config["communities"]["v1"]:
        logger.info(f"Configuring V1 {community}")
        config.addV1System(snmpEngine, community, community)

    # Register SNMP Application at the SNMP engine
    ntfrcv.NotificationReceiver(snmpEngine, cbFun)

    snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

    # Run I/O dispatcher which would receive queries and send confirmations
    try:
        snmpEngine.transportDispatcher.runDispatcher()

    finally:
        snmpEngine.observer.unregisterObserver()
        snmpEngine.transportDispatcher.closeDispatcher()


# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    logger.debug(
        'Notification from ContextEngineId "%s", ContextName "%s"'
        % (contextEngineId.prettyPrint(), contextName.prettyPrint())
    )
    for name, val in varBinds:
        logger.debug("%s = %s" % (name.prettyPrint(), val.prettyPrint()))


# Register a callback to be invoked at specified execution point of
# SNMP Engine and passed local variables at code point's local scope
# noinspection PyUnusedLocal,PyUnusedLocal
def requestObserver(snmpEngine, execpoint, variables, cbCtx):
    logger.debug("Execution point: %s" % execpoint)
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
    logger.debug("* contextEngineId: %s" % variables["contextEngineId"].prettyPrint())
    logger.debug("* contextName: %s" % variables["contextName"].prettyPrint())
    logger.debug("* PDU: %s" % variables["pdu"].prettyPrint())

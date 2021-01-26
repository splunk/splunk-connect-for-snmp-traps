import logging.config

from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.smi import builder, view, compiler, rfc1902

import json

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="snmp_debug.log", level=logging.DEBUG, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
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
    
    
    logger.debug("[snmp_debug] type of varBinds: {}".format(type(varBinds)))
    logger.debug("[snmp_debug] varBinds: {}".format(varBinds))
    for element in varBinds:
        logger.debug("[snmp_debug] type of element: {}".format(type(element)))
        logger.debug("[snmp_debug] element: {}".format(element))


    """
    2021-01-25 15:25:32,947 | splunk_connect_for_snmp_traps.manager | DEBUG | 	 PPType <TagSet object, tags 0:0:6> -> ObjectName = <TagSet object, tags 64:0:3> -> TimeTicks

    """

    for name, val in varBinds:
        logger.debug("\t %s = %s" % (name, val))
        logger.debug("\t PPType %s = %s" % (name.prettyPrintType(), val.prettyPrintType()))
        # logger.debug("\t PPType %s = %s" % (type(name).__name__, type(val).__name__))
        
        
        cursor = "->"
        nameType = name.prettyPrintType()
        if cursor in nameType:
            nameType = nameType.split(cursor)[1].strip()
            
        valType = val.prettyPrintType()
        if cursor in valType:
            valType = valType.split(cursor)[1].strip()
        
        # logger.debug("\t name %s = val %s" % (, ))

        # logger.debug("[snmp_debug] type: %s = %s" % (name.asn1_type(), val.asn1_type()))

        result = {}
        result["oid"] = name.prettyPrint()
        result["value"] = val.prettyPrint()
        result["val_type"] = valType
        result["oid_type"] = nameType
        result["mib"] = pduToMib(name, val)
        
        logger.debug("--- JSON Event ---")
        logger.debug("\n{}".format(json.dumps(result, indent=4, sort_keys=True)))
        logger.debug("--- /JSON Event ---")


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

# Translate SNMP PDU varBinds into MIB objects
def pduToMib(name, val):
    # Assemble MIB browser
    mibBuilder = builder.MibBuilder()
    mibViewController = view.MibViewController(mibBuilder)
    compiler.addMibCompiler(mibBuilder, sources=['file:///usr/share/snmp/mibs',
                                                'http://mibs.snmplabs.com/asn1/@mib@'])

    # Pre-load MIB modules we expect to work with
    mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-COMMUNITY-MIB')

    # Run var-binds through MIB resolver
    try:
        varBind = rfc1902.ObjectType(rfc1902.ObjectIdentity(name), val).resolveWithMib(mibViewController)
        logger.debug("* Translated PDU: %s" % varBind.prettyPrint())
        return varBind.prettyPrint()
    except Exception as e:
        logger.error("Error happended in translateion: %s" % e)
        


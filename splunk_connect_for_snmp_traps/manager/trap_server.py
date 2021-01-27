import logging

from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.smi import builder, view, compiler, rfc1902
# from splunk_connect_for_snmp_traps.utilities import get_custom_translation_table
import os
import json
import csv

logger = logging.getLogger(__name__)


# Register a callback to be invoked at specified execution point of
# SNMP Engine and passed local variables at code point's local scope
# noinspection PyUnusedLocal,PyUnusedLocal
def request_observer(snmp_engine, execution_point, variables, callback_ctx):
    logger.debug(f'Raw data is "{variables}"')
    logger.debug('Execution point: %s' % execution_point)
    logger.debug(
        '* transportDomain: %s'
        % '.'.join([str(x) for x in variables['transportDomain']])
    )
    logger.debug(
        '* transportAddress: %s'
        % '@'.join([str(x) for x in variables['transportAddress']])
    )
    logger.debug('* securityModel: %s' % variables['securityModel'])
    logger.debug('* securityName: %s' % variables['securityName'])
    logger.debug('* securityLevel: %s' % variables['securityLevel'])
    logger.debug('* contextEngineId: %s' % variables['contextEngineId'].prettyPrint())
    logger.debug('* contextName: %s' % variables['contextName'].prettyPrint())
    logger.debug('* PDU: %s' % variables['pdu'].prettyPrint())


# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def snmp_callback_function(snmp_engine, state_reference, context_engine_id, context_name, var_binds, callback_ctx):
    logger.debug(
        'Notification from ContextEngineId "%s", ContextName "%s"'
        % (context_engine_id.prettyPrint(), context_name.prettyPrint())
    )
    trap_event_string = ""
    offset = 0
    customTranslationTable = get_custom_translation_table()
    for name, val in var_binds:
        logger.debug('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        # extract oid and value
        oid = name.prettyPrint()
        value = val.prettyPrint()

        # Extrat the types
        cursor = "->"
        nameType = name.prettyPrintType()
        if cursor in nameType:
            nameType = nameType.split(cursor)[1].strip()
            
        valType = val.prettyPrintType()
        if cursor in valType:
            valType = valType.split(cursor)[1].strip()

        # custom translation 
        custom_translated_oid = custom_translator(customTranslationTable, oid)
        custom_translated_value = value
        # tranlate value ONLY when it is oid
        if valType == "ObjectName":
            custom_translated_value = custom_translator(customTranslationTable, value)

        # Constract the payload 
        # TODO 
        # 1. Clear the debugging statement -> change logging level back to info, remove snmp_debug.log file
        # 2. Refact code 
        offset += 1
        trap_event_string += """
        oid{offset} = {oid}
        oid_type{offset} = {oid_type}
        value{offset} = {value}
        val_type{offset} = {val_type}
        mib{offset} = {mib}
        custom_mib{offset} = {custom_translated_oid} = {custom_translated_value}
        """.format(offset=offset, oid=oid, oid_type=nameType, value=value, val_type=valType, mib=mib_translator(name, val), custom_translated_oid=custom_translated_oid, custom_translated_value=custom_translated_value )
    logger.debug("--- Trap Event String ---")
    logger.debug(trap_event_string)
    logger.debug("--- Sent out Payload---")
    payload = {
        "event": trap_event_string
    }
    logger.debug("\n{}".format(json.dumps(payload, indent=4, sort_keys=True)))



# Translate SNMP PDU varBinds into MIB objects using MIB
def mib_translator(name, val):
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

# Translate SNMP PDU varBinds into MIB objects using custom translation table
def custom_translator(translation_table, oid):
    label = translation_table.get(oid, None)
    return label


# Read the custom mib translation table into memory
def get_custom_translation_table():
    translation_table = {}
    script_dir = os.path.dirname(__file__)  # Script directory
    logger.debug("script_dir %s" % script_dir)
    file_path = os.path.join(script_dir, "../custom_mib_string_table.csv")
    logger.debug("file_path %s" % file_path)
    with open(file_path) as files:
        reader = csv.reader(files)
        next(reader) # skip header
        for row in reader:
            logger.debug("data %s" % row)
            translation_table[row[0]] = row[1]
    return translation_table


def trap_server(port, server_config):
    # Create SNMP engine with autogenerated engineID and pre-bound to socket transport dispatcher
    snmp_engine = engine.SnmpEngine()
    snmp_engine.observer.registerObserver(request_observer, 'rfc3412.receiveMessage:request',
                                          'rfc3412.returnResponsePdu')
    # UDP over IPv4
    if server_config['ipv4']:
        config.addTransport(snmp_engine, udp.domainName, udp.UdpTransport().openServerMode(('127.0.0.1', port)))

    # UDP over IPv6
    if server_config['ipv6']:
        config.addTransport(snmp_engine, udp6.domainName, udp6.Udp6Transport().openServerMode(('::1', port)))

    # SNMPv1/2c setup

    # SecurityName <-> CommunityName mapping
    for community in server_config['communities']['v1']:
        logger.info(f'Configuring V1 {community}')
        config.addV1System(snmp_engine, community, community)

    # Register SNMP Application at the SNMP engine
    ntfrcv.NotificationReceiver(snmp_engine, snmp_callback_function)

    snmp_engine.transportDispatcher.jobStarted(1)  # this job would never finish

    # Run I/O dispatcher which would receive queries and send confirmations
    try:
        snmp_engine.transportDispatcher.runDispatcher()

    finally:
        snmp_engine.observer.unregisterObserver()
        snmp_engine.transportDispatcher.closeDispatcher()

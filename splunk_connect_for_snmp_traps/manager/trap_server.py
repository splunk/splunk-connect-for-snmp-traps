import logging
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity.rfc3413 import ntfrcv

logger = logging.getLogger(__name__)


# Register a callback to be invoked at specified execution point of
# SNMP Engine and passed local variables at code point's local scope
# noinspection PyUnusedLocal,PyUnusedLocal
def request_observer(snmp_engine, execution_point, variables, callback_ctx):
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
    for name, val in var_binds:
        logger.debug('%s = %s' % (name.prettyPrint(), val.prettyPrint()))


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

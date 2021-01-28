import concurrent.futures
import logging

import requests
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv

from splunk_connect_for_snmp_traps.manager.hec_config import HecConfiguration
from splunk_connect_for_snmp_traps.manager.os_config_utils import max_allowed_working_threads

logger = logging.getLogger(__name__)


class TrapServer:
    def __init__(self, server_config):
        self._server_config = server_config
        self._snmp_engine = engine.SnmpEngine()
        self.configure_trap_server()
        self._hec_config = HecConfiguration(self._server_config['hec'])
        self._thread_pool_executor = self.configure_thread_pool()

    def configure_thread_pool(self):
        user_suggested_working_threads = self._server_config['thread-pool']['max-suggested-working-threads']
        max_workers = max_allowed_working_threads(user_suggested_working_threads)
        logger.debug(f'Configured a thread-pool with {max_workers} concurrent threads')
        return concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def configure_trap_server(self):
        self._snmp_engine.observer.registerObserver(self.request_observer, 'rfc3412.receiveMessage:request',
                                                    'rfc3412.returnResponsePdu')
        snmp_config = self._server_config['snmp']
        if snmp_config['ipv4']:
            config.addTransport(self._snmp_engine, udp.domainName,
                                udp.UdpTransport().openServerMode(('127.0.0.1', snmp_config['port'])))
        if snmp_config['ipv6']:
            config.addTransport(self._snmp_engine, udp6.domainName,
                                udp6.Udp6Transport().openServerMode(('::1', snmp_config['port'])))
        # SNMPv1/2c setup
        # SecurityName <-> CommunityName mapping
        for community in snmp_config['communities']['v1']:
            logger.info(f'Configuring V1 {community}')
            config.addV1System(self._snmp_engine, community, community)
        # Register SNMP Application at the SNMP engine
        ntfrcv.NotificationReceiver(self._snmp_engine, self.snmp_callback_function)

    def post_trap_to_hec(self, variables_binds):
        logger.debug('Task received, sleeping for few seconds ...')
        from time import sleep
        sleep(5)
        endpoint = self._hec_config.endpoint()
        headers = {'Authorization': f'Splunk {self._hec_config.get_authentication_token()}'}
        splunk_trap_data = ','.join([str(key) + str(value) for key, value in variables_binds])
        data = {'sourcetype': 'trap-server', 'event': splunk_trap_data}
        logger.debug(f'Posting trap to HEC using {self._hec_config.endpoint()} and headers {headers}')
        response = requests.post(url=endpoint, json=data, headers=headers, verify=False)
        logger.debug(f'Response code is {response.status_code}')

    # Register a callback to be invoked at specified execution point of
    # SNMP Engine and passed local variables at code point's local scope
    # noinspection PyUnusedLocal,PyUnusedLocal
    def request_observer(self, snmp_engine, execution_point, variables, callback_ctx):
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
    def snmp_callback_function(self, snmp_engine, state_reference, context_engine_id, context_name, var_binds,
                               callback_ctx):
        logger.debug(
            'Notification from ContextEngineId "%s", ContextName "%s"'
            % (context_engine_id.prettyPrint(), context_name.prettyPrint())
        )
        for name, val in var_binds:
            logger.debug('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        self._thread_pool_executor.submit(self.post_trap_to_hec, var_binds)

    def run_trap_server(self):
        self._snmp_engine.transportDispatcher.jobStarted(1)
        try:
            self._snmp_engine.transportDispatcher.runDispatcher()
        finally:
            self._snmp_engine.observer.unregisterObserver()
            self._snmp_engine.transportDispatcher.closeDispatcher()
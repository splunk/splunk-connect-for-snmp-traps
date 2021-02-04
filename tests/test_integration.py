import sys

import threading
import time

import yaml
from pysnmp.hlapi import *

from splunk_connect_for_snmp_traps.manager.trap_server import TrapServer
from splunk_connect_for_snmp_traps.snmp_trap_server import parse_arguments
from tests.splunkutils import splunk_single


def start_snmp_server():
    args = parse_arguments(sys.argv[2:])
    config_file = args.config

    with open(config_file, "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    trap_server = TrapServer(args, server_config)
    trap_server.run_trap_server()


def send_trap(host, port, object_identity, *var_binds):
    iterator = sendNotification(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((host, port)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity(object_identity)
        ).addVarBinds(
            *var_binds
        ).loadMibs(
            'SNMPv2-MIB'
        )
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)


def test_integration(setup_splunk):
    th = threading.Thread(target=start_snmp_server)
    th.setDaemon(True)
    th.start()

    # wait for the server to start
    time.sleep(2)

    # send trap
    varbind1 = ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2')
    varbind2 = ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
    send_trap('localhost', 2162, '1.3.6.1.6.3.1.1.5.2', varbind1, varbind2)

    # wait for the message to be processed
    time.sleep(200)

    search_query = 'sourcetype="trap-server" 1.3.6.1.2.1.1.3.00,1.3.6.1.6.3.1.1.4.1.01.3.6.1.6.3.1.1.5.2,1.3.6.1.6.3.18.1.3.0,1.3.6.1.6.3.18.1.4.0public,1.3.6.1.6.3.1.1.4.3.01.3.6.1.4.1.20408.4.1.1.2,1.3.6.1.2.1.1.1.0my system earliest=-20s | head 1'

    resultCount, eventCount = splunk_single(setup_splunk, search_query)

    # run the search on Splunk instance
#        host = 'https://localhost'
#        port = 8089
#        search_url = '/servicesNS/admin/search/search/jobs/export'
#        username = 'admin'
#        password = 'password'

#        response = requests.post(host + ':' + str(port) + search_url, 'search=search ' + search_query, verify=False,
#                                 auth=(username, password))

#        result = etree.fromstring(response.content).xpath("//result/field[@k='_raw']/v")
#        raw = str(etree.tostring(result[0], encoding='utf8', method='text'))[2:]

#        expected1 = '1.3.6.1.2.1.1.3.00,1.3.6.1.6.3.1.1.4.1.01.3.6.1.6.3.1.1.5.2,1.3.6.1.6.3.18.1.3.0'
#        expected2 = '1.3.6.1.6.3.1.1.4.3.01.3.6.1.4.1.20408.4.1.1.2,1.3.6.1.2.1.1.1.0'

#        assert (expected1 in raw)
#        assert (expected2 in raw)

import os
import threading
import time

import requests
import yaml
from lxml import etree
from unittest import TestCase

from splunk_connect_for_snmp_traps.manager.trap_server import TrapServer


def start_snmp_server():
    print('Starting server ....')
    # start Splunk connect for traps
    with open("../config.yaml", "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    trap_server = TrapServer(server_config)
    trap_server.run_trap_server()


class IntegrationTest(TestCase):

    def test_integration(self):
        th = threading.Thread(target=start_snmp_server)
        th.setDaemon(True)
        th.start()

        # wait for the server to start
        time.sleep(2)

        # send trap
        os.system("snmptrap -v 2c -c public localhost:2162 '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 i 123456")

        # wait for the message to be processed
        time.sleep(2)

        # run the search on Splunk instance
        host = 'https://localhost'
        port = 8089
        search_url = '/servicesNS/admin/search/search/jobs/export'
        username = 'admin'
        password = 'password'
        search_query = 'sourcetype="trap-server" earliest=-20s | head 1'

        response = requests.post(host + ':' + str(port) + search_url, 'search=search ' + search_query, verify=False,
                                 auth=(username, password))

        result = etree.fromstring(response.content).xpath("//result/field[@k='_raw']/v")
        raw = str(etree.tostring(result[0], encoding='utf8', method='text'))[2:]

        expected = '1.3.6.1.6.3.1.1.4.1.01.3.6.1.4.1.8072.2.3.0.1,1.3.6.1.4.1.8072.2.3.2.1123456'

        assert (expected in raw)

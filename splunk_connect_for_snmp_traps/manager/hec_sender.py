import concurrent.futures
import logging
import threading

import requests

from splunk_connect_for_snmp_traps.manager.hec_config import HecConfiguration
from splunk_connect_for_snmp_traps.manager.os_config_utils import (
    max_allowed_working_threads,
)

logger = logging.getLogger(__name__)


class HecSender:
    def __init__(self, server_config):
        self._server_config = server_config
        self._hec_config = HecConfiguration()
        self._thread_local = threading.local()
        self._thread_pool_executor = self.configure_thread_pool()

    def configure_thread_pool(self):
        user_suggested_working_threads = self._server_config["thread-pool"][
            "max-suggested-working-threads"
        ]
        max_workers = max_allowed_working_threads(user_suggested_working_threads)
        logger.debug(f"Configured a thread-pool with {max_workers} concurrent threads")
        return concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def get_session(self):
        if not hasattr(self._thread_local, "session"):
            self._thread_local.session = requests.Session()
        return self._thread_local.session

    def post_data_to_thread_pool(self, variables_binds):
        headers = {
            "Authorization": f"Splunk {self._hec_config.get_authentication_token()}"
        }
        data = {"sourcetype": "trap-server", "event": variables_binds}
        try:
            session = self.get_session()
            for endpoint in self._hec_config.get_endpoints():
                response = session.post(
                    url=endpoint, json=data, headers=headers, verify=False
                )
                logger.debug(f"Response code is {response.status_code}")
        except requests.ConnectionError as e:
            logger.error(f"Connection error when sending data to HEC: {e}")

    def post_data(self, variables_binds):
        self._thread_pool_executor.submit(
            self.post_data_to_thread_pool, variables_binds
        )

#   ########################################################################
#   Copyright 2021 Splunk Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#   ########################################################################
import concurrent.futures
import logging
import os
import threading
import time

import requests

from splunk_connect_for_snmp_traps.manager.os_config_utils import (
    max_allowed_working_threads,
)

logger = logging.getLogger(__name__)


class HecSender:
    def __init__(self, args, server_config):
        self._args = args
        self._server_config = server_config
        self._thread_local = threading.local()
        self._thread_pool_executor = self.configure_thread_pool()
        self._endpoint = os.environ["OTEL_SERVER_URL"]

    def configure_thread_pool(self):
        user_suggested_working_threads = self._args.hec_threads
        max_workers = max_allowed_working_threads(user_suggested_working_threads)
        logger.debug(f"Configured a thread-pool with {max_workers} concurrent threads")
        logger.debug(f"Configured Splunk index for SNMP traps: {self._args.index}")
        return concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def get_session(self):
        if not hasattr(self._thread_local, "session"):
            self._thread_local.session = requests.Session()
        return self._thread_local.session

    def post_data_to_thread_pool(self, host, variables_binds):
        data = {
            "time": time.time(),
            "sourcetype": "sc4snmp:traps",
            "host": host,
            "index": self._args.index,
            "event": variables_binds,
        }

        try:
            session = self.get_session()
            response = session.post(url=self._endpoint, json=data)
            logger.debug(f"Response code is {response.status_code}")
        except requests.ConnectionError as e:
            logger.error(f"Connection error when sending data to HEC: {e}")

    def post_data(self, host, variables_binds):
        self._thread_pool_executor.submit(
            self.post_data_to_thread_pool, host, variables_binds
        )

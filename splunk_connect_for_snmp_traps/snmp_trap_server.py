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
import argparse
import logging.config

import yaml

from splunk_connect_for_snmp_traps.manager.trap_server import TrapServer
from splunk_connect_for_snmp_traps.utilities import initialize_signals_handler

logger = logging.getLogger(__name__)


def main():
    logger.info("Startup Config")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--loglevel",
        default="info",
        help="Provide logging level. Example --loglevel debug, default=warning",
    )
    parser.add_argument(
        "-p", "--port", default=2162, help="Port to accept connections on", type=int
    )
    parser.add_argument(
        "--ipv4", default=True, help="accept connections on ipv4", type=bool
    )
    parser.add_argument(
        "--ipv6", default=True, help="accept connections on ipv6", type=bool
    )
    parser.add_argument(
        "--hec_threads", default=10, help="Max http worker thread count", type=int
    )
    parser.add_argument("-c", "--config", default="config.yaml", help="Config File")

    parser.add_argument(
        "-i", "--index", default="##EVENTS_INDEX##", help="Index for traps"
    )

    args = parser.parse_args()

    log_level = args.loglevel.upper()
    config_file = args.config

    logging.getLogger().setLevel(log_level)
    logger.info(f"Log Level is {log_level}")
    logger.info(f"Config file is {config_file}")

    logger.info("Completed Argument parsing")

    with open(config_file, "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    logger.debug(f"Server Config is:  {server_config}")
    trap_server = TrapServer(args, server_config)
    trap_server.run_trap_server()


if __name__ == "__main__":
    initialize_signals_handler()
    main()

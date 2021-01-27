import argparse
import logging.config

import yaml

from splunk_connect_for_snmp_traps.manager.trap_server import TrapServer
from utilities import initialize_signals_handler

logger = logging.getLogger(__name__)


def main():
    logger.info(f'Startup Config')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l',
        '--loglevel',
        default='debug',
        help='Provide logging level. Example --loglevel debug, default=warning',
    )

    parser.add_argument('-c', '--config', default='config.yaml', help='Config File')
    args = parser.parse_args()

    log_level = args.loglevel.upper()
    config_file = args.config

    logging.getLogger().setLevel(log_level)
    logger.info(f'Log Level is {log_level}')
    logger.info(f'Config file is {config_file}')

    logger.info('Completed Argument parsing')

    with open(config_file, 'r') as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    logger.debug(f'Server Config is:  {server_config}')
    trap_server = TrapServer(server_config)
    trap_server.run_trap_server()


if __name__ == '__main__':
    initialize_signals_handler()
    main()

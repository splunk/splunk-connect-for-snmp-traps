import logging
import signal

logger = logging.getLogger(__name__)


def default_signal_handler(signal_number, frame):
    logger.info(f'Received Signal: {signal_number}')
    return


def initialize_signals_handler():
    signals_to_catch = (
        signal.SIGHUP, signal.SIGINT, signal.SIGQUIT, signal.SIGQUIT, signal.SIGILL, signal.SIGTRAP, signal.SIGABRT,
        signal.SIGBUS, signal.SIGFPE, signal.SIGUSR1, signal.SIGSEGV, signal.SIGUSR2, signal.SIGPIPE, signal.SIGALRM,
        signal.SIGTERM)
    for one_signal in signals_to_catch:
        signal.signal(one_signal, default_signal_handler)


class HecConfiguration:
    def __init__(self, hec_config):
        self._protocol = hec_config['protocol']
        self._host = hec_config['host']
        self._port = hec_config['port']
        self._endpoint = hec_config['endpoint']
        self._authentication_token = hec_config['authentication_token']

    def endpoint(self):
        from urllib.parse import urlunsplit
        base_url = f'{self._host}:{self._port}'
        return urlunsplit((self._protocol, base_url, self._endpoint, '', ''))

    def authentication_token(self):
        return self._authentication_token

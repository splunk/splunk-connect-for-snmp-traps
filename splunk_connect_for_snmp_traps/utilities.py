import logging
import signal

logger = logging.getLogger(__name__)


def default_signal_handler(signal_number, frame):
    logger.info(f"Received Signal: {signal_number}")
    return


def initialize_signals_handler():
    signals_to_catch = (
        signal.SIGHUP,
        signal.SIGINT,
        signal.SIGQUIT,
        signal.SIGQUIT,
        signal.SIGILL,
        signal.SIGTRAP,
        signal.SIGABRT,
        signal.SIGBUS,
        signal.SIGFPE,
        signal.SIGUSR1,
        signal.SIGSEGV,
        signal.SIGUSR2,
        signal.SIGPIPE,
        signal.SIGALRM,
        signal.SIGTERM,
    )
    for one_signal in signals_to_catch:
        signal.signal(one_signal, default_signal_handler)

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


# 1.3.6.1.2.1.2.2.1.4.1|Integer|16436|16436|True
# 1.3.6.1.2.1.1.6.0|DisplayString|San Francisco, California, United States|San Francisco, California, United States|True
# 1.3.6.1.2.1.2.2.1.6.2|OctetString|<null>ybù@|0x00127962f940|False
# 1.3.6.1.2.1.1.9.1.2.7|ObjectIdentity|1.3.6.1.2.1.50|SNMPv2-SMI::mib-2.50|False
# 1.3.6.1.2.1.6.13.1.4.195.218.254.105.51684.194.67.10.226.22|IpAddress|ÂCâ|194.67.10.226|False
# 1.3.6.1.2.1.25.3.2.1.6.1025|Counter32|0|0|True
# 1.3.6.1.2.1.31.1.1.1.15.2|Gauge32|100|100|True
# 1.3.6.1.2.1.1.3.0|TimeTicks|148271768|148271768|True
# 1.3.6.1.4.1.2021.10.1.6.1|Opaque|x>ë|0x9f78043eeb851f|False
# 1.3.6.1.2.1.31.1.1.1.10.1|Counter64|453477588|453477588|True
#
# As you can see, for most types str(value) == value.prettyPrint(), however:
# - for Opaque, IpAddress, and OctetString we need to use prettyPrint(), otherwise the data is rubbish
# - any other type should use str() before sending data to MIB-server
def format_value_for_mib_server(value, value_type):
    if value_type in ("OctetString", "IpAddress", "Opaque"):
        return value.prettyPrint()
    else:
        return str(value)

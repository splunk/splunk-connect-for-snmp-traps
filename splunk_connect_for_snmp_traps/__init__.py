import signal
import logging.config
import argparse
import yaml

from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.entity.rfc3413 import ntfrcv

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)


def receiveSignal(signalNumber, frame):
    logger.info("Received Signal:", signalNumber)
    return


def trap_server(port, server_config):
    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher
    snmpEngine = engine.SnmpEngine()

    snmpEngine.observer.registerObserver(
        requestObserver, "rfc3412.receiveMessage:request", "rfc3412.returnResponsePdu"
    )

    # UDP over IPv4
    config.addTransport(
        snmpEngine,
        udp.domainName,
        udp.UdpTransport().openServerMode(("127.0.0.1", port)),
    )

    # UDP over IPv6
    config.addTransport(
        snmpEngine, udp6.domainName, udp6.Udp6Transport().openServerMode(("::1", port))
    )

    # SNMPv1/2c setup

    # SecurityName <-> CommunityName mapping
    for community in server_config["communities"]["v1"]:
        logger.info(f"Configuring V1 {community}")
        config.addV1System(snmpEngine, community, community)

    # Register SNMP Application at the SNMP engine
    ntfrcv.NotificationReceiver(snmpEngine, cbFun)

    snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

    # Run I/O dispatcher which would receive queries and send confirmations
    try:
        snmpEngine.transportDispatcher.runDispatcher()

    finally:
        snmpEngine.observer.unregisterObserver()
        snmpEngine.transportDispatcher.closeDispatcher()


# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    logger.debug(
        'Notification from ContextEngineId "%s", ContextName "%s"'
        % (contextEngineId.prettyPrint(), contextName.prettyPrint())
    )
    for name, val in varBinds:
        logger.debug("%s = %s" % (name.prettyPrint(), val.prettyPrint()))


# Register a callback to be invoked at specified execution point of
# SNMP Engine and passed local variables at code point's local scope
# noinspection PyUnusedLocal,PyUnusedLocal
def requestObserver(snmpEngine, execpoint, variables, cbCtx):
    logger.debug("Execution point: %s" % execpoint)
    logger.debug(
        "* transportDomain: %s"
        % ".".join([str(x) for x in variables["transportDomain"]])
    )
    logger.debug(
        "* transportAddress: %s"
        % "@".join([str(x) for x in variables["transportAddress"]])
    )
    logger.debug("* securityModel: %s" % variables["securityModel"])
    logger.debug("* securityName: %s" % variables["securityName"])
    logger.debug("* securityLevel: %s" % variables["securityLevel"])
    logger.debug("* contextEngineId: %s" % variables["contextEngineId"].prettyPrint())
    logger.debug("* contextName: %s" % variables["contextName"].prettyPrint())
    logger.debug("* PDU: %s" % variables["pdu"].prettyPrint())


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--loglevel",
        default="warning",
        help="Provide logging level. Example --loglevel debug, default=warning",
    )
    parser.add_argument(
        "-p", "--port", default="2062", help="Port used to accept traps", type=int
    )
    parser.add_argument("-c", "--config", default="config.yaml", help="Config File")
    args = parser.parse_args()
    log_level = args.loglevel.upper()
    config_file = args.config
    logging.getLogger().setLevel(log_level)
    logger.debug(f"Log Level is {log_level}")
    logger.debug(f"Config file is {config_file}")

    logger.debug("Completed Argument parsing")

    with open(config_file, "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    logger.debug(f"Server Config is:  {server_config}")
    trap_server(port=args.port, server_config=server_config)


if __name__ == "__main__":
    # register the signals to be caught
    signal.signal(signal.SIGHUP, receiveSignal)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    # signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)

    main()

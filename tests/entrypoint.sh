#!/bin/sh

export PYTHONPATH="${PYTHONPATH}:/splunk-connect-for-snmp-traps"
python3 splunk_connect_for_snmp_traps/snmp_trap_server.py -l DEBUG -i main
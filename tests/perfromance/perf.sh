#!/bin/bash
#
# Copyright 2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# SET TRAP DESTINATION -> SNMP CONNECTOR
SNMP_CONNECTOR_HOST_IP=10.202.2.209
TRAP_PORT=162

# DEFINE STRING WHICH WILL BE SEND IN TRAP
PREFIX=TEST_1
TRAP_NAME=${PREFIX}_abc_

# DEFINE HOW MUCH DATA WE WILL SEND
MULTIPLAYER=10 # this is the number of 'snmptrap' inside for loop
HOW_LONG_TO_RUN__NUMBER_OF_LOOPS=10

# SCRIPT STARTS
count=0
START_TIME=$(date +%s)
for (( ; ; )); do
  # FIRST 10
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}0_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}1_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}2_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}3_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}4_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}5_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}6_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}7_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}8_$count
  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}9_$count
  # ANOTHER 10
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}10_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}11_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}12_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}13_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}14_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}15_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}16_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}17_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}18_$count
  #  snmptrap -v 2c -c public $SNMP_CONNECTOR_HOST_IP:$TRAP_PORT 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s ${TRAP_NAME}19_$count
  ((count++))
  echo "Count: $count"
  if ((count > HOW_LONG_TO_RUN__NUMBER_OF_LOOPS)); then
    break #Abandon the loop.
  fi
done
END_TIME=$(date +%s)
echo $count

echo "RESULTS"
test_time=$((END_TIME - START_TIME))
traps=$((count * MULTIPLAYER))
per_sec=$((traps / test_time))
echo "Test duration $test_time, number of traps $traps"
echo "Traps/sec: $per_sec" && bc <<<"scale=2; $traps/$test_time"
echo "DONE"

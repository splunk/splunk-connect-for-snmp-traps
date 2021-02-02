# Splunk Connect for SNMP Traps

This project connects SNMP Trap sending source to Splunk Enterprise and Splunk Enterprise Cloud

## Third Party

We use SNMP library for Python under the BSD 2 Clause License https://github.com/etingof/pysnmp

## Development Steps (For Internal Tests)

### Install Poetry
pip3 install poetry

### Install deps

poetry install

### Setup Splunk HEC Environment
```
export SPLUNK_HEC_URL=http://0.0.0.0:8088/services/collector/event
export SPLUNK_HEC_TOKEN=<token>
export SPLUNK_HEC_TLS_VERIFY=False
```

### Run Trap Server
poetry run sc4snmp-traps -l debug


### Send Sample Traps

```
sudo snmptrap -v 2c -c public 0.0.0.0:2162 '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 i 123
```


#### Sample Output in Splunk

```js
oid1 = 1.3.6.1.2.1.1.3.0
oid_type1 = ObjectName
value1 = 65521705
val_type1 = TimeTicks
mib1 = SNMPv2-MIB::sysUpTime.0 = 65521705
custom_mib1 = 正常运行时间 = 65521705

oid2 = 1.3.6.1.6.3.1.1.4.1.0
oid_type2 = ObjectName
value2 = 1.3.6.1.4.1.8072.2.3.0.1
val_type2 = ObjectIdentifier
mib2 = SNMPv2-MIB::snmpTrapOID.0 = NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatNotification
custom_mib2 =  trap 陷阱 =  NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatNotification

oid3 = 1.3.6.1.4.1.8072.2.3.2.1
oid_type3 = ObjectName
value3 = 123
val_type3 = Integer
mib3 = NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatRate = 123
custom_mib3 =  NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatRate = 123
```



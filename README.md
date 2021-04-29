# Splunk Connect for SNMP Traps

This project connects SNMP Trap sending source to Splunk Enterprise and Splunk Enterprise Cloud

## Third Party

We use SNMP library for Python under the BSD 2 Clause License https://github.com/etingof/pysnmp

## Development Instructions for Traps

> This is used as a reference steps while working on development aspects of SNMP Traps component of Splunk Connect for SNMP!

### Get Started
```
git clone git@github.com:splunk/splunk-connect-for-snmp-traps.git
cd "splunk-connect-for-snmp-trapsr"
```

### Install Poetry
`pip3 install poetry`


### Setup Splunk HEC Environment
```
export SPLUNK_HEC_URL=http://0.0.0.0:8088/services/collector/event
export SPLUNK_HEC_TOKEN=<token>
export SPLUNK_HEC_TLS_VERIFY=False
export MIBS_SERVER_URL=<mib-server-url>
```

**Note**: Please refer to here to set up the MIB SERVER: https://github.com/splunk/splunk-connect-for-snmp-mib-server

### Run Trap Server

```
poetry install
poetry run sc4snmp-traps
```

### Send Sample Traps

```
sudo snmptrap -v 2c -c public 0.0.0.0:2162 '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 i 123
```


#### Sample Output in Splunk

```js
oid-type1="ObjectName" value1-type="TimeTicks" 1.3.6.1.2.1.1.3.0="123" value1="123" SNMPv2-MIB::sysUpTime.0="123" 正常运行时间="123"
oid-type2="ObjectName" value2-type="ObjectIdentifier" 1.3.6.1.6.3.1.1.4.1.0="1.3.6.1.6.3.1.1.5.1" value2="1.3.6.1.6.3.1.1.5.1" SNMPv2-MIB::snmpTrapOID.0="SNMPv2-MIB::coldStart" 陷阱="None"
oid-type3="ObjectName" value3-type="OctetString" 1.3.6.1.2.1.1.5.0="testk8s" value3="testk8s" SNMPv2-MIB::sysName.0="testk8s" 
```

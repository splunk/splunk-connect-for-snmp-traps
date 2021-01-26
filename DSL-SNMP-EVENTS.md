# SNMP : Domain Specific Language and Translations

# Original PDU

```
 variable-bindings=VarBindList:
  VarBind:
   name=1.3.6.1.2.1.1.3.0
   =_BindValue:
    value=ObjectSyntax:
     application-wide=ApplicationSyntax:
      timeticks-value=184027995
  VarBind:
   name=1.3.6.1.6.3.1.1.4.1.0
   =_BindValue:
    value=ObjectSyntax:
     simple=SimpleSyntax:
      objectID-value=1.3.6.1.6.3.1.1.5.2
```

# Translated data structure

```py
custom structure spec:
{
    "mib": Translated oid = Translated value,
    "oid": Original oid,
    "oid_type": Type of oid,
    "val_type": Type of value,
    "value": Original value
}
```

```json
{
    "mib": "SNMPv2-MIB::sysUpTime.0 = 184027995",
    "oid": "1.3.6.1.2.1.1.3.0",
    "oid_type": "ObjectName",
    "val_type": "TimeTicks",
    "value": "184027995"
}
```

```json
{
    "mib": "SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-MIB::warmStart",
    "oid": "1.3.6.1.6.3.1.1.4.1.0",
    "oid_type": "ObjectName",
    "val_type": "ObjectIdentifier",
    "value": "1.3.6.1.6.3.1.1.5.2"
}
```




# Simplified MIB

```
SNMPv2 - MIB::snmpTrapOID.0 = SNMPv2 - MIB::warmStart
```

> Shall we replace above MIB value to:


```json
{
    "mib_name": "snmpTrapOID.0",
    "mib_value": "warmStart"
}
```

OR


```json
{
    "mib_name": "snmpTrapOID",
    "mib_value": "warmStart"
}
```
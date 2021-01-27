# SNMP : Domain Specific Language and Translations
# Trap sent by
```shell
sudo snmptrap -v 2c -c public 127.0.0.1:1024 "" 1.3.6.1.4.1.6141.2.60.37.0.2 1.3.6.1.4.1.6141.2.60.37.1.1.11.1.1.1 t 14096763
```

# Original PDU

```
 variable-bindings=VarBindList:
  VarBind:
   name=1.3.6.1.2.1.1.3.0
   =_BindValue:
    value=ObjectSyntax:
     application-wide=ApplicationSyntax:
      timeticks-value=192430459



  VarBind:
   name=1.3.6.1.6.3.1.1.4.1.0
   =_BindValue:
    value=ObjectSyntax:
     simple=SimpleSyntax:
      objectID-value=1.3.6.1.4.1.6141.2.60.37.0.2



  VarBind:
   name=1.3.6.1.4.1.6141.2.60.37.1.1.11.1.1.1
   =_BindValue:
    value=ObjectSyntax:
     application-wide=ApplicationSyntax:
      timeticks-value=14096763
```

# Translated trap string
custom trap string spec:
```
oidi = Original oid for ith item
oid_typei = Type of oid for ith item
valuei = Original value for ith item
val_typei = Type of value for ith item
mibi = SNMPv2-MIB::sysUpTime.0 = Translated oid = Translated value for ith item
custom_mibi = Custom translated oid = Custom translated value for ith item
```
Note: 
1. If **value** is not a `oid`, we keep the original value in the value part for both **mib** field and **custom_mib** field.
2. If there is no custom translation for a specific `oid`, we just put `None` here.

```
        oid1 = 1.3.6.1.2.1.1.3.0
        oid_type1 = ObjectName
        value1 = 192430459
        val_type1 = TimeTicks
        mib1 = SNMPv2-MIB::sysUpTime.0 = 192430459
        custom_mib1 = 正常运行时间 = 192430459
        
        oid2 = 1.3.6.1.6.3.1.1.4.1.0
        oid_type2 = ObjectName
        value2 = 1.3.6.1.4.1.6141.2.60.37.0.2
        val_type2 = ObjectIdentifier
        mib2 = SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::enterprises.6141.2.60.37.0.2
        custom_mib2 = lalala = 1.3.6.1.4.1.6141.2.60.37.0.2
        
        oid3 = 1.3.6.1.4.1.6141.2.60.37.1.1.11.1.1.1
        oid_type3 = ObjectName
        value3 = 14096763
        val_type3 = TimeTicks
        mib3 = SNMPv2-SMI::enterprises.6141.2.60.37.1.1.11.1.1.1 = 14096763
        custom_mib3 = None = 14096763
```
# Sendng-out payload

```json
{
    "event": "\n        oid1 = 1.3.6.1.2.1.1.3.0\n        oid_type1 = ObjectName\n        value1 = 192430459\n        val_type1 = TimeTicks\n        mib1 = SNMPv2-MIB::sysUpTime.0 = 192430459\n        custom_mib1 = \u6b63\u5e38\u8fd0\u884c\u65f6\u95f4 = 192430459\n        \n        oid2 = 1.3.6.1.6.3.1.1.4.1.0\n        oid_type2 = ObjectName\n        value2 = 1.3.6.1.4.1.6141.2.60.37.0.2\n        val_type2 = ObjectIdentifier\n        mib2 = SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::enterprises.6141.2.60.37.0.2\n        custom_mib2 = lalala = 1.3.6.1.4.1.6141.2.60.37.0.2\n        \n        oid3 = 1.3.6.1.4.1.6141.2.60.37.1.1.11.1.1.1\n        oid_type3 = ObjectName\n        value3 = 14096763\n        val_type3 = TimeTicks\n        mib3 = SNMPv2-SMI::enterprises.6141.2.60.37.1.1.11.1.1.1 = 14096763\n        custom_mib3 = None = 14096763\n        "
}
```




# Simplified MIB

```
SNMPv2 - MIB::snmpTrapOID.0 = SNMPv2 - MIB::warmStart
```
# Discussions
- Shall we translate both oid and its value? Or just the oid/value?
- Shall we add custom translation regardless wether we find its translation in the custom translation table?
- Share we replace below MIB values to

```
mib1 = SNMPv2-MIB::sysUpTime.0 = 192430459
custom_mib1 = 正常运行时间 = 192430459
```
```
mib_name = SNMPv2-MIB::sysUpTime.0 
mib_value = 192430459
custom_mib_name = 正常运行时间 
custom_mib_value = 192430459
```
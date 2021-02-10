#
# PySNMP MIB module TIARA-NETWORKS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, Integer32, Bits, NotificationType, MibIdentifier, iso, Counter64, ObjectIdentity, TimeTicks, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "Bits", "NotificationType", "MibIdentifier", "iso", "Counter64", "ObjectIdentity", "TimeTicks", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraSnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 5))
tiaraSnmpMib.setRevisions(('1999-04-23 00:00',))
if mibBuilder.loadTexts: tiaraSnmpMib.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: tiaraSnmpMib.setOrganization('Tiara Networks, Inc.')
snmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1))
snmpAgentType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmpV1", 2), ("snmpV2V1", 3), ("snmpV2cV1", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpAgentType.setStatus('current')
snmpRmonSupported = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("not-supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpRmonSupported.setStatus('current')
snmpTrapRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4), )
if mibBuilder.loadTexts: snmpTrapRcvrTable.setStatus('current')
snmpTrapRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1), ).setIndexNames((0, "TIARA-NETWORKS-SNMP-MIB", "snmpTrapRcvrAddress"))
if mibBuilder.loadTexts: snmpTrapRcvrEntry.setStatus('current')
snmpTrapRcvrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapRcvrEntryStatus.setStatus('current')
snmpTrapRcvrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapRcvrAddress.setStatus('current')
snmpTrapRcvrCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapRcvrCommunity.setStatus('current')
mibBuilder.exportSymbols("TIARA-NETWORKS-SNMP-MIB", snmpTrapRcvrEntry=snmpTrapRcvrEntry, PYSNMP_MODULE_ID=tiaraSnmpMib, snmpTrapRcvrAddress=snmpTrapRcvrAddress, snmpTrapRcvrCommunity=snmpTrapRcvrCommunity, snmpTrapRcvrTable=snmpTrapRcvrTable, tiaraSnmpMib=tiaraSnmpMib, snmpAgentType=snmpAgentType, snmpTrapRcvrEntryStatus=snmpTrapRcvrEntryStatus, snmpObjects=snmpObjects, snmpRmonSupported=snmpRmonSupported)

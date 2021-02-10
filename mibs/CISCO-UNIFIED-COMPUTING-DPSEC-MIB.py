#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-DPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-DPSEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, Unsigned64, CiscoInetAddressMask, CiscoNetworkAddress, TimeIntervalSec = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "Unsigned64", "CiscoInetAddressMask", "CiscoNetworkAddress", "TimeIntervalSec")
CucsManagedObjectId, CucsManagedObjectDn, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectId", "CucsManagedObjectDn", "ciscoUnifiedComputingMIBObjects")
CucsPolicyPolicyOwner, CucsDpsecForgedTransmit = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsPolicyPolicyOwner", "CucsDpsecForgedTransmit")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, ModuleIdentity, Gauge32, Bits, NotificationType, Counter32, ObjectIdentity, Unsigned32, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32", "Bits", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowPointer, TruthValue, DisplayString, TimeStamp, TimeInterval, MacAddress, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "DisplayString", "TimeStamp", "TimeInterval", "MacAddress", "TextualConvention", "DateAndTime")
cucsDpsecObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13))
if mibBuilder.loadTexts: cucsDpsecObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsDpsecObjects.setOrganization('Cisco Systems Inc.')
cucsDpsecMacTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1), )
if mibBuilder.loadTexts: cucsDpsecMacTable.setStatus('current')
cucsDpsecMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DPSEC-MIB", "cucsDpsecMacInstanceId"))
if mibBuilder.loadTexts: cucsDpsecMacEntry.setStatus('current')
cucsDpsecMacInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDpsecMacInstanceId.setStatus('current')
cucsDpsecMacDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacDn.setStatus('current')
cucsDpsecMacRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacRn.setStatus('current')
cucsDpsecMacDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacDescr.setStatus('current')
cucsDpsecMacForge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 5), CucsDpsecForgedTransmit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacForge.setStatus('current')
cucsDpsecMacIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacIntId.setStatus('current')
cucsDpsecMacName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacName.setStatus('current')
cucsDpsecMacPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPolicyLevel.setStatus('current')
cucsDpsecMacPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 9), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPolicyOwner.setStatus('current')
cucsDpsecMacPropAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 10), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPropAcl.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-DPSEC-MIB", cucsDpsecMacTable=cucsDpsecMacTable, cucsDpsecMacIntId=cucsDpsecMacIntId, cucsDpsecMacName=cucsDpsecMacName, cucsDpsecMacDescr=cucsDpsecMacDescr, cucsDpsecObjects=cucsDpsecObjects, cucsDpsecMacInstanceId=cucsDpsecMacInstanceId, cucsDpsecMacRn=cucsDpsecMacRn, cucsDpsecMacPropAcl=cucsDpsecMacPropAcl, cucsDpsecMacForge=cucsDpsecMacForge, cucsDpsecMacPolicyOwner=cucsDpsecMacPolicyOwner, cucsDpsecMacEntry=cucsDpsecMacEntry, PYSNMP_MODULE_ID=cucsDpsecObjects, cucsDpsecMacPolicyLevel=cucsDpsecMacPolicyLevel, cucsDpsecMacDn=cucsDpsecMacDn)

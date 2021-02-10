#
# PySNMP MIB module ZYXEL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, Bits, Integer32, Unsigned32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Bits", "Integer32", "Unsigned32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61))
if mibBuilder.loadTexts: zyxelPort.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPort.setOrganization('Enterprise Solution ZyXEL')
zyxelPortSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1))
zyxelPortStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2))
zyxelPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3))
zyxelPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1), )
if mibBuilder.loadTexts: zyxelPortTable.setStatus('current')
zyxelPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortEntry.setStatus('current')
zyPortSpeedDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("auto", 0), ("speed10Half", 1), ("speed10Full", 2), ("speed100Half", 3), ("speed100Full", 4), ("speed1000Full", 5), ("speed10000Full", 6), ("speed12000Full", 7), ("speed40000Full", 8), ("speed1000Auto", 9), ("speedAuto1000", 10), ("speedAuto10000", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSpeedDuplex.setStatus('current')
zyPortFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortFlowControlState.setStatus('current')
zyPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortName.setStatus('current')
zyPortIntrusionLockState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortIntrusionLockState.setStatus('current')
zyPortCX4CableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("halfMeters", 0), ("oneMeters", 1), ("threeMeters", 2), ("fiveMeters", 3), ("tenMeters", 4), ("fifteenMeters", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortCX4CableLength.setStatus('current')
zyPort10GMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("sfpPlus", 0), ("dac10g", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPort10GMediaType.setStatus('current')
zyxelPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1), )
if mibBuilder.loadTexts: zyxelPortInfoTable.setStatus('current')
zyxelPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortInfoEntry.setStatus('current')
zyPortModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("fastEthernet", 0), ("gigabitEthernet", 1), ("xgEthernet10000", 2), ("x1Ethernet40000", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPortModuleType.setStatus('current')
zyPortLinkUpType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 0), ("copper", 1), ("fiber", 2), ("xfp", 3), ("cx4", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPortLinkUpType.setStatus('current')
zyPortTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("underTesting", 1), ("success", 2), ("fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPortTestStatus.setStatus('current')
zyPortCounterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortCounterReset.setStatus('current')
zyPortAutonegotiationFailed = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPortAutonegotiationFailed.setStatus('current')
zyPortIntrusionLock = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPortIntrusionLock.setStatus('current')
zyPortAutonegotiationFailedRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPortAutonegotiationFailedRecovered.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-MIB", zyxelPortTable=zyxelPortTable, zyxelPortSetup=zyxelPortSetup, zyxelPort=zyxelPort, zyxelPortInfoTable=zyxelPortInfoTable, zyPort10GMediaType=zyPort10GMediaType, zyxelPortInfoEntry=zyxelPortInfoEntry, zyxelPortEntry=zyxelPortEntry, zyPortCounterReset=zyPortCounterReset, zyPortFlowControlState=zyPortFlowControlState, zyPortAutonegotiationFailedRecovered=zyPortAutonegotiationFailedRecovered, zyPortAutonegotiationFailed=zyPortAutonegotiationFailed, zyxelPortStatus=zyxelPortStatus, zyPortLinkUpType=zyPortLinkUpType, zyPortCX4CableLength=zyPortCX4CableLength, zyPortTestStatus=zyPortTestStatus, PYSNMP_MODULE_ID=zyxelPort, zyPortSpeedDuplex=zyPortSpeedDuplex, zyxelPortNotifications=zyxelPortNotifications, zyPortIntrusionLock=zyPortIntrusionLock, zyPortName=zyPortName, zyPortIntrusionLockState=zyPortIntrusionLockState, zyPortModuleType=zyPortModuleType)

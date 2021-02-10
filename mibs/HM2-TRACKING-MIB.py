#
# PySNMP MIB module HM2-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-TRACKING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
HmEnabledStatus, hm2ConfigurationMibs, HmTimeSeconds1970 = mibBuilder.importSymbols("HM2-TC-MIB", "HmEnabledStatus", "hm2ConfigurationMibs", "HmTimeSeconds1970")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
inetCidrRouteEntry, = mibBuilder.importSymbols("IP-FORWARD-MIB", "inetCidrRouteEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Bits, TimeTicks, NotificationType, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Bits", "TimeTicks", "NotificationType", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "Gauge32", "Counter32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hm2TrackingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 115))
hm2TrackingMib.setRevisions(('2013-09-03 12:00',))
if mibBuilder.loadTexts: hm2TrackingMib.setLastUpdated('201309031200Z')
if mibBuilder.loadTexts: hm2TrackingMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2TrackingMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 0))
hm2TrackingMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1))
hm2TrackStatusChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 115, 0, 1)).setObjects(("HM2-TRACKING-MIB", "hm2TrackType"), ("HM2-TRACKING-MIB", "hm2TrackId"), ("HM2-TRACKING-MIB", "hm2TrackStatus"), ("HM2-TRACKING-MIB", "hm2TrackOperState"))
if mibBuilder.loadTexts: hm2TrackStatusChangeEvent.setStatus('current')
hm2TrackingConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1))
hm2TrackingInterfaceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2))
hm2TrackingPingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3))
hm2TrackingLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4))
hm2TrackingApplicationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5))
hm2TrackingStaticRouteGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6))
hm2TrackingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1), )
if mibBuilder.loadTexts: hm2TrackingConfigTable.setStatus('current')
hm2TrackingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1), ).setIndexNames((0, "HM2-TRACKING-MIB", "hm2TrackType"), (0, "HM2-TRACKING-MIB", "hm2TrackId"))
if mibBuilder.loadTexts: hm2TrackingConfigEntry.setStatus('current')
hm2TrackType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("interface", 1), ("ping", 2), ("logical", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2TrackType.setStatus('current')
hm2TrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2TrackId.setStatus('current')
hm2TrackName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackName.setStatus('current')
hm2TrackDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2TrackDescription.setStatus('current')
hm2TrackOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notReady", 3))).clone('notReady')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackOperState.setStatus('current')
hm2TrackNumberOfChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackNumberOfChanges.setStatus('current')
hm2TrackTimeLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 7), HmTimeSeconds1970()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackTimeLastChange.setStatus('current')
hm2TrackSendStateChangeTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 8), HmEnabledStatus().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2TrackSendStateChangeTrap.setStatus('current')
hm2TrackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2TrackStatus.setStatus('current')
hm2TrackingInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1), )
if mibBuilder.loadTexts: hm2TrackingInterfaceTable.setStatus('current')
hm2TrackingInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1), ).setIndexNames((0, "HM2-TRACKING-MIB", "hm2TrackInterfaceId"))
if mibBuilder.loadTexts: hm2TrackingInterfaceEntry.setStatus('current')
hm2TrackInterfaceId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2TrackInterfaceId.setStatus('current')
hm2TrackIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackIfNumber.setStatus('current')
hm2TrackIfLinkUpDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackIfLinkUpDelay.setStatus('current')
hm2TrackIfLinkDownDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackIfLinkDownDelay.setStatus('current')
hm2TrackingPingTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1), )
if mibBuilder.loadTexts: hm2TrackingPingTable.setStatus('current')
hm2TrackingPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1), ).setIndexNames((0, "HM2-TRACKING-MIB", "hm2TrackPingId"))
if mibBuilder.loadTexts: hm2TrackingPingEntry.setStatus('current')
hm2TrackPingId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2TrackPingId.setStatus('current')
hm2TrackPingIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingIfNumber.setStatus('current')
hm2TrackPingInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingInetAddrType.setStatus('current')
hm2TrackPingInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingInetAddr.setStatus('current')
hm2TrackPingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 20000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingInterval.setStatus('current')
hm2TrackPingMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingMiss.setStatus('current')
hm2TrackPingSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingSuccess.setStatus('current')
hm2TrackPingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingTimeout.setStatus('current')
hm2TrackPingTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackPingTTL.setStatus('current')
hm2TrackPingBestRouteIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackPingBestRouteIfNumber.setStatus('current')
hm2TrackLogicalInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1), )
if mibBuilder.loadTexts: hm2TrackLogicalInstanceTable.setStatus('current')
hm2TrackLogicalInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1), ).setIndexNames((0, "HM2-TRACKING-MIB", "hm2TrackLogicalId"))
if mibBuilder.loadTexts: hm2TrackLogicalInstanceEntry.setStatus('current')
hm2TrackLogicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2TrackLogicalId.setStatus('current')
hm2TrackLogicalOperandNameA = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackLogicalOperandNameA.setStatus('current')
hm2TrackLogicalOperandNameB = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackLogicalOperandNameB.setStatus('current')
hm2TrackLogicalOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("and", 1), ("or", 2))).clone('or')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2TrackLogicalOperator.setStatus('current')
hm2TrackingApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1), )
if mibBuilder.loadTexts: hm2TrackingApplicationTable.setStatus('current')
hm2TrackingApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1), ).setIndexNames((0, "HM2-TRACKING-MIB", "hm2TrackAppId"), (0, "HM2-TRACKING-MIB", "hm2TrackType"), (0, "HM2-TRACKING-MIB", "hm2TrackId"))
if mibBuilder.loadTexts: hm2TrackingApplicationEntry.setStatus('current')
hm2TrackAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2TrackAppId.setStatus('current')
hm2TrackAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackAppName.setStatus('current')
hm2TrackAppObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackAppObjectName.setStatus('current')
hm2TrackStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1), )
if mibBuilder.loadTexts: hm2TrackStaticRouteTable.setStatus('current')
hm2TrackStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1), )
inetCidrRouteEntry.registerAugmentions(("HM2-TRACKING-MIB", "hm2TrackStaticRouteEntry"))
hm2TrackStaticRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
if mibBuilder.loadTexts: hm2TrackStaticRouteEntry.setStatus('current')
hm2TrackStaticRouteTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2TrackStaticRouteTrackId.setStatus('current')
hm2TrackStaticRouteTrackState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notReady", 3))).clone('notReady')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2TrackStaticRouteTrackState.setStatus('current')
mibBuilder.exportSymbols("HM2-TRACKING-MIB", hm2TrackingApplicationTable=hm2TrackingApplicationTable, hm2TrackAppId=hm2TrackAppId, hm2TrackPingBestRouteIfNumber=hm2TrackPingBestRouteIfNumber, hm2TrackStaticRouteTrackId=hm2TrackStaticRouteTrackId, hm2TrackLogicalOperandNameB=hm2TrackLogicalOperandNameB, hm2TrackStaticRouteTable=hm2TrackStaticRouteTable, hm2TrackTimeLastChange=hm2TrackTimeLastChange, hm2TrackPingInetAddrType=hm2TrackPingInetAddrType, hm2TrackLogicalOperandNameA=hm2TrackLogicalOperandNameA, hm2TrackLogicalInstanceEntry=hm2TrackLogicalInstanceEntry, hm2TrackAppName=hm2TrackAppName, hm2TrackAppObjectName=hm2TrackAppObjectName, hm2TrackingStaticRouteGroup=hm2TrackingStaticRouteGroup, hm2TrackDescription=hm2TrackDescription, hm2TrackPingTimeout=hm2TrackPingTimeout, hm2TrackLogicalId=hm2TrackLogicalId, hm2TrackingConfigGroup=hm2TrackingConfigGroup, hm2TrackingLogicalGroup=hm2TrackingLogicalGroup, hm2TrackingInterfaceTable=hm2TrackingInterfaceTable, hm2TrackStatusChangeEvent=hm2TrackStatusChangeEvent, hm2TrackingApplicationEntry=hm2TrackingApplicationEntry, hm2TrackNumberOfChanges=hm2TrackNumberOfChanges, hm2TrackIfLinkDownDelay=hm2TrackIfLinkDownDelay, hm2TrackId=hm2TrackId, hm2TrackPingMiss=hm2TrackPingMiss, hm2TrackSendStateChangeTrap=hm2TrackSendStateChangeTrap, hm2TrackIfLinkUpDelay=hm2TrackIfLinkUpDelay, hm2TrackingPingGroup=hm2TrackingPingGroup, hm2TrackPingIfNumber=hm2TrackPingIfNumber, hm2TrackPingInetAddr=hm2TrackPingInetAddr, hm2TrackType=hm2TrackType, hm2TrackIfNumber=hm2TrackIfNumber, hm2TrackOperState=hm2TrackOperState, hm2TrackStatus=hm2TrackStatus, PYSNMP_MODULE_ID=hm2TrackingMib, hm2TrackPingTTL=hm2TrackPingTTL, hm2TrackingPingEntry=hm2TrackingPingEntry, hm2TrackingConfigTable=hm2TrackingConfigTable, hm2TrackStaticRouteTrackState=hm2TrackStaticRouteTrackState, hm2TrackingInterfaceGroup=hm2TrackingInterfaceGroup, hm2TrackingApplicationGroup=hm2TrackingApplicationGroup, hm2TrackInterfaceId=hm2TrackInterfaceId, hm2TrackingMibNotifications=hm2TrackingMibNotifications, hm2TrackingPingTable=hm2TrackingPingTable, hm2TrackPingInterval=hm2TrackPingInterval, hm2TrackLogicalOperator=hm2TrackLogicalOperator, hm2TrackName=hm2TrackName, hm2TrackPingId=hm2TrackPingId, hm2TrackingMib=hm2TrackingMib, hm2TrackingConfigEntry=hm2TrackingConfigEntry, hm2TrackingInterfaceEntry=hm2TrackingInterfaceEntry, hm2TrackLogicalInstanceTable=hm2TrackLogicalInstanceTable, hm2TrackStaticRouteEntry=hm2TrackStaticRouteEntry, hm2TrackPingSuccess=hm2TrackPingSuccess, hm2TrackingMibObjects=hm2TrackingMibObjects)
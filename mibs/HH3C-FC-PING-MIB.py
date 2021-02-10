#
# PySNMP MIB module HH3C-FC-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FC-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
Hh3cFcVsanIndex, Hh3cFcStartOper, Hh3cFcAddress, Hh3cFcAddressType = mibBuilder.importSymbols("HH3C-FC-TC-MIB", "Hh3cFcVsanIndex", "Hh3cFcStartOper", "Hh3cFcAddress", "Hh3cFcAddressType")
hh3cSan, = mibBuilder.importSymbols("HH3C-VSAN-MIB", "hh3cSan")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Unsigned32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, IpAddress, Bits, TimeTicks, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "IpAddress", "Bits", "TimeTicks", "Integer32", "iso", "Counter64")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
hh3cFcPing = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5))
hh3cFcPing.setRevisions(('2013-03-15 00:00',))
if mibBuilder.loadTexts: hh3cFcPing.setLastUpdated('201303150000Z')
if mibBuilder.loadTexts: hh3cFcPing.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cFcPingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1))
hh3cFcPingConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1))
hh3cFcPingStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2))
hh3cFcPingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3))
hh3cFcPingNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3, 0))
hh3cFcPingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cFcPingTable.setStatus('current')
hh3cFcPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-FC-PING-MIB", "hh3cFcPingIndex"))
if mibBuilder.loadTexts: hh3cFcPingEntry.setStatus('current')
hh3cFcPingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cFcPingIndex.setStatus('current')
hh3cFcPingVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 2), Hh3cFcVsanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingVsan.setStatus('current')
hh3cFcPingAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 3), Hh3cFcAddressType().clone('fcid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingAddressType.setStatus('current')
hh3cFcPingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 4), Hh3cFcAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingAddress.setStatus('current')
hh3cFcPingPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingPacketCount.setStatus('current')
hh3cFcPingPayloadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingPayloadSize.setStatus('current')
hh3cFcPingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingTimeout.setStatus('current')
hh3cFcPingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingDelay.setStatus('current')
hh3cFcPingAgeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(500, 900)).clone(500)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingAgeInterval.setStatus('current')
hh3cFcPingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 10), Hh3cFcStartOper().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingAdminStatus.setStatus('current')
hh3cFcPingOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("complete", 2), ("disabled", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingOperStatus.setStatus('current')
hh3cFcPingTrapOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingTrapOnCompletion.setStatus('current')
hh3cFcPingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPingRowStatus.setStatus('current')
hh3cFcPingStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cFcPingStatTable.setStatus('current')
hh3cFcPingStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-FC-PING-MIB", "hh3cFcPingIndex"))
if mibBuilder.loadTexts: hh3cFcPingStatEntry.setStatus('current')
hh3cFcPingReqPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingReqPackets.setStatus('current')
hh3cFcPingResPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingResPackets.setStatus('current')
hh3cFcPingMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 3), Integer32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingMinTime.setStatus('current')
hh3cFcPingAverageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 4), Integer32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingAverageTime.setStatus('current')
hh3cFcPingMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 5), Integer32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingMaxTime.setStatus('current')
hh3cFcPingTimeoutNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPingTimeoutNum.setStatus('current')
hh3cFcPingCompletionNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 127, 5, 1, 3, 0, 1)).setObjects(("HH3C-FC-PING-MIB", "hh3cFcPingIndex"), ("HH3C-FC-PING-MIB", "hh3cFcPingVsan"), ("HH3C-FC-PING-MIB", "hh3cFcPingAddressType"), ("HH3C-FC-PING-MIB", "hh3cFcPingAddress"), ("HH3C-FC-PING-MIB", "hh3cFcPingReqPackets"), ("HH3C-FC-PING-MIB", "hh3cFcPingResPackets"))
if mibBuilder.loadTexts: hh3cFcPingCompletionNotify.setStatus('current')
mibBuilder.exportSymbols("HH3C-FC-PING-MIB", hh3cFcPingMinTime=hh3cFcPingMinTime, hh3cFcPingPacketCount=hh3cFcPingPacketCount, hh3cFcPingTrapOnCompletion=hh3cFcPingTrapOnCompletion, hh3cFcPingVsan=hh3cFcPingVsan, hh3cFcPingRowStatus=hh3cFcPingRowStatus, hh3cFcPingStatEntry=hh3cFcPingStatEntry, hh3cFcPingEntry=hh3cFcPingEntry, hh3cFcPingStatTable=hh3cFcPingStatTable, hh3cFcPingIndex=hh3cFcPingIndex, hh3cFcPingTimeout=hh3cFcPingTimeout, hh3cFcPingPayloadSize=hh3cFcPingPayloadSize, hh3cFcPingAgeInterval=hh3cFcPingAgeInterval, hh3cFcPingMaxTime=hh3cFcPingMaxTime, hh3cFcPingCompletionNotify=hh3cFcPingCompletionNotify, hh3cFcPingOperStatus=hh3cFcPingOperStatus, hh3cFcPingAddressType=hh3cFcPingAddressType, hh3cFcPingNotifications=hh3cFcPingNotifications, hh3cFcPingAverageTime=hh3cFcPingAverageTime, hh3cFcPingStatistics=hh3cFcPingStatistics, hh3cFcPingReqPackets=hh3cFcPingReqPackets, PYSNMP_MODULE_ID=hh3cFcPing, hh3cFcPingTimeoutNum=hh3cFcPingTimeoutNum, hh3cFcPingNotifyPrefix=hh3cFcPingNotifyPrefix, hh3cFcPingTable=hh3cFcPingTable, hh3cFcPingResPackets=hh3cFcPingResPackets, hh3cFcPingObjects=hh3cFcPingObjects, hh3cFcPingAdminStatus=hh3cFcPingAdminStatus, hh3cFcPing=hh3cFcPing, hh3cFcPingDelay=hh3cFcPingDelay, hh3cFcPingConfigurations=hh3cFcPingConfigurations, hh3cFcPingAddress=hh3cFcPingAddress)

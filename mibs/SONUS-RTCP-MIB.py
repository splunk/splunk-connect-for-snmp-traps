#
# PySNMP MIB module SONUS-RTCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-RTCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, IpAddress, TimeTicks, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Counter64, ObjectIdentity, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "IpAddress", "TimeTicks", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Counter64", "ObjectIdentity", "Integer32", "MibIdentifier", "Unsigned32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
sonusEventDescription, sonusSlotIndex, sonusShelfIndex, sonusEventLevel, sonusEventClass = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusEventDescription", "sonusSlotIndex", "sonusShelfIndex", "sonusEventLevel", "sonusEventClass")
sonusResourcesMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusResourcesMIBs")
SonusBoolean, SonusShelfIndex = mibBuilder.importSymbols("SONUS-TC", "SonusBoolean", "SonusShelfIndex")
sonusRtcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7))
if mibBuilder.loadTexts: sonusRtcpMIB.setLastUpdated('200104180000Z')
if mibBuilder.loadTexts: sonusRtcpMIB.setOrganization('Sonus Networks, Inc.')
sonusRtcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1))
sonusRtcpShelfAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1), )
if mibBuilder.loadTexts: sonusRtcpShelfAdmnTable.setStatus('current')
sonusRtcpShelfAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1), ).setIndexNames((0, "SONUS-RTCP-MIB", "sonusRtcpShelfAdmnIndex"))
if mibBuilder.loadTexts: sonusRtcpShelfAdmnEntry.setStatus('current')
sonusRtcpShelfAdmnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnIndex.setStatus('current')
sonusRtcpShelfAdmnSrInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 40)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnSrInterval.setStatus('current')
sonusRtcpShelfAdmnEstablishInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnEstablishInterval.setStatus('current')
sonusRtcpShelfAdmnLossTrapHistoryEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnLossTrapHistoryEntries.setStatus('current')
sonusRtcpShelfAdmnAbsenceTrapHistoryEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnAbsenceTrapHistoryEntries.setStatus('current')
sonusRtcpShelfAdmnLossTrapHistoryTableReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("reset", 2))).clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnLossTrapHistoryTableReset.setStatus('current')
sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("reset", 2))).clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset.setStatus('current')
sonusRtcpSlotLinkLossTrapStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4), )
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatusTable.setStatus('current')
sonusRtcpSlotLinkLossTrapStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1), ).setIndexNames((0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatShelfIndex"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatSlotIndex"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatSrcIpAddress"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatDestIpAddress"))
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatusEntry.setStatus('current')
sonusRtcpSlotLinkLossTrapStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatShelfIndex.setStatus('current')
sonusRtcpSlotLinkLossTrapStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatSlotIndex.setStatus('current')
sonusRtcpSlotLinkLossTrapStatSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatSrcIpAddress.setStatus('current')
sonusRtcpSlotLinkLossTrapStatDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatDestIpAddress.setStatus('current')
sonusRtcpSlotLinkLossTrapStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatCount.setStatus('current')
sonusRtcpSlotLinkLossTrapStatTotalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatTotalCount.setStatus('current')
sonusRtcpSlotLinkLossTrapStatStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatStartTime.setStatus('current')
sonusRtcpSlotLinkLossTrapStatLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatLastTime.setStatus('current')
sonusRtcpSlotLinkLossTrapStatActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 9), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkLossTrapStatActive.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5), )
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatusTable.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1), ).setIndexNames((0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatShelfIndex"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatSlotIndex"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress"), (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress"))
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatusEntry.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatShelfIndex.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatSlotIndex.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatCount.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatTotalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatTotalCount.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatStartTime.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatLastTime.setStatus('current')
sonusRtcpSlotLinkAbsenceTrapStatActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 9), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpSlotLinkAbsenceTrapStatActive.setStatus('current')
sonusRtcpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2))
sonusRtcpMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0))
sonusRtcpMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1))
sonusRtcpLocalIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpLocalIpAddr.setStatus('current')
sonusRtcpRemoteIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusRtcpRemoteIpAddr.setStatus('current')
sonusRtcpPacketLossThresholdExceededNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 1)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusRtcpPacketLossThresholdExceededNotification.setStatus('current')
sonusRtcpPacketLossThresholdClearedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 2)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusRtcpPacketLossThresholdClearedNotification.setStatus('current')
sonusRtcpNoRtpOrRtcpPacketsReceivedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 3)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusRtcpNoRtpOrRtcpPacketsReceivedNotification.setStatus('current')
sonusRtcpNoRtpOrRtcpPacketsClearedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 4)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusRtcpNoRtpOrRtcpPacketsClearedNotification.setStatus('current')
mibBuilder.exportSymbols("SONUS-RTCP-MIB", sonusRtcpRemoteIpAddr=sonusRtcpRemoteIpAddr, sonusRtcpSlotLinkLossTrapStatDestIpAddress=sonusRtcpSlotLinkLossTrapStatDestIpAddress, sonusRtcpSlotLinkAbsenceTrapStatSlotIndex=sonusRtcpSlotLinkAbsenceTrapStatSlotIndex, sonusRtcpPacketLossThresholdExceededNotification=sonusRtcpPacketLossThresholdExceededNotification, sonusRtcpLocalIpAddr=sonusRtcpLocalIpAddr, sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress=sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress, sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset=sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset, sonusRtcpSlotLinkAbsenceTrapStatTotalCount=sonusRtcpSlotLinkAbsenceTrapStatTotalCount, sonusRtcpSlotLinkAbsenceTrapStatLastTime=sonusRtcpSlotLinkAbsenceTrapStatLastTime, sonusRtcpSlotLinkAbsenceTrapStatusTable=sonusRtcpSlotLinkAbsenceTrapStatusTable, sonusRtcpNoRtpOrRtcpPacketsReceivedNotification=sonusRtcpNoRtpOrRtcpPacketsReceivedNotification, sonusRtcpSlotLinkLossTrapStatCount=sonusRtcpSlotLinkLossTrapStatCount, sonusRtcpMIBObjects=sonusRtcpMIBObjects, sonusRtcpShelfAdmnEntry=sonusRtcpShelfAdmnEntry, sonusRtcpSlotLinkLossTrapStatActive=sonusRtcpSlotLinkLossTrapStatActive, sonusRtcpMIB=sonusRtcpMIB, sonusRtcpSlotLinkAbsenceTrapStatCount=sonusRtcpSlotLinkAbsenceTrapStatCount, sonusRtcpSlotLinkLossTrapStatSlotIndex=sonusRtcpSlotLinkLossTrapStatSlotIndex, sonusRtcpSlotLinkAbsenceTrapStatStartTime=sonusRtcpSlotLinkAbsenceTrapStatStartTime, sonusRtcpMIBNotificationsObjects=sonusRtcpMIBNotificationsObjects, sonusRtcpSlotLinkLossTrapStatLastTime=sonusRtcpSlotLinkLossTrapStatLastTime, sonusRtcpPacketLossThresholdClearedNotification=sonusRtcpPacketLossThresholdClearedNotification, PYSNMP_MODULE_ID=sonusRtcpMIB, sonusRtcpShelfAdmnLossTrapHistoryTableReset=sonusRtcpShelfAdmnLossTrapHistoryTableReset, sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress=sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress, sonusRtcpSlotLinkAbsenceTrapStatShelfIndex=sonusRtcpSlotLinkAbsenceTrapStatShelfIndex, sonusRtcpSlotLinkLossTrapStatSrcIpAddress=sonusRtcpSlotLinkLossTrapStatSrcIpAddress, sonusRtcpShelfAdmnIndex=sonusRtcpShelfAdmnIndex, sonusRtcpSlotLinkLossTrapStatTotalCount=sonusRtcpSlotLinkLossTrapStatTotalCount, sonusRtcpSlotLinkLossTrapStatusEntry=sonusRtcpSlotLinkLossTrapStatusEntry, sonusRtcpSlotLinkLossTrapStatShelfIndex=sonusRtcpSlotLinkLossTrapStatShelfIndex, sonusRtcpSlotLinkLossTrapStatusTable=sonusRtcpSlotLinkLossTrapStatusTable, sonusRtcpShelfAdmnEstablishInterval=sonusRtcpShelfAdmnEstablishInterval, sonusRtcpShelfAdmnAbsenceTrapHistoryEntries=sonusRtcpShelfAdmnAbsenceTrapHistoryEntries, sonusRtcpSlotLinkAbsenceTrapStatusEntry=sonusRtcpSlotLinkAbsenceTrapStatusEntry, sonusRtcpMIBNotifications=sonusRtcpMIBNotifications, sonusRtcpShelfAdmnLossTrapHistoryEntries=sonusRtcpShelfAdmnLossTrapHistoryEntries, sonusRtcpSlotLinkLossTrapStatStartTime=sonusRtcpSlotLinkLossTrapStatStartTime, sonusRtcpShelfAdmnTable=sonusRtcpShelfAdmnTable, sonusRtcpShelfAdmnSrInterval=sonusRtcpShelfAdmnSrInterval, sonusRtcpNoRtpOrRtcpPacketsClearedNotification=sonusRtcpNoRtpOrRtcpPacketsClearedNotification, sonusRtcpMIBNotificationsPrefix=sonusRtcpMIBNotificationsPrefix, sonusRtcpSlotLinkAbsenceTrapStatActive=sonusRtcpSlotLinkAbsenceTrapStatActive)

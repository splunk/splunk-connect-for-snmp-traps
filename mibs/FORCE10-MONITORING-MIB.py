#
# PySNMP MIB module FORCE10-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORCE10-MONITORING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
F10ProcessorModuleType, F10SlotID, F10QueueID, F10CycloneVersion, F10VlanID, F10PortPipeID = mibBuilder.importSymbols("FORCE10-TC", "F10ProcessorModuleType", "F10SlotID", "F10QueueID", "F10CycloneVersion", "F10VlanID", "F10PortPipeID")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, IpAddress, ObjectIdentity, iso, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "iso", "MibIdentifier", "TimeTicks", "Counter32")
DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
f10MonitoringMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 3))
f10MonitoringMib.setRevisions(('2008-12-18 12:00', '1906-01-20 00:00', '2000-11-02 10:30',))
if mibBuilder.loadTexts: f10MonitoringMib.setLastUpdated('200812181200Z')
if mibBuilder.loadTexts: f10MonitoringMib.setOrganization('Force10 Networks, Inc.')
f10MonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 1))
f10MonQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2))
f10MonMac = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3))
f10MonIfQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4))
f10NetworkStat = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5))
f10IpStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 1))
f10ArpStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2))
f10MonMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version1", 1), ("version1dot1", 2), ("version1dot2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MonMibVersion.setStatus('current')
f10MonQueueGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 1))
f10MonMaxQueue = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MonMaxQueue.setStatus('current')
f10InQueueStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2), )
if mibBuilder.loadTexts: f10InQueueStatisticsTable.setStatus('current')
f10InQueueStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FORCE10-MONITORING-MIB", "f10InQueueId"))
if mibBuilder.loadTexts: f10InQueueStatisticsEntry.setStatus('current')
f10InQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 1), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueId.setStatus('current')
f10InQueueDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueDropPackets.setStatus('current')
f10InQueueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueBytes.setStatus('current')
f10InQueueMatchPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueMatchPackets.setStatus('current')
f10InQueueMatchBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueMatchBytes.setStatus('current')
f10InQueueMatchBps = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueMatchBps.setStatus('current')
f10InQueueCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 7), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueCycloneVersion.setStatus('current')
f10InQueueBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueueBytesCount.setStatus('current')
f10InQueuePktsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10InQueuePktsCount.setStatus('current')
f10OutQueueStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3), )
if mibBuilder.loadTexts: f10OutQueueStatisticsTable.setStatus('current')
f10OutQueueStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FORCE10-MONITORING-MIB", "f10OutQueueId"))
if mibBuilder.loadTexts: f10OutQueueStatisticsEntry.setStatus('current')
f10OutQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 1), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueueId.setStatus('current')
f10OutQueuePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueuePackets.setStatus('current')
f10OutQueueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueueBytes.setStatus('current')
f10OutQueueBps = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueueBps.setStatus('current')
f10OutQueueCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 5), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueueCycloneVersion.setStatus('current')
f10OutQueueBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10OutQueueBytesCount.setStatus('current')
f10WredStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4), )
if mibBuilder.loadTexts: f10WredStatisticsTable.setStatus('current')
f10WredStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FORCE10-MONITORING-MIB", "f10WredQueueId"))
if mibBuilder.loadTexts: f10WredStatisticsEntry.setStatus('current')
f10WredQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 1), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredQueueId.setStatus('current')
f10WredGreenName = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenName.setStatus('current')
f10WredGreenThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenThresholdLow.setStatus('current')
f10WredGreenThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenThresholdHigh.setStatus('current')
f10WredGreenDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenDropPackets.setStatus('current')
f10WredGreenReserve1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenReserve1.setStatus('current')
f10WredGreenReserve2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredGreenReserve2.setStatus('current')
f10WredYellowName = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowName.setStatus('current')
f10WredYellowThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowThresholdLow.setStatus('current')
f10WredYellowThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowThresholdHigh.setStatus('current')
f10WredYellowDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowDropPackets.setStatus('current')
f10WredYellowReserve1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowReserve1.setStatus('current')
f10WredYellowReserve2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredYellowReserve2.setStatus('current')
f10WredRedName = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedName.setStatus('current')
f10WredRedThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedThresholdLow.setStatus('current')
f10WredRedThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedThresholdHigh.setStatus('current')
f10WredRedDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedDropPackets.setStatus('current')
f10WredRedReserve1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedReserve1.setStatus('current')
f10WredRedReserve2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 2, 4, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10WredRedReserve2.setStatus('current')
f10MacGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 1))
f10MacAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2))
f10MacAccountingDestTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1), )
if mibBuilder.loadTexts: f10MacAccountingDestTable.setStatus('current')
f10MacAccountingDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1), ).setIndexNames((0, "FORCE10-MONITORING-MIB", "f10MacAccInIfIndex"), (0, "FORCE10-MONITORING-MIB", "f10MacAccVlan"), (0, "FORCE10-MONITORING-MIB", "f10MacAccMacAddr"))
if mibBuilder.loadTexts: f10MacAccountingDestEntry.setStatus('current')
f10MacAccInIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccInIfIndex.setStatus('current')
f10MacAccVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 2), F10VlanID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccVlan.setStatus('current')
f10MacAccMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccMacAddr.setStatus('current')
f10MacAccOutIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccOutIfIndex.setStatus('current')
f10MacAccPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccPackets.setStatus('current')
f10MacAccBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 3, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10MacAccBytes.setStatus('current')
f10MonIfQueueGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 1))
f10IngQueueUnicastStatTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2), )
if mibBuilder.loadTexts: f10IngQueueUnicastStatTable.setStatus('current')
f10IngQueueUnicastStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1), ).setIndexNames((0, "FORCE10-MONITORING-MIB", "f10IngUnicastSrcCard"), (0, "FORCE10-MONITORING-MIB", "f10IngUnicastDestCard"), (0, "FORCE10-MONITORING-MIB", "f10IngUnicastSrcPortPipe"), (0, "FORCE10-MONITORING-MIB", "f10IngUnicastDestPortPipe"), (0, "FORCE10-MONITORING-MIB", "f10IngUnicastQueueId"))
if mibBuilder.loadTexts: f10IngQueueUnicastStatEntry.setStatus('current')
f10IngUnicastSrcCard = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 1), F10SlotID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastSrcCard.setStatus('current')
f10IngUnicastDestCard = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 2), F10SlotID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastDestCard.setStatus('current')
f10IngUnicastSrcPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 3), F10PortPipeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastSrcPortPipe.setStatus('current')
f10IngUnicastDestPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 4), F10PortPipeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastDestPortPipe.setStatus('current')
f10IngUnicastQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 5), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastQueueId.setStatus('current')
f10IngUnicastCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 6), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastCycloneVersion.setStatus('current')
f10IngUnicastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastBytes.setStatus('current')
f10IngUnicastBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastBytesCount.setStatus('current')
f10IngUnicastPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastPacketCount.setStatus('current')
f10IngUnicastGreenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastGreenMin.setStatus('current')
f10IngUnicastGreenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastGreenMax.setStatus('current')
f10IngUnicastGreenDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastGreenDrop.setStatus('current')
f10IngUnicastYellowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastYellowMin.setStatus('current')
f10IngUnicastYellowMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastYellowMax.setStatus('current')
f10IngUnicastYellowDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastYellowDrop.setStatus('current')
f10IngUnicastRedDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngUnicastRedDrop.setStatus('current')
f10IngQueueMulticastStatTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3), )
if mibBuilder.loadTexts: f10IngQueueMulticastStatTable.setStatus('current')
f10IngQueueMulticastStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1), ).setIndexNames((0, "FORCE10-MONITORING-MIB", "f10IngMulticastSrcCard"), (0, "FORCE10-MONITORING-MIB", "f10IngMulticastSrcPortPipe"), (0, "FORCE10-MONITORING-MIB", "f10IngMulticastQueueId"))
if mibBuilder.loadTexts: f10IngQueueMulticastStatEntry.setStatus('current')
f10IngMulticastSrcCard = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 1), F10SlotID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastSrcCard.setStatus('current')
f10IngMulticastSrcPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 2), F10PortPipeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastSrcPortPipe.setStatus('current')
f10IngMulticastQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 3), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastQueueId.setStatus('current')
f10IngMulticastCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 4), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastCycloneVersion.setStatus('current')
f10IngMulticastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastBytes.setStatus('current')
f10IngMulticastBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastBytesCount.setStatus('current')
f10IngMulticastPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastPacketCount.setStatus('current')
f10IngMulticastGreenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastGreenMin.setStatus('current')
f10IngMulticastGreenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastGreenMax.setStatus('current')
f10IngMulticastGreenDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastGreenDrop.setStatus('current')
f10IngMulticastYellowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastYellowMin.setStatus('current')
f10IngMulticastYellowMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastYellowMax.setStatus('current')
f10IngMulticastYellowDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastYellowDrop.setStatus('current')
f10IngMulticastRedDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IngMulticastRedDrop.setStatus('current')
f10EgQueueUnicastStatTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4), )
if mibBuilder.loadTexts: f10EgQueueUnicastStatTable.setStatus('current')
f10EgQueueUnicastStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FORCE10-MONITORING-MIB", "f10EgUnicastQueueId"))
if mibBuilder.loadTexts: f10EgQueueUnicastStatEntry.setStatus('current')
f10EgUnicastQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 1), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastQueueId.setStatus('current')
f10EgUnicastCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 2), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastCycloneVersion.setStatus('current')
f10EgUnicastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastBytes.setStatus('current')
f10EgUnicastBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastBytesCount.setStatus('current')
f10EgUnicastPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastPacketCount.setStatus('current')
f10EgUnicastGreenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastGreenMin.setStatus('current')
f10EgUnicastGreenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastGreenMax.setStatus('current')
f10EgUnicastGreenDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastGreenDrop.setStatus('current')
f10EgUnicastYellowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastYellowMin.setStatus('current')
f10EgUnicastYellowMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastYellowMax.setStatus('current')
f10EgUnicastYellowDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastYellowDrop.setStatus('current')
f10EgUnicastRedDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgUnicastRedDrop.setStatus('current')
f10EgQueueMulticastStatTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5), )
if mibBuilder.loadTexts: f10EgQueueMulticastStatTable.setStatus('current')
f10EgQueueMulticastStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FORCE10-MONITORING-MIB", "f10EgMulticastQueueId"))
if mibBuilder.loadTexts: f10EgQueueMulticastStatEntry.setStatus('current')
f10EgMulticastQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 1), F10QueueID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastQueueId.setStatus('current')
f10EgMulticastCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 2), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastCycloneVersion.setStatus('current')
f10EgMulticastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastBytes.setStatus('current')
f10EgMulticastBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastBytesCount.setStatus('current')
f10EgMulticastPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastPacketCount.setStatus('current')
f10EgMulticastGreenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastGreenMin.setStatus('current')
f10EgMulticastGreenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastGreenMax.setStatus('current')
f10EgMulticastGreenDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastGreenDrop.setStatus('current')
f10EgMulticastYellowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastYellowMin.setStatus('current')
f10EgMulticastYellowMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastYellowMax.setStatus('current')
f10EgMulticastYellowDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastYellowDrop.setStatus('current')
f10EgMulticastRedDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 5, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10EgMulticastRedDrop.setStatus('current')
f10CpuIngQueueUnicastStatTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6), )
if mibBuilder.loadTexts: f10CpuIngQueueUnicastStatTable.setStatus('current')
f10CpuIngQueueUnicastStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1), ).setIndexNames((0, "FORCE10-MONITORING-MIB", "f10CpuIngUnicastSrcCard"), (0, "FORCE10-MONITORING-MIB", "f10CpuIngUnicastSrcPortPipe"), (0, "FORCE10-MONITORING-MIB", "f10CpuIngUnicastDestCpu"), (0, "FORCE10-MONITORING-MIB", "f10CpuIngUnicastQueueId"))
if mibBuilder.loadTexts: f10CpuIngQueueUnicastStatEntry.setStatus('current')
f10CpuIngUnicastSrcCard = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 1), F10SlotID())
if mibBuilder.loadTexts: f10CpuIngUnicastSrcCard.setStatus('current')
f10CpuIngUnicastSrcPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 2), F10PortPipeID())
if mibBuilder.loadTexts: f10CpuIngUnicastSrcPortPipe.setStatus('current')
f10CpuIngUnicastDestCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 3), F10ProcessorModuleType())
if mibBuilder.loadTexts: f10CpuIngUnicastDestCpu.setStatus('current')
f10CpuIngUnicastQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 4), F10QueueID())
if mibBuilder.loadTexts: f10CpuIngUnicastQueueId.setStatus('current')
f10CpuIngUnicastCycloneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 5), F10CycloneVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastCycloneVersion.setStatus('current')
f10CpuIngUnicastBytesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastBytesCount.setStatus('current')
f10CpuIngUnicastPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastPacketCount.setStatus('current')
f10CpuIngUnicastGreenMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastGreenMin.setStatus('current')
f10CpuIngUnicastGreenMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastGreenMax.setStatus('current')
f10CpuIngUnicastGreenDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastGreenDrop.setStatus('current')
f10CpuIngUnicastYellowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastYellowMin.setStatus('current')
f10CpuIngUnicastYellowMax = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastYellowMax.setStatus('current')
f10CpuIngUnicastYellowDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastYellowDrop.setStatus('current')
f10CpuIngUnicastRedDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 3, 4, 6, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10CpuIngUnicastRedDrop.setStatus('current')
f10BcastPktRecv = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10BcastPktRecv.setStatus('current')
f10BcastPktSent = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10BcastPktSent.setStatus('current')
f10McastPktRecv = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10McastPktRecv.setStatus('current')
f10McastPktSent = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10McastPktSent.setStatus('current')
f10ArpReqRecv = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ArpReqRecv.setStatus('current')
f10ArpReqSent = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ArpReqSent.setStatus('current')
f10ArpReplyRecv = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ArpReplyRecv.setStatus('current')
f10ArpReplySent = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ArpReplySent.setStatus('current')
f10ArpProxySent = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 3, 5, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ArpProxySent.setStatus('current')
mibBuilder.exportSymbols("FORCE10-MONITORING-MIB", f10WredRedDropPackets=f10WredRedDropPackets, f10ArpReqRecv=f10ArpReqRecv, f10WredGreenReserve2=f10WredGreenReserve2, f10OutQueueStatisticsTable=f10OutQueueStatisticsTable, f10CpuIngUnicastQueueId=f10CpuIngUnicastQueueId, f10MonMac=f10MonMac, f10EgUnicastBytesCount=f10EgUnicastBytesCount, f10InQueueBytes=f10InQueueBytes, f10IngUnicastGreenMin=f10IngUnicastGreenMin, f10IngMulticastRedDrop=f10IngMulticastRedDrop, f10InQueueBytesCount=f10InQueueBytesCount, f10OutQueueBytes=f10OutQueueBytes, f10CpuIngUnicastYellowMin=f10CpuIngUnicastYellowMin, f10WredRedReserve1=f10WredRedReserve1, f10CpuIngUnicastGreenMin=f10CpuIngUnicastGreenMin, f10EgMulticastYellowMin=f10EgMulticastYellowMin, f10WredStatisticsTable=f10WredStatisticsTable, f10NetworkStat=f10NetworkStat, f10EgUnicastPacketCount=f10EgUnicastPacketCount, f10InQueueId=f10InQueueId, f10CpuIngQueueUnicastStatTable=f10CpuIngQueueUnicastStatTable, f10EgQueueMulticastStatTable=f10EgQueueMulticastStatTable, f10MonGroup=f10MonGroup, f10CpuIngUnicastYellowMax=f10CpuIngUnicastYellowMax, f10IngMulticastGreenMin=f10IngMulticastGreenMin, f10IngMulticastQueueId=f10IngMulticastQueueId, f10InQueueMatchBps=f10InQueueMatchBps, f10WredQueueId=f10WredQueueId, f10WredRedThresholdLow=f10WredRedThresholdLow, f10IngUnicastSrcCard=f10IngUnicastSrcCard, f10IngUnicastYellowDrop=f10IngUnicastYellowDrop, f10EgMulticastYellowMax=f10EgMulticastYellowMax, f10MacAccBytes=f10MacAccBytes, f10EgMulticastCycloneVersion=f10EgMulticastCycloneVersion, f10IpStatistic=f10IpStatistic, f10MacAccounting=f10MacAccounting, f10WredRedThresholdHigh=f10WredRedThresholdHigh, f10ArpReplyRecv=f10ArpReplyRecv, f10InQueueStatisticsEntry=f10InQueueStatisticsEntry, f10MacAccountingDestEntry=f10MacAccountingDestEntry, f10MacAccPackets=f10MacAccPackets, f10IngUnicastBytes=f10IngUnicastBytes, f10InQueueStatisticsTable=f10InQueueStatisticsTable, f10MonitoringMib=f10MonitoringMib, f10IngUnicastQueueId=f10IngUnicastQueueId, f10WredGreenName=f10WredGreenName, f10WredYellowThresholdHigh=f10WredYellowThresholdHigh, f10OutQueueCycloneVersion=f10OutQueueCycloneVersion, f10ArpStatistic=f10ArpStatistic, f10EgQueueMulticastStatEntry=f10EgQueueMulticastStatEntry, f10EgMulticastBytesCount=f10EgMulticastBytesCount, f10BcastPktRecv=f10BcastPktRecv, f10CpuIngUnicastRedDrop=f10CpuIngUnicastRedDrop, f10MonQueueGroup=f10MonQueueGroup, f10IngUnicastYellowMax=f10IngUnicastYellowMax, f10ArpReplySent=f10ArpReplySent, f10EgMulticastYellowDrop=f10EgMulticastYellowDrop, f10MonIfQueueGroup=f10MonIfQueueGroup, f10IngUnicastDestPortPipe=f10IngUnicastDestPortPipe, f10EgUnicastRedDrop=f10EgUnicastRedDrop, f10CpuIngUnicastPacketCount=f10CpuIngUnicastPacketCount, f10CpuIngUnicastBytesCount=f10CpuIngUnicastBytesCount, f10IngMulticastBytesCount=f10IngMulticastBytesCount, f10IngMulticastGreenDrop=f10IngMulticastGreenDrop, f10MacGroup=f10MacGroup, f10MonIfQueue=f10MonIfQueue, f10WredYellowReserve2=f10WredYellowReserve2, f10IngMulticastYellowMax=f10IngMulticastYellowMax, f10IngUnicastRedDrop=f10IngUnicastRedDrop, f10CpuIngUnicastYellowDrop=f10CpuIngUnicastYellowDrop, f10McastPktSent=f10McastPktSent, f10CpuIngUnicastSrcCard=f10CpuIngUnicastSrcCard, f10WredGreenThresholdHigh=f10WredGreenThresholdHigh, f10ArpProxySent=f10ArpProxySent, f10CpuIngUnicastCycloneVersion=f10CpuIngUnicastCycloneVersion, f10MonMibVersion=f10MonMibVersion, f10CpuIngUnicastGreenDrop=f10CpuIngUnicastGreenDrop, f10IngMulticastGreenMax=f10IngMulticastGreenMax, f10WredGreenDropPackets=f10WredGreenDropPackets, f10MacAccVlan=f10MacAccVlan, f10OutQueuePackets=f10OutQueuePackets, f10IngUnicastSrcPortPipe=f10IngUnicastSrcPortPipe, f10IngMulticastSrcPortPipe=f10IngMulticastSrcPortPipe, f10OutQueueBytesCount=f10OutQueueBytesCount, f10CpuIngQueueUnicastStatEntry=f10CpuIngQueueUnicastStatEntry, f10WredRedName=f10WredRedName, f10EgUnicastGreenDrop=f10EgUnicastGreenDrop, f10InQueueMatchBytes=f10InQueueMatchBytes, f10IngMulticastPacketCount=f10IngMulticastPacketCount, f10MacAccInIfIndex=f10MacAccInIfIndex, PYSNMP_MODULE_ID=f10MonitoringMib, f10EgMulticastPacketCount=f10EgMulticastPacketCount, f10WredYellowName=f10WredYellowName, f10EgUnicastGreenMin=f10EgUnicastGreenMin, f10CpuIngUnicastSrcPortPipe=f10CpuIngUnicastSrcPortPipe, f10OutQueueStatisticsEntry=f10OutQueueStatisticsEntry, f10EgUnicastCycloneVersion=f10EgUnicastCycloneVersion, f10IngMulticastBytes=f10IngMulticastBytes, f10IngUnicastDestCard=f10IngUnicastDestCard, f10IngQueueMulticastStatTable=f10IngQueueMulticastStatTable, f10IngUnicastCycloneVersion=f10IngUnicastCycloneVersion, f10IngQueueMulticastStatEntry=f10IngQueueMulticastStatEntry, f10InQueueMatchPackets=f10InQueueMatchPackets, f10EgUnicastYellowMax=f10EgUnicastYellowMax, f10MacAccOutIfIndex=f10MacAccOutIfIndex, f10MacAccountingDestTable=f10MacAccountingDestTable, f10WredGreenReserve1=f10WredGreenReserve1, f10EgMulticastGreenMin=f10EgMulticastGreenMin, f10IngMulticastCycloneVersion=f10IngMulticastCycloneVersion, f10IngQueueUnicastStatTable=f10IngQueueUnicastStatTable, f10EgUnicastBytes=f10EgUnicastBytes, f10IngQueueUnicastStatEntry=f10IngQueueUnicastStatEntry, f10InQueueDropPackets=f10InQueueDropPackets, f10EgQueueUnicastStatTable=f10EgQueueUnicastStatTable, f10CpuIngUnicastGreenMax=f10CpuIngUnicastGreenMax, f10EgQueueUnicastStatEntry=f10EgQueueUnicastStatEntry, f10EgMulticastRedDrop=f10EgMulticastRedDrop, f10MonMaxQueue=f10MonMaxQueue, f10WredYellowThresholdLow=f10WredYellowThresholdLow, f10InQueueCycloneVersion=f10InQueueCycloneVersion, f10EgUnicastYellowDrop=f10EgUnicastYellowDrop, f10IngUnicastYellowMin=f10IngUnicastYellowMin, f10InQueuePktsCount=f10InQueuePktsCount, f10WredYellowReserve1=f10WredYellowReserve1, f10EgUnicastYellowMin=f10EgUnicastYellowMin, f10IngMulticastYellowDrop=f10IngMulticastYellowDrop, f10IngMulticastSrcCard=f10IngMulticastSrcCard, f10BcastPktSent=f10BcastPktSent, f10IngUnicastPacketCount=f10IngUnicastPacketCount, f10WredGreenThresholdLow=f10WredGreenThresholdLow, f10IngUnicastGreenMax=f10IngUnicastGreenMax, f10CpuIngUnicastDestCpu=f10CpuIngUnicastDestCpu, f10MonQueue=f10MonQueue, f10IngUnicastGreenDrop=f10IngUnicastGreenDrop, f10EgUnicastGreenMax=f10EgUnicastGreenMax, f10EgUnicastQueueId=f10EgUnicastQueueId, f10WredStatisticsEntry=f10WredStatisticsEntry, f10OutQueueBps=f10OutQueueBps, f10EgMulticastQueueId=f10EgMulticastQueueId, f10EgMulticastBytes=f10EgMulticastBytes, f10WredYellowDropPackets=f10WredYellowDropPackets, f10EgMulticastGreenMax=f10EgMulticastGreenMax, f10IngMulticastYellowMin=f10IngMulticastYellowMin, f10MacAccMacAddr=f10MacAccMacAddr, f10McastPktRecv=f10McastPktRecv, f10OutQueueId=f10OutQueueId, f10ArpReqSent=f10ArpReqSent, f10WredRedReserve2=f10WredRedReserve2, f10IngUnicastBytesCount=f10IngUnicastBytesCount, f10EgMulticastGreenDrop=f10EgMulticastGreenDrop)

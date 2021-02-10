#
# PySNMP MIB module DLINK-3100-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-STATISTICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:34:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, TimeTicks, Unsigned32, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, Counter32, iso, Counter64, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter32", "iso", "Counter64", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141))
rlStatistics.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlStatistics.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlStatistics.setOrganization('Dlink, Inc.')
rlStatisticsPacketTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketTable.setStatus('current')
rlStatisticsPacketEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlStatisticsPacketEntry.setStatus('current')
rlStatisticsPacket64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket64Octets.setStatus('current')
rlStatisticsPacket65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket65to127Octets.setStatus('current')
rlStatisticsPacket128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket128to255Octets.setStatus('current')
rlStatisticsPacket256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket256to511Octets.setStatus('current')
rlStatisticsPacket512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket512to1023Octets.setStatus('current')
rlStatisticsPacket1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacket1024to1518Octets.setStatus('current')
rlStatisticsPacketOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketOversizePkts.setStatus('current')
rlStatisticsPacketUnicastRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketUnicastRx.setStatus('current')
rlStatisticsPacketMulticastRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketMulticastRx.setStatus('current')
rlStatisticsPacketBroadcastRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketBroadcastRx.setStatus('current')
rlStatisticsPacketRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketRxBytes.setStatus('current')
rlStatisticsPacketRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketRxFrames.setStatus('current')
rlStatisticsPacketTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketTxBytes.setStatus('current')
rlStatisticsPacketTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPacketTxFrames.setStatus('current')
rlStatisticsPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPortTable.setStatus('current')
rlStatisticsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1), ).setMaxAccess("readonly").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlStatisticsPortEntry.setStatus('current')
rlStatisticsPortRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPortRx.setStatus('current')
rlStatisticsPortTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPortTx.setStatus('current')
rlStatisticsPortUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStatisticsPortUtilization.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-STATISTICS-MIB", rlStatistics=rlStatistics, rlStatisticsPacketRxFrames=rlStatisticsPacketRxFrames, rlStatisticsPacket1024to1518Octets=rlStatisticsPacket1024to1518Octets, rlStatisticsPortUtilization=rlStatisticsPortUtilization, rlStatisticsPortRx=rlStatisticsPortRx, rlStatisticsPacket64Octets=rlStatisticsPacket64Octets, rlStatisticsPacketRxBytes=rlStatisticsPacketRxBytes, rlStatisticsPacketOversizePkts=rlStatisticsPacketOversizePkts, rlStatisticsPortEntry=rlStatisticsPortEntry, rlStatisticsPacketMulticastRx=rlStatisticsPacketMulticastRx, rlStatisticsPacketTable=rlStatisticsPacketTable, rlStatisticsPacket128to255Octets=rlStatisticsPacket128to255Octets, rlStatisticsPacket256to511Octets=rlStatisticsPacket256to511Octets, rlStatisticsPortTx=rlStatisticsPortTx, rlStatisticsPacketTxFrames=rlStatisticsPacketTxFrames, rlStatisticsPacketTxBytes=rlStatisticsPacketTxBytes, rlStatisticsPortTable=rlStatisticsPortTable, rlStatisticsPacket65to127Octets=rlStatisticsPacket65to127Octets, rlStatisticsPacketUnicastRx=rlStatisticsPacketUnicastRx, rlStatisticsPacketEntry=rlStatisticsPacketEntry, PYSNMP_MODULE_ID=rlStatistics, rlStatisticsPacket512to1023Octets=rlStatisticsPacket512to1023Octets, rlStatisticsPacketBroadcastRx=rlStatisticsPacketBroadcastRx)
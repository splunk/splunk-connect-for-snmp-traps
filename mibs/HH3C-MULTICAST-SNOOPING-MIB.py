#
# PySNMP MIB module HH3C-MULTICAST-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MULTICAST-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, ModuleIdentity, Integer32, IpAddress, TimeTicks, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "Bits")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
hh3cMulticastSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 123))
hh3cMulticastSnoop.setRevisions(('2014-05-14 17:00',))
if mibBuilder.loadTexts: hh3cMulticastSnoop.setLastUpdated('201405141700Z')
if mibBuilder.loadTexts: hh3cMulticastSnoop.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cVirtualUnitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("vlan", 1), ("vsi", 2))

hh3cMulticastSnoopObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1))
hh3cMcsGlobalConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1), )
if mibBuilder.loadTexts: hh3cMcsGlobalConfigTable.setStatus('current')
hh3cMcsGlobalConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsGlbSnoopingType"))
if mibBuilder.loadTexts: hh3cMcsGlobalConfigEntry.setStatus('current')
hh3cMcsGlbSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsGlbSnoopingType.setStatus('current')
hh3cMcsGlbRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbRowStatus.setStatus('current')
hh3cMcsGlbEntryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbEntryLimit.setStatus('current')
hh3cMcsGlbHostAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8097894)).clone(260)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbHostAgingTime.setStatus('current')
hh3cMcsGlbMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3174)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbMaxResponseTime.setStatus('current')
hh3cMcsGlbRouterAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8097894)).clone(260)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbRouterAgingTime.setStatus('current')
hh3cMcsGlbLastMemQryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbLastMemQryInterval.setStatus('current')
hh3cMcsGlbDropUnknownEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsGlbDropUnknownEnabled.setStatus('current')
hh3cMcsVirtualUnitConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2), )
if mibBuilder.loadTexts: hh3cMcsVirtualUnitConfigTable.setStatus('current')
hh3cMcsVirtualUnitConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUID"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUSnoopingType"))
if mibBuilder.loadTexts: hh3cMcsVirtualUnitConfigEntry.setStatus('current')
hh3cMcsVUType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 1), Hh3cVirtualUnitType())
if mibBuilder.loadTexts: hh3cMcsVUType.setStatus('current')
hh3cMcsVUID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hh3cMcsVUID.setStatus('current')
hh3cMcsVUSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 3), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsVUSnoopingType.setStatus('current')
hh3cMcsVURowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVURowStatus.setStatus('current')
hh3cMcsVUHostAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8097894))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUHostAgingTime.setStatus('current')
hh3cMcsVUMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3174))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUMaxResponseTime.setStatus('current')
hh3cMcsVURouterAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8097894))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVURouterAgingTime.setStatus('current')
hh3cMcsVULastMemQryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 25))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVULastMemQryInterval.setStatus('current')
hh3cMcsVUDropUnknownEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUDropUnknownEnabled.setStatus('current')
hh3cMcsVUPimSnoopingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUPimSnoopingEnabled.setStatus('current')
hh3cMcsVUVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 2), ValueRangeConstraint(3, 3), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUVersion.setStatus('current')
hh3cMcsVUQuerierEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUQuerierEnabled.setStatus('current')
hh3cMcsVUQuerierInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 31744)).clone(125)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUQuerierInterval.setStatus('current')
hh3cMcsVUGeneQuerierSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 14), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUGeneQuerierSourceAddress.setStatus('current')
hh3cMcsVUSpecQuerierSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 15), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUSpecQuerierSourceAddress.setStatus('current')
hh3cMcsVULeaveSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 16), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVULeaveSourceAddress.setStatus('current')
hh3cMcsVUReportSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 17), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsVUReportSourceAddress.setStatus('current')
hh3cMcsL2EntryTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3), )
if mibBuilder.loadTexts: hh3cMcsL2EntryTable.setStatus('current')
hh3cMcsL2EntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryVUType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryVUID"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryAddressType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryGroupAddress"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntrySourceAddress"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryIfIndex"))
if mibBuilder.loadTexts: hh3cMcsL2EntryEntry.setStatus('current')
hh3cMcsL2EntryVUType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 1), Hh3cVirtualUnitType())
if mibBuilder.loadTexts: hh3cMcsL2EntryVUType.setStatus('current')
hh3cMcsL2EntryVUID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hh3cMcsL2EntryVUID.setStatus('current')
hh3cMcsL2EntryAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 3), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsL2EntryAddressType.setStatus('current')
hh3cMcsL2EntryGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 4), InetAddress())
if mibBuilder.loadTexts: hh3cMcsL2EntryGroupAddress.setStatus('current')
hh3cMcsL2EntrySourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 5), InetAddress())
if mibBuilder.loadTexts: hh3cMcsL2EntrySourceAddress.setStatus('current')
hh3cMcsL2EntryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 6), InterfaceIndex())
if mibBuilder.loadTexts: hh3cMcsL2EntryIfIndex.setStatus('current')
hh3cMcsL2EntryPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("interface", 1), ("ac", 2), ("npw", 3), ("upw", 4), ("trill", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsL2EntryPortType.setStatus('current')
hh3cMcsL2EntryPortAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("d", 0), ("s", 1), ("p", 2), ("k", 3), ("r", 4), ("w", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsL2EntryPortAttribute.setStatus('current')
hh3cMcsPacketStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4), )
if mibBuilder.loadTexts: hh3cMcsPacketStatisticsTable.setStatus('current')
hh3cMcsPacketStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsStatisticsSnoopingType"))
if mibBuilder.loadTexts: hh3cMcsPacketStatisticsEntry.setStatus('current')
hh3cMcsStatisticsSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsStatisticsSnoopingType.setStatus('current')
hh3cMcsRxGeneryQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxGeneryQueryNum.setStatus('current')
hh3cMcsRxV2SpecificQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV2SpecificQueryNum.setStatus('current')
hh3cMcsRxV3SpecificQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV3SpecificQueryNum.setStatus('current')
hh3cMcsRxV3SpecificSGQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV3SpecificSGQueryNum.setStatus('current')
hh3cMcsRxV1ReportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV1ReportNum.setStatus('current')
hh3cMcsRxV2ReportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV2ReportNum.setStatus('current')
hh3cMcsRxV3ReportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV3ReportNum.setStatus('current')
hh3cMcsRxV3ErrCorReportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxV3ErrCorReportNum.setStatus('current')
hh3cMcsRxLeaveNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxLeaveNum.setStatus('current')
hh3cMcsRxPimHelloNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxPimHelloNum.setStatus('current')
hh3cMcsRxErrorPacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsRxErrorPacketNum.setStatus('current')
hh3cMcsTxV2SpecificQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsTxV2SpecificQueryNum.setStatus('current')
hh3cMcsTxV3SpecificQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsTxV3SpecificQueryNum.setStatus('current')
hh3cMcsTxV3SpecificSGQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMcsTxV3SpecificSGQueryNum.setStatus('current')
hh3cMcsPortJoinGroupConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5), )
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupConfigTable.setStatus('current')
hh3cMcsPortJoinGroupConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupIfIndex"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupSnoopingType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupVlanID"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupGroupAddress"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupSourceAddress"))
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupConfigEntry.setStatus('current')
hh3cMcsPortJoinGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupIfIndex.setStatus('current')
hh3cMcsPortJoinGroupSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupSnoopingType.setStatus('current')
hh3cMcsPortJoinGroupVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupVlanID.setStatus('current')
hh3cMcsPortJoinGroupGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 4), InetAddress())
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupGroupAddress.setStatus('current')
hh3cMcsPortJoinGroupSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 5), InetAddress())
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupSourceAddress.setStatus('current')
hh3cMcsPortJoinGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortJoinGroupStatus.setStatus('current')
hh3cMcsPortStaticGroupConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6), )
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupConfigTable.setStatus('current')
hh3cMcsPortStaticGroupConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupIfIndex"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupSnoopingType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupVlanID"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupGroupAddress"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupSourceAddress"))
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupConfigEntry.setStatus('current')
hh3cMcsPortStaticGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupIfIndex.setStatus('current')
hh3cMcsPortStaticGroupSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupSnoopingType.setStatus('current')
hh3cMcsPortStaticGroupVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupVlanID.setStatus('current')
hh3cMcsPortStaticGroupGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 4), InetAddress())
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupGroupAddress.setStatus('current')
hh3cMcsPortStaticGroupSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 5), InetAddress())
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupSourceAddress.setStatus('current')
hh3cMcsPortStaticGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortStaticGroupStatus.setStatus('current')
hh3cMcsRouterPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7), )
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigTable.setStatus('current')
hh3cMcsRouterPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigIfIndex"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigSnoopingType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigVlanID"))
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigEntry.setStatus('current')
hh3cMcsRouterPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigIfIndex.setStatus('current')
hh3cMcsRouterPortConfigSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigSnoopingType.setStatus('current')
hh3cMcsRouterPortConfigVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigVlanID.setStatus('current')
hh3cMcsRouterPortConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsRouterPortConfigRowStatus.setStatus('current')
hh3cMcsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8), )
if mibBuilder.loadTexts: hh3cMcsPortConfigTable.setStatus('current')
hh3cMcsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1), ).setIndexNames((0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigIfIndex"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigSnoopingType"), (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigVlanID"))
if mibBuilder.loadTexts: hh3cMcsPortConfigEntry.setStatus('current')
hh3cMcsPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cMcsPortConfigIfIndex.setStatus('current')
hh3cMcsPortConfigSnoopingType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hh3cMcsPortConfigSnoopingType.setStatus('current')
hh3cMcsPortConfigVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cMcsPortConfigVlanID.setStatus('current')
hh3cMcsPortConfigGroupLimitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortConfigGroupLimitNumber.setStatus('current')
hh3cMcsPortConfigFastLeaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortConfigFastLeaveStatus.setStatus('current')
hh3cMcsPortConfigGroupPolicyParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortConfigGroupPolicyParameter.setStatus('current')
hh3cMcsPortConfigOverflowReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortConfigOverflowReplace.setStatus('current')
hh3cMcsPortConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMcsPortConfigRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-MULTICAST-SNOOPING-MIB", hh3cMcsPortStaticGroupSnoopingType=hh3cMcsPortStaticGroupSnoopingType, hh3cMcsL2EntryEntry=hh3cMcsL2EntryEntry, hh3cMcsGlbMaxResponseTime=hh3cMcsGlbMaxResponseTime, hh3cMcsPortJoinGroupSnoopingType=hh3cMcsPortJoinGroupSnoopingType, hh3cMcsRouterPortConfigSnoopingType=hh3cMcsRouterPortConfigSnoopingType, hh3cMcsVUDropUnknownEnabled=hh3cMcsVUDropUnknownEnabled, hh3cMcsPortConfigVlanID=hh3cMcsPortConfigVlanID, hh3cMcsRxV2SpecificQueryNum=hh3cMcsRxV2SpecificQueryNum, hh3cMcsPortConfigIfIndex=hh3cMcsPortConfigIfIndex, hh3cMcsVULastMemQryInterval=hh3cMcsVULastMemQryInterval, hh3cMcsGlbLastMemQryInterval=hh3cMcsGlbLastMemQryInterval, hh3cMcsGlbHostAgingTime=hh3cMcsGlbHostAgingTime, hh3cMcsRxV2ReportNum=hh3cMcsRxV2ReportNum, hh3cMcsL2EntryVUID=hh3cMcsL2EntryVUID, hh3cMcsVUType=hh3cMcsVUType, hh3cMcsPortConfigFastLeaveStatus=hh3cMcsPortConfigFastLeaveStatus, hh3cMcsPortStaticGroupGroupAddress=hh3cMcsPortStaticGroupGroupAddress, hh3cMcsL2EntryAddressType=hh3cMcsL2EntryAddressType, hh3cMcsGlbDropUnknownEnabled=hh3cMcsGlbDropUnknownEnabled, hh3cMcsPortJoinGroupStatus=hh3cMcsPortJoinGroupStatus, hh3cMcsGlobalConfigEntry=hh3cMcsGlobalConfigEntry, hh3cMcsGlbEntryLimit=hh3cMcsGlbEntryLimit, hh3cMcsRxPimHelloNum=hh3cMcsRxPimHelloNum, hh3cMcsRxV1ReportNum=hh3cMcsRxV1ReportNum, hh3cMcsPortConfigGroupPolicyParameter=hh3cMcsPortConfigGroupPolicyParameter, hh3cMcsRouterPortConfigRowStatus=hh3cMcsRouterPortConfigRowStatus, hh3cMcsPortStaticGroupStatus=hh3cMcsPortStaticGroupStatus, hh3cMcsL2EntryVUType=hh3cMcsL2EntryVUType, hh3cMcsPortConfigRowStatus=hh3cMcsPortConfigRowStatus, hh3cMcsVURouterAgingTime=hh3cMcsVURouterAgingTime, hh3cMcsVUQuerierInterval=hh3cMcsVUQuerierInterval, hh3cMcsPortStaticGroupSourceAddress=hh3cMcsPortStaticGroupSourceAddress, hh3cMcsPortStaticGroupConfigEntry=hh3cMcsPortStaticGroupConfigEntry, hh3cMcsTxV2SpecificQueryNum=hh3cMcsTxV2SpecificQueryNum, PYSNMP_MODULE_ID=hh3cMulticastSnoop, hh3cMcsL2EntryPortAttribute=hh3cMcsL2EntryPortAttribute, hh3cMcsPacketStatisticsTable=hh3cMcsPacketStatisticsTable, hh3cMcsRouterPortConfigVlanID=hh3cMcsRouterPortConfigVlanID, hh3cMcsVUVersion=hh3cMcsVUVersion, hh3cMcsL2EntryTable=hh3cMcsL2EntryTable, hh3cMulticastSnoopObject=hh3cMulticastSnoopObject, hh3cMcsRxLeaveNum=hh3cMcsRxLeaveNum, hh3cMcsPortConfigOverflowReplace=hh3cMcsPortConfigOverflowReplace, hh3cMcsVULeaveSourceAddress=hh3cMcsVULeaveSourceAddress, hh3cMcsPortJoinGroupSourceAddress=hh3cMcsPortJoinGroupSourceAddress, hh3cMcsPortStaticGroupVlanID=hh3cMcsPortStaticGroupVlanID, hh3cMcsPortJoinGroupConfigEntry=hh3cMcsPortJoinGroupConfigEntry, hh3cMcsRxV3SpecificSGQueryNum=hh3cMcsRxV3SpecificSGQueryNum, hh3cMcsVUHostAgingTime=hh3cMcsVUHostAgingTime, hh3cMcsRxV3ErrCorReportNum=hh3cMcsRxV3ErrCorReportNum, hh3cMcsStatisticsSnoopingType=hh3cMcsStatisticsSnoopingType, hh3cMcsRxV3SpecificQueryNum=hh3cMcsRxV3SpecificQueryNum, hh3cMcsTxV3SpecificQueryNum=hh3cMcsTxV3SpecificQueryNum, hh3cMcsRouterPortConfigEntry=hh3cMcsRouterPortConfigEntry, hh3cMulticastSnoop=hh3cMulticastSnoop, hh3cMcsL2EntryIfIndex=hh3cMcsL2EntryIfIndex, hh3cMcsVUSpecQuerierSourceAddress=hh3cMcsVUSpecQuerierSourceAddress, hh3cMcsGlbRouterAgingTime=hh3cMcsGlbRouterAgingTime, hh3cMcsGlbSnoopingType=hh3cMcsGlbSnoopingType, hh3cMcsPortConfigEntry=hh3cMcsPortConfigEntry, hh3cMcsPortJoinGroupConfigTable=hh3cMcsPortJoinGroupConfigTable, hh3cMcsVUReportSourceAddress=hh3cMcsVUReportSourceAddress, hh3cMcsPacketStatisticsEntry=hh3cMcsPacketStatisticsEntry, hh3cMcsGlobalConfigTable=hh3cMcsGlobalConfigTable, hh3cMcsTxV3SpecificSGQueryNum=hh3cMcsTxV3SpecificSGQueryNum, hh3cMcsL2EntrySourceAddress=hh3cMcsL2EntrySourceAddress, hh3cMcsRouterPortConfigTable=hh3cMcsRouterPortConfigTable, hh3cMcsPortConfigTable=hh3cMcsPortConfigTable, hh3cMcsRxErrorPacketNum=hh3cMcsRxErrorPacketNum, hh3cMcsVUMaxResponseTime=hh3cMcsVUMaxResponseTime, hh3cMcsVUGeneQuerierSourceAddress=hh3cMcsVUGeneQuerierSourceAddress, hh3cMcsVirtualUnitConfigTable=hh3cMcsVirtualUnitConfigTable, hh3cMcsPortStaticGroupIfIndex=hh3cMcsPortStaticGroupIfIndex, hh3cMcsPortJoinGroupIfIndex=hh3cMcsPortJoinGroupIfIndex, hh3cMcsPortJoinGroupGroupAddress=hh3cMcsPortJoinGroupGroupAddress, hh3cMcsL2EntryPortType=hh3cMcsL2EntryPortType, hh3cMcsVUSnoopingType=hh3cMcsVUSnoopingType, Hh3cVirtualUnitType=Hh3cVirtualUnitType, hh3cMcsVUID=hh3cMcsVUID, hh3cMcsRouterPortConfigIfIndex=hh3cMcsRouterPortConfigIfIndex, hh3cMcsPortStaticGroupConfigTable=hh3cMcsPortStaticGroupConfigTable, hh3cMcsVUPimSnoopingEnabled=hh3cMcsVUPimSnoopingEnabled, hh3cMcsRxV3ReportNum=hh3cMcsRxV3ReportNum, hh3cMcsPortConfigGroupLimitNumber=hh3cMcsPortConfigGroupLimitNumber, hh3cMcsPortConfigSnoopingType=hh3cMcsPortConfigSnoopingType, hh3cMcsGlbRowStatus=hh3cMcsGlbRowStatus, hh3cMcsVUQuerierEnabled=hh3cMcsVUQuerierEnabled, hh3cMcsRxGeneryQueryNum=hh3cMcsRxGeneryQueryNum, hh3cMcsL2EntryGroupAddress=hh3cMcsL2EntryGroupAddress, hh3cMcsPortJoinGroupVlanID=hh3cMcsPortJoinGroupVlanID, hh3cMcsVURowStatus=hh3cMcsVURowStatus, hh3cMcsVirtualUnitConfigEntry=hh3cMcsVirtualUnitConfigEntry)

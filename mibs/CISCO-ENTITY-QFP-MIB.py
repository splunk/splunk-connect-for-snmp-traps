#
# PySNMP MIB module CISCO-ENTITY-QFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-QFP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, NotificationType, Gauge32, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Bits, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Bits", "ObjectIdentity", "TimeTicks", "iso")
DisplayString, TextualConvention, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "DateAndTime")
ciscoEntityQfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 715))
ciscoEntityQfpMIB.setRevisions(('2014-06-18 00:00', '2012-06-06 00:00', '2009-12-02 00:00',))
if mibBuilder.loadTexts: ciscoEntityQfpMIB.setLastUpdated('201406180000Z')
if mibBuilder.loadTexts: ciscoEntityQfpMIB.setOrganization('Cisco Systems, Inc.')
class CiscoQfpPacketRate(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class CiscoQfpBitRate(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class CiscoQfpTimeInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fiveSeconds", 1), ("oneMinute", 2), ("fiveMinutes", 3), ("sixtyMinutes", 4))

class CiscoQfpMemoryResource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dram", 1))

ciscoEntityQfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 0))
ciscoEntityQfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 1))
ciscoEntityQfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 2))
ciscoEntityQfp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1))
ciscoEntityQfpNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2))
ceqfpSystemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1), )
if mibBuilder.loadTexts: ceqfpSystemTable.setStatus('current')
ceqfpSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceqfpSystemEntry.setStatus('current')
ceqfpSystemTrafficDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("ingress", 2), ("egress", 3), ("both", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpSystemTrafficDirection.setStatus('current')
ceqfpSystemState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("reset", 2), ("init", 3), ("active", 4), ("activeSolo", 5), ("standby", 6), ("hotStandby", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpSystemState.setStatus('current')
ceqfpNumberSystemLoads = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpNumberSystemLoads.setStatus('current')
ceqfpSystemLastLoadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpSystemLastLoadTime.setStatus('current')
ceqfpFiveSecondUtilAlgo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("fiveSecSample", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpFiveSecondUtilAlgo.setStatus('current')
ceqfpOneMinuteUtilAlgo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("fiveSecSMA", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpOneMinuteUtilAlgo.setStatus('current')
ceqfpFiveMinutesUtilAlgo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("fiveSecSMA", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpFiveMinutesUtilAlgo.setStatus('current')
ceqfpSixtyMinutesUtilAlgo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("fiveSecSMA", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpSixtyMinutesUtilAlgo.setStatus('current')
ceqfpUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6), )
if mibBuilder.loadTexts: ceqfpUtilizationTable.setStatus('current')
ceqfpUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-QFP-MIB", "ceqfpUtilTimeInterval"))
if mibBuilder.loadTexts: ceqfpUtilizationEntry.setStatus('current')
ceqfpUtilTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 1), CiscoQfpTimeInterval())
if mibBuilder.loadTexts: ceqfpUtilTimeInterval.setStatus('current')
ceqfpUtilInputPriorityPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 2), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputPriorityPktRate.setStatus('current')
ceqfpUtilInputPriorityBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 3), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputPriorityBitRate.setStatus('current')
ceqfpUtilInputNonPriorityPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 4), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputNonPriorityPktRate.setStatus('current')
ceqfpUtilInputNonPriorityBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 5), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputNonPriorityBitRate.setStatus('current')
ceqfpUtilInputTotalPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 6), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputTotalPktRate.setStatus('current')
ceqfpUtilInputTotalBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 7), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilInputTotalBitRate.setStatus('current')
ceqfpUtilOutputPriorityPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 8), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputPriorityPktRate.setStatus('current')
ceqfpUtilOutputPriorityBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 9), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputPriorityBitRate.setStatus('current')
ceqfpUtilOutputNonPriorityPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 10), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputNonPriorityPktRate.setStatus('current')
ceqfpUtilOutputNonPriorityBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 11), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputNonPriorityBitRate.setStatus('current')
ceqfpUtilOutputTotalPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 12), CiscoQfpPacketRate()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputTotalPktRate.setStatus('current')
ceqfpUtilOutputTotalBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 13), CiscoQfpBitRate()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilOutputTotalBitRate.setStatus('current')
ceqfpUtilProcessingLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpUtilProcessingLoad.setStatus('current')
ceqfpMemoryResourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7), )
if mibBuilder.loadTexts: ceqfpMemoryResourceTable.setStatus('current')
ceqfpMemoryResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResType"))
if mibBuilder.loadTexts: ceqfpMemoryResourceEntry.setStatus('current')
ceqfpMemoryResType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 1), CiscoQfpMemoryResource())
if mibBuilder.loadTexts: ceqfpMemoryResType.setStatus('current')
ceqfpMemoryResTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 2), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResTotal.setStatus('current')
ceqfpMemoryResInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 3), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResInUse.setStatus('current')
ceqfpMemoryResFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 4), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResFree.setStatus('current')
ceqfpMemoryResLowFreeWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 5), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResLowFreeWatermark.setStatus('current')
ceqfpMemoryResRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(90)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpMemoryResRisingThreshold.setStatus('current')
ceqfpMemoryResFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(85)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpMemoryResFallingThreshold.setStatus('current')
ceqfpMemoryResTotalOvrflw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 8), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResTotalOvrflw.setStatus('current')
ceqfpMemoryHCResTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 9), CounterBasedGauge64()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryHCResTotal.setStatus('current')
ceqfpMemoryResInUseOvrflw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 10), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResInUseOvrflw.setStatus('current')
ceqfpMemoryHCResInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 11), CounterBasedGauge64()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryHCResInUse.setStatus('current')
ceqfpMemoryResFreeOvrflw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 12), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResFreeOvrflw.setStatus('current')
ceqfpMemoryHCResFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 13), CounterBasedGauge64()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryHCResFree.setStatus('current')
ceqfpMemoryResLowFreeWatermarkOvrflw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 14), Gauge32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryResLowFreeWatermarkOvrflw.setStatus('current')
ceqfpMemoryHCResLowFreeWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 15), CounterBasedGauge64()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpMemoryHCResLowFreeWatermark.setStatus('current')
ceqfpThroughputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8), )
if mibBuilder.loadTexts: ceqfpThroughputTable.setStatus('current')
ceqfpThroughputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceqfpThroughputEntry.setStatus('current')
ceqfpThroughputLicensedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 1), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpThroughputLicensedBW.setStatus('current')
ceqfpThroughputLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("exceed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpThroughputLevel.setStatus('current')
ceqfpThroughputInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpThroughputInterval.setStatus('current')
ceqfpThroughputThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(75, 95))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpThroughputThreshold.setStatus('current')
ceqfpThroughputAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 5), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceqfpThroughputAvgRate.setStatus('current')
ceqfpMemoryResThreshNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpMemoryResThreshNotifEnabled.setStatus('current')
ceqfpMemoryResCurrentRisingThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ceqfpMemoryResCurrentRisingThresh.setStatus('current')
ceqfpMemoryResCurrentFallingThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 3), Unsigned32()).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ceqfpMemoryResCurrentFallingThresh.setStatus('current')
ceqfpThroughputNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceqfpThroughputNotifEnabled.setStatus('current')
ciscoEntityQfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1))
ceqfpMemoryResRisingThreshNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 1)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentRisingThresh"))
if mibBuilder.loadTexts: ceqfpMemoryResRisingThreshNotif.setStatus('current')
ceqfpMemoryResFallingThreshNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 2)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentFallingThresh"))
if mibBuilder.loadTexts: ceqfpMemoryResFallingThreshNotif.setStatus('current')
ceqfpThroughputNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 3)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLicensedBW"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLevel"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputAvgRate"))
if mibBuilder.loadTexts: ceqfpThroughputNotif.setStatus('current')
ciscoEntityQfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2))
ciscoEntityQfpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1, 1)).setObjects(("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpSystemGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpUtilizationGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpUtilizationAlgoGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryResourceGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryResNotifGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMIBComplianceRev1 = ciscoEntityQfpMIBComplianceRev1.setStatus('deprecated')
ciscoEntityQfpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1, 2)).setObjects(("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpSystemGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpUtilizationGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpUtilizationAlgoGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryResourceGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryResourceOvrflwGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryHCResourceGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpMemoryResNotifGroup"), ("CISCO-ENTITY-QFP-MIB", "ciscoEntityQfpNotifGroup"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMIBComplianceRev2 = ciscoEntityQfpMIBComplianceRev2.setStatus('current')
ciscoEntityQfpSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 1)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpSystemTrafficDirection"), ("CISCO-ENTITY-QFP-MIB", "ceqfpSystemState"), ("CISCO-ENTITY-QFP-MIB", "ceqfpNumberSystemLoads"), ("CISCO-ENTITY-QFP-MIB", "ceqfpSystemLastLoadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpSystemGroup = ciscoEntityQfpSystemGroup.setStatus('current')
ciscoEntityQfpUtilizationAlgoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 2)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpFiveSecondUtilAlgo"), ("CISCO-ENTITY-QFP-MIB", "ceqfpOneMinuteUtilAlgo"), ("CISCO-ENTITY-QFP-MIB", "ceqfpFiveMinutesUtilAlgo"), ("CISCO-ENTITY-QFP-MIB", "ceqfpSixtyMinutesUtilAlgo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpUtilizationAlgoGroup = ciscoEntityQfpUtilizationAlgoGroup.setStatus('current')
ciscoEntityQfpUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 3)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputPriorityPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputPriorityBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputNonPriorityPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputNonPriorityBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputTotalPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputTotalBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputPriorityPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputPriorityBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputNonPriorityPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputNonPriorityBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputTotalPktRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputTotalBitRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilProcessingLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpUtilizationGroup = ciscoEntityQfpUtilizationGroup.setStatus('current')
ciscoEntityQfpMemoryResourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 4)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResTotal"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFree"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResLowFreeWatermark"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResRisingThreshold"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFallingThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMemoryResourceGroup = ciscoEntityQfpMemoryResourceGroup.setStatus('current')
ciscoEntityQfpNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 5)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResRisingThreshNotif"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFallingThreshNotif"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpNotifGroup = ciscoEntityQfpNotifGroup.setStatus('current')
ciscoEntityQfpMemoryResNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 6)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResThreshNotifEnabled"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentRisingThresh"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentFallingThresh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMemoryResNotifGroup = ciscoEntityQfpMemoryResNotifGroup.setStatus('current')
ciscoEntityQfpMemoryResourceOvrflwGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 7)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResTotalOvrflw"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUseOvrflw"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFreeOvrflw"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResLowFreeWatermarkOvrflw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMemoryResourceOvrflwGroup = ciscoEntityQfpMemoryResourceOvrflwGroup.setStatus('current')
ciscoEntityQfpMemoryHCResourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 8)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResTotal"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResInUse"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResFree"), ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResLowFreeWatermark"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityQfpMemoryHCResourceGroup = ciscoEntityQfpMemoryHCResourceGroup.setStatus('current')
ceqfpThroughputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 9)).setObjects(("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLicensedBW"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLevel"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputInterval"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputThreshold"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputAvgRate"), ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceqfpThroughputGroup = ceqfpThroughputGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-QFP-MIB", ceqfpUtilInputPriorityPktRate=ceqfpUtilInputPriorityPktRate, ceqfpThroughputThreshold=ceqfpThroughputThreshold, ciscoEntityQfpMIBConform=ciscoEntityQfpMIBConform, ceqfpMemoryResCurrentRisingThresh=ceqfpMemoryResCurrentRisingThresh, ceqfpMemoryResCurrentFallingThresh=ceqfpMemoryResCurrentFallingThresh, ceqfpMemoryHCResLowFreeWatermark=ceqfpMemoryHCResLowFreeWatermark, ceqfpUtilInputNonPriorityPktRate=ceqfpUtilInputNonPriorityPktRate, ciscoEntityQfpMemoryResourceGroup=ciscoEntityQfpMemoryResourceGroup, ceqfpSystemState=ceqfpSystemState, ceqfpFiveSecondUtilAlgo=ceqfpFiveSecondUtilAlgo, ceqfpMemoryResLowFreeWatermarkOvrflw=ceqfpMemoryResLowFreeWatermarkOvrflw, ceqfpThroughputNotifEnabled=ceqfpThroughputNotifEnabled, ceqfpThroughputEntry=ceqfpThroughputEntry, ceqfpThroughputLevel=ceqfpThroughputLevel, ceqfpMemoryResourceTable=ceqfpMemoryResourceTable, ciscoEntityQfpUtilizationAlgoGroup=ciscoEntityQfpUtilizationAlgoGroup, ceqfpMemoryResTotalOvrflw=ceqfpMemoryResTotalOvrflw, ceqfpUtilInputPriorityBitRate=ceqfpUtilInputPriorityBitRate, ceqfpFiveMinutesUtilAlgo=ceqfpFiveMinutesUtilAlgo, ceqfpMemoryResFree=ceqfpMemoryResFree, ciscoEntityQfpMIBNotifs=ciscoEntityQfpMIBNotifs, ceqfpSystemTrafficDirection=ceqfpSystemTrafficDirection, CiscoQfpPacketRate=CiscoQfpPacketRate, ceqfpUtilOutputNonPriorityBitRate=ceqfpUtilOutputNonPriorityBitRate, ceqfpUtilInputTotalBitRate=ceqfpUtilInputTotalBitRate, ceqfpMemoryResFallingThreshNotif=ceqfpMemoryResFallingThreshNotif, CiscoQfpMemoryResource=CiscoQfpMemoryResource, ceqfpUtilOutputPriorityPktRate=ceqfpUtilOutputPriorityPktRate, ceqfpMemoryHCResFree=ceqfpMemoryHCResFree, ceqfpMemoryResRisingThreshold=ceqfpMemoryResRisingThreshold, ciscoEntityQfpMemoryHCResourceGroup=ciscoEntityQfpMemoryHCResourceGroup, ceqfpUtilProcessingLoad=ceqfpUtilProcessingLoad, ceqfpThroughputInterval=ceqfpThroughputInterval, ceqfpThroughputNotif=ceqfpThroughputNotif, CiscoQfpTimeInterval=CiscoQfpTimeInterval, ceqfpUtilTimeInterval=ceqfpUtilTimeInterval, ciscoEntityQfpMIBCompliances=ciscoEntityQfpMIBCompliances, ceqfpUtilOutputTotalBitRate=ceqfpUtilOutputTotalBitRate, ceqfpMemoryResRisingThreshNotif=ceqfpMemoryResRisingThreshNotif, ceqfpUtilizationEntry=ceqfpUtilizationEntry, ceqfpNumberSystemLoads=ceqfpNumberSystemLoads, ceqfpMemoryResInUse=ceqfpMemoryResInUse, ceqfpMemoryResTotal=ceqfpMemoryResTotal, ceqfpThroughputTable=ceqfpThroughputTable, ciscoEntityQfpSystemGroup=ciscoEntityQfpSystemGroup, ceqfpMemoryResFallingThreshold=ceqfpMemoryResFallingThreshold, ceqfpSystemEntry=ceqfpSystemEntry, ceqfpThroughputLicensedBW=ceqfpThroughputLicensedBW, ceqfpSystemTable=ceqfpSystemTable, ceqfpMemoryResThreshNotifEnabled=ceqfpMemoryResThreshNotifEnabled, ceqfpSystemLastLoadTime=ceqfpSystemLastLoadTime, ceqfpMemoryResLowFreeWatermark=ceqfpMemoryResLowFreeWatermark, ceqfpOneMinuteUtilAlgo=ceqfpOneMinuteUtilAlgo, ceqfpThroughputGroup=ceqfpThroughputGroup, PYSNMP_MODULE_ID=ciscoEntityQfpMIB, ciscoEntityQfpMIB=ciscoEntityQfpMIB, ceqfpMemoryHCResTotal=ceqfpMemoryHCResTotal, CiscoQfpBitRate=CiscoQfpBitRate, ceqfpMemoryResourceEntry=ceqfpMemoryResourceEntry, ciscoEntityQfpMIBObjects=ciscoEntityQfpMIBObjects, ciscoEntityQfp=ciscoEntityQfp, ceqfpThroughputAvgRate=ceqfpThroughputAvgRate, ceqfpUtilInputNonPriorityBitRate=ceqfpUtilInputNonPriorityBitRate, ciscoEntityQfpMIBGroups=ciscoEntityQfpMIBGroups, ceqfpSixtyMinutesUtilAlgo=ceqfpSixtyMinutesUtilAlgo, ciscoEntityQfpMemoryResourceOvrflwGroup=ciscoEntityQfpMemoryResourceOvrflwGroup, ciscoEntityQfpMIBComplianceRev2=ciscoEntityQfpMIBComplianceRev2, ceqfpMemoryResInUseOvrflw=ceqfpMemoryResInUseOvrflw, ceqfpUtilInputTotalPktRate=ceqfpUtilInputTotalPktRate, ceqfpUtilOutputPriorityBitRate=ceqfpUtilOutputPriorityBitRate, ceqfpUtilOutputNonPriorityPktRate=ceqfpUtilOutputNonPriorityPktRate, ceqfpUtilOutputTotalPktRate=ceqfpUtilOutputTotalPktRate, ciscoEntityQfpNotif=ciscoEntityQfpNotif, ciscoEntityQfpUtilizationGroup=ciscoEntityQfpUtilizationGroup, ceqfpMemoryResFreeOvrflw=ceqfpMemoryResFreeOvrflw, ciscoEntityQfpMIBComplianceRev1=ciscoEntityQfpMIBComplianceRev1, ciscoEntityQfpNotifGroup=ciscoEntityQfpNotifGroup, ceqfpUtilizationTable=ceqfpUtilizationTable, ceqfpMemoryResType=ceqfpMemoryResType, ciscoEntityQfpMemoryResNotifGroup=ciscoEntityQfpMemoryResNotifGroup, ceqfpMemoryHCResInUse=ceqfpMemoryHCResInUse)

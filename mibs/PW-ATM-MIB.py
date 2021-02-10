#
# PySNMP MIB module PW-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
pwIndex, = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex")
PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Bits, Gauge32, mib_2, Counter32, MibIdentifier, Unsigned32, NotificationType, iso, TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Gauge32", "mib-2", "Counter32", "MibIdentifier", "Unsigned32", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, RowPointer, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "RowPointer", "TextualConvention", "TruthValue")
pwAtmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 183))
pwAtmMIB.setRevisions(('2009-06-16 00:00',))
if mibBuilder.loadTexts: pwAtmMIB.setLastUpdated('200906160000Z')
if mibBuilder.loadTexts: pwAtmMIB.setOrganization('Pseudowire Emulation Edge-to-Edge (PWE3) Working Group')
pwAtmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 183, 0))
pwAtmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 183, 1))
pwAtmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 183, 2))
pwAtmOutboundTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 1), )
if mibBuilder.loadTexts: pwAtmOutboundTable.setStatus('current')
pwAtmOutboundEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 1, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwAtmOutboundEntry.setStatus('current')
pwAtmOutboundAtmIf = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundAtmIf.setStatus('current')
pwAtmOutboundVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 2), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundVpi.setStatus('current')
pwAtmOutboundVci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 3), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundVci.setStatus('current')
pwAtmOutboundTrafficParamDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 4), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundTrafficParamDescr.setStatus('current')
pwAtmOutboundRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundRowStatus.setStatus('current')
pwAtmInboundTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 3), )
if mibBuilder.loadTexts: pwAtmInboundTable.setStatus('current')
pwAtmInboundEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 3, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwAtmInboundEntry.setStatus('current')
pwAtmInboundAtmIf = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundAtmIf.setStatus('current')
pwAtmInboundVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 2), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundVpi.setStatus('current')
pwAtmInboundVci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 3), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundVci.setStatus('current')
pwAtmInboundTrafficParamDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 4), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundTrafficParamDescr.setStatus('current')
pwAtmInboundRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundRowStatus.setStatus('current')
pwAtmCfgTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 5), )
if mibBuilder.loadTexts: pwAtmCfgTable.setStatus('current')
pwAtmCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 5, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwAtmCfgEntry.setStatus('current')
pwAtmCfgMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAtmCfgMaxCellConcatenation.setStatus('current')
pwAtmCfgFarEndMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAtmCfgFarEndMaxCellConcatenation.setStatus('current')
pwAtmCfgTimeoutMode = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAtmCfgTimeoutMode.setStatus('current')
pwAtmClpQosMapping = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAtmClpQosMapping.setStatus('current')
pwAtmOutboundNto1Table = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 6), )
if mibBuilder.loadTexts: pwAtmOutboundNto1Table.setStatus('current')
pwAtmOutboundNto1Entry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 6, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-ATM-MIB", "pwAtmOutboundNto1AtmIf"), (0, "PW-ATM-MIB", "pwAtmOutboundNto1Vpi"), (0, "PW-ATM-MIB", "pwAtmOutboundNto1Vci"))
if mibBuilder.loadTexts: pwAtmOutboundNto1Entry.setStatus('current')
pwAtmOutboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pwAtmOutboundNto1AtmIf.setStatus('current')
pwAtmOutboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: pwAtmOutboundNto1Vpi.setStatus('current')
pwAtmOutboundNto1Vci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: pwAtmOutboundNto1Vci.setStatus('current')
pwAtmOutboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundNto1RowStatus.setStatus('current')
pwAtmOutboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 5), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundNto1TrafficParamDescr.setStatus('current')
pwAtmOutboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 6), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundNto1MappedVpi.setStatus('current')
pwAtmOutboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 7), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmOutboundNto1MappedVci.setStatus('current')
pwAtmInboundNto1Table = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 7), )
if mibBuilder.loadTexts: pwAtmInboundNto1Table.setStatus('current')
pwAtmInboundNto1Entry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 7, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-ATM-MIB", "pwAtmInboundNto1AtmIf"), (0, "PW-ATM-MIB", "pwAtmInboundNto1Vpi"), (0, "PW-ATM-MIB", "pwAtmInboundNto1Vci"))
if mibBuilder.loadTexts: pwAtmInboundNto1Entry.setStatus('current')
pwAtmInboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pwAtmInboundNto1AtmIf.setStatus('current')
pwAtmInboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: pwAtmInboundNto1Vpi.setStatus('current')
pwAtmInboundNto1Vci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: pwAtmInboundNto1Vci.setStatus('current')
pwAtmInboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundNto1RowStatus.setStatus('current')
pwAtmInboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 5), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundNto1TrafficParamDescr.setStatus('current')
pwAtmInboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 6), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundNto1MappedVpi.setStatus('current')
pwAtmInboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 7), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAtmInboundNto1MappedVci.setStatus('current')
pwAtmPerfCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 8), )
if mibBuilder.loadTexts: pwAtmPerfCurrentTable.setStatus('current')
pwAtmPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 8, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwAtmPerfCurrentEntry.setStatus('current')
pwAtmPerfCurrentMissingPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentMissingPkts.setStatus('current')
pwAtmPerfCurrentPktsReOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentPktsReOrder.setStatus('current')
pwAtmPerfCurrentPktsMisOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentPktsMisOrder.setStatus('current')
pwAtmPerfCurrentPktsTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentPktsTimeout.setStatus('current')
pwAtmPerfCurrentCellsXmit = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentCellsXmit.setStatus('current')
pwAtmPerfCurrentCellsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentCellsDropped.setStatus('current')
pwAtmPerfCurrentCellsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentCellsReceived.setStatus('current')
pwAtmPerfCurrentUnknownCells = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfCurrentUnknownCells.setStatus('current')
pwAtmPerfIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 9), )
if mibBuilder.loadTexts: pwAtmPerfIntervalTable.setStatus('current')
pwAtmPerfIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 9, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-ATM-MIB", "pwAtmPerfIntervalNumber"))
if mibBuilder.loadTexts: pwAtmPerfIntervalEntry.setStatus('current')
pwAtmPerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: pwAtmPerfIntervalNumber.setStatus('current')
pwAtmPerfIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalValidData.setStatus('current')
pwAtmPerfIntervalDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalDuration.setStatus('current')
pwAtmPerfIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalMissingPkts.setStatus('current')
pwAtmPerfIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalPktsReOrder.setStatus('current')
pwAtmPerfIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalPktsMisOrder.setStatus('current')
pwAtmPerfIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalPktsTimeout.setStatus('current')
pwAtmPerfIntervalCellsXmit = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalCellsXmit.setStatus('current')
pwAtmPerfIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalCellsDropped.setStatus('current')
pwAtmPerfIntervalCellsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 10), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalCellsReceived.setStatus('current')
pwAtmPerfIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 11), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerfIntervalUnknownCells.setStatus('current')
pwAtmPerf1DayIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 183, 1, 10), )
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalTable.setStatus('current')
pwAtmPerf1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 183, 1, 10, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-ATM-MIB", "pwAtmPerf1DayIntervalNumber"))
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalEntry.setStatus('current')
pwAtmPerf1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 365)))
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalNumber.setStatus('current')
pwAtmPerf1DayIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalValidData.setStatus('current')
pwAtmPerf1DayIntervalDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalDuration.setStatus('current')
pwAtmPerf1DayIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalMissingPkts.setStatus('current')
pwAtmPerf1DayIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalPktsReOrder.setStatus('current')
pwAtmPerf1DayIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalPktsMisOrder.setStatus('current')
pwAtmPerf1DayIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalPktsTimeout.setStatus('current')
pwAtmPerf1DayIntervalCellsXmit = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalCellsXmit.setStatus('current')
pwAtmPerf1DayIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalCellsDropped.setStatus('current')
pwAtmPerf1DayIntervalCellsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalCellsReceived.setStatus('current')
pwAtmPerf1DayIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAtmPerf1DayIntervalUnknownCells.setStatus('current')
pwAtmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 183, 2, 1))
pwAtmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 183, 2, 2))
pwAtmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 183, 2, 1, 2)).setObjects(("PW-ATM-MIB", "pwAtmCfgGroup"), ("PW-ATM-MIB", "pwAtmPerfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmCompliance = pwAtmCompliance.setStatus('current')
pwAtmCfgGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 5)).setObjects(("PW-ATM-MIB", "pwAtmCfgMaxCellConcatenation"), ("PW-ATM-MIB", "pwAtmCfgFarEndMaxCellConcatenation"), ("PW-ATM-MIB", "pwAtmCfgTimeoutMode"), ("PW-ATM-MIB", "pwAtmClpQosMapping"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmCfgGroup = pwAtmCfgGroup.setStatus('current')
pwAtmPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 6)).setObjects(("PW-ATM-MIB", "pwAtmPerfCurrentMissingPkts"), ("PW-ATM-MIB", "pwAtmPerfCurrentPktsReOrder"), ("PW-ATM-MIB", "pwAtmPerfCurrentPktsMisOrder"), ("PW-ATM-MIB", "pwAtmPerfCurrentPktsTimeout"), ("PW-ATM-MIB", "pwAtmPerfCurrentCellsXmit"), ("PW-ATM-MIB", "pwAtmPerfCurrentCellsDropped"), ("PW-ATM-MIB", "pwAtmPerfCurrentCellsReceived"), ("PW-ATM-MIB", "pwAtmPerfCurrentUnknownCells"), ("PW-ATM-MIB", "pwAtmPerfIntervalValidData"), ("PW-ATM-MIB", "pwAtmPerfIntervalDuration"), ("PW-ATM-MIB", "pwAtmPerfIntervalMissingPkts"), ("PW-ATM-MIB", "pwAtmPerfIntervalPktsReOrder"), ("PW-ATM-MIB", "pwAtmPerfIntervalPktsMisOrder"), ("PW-ATM-MIB", "pwAtmPerfIntervalPktsTimeout"), ("PW-ATM-MIB", "pwAtmPerfIntervalCellsXmit"), ("PW-ATM-MIB", "pwAtmPerfIntervalCellsDropped"), ("PW-ATM-MIB", "pwAtmPerfIntervalCellsReceived"), ("PW-ATM-MIB", "pwAtmPerfIntervalUnknownCells"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalValidData"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalDuration"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalMissingPkts"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsReOrder"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsMisOrder"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsTimeout"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsXmit"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsDropped"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsReceived"), ("PW-ATM-MIB", "pwAtmPerf1DayIntervalUnknownCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmPerfGroup = pwAtmPerfGroup.setStatus('current')
pwAtmOutbound1to1Group = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 7)).setObjects(("PW-ATM-MIB", "pwAtmOutboundAtmIf"), ("PW-ATM-MIB", "pwAtmOutboundVpi"), ("PW-ATM-MIB", "pwAtmOutboundVci"), ("PW-ATM-MIB", "pwAtmOutboundTrafficParamDescr"), ("PW-ATM-MIB", "pwAtmOutboundRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmOutbound1to1Group = pwAtmOutbound1to1Group.setStatus('current')
pwAtmInbound1to1Group = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 8)).setObjects(("PW-ATM-MIB", "pwAtmInboundAtmIf"), ("PW-ATM-MIB", "pwAtmInboundVpi"), ("PW-ATM-MIB", "pwAtmInboundVci"), ("PW-ATM-MIB", "pwAtmInboundTrafficParamDescr"), ("PW-ATM-MIB", "pwAtmInboundRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmInbound1to1Group = pwAtmInbound1to1Group.setStatus('current')
pwAtmOutboundNto1Group = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 9)).setObjects(("PW-ATM-MIB", "pwAtmOutboundNto1RowStatus"), ("PW-ATM-MIB", "pwAtmOutboundNto1TrafficParamDescr"), ("PW-ATM-MIB", "pwAtmOutboundNto1MappedVpi"), ("PW-ATM-MIB", "pwAtmOutboundNto1MappedVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmOutboundNto1Group = pwAtmOutboundNto1Group.setStatus('current')
pwAtmInboundNto1Group = ObjectGroup((1, 3, 6, 1, 2, 1, 183, 2, 2, 10)).setObjects(("PW-ATM-MIB", "pwAtmInboundNto1RowStatus"), ("PW-ATM-MIB", "pwAtmInboundNto1TrafficParamDescr"), ("PW-ATM-MIB", "pwAtmInboundNto1MappedVpi"), ("PW-ATM-MIB", "pwAtmInboundNto1MappedVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAtmInboundNto1Group = pwAtmInboundNto1Group.setStatus('current')
mibBuilder.exportSymbols("PW-ATM-MIB", pwAtmGroups=pwAtmGroups, pwAtmPerfIntervalMissingPkts=pwAtmPerfIntervalMissingPkts, pwAtmCfgFarEndMaxCellConcatenation=pwAtmCfgFarEndMaxCellConcatenation, pwAtmPerfIntervalValidData=pwAtmPerfIntervalValidData, pwAtmOutboundNto1Vpi=pwAtmOutboundNto1Vpi, pwAtmOutboundVci=pwAtmOutboundVci, PYSNMP_MODULE_ID=pwAtmMIB, pwAtmCompliance=pwAtmCompliance, pwAtmPerf1DayIntervalMissingPkts=pwAtmPerf1DayIntervalMissingPkts, pwAtmOutboundNto1RowStatus=pwAtmOutboundNto1RowStatus, pwAtmInboundNto1RowStatus=pwAtmInboundNto1RowStatus, pwAtmCfgGroup=pwAtmCfgGroup, pwAtmPerfIntervalPktsMisOrder=pwAtmPerfIntervalPktsMisOrder, pwAtmPerfIntervalCellsReceived=pwAtmPerfIntervalCellsReceived, pwAtmOutboundNto1AtmIf=pwAtmOutboundNto1AtmIf, pwAtmInbound1to1Group=pwAtmInbound1to1Group, pwAtmOutboundNto1MappedVpi=pwAtmOutboundNto1MappedVpi, pwAtmCfgEntry=pwAtmCfgEntry, pwAtmPerfCurrentPktsTimeout=pwAtmPerfCurrentPktsTimeout, pwAtmPerf1DayIntervalUnknownCells=pwAtmPerf1DayIntervalUnknownCells, pwAtmOutboundNto1Vci=pwAtmOutboundNto1Vci, pwAtmOutboundTable=pwAtmOutboundTable, pwAtmInboundNto1MappedVpi=pwAtmInboundNto1MappedVpi, pwAtmConformance=pwAtmConformance, pwAtmPerf1DayIntervalCellsReceived=pwAtmPerf1DayIntervalCellsReceived, pwAtmInboundNto1MappedVci=pwAtmInboundNto1MappedVci, pwAtmPerfIntervalEntry=pwAtmPerfIntervalEntry, pwAtmOutboundNto1Entry=pwAtmOutboundNto1Entry, pwAtmOutboundNto1TrafficParamDescr=pwAtmOutboundNto1TrafficParamDescr, pwAtmOutboundNto1Group=pwAtmOutboundNto1Group, pwAtmCfgTimeoutMode=pwAtmCfgTimeoutMode, pwAtmPerf1DayIntervalEntry=pwAtmPerf1DayIntervalEntry, pwAtmPerfCurrentCellsXmit=pwAtmPerfCurrentCellsXmit, pwAtmOutboundEntry=pwAtmOutboundEntry, pwAtmInboundVpi=pwAtmInboundVpi, pwAtmPerf1DayIntervalPktsTimeout=pwAtmPerf1DayIntervalPktsTimeout, pwAtmCfgMaxCellConcatenation=pwAtmCfgMaxCellConcatenation, pwAtmPerfCurrentCellsDropped=pwAtmPerfCurrentCellsDropped, pwAtmPerfCurrentTable=pwAtmPerfCurrentTable, pwAtmPerfCurrentUnknownCells=pwAtmPerfCurrentUnknownCells, pwAtmInboundNto1AtmIf=pwAtmInboundNto1AtmIf, pwAtmPerfIntervalPktsReOrder=pwAtmPerfIntervalPktsReOrder, pwAtmInboundTrafficParamDescr=pwAtmInboundTrafficParamDescr, pwAtmOutboundNto1MappedVci=pwAtmOutboundNto1MappedVci, pwAtmInboundAtmIf=pwAtmInboundAtmIf, pwAtmPerfIntervalCellsXmit=pwAtmPerfIntervalCellsXmit, pwAtmInboundVci=pwAtmInboundVci, pwAtmInboundRowStatus=pwAtmInboundRowStatus, pwAtmPerf1DayIntervalCellsXmit=pwAtmPerf1DayIntervalCellsXmit, pwAtmOutboundRowStatus=pwAtmOutboundRowStatus, pwAtmNotifications=pwAtmNotifications, pwAtmInboundTable=pwAtmInboundTable, pwAtmOutboundNto1Table=pwAtmOutboundNto1Table, pwAtmPerfIntervalDuration=pwAtmPerfIntervalDuration, pwAtmPerfCurrentMissingPkts=pwAtmPerfCurrentMissingPkts, pwAtmInboundNto1Group=pwAtmInboundNto1Group, pwAtmClpQosMapping=pwAtmClpQosMapping, pwAtmPerfIntervalNumber=pwAtmPerfIntervalNumber, pwAtmCompliances=pwAtmCompliances, pwAtmPerf1DayIntervalDuration=pwAtmPerf1DayIntervalDuration, pwAtmOutboundVpi=pwAtmOutboundVpi, pwAtmPerf1DayIntervalPktsMisOrder=pwAtmPerf1DayIntervalPktsMisOrder, pwAtmPerfIntervalCellsDropped=pwAtmPerfIntervalCellsDropped, pwAtmPerfGroup=pwAtmPerfGroup, pwAtmInboundNto1Table=pwAtmInboundNto1Table, pwAtmPerfCurrentCellsReceived=pwAtmPerfCurrentCellsReceived, pwAtmInboundEntry=pwAtmInboundEntry, pwAtmPerfIntervalUnknownCells=pwAtmPerfIntervalUnknownCells, pwAtmPerf1DayIntervalCellsDropped=pwAtmPerf1DayIntervalCellsDropped, pwAtmOutboundTrafficParamDescr=pwAtmOutboundTrafficParamDescr, pwAtmPerf1DayIntervalNumber=pwAtmPerf1DayIntervalNumber, pwAtmPerfCurrentPktsReOrder=pwAtmPerfCurrentPktsReOrder, pwAtmPerf1DayIntervalValidData=pwAtmPerf1DayIntervalValidData, pwAtmPerf1DayIntervalTable=pwAtmPerf1DayIntervalTable, pwAtmInboundNto1TrafficParamDescr=pwAtmInboundNto1TrafficParamDescr, pwAtmCfgTable=pwAtmCfgTable, pwAtmPerfIntervalTable=pwAtmPerfIntervalTable, pwAtmMIB=pwAtmMIB, pwAtmInboundNto1Entry=pwAtmInboundNto1Entry, pwAtmInboundNto1Vci=pwAtmInboundNto1Vci, pwAtmPerf1DayIntervalPktsReOrder=pwAtmPerf1DayIntervalPktsReOrder, pwAtmOutboundAtmIf=pwAtmOutboundAtmIf, pwAtmObjects=pwAtmObjects, pwAtmPerfIntervalPktsTimeout=pwAtmPerfIntervalPktsTimeout, pwAtmOutbound1to1Group=pwAtmOutbound1to1Group, pwAtmPerfCurrentEntry=pwAtmPerfCurrentEntry, pwAtmPerfCurrentPktsMisOrder=pwAtmPerfCurrentPktsMisOrder, pwAtmInboundNto1Vpi=pwAtmInboundNto1Vpi)

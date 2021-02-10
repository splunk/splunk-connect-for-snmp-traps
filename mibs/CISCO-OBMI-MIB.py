#
# PySNMP MIB module CISCO-OBMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OBMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Gauge32, Counter32, ModuleIdentity, Unsigned32, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Gauge32", "Counter32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Integer32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoObmiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 698))
ciscoObmiMIB.setRevisions(('2009-05-28 00:00',))
if mibBuilder.loadTexts: ciscoObmiMIB.setLastUpdated('200905280000Z')
if mibBuilder.loadTexts: ciscoObmiMIB.setOrganization('Cisco Systems, Inc.')
ciscoObmiMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 0))
ciscoObmiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 1))
ciscoObmiMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2))
cObmiTransportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2), )
if mibBuilder.loadTexts: cObmiTransportTable.setStatus('current')
cObmiTransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiTransportEntry.setStatus('current')
cObmiBusID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: cObmiBusID.setStatus('current')
cObmiBusName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiBusName.setStatus('current')
cObmiCommandRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 3), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandRx.setStatus('current')
cObmiCommandProcessedTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 4), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandProcessedTotal.setStatus('current')
cObmiCommandGets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 5), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandGets.setStatus('current')
cObmiCommandSets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 6), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandSets.setStatus('current')
cObmiCommandProcessedInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 7), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandProcessedInvalid.setStatus('current')
cObmiCommandPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 8), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandPending.setStatus('current')
cObmiCommandDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 9), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandDropped.setStatus('current')
cObmiTelemetrySent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 10), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetrySent.setStatus('current')
cObmiTelemetryDemandSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 11), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetryDemandSent.setStatus('current')
cObmiTelemetryPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 12), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetryPending.setStatus('current')
cObmiTransportHeartBeatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3), )
if mibBuilder.loadTexts: cObmiTransportHeartBeatTable.setStatus('current')
cObmiTransportHeartBeatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"), (0, "CISCO-OBMI-MIB", "cObmiHeartBeatPort"))
if mibBuilder.loadTexts: cObmiTransportHeartBeatEntry.setStatus('current')
cObmiHeartBeatPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: cObmiHeartBeatPort.setStatus('current')
cObmiHeartBeatSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 2), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiHeartBeatSent.setStatus('current')
cObmiHeartBeatPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 3), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiHeartBeatPending.setStatus('current')
cObmiM500FramingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4), )
if mibBuilder.loadTexts: cObmiM500FramingTable.setStatus('current')
cObmiM500FramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiM500FramingEntry.setStatus('current')
cObmiM500RxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 1), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxFrames.setStatus('current')
cObmiM500RxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 2), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxBytes.setStatus('current')
cObmiM500RxAbortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 3), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxAbortFrames.setStatus('current')
cObmiM500RxEchoFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 4), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxEchoFrames.setStatus('current')
cObmiM500RxResetFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 5), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxResetFrames.setStatus('current')
cObmiM500RxTransportErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 6), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxTransportErrFrames.setStatus('current')
cObmiM500RxUnknownOpFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 7), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxUnknownOpFrames.setStatus('current')
cObmiM500TxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 8), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxFrames.setStatus('current')
cObmiM500TxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 9), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxBytes.setStatus('current')
cObmiM500TxAbortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 10), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxAbortFrames.setStatus('current')
cObmiM500TxEchoFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 11), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxEchoFrames.setStatus('current')
cObmiM500TxTransportErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 12), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxTransportErrFrames.setStatus('current')
cObmiM500RxQOverRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 13), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxQOverRun.setStatus('current')
cObmiM500TxQ0UnderRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 14), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxQ0UnderRun.setStatus('current')
cObmiM500TxQ1UnderRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 15), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxQ1UnderRun.setStatus('current')
cObmiM500TxCtlQOverRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 16), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxCtlQOverRun.setStatus('current')
cObmiM500PhyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5), )
if mibBuilder.loadTexts: cObmiM500PhyTable.setStatus('current')
cObmiM500PhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiM500PhyEntry.setStatus('current')
cObmiM500BusALOS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500BusALOS.setStatus('current')
cObmiM500BusBLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500BusBLOS.setStatus('current')
cObmiM500LastActiveBus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 3), Bits().clone(namedValues=NamedValues(("a", 0), ("b", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500LastActiveBus.setStatus('current')
cObmiM500CommandsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 4), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandsRcvd.setStatus('current')
cObmiM500TelemetrySent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 5), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetrySent.setStatus('current')
cObmiM500TelemetryErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 6), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetryErrs.setStatus('current')
cObmiM500CommandErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 7), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandErrs.setStatus('current')
cObmiM500CommandOverWrts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 8), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandOverWrts.setStatus('current')
cObmiM500HWParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500HWParityErr.setStatus('current')
cObmiM500TelemetryReqParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetryReqParityErr.setStatus('current')
cObmiM500CommandParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandParityErr.setStatus('current')
cObmiM500CommandTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandTimeout.setStatus('current')
cObmiM500CommandOverWrt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandOverWrt.setStatus('current')
ciscoObmiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1))
ciscoObmiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2))
ciscoObmiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1, 1)).setObjects(("CISCO-OBMI-MIB", "ciscoObmiMIBMainObjectGroup"), ("CISCO-OBMI-MIB", "ciscoObmiMIBM500ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBCompliance = ciscoObmiMIBCompliance.setStatus('current')
ciscoObmiMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 1)).setObjects(("CISCO-OBMI-MIB", "cObmiBusName"), ("CISCO-OBMI-MIB", "cObmiCommandRx"), ("CISCO-OBMI-MIB", "cObmiCommandProcessedTotal"), ("CISCO-OBMI-MIB", "cObmiCommandGets"), ("CISCO-OBMI-MIB", "cObmiCommandSets"), ("CISCO-OBMI-MIB", "cObmiCommandProcessedInvalid"), ("CISCO-OBMI-MIB", "cObmiCommandPending"), ("CISCO-OBMI-MIB", "cObmiCommandDropped"), ("CISCO-OBMI-MIB", "cObmiTelemetrySent"), ("CISCO-OBMI-MIB", "cObmiTelemetryDemandSent"), ("CISCO-OBMI-MIB", "cObmiTelemetryPending"), ("CISCO-OBMI-MIB", "cObmiHeartBeatSent"), ("CISCO-OBMI-MIB", "cObmiHeartBeatPending"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBMainObjectGroup = ciscoObmiMIBMainObjectGroup.setStatus('current')
ciscoObmiMIBM500ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 2)).setObjects(("CISCO-OBMI-MIB", "cObmiM500RxFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxBytes"), ("CISCO-OBMI-MIB", "cObmiM500RxAbortFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxEchoFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxResetFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxTransportErrFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxUnknownOpFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxBytes"), ("CISCO-OBMI-MIB", "cObmiM500TxAbortFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxEchoFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxTransportErrFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxQOverRun"), ("CISCO-OBMI-MIB", "cObmiM500TxQ0UnderRun"), ("CISCO-OBMI-MIB", "cObmiM500TxQ1UnderRun"), ("CISCO-OBMI-MIB", "cObmiM500TxCtlQOverRun"), ("CISCO-OBMI-MIB", "cObmiM500BusALOS"), ("CISCO-OBMI-MIB", "cObmiM500BusBLOS"), ("CISCO-OBMI-MIB", "cObmiM500LastActiveBus"), ("CISCO-OBMI-MIB", "cObmiM500CommandsRcvd"), ("CISCO-OBMI-MIB", "cObmiM500TelemetrySent"), ("CISCO-OBMI-MIB", "cObmiM500TelemetryErrs"), ("CISCO-OBMI-MIB", "cObmiM500CommandErrs"), ("CISCO-OBMI-MIB", "cObmiM500HWParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrts"), ("CISCO-OBMI-MIB", "cObmiM500TelemetryReqParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandTimeout"), ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBM500ObjectGroup = ciscoObmiMIBM500ObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OBMI-MIB", cObmiTelemetryDemandSent=cObmiTelemetryDemandSent, cObmiM500RxAbortFrames=cObmiM500RxAbortFrames, cObmiCommandProcessedTotal=cObmiCommandProcessedTotal, cObmiBusName=cObmiBusName, cObmiM500BusALOS=cObmiM500BusALOS, cObmiM500CommandsRcvd=cObmiM500CommandsRcvd, ciscoObmiMIBCompliances=ciscoObmiMIBCompliances, cObmiM500FramingTable=cObmiM500FramingTable, cObmiM500TxBytes=cObmiM500TxBytes, ciscoObmiMIBM500ObjectGroup=ciscoObmiMIBM500ObjectGroup, cObmiM500RxBytes=cObmiM500RxBytes, cObmiM500TxQ1UnderRun=cObmiM500TxQ1UnderRun, ciscoObmiMIBObjects=ciscoObmiMIBObjects, cObmiTransportHeartBeatEntry=cObmiTransportHeartBeatEntry, cObmiTelemetryPending=cObmiTelemetryPending, cObmiM500PhyEntry=cObmiM500PhyEntry, cObmiM500TelemetrySent=cObmiM500TelemetrySent, cObmiM500CommandErrs=cObmiM500CommandErrs, ciscoObmiMIB=ciscoObmiMIB, ciscoObmiMIBGroups=ciscoObmiMIBGroups, cObmiHeartBeatSent=cObmiHeartBeatSent, ciscoObmiMIBNotifs=ciscoObmiMIBNotifs, cObmiTelemetrySent=cObmiTelemetrySent, cObmiM500TxQ0UnderRun=cObmiM500TxQ0UnderRun, cObmiM500PhyTable=cObmiM500PhyTable, cObmiM500TxCtlQOverRun=cObmiM500TxCtlQOverRun, cObmiM500TxAbortFrames=cObmiM500TxAbortFrames, cObmiBusID=cObmiBusID, cObmiTransportEntry=cObmiTransportEntry, ciscoObmiMIBCompliance=ciscoObmiMIBCompliance, cObmiCommandProcessedInvalid=cObmiCommandProcessedInvalid, cObmiCommandGets=cObmiCommandGets, cObmiHeartBeatPort=cObmiHeartBeatPort, cObmiM500HWParityErr=cObmiM500HWParityErr, cObmiM500FramingEntry=cObmiM500FramingEntry, cObmiM500CommandOverWrt=cObmiM500CommandOverWrt, cObmiM500RxFrames=cObmiM500RxFrames, cObmiM500BusBLOS=cObmiM500BusBLOS, cObmiHeartBeatPending=cObmiHeartBeatPending, cObmiM500RxResetFrames=cObmiM500RxResetFrames, PYSNMP_MODULE_ID=ciscoObmiMIB, cObmiM500TxEchoFrames=cObmiM500TxEchoFrames, cObmiM500RxEchoFrames=cObmiM500RxEchoFrames, cObmiTransportHeartBeatTable=cObmiTransportHeartBeatTable, cObmiM500RxTransportErrFrames=cObmiM500RxTransportErrFrames, cObmiM500RxQOverRun=cObmiM500RxQOverRun, cObmiM500CommandOverWrts=cObmiM500CommandOverWrts, cObmiM500TxFrames=cObmiM500TxFrames, cObmiM500CommandTimeout=cObmiM500CommandTimeout, cObmiTransportTable=cObmiTransportTable, cObmiCommandSets=cObmiCommandSets, cObmiM500TxTransportErrFrames=cObmiM500TxTransportErrFrames, cObmiM500LastActiveBus=cObmiM500LastActiveBus, ciscoObmiMIBConform=ciscoObmiMIBConform, cObmiM500CommandParityErr=cObmiM500CommandParityErr, ciscoObmiMIBMainObjectGroup=ciscoObmiMIBMainObjectGroup, cObmiM500TelemetryErrs=cObmiM500TelemetryErrs, cObmiM500RxUnknownOpFrames=cObmiM500RxUnknownOpFrames, cObmiCommandPending=cObmiCommandPending, cObmiM500TelemetryReqParityErr=cObmiM500TelemetryReqParityErr, cObmiCommandRx=cObmiCommandRx, cObmiCommandDropped=cObmiCommandDropped)

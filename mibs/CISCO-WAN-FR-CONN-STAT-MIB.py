#
# PySNMP MIB module CISCO-WAN-FR-CONN-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-FR-CONN-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
frChan, = mibBuilder.importSymbols("BASIS-MIB", "frChan")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, iso, IpAddress, Counter64, Bits, TimeTicks, Gauge32, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "IpAddress", "Counter64", "Bits", "TimeTicks", "Gauge32", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanFrConnStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 48))
ciscoWanFrConnStatMIB.setRevisions(('2002-10-18 00:00',))
if mibBuilder.loadTexts: ciscoWanFrConnStatMIB.setLastUpdated('200210180000Z')
if mibBuilder.loadTexts: ciscoWanFrConnStatMIB.setOrganization('Cisco Systems, Inc.')
frChanCntGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3))
frChanCntGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1), )
if mibBuilder.loadTexts: frChanCntGrpTable.setStatus('current')
frChanCntGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1), ).setIndexNames((0, "CISCO-WAN-FR-CONN-STAT-MIB", "cntChanNum"))
if mibBuilder.loadTexts: frChanCntGrpEntry.setStatus('current')
cntChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntChanNum.setStatus('current')
rcvFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 2), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFrames.setStatus('current')
rcvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 3), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytes.setStatus('current')
rcvFramesDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 4), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDE.setStatus('current')
rcvBytesDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 5), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytesDE.setStatus('current')
rcvFramesDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 6), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDiscard.setStatus('current')
rcvBytesDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 7), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytesDiscard.setStatus('current')
rcvFramesDiscShelfAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 8), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDiscShelfAlarm.setStatus('current')
rcvFramesDiscXceedQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 9), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDiscXceedQDepth.setStatus('current')
rcvBytesDiscXceedQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 10), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytesDiscXceedQDepth.setStatus('current')
rcvFramesDiscXceedDEThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 11), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDiscXceedDEThresh.setStatus('current')
rcvFramesFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 12), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesFECN.setStatus('current')
rcvFramesBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 13), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesBECN.setStatus('current')
rcvFramesTaggedFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 14), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesTaggedFECN.setStatus('current')
rcvFramesTaggedBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 15), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesTaggedBECN.setStatus('current')
rcvFramesTaggedDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 16), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesTaggedDE.setStatus('current')
rcvBytesTaggedDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 17), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytesTaggedDE.setStatus('current')
rcvKbpsAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 18), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvKbpsAIR.setStatus('current')
xmtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 19), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFrames.setStatus('current')
xmtBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 20), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytes.setStatus('current')
xmtFramesFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 21), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesFECN.setStatus('current')
xmtFramesBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 22), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesBECN.setStatus('current')
xmtFramesDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 23), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDE.setStatus('current')
xmtBytesDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 24), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesDE.setStatus('current')
xmtFramesDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 25), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscard.setStatus('current')
xmtBytesDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 26), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesDiscard.setStatus('current')
xmtFramesDiscXceedQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 27), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscXceedQDepth.setStatus('current')
xmtBytesDiscXceedQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 28), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesDiscXceedQDepth.setStatus('current')
xmtFramesDiscXceedDEThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 29), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscXceedDEThresh.setStatus('current')
xmtFramesDiscPhyLayerFail = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 30), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscPhyLayerFail.setStatus('current')
xmtFramesDiscCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 31), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscCRCError.setStatus('current')
xmtFramesDiscReassmFail = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscReassmFail.setStatus('current')
xmtFramesDiscSrcAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDiscSrcAbort.setStatus('current')
xmtFramesDuringLMIAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesDuringLMIAlarm.setStatus('current')
xmtBytesDuringLMIAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesDuringLMIAlarm.setStatus('current')
xmtFramesTaggedFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesTaggedFECN.setStatus('current')
xmtFramesTaggedBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 37), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesTaggedBECN.setStatus('current')
xmtKbpsAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 38), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtKbpsAIR.setStatus('current')
chanClrButton = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chanClrButton.setStatus('current')
xmtFramesTaggedDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 40), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesTaggedDE.setStatus('current')
xmtBytesTaggedDE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 41), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesTaggedDE.setStatus('current')
rcvFramesDiscUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 42), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesDiscUPC.setStatus('current')
chanSecUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 43), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: chanSecUpTime.setStatus('current')
xmtFramesInvalidCPIs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 44), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesInvalidCPIs.setStatus('current')
xmtFramesLengthViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 45), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesLengthViolations.setStatus('current')
xmtFramesOversizedSDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 46), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesOversizedSDUs.setStatus('current')
xmtFramesUnknownProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtFramesUnknownProtocols.setStatus('current')
rcvFramesUnknownProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 48), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvFramesUnknownProtocols.setStatus('current')
xmtBytesDEDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 49), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtBytesDEDiscard.setStatus('current')
rcvBytesDEDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 50), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvBytesDEDiscard.setStatus('current')
frstdABRCntGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2), )
if mibBuilder.loadTexts: frstdABRCntGrpTable.setStatus('current')
frstdABRCntGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1), ).setIndexNames((0, "CISCO-WAN-FR-CONN-STAT-MIB", "frstdABRcntChanNum"))
if mibBuilder.loadTexts: frstdABRCntGrpEntry.setStatus('current')
frstdABRcntChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frstdABRcntChanNum.setStatus('current')
frChanFrmXmtToNetworkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanFrmXmtToNetworkCnt.setStatus('current')
frChanBrmXmtToNetworkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanBrmXmtToNetworkCnt.setStatus('current')
frChanCrcErrRmRcvFromNetworkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanCrcErrRmRcvFromNetworkCnt.setStatus('current')
frChanFrmRcvFromNetworkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanFrmRcvFromNetworkCnt.setStatus('current')
frChanBrmRcvFromNetworkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanBrmRcvFromNetworkCnt.setStatus('current')
frChanFrmNotTurnedAroundCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frChanFrmNotTurnedAroundCnt.setStatus('current')
cwfConnStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 48, 2))
cwfConnStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1))
cwfConnStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 2))
ciscoWanFrConnStatCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 2, 1)).setObjects(("CISCO-WAN-FR-CONN-STAT-MIB", "ciscoWanFrConnStatsGroup"), ("CISCO-WAN-FR-CONN-STAT-MIB", "ciscoWanFrConnABRStatsGroup"), ("CISCO-WAN-FR-CONN-STAT-MIB", "ciscoWanFrConnQueueStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrConnStatCompliance = ciscoWanFrConnStatCompliance.setStatus('current')
ciscoWanFrConnStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 1)).setObjects(("CISCO-WAN-FR-CONN-STAT-MIB", "cntChanNum"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFrames"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytes"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscard"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDiscard"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscShelfAlarm"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesFECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesBECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedFECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedBECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesTaggedDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvKbpsAIR"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFrames"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytes"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesFECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesBECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscard"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDiscard"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscPhyLayerFail"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscCRCError"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscReassmFail"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscSrcAbort"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDuringLMIAlarm"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDuringLMIAlarm"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedFECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedBECN"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtKbpsAIR"), ("CISCO-WAN-FR-CONN-STAT-MIB", "chanClrButton"), ("CISCO-WAN-FR-CONN-STAT-MIB", "chanSecUpTime"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscUPC"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesTaggedDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedDE"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesInvalidCPIs"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesLengthViolations"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesOversizedSDUs"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesUnknownProtocols"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesUnknownProtocols"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDEDiscard"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDEDiscard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrConnStatsGroup = ciscoWanFrConnStatsGroup.setStatus('current')
ciscoWanFrConnQueueStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 2)).setObjects(("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscXceedQDepth"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDiscXceedQDepth"), ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscXceedDEThresh"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscXceedQDepth"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDiscXceedQDepth"), ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscXceedDEThresh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrConnQueueStatsGroup = ciscoWanFrConnQueueStatsGroup.setStatus('current')
ciscoWanFrConnABRStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 3)).setObjects(("CISCO-WAN-FR-CONN-STAT-MIB", "frstdABRcntChanNum"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmXmtToNetworkCnt"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanBrmXmtToNetworkCnt"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanCrcErrRmRcvFromNetworkCnt"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmRcvFromNetworkCnt"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanBrmRcvFromNetworkCnt"), ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmNotTurnedAroundCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrConnABRStatsGroup = ciscoWanFrConnABRStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-FR-CONN-STAT-MIB", frstdABRCntGrpTable=frstdABRCntGrpTable, rcvFramesDiscXceedDEThresh=rcvFramesDiscXceedDEThresh, cwfConnStatMIBCompliances=cwfConnStatMIBCompliances, ciscoWanFrConnQueueStatsGroup=ciscoWanFrConnQueueStatsGroup, xmtFramesDiscard=xmtFramesDiscard, rcvBytesDEDiscard=rcvBytesDEDiscard, xmtFramesLengthViolations=xmtFramesLengthViolations, rcvFramesDiscShelfAlarm=rcvFramesDiscShelfAlarm, xmtFramesDiscCRCError=xmtFramesDiscCRCError, xmtFramesUnknownProtocols=xmtFramesUnknownProtocols, ciscoWanFrConnStatMIB=ciscoWanFrConnStatMIB, frChanCntGrp=frChanCntGrp, xmtFramesBECN=xmtFramesBECN, rcvFramesDiscUPC=rcvFramesDiscUPC, ciscoWanFrConnStatsGroup=ciscoWanFrConnStatsGroup, xmtBytesDEDiscard=xmtBytesDEDiscard, xmtFramesInvalidCPIs=xmtFramesInvalidCPIs, rcvBytesDiscXceedQDepth=rcvBytesDiscXceedQDepth, rcvFramesUnknownProtocols=rcvFramesUnknownProtocols, frChanFrmRcvFromNetworkCnt=frChanFrmRcvFromNetworkCnt, rcvFramesFECN=rcvFramesFECN, frChanCntGrpTable=frChanCntGrpTable, cntChanNum=cntChanNum, rcvBytesTaggedDE=rcvBytesTaggedDE, xmtBytes=xmtBytes, rcvFramesDE=rcvFramesDE, xmtFramesOversizedSDUs=xmtFramesOversizedSDUs, xmtFramesDuringLMIAlarm=xmtFramesDuringLMIAlarm, xmtFramesDiscPhyLayerFail=xmtFramesDiscPhyLayerFail, rcvFramesTaggedBECN=rcvFramesTaggedBECN, frChanCntGrpEntry=frChanCntGrpEntry, rcvBytesDiscard=rcvBytesDiscard, xmtFramesFECN=xmtFramesFECN, rcvFramesDiscard=rcvFramesDiscard, xmtBytesTaggedDE=xmtBytesTaggedDE, rcvKbpsAIR=rcvKbpsAIR, frChanFrmXmtToNetworkCnt=frChanFrmXmtToNetworkCnt, xmtFrames=xmtFrames, frChanBrmXmtToNetworkCnt=frChanBrmXmtToNetworkCnt, PYSNMP_MODULE_ID=ciscoWanFrConnStatMIB, frstdABRCntGrpEntry=frstdABRCntGrpEntry, rcvFramesTaggedFECN=rcvFramesTaggedFECN, rcvBytesDE=rcvBytesDE, xmtBytesDE=xmtBytesDE, xmtFramesDiscXceedQDepth=xmtFramesDiscXceedQDepth, cwfConnStatMIBConformance=cwfConnStatMIBConformance, frChanFrmNotTurnedAroundCnt=frChanFrmNotTurnedAroundCnt, rcvBytes=rcvBytes, cwfConnStatMIBGroups=cwfConnStatMIBGroups, xmtFramesDiscSrcAbort=xmtFramesDiscSrcAbort, rcvFrames=rcvFrames, xmtBytesDuringLMIAlarm=xmtBytesDuringLMIAlarm, xmtBytesDiscXceedQDepth=xmtBytesDiscXceedQDepth, frChanBrmRcvFromNetworkCnt=frChanBrmRcvFromNetworkCnt, xmtKbpsAIR=xmtKbpsAIR, ciscoWanFrConnABRStatsGroup=ciscoWanFrConnABRStatsGroup, chanClrButton=chanClrButton, rcvFramesTaggedDE=rcvFramesTaggedDE, frChanCrcErrRmRcvFromNetworkCnt=frChanCrcErrRmRcvFromNetworkCnt, ciscoWanFrConnStatCompliance=ciscoWanFrConnStatCompliance, frstdABRcntChanNum=frstdABRcntChanNum, chanSecUpTime=chanSecUpTime, xmtFramesTaggedDE=xmtFramesTaggedDE, xmtFramesDE=xmtFramesDE, xmtFramesDiscXceedDEThresh=xmtFramesDiscXceedDEThresh, xmtFramesDiscReassmFail=xmtFramesDiscReassmFail, xmtFramesTaggedFECN=xmtFramesTaggedFECN, xmtFramesTaggedBECN=xmtFramesTaggedBECN, rcvFramesBECN=rcvFramesBECN, rcvFramesDiscXceedQDepth=rcvFramesDiscXceedQDepth, xmtBytesDiscard=xmtBytesDiscard)
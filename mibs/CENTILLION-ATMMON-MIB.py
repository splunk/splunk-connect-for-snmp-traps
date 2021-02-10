#
# PySNMP MIB module CENTILLION-ATMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-ATMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
MacAddress, PortId, atmMonitor, CardId = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "MacAddress", "PortId", "atmMonitor", "CardId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, TimeTicks, ModuleIdentity, IpAddress, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmPortMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1))
atmElanMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2))
atmPvcStatusMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3))
atmSigMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4))
atmCardMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5))
atmStatusEnqMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6))
atmPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1), )
if mibBuilder.loadTexts: atmPortStatTable.setStatus('mandatory')
atmPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmStatCardId"), (0, "CENTILLION-ATMMON-MIB", "atmStatPortId"))
if mibBuilder.loadTexts: atmPortStatEntry.setStatus('mandatory')
atmStatCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmStatCardId.setStatus('mandatory')
atmStatPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 2), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmStatPortId.setStatus('mandatory')
atmSigDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalpresent", 1), ("nosignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSigDetected.setStatus('mandatory')
atmRxBadHecCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxBadHecCell.setStatus('mandatory')
atmRxDmaDropCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxDmaDropCell.setStatus('mandatory')
atmRxGoodCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxGoodCell.setStatus('mandatory')
atmTxDmaDropCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTxDmaDropCell.setStatus('mandatory')
atmTxGoodCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTxGoodCell.setStatus('mandatory')
atmSuniFifoOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSuniFifoOverrun.setStatus('mandatory')
atmElanPvcStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: atmElanPvcStatisticTable.setStatus('mandatory')
atmElanPvcStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmElanId"))
if mibBuilder.loadTexts: atmElanPvcStatisticEntry.setStatus('mandatory')
atmElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanId.setStatus('mandatory')
atmElanPvcInUcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcInUcastPkt.setStatus('mandatory')
atmElanPvcInMcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcInMcastPkt.setStatus('mandatory')
atmElanPvcOutUcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcOutUcastPkt.setStatus('mandatory')
atmElanPvcOutMcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcOutMcastPkt.setStatus('mandatory')
atmPvcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1), )
if mibBuilder.loadTexts: atmPvcStatusTable.setStatus('mandatory')
atmPvcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmPvcCktId"))
if mibBuilder.loadTexts: atmPvcStatusEntry.setStatus('mandatory')
atmPvcCktId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcCktId.setStatus('mandatory')
atmPvcElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcElanId.setStatus('mandatory')
atmPvcRemoteSwitchInfoValid = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchInfoValid.setStatus('mandatory')
atmPvcRemoteSwitchMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchMacAddress.setStatus('mandatory')
atmPvcRemoteSwitchPvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchPvcStatus.setStatus('mandatory')
atmPvcSTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcSTPState.setStatus('mandatory')
atmPvcRemoteElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteElanId.setStatus('mandatory')
atmPvcRemoteMcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteMcpIpAddress.setStatus('mandatory')
cnCurPtptConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPtptConns.setStatus('mandatory')
cnCurPtmptConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPtmptConns.setStatus('mandatory')
cnCurActiveConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurActiveConns.setStatus('mandatory')
cnCurPortConnsTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4), )
if mibBuilder.loadTexts: cnCurPortConnsTable.setStatus('mandatory')
cnCurPortConnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cnCurPortConnsEntry.setStatus('mandatory')
cnCurPortConnsPtptConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsPtptConns.setStatus('mandatory')
cnCurPortConnsPtmptConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsPtmptConns.setStatus('mandatory')
cnCurPortConnsActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsActiveConns.setStatus('mandatory')
atmCardOperTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: atmCardOperTable.setStatus('mandatory')
atmCardOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmCardOperCardId"))
if mibBuilder.loadTexts: atmCardOperEntry.setStatus('mandatory')
atmCardOperCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperCardId.setStatus('mandatory')
atmCardOperExtClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperExtClockSource.setStatus('mandatory')
cnStsEnqPTPCalls = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqPTPCalls.setStatus('mandatory')
cnStsEnqActiveParties = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqActiveParties.setStatus('mandatory')
cnStsEnqSent = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqSent.setStatus('mandatory')
cnStsEnqCfmsRecvd = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqCfmsRecvd.setStatus('mandatory')
cnStsEnqRetried = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqRetried.setStatus('mandatory')
cnStsEnqTimeOuts = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqTimeOuts.setStatus('mandatory')
cnStsEnqQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqQueueSize.setStatus('mandatory')
cnStsEnqCallsCleared = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqCallsCleared.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-ATMMON-MIB", cnCurPortConnsEntry=cnCurPortConnsEntry, cnStsEnqPTPCalls=cnStsEnqPTPCalls, cnStsEnqActiveParties=cnStsEnqActiveParties, atmPvcStatusEntry=atmPvcStatusEntry, atmElanPvcOutUcastPkt=atmElanPvcOutUcastPkt, atmPortStatEntry=atmPortStatEntry, atmTxGoodCell=atmTxGoodCell, atmStatusEnqMonitor=atmStatusEnqMonitor, cnStsEnqCfmsRecvd=cnStsEnqCfmsRecvd, atmPvcRemoteSwitchPvcStatus=atmPvcRemoteSwitchPvcStatus, atmElanId=atmElanId, cnCurPtmptConns=cnCurPtmptConns, atmElanMonitor=atmElanMonitor, cnCurActiveConns=cnCurActiveConns, atmCardMonitor=atmCardMonitor, atmPvcRemoteSwitchMacAddress=atmPvcRemoteSwitchMacAddress, atmTxDmaDropCell=atmTxDmaDropCell, atmPvcRemoteSwitchInfoValid=atmPvcRemoteSwitchInfoValid, cnCurPortConnsPtptConns=cnCurPortConnsPtptConns, atmPortMonitor=atmPortMonitor, cnStsEnqCallsCleared=cnStsEnqCallsCleared, atmRxBadHecCell=atmRxBadHecCell, atmElanPvcStatisticEntry=atmElanPvcStatisticEntry, atmPvcCktId=atmPvcCktId, cnCurPortConnsPtmptConns=cnCurPortConnsPtmptConns, atmCardOperEntry=atmCardOperEntry, atmPvcStatusMonitor=atmPvcStatusMonitor, atmStatCardId=atmStatCardId, atmPvcElanId=atmPvcElanId, atmSigMonitor=atmSigMonitor, atmRxDmaDropCell=atmRxDmaDropCell, atmCardOperCardId=atmCardOperCardId, cnStsEnqQueueSize=cnStsEnqQueueSize, atmElanPvcInUcastPkt=atmElanPvcInUcastPkt, atmPvcStatusTable=atmPvcStatusTable, atmPvcSTPState=atmPvcSTPState, atmPvcRemoteElanId=atmPvcRemoteElanId, atmCardOperTable=atmCardOperTable, atmRxGoodCell=atmRxGoodCell, atmElanPvcInMcastPkt=atmElanPvcInMcastPkt, atmElanPvcOutMcastPkt=atmElanPvcOutMcastPkt, cnCurPortConnsTable=cnCurPortConnsTable, cnStsEnqRetried=cnStsEnqRetried, atmPortStatTable=atmPortStatTable, atmPvcRemoteMcpIpAddress=atmPvcRemoteMcpIpAddress, atmCardOperExtClockSource=atmCardOperExtClockSource, atmStatPortId=atmStatPortId, atmElanPvcStatisticTable=atmElanPvcStatisticTable, atmSigDetected=atmSigDetected, cnStsEnqSent=cnStsEnqSent, cnStsEnqTimeOuts=cnStsEnqTimeOuts, cnCurPtptConns=cnCurPtptConns, atmSuniFifoOverrun=atmSuniFifoOverrun, cnCurPortConnsActiveConns=cnCurPortConnsActiveConns)

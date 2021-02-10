#
# PySNMP MIB module Wellfleet-INT-SERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-INT-SERV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, Gauge32, Unsigned32, NotificationType, TimeTicks, Counter64, IpAddress, ModuleIdentity, iso, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "iso", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfIntegratedServicesGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIntegratedServicesGroup")
wfReservationsResourcesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2))
wfTxLineRscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1))
wfReservationsFlowspecGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3))
wfIntSrvIfFlowGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4))
wfTxLineRscTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1), )
if mibBuilder.loadTexts: wfTxLineRscTable.setStatus('mandatory')
wfTxLineRscEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1), ).setIndexNames((0, "Wellfleet-INT-SERV-MIB", "wfTxLineRscLineNumber"))
if mibBuilder.loadTexts: wfTxLineRscEntry.setStatus('mandatory')
wfTxLineRscKillReservations = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keep", 1), ("kill", 2))).clone('keep')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscKillReservations.setStatus('mandatory')
wfTxLineRscLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscLineNumber.setStatus('mandatory')
wfTxLineRscReservableBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscReservableBandwidth.setStatus('mandatory')
wfTxLineRscReservedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscReservedBandwidth.setStatus('mandatory')
wfTxLineRscGuaranteedFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedFlows.setStatus('mandatory')
wfTxLineRscGuaranteedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedPackets.setStatus('mandatory')
wfTxLineRscGuaranteedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedBytes.setStatus('mandatory')
wfTxLineRscGuaranteedPolicedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedPolicedPackets.setStatus('mandatory')
wfTxLineRscGuaranteedPolicedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedPolicedBytes.setStatus('mandatory')
wfTxLineRscGuaranteedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedBandwidth.setStatus('mandatory')
wfTxLineRscGuaranteedAvgBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedAvgBandwidth.setStatus('mandatory')
wfTxLineRscGuaranteedMaxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedMaxBandwidth.setStatus('mandatory')
wfTxLineRscGuaranteedAvgPacketDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedAvgPacketDelay.setStatus('mandatory')
wfTxLineRscGuaranteedMaxPacketDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscGuaranteedMaxPacketDelay.setStatus('mandatory')
wfTxLineRscUnreservedPolicedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscUnreservedPolicedPackets.setStatus('mandatory')
wfTxLineRscUnreservedPolicedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscUnreservedPolicedBytes.setStatus('mandatory')
wfTxLineRscCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3), )
if mibBuilder.loadTexts: wfTxLineRscCfgTable.setStatus('mandatory')
wfTxLineRscCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1), ).setIndexNames((0, "Wellfleet-INT-SERV-MIB", "wfTxLineRscCfgLineNumber"))
if mibBuilder.loadTexts: wfTxLineRscCfgEntry.setStatus('mandatory')
wfTxLineRscCfgDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgDelete.setStatus('mandatory')
wfTxLineRscCfgLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTxLineRscCfgLineNumber.setStatus('mandatory')
wfTxLineRscCfgEstBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgEstBandwidth.setStatus('mandatory')
wfTxLineRscCfgResvBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgResvBandwidth.setStatus('mandatory')
wfTxLineRscCfgResvTrafficAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("priority", 2))).clone('priority')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgResvTrafficAlgorithm.setStatus('mandatory')
wfTxLineRscCfgResvPolicingAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("lbucket", 2))).clone('lbucket')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgResvPolicingAlgorithm.setStatus('mandatory')
wfTxLineRscCfgBandwidthInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10))).clone(namedValues=NamedValues(("default", 10))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgBandwidthInterval.setStatus('mandatory')
wfTxLineRscCfgInflateReservations = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgInflateReservations.setStatus('mandatory')
wfTxLineRscCfgUnreservedPolicingAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("qlimit", 1), ("lbucket", 2))).clone('qlimit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgUnreservedPolicingAlgorithm.setStatus('mandatory')
wfTxLineRscCfgUnreservedQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(20))).clone(namedValues=NamedValues(("default", 20))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgUnreservedQueueLength.setStatus('mandatory')
wfTxLineRscCfgMultiLineSelectAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("first", 1), ("round", 2))).clone('first')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgMultiLineSelectAlgorithm.setStatus('mandatory')
wfTxLineRscCfgMultiLineThresholdBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgMultiLineThresholdBandwidth.setStatus('mandatory')
wfTxLineRscCfgResvLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgResvLatency.setStatus('mandatory')
wfTxLineRscCfgLargestBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgLargestBandwidth.setStatus('mandatory')
wfTxLineRscCfgLargestBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTxLineRscCfgLargestBuffer.setStatus('mandatory')
wfFlowspecSt2V3Table = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1), )
if mibBuilder.loadTexts: wfFlowspecSt2V3Table.setStatus('mandatory')
wfFlowspecSt2V3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1), ).setIndexNames((0, "Wellfleet-INT-SERV-MIB", "wfFlowspecSt2V3Index"))
if mibBuilder.loadTexts: wfFlowspecSt2V3Entry.setStatus('mandatory')
wfFlowspecSt2V3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3Index.setStatus('mandatory')
wfFlowspecSt2V3Version = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3Version.setStatus('mandatory')
wfFlowspecSt2V3DutyFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3DutyFactor.setStatus('mandatory')
wfFlowspecSt2V3ErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3ErrorRate.setStatus('mandatory')
wfFlowspecSt2V3Precedence = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3Precedence.setStatus('mandatory')
wfFlowspecSt2V3Reliability = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3Reliability.setStatus('mandatory')
wfFlowspecSt2V3Tradeoffs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3Tradeoffs.setStatus('mandatory')
wfFlowspecSt2V3RecoveryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3RecoveryTimeout.setStatus('mandatory')
wfFlowspecSt2V3LimitOnCost = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3LimitOnCost.setStatus('mandatory')
wfFlowspecSt2V3LimitOnDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3LimitOnDelay.setStatus('mandatory')
wfFlowspecSt2V3LimitOnPDUBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3LimitOnPDUBytes.setStatus('mandatory')
wfFlowspecSt2V3LimitOnPDURate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3LimitOnPDURate.setStatus('mandatory')
wfFlowspecSt2V3MinBytesXRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3MinBytesXRate.setStatus('mandatory')
wfFlowspecSt2V3AccdMeanDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3AccdMeanDelay.setStatus('mandatory')
wfFlowspecSt2V3AccdDelayVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3AccdDelayVariance.setStatus('mandatory')
wfFlowspecSt2V3DesPDUBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3DesPDUBytes.setStatus('mandatory')
wfFlowspecSt2V3DesPDURate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFlowspecSt2V3DesPDURate.setStatus('mandatory')
wfIntSrvIfFlowTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1), )
if mibBuilder.loadTexts: wfIntSrvIfFlowTable.setStatus('mandatory')
wfIntSrvIfFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1), ).setIndexNames((0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestination"), (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestinationProtocol"), (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestinationPort"), (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowSource"), (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowSourcePort"), (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowCct"))
if mibBuilder.loadTexts: wfIntSrvIfFlowEntry.setStatus('mandatory')
wfIntSrvIfFlowDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowDestination.setStatus('mandatory')
wfIntSrvIfFlowDestinationProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowDestinationProtocol.setStatus('mandatory')
wfIntSrvIfFlowDestinationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowDestinationPort.setStatus('mandatory')
wfIntSrvIfFlowSource = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowSource.setStatus('mandatory')
wfIntSrvIfFlowSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowSourcePort.setStatus('mandatory')
wfIntSrvIfFlowRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowRate.setStatus('mandatory')
wfIntSrvIfFlowWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowWeight.setStatus('mandatory')
wfIntSrvIfFlowQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowQueue.setStatus('mandatory')
wfIntSrvIfFlowMin = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowMin.setStatus('mandatory')
wfIntSrvIfFlowCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIntSrvIfFlowCct.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-INT-SERV-MIB", wfFlowspecSt2V3Index=wfFlowspecSt2V3Index, wfTxLineRscUnreservedPolicedBytes=wfTxLineRscUnreservedPolicedBytes, wfTxLineRscGuaranteedPolicedPackets=wfTxLineRscGuaranteedPolicedPackets, wfTxLineRscGuaranteedBandwidth=wfTxLineRscGuaranteedBandwidth, wfTxLineRscCfgResvTrafficAlgorithm=wfTxLineRscCfgResvTrafficAlgorithm, wfFlowspecSt2V3MinBytesXRate=wfFlowspecSt2V3MinBytesXRate, wfTxLineRscKillReservations=wfTxLineRscKillReservations, wfTxLineRscGroup=wfTxLineRscGroup, wfTxLineRscGuaranteedPackets=wfTxLineRscGuaranteedPackets, wfTxLineRscCfgTable=wfTxLineRscCfgTable, wfTxLineRscCfgResvPolicingAlgorithm=wfTxLineRscCfgResvPolicingAlgorithm, wfTxLineRscCfgDelete=wfTxLineRscCfgDelete, wfFlowspecSt2V3Precedence=wfFlowspecSt2V3Precedence, wfFlowspecSt2V3LimitOnCost=wfFlowspecSt2V3LimitOnCost, wfFlowspecSt2V3LimitOnDelay=wfFlowspecSt2V3LimitOnDelay, wfTxLineRscCfgEstBandwidth=wfTxLineRscCfgEstBandwidth, wfTxLineRscGuaranteedAvgPacketDelay=wfTxLineRscGuaranteedAvgPacketDelay, wfIntSrvIfFlowDestinationProtocol=wfIntSrvIfFlowDestinationProtocol, wfFlowspecSt2V3DesPDUBytes=wfFlowspecSt2V3DesPDUBytes, wfIntSrvIfFlowTable=wfIntSrvIfFlowTable, wfIntSrvIfFlowDestinationPort=wfIntSrvIfFlowDestinationPort, wfTxLineRscGuaranteedBytes=wfTxLineRscGuaranteedBytes, wfFlowspecSt2V3Version=wfFlowspecSt2V3Version, wfIntSrvIfFlowQueue=wfIntSrvIfFlowQueue, wfIntSrvIfFlowDestination=wfIntSrvIfFlowDestination, wfFlowspecSt2V3DutyFactor=wfFlowspecSt2V3DutyFactor, wfIntSrvIfFlowRate=wfIntSrvIfFlowRate, wfFlowspecSt2V3LimitOnPDURate=wfFlowspecSt2V3LimitOnPDURate, wfTxLineRscTable=wfTxLineRscTable, wfTxLineRscGuaranteedFlows=wfTxLineRscGuaranteedFlows, wfTxLineRscCfgLineNumber=wfTxLineRscCfgLineNumber, wfIntSrvIfFlowSourcePort=wfIntSrvIfFlowSourcePort, wfFlowspecSt2V3DesPDURate=wfFlowspecSt2V3DesPDURate, wfIntSrvIfFlowSource=wfIntSrvIfFlowSource, wfTxLineRscCfgResvLatency=wfTxLineRscCfgResvLatency, wfTxLineRscCfgMultiLineSelectAlgorithm=wfTxLineRscCfgMultiLineSelectAlgorithm, wfIntSrvIfFlowWeight=wfIntSrvIfFlowWeight, wfTxLineRscLineNumber=wfTxLineRscLineNumber, wfFlowspecSt2V3Table=wfFlowspecSt2V3Table, wfTxLineRscGuaranteedMaxPacketDelay=wfTxLineRscGuaranteedMaxPacketDelay, wfTxLineRscCfgEntry=wfTxLineRscCfgEntry, wfFlowspecSt2V3LimitOnPDUBytes=wfFlowspecSt2V3LimitOnPDUBytes, wfFlowspecSt2V3Entry=wfFlowspecSt2V3Entry, wfFlowspecSt2V3RecoveryTimeout=wfFlowspecSt2V3RecoveryTimeout, wfTxLineRscCfgInflateReservations=wfTxLineRscCfgInflateReservations, wfTxLineRscGuaranteedAvgBandwidth=wfTxLineRscGuaranteedAvgBandwidth, wfTxLineRscCfgLargestBuffer=wfTxLineRscCfgLargestBuffer, wfTxLineRscGuaranteedMaxBandwidth=wfTxLineRscGuaranteedMaxBandwidth, wfTxLineRscCfgUnreservedQueueLength=wfTxLineRscCfgUnreservedQueueLength, wfFlowspecSt2V3Tradeoffs=wfFlowspecSt2V3Tradeoffs, wfTxLineRscCfgUnreservedPolicingAlgorithm=wfTxLineRscCfgUnreservedPolicingAlgorithm, wfTxLineRscReservedBandwidth=wfTxLineRscReservedBandwidth, wfTxLineRscEntry=wfTxLineRscEntry, wfReservationsFlowspecGroup=wfReservationsFlowspecGroup, wfTxLineRscGuaranteedPolicedBytes=wfTxLineRscGuaranteedPolicedBytes, wfTxLineRscCfgLargestBandwidth=wfTxLineRscCfgLargestBandwidth, wfReservationsResourcesGroup=wfReservationsResourcesGroup, wfFlowspecSt2V3ErrorRate=wfFlowspecSt2V3ErrorRate, wfTxLineRscCfgMultiLineThresholdBandwidth=wfTxLineRscCfgMultiLineThresholdBandwidth, wfFlowspecSt2V3AccdMeanDelay=wfFlowspecSt2V3AccdMeanDelay, wfIntSrvIfFlowCct=wfIntSrvIfFlowCct, wfFlowspecSt2V3AccdDelayVariance=wfFlowspecSt2V3AccdDelayVariance, wfTxLineRscCfgResvBandwidth=wfTxLineRscCfgResvBandwidth, wfIntSrvIfFlowGroup=wfIntSrvIfFlowGroup, wfTxLineRscCfgBandwidthInterval=wfTxLineRscCfgBandwidthInterval, wfTxLineRscReservableBandwidth=wfTxLineRscReservableBandwidth, wfTxLineRscUnreservedPolicedPackets=wfTxLineRscUnreservedPolicedPackets, wfIntSrvIfFlowEntry=wfIntSrvIfFlowEntry, wfIntSrvIfFlowMin=wfIntSrvIfFlowMin, wfFlowspecSt2V3Reliability=wfFlowspecSt2V3Reliability)

#
# PySNMP MIB module S5-TOKENRING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-TOKENRING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
s5Tok, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Tok")
TimeIntervalSec, SrcIndx, TimeIntervalHrd = mibBuilder.importSymbols("S5-TCS-MIB", "TimeIntervalSec", "SrcIndx", "TimeIntervalHrd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter32, Bits, NotificationType, TimeTicks, Counter64, Integer32, Unsigned32, ModuleIdentity, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter32", "Bits", "NotificationType", "TimeTicks", "Counter64", "Integer32", "Unsigned32", "ModuleIdentity", "IpAddress", "Gauge32", "iso")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
s5TrCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1))
s5TrStat = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2))
s5TrRing = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3))
s5TrTest = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4))
s5TrRingInfoTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1), )
if mibBuilder.loadTexts: s5TrRingInfoTable.setStatus('mandatory')
s5TrRingInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1), ).setIndexNames((0, "S5-TOKENRING-MIB", "s5TrRingInfoSrcIndx"))
if mibBuilder.loadTexts: s5TrRingInfoEntry.setStatus('mandatory')
s5TrRingInfoSrcIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 1), SrcIndx()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoSrcIndx.setStatus('mandatory')
s5TrRingInfoRingNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoRingNum.setStatus('mandatory')
s5TrRingInfoStaTableOperSize = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoStaTableOperSize.setStatus('mandatory')
s5TrRingInfoActiveStations = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoActiveStations.setStatus('mandatory')
s5TrRingInfoDeletes = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoDeletes.setStatus('mandatory')
s5TrRingInfoLastDeleteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoLastDeleteTime.setStatus('mandatory')
s5TrRingInfoAgeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 7), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrRingInfoAgeInterval.setStatus('mandatory')
s5TrRingInfoMonTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoMonTime.setStatus('mandatory')
s5TrRingInfoRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normalOperation", 1), ("ringPurge", 2), ("monitorContention", 3), ("beaconFrameStreaming", 4), ("beaconBitStreaming", 5), ("beaconRingSignalLoss", 6), ("beaconSetRecoveryMode", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoRingState.setStatus('mandatory')
s5TrRingInfoBeaconSender = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoBeaconSender.setStatus('mandatory')
s5TrRingInfoBeaconNaun = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoBeaconNaun.setStatus('mandatory')
s5TrRingInfoBeaconType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("recovery", 2), ("signalLoss", 3), ("bitStreaming", 4), ("contentionStreaming", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoBeaconType.setStatus('mandatory')
s5TrRingInfoLastBeaconTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoLastBeaconTime.setStatus('mandatory')
s5TrRingInfoActiveMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoActiveMonitor.setStatus('mandatory')
s5TrRingInfoChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoChanges.setStatus('mandatory')
s5TrRingInfoRingPurgeEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoRingPurgeEvents.setStatus('mandatory')
s5TrRingInfoBeaconEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoBeaconEvents.setStatus('mandatory')
s5TrRingInfoBeaconTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 18), TimeIntervalHrd()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoBeaconTime.setStatus('mandatory')
s5TrRingInfoMonitorContentionEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoMonitorContentionEvents.setStatus('mandatory')
s5TrRingInfoNaunChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoNaunChanges.setStatus('mandatory')
s5TrRingInfoRingPollEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrRingInfoRingPollEvents.setStatus('mandatory')
s5TrStaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2), )
if mibBuilder.loadTexts: s5TrStaInfoTable.setStatus('mandatory')
s5TrStaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1), ).setIndexNames((0, "S5-TOKENRING-MIB", "s5TrStaInfoSrcIndx"), (0, "S5-TOKENRING-MIB", "s5TrStaInfoAddr"))
if mibBuilder.loadTexts: s5TrStaInfoEntry.setStatus('mandatory')
s5TrStaInfoSrcIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 1), SrcIndx()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoSrcIndx.setStatus('mandatory')
s5TrStaInfoAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoAddr.setStatus('mandatory')
s5TrStaInfoLastNaun = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoLastNaun.setStatus('mandatory')
s5TrStaInfoStationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("notInRingPoll", 2), ("inactive", 3), ("forcedRemoval", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoStationStatus.setStatus('mandatory')
s5TrStaInfoFirstEnterTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoFirstEnterTime.setStatus('mandatory')
s5TrStaInfoLastEnterTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoLastEnterTime.setStatus('mandatory')
s5TrStaInfoLastExitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoLastExitTime.setStatus('mandatory')
s5TrStaInfoDupAddrErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoDupAddrErrs.setStatus('mandatory')
s5TrStaInfoInLineErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInLineErrs.setStatus('mandatory')
s5TrStaInfoOutLineErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoOutLineErrs.setStatus('mandatory')
s5TrStaInfoInternalErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInternalErrs.setStatus('mandatory')
s5TrStaInfoInBurstErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInBurstErrs.setStatus('mandatory')
s5TrStaInfoOutBurstErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoOutBurstErrs.setStatus('mandatory')
s5TrStaInfoInACErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInACErrs.setStatus('mandatory')
s5TrStaInfoOutACErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoOutACErrs.setStatus('mandatory')
s5TrStaInfoAbortErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoAbortErrs.setStatus('mandatory')
s5TrStaInfoLostFrameErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoLostFrameErrs.setStatus('mandatory')
s5TrStaInfoCongestionErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoCongestionErrs.setStatus('mandatory')
s5TrStaInfoFrameCopiedErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoFrameCopiedErrs.setStatus('mandatory')
s5TrStaInfoFrequencyErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoFrequencyErrs.setStatus('mandatory')
s5TrStaInfoTokenErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoTokenErrs.setStatus('mandatory')
s5TrStaInfoInBeaconErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInBeaconErrs.setStatus('mandatory')
s5TrStaInfoOutBeaconErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoOutBeaconErrs.setStatus('mandatory')
s5TrStaInfoInsertions = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaInfoInsertions.setStatus('mandatory')
s5TrStaCtlTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3), )
if mibBuilder.loadTexts: s5TrStaCtlTable.setStatus('mandatory')
s5TrStaCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1), ).setIndexNames((0, "S5-TOKENRING-MIB", "s5TrStaCtlSrcIndx"), (0, "S5-TOKENRING-MIB", "s5TrStaCtlAddr"))
if mibBuilder.loadTexts: s5TrStaCtlEntry.setStatus('mandatory')
s5TrStaCtlSrcIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 1), SrcIndx()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlSrcIndx.setStatus('mandatory')
s5TrStaCtlAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlAddr.setStatus('mandatory')
s5TrStaCtlRemove = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stable", 1), ("remove", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrStaCtlRemove.setStatus('mandatory')
s5TrStaCtlUpdateStats = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("inactive", 2), ("stable", 3), ("update", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrStaCtlUpdateStats.setStatus('mandatory')
s5TrStaCtlUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlUpdateTime.setStatus('mandatory')
s5TrStaCtlProductId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlProductId.setStatus('mandatory')
s5TrStaCtlNodeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlNodeVersion.setStatus('mandatory')
s5TrStaCtlPhysDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlPhysDrop.setStatus('mandatory')
s5TrStaCtlFuncAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlFuncAddr.setStatus('mandatory')
s5TrStaCtlAuthFuncClass = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlAuthFuncClass.setStatus('mandatory')
s5TrStaCtlAuthAccPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlAuthAccPriority.setStatus('mandatory')
s5TrStaCtlStationId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlStationId.setStatus('mandatory')
s5TrStaCtlNumGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrStaCtlNumGrpAddr.setStatus('mandatory')
s5TrTestPathTestTimer = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 1), TimeIntervalHrd().clone(400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrTestPathTestTimer.setStatus('mandatory')
s5TrTestPathAgeTimer = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 2), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrTestPathAgeTimer.setStatus('mandatory')
s5TrTestPathTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3), )
if mibBuilder.loadTexts: s5TrTestPathTable.setStatus('mandatory')
s5TrTestPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1), ).setIndexNames((0, "S5-TOKENRING-MIB", "s5TrTestTpIfIndex"), (0, "S5-TOKENRING-MIB", "s5TrTestTpAddrTo"))
if mibBuilder.loadTexts: s5TrTestPathEntry.setStatus('mandatory')
s5TrTestTpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrTestTpIfIndex.setStatus('mandatory')
s5TrTestTpAddrTo = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrTestTpAddrTo.setStatus('mandatory')
s5TrTestTpStart = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("startTestSourceRoute", 2), ("startTestTransparent", 3), ("retryTestSourceRoute", 4), ("retryTestTransparent", 5), ("clearTest", 6))).clone('startTestSourceRoute')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrTestTpStart.setStatus('mandatory')
s5TrTestTpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("testInProgress", 2), ("testPassed", 3), ("testFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrTestTpStatus.setStatus('mandatory')
s5TrTestTpRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5TrTestTpRoute.setStatus('mandatory')
s5TrTestTpDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 6), TimeIntervalHrd()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrTestTpDuration.setStatus('mandatory')
s5TrTestTpTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5TrTestTpTimeStamp.setStatus('mandatory')
mibBuilder.exportSymbols("S5-TOKENRING-MIB", s5TrStaInfoOutBurstErrs=s5TrStaInfoOutBurstErrs, s5TrStaCtlStationId=s5TrStaCtlStationId, s5TrStaInfoCongestionErrs=s5TrStaInfoCongestionErrs, s5TrStaCtlNumGrpAddr=s5TrStaCtlNumGrpAddr, s5TrStaInfoStationStatus=s5TrStaInfoStationStatus, s5TrStaCtlUpdateTime=s5TrStaCtlUpdateTime, s5TrTestPathAgeTimer=s5TrTestPathAgeTimer, s5TrStaInfoSrcIndx=s5TrStaInfoSrcIndx, s5TrStaInfoFirstEnterTime=s5TrStaInfoFirstEnterTime, s5TrRingInfoBeaconType=s5TrRingInfoBeaconType, s5TrRingInfoDeletes=s5TrRingInfoDeletes, s5TrRingInfoRingNum=s5TrRingInfoRingNum, s5TrStaCtlEntry=s5TrStaCtlEntry, s5TrTestTpStart=s5TrTestTpStart, s5TrStaInfoAbortErrs=s5TrStaInfoAbortErrs, s5TrStaCtlProductId=s5TrStaCtlProductId, s5TrStaCtlFuncAddr=s5TrStaCtlFuncAddr, s5TrStaCtlAuthAccPriority=s5TrStaCtlAuthAccPriority, s5TrStaInfoInBeaconErrs=s5TrStaInfoInBeaconErrs, s5TrRingInfoBeaconEvents=s5TrRingInfoBeaconEvents, s5TrTest=s5TrTest, s5TrRingInfoLastBeaconTime=s5TrRingInfoLastBeaconTime, s5TrRingInfoActiveStations=s5TrRingInfoActiveStations, s5TrRingInfoBeaconNaun=s5TrRingInfoBeaconNaun, s5TrTestTpTimeStamp=s5TrTestTpTimeStamp, s5TrStaCtlPhysDrop=s5TrStaCtlPhysDrop, s5TrRingInfoBeaconTime=s5TrRingInfoBeaconTime, s5TrRingInfoTable=s5TrRingInfoTable, s5TrStaInfoInACErrs=s5TrStaInfoInACErrs, s5TrRingInfoAgeInterval=s5TrRingInfoAgeInterval, s5TrStaInfoLostFrameErrs=s5TrStaInfoLostFrameErrs, s5TrStaInfoInLineErrs=s5TrStaInfoInLineErrs, s5TrStaInfoOutACErrs=s5TrStaInfoOutACErrs, s5TrTestTpAddrTo=s5TrTestTpAddrTo, s5TrRingInfoBeaconSender=s5TrRingInfoBeaconSender, s5TrRingInfoMonitorContentionEvents=s5TrRingInfoMonitorContentionEvents, s5TrStaInfoLastNaun=s5TrStaInfoLastNaun, s5TrRingInfoRingState=s5TrRingInfoRingState, s5TrRingInfoRingPollEvents=s5TrRingInfoRingPollEvents, s5TrTestTpIfIndex=s5TrTestTpIfIndex, s5TrStaInfoInternalErrs=s5TrStaInfoInternalErrs, s5TrTestTpRoute=s5TrTestTpRoute, s5TrStaInfoLastEnterTime=s5TrStaInfoLastEnterTime, s5TrStaInfoOutBeaconErrs=s5TrStaInfoOutBeaconErrs, s5TrStaCtlAuthFuncClass=s5TrStaCtlAuthFuncClass, s5TrStaCtlSrcIndx=s5TrStaCtlSrcIndx, s5TrRingInfoLastDeleteTime=s5TrRingInfoLastDeleteTime, s5TrStaCtlRemove=s5TrStaCtlRemove, s5TrTestPathTestTimer=s5TrTestPathTestTimer, s5TrStaInfoAddr=s5TrStaInfoAddr, s5TrStaInfoInsertions=s5TrStaInfoInsertions, s5TrRingInfoEntry=s5TrRingInfoEntry, s5TrStaCtlNodeVersion=s5TrStaCtlNodeVersion, s5TrTestTpDuration=s5TrTestTpDuration, s5TrTestPathEntry=s5TrTestPathEntry, s5TrRingInfoStaTableOperSize=s5TrRingInfoStaTableOperSize, s5TrStaInfoEntry=s5TrStaInfoEntry, s5TrStaInfoDupAddrErrs=s5TrStaInfoDupAddrErrs, s5TrRingInfoChanges=s5TrRingInfoChanges, s5TrStaInfoFrequencyErrs=s5TrStaInfoFrequencyErrs, s5TrStaInfoInBurstErrs=s5TrStaInfoInBurstErrs, s5TrTestTpStatus=s5TrTestTpStatus, s5TrStaInfoOutLineErrs=s5TrStaInfoOutLineErrs, s5TrRingInfoActiveMonitor=s5TrRingInfoActiveMonitor, s5TrRingInfoNaunChanges=s5TrRingInfoNaunChanges, s5TrCfg=s5TrCfg, s5TrStaCtlUpdateStats=s5TrStaCtlUpdateStats, s5TrStaInfoFrameCopiedErrs=s5TrStaInfoFrameCopiedErrs, s5TrStaCtlTable=s5TrStaCtlTable, s5TrRingInfoSrcIndx=s5TrRingInfoSrcIndx, s5TrStaInfoTokenErrs=s5TrStaInfoTokenErrs, s5TrRing=s5TrRing, s5TrStat=s5TrStat, s5TrStaInfoLastExitTime=s5TrStaInfoLastExitTime, s5TrRingInfoMonTime=s5TrRingInfoMonTime, s5TrStaCtlAddr=s5TrStaCtlAddr, s5TrRingInfoRingPurgeEvents=s5TrRingInfoRingPurgeEvents, s5TrStaInfoTable=s5TrStaInfoTable, s5TrTestPathTable=s5TrTestPathTable)
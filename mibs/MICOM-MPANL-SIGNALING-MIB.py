#
# PySNMP MIB module MICOM-MPANL-SIGNALING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-MPANL-SIGNALING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
mcmSysAsciiTimeOfDay, = mibBuilder.importSymbols("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Bits, IpAddress, Gauge32, ModuleIdentity, ObjectIdentity, Counter32, Unsigned32, iso, Integer32, Counter64, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Bits", "IpAddress", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Counter32", "Unsigned32", "iso", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom_msm = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19)).setLabel("micom-msm")
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1))
control = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2))
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4))
mcmMSMProfileCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1))
mcmMSMProfileCfgGroupNodeID = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMProfileCfgGroupNodeID.setStatus('mandatory')
mcmMSMProfileCfgGroupCustomerID = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMProfileCfgGroupCustomerID.setStatus('mandatory')
mcmMSMProfileCfgGroupDNAPrefix = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMProfileCfgGroupDNAPrefix.setStatus('mandatory')
nvmMSMProfileCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2))
nvmMSMProfileCfgGroupNodeID = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMProfileCfgGroupNodeID.setStatus('mandatory')
nvmMSMProfileCfgGroupCustomerID = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMProfileCfgGroupCustomerID.setStatus('mandatory')
nvmMSMProfileCfgGroupDNAPrefix = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMProfileCfgGroupDNAPrefix.setStatus('mandatory')
mcmMSMDTELinkCfgTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3), )
if mibBuilder.loadTexts: mcmMSMDTELinkCfgTable.setStatus('mandatory')
mcmMSMDTELinkCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkCfgIfIndex"))
if mibBuilder.loadTexts: mcmMSMDTELinkCfgEntry.setStatus('mandatory')
mcmMSMDTELinkCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgIfIndex.setStatus('mandatory')
mcmMSMDTELinkCfgMaxSubChannelRange = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(17, 255)).clone(63)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgMaxSubChannelRange.setStatus('mandatory')
mcmMSMDTELinkCfgDTEReceiverBW = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16000, 2048000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgDTEReceiverBW.setStatus('mandatory')
mcmMSMDTELinkCfgDCEReceiverBW = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16000, 2048000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgDCEReceiverBW.setStatus('mandatory')
mcmMSMDTELinkCfgDTEMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 4100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgDTEMaxFrameSize.setStatus('mandatory')
mcmMSMDTELinkCfgDCEMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 4100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkCfgDCEMaxFrameSize.setStatus('mandatory')
nvmMSMDTELinkCfgTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4), )
if mibBuilder.loadTexts: nvmMSMDTELinkCfgTable.setStatus('mandatory')
nvmMSMDTELinkCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "nvmMSMDTELinkCfgIfIndex"))
if mibBuilder.loadTexts: nvmMSMDTELinkCfgEntry.setStatus('mandatory')
nvmMSMDTELinkCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgIfIndex.setStatus('mandatory')
nvmMSMDTELinkCfgMaxSubChannelRange = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(17, 255)).clone(63)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgMaxSubChannelRange.setStatus('mandatory')
nvmMSMDTELinkCfgDTEReceiverBW = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16000, 2048000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgDTEReceiverBW.setStatus('mandatory')
nvmMSMDTELinkCfgDCEReceiverBW = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16000, 2048000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgDCEReceiverBW.setStatus('mandatory')
nvmMSMDTELinkCfgDTEMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 4100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgDTEMaxFrameSize.setStatus('mandatory')
nvmMSMDTELinkCfgDCEMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 4100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgDCEMaxFrameSize.setStatus('mandatory')
nvmMSMDTELinkCfgEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("modify", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nvmMSMDTELinkCfgEntryStatus.setStatus('obsolete')
mcmMSMStatsLAPFConnTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1), )
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnTable.setStatus('mandatory')
mcmMSMStatsLAPFConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMStatsLAPFConnIfIndex"))
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnEntry.setStatus('mandatory')
mcmMSMStatsLAPFConnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnIfIndex.setStatus('mandatory')
mcmMSMStatsLAPFConnReestablished = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnReestablished.setStatus('obsolete')
mcmMSMStatsLAPFConnEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnEstablished.setStatus('mandatory')
mcmMSMStatsLAPFConnDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsLAPFConnDisconnects.setStatus('mandatory')
mcmMSMStatsProfileTxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsProfileTxCnt.setStatus('mandatory')
mcmMSMStatsProfileRxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsProfileRxCnt.setStatus('mandatory')
mcmMSMStatsRestartReqTxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsRestartReqTxCnt.setStatus('mandatory')
mcmMSMStatsRestartReqRxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsRestartReqRxCnt.setStatus('mandatory')
mcmMSMStatsDnaAssociationCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsDnaAssociationCnt.setStatus('mandatory')
mcmMSMStatsDnaDeassociationCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsDnaDeassociationCnt.setStatus('mandatory')
mcmMSMStatsPANLInfoElementsTxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsPANLInfoElementsTxCnt.setStatus('mandatory')
mcmMSMStatsPANLInfoElementsRxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMStatsPANLInfoElementsRxCnt.setStatus('mandatory')
mcmMSMDTELinkStatsTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2), )
if mibBuilder.loadTexts: mcmMSMDTELinkStatsTable.setStatus('deprecated')
mcmMSMDTELinkStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkStatsIfIndex"))
if mibBuilder.loadTexts: mcmMSMDTELinkStatsEntry.setStatus('deprecated')
mcmMSMDTELinkStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkStatsIfIndex.setStatus('deprecated')
mcmMSMDTELinkStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkStatsStatus.setStatus('deprecated')
mcmMSMDTELinkStatsLocalCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkStatsLocalCompName.setStatus('deprecated')
mcmMSMDTELinkStatsRemoteCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDTELinkStatsRemoteCompName.setStatus('deprecated')
mcmMSMLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1), )
if mibBuilder.loadTexts: mcmMSMLinkStatusTable.setStatus('mandatory')
mcmMSMLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"))
if mibBuilder.loadTexts: mcmMSMLinkStatusEntry.setStatus('mandatory')
mcmMSMLinkStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusIfIndex.setStatus('mandatory')
mcmMSMLinkStatusInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusInterfaceType.setStatus('mandatory')
mcmMSMLinkStatusLAPFStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusLAPFStatus.setStatus('mandatory')
mcmMSMLinkStatusLocalCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusLocalCompName.setStatus('mandatory')
mcmMSMLinkStatusRemoteCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusRemoteCompName.setStatus('mandatory')
mcmMSMLinkStatusRemoteGenCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("micomAccessDevice", 1), ("nortelAccessDevice", 2), ("passportSwitch", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusRemoteGenCfgType.setStatus('mandatory')
mcmMSMLinkStatusPANLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("restart", 3), ("incompatible", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLinkStatusPANLStatus.setStatus('mandatory')
mcmMSMDCELinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2), )
if mibBuilder.loadTexts: mcmMSMDCELinkStatusTable.setStatus('mandatory')
mcmMSMDCELinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDCELinkStatusIfIndex"))
if mibBuilder.loadTexts: mcmMSMDCELinkStatusEntry.setStatus('mandatory')
mcmMSMDCELinkStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusIfIndex.setStatus('mandatory')
mcmMSMDCELinkStatusRemoteNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusRemoteNodeId.setStatus('mandatory')
mcmMSMDCELinkStatusRemoteCustId = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusRemoteCustId.setStatus('mandatory')
mcmMSMDCELinkStatusRemoteRxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1600, 2048000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusRemoteRxBw.setStatus('mandatory')
mcmMSMDCELinkStatusRemoteMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 4100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusRemoteMaxFrameSize.setStatus('mandatory')
mcmMSMDCELinkStatusRemoteDLCIRange = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(17, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDCELinkStatusRemoteDLCIRange.setStatus('mandatory')
mcmMSMDNAStatusTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3), )
if mibBuilder.loadTexts: mcmMSMDNAStatusTable.setStatus('mandatory')
mcmMSMDNAStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusPrefixNumber"))
if mibBuilder.loadTexts: mcmMSMDNAStatusEntry.setStatus('mandatory')
mcmMSMDNAStatusPrefixNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDNAStatusPrefixNumber.setStatus('mandatory')
mcmMSMDNAStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDNAStatusIfIndex.setStatus('mandatory')
mcmMSMDNAStatusAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("associatedDNA", 1), ("deassociatedDNA", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMDNAStatusAssociation.setStatus('mandatory')
mcmMSMLAPFConnectionsCntrTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1), )
if mibBuilder.loadTexts: mcmMSMLAPFConnectionsCntrTable.setStatus('obsolete')
mcmMSMLAPFConnectionsCntrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1), ).setIndexNames((0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMLAPFConnectionsCntrIndex"))
if mibBuilder.loadTexts: mcmMSMLAPFConnectionsCntrEntry.setStatus('obsolete')
mcmMSMLAPFConnectionsCntrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMSMLAPFConnectionsCntrIndex.setStatus('obsolete')
mcmMSMLAPFConnectionsCntrAction = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mcmMSMLAPFConnectionsCntrAction.setStatus('obsolete')
mcmMSMProfileReceivedFromPassport = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,1)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkStatsRemoteCompName"))
mcmMpanlInterfaceLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,2)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"))
mcmMpanlInterfaceLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,3)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"))
mcmMpanlPrefixDNAhasNotBeenConfigured = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,4)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"))
mcmMpanlPrefixDNAChangedWithoutDeassociation = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,5)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusPrefixNumber"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusIfIndex"))
mcmMpanlIncompatibleType = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 19) + (0,6)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"), ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusRemoteGenCfgType"))
mibBuilder.exportSymbols("MICOM-MPANL-SIGNALING-MIB", nvmMSMDTELinkCfgTable=nvmMSMDTELinkCfgTable, nvmMSMProfileCfgGroup=nvmMSMProfileCfgGroup, mcmMSMStatsPANLInfoElementsRxCnt=mcmMSMStatsPANLInfoElementsRxCnt, mcmMSMDTELinkCfgDCEMaxFrameSize=mcmMSMDTELinkCfgDCEMaxFrameSize, mcmMSMStatsProfileRxCnt=mcmMSMStatsProfileRxCnt, mcmMSMLinkStatusLAPFStatus=mcmMSMLinkStatusLAPFStatus, mcmMSMStatsDnaAssociationCnt=mcmMSMStatsDnaAssociationCnt, mcmMSMLinkStatusPANLStatus=mcmMSMLinkStatusPANLStatus, mcmMSMDCELinkStatusIfIndex=mcmMSMDCELinkStatusIfIndex, mcmMSMDNAStatusEntry=mcmMSMDNAStatusEntry, mcmMSMDNAStatusIfIndex=mcmMSMDNAStatusIfIndex, nvmMSMDTELinkCfgEntry=nvmMSMDTELinkCfgEntry, mcmMSMDCELinkStatusTable=mcmMSMDCELinkStatusTable, nvmMSMDTELinkCfgDTEReceiverBW=nvmMSMDTELinkCfgDTEReceiverBW, mcmMSMStatsRestartReqRxCnt=mcmMSMStatsRestartReqRxCnt, mcmMSMStatsLAPFConnEstablished=mcmMSMStatsLAPFConnEstablished, mcmMSMProfileCfgGroup=mcmMSMProfileCfgGroup, mcmMSMDCELinkStatusRemoteRxBw=mcmMSMDCELinkStatusRemoteRxBw, mcmMSMLinkStatusEntry=mcmMSMLinkStatusEntry, mcmMSMStatsLAPFConnReestablished=mcmMSMStatsLAPFConnReestablished, mcmMSMLAPFConnectionsCntrEntry=mcmMSMLAPFConnectionsCntrEntry, mcmMSMDTELinkStatsEntry=mcmMSMDTELinkStatsEntry, nvmMSMProfileCfgGroupNodeID=nvmMSMProfileCfgGroupNodeID, mcmMSMDTELinkCfgEntry=mcmMSMDTELinkCfgEntry, mcmMSMLAPFConnectionsCntrIndex=mcmMSMLAPFConnectionsCntrIndex, mcmMSMDCELinkStatusRemoteDLCIRange=mcmMSMDCELinkStatusRemoteDLCIRange, mcmMSMDCELinkStatusRemoteCustId=mcmMSMDCELinkStatusRemoteCustId, nvmMSMDTELinkCfgEntryStatus=nvmMSMDTELinkCfgEntryStatus, control=control, nvmMSMDTELinkCfgMaxSubChannelRange=nvmMSMDTELinkCfgMaxSubChannelRange, mcmMSMDTELinkStatsTable=mcmMSMDTELinkStatsTable, mcmMSMDTELinkStatsStatus=mcmMSMDTELinkStatsStatus, nvmMSMDTELinkCfgDTEMaxFrameSize=nvmMSMDTELinkCfgDTEMaxFrameSize, mcmMSMStatsLAPFConnTable=mcmMSMStatsLAPFConnTable, mcmMSMDTELinkCfgMaxSubChannelRange=mcmMSMDTELinkCfgMaxSubChannelRange, mcmMpanlInterfaceLinkDown=mcmMpanlInterfaceLinkDown, mcmMSMDTELinkStatsRemoteCompName=mcmMSMDTELinkStatsRemoteCompName, mcmMSMLinkStatusRemoteCompName=mcmMSMLinkStatusRemoteCompName, nvmMSMDTELinkCfgIfIndex=nvmMSMDTELinkCfgIfIndex, mcmMSMDNAStatusTable=mcmMSMDNAStatusTable, mcmMSMLinkStatusLocalCompName=mcmMSMLinkStatusLocalCompName, mcmMSMDTELinkCfgTable=mcmMSMDTELinkCfgTable, mcmMSMStatsDnaDeassociationCnt=mcmMSMStatsDnaDeassociationCnt, mcmMSMProfileReceivedFromPassport=mcmMSMProfileReceivedFromPassport, mcmMSMDNAStatusPrefixNumber=mcmMSMDNAStatusPrefixNumber, nvmMSMProfileCfgGroupDNAPrefix=nvmMSMProfileCfgGroupDNAPrefix, nvmMSMProfileCfgGroupCustomerID=nvmMSMProfileCfgGroupCustomerID, mcmMSMDTELinkStatsIfIndex=mcmMSMDTELinkStatsIfIndex, configuration=configuration, mcmMSMStatsLAPFConnIfIndex=mcmMSMStatsLAPFConnIfIndex, status=status, mcmMSMDTELinkCfgDTEReceiverBW=mcmMSMDTELinkCfgDTEReceiverBW, nvmMSMDTELinkCfgDCEReceiverBW=nvmMSMDTELinkCfgDCEReceiverBW, mcmMpanlInterfaceLinkUp=mcmMpanlInterfaceLinkUp, mcmMSMLinkStatusTable=mcmMSMLinkStatusTable, mcmMSMProfileCfgGroupCustomerID=mcmMSMProfileCfgGroupCustomerID, mcmMpanlPrefixDNAhasNotBeenConfigured=mcmMpanlPrefixDNAhasNotBeenConfigured, mcmMSMDCELinkStatusRemoteMaxFrameSize=mcmMSMDCELinkStatusRemoteMaxFrameSize, mcmMSMDCELinkStatusEntry=mcmMSMDCELinkStatusEntry, mcmMSMLinkStatusInterfaceType=mcmMSMLinkStatusInterfaceType, micom_msm=micom_msm, mcmMSMDNAStatusAssociation=mcmMSMDNAStatusAssociation, mcmMSMDTELinkCfgIfIndex=mcmMSMDTELinkCfgIfIndex, mcmMSMDTELinkCfgDTEMaxFrameSize=mcmMSMDTELinkCfgDTEMaxFrameSize, nvmMSMDTELinkCfgDCEMaxFrameSize=nvmMSMDTELinkCfgDCEMaxFrameSize, mcmMSMProfileCfgGroupNodeID=mcmMSMProfileCfgGroupNodeID, statistics=statistics, mcmMpanlIncompatibleType=mcmMpanlIncompatibleType, mcmMSMDCELinkStatusRemoteNodeId=mcmMSMDCELinkStatusRemoteNodeId, mcmMSMDTELinkCfgDCEReceiverBW=mcmMSMDTELinkCfgDCEReceiverBW, mcmMSMLinkStatusRemoteGenCfgType=mcmMSMLinkStatusRemoteGenCfgType, mcmMSMStatsRestartReqTxCnt=mcmMSMStatsRestartReqTxCnt, mcmMSMLinkStatusIfIndex=mcmMSMLinkStatusIfIndex, mcmMSMStatsLAPFConnEntry=mcmMSMStatsLAPFConnEntry, mcmMpanlPrefixDNAChangedWithoutDeassociation=mcmMpanlPrefixDNAChangedWithoutDeassociation, mcmMSMStatsLAPFConnDisconnects=mcmMSMStatsLAPFConnDisconnects, mcmMSMStatsProfileTxCnt=mcmMSMStatsProfileTxCnt, mcmMSMProfileCfgGroupDNAPrefix=mcmMSMProfileCfgGroupDNAPrefix, mcmMSMStatsPANLInfoElementsTxCnt=mcmMSMStatsPANLInfoElementsTxCnt, mcmMSMLAPFConnectionsCntrTable=mcmMSMLAPFConnectionsCntrTable, mcmMSMLAPFConnectionsCntrAction=mcmMSMLAPFConnectionsCntrAction, mcmMSMDTELinkStatsLocalCompName=mcmMSMDTELinkStatsLocalCompName)

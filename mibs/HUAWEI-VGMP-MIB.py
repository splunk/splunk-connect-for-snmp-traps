#
# PySNMP MIB module HUAWEI-VGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VGMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, TimeTicks, Integer32, Bits, Gauge32, Counter64, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Integer32", "Bits", "Gauge32", "Counter64", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32")
RowStatus, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TimeStamp")
hwVgmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122))
hwVgmpMib.setRevisions(('2007-01-11 21:00',))
if mibBuilder.loadTexts: hwVgmpMib.setLastUpdated('200701112100Z')
if mibBuilder.loadTexts: hwVgmpMib.setOrganization('Huawei Technologies co., Ltd.')
vgmpGlobalCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0))
hwVgmpTrapSnmpCtrl = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVgmpTrapSnmpCtrl.setStatus('current')
hwVgmpStrictCheck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVgmpStrictCheck.setStatus('current')
vgmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1))
hwVgmpOtherStateToMaster = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1, 1)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
if mibBuilder.loadTexts: hwVgmpOtherStateToMaster.setStatus('current')
hwVgmpMasterToOtherState = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1, 2)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
if mibBuilder.loadTexts: hwVgmpMasterToOtherState.setStatus('current')
vgmpOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2))
vgmpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3))
vgmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4))
hwVgmpGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1), )
if mibBuilder.loadTexts: hwVgmpGroupCfgTable.setStatus('current')
hwVgmpGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1), ).setIndexNames((0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"))
if mibBuilder.loadTexts: hwVgmpGroupCfgEntry.setStatus('current')
hwVgmpGroupCfgID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwVgmpGroupCfgID.setStatus('current')
hwVgmpGroupCfgEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgEnable.setStatus('current')
hwVgmpGroupCfgPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgPri.setStatus('current')
hwVgmpGroupCfgUseVrrpPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgUseVrrpPri.setStatus('current')
hwVgmpGroupCfgPriPlusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgPriPlusValue.setStatus('current')
hwVgmpGroupCfgPreemptEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgPreemptEnable.setStatus('current')
hwVgmpGroupCfgPreemptDelayValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60000))).setUnits('milli-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgPreemptDelayValue.setStatus('current')
hwVgmpGroupCfgHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 60000))).setUnits('milli-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgHelloInterval.setStatus('current')
hwVgmpGroupCfgSendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgSendEnable.setStatus('current')
hwVgmpGroupCfgState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("nouse", 1), ("init", 2), ("master", 3), ("slave", 4), ("master2slave", 5), ("slave2master", 6), ("max", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgState.setStatus('current')
hwVgmpGroupCfgRunPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgRunPri.setStatus('current')
hwVgmpGroupCfgCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgCreateTime.setStatus('current')
hwVgmpGroupCfgLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgLastChangeTime.setStatus('current')
hwVgmpGroupCfgPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgPeerState.setStatus('current')
hwVgmpGroupCfgVrrpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgVrrpNum.setStatus('current')
hwVgmpGroupCfgReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("unused", 2))).clone('unused')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgReset.setStatus('current')
hwVgmpGroupCfgOperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpGroupCfgOperRowStatus.setStatus('current')
hwVgmpGroupCfgNextState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("nouse", 1), ("init", 2), ("master", 3), ("slave", 4), ("master2slave", 5), ("slave2master", 6), ("unknown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpGroupCfgNextState.setStatus('current')
hwVgmpMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2), )
if mibBuilder.loadTexts: hwVgmpMemberTable.setStatus('current')
hwVgmpMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1), ).setIndexNames((0, "HUAWEI-VGMP-MIB", "hwVgmpMemberIfIndex"), (0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"), (0, "HUAWEI-VGMP-MIB", "hwVgmpMemberVRID"))
if mibBuilder.loadTexts: hwVgmpMemberEntry.setStatus('current')
hwVgmpMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwVgmpMemberIfIndex.setStatus('current')
hwVgmpMemberVRID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwVgmpMemberVRID.setStatus('current')
hwVgmpMemberData = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpMemberData.setStatus('current')
hwVgmpMemberTran = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpMemberTran.setStatus('current')
hwVgmpMemberVrrpOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("peerDown", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpMemberVrrpOnline.setStatus('current')
hwVgmpMemberOperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpMemberOperRowStatus.setStatus('current')
hwVgmpTrackBFDTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3), )
if mibBuilder.loadTexts: hwVgmpTrackBFDTable.setStatus('current')
hwVgmpTrackBFDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1), ).setIndexNames((0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"), (0, "HUAWEI-VGMP-MIB", "hwVgmpTrackBFDID"))
if mibBuilder.loadTexts: hwVgmpTrackBFDEntry.setStatus('current')
hwVgmpTrackBFDID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191)))
if mibBuilder.loadTexts: hwVgmpTrackBFDID.setStatus('current')
hwVgmpTrackBFDReduceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpTrackBFDReduceValue.setStatus('current')
hwVgmpTrackBFDPreeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpTrackBFDPreeEnable.setStatus('current')
hwVgmpTrackBFDOperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVgmpTrackBFDOperRowStatus.setStatus('current')
hwVgmpStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1), )
if mibBuilder.loadTexts: hwVgmpStatisticTable.setStatus('current')
hwVgmpStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1), ).setIndexNames((0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"))
if mibBuilder.loadTexts: hwVgmpStatisticEntry.setStatus('current')
hwVgmpStatisticCheckFailDropNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticCheckFailDropNum.setStatus('current')
hwVgmpStatisticDisableDropNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticDisableDropNum.setStatus('current')
hwVgmpStatisticModeTypeErrDropNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticModeTypeErrDropNum.setStatus('current')
hwVgmpStatisticAccHelloREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccHelloREQ.setStatus('current')
hwVgmpStatisticSendHelloREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendHelloREQ.setStatus('current')
hwVgmpStatisticAccHelloACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccHelloACK.setStatus('current')
hwVgmpStatisticSendHelloACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendHelloACK.setStatus('current')
hwVgmpStatisticAccMasterToSlaveREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccMasterToSlaveREQ.setStatus('current')
hwVgmpStatisticSendMasterToSlaveREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendMasterToSlaveREQ.setStatus('current')
hwVgmpStatisticAccMasterToSlaveACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccMasterToSlaveACK.setStatus('current')
hwVgmpStatisticSendMasterToSlaveACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendMasterToSlaveACK.setStatus('current')
hwVgmpStatisticAccMasterToSlaveNACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccMasterToSlaveNACK.setStatus('current')
hwVgmpStatisticSendMasterToSlaveNACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendMasterToSlaveNACK.setStatus('current')
hwVgmpStatisticAccSlaveToMasterREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccSlaveToMasterREQ.setStatus('current')
hwVgmpStatisticSendSlaveToMasterREQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendSlaveToMasterREQ.setStatus('current')
hwVgmpStatisticAccSlaveToMasterACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccSlaveToMasterACK.setStatus('current')
hwVgmpStatisticSendSlaveToMasterACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendSlaveToMasterACK.setStatus('current')
hwVgmpStatisticAccSlaveToMasterNACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticAccSlaveToMasterNACK.setStatus('current')
hwVgmpStatisticSendSlaveToMasterNACK = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVgmpStatisticSendSlaveToMasterNACK.setStatus('current')
hwVGMPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1))
hwVGMPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1))
hwVGMPGroAttrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 1)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgEnable"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPri"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgUseVrrpPri"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPriPlusValue"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPreemptEnable"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPreemptDelayValue"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgHelloInterval"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgSendEnable"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgRunPri"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgCreateTime"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgLastChangeTime"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPeerState"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgVrrpNum"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgReset"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgOperRowStatus"), ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPGroAttrGroup = hwVGMPGroAttrGroup.setStatus('current')
hwVGMPMenAttrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 2)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpMemberData"), ("HUAWEI-VGMP-MIB", "hwVgmpMemberTran"), ("HUAWEI-VGMP-MIB", "hwVgmpMemberVrrpOnline"), ("HUAWEI-VGMP-MIB", "hwVgmpMemberOperRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPMenAttrGroup = hwVGMPMenAttrGroup.setStatus('current')
hwVGMPBFDSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 3)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDReduceValue"), ("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDPreeEnable"), ("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDOperRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPBFDSessionGroup = hwVGMPBFDSessionGroup.setStatus('current')
hwVGMPStaticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 4)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpStatisticCheckFailDropNum"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticDisableDropNum"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticModeTypeErrDropNum"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccHelloREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendHelloREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccHelloACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendHelloACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveNACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveNACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterREQ"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterNACK"), ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterNACK"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPStaticGroup = hwVGMPStaticGroup.setStatus('current')
hwVGMPGlobalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 5)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpTrapSnmpCtrl"), ("HUAWEI-VGMP-MIB", "hwVgmpStrictCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPGlobalsGroup = hwVGMPGlobalsGroup.setStatus('current')
hwVGMPNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 6)).setObjects(("HUAWEI-VGMP-MIB", "hwVgmpOtherStateToMaster"), ("HUAWEI-VGMP-MIB", "hwVgmpMasterToOtherState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVGMPNotificationGroup = hwVGMPNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-VGMP-MIB", vgmpGlobalCtrl=vgmpGlobalCtrl, vgmpNotifications=vgmpNotifications, hwVgmpGroupCfgRunPri=hwVgmpGroupCfgRunPri, hwVgmpStatisticAccSlaveToMasterACK=hwVgmpStatisticAccSlaveToMasterACK, hwVgmpStatisticSendMasterToSlaveNACK=hwVgmpStatisticSendMasterToSlaveNACK, hwVgmpGroupCfgNextState=hwVgmpGroupCfgNextState, hwVgmpStatisticSendSlaveToMasterREQ=hwVgmpStatisticSendSlaveToMasterREQ, hwVgmpGroupCfgPriPlusValue=hwVgmpGroupCfgPriPlusValue, hwVgmpGroupCfgCreateTime=hwVgmpGroupCfgCreateTime, PYSNMP_MODULE_ID=hwVgmpMib, hwVgmpGroupCfgReset=hwVgmpGroupCfgReset, hwVgmpMemberOperRowStatus=hwVgmpMemberOperRowStatus, hwVgmpStatisticAccHelloACK=hwVgmpStatisticAccHelloACK, vgmpStatistics=vgmpStatistics, hwVgmpGroupCfgPreemptDelayValue=hwVgmpGroupCfgPreemptDelayValue, hwVgmpGroupCfgEnable=hwVgmpGroupCfgEnable, hwVgmpGroupCfgHelloInterval=hwVgmpGroupCfgHelloInterval, hwVgmpTrackBFDReduceValue=hwVgmpTrackBFDReduceValue, hwVgmpStatisticAccHelloREQ=hwVgmpStatisticAccHelloREQ, hwVgmpGroupCfgPreemptEnable=hwVgmpGroupCfgPreemptEnable, hwVgmpMib=hwVgmpMib, hwVgmpTrackBFDTable=hwVgmpTrackBFDTable, hwVgmpStatisticAccMasterToSlaveACK=hwVgmpStatisticAccMasterToSlaveACK, hwVgmpStatisticAccSlaveToMasterNACK=hwVgmpStatisticAccSlaveToMasterNACK, hwVGMPBFDSessionGroup=hwVGMPBFDSessionGroup, hwVgmpTrackBFDOperRowStatus=hwVgmpTrackBFDOperRowStatus, hwVGMPStaticGroup=hwVGMPStaticGroup, hwVGMPMIBCompliances=hwVGMPMIBCompliances, hwVgmpGroupCfgPeerState=hwVgmpGroupCfgPeerState, hwVgmpStatisticSendSlaveToMasterACK=hwVgmpStatisticSendSlaveToMasterACK, vgmpConformance=vgmpConformance, hwVgmpGroupCfgID=hwVgmpGroupCfgID, hwVgmpMemberVRID=hwVgmpMemberVRID, hwVgmpStrictCheck=hwVgmpStrictCheck, hwVgmpGroupCfgTable=hwVgmpGroupCfgTable, hwVgmpStatisticAccMasterToSlaveNACK=hwVgmpStatisticAccMasterToSlaveNACK, hwVGMPGroAttrGroup=hwVGMPGroAttrGroup, hwVgmpTrackBFDEntry=hwVgmpTrackBFDEntry, hwVgmpStatisticSendHelloACK=hwVgmpStatisticSendHelloACK, hwVgmpGroupCfgVrrpNum=hwVgmpGroupCfgVrrpNum, hwVgmpStatisticSendMasterToSlaveREQ=hwVgmpStatisticSendMasterToSlaveREQ, hwVGMPMenAttrGroup=hwVGMPMenAttrGroup, hwVgmpStatisticEntry=hwVgmpStatisticEntry, hwVgmpGroupCfgState=hwVgmpGroupCfgState, hwVgmpStatisticSendMasterToSlaveACK=hwVgmpStatisticSendMasterToSlaveACK, hwVGMPGlobalsGroup=hwVGMPGlobalsGroup, hwVgmpTrackBFDPreeEnable=hwVgmpTrackBFDPreeEnable, hwVgmpStatisticDisableDropNum=hwVgmpStatisticDisableDropNum, hwVgmpMemberTable=hwVgmpMemberTable, hwVgmpStatisticAccMasterToSlaveREQ=hwVgmpStatisticAccMasterToSlaveREQ, hwVgmpMemberIfIndex=hwVgmpMemberIfIndex, hwVgmpStatisticSendHelloREQ=hwVgmpStatisticSendHelloREQ, hwVGMPMIBGroups=hwVGMPMIBGroups, hwVgmpMemberData=hwVgmpMemberData, vgmpOperations=vgmpOperations, hwVgmpMemberEntry=hwVgmpMemberEntry, hwVgmpMasterToOtherState=hwVgmpMasterToOtherState, hwVgmpGroupCfgSendEnable=hwVgmpGroupCfgSendEnable, hwVgmpGroupCfgOperRowStatus=hwVgmpGroupCfgOperRowStatus, hwVGMPNotificationGroup=hwVGMPNotificationGroup, hwVgmpMemberVrrpOnline=hwVgmpMemberVrrpOnline, hwVgmpStatisticAccSlaveToMasterREQ=hwVgmpStatisticAccSlaveToMasterREQ, hwVgmpMemberTran=hwVgmpMemberTran, hwVgmpGroupCfgUseVrrpPri=hwVgmpGroupCfgUseVrrpPri, hwVgmpStatisticSendSlaveToMasterNACK=hwVgmpStatisticSendSlaveToMasterNACK, hwVgmpStatisticCheckFailDropNum=hwVgmpStatisticCheckFailDropNum, hwVgmpStatisticModeTypeErrDropNum=hwVgmpStatisticModeTypeErrDropNum, hwVgmpTrapSnmpCtrl=hwVgmpTrapSnmpCtrl, hwVgmpGroupCfgEntry=hwVgmpGroupCfgEntry, hwVgmpGroupCfgPri=hwVgmpGroupCfgPri, hwVgmpOtherStateToMaster=hwVgmpOtherStateToMaster, hwVgmpStatisticTable=hwVgmpStatisticTable, hwVgmpTrackBFDID=hwVgmpTrackBFDID, hwVgmpGroupCfgLastChangeTime=hwVgmpGroupCfgLastChangeTime)
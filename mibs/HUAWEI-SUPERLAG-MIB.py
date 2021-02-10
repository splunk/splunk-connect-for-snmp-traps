#
# PySNMP MIB module HUAWEI-SUPERLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SUPERLAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
huaweiMgmt, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, Integer32, Bits, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Integer32", "Bits", "iso", "Counter64")
DisplayString, PhysAddress, TextualConvention, TruthValue, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention", "TruthValue", "RowStatus", "TimeStamp")
hwSuperLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178))
if mibBuilder.loadTexts: hwSuperLagMIB.setLastUpdated('200810211010Z')
if mibBuilder.loadTexts: hwSuperLagMIB.setOrganization('Organization.')
hwDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwSuperLagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1))
hwSuperLagTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1), )
if mibBuilder.loadTexts: hwSuperLagTable.setStatus('current')
hwSuperLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1), ).setIndexNames((0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagId"))
if mibBuilder.loadTexts: hwSuperLagEntry.setStatus('current')
hwSuperLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSuperLagId.setStatus('current')
hwSuperLagSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagSystemId.setStatus('current')
hwSuperLagPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagPri.setStatus('current')
hwSuperLagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagStatus.setStatus('current')
hwSuperLagStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("pri", 1), ("timeout", 2), ("bfdDown", 3), ("peerTimeout", 4), ("peerBfdDown", 5), ("allMemberDown", 6), ("init", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagStatusReason.setStatus('current')
hwSuperLagPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagPeerIpAddr.setStatus('current')
hwSuperLagSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSourceIpAddr.setStatus('current')
hwSuperLagReceiveFailTimeMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagReceiveFailTimeMultiple.setStatus('current')
hwSuperLagSendPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSendPeriod.setStatus('current')
hwSuperLagPacketReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketReceive.setStatus('current')
hwSuperLagPacketSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketSend.setStatus('current')
hwSuperLagPacketRecDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketRecDrop.setStatus('current')
hwSuperLagPacketSndDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketSndDrop.setStatus('current')
hwSuperLagPeerSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerSystemId.setStatus('current')
hwSuperLagPeerPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerPri.setStatus('current')
hwSuperLagPeerReceiveFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerReceiveFailTime.setStatus('current')
hwSuperLagSecurityKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSecurityKeyType.setStatus('current')
hwSuperLagSecurityKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSecurityKey.setStatus('current')
hwSuperLagBfdSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagBfdSessId.setStatus('current')
hwSuperLagResetCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagResetCounter.setStatus('current')
hwSuperLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagRowStatus.setStatus('current')
hwSuperLagMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2), )
if mibBuilder.loadTexts: hwSuperLagMemberTable.setStatus('current')
hwSuperLagMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1), ).setIndexNames((0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberParentSuperLagId"), (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberType"), (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberId"))
if mibBuilder.loadTexts: hwSuperLagMemberEntry.setStatus('current')
hwSuperLagMemberParentSuperLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSuperLagMemberParentSuperLagId.setStatus('current')
hwSuperLagMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwSuperLagMemberType.setStatus('current')
hwSuperLagMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwSuperLagMemberId.setStatus('current')
hwSuperLagMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberStatus.setStatus('current')
hwSuperLagMemberStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("forceBackup", 1), ("forceMaster", 2), ("suplagInit", 3), ("suplagBackup", 4), ("suplagMaster", 5), ("peerMemberDown", 6), ("peerMemberUp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberStatusReason.setStatus('current')
hwSuperLagMemberWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("forceBackup", 2), ("forceMaster", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagMemberWorkMode.setStatus('current')
hwSuperLagMemberLocaPhylLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberLocaPhylLinkStatus.setStatus('current')
hwSuperLagMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagMemberRowStatus.setStatus('current')
hwSuperLagTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2))
hwSuperLagStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"))
if mibBuilder.loadTexts: hwSuperLagStatusChange.setStatus('current')
hwSuperLagMemberStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"))
if mibBuilder.loadTexts: hwSuperLagMemberStatusChange.setStatus('current')
hwSuperLagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3))
hwSuperLagCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1))
hwSuperLagFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagGroup"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberGroup"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagFullCompliance = hwSuperLagFullCompliance.setStatus('current')
hwSuperLagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2))
hwSuperLagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagSystemId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPri"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerIpAddr"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSourceIpAddr"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagReceiveFailTimeMultiple"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSendPeriod"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketReceive"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSend"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketRecDrop"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSndDrop"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerSystemId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerPri"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerReceiveFailTime"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKeyType"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKey"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagBfdSessId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagResetCounter"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagGroup = hwSuperLagGroup.setStatus('current')
hwSuperLagMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberWorkMode"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberLocaPhylLinkStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagMemberGroup = hwSuperLagMemberGroup.setStatus('current')
hwSuperLagNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusChange"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagNotificationGroup = hwSuperLagNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SUPERLAG-MIB", hwSuperLagFullCompliance=hwSuperLagFullCompliance, hwSuperLagSendPeriod=hwSuperLagSendPeriod, hwSuperLagStatusChange=hwSuperLagStatusChange, hwSuperLagMemberStatusChange=hwSuperLagMemberStatusChange, hwSuperLagNotificationGroup=hwSuperLagNotificationGroup, hwSuperLagBfdSessId=hwSuperLagBfdSessId, hwSuperLagMemberEntry=hwSuperLagMemberEntry, hwSuperLagStatusReason=hwSuperLagStatusReason, hwSuperLagGroups=hwSuperLagGroups, hwSuperLagMemberWorkMode=hwSuperLagMemberWorkMode, hwSuperLagPacketReceive=hwSuperLagPacketReceive, hwSuperLagPeerSystemId=hwSuperLagPeerSystemId, hwSuperLagRowStatus=hwSuperLagRowStatus, hwSuperLagMIB=hwSuperLagMIB, hwSuperLagReceiveFailTimeMultiple=hwSuperLagReceiveFailTimeMultiple, hwSuperLagPeerReceiveFailTime=hwSuperLagPeerReceiveFailTime, hwSuperLagId=hwSuperLagId, hwSuperLagMemberStatusReason=hwSuperLagMemberStatusReason, hwDatacomm=hwDatacomm, hwSuperLagSystemId=hwSuperLagSystemId, hwSuperLagPeerPri=hwSuperLagPeerPri, hwSuperLagMemberId=hwSuperLagMemberId, hwSuperLagPri=hwSuperLagPri, hwSuperLagMemberRowStatus=hwSuperLagMemberRowStatus, hwSuperLagPacketSndDrop=hwSuperLagPacketSndDrop, hwSuperLagMemberType=hwSuperLagMemberType, hwSuperLagMemberLocaPhylLinkStatus=hwSuperLagMemberLocaPhylLinkStatus, hwSuperLagObjects=hwSuperLagObjects, hwSuperLagPeerIpAddr=hwSuperLagPeerIpAddr, hwSuperLagSecurityKeyType=hwSuperLagSecurityKeyType, hwSuperLagTable=hwSuperLagTable, hwSuperLagMemberParentSuperLagId=hwSuperLagMemberParentSuperLagId, hwSuperLagPacketSend=hwSuperLagPacketSend, hwSuperLagPacketRecDrop=hwSuperLagPacketRecDrop, hwSuperLagMemberGroup=hwSuperLagMemberGroup, hwSuperLagCompliances=hwSuperLagCompliances, hwSuperLagMemberTable=hwSuperLagMemberTable, hwSuperLagSourceIpAddr=hwSuperLagSourceIpAddr, hwSuperLagStatus=hwSuperLagStatus, hwSuperLagEntry=hwSuperLagEntry, hwSuperLagMemberStatus=hwSuperLagMemberStatus, hwSuperLagTraps=hwSuperLagTraps, hwSuperLagConformance=hwSuperLagConformance, PYSNMP_MODULE_ID=hwSuperLagMIB, hwSuperLagGroup=hwSuperLagGroup, hwSuperLagResetCounter=hwSuperLagResetCounter, hwSuperLagSecurityKey=hwSuperLagSecurityKey)

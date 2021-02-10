#
# PySNMP MIB module ELTEX-MES-BRIDGE-ERPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-BRIDGE-ERPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
eltMesBridgeExtMIBObjects, = mibBuilder.importSymbols("ELTEX-MES-BRIDGE-EXT-MIB", "eltMesBridgeExtMIBObjects")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Integer32, Counter64, MibIdentifier, TimeTicks, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Gauge32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Bits", "IpAddress")
TruthValue, RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
eltMesErpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1))
eltMesErpsMIB.setRevisions(('2015-11-19 00:00',))
if mibBuilder.loadTexts: eltMesErpsMIB.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesErpsMIB.setOrganization('Eltex Ltd.')
eltMesErpsCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1))
eltMesErpsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 2))
eltMesErpsMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3))
eltMesErpsNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4))
class EltErpsEnabledState(TextualConvention, Integer32):
    reference = 'ITU-T G.8032'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class EltErpsMgmtRAPSPortState(TextualConvention, Integer32):
    reference = 'ITU-T G.8032'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fowarding", 1), ("blocking", 2), ("signal-fail", 3), ("manual-switch", 4), ("forced-switch", 5))

class EltErpsMgmtRAPSPortId(TextualConvention, Integer32):
    reference = 'ITU-T G.8032'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("west", 2), ("east", 3))

eltErpsAdminState = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 1), EltErpsEnabledState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsAdminState.setStatus('deprecated')
eltErpsLogState = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 2), EltErpsEnabledState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsLogState.setStatus('deprecated')
eltErpsTrapState = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 3), EltErpsEnabledState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsTrapState.setStatus('deprecated')
eltErpsPendingAction = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyPendingActive", 1), ("copyActivePending", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsPendingAction.setStatus('deprecated')
eltErpsPendingActionVlan = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsPendingActionVlan.setStatus('deprecated')
eltErpsGetConfigId = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("pending", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsGetConfigId.setStatus('deprecated')
eltErpsMgmtRAPSVlanTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1), )
if mibBuilder.loadTexts: eltErpsMgmtRAPSVlanTable.setStatus('deprecated')
eltErpsMgmtRAPSVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1), ).setIndexNames((0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtRAPSVlanId"))
if mibBuilder.loadTexts: eltErpsMgmtRAPSVlanEntry.setStatus('deprecated')
eltErpsMgmtRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltErpsMgmtRAPSVlanId.setStatus('deprecated')
eltErpsMgmtRAPSWestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSWestPort.setStatus('deprecated')
eltErpsMgmtRAPSWestPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 3), EltErpsMgmtRAPSPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltErpsMgmtRAPSWestPortState.setStatus('deprecated')
eltErpsMgmtRAPSEastPort = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSEastPort.setStatus('deprecated')
eltErpsMgmtRAPSEastPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 5), EltErpsMgmtRAPSPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltErpsMgmtRAPSEastPortState.setStatus('deprecated')
eltErpsMgmtRAPSRPLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 6), EltErpsMgmtRAPSPortId().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRPLPort.setStatus('deprecated')
eltErpsMgmtRAPSRPLOwnerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 7), EltErpsEnabledState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRPLOwnerAdminState.setStatus('deprecated')
eltErpsMgmtRAPSRingMEL = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRingMEL.setStatus('deprecated')
eltErpsMgmtRAPSHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSHoldOffTime.setStatus('deprecated')
eltErpsMgmtRAPSGuardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSGuardTime.setStatus('deprecated')
eltErpsMgmtRAPSWTRTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSWTRTime.setStatus('deprecated')
eltErpsMgmtRAPSRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("init", 1), ("idle", 2), ("protection", 3), ("manual-switch", 4), ("forced-switch", 5), ("pending", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRingState.setStatus('deprecated')
eltErpsMgmtRAPSRingAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 13), EltErpsEnabledState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRingAdminState.setStatus('deprecated')
eltErpsMgmtRAPSRPLOwnerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRPLOwnerOperStatus.setStatus('deprecated')
eltErpsMgmtRAPSProtectionVlanRangeList1to1024 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSProtectionVlanRangeList1to1024.setStatus('deprecated')
eltErpsMgmtRAPSProtectionVlanRangeList1025to2048 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSProtectionVlanRangeList1025to2048.setStatus('deprecated')
eltErpsMgmtRAPSProtectionVlanRangeList2049to3072 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSProtectionVlanRangeList2049to3072.setStatus('deprecated')
eltErpsMgmtRAPSProtectionVlanRangeList3073to4094 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSProtectionVlanRangeList3073to4094.setStatus('deprecated')
eltErpsMgmtRAPSRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 19), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRevertive.setStatus('deprecated')
eltErpsMgmtRAPSProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSProtocolVersion.setStatus('deprecated')
eltErpsMgmtRAPSPortForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 21), EltErpsMgmtRAPSPortId().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSPortForcedSwitch.setStatus('deprecated')
eltErpsMgmtRAPSPortManualSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 22), EltErpsMgmtRAPSPortId().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtRAPSPortManualSwitch.setStatus('deprecated')
eltErpsMgmtRAPSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 23), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltErpsMgmtRAPSRowStatus.setStatus('deprecated')
eltErpsMgmtSubRingCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2), )
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlTable.setStatus('deprecated')
eltErpsMgmtSubRingCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1), ).setIndexNames((0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtSubRingCtrlRAPSVlanId"), (0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtSubRingCtrlSubRingRAPSVlanId"))
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlEntry.setStatus('deprecated')
eltErpsMgmtSubRingCtrlRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlRAPSVlanId.setStatus('deprecated')
eltErpsMgmtSubRingCtrlSubRingRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlSubRingRAPSVlanId.setStatus('deprecated')
eltErpsMgmtSubRingCtrlTCPropagationState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 3), EltErpsEnabledState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlTCPropagationState.setStatus('deprecated')
eltErpsMgmtSubRingCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltErpsMgmtSubRingCtrlRowStatus.setStatus('deprecated')
eltMesErpsNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0))
eltErpsSFDetectedTrap = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 1)).setObjects(("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId"))
if mibBuilder.loadTexts: eltErpsSFDetectedTrap.setStatus('deprecated')
eltErpsSFClearedTrap = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 2)).setObjects(("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId"))
if mibBuilder.loadTexts: eltErpsSFClearedTrap.setStatus('deprecated')
eltErpsRPLOwnerConflictTrap = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 3)).setObjects(("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId"))
if mibBuilder.loadTexts: eltErpsRPLOwnerConflictTrap.setStatus('deprecated')
eltMesErpsNotificationBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 2))
eltErpsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 2, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eltErpsNodeId.setStatus('deprecated')
mibBuilder.exportSymbols("ELTEX-MES-BRIDGE-ERPS-MIB", EltErpsMgmtRAPSPortState=EltErpsMgmtRAPSPortState, eltErpsMgmtSubRingCtrlRAPSVlanId=eltErpsMgmtSubRingCtrlRAPSVlanId, EltErpsEnabledState=EltErpsEnabledState, eltErpsMgmtRAPSEastPort=eltErpsMgmtRAPSEastPort, eltErpsMgmtRAPSPortForcedSwitch=eltErpsMgmtRAPSPortForcedSwitch, eltErpsMgmtRAPSRingAdminState=eltErpsMgmtRAPSRingAdminState, eltErpsSFDetectedTrap=eltErpsSFDetectedTrap, eltErpsMgmtRAPSRowStatus=eltErpsMgmtRAPSRowStatus, EltErpsMgmtRAPSPortId=EltErpsMgmtRAPSPortId, eltErpsMgmtRAPSVlanEntry=eltErpsMgmtRAPSVlanEntry, eltErpsMgmtSubRingCtrlRowStatus=eltErpsMgmtSubRingCtrlRowStatus, eltMesErpsMgmt=eltMesErpsMgmt, eltErpsMgmtRAPSRPLOwnerOperStatus=eltErpsMgmtRAPSRPLOwnerOperStatus, eltErpsMgmtRAPSEastPortState=eltErpsMgmtRAPSEastPortState, eltErpsMgmtRAPSWestPortState=eltErpsMgmtRAPSWestPortState, eltMesErpsNotificationBindings=eltMesErpsNotificationBindings, eltErpsNodeId=eltErpsNodeId, eltErpsMgmtRAPSVlanTable=eltErpsMgmtRAPSVlanTable, eltMesErpsMIB=eltMesErpsMIB, eltErpsAdminState=eltErpsAdminState, eltErpsTrapState=eltErpsTrapState, eltErpsMgmtRAPSRPLPort=eltErpsMgmtRAPSRPLPort, eltMesErpsNotifyPrefix=eltMesErpsNotifyPrefix, eltErpsMgmtRAPSProtectionVlanRangeList3073to4094=eltErpsMgmtRAPSProtectionVlanRangeList3073to4094, eltErpsMgmtRAPSRPLOwnerAdminState=eltErpsMgmtRAPSRPLOwnerAdminState, eltErpsMgmtRAPSVlanId=eltErpsMgmtRAPSVlanId, eltErpsMgmtRAPSProtocolVersion=eltErpsMgmtRAPSProtocolVersion, eltMesErpsInfo=eltMesErpsInfo, eltErpsMgmtRAPSWTRTime=eltErpsMgmtRAPSWTRTime, eltErpsMgmtSubRingCtrlEntry=eltErpsMgmtSubRingCtrlEntry, eltMesErpsCtrl=eltMesErpsCtrl, eltErpsMgmtSubRingCtrlTable=eltErpsMgmtSubRingCtrlTable, eltErpsSFClearedTrap=eltErpsSFClearedTrap, eltErpsMgmtSubRingCtrlSubRingRAPSVlanId=eltErpsMgmtSubRingCtrlSubRingRAPSVlanId, eltErpsMgmtRAPSProtectionVlanRangeList1to1024=eltErpsMgmtRAPSProtectionVlanRangeList1to1024, eltErpsMgmtRAPSProtectionVlanRangeList1025to2048=eltErpsMgmtRAPSProtectionVlanRangeList1025to2048, eltErpsMgmtSubRingCtrlTCPropagationState=eltErpsMgmtSubRingCtrlTCPropagationState, eltErpsRPLOwnerConflictTrap=eltErpsRPLOwnerConflictTrap, eltErpsPendingAction=eltErpsPendingAction, eltErpsMgmtRAPSRingState=eltErpsMgmtRAPSRingState, eltErpsMgmtRAPSRevertive=eltErpsMgmtRAPSRevertive, eltErpsPendingActionVlan=eltErpsPendingActionVlan, eltErpsMgmtRAPSHoldOffTime=eltErpsMgmtRAPSHoldOffTime, eltErpsMgmtRAPSGuardTime=eltErpsMgmtRAPSGuardTime, PYSNMP_MODULE_ID=eltMesErpsMIB, eltErpsMgmtRAPSProtectionVlanRangeList2049to3072=eltErpsMgmtRAPSProtectionVlanRangeList2049to3072, eltErpsGetConfigId=eltErpsGetConfigId, eltErpsMgmtRAPSWestPort=eltErpsMgmtRAPSWestPort, eltErpsLogState=eltErpsLogState, eltMesErpsNotify=eltMesErpsNotify, eltErpsMgmtRAPSPortManualSwitch=eltErpsMgmtRAPSPortManualSwitch, eltErpsMgmtRAPSRingMEL=eltErpsMgmtRAPSRingMEL)

#
# PySNMP MIB module RBN-SSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-SSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
IANAItuProbableCause, IANAItuEventType = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuProbableCause", "IANAItuEventType")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnPercentage, RbnSlot = mibBuilder.importSymbols("RBN-TC", "RbnPercentage", "RbnSlot")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, iso, Counter64, MibIdentifier, NotificationType, Counter32, TimeTicks, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter64", "MibIdentifier", "NotificationType", "Counter32", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Bits")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
rbnSseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 48))
rbnSseMIB.setRevisions(('2009-09-01 00:00',))
if mibBuilder.loadTexts: rbnSseMIB.setLastUpdated('200909010000Z')
if mibBuilder.loadTexts: rbnSseMIB.setOrganization('RedBack Networks, Inc.')
rbnSseMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0))
rbnSseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1))
rbnSseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2))
rbnFSGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1), )
if mibBuilder.loadTexts: rbnFSGroupTable.setStatus('current')
rbnFSGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1), ).setIndexNames((0, "RBN-SSE-MIB", "rbnFSGroupName"))
if mibBuilder.loadTexts: rbnFSGroupEntry.setStatus('current')
rbnFSGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: rbnFSGroupName.setStatus('current')
rbnFSGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("partial", 3), ("stale", 4), ("noCard", 5), ("unassigned", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSGroupState.setStatus('current')
rbnFSGroupMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("diskRedundancy", 1), ("networkRedundancy", 2), ("nonRedundant", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSGroupMode.setStatus('current')
rbnFSGroupRaidMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("raid0", 1), ("raid1", 2), ("independent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSGroupRaidMode.setStatus('current')
rbnFSGroupRevert = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 5), TruthValue().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSGroupRevert.setStatus('current')
rbnFSPrimarySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 6), RbnSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPrimarySlot.setStatus('current')
rbnFSSecondarySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 7), RbnSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSSecondarySlot.setStatus('current')
rbnFSActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 8), RbnSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSActiveSlot.setStatus('current')
rbnFSPartitionTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2), )
if mibBuilder.loadTexts: rbnFSPartitionTable.setStatus('current')
rbnFSPartitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1), ).setIndexNames((0, "RBN-SSE-MIB", "rbnFSGroupName"), (0, "RBN-SSE-MIB", "rbnFSPartitionName"))
if mibBuilder.loadTexts: rbnFSPartitionEntry.setStatus('current')
rbnFSPartitionName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: rbnFSPartitionName.setStatus('current')
rbnFSPartitionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("stale", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionState.setStatus('current')
rbnFSPartitionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('GBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionSize.setStatus('current')
rbnFSPartitionDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionDisk.setStatus('current')
rbnFSPartitionMirrored = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionMirrored.setStatus('current')
rbnFSPartitionRaiseTriggerPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 6), RbnPercentage().subtype(subtypeSpec=ValueRangeConstraint(50, 100)).clone(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionRaiseTriggerPercentage.setStatus('current')
rbnFSPartitionClearTriggerPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 7), RbnPercentage().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(70)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFSPartitionClearTriggerPercentage.setStatus('current')
rbnSseAlarmDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnSseAlarmDateAndTime.setStatus('current')
rbnSseAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 4), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnSseAlarmSeverity.setStatus('current')
rbnSseAlarmProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 5), IANAItuProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnSseAlarmProbableCause.setStatus('current')
rbnSseEventType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 6), IANAItuEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnSseEventType.setStatus('current')
rbnSseAlarmDescription = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnSseAlarmDescription.setStatus('current')
rbnSseFsgSwitchManual = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 1)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgSwitchManual.setStatus('current')
rbnSseFsgSwitchAuto = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 2)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgSwitchAuto.setStatus('current')
rbnSseFsgSwitchCompleted = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 3)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgSwitchCompleted.setStatus('current')
rbnSseFsgSwitchFail = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 4)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgSwitchFail.setStatus('current')
rbnSseFsgSwitchWtr = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 5)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgSwitchWtr.setStatus('current')
rbnSseFsgNotOperational = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 6)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgNotOperational.setStatus('current')
rbnSseFsgBlockDeviceFail = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 7)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSGroupState"))
if mibBuilder.loadTexts: rbnSseFsgBlockDeviceFail.setStatus('current')
rbnSseFsgPartitionNotOperational = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 8)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgPartitionNotOperational.setStatus('current')
rbnSseFsgParitionDataSyncing = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 9)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgParitionDataSyncing.setStatus('current')
rbnSseFsgParitionDataSyncFail = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 10)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgParitionDataSyncFail.setStatus('current')
rbnSseFsgPartitionFull = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 11)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgPartitionFull.setStatus('current')
rbnSseFsgPartitionLow = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 12)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgPartitionLow.setStatus('current')
rbnSseFsgPartitionNotOperStandby = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 13)).setObjects(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnFSPartitionState"))
if mibBuilder.loadTexts: rbnSseFsgPartitionNotOperStandby.setStatus('current')
rbnSseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1))
rbnSseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 2))
rbnSseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 2, 1)).setObjects(("RBN-SSE-MIB", "rbnSseFileServerGroup"), ("RBN-SSE-MIB", "rbnSsePartitionGroup"), ("RBN-SSE-MIB", "rbnSseEventObjectGroup"), ("RBN-SSE-MIB", "rbnSseEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSseMIBCompliance = rbnSseMIBCompliance.setStatus('current')
rbnSseFileServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 1)).setObjects(("RBN-SSE-MIB", "rbnFSGroupMode"), ("RBN-SSE-MIB", "rbnFSGroupState"), ("RBN-SSE-MIB", "rbnFSGroupRaidMode"), ("RBN-SSE-MIB", "rbnFSGroupRevert"), ("RBN-SSE-MIB", "rbnFSPrimarySlot"), ("RBN-SSE-MIB", "rbnFSSecondarySlot"), ("RBN-SSE-MIB", "rbnFSActiveSlot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSseFileServerGroup = rbnSseFileServerGroup.setStatus('current')
rbnSsePartitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 2)).setObjects(("RBN-SSE-MIB", "rbnFSPartitionSize"), ("RBN-SSE-MIB", "rbnFSPartitionState"), ("RBN-SSE-MIB", "rbnFSPartitionDisk"), ("RBN-SSE-MIB", "rbnFSPartitionMirrored"), ("RBN-SSE-MIB", "rbnFSPartitionRaiseTriggerPercentage"), ("RBN-SSE-MIB", "rbnFSPartitionClearTriggerPercentage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSsePartitionGroup = rbnSsePartitionGroup.setStatus('current')
rbnSseEventObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 3)).setObjects(("RBN-SSE-MIB", "rbnSseEventType"), ("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"), ("RBN-SSE-MIB", "rbnSseAlarmDescription"), ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"), ("RBN-SSE-MIB", "rbnSseAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSseEventObjectGroup = rbnSseEventObjectGroup.setStatus('current')
rbnSseEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 4)).setObjects(("RBN-SSE-MIB", "rbnSseFsgSwitchManual"), ("RBN-SSE-MIB", "rbnSseFsgSwitchAuto"), ("RBN-SSE-MIB", "rbnSseFsgSwitchCompleted"), ("RBN-SSE-MIB", "rbnSseFsgSwitchFail"), ("RBN-SSE-MIB", "rbnSseFsgSwitchWtr"), ("RBN-SSE-MIB", "rbnSseFsgNotOperational"), ("RBN-SSE-MIB", "rbnSseFsgBlockDeviceFail"), ("RBN-SSE-MIB", "rbnSseFsgPartitionNotOperational"), ("RBN-SSE-MIB", "rbnSseFsgParitionDataSyncing"), ("RBN-SSE-MIB", "rbnSseFsgParitionDataSyncFail"), ("RBN-SSE-MIB", "rbnSseFsgPartitionFull"), ("RBN-SSE-MIB", "rbnSseFsgPartitionLow"), ("RBN-SSE-MIB", "rbnSseFsgPartitionNotOperStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSseEventGroup = rbnSseEventGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-SSE-MIB", rbnSseAlarmProbableCause=rbnSseAlarmProbableCause, PYSNMP_MODULE_ID=rbnSseMIB, rbnSseFsgPartitionFull=rbnSseFsgPartitionFull, rbnSseFsgPartitionLow=rbnSseFsgPartitionLow, rbnFSPrimarySlot=rbnFSPrimarySlot, rbnSseFsgNotOperational=rbnSseFsgNotOperational, rbnSseFsgBlockDeviceFail=rbnSseFsgBlockDeviceFail, rbnSseMIBConformance=rbnSseMIBConformance, rbnFSPartitionDisk=rbnFSPartitionDisk, rbnFSPartitionRaiseTriggerPercentage=rbnFSPartitionRaiseTriggerPercentage, rbnSseAlarmDateAndTime=rbnSseAlarmDateAndTime, rbnFSGroupRevert=rbnFSGroupRevert, rbnSseFsgParitionDataSyncFail=rbnSseFsgParitionDataSyncFail, rbnSseFsgParitionDataSyncing=rbnSseFsgParitionDataSyncing, rbnFSPartitionMirrored=rbnFSPartitionMirrored, rbnFSActiveSlot=rbnFSActiveSlot, rbnSsePartitionGroup=rbnSsePartitionGroup, rbnSseAlarmSeverity=rbnSseAlarmSeverity, rbnFSPartitionName=rbnFSPartitionName, rbnFSPartitionSize=rbnFSPartitionSize, rbnSseMIBNotifications=rbnSseMIBNotifications, rbnSseFsgPartitionNotOperStandby=rbnSseFsgPartitionNotOperStandby, rbnSseFileServerGroup=rbnSseFileServerGroup, rbnSseEventType=rbnSseEventType, rbnFSPartitionState=rbnFSPartitionState, rbnFSPartitionTable=rbnFSPartitionTable, rbnSseFsgSwitchFail=rbnSseFsgSwitchFail, rbnSseFsgSwitchWtr=rbnSseFsgSwitchWtr, rbnSseFsgPartitionNotOperational=rbnSseFsgPartitionNotOperational, rbnSseMIBCompliance=rbnSseMIBCompliance, rbnFSGroupEntry=rbnFSGroupEntry, rbnSseMIBObjects=rbnSseMIBObjects, rbnSseAlarmDescription=rbnSseAlarmDescription, rbnFSPartitionClearTriggerPercentage=rbnFSPartitionClearTriggerPercentage, rbnFSGroupMode=rbnFSGroupMode, rbnFSGroupState=rbnFSGroupState, rbnSseFsgSwitchAuto=rbnSseFsgSwitchAuto, rbnFSSecondarySlot=rbnFSSecondarySlot, rbnFSGroupRaidMode=rbnFSGroupRaidMode, rbnSseGroups=rbnSseGroups, rbnFSGroupName=rbnFSGroupName, rbnSseEventObjectGroup=rbnSseEventObjectGroup, rbnFSGroupTable=rbnFSGroupTable, rbnSseCompliances=rbnSseCompliances, rbnSseEventGroup=rbnSseEventGroup, rbnFSPartitionEntry=rbnFSPartitionEntry, rbnSseFsgSwitchCompleted=rbnSseFsgSwitchCompleted, rbnSseFsgSwitchManual=rbnSseFsgSwitchManual, rbnSseMIB=rbnSseMIB)

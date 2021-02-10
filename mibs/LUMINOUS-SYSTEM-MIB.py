#
# PySNMP MIB module LUMINOUS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
LumDescr, LumSimpleIndex, LumResetCmd, LumSlotNum, LumPortNum, LumAlarmSeverity, LumCardBaseType, LumSignalState, LumVersionString, LumName, LumAdminStatus, LumOperStatus = mibBuilder.importSymbols("LUMINOUS-TC-MIB", "LumDescr", "LumSimpleIndex", "LumResetCmd", "LumSlotNum", "LumPortNum", "LumAlarmSeverity", "LumCardBaseType", "LumSignalState", "LumVersionString", "LumName", "LumAdminStatus", "LumOperStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Bits, MibIdentifier, Counter64, Gauge32, ObjectIdentity, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, enterprises, Unsigned32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Bits", "MibIdentifier", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "enterprises", "Unsigned32", "ObjectName")
RowStatus, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 4))
lumSystemMIB.setRevisions(('1901-06-27 00:00', '1901-05-24 00:00', '1900-10-16 00:00',))
if mibBuilder.loadTexts: lumSystemMIB.setLastUpdated('0007250000Z')
if mibBuilder.loadTexts: lumSystemMIB.setOrganization('Luminous Networks')
lumSoftwareDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1))
lumSystemReset = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2))
lumAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3))
lumAlarmType = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1))
lumAlarmSource = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2))
lumAlarmLog = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4))
lumAlarmSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5))
lumAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 10))
lumAlarmV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0))
lumDownLoadImageType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 1), LumCardBaseType().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadImageType.setStatus('current')
lumDownLoadHost = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadHost.setStatus('current')
lumDownLoadUsrName = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadUsrName.setStatus('current')
lumDownLoadPasswd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadPasswd.setStatus('current')
lumDownLoadFilePath = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadFilePath.setStatus('current')
lumDownLoadVersion = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 6), LumVersionString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadVersion.setStatus('current')
lumDownLoadSlot = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 7), LumSlotNum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadSlot.setStatus('current')
lumDownLoadTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 8), Integer32().clone(10)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadTimeOut.setStatus('current')
lumDownLoadCmd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("download", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadCmd.setStatus('current')
lumDownLoadStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("download-in-progress", 2), ("download-succeeded", 3), ("download-failed", 4))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumDownLoadStatus.setStatus('current')
lumDownLoadAbort = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("abort", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadAbort.setStatus('current')
lumSystemResetCardTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1), )
if mibBuilder.loadTexts: lumSystemResetCardTable.setStatus('deprecated')
lumSystemResetCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumSystemResetCardIndex"))
if mibBuilder.loadTexts: lumSystemResetCardEntry.setStatus('deprecated')
lumSystemResetCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 1), LumSlotNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumSystemResetCardIndex.setStatus('deprecated')
lumSystemResetCardCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 2), LumResetCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumSystemResetCardCmd.setStatus('deprecated')
lumSystemResetShelfCmd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 2), LumResetCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumSystemResetShelfCmd.setStatus('deprecated')
lumProvisionAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("provCardFailedNoBackup", 1), ("provCardFailedWithBackup", 2))))
if mibBuilder.loadTexts: lumProvisionAlarmType.setStatus('current')
lumAlarmCardAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("input0", 1), ("input1", 2), ("input2", 3), ("input3", 4), ("input4", 5), ("input5", 6), ("input6", 7), ("input7", 8), ("alarmCardFailedNoBackup", 9), ("alarmCardFailedWithBackup", 10), ("card-lost", 11))))
if mibBuilder.loadTexts: lumAlarmCardAlarmType.setStatus('current')
lumSysconAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cmmlf", 1), ("redundancy-lost", 2))))
if mibBuilder.loadTexts: lumSysconAlarmType.setStatus('current')
lumT1AlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("bpv", 1), ("lof", 2), ("los", 3), ("ais", 4), ("rai", 5), ("ovrfl", 6), ("sf-ber", 7), ("sf-es", 8), ("sf-ses", 9), ("tcfl", 10))))
if mibBuilder.loadTexts: lumT1AlarmType.setStatus('current')
lumTEN100AlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("an-fail", 1), ("los", 2), ("symer", 3), ("rxer", 4), ("frlex", 5), ("aler", 6), ("fcserr", 7))))
if mibBuilder.loadTexts: lumTEN100AlarmType.setStatus('current')
lumSonetAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("laser-loop", 1), ("laser-bias", 2), ("laser-pwr", 3), ("loss-of-sync", 4), ("los-s", 5), ("lof-s", 6), ("ais-l", 7), ("rfi-l", 8), ("sf-ber", 9), ("sd-ber", 10), ("ais-p", 11), ("rfi-p", 12), ("lop-p", 13), ("uneq-p", 14), ("plm-p", 15), ("aps-k1", 16), ("aps-k2", 17), ("aps-mode", 18), ("aps-far-end", 19), ("aps-success", 20), ("aps-failed", 21))))
if mibBuilder.loadTexts: lumSonetAlarmType.setStatus('current')
lumRingCardAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("los", 1), ("losynch", 2), ("sf-ber", 3), ("sd-ber", 4), ("pri-los", 5), ("sec-los", 6), ("io-west-lost", 7), ("io-east-lost", 8), ("io-card-lost", 9), ("switch-fabric-lost", 10), ("switch-fabric-redundancy-lost", 11))))
if mibBuilder.loadTexts: lumRingCardAlarmType.setStatus('current')
lumUtilityAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vltg", 1), ("hitmp", 2), ("pwra", 3), ("pwrb", 4), ("card-lost", 5))))
if mibBuilder.loadTexts: lumUtilityAlarmType.setStatus('current')
lumEquipmentAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fncrt", 1), ("fnmjr", 2), ("boot", 3), ("hwfl", 4), ("hitmp", 5), ("vltg", 6), ("trans-mea", 7), ("sgeo", 8), ("ueq", 9), ("mea", 10), ("prov-io-card-lost", 11), ("io-card-lost", 12), ("prov-io-card-mismatched", 13), ("io-card-mismatched", 14))))
if mibBuilder.loadTexts: lumEquipmentAlarmType.setStatus('current')
lumDataFlowAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sf-dfc", 1), ("sf-ifc", 2), ("sf-bfc", 3))))
if mibBuilder.loadTexts: lumDataFlowAlarmType.setStatus('current')
lumDataBaseAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("saveFailed", 1), ("restoreFailed", 2))))
if mibBuilder.loadTexts: lumDataBaseAlarmType.setStatus('current')
lumPPPAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("linkDown", 1))))
if mibBuilder.loadTexts: lumPPPAlarmType.setStatus('current')
lumAlarmSlotId = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 1), LumSlotNum())
if mibBuilder.loadTexts: lumAlarmSlotId.setStatus('current')
lumAlarmPortId = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 2), LumPortNum())
if mibBuilder.loadTexts: lumAlarmPortId.setStatus('current')
lumAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("alarmClear", 1), ("alarmSet", 2), ("alarmMasked", 3))))
if mibBuilder.loadTexts: lumAlarmStatus.setStatus('current')
lumAlarmSummaryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1))
lumAlarmSummaryState = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 1), LumAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryState.setStatus('current')
lumAlarmSummaryCriticalStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 2), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryCriticalStatus.setStatus('current')
lumAlarmSummaryMajorStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 3), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryMajorStatus.setStatus('current')
lumAlarmSummaryMinorStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 4), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryMinorStatus.setStatus('current')
lumAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1), )
if mibBuilder.loadTexts: lumAlarmActiveTable.setStatus('current')
lumAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumAlarmActiveIndex"))
if mibBuilder.loadTexts: lumAlarmActiveEntry.setStatus('current')
lumAlarmActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveIndex.setStatus('current')
lumAlarmActiveType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("provision", 1), ("alarmCard", 2), ("syscon", 3), ("t1", 4), ("tEN100", 5), ("sonet", 6), ("ringCard", 7), ("utility", 8), ("equipment", 9), ("dataFlow", 10), ("dataBase", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveType.setStatus('current')
lumAlarmActiveValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveValue.setStatus('current')
lumAlarmActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("alarmClear", 1), ("alarmSet", 2), ("alarmMasked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveStatus.setStatus('current')
lumAlarmActiveTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveTimeStamp.setStatus('current')
lumAlarmActiveSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 6), LumSlotNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveSlotId.setStatus('current')
lumAlarmActivePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 7), LumPortNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActivePortId.setStatus('current')
lumAlarmHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2), )
if mibBuilder.loadTexts: lumAlarmHistoryTable.setStatus('current')
lumAlarmHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumAlarmHistoryIndex"))
if mibBuilder.loadTexts: lumAlarmHistoryEntry.setStatus('current')
lumAlarmHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmHistoryIndex.setStatus('current')
lumAlarmHistoryData = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmHistoryData.setStatus('current')
lumAlarmSummaryChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0, 1)).setObjects(("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryState"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryCriticalStatus"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMajorStatus"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMinorStatus"))
if mibBuilder.loadTexts: lumAlarmSummaryChangeTrap.setStatus('current')
mibBuilder.exportSymbols("LUMINOUS-SYSTEM-MIB", lumSystemResetShelfCmd=lumSystemResetShelfCmd, PYSNMP_MODULE_ID=lumSystemMIB, lumDownLoadTimeOut=lumDownLoadTimeOut, lumAlarmSummaryMajorStatus=lumAlarmSummaryMajorStatus, lumSonetAlarmType=lumSonetAlarmType, lumAlarmActiveTable=lumAlarmActiveTable, lumAlarmSummaryGroup=lumAlarmSummaryGroup, lumADM=lumADM, lumAlarmSummary=lumAlarmSummary, lumT1AlarmType=lumT1AlarmType, lumAlarmActiveStatus=lumAlarmActiveStatus, lumAlarmTraps=lumAlarmTraps, lumDownLoadImageType=lumDownLoadImageType, lumAlarmSlotId=lumAlarmSlotId, lumAlarmCardAlarmType=lumAlarmCardAlarmType, lumDownLoadFilePath=lumDownLoadFilePath, lumDownLoadAbort=lumDownLoadAbort, lumSysconAlarmType=lumSysconAlarmType, lumAlarmActiveSlotId=lumAlarmActiveSlotId, lumDataFlowAlarmType=lumDataFlowAlarmType, lumDownLoadVersion=lumDownLoadVersion, lumDownLoadCmd=lumDownLoadCmd, lumSystemMIB=lumSystemMIB, lumAlarmActiveIndex=lumAlarmActiveIndex, lumAlarmPortId=lumAlarmPortId, lumAlarmSummaryState=lumAlarmSummaryState, lumDownLoadSlot=lumDownLoadSlot, lumAlarmV2Traps=lumAlarmV2Traps, lumAlarmSummaryCriticalStatus=lumAlarmSummaryCriticalStatus, lumAlarmHistoryIndex=lumAlarmHistoryIndex, lumAlarmSummaryMinorStatus=lumAlarmSummaryMinorStatus, lumPPPAlarmType=lumPPPAlarmType, lumSystemResetCardIndex=lumSystemResetCardIndex, lumAlarmActiveValue=lumAlarmActiveValue, lumAlarmHistoryEntry=lumAlarmHistoryEntry, lumAlarmSummaryChangeTrap=lumAlarmSummaryChangeTrap, lumSystemReset=lumSystemReset, lumDownLoadHost=lumDownLoadHost, lumEquipmentAlarmType=lumEquipmentAlarmType, lumAlarmActiveType=lumAlarmActiveType, lumSystemResetCardCmd=lumSystemResetCardCmd, lumRingCardAlarmType=lumRingCardAlarmType, lumAlarmSource=lumAlarmSource, lumAlarmHistoryTable=lumAlarmHistoryTable, lumDataBaseAlarmType=lumDataBaseAlarmType, lumSoftwareDownload=lumSoftwareDownload, lumSystemResetCardTable=lumSystemResetCardTable, lumAlarmActivePortId=lumAlarmActivePortId, lumDownLoadUsrName=lumDownLoadUsrName, lumAlarmHistoryData=lumAlarmHistoryData, lumUtilityAlarmType=lumUtilityAlarmType, lumProvisionAlarmType=lumProvisionAlarmType, lumAlarmStatus=lumAlarmStatus, lumSystemResetCardEntry=lumSystemResetCardEntry, lumDownLoadPasswd=lumDownLoadPasswd, luminous=luminous, lumAlarms=lumAlarms, lumDownLoadStatus=lumDownLoadStatus, lumTEN100AlarmType=lumTEN100AlarmType, lumAlarmActiveEntry=lumAlarmActiveEntry, lumAlarmActiveTimeStamp=lumAlarmActiveTimeStamp, lumAlarmLog=lumAlarmLog, lumAlarmType=lumAlarmType)

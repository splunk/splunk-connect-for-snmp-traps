#
# PySNMP MIB module AVAYA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-ENTITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
lsg, = mibBuilder.importSymbols("AVAYAGEN-MIB", "lsg")
entPhysicalIndex, entPhysicalParentRelPos, entPhysicalDescr, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalParentRelPos", "entPhysicalDescr", "PhysicalIndex")
EntitySensorValue, entPhySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorValue")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Counter32, Bits, ModuleIdentity, ObjectIdentity, Integer32, mib_2, Counter64, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Counter32", "Bits", "ModuleIdentity", "ObjectIdentity", "Integer32", "mib-2", "Counter64", "iso", "MibIdentifier")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
avayaEntity = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99))
if mibBuilder.loadTexts: avayaEntity.setLastUpdated('200612251800Z')
if mibBuilder.loadTexts: avayaEntity.setOrganization('Avaya Inc.')
class AvEntPhyItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

avEntPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1), )
if mibBuilder.loadTexts: avEntPhySensorTable.setStatus('current')
avEntPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: avEntPhySensorEntry.setStatus('current')
avEntPhySensorHiShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorHiShutdown.setStatus('current')
avEntPhySensorHiWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorHiWarning.setStatus('current')
avEntPhySensorHiWarningClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 3), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorHiWarningClear.setStatus('current')
avEntPhySensorLoWarningClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorLoWarningClear.setStatus('current')
avEntPhySensorLoWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 5), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorLoWarning.setStatus('current')
avEntPhySensorLoShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 6), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorLoShutdown.setStatus('current')
avEntPhySensorEventSupportMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhySensorEventSupportMask.setStatus('current')
avEntTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2))
avEntTrapsV3separator = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0))
avEntFanFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 1)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"))
if mibBuilder.loadTexts: avEntFanFlt.setStatus('current')
avEntFanOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 2)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"))
if mibBuilder.loadTexts: avEntFanOk.setStatus('current')
avEnt48vPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 4)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt48vPwrFlt.setStatus('current')
avEnt48vPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 5)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt48vPwrFltOk.setStatus('current')
avEnt5vPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 7)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt5vPwrFlt.setStatus('current')
avEnt5vPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 8)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt5vPwrFltOk.setStatus('current')
avEnt3300mvPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 10)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt3300mvPwrFlt.setStatus('current')
avEnt3300mvPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 11)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt3300mvPwrFltOk.setStatus('current')
avEnt2500mvPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 13)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt2500mvPwrFlt.setStatus('current')
avEnt2500mvPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 14)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt2500mvPwrFltOk.setStatus('current')
avEnt1800mvPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 16)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt1800mvPwrFlt.setStatus('current')
avEnt1800mvPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 17)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt1800mvPwrFltOk.setStatus('current')
avEnt1600mvPwrFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 19)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt1600mvPwrFlt.setStatus('current')
avEnt1600mvPwrFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 20)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEnt1600mvPwrFltOk.setStatus('current')
avEntAmbientHiTempFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 22)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEntAmbientHiTempFlt.setStatus('current')
avEntAmbientHiTempFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 23)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEntAmbientHiTempFltOk.setStatus('current')
avEntAmbientLoTempFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 24)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEntAmbientLoTempFlt.setStatus('current')
avEntAmbientLoTempFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 25)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"), ("ENTITY-MIB", "entPhysicalParentRelPos"))
if mibBuilder.loadTexts: avEntAmbientLoTempFltOk.setStatus('current')
avEntPhyUSBDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3))
avEntPhyUSBDevicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0))
avEntPhyUSBDeviceRemovalOnBackupRestoreOperation = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 1)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBDeviceRemovalOnBackupRestoreOperation.setStatus('current')
avEntPhyUSBDeviceInsecureRemoval = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 2)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBDeviceInsecureRemoval.setStatus('current')
avEntPhyUSBDevicePowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 3)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBDevicePowerFailure.setStatus('current')
avEntPhyUSBDeviceNotSupported = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 4)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBDeviceNotSupported.setStatus('current')
avEntPhyUSBDeviceExceedMaxNumber = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 5)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBDeviceExceedMaxNumber.setStatus('current')
avEntPhyUSBFileSystemNotSupported = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 6)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"), ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyUSBFileSystemNotSupported.setStatus('current')
avEntPhyUSBDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1), )
if mibBuilder.loadTexts: avEntPhyUSBDevicesTable.setStatus('current')
avEntPhyUSBDevicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: avEntPhyUSBDevicesEntry.setStatus('current')
avEntPhyUSBDeviceUSBSupportVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceUSBSupportVersion.setStatus('current')
avEntPhyUSBDeviceClassCode = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceClassCode.setStatus('current')
avEntPhyUSBDeviceSubClassCode = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceSubClassCode.setStatus('current')
avEntPhyUSBDeviceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceProtocol.setStatus('current')
avEntPhyUSBDeviceVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceVendorId.setStatus('current')
avEntPhyUSBDeviceSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceSpeed.setStatus('current')
avEntPhyUSBDevicePower = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDevicePower.setStatus('current')
avEntPhyUSBDeviceCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBDeviceCurrent.setStatus('current')
avEntPhyUSBMassStorageDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2), )
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDevicesTable.setStatus('current')
avEntPhyUSBMassStorageDevicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDevicesEntry.setStatus('current')
avEntPhyUSBMassStorageDeviceFileSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDeviceFileSystemName.setStatus('current')
avEntPhyUSBMassStorageDeviceCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDeviceCapacity.setStatus('current')
avEntPhyUSBMassStorageDeviceFreeMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDeviceFreeMemory.setStatus('current')
avEntPhyUSBMassStorageDeviceFs = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyUSBMassStorageDeviceFs.setStatus('current')
avEntPhyNotificationDefinitions = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4))
avEntPhySeverity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 1), AvEntPhyItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: avEntPhySeverity.setStatus('current')
avEntPhyProductId = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: avEntPhyProductId.setStatus('current')
avEntPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 3), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: avEntPhysicalIndex.setStatus('current')
avEntPhyChFru = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5))
avEntPhyChFruNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0))
avEntPhyChFruRemoval = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 1)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruRemoval.setStatus('current')
avEntPhyChFruInsertion = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 2)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruInsertion.setStatus('current')
avEntPhyChFruPsuFlt = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 3)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruPsuFlt.setStatus('current')
avEntPhyChFruPsuFltOk = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 4)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruPsuFltOk.setStatus('current')
avEntPhyChFruExpansionTestFailure = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 5)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruExpansionTestFailure.setStatus('current')
avEntPhyChFruExpansionTestClear = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 6)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"), ("ENTITY-MIB", "entPhysicalDescr"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"), ("AVAYA-ENTITY-MIB", "avEntPhyProductId"), ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
if mibBuilder.loadTexts: avEntPhyChFruExpansionTestClear.setStatus('current')
avEntPhyChFruTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1), )
if mibBuilder.loadTexts: avEntPhyChFruTable.setStatus('current')
avEntPhyChFruEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: avEntPhyChFruEntry.setStatus('current')
avEntPhyChFruOperStat = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("ok", 1), ("fault", 2), ("notPresent", 3), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyChFruOperStat.setStatus('current')
avEntPhyChFruFault = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 255))).clone(namedValues=NamedValues(("none", 1), ("mulfunction", 2), ("acFault", 3), ("malfunctionAndAcFault", 4), ("singleFanFault", 5), ("multipleFanFault", 6), ("badExpansionCable", 7), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEntPhyChFruFault.setStatus('current')
avEntPhyChFruGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 2)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avEntPhyChFruGroup = avEntPhyChFruGroup.setStatus('current')
avEntPhyChFruNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 3)).setObjects(("AVAYA-ENTITY-MIB", "avEntPhyChFruRemoval"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruInsertion"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruPsuFlt"), ("AVAYA-ENTITY-MIB", "avEntPhyChFruPsuFltOk"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avEntPhyChFruNotificationGroup = avEntPhyChFruNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("AVAYA-ENTITY-MIB", avEntPhyChFruInsertion=avEntPhyChFruInsertion, avEntPhysicalIndex=avEntPhysicalIndex, avEntPhyUSBMassStorageDeviceCapacity=avEntPhyUSBMassStorageDeviceCapacity, avEnt3300mvPwrFlt=avEnt3300mvPwrFlt, avEntPhyChFru=avEntPhyChFru, avEntPhyChFruPsuFltOk=avEntPhyChFruPsuFltOk, avEntPhySensorHiWarningClear=avEntPhySensorHiWarningClear, avEntTrapsV3separator=avEntTrapsV3separator, avEntAmbientHiTempFlt=avEntAmbientHiTempFlt, avEntPhyUSBDeviceExceedMaxNumber=avEntPhyUSBDeviceExceedMaxNumber, avEnt1800mvPwrFltOk=avEnt1800mvPwrFltOk, avEntPhyUSBDeviceVendorId=avEntPhyUSBDeviceVendorId, avEnt5vPwrFltOk=avEnt5vPwrFltOk, avEntPhyProductId=avEntPhyProductId, avEntPhyChFruTable=avEntPhyChFruTable, avEntAmbientLoTempFlt=avEntAmbientLoTempFlt, avEntPhyNotificationDefinitions=avEntPhyNotificationDefinitions, avEntPhySensorLoWarning=avEntPhySensorLoWarning, avEnt5vPwrFlt=avEnt5vPwrFlt, avEntPhySensorLoWarningClear=avEntPhySensorLoWarningClear, avEntPhyUSBDeviceSubClassCode=avEntPhyUSBDeviceSubClassCode, avEntPhyUSBMassStorageDeviceFs=avEntPhyUSBMassStorageDeviceFs, avEntPhyChFruOperStat=avEntPhyChFruOperStat, avEntPhyChFruExpansionTestFailure=avEntPhyChFruExpansionTestFailure, avEntPhyChFruExpansionTestClear=avEntPhyChFruExpansionTestClear, avEntPhyChFruNotificationGroup=avEntPhyChFruNotificationGroup, avEntPhySensorTable=avEntPhySensorTable, avEnt2500mvPwrFlt=avEnt2500mvPwrFlt, avEntPhyUSBDeviceSpeed=avEntPhyUSBDeviceSpeed, avEnt2500mvPwrFltOk=avEnt2500mvPwrFltOk, avEntPhyUSBDeviceClassCode=avEntPhyUSBDeviceClassCode, avEntPhyUSBDevicesTraps=avEntPhyUSBDevicesTraps, avEntPhySensorHiShutdown=avEntPhySensorHiShutdown, avEntAmbientHiTempFltOk=avEntAmbientHiTempFltOk, PYSNMP_MODULE_ID=avayaEntity, avEnt1600mvPwrFlt=avEnt1600mvPwrFlt, avEnt1600mvPwrFltOk=avEnt1600mvPwrFltOk, avEntPhyUSBDevicePowerFailure=avEntPhyUSBDevicePowerFailure, avEntPhyUSBDevicesTable=avEntPhyUSBDevicesTable, avEntPhyUSBDeviceCurrent=avEntPhyUSBDeviceCurrent, avEntPhyUSBMassStorageDevicesTable=avEntPhyUSBMassStorageDevicesTable, avEntPhyChFruRemoval=avEntPhyChFruRemoval, avEntPhyChFruNotifications=avEntPhyChFruNotifications, avEntPhyUSBDeviceProtocol=avEntPhyUSBDeviceProtocol, avEnt48vPwrFlt=avEnt48vPwrFlt, avEnt1800mvPwrFlt=avEnt1800mvPwrFlt, avEntFanFlt=avEntFanFlt, avEntPhyChFruEntry=avEntPhyChFruEntry, avEntPhyUSBMassStorageDevicesEntry=avEntPhyUSBMassStorageDevicesEntry, avEntPhySensorEntry=avEntPhySensorEntry, avEntPhyChFruGroup=avEntPhyChFruGroup, avEntPhyUSBDevices=avEntPhyUSBDevices, avEntPhyChFruPsuFlt=avEntPhyChFruPsuFlt, avEntPhyUSBDeviceNotSupported=avEntPhyUSBDeviceNotSupported, avEntPhySensorEventSupportMask=avEntPhySensorEventSupportMask, avayaEntity=avayaEntity, avEntPhyChFruFault=avEntPhyChFruFault, avEntPhyUSBDeviceInsecureRemoval=avEntPhyUSBDeviceInsecureRemoval, avEntPhyUSBDeviceRemovalOnBackupRestoreOperation=avEntPhyUSBDeviceRemovalOnBackupRestoreOperation, avEntAmbientLoTempFltOk=avEntAmbientLoTempFltOk, avEnt3300mvPwrFltOk=avEnt3300mvPwrFltOk, avEntPhyUSBDevicesEntry=avEntPhyUSBDevicesEntry, avEntPhyUSBMassStorageDeviceFreeMemory=avEntPhyUSBMassStorageDeviceFreeMemory, avEntPhySensorLoShutdown=avEntPhySensorLoShutdown, avEntTraps=avEntTraps, avEntPhyUSBFileSystemNotSupported=avEntPhyUSBFileSystemNotSupported, avEntPhySensorHiWarning=avEntPhySensorHiWarning, avEntFanOk=avEntFanOk, avEnt48vPwrFltOk=avEnt48vPwrFltOk, AvEntPhyItuPerceivedSeverity=AvEntPhyItuPerceivedSeverity, avEntPhyUSBMassStorageDeviceFileSystemName=avEntPhyUSBMassStorageDeviceFileSystemName, avEntPhyUSBDeviceUSBSupportVersion=avEntPhyUSBDeviceUSBSupportVersion, avEntPhySeverity=avEntPhySeverity, avEntPhyUSBDevicePower=avEntPhyUSBDevicePower)
#
# PySNMP MIB module H3C-STORAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-STORAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
entPhysicalIndex, PhysicalIndex, entPhysicalName, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex", "entPhysicalName", "entPhysicalDescr")
h3cDiskPowerOffReason, = mibBuilder.importSymbols("H3C-DISK-MIB", "h3cDiskPowerOffReason")
h3cEntityExtCriticalLowerTemperatureThreshold, h3cEntityExtTemperature, h3cEntityExtPhysicalIndex, h3cEntityExtOperStatus, h3cEntityExtShutdownLowerTemperatureThreshold = mibBuilder.importSymbols("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalLowerTemperatureThreshold", "h3cEntityExtTemperature", "h3cEntityExtPhysicalIndex", "h3cEntityExtOperStatus", "h3cEntityExtShutdownLowerTemperatureThreshold")
h3cRaidRunState, h3cRaidHideState, h3cRaidName, h3cRaidUuid = mibBuilder.importSymbols("H3C-RAID-MIB", "h3cRaidRunState", "h3cRaidHideState", "h3cRaidName", "h3cRaidUuid")
H3cStorageLedStateType, H3cSoftwareInfoString, H3cStorageActionType, H3cStorageEnableState, H3cStorageCapableState, h3cStorageRef, H3cWwpnListType = mibBuilder.importSymbols("H3C-STORAGE-REF-MIB", "H3cStorageLedStateType", "H3cSoftwareInfoString", "H3cStorageActionType", "H3cStorageEnableState", "H3cStorageCapableState", "h3cStorageRef", "H3cWwpnListType")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, MibIdentifier, Counter32, ObjectIdentity, NotificationType, Bits, Counter64, Integer32, ModuleIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "ObjectIdentity", "NotificationType", "Bits", "Counter64", "Integer32", "ModuleIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cStorageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1))
if mibBuilder.loadTexts: h3cStorageMIB.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: h3cStorageMIB.setOrganization('H3C Technologies Co., Ltd.')
h3cStorageMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1))
h3cStorageServerInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1))
h3cStoragePhysicalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2))
h3cStorageServerCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1))
h3cRaidCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 1), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRaidCapability.setStatus('current')
h3cFcCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 2), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcCapability.setStatus('current')
h3cNasCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 3), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cNasCapability.setStatus('current')
h3cAdaptiveRepCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 4), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAdaptiveRepCapability.setStatus('current')
h3cRemoteRepCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 5), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRemoteRepCapability.setStatus('current')
h3cSafeCacheCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 6), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSafeCacheCapability.setStatus('current')
h3cSyncMirrorCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 7), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyncMirrorCapability.setStatus('current')
h3cAsyncMirrorCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 8), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAsyncMirrorCapability.setStatus('current')
h3cTimeMarkCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 9), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTimeMarkCapability.setStatus('current')
h3cSseCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 10), H3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSseCapability.setStatus('current')
h3cStorageTargetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2))
h3ciSCSITargetEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2, 1), H3cStorageEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3ciSCSITargetEnable.setStatus('current')
h3cFcTargetEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2, 2), H3cStorageEnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFcTargetEnable.setStatus('current')
h3cStorageServerPhysInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3))
h3cServerLocationLedState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 1), H3cStorageLedStateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cServerLocationLedState.setStatus('current')
h3cServerResetButtonState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 2), H3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cServerResetButtonState.setStatus('current')
h3cServerPowerButtonState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 3), H3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cServerPowerButtonState.setStatus('current')
h3cServerPowerState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("online", 1), ("onlinebypass", 2), ("onbattery", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cServerPowerState.setStatus('current')
h3cDeuTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1), )
if mibBuilder.loadTexts: h3cDeuTable.setStatus('current')
h3cDeuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1), ).setIndexNames((0, "H3C-STORAGE-MIB", "h3cDeuIndex"))
if mibBuilder.loadTexts: h3cDeuEntry.setStatus('current')
h3cDeuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDeuIndex.setStatus('current')
h3cDeuIDLed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 2), H3cStorageLedStateType().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDeuIDLed.setStatus('current')
h3cDeuDiskScan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 3), H3cStorageActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDeuDiskScan.setStatus('current')
h3cStorageInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2), )
if mibBuilder.loadTexts: h3cStorageInterfaceTable.setStatus('current')
h3cStorageInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1), ).setIndexNames((0, "H3C-STORAGE-MIB", "h3cStorageInterfaceIndex"))
if mibBuilder.loadTexts: h3cStorageInterfaceEntry.setStatus('current')
h3cStorageInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cStorageInterfaceIndex.setStatus('current')
h3cStorageInterfaceGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cStorageInterfaceGateway.setStatus('current')
h3cStorageInterfaceGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cStorageInterfaceGatewayType.setStatus('current')
h3cStorageInterfaceMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1500, 9000))).clone(namedValues=NamedValues(("mtu1", 1500), ("mtu2", 9000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cStorageInterfaceMTU.setStatus('current')
h3cBondingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3), )
if mibBuilder.loadTexts: h3cBondingTable.setStatus('current')
h3cBondingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1), ).setIndexNames((0, "H3C-STORAGE-MIB", "h3cBondingIndex"))
if mibBuilder.loadTexts: h3cBondingEntry.setStatus('current')
h3cBondingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cBondingIndex.setStatus('current')
h3cBondingPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBondingPortList.setStatus('current')
h3cScsiAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4), )
if mibBuilder.loadTexts: h3cScsiAdapterTable.setStatus('current')
h3cScsiAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "H3C-STORAGE-MIB", "h3cAdapterNumber"))
if mibBuilder.loadTexts: h3cScsiAdapterEntry.setStatus('current')
h3cAdapterNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cAdapterNumber.setStatus('current')
h3cAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAdapterDesc.setStatus('current')
h3cAdapterType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scsi", 1), ("fc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAdapterType.setStatus('current')
h3cFcAdapterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initiator", 1), ("target", 2), ("dual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcAdapterMode.setStatus('current')
h3cFcAdapterInitiatorWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 5), H3cWwpnListType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcAdapterInitiatorWwpnName.setStatus('current')
h3cFcAdapterTargetWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 6), H3cWwpnListType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcAdapterTargetWwpnName.setStatus('current')
h3cFcAdapterPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkup", 1), ("linkdown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcAdapterPortState.setStatus('current')
h3cFcAdapterModeSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 8), H3cStorageEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFcAdapterModeSwitch.setStatus('current')
h3cExtVoltageTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5), )
if mibBuilder.loadTexts: h3cExtVoltageTable.setStatus('current')
h3cExtVoltageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1), ).setIndexNames((0, "H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"))
if mibBuilder.loadTexts: h3cExtVoltageEntry.setStatus('current')
h3cExtVoltagePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cExtVoltagePhysicalIndex.setStatus('current')
h3cExtVoltagePhysicalName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cExtVoltagePhysicalName.setStatus('current')
h3cExtVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cExtVoltage.setStatus('current')
h3cExtVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtVoltageLowThreshold.setStatus('current')
h3cExtVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtVoltageHighThreshold.setStatus('current')
h3cExtCriticalVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtCriticalVoltageLowThreshold.setStatus('current')
h3cExtCriticalVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtCriticalVoltageHighThreshold.setStatus('current')
h3cExtShutdownVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtShutdownVoltageLowThreshold.setStatus('current')
h3cExtShutdownVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExtShutdownVoltageHighThreshold.setStatus('current')
h3cStorageTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3))
h3cStorageTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0))
h3cStorageTrapsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 1))
h3cSoftwareInfoString = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 1, 1), H3cSoftwareInfoString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSoftwareInfoString.setStatus('current')
h3cStorCriticalLowerTemperatureThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 1)).setObjects(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"), ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalLowerTemperatureThreshold"))
if mibBuilder.loadTexts: h3cStorCriticalLowerTemperatureThresholdNotification.setStatus('current')
h3cStorTemperatureTooLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 2)).setObjects(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"), ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownLowerTemperatureThreshold"))
if mibBuilder.loadTexts: h3cStorTemperatureTooLow.setStatus('current')
h3cExtVoltageLowThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 3)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtVoltageLowThreshold"))
if mibBuilder.loadTexts: h3cExtVoltageLowThresholdNotification.setStatus('current')
h3cExtVoltageHighThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 4)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtVoltageHighThreshold"))
if mibBuilder.loadTexts: h3cExtVoltageHighThresholdNotification.setStatus('current')
h3cExtCriticalVoltageLowThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 5)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtCriticalVoltageLowThreshold"))
if mibBuilder.loadTexts: h3cExtCriticalVoltageLowThresholdNotification.setStatus('current')
h3cExtCriticalVoltageHighThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 6)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtCriticalVoltageHighThreshold"))
if mibBuilder.loadTexts: h3cExtCriticalVoltageHighThresholdNotification.setStatus('current')
h3cExtVoltageTooLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 7)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtShutdownVoltageLowThreshold"))
if mibBuilder.loadTexts: h3cExtVoltageTooLow.setStatus('current')
h3cExtVoltageTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 8)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtShutdownVoltageHighThreshold"))
if mibBuilder.loadTexts: h3cExtVoltageTooHigh.setStatus('current')
h3cExtBatteryStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 9)).setObjects(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperStatus"))
if mibBuilder.loadTexts: h3cExtBatteryStateNotification.setStatus('current')
h3cDiskIOErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 10)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: h3cDiskIOErrorNotification.setStatus('current')
h3cRaidCreateNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 11)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidCreateNotification.setStatus('current')
h3cRaidDeleteNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 12)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidDeleteNotification.setStatus('current')
h3cRaidHideStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 13)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"), ("H3C-RAID-MIB", "h3cRaidHideState"))
if mibBuilder.loadTexts: h3cRaidHideStateNotification.setStatus('current')
h3cRaidRunStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 14)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"), ("H3C-RAID-MIB", "h3cRaidRunState"))
if mibBuilder.loadTexts: h3cRaidRunStateNotification.setStatus('current')
h3cRaidImportNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 15)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidImportNotification.setStatus('current')
h3cRaidRebuildStartNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 16)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidRebuildStartNotification.setStatus('current')
h3cRaidRebuildFinishNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 17)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidRebuildFinishNotification.setStatus('current')
h3cRaidRebuildPauseNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 18)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidRebuildPauseNotification.setStatus('current')
h3cRaidRebuildInterruptNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 19)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidRebuildInterruptNotification.setStatus('current')
h3cSoftwareModuleFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 20)).setObjects(("H3C-STORAGE-MIB", "h3cSoftwareInfoString"))
if mibBuilder.loadTexts: h3cSoftwareModuleFailNotification.setStatus('current')
h3cRaidBatteryExpiredNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 21))
if mibBuilder.loadTexts: h3cRaidBatteryExpiredNotification.setStatus('current')
h3cRaidBatteryWillExpireNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 22))
if mibBuilder.loadTexts: h3cRaidBatteryWillExpireNotification.setStatus('current')
h3cLvOnlineFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 23)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cLvOnlineFailNotification.setStatus('current')
h3cLvOfflineFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 24)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cLvOfflineFailNotification.setStatus('current')
h3cRaidRunNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 25)).setObjects(("H3C-RAID-MIB", "h3cRaidUuid"), ("H3C-RAID-MIB", "h3cRaidName"))
if mibBuilder.loadTexts: h3cRaidRunNotification.setStatus('current')
h3cExtVoltageNormal = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 26)).setObjects(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"), ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"), ("H3C-STORAGE-MIB", "h3cExtVoltage"), ("H3C-STORAGE-MIB", "h3cExtVoltageLowThreshold"), ("H3C-STORAGE-MIB", "h3cExtVoltageHighThreshold"))
if mibBuilder.loadTexts: h3cExtVoltageNormal.setStatus('current')
h3cDiskPowerOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 27)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: h3cDiskPowerOnNotification.setStatus('current')
h3cDiskPowerOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 28)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("H3C-DISK-MIB", "h3cDiskPowerOffReason"))
if mibBuilder.loadTexts: h3cDiskPowerOffNotification.setStatus('current')
mibBuilder.exportSymbols("H3C-STORAGE-MIB", h3cStorageInterfaceEntry=h3cStorageInterfaceEntry, h3cExtVoltageLowThreshold=h3cExtVoltageLowThreshold, h3cFcAdapterTargetWwpnName=h3cFcAdapterTargetWwpnName, h3cDeuTable=h3cDeuTable, h3cRaidRebuildFinishNotification=h3cRaidRebuildFinishNotification, h3cScsiAdapterTable=h3cScsiAdapterTable, h3cAdapterNumber=h3cAdapterNumber, h3cExtShutdownVoltageLowThreshold=h3cExtShutdownVoltageLowThreshold, h3cRaidRebuildPauseNotification=h3cRaidRebuildPauseNotification, h3cStorageInterfaceGateway=h3cStorageInterfaceGateway, h3cDiskPowerOffNotification=h3cDiskPowerOffNotification, h3cStorageInterfaceIndex=h3cStorageInterfaceIndex, h3cServerPowerState=h3cServerPowerState, h3cFcCapability=h3cFcCapability, h3cRaidBatteryExpiredNotification=h3cRaidBatteryExpiredNotification, h3cBondingTable=h3cBondingTable, h3cRaidRunStateNotification=h3cRaidRunStateNotification, h3cFcAdapterPortState=h3cFcAdapterPortState, h3cStorTemperatureTooLow=h3cStorTemperatureTooLow, h3cSyncMirrorCapability=h3cSyncMirrorCapability, h3cSafeCacheCapability=h3cSafeCacheCapability, h3cExtBatteryStateNotification=h3cExtBatteryStateNotification, h3cServerLocationLedState=h3cServerLocationLedState, h3cStorCriticalLowerTemperatureThresholdNotification=h3cStorCriticalLowerTemperatureThresholdNotification, h3cDeuIDLed=h3cDeuIDLed, h3cExtVoltageTooHigh=h3cExtVoltageTooHigh, h3cStorageTargetConfig=h3cStorageTargetConfig, h3ciSCSITargetEnable=h3ciSCSITargetEnable, h3cStorageTrapsPrefix=h3cStorageTrapsPrefix, h3cAdapterDesc=h3cAdapterDesc, h3cRaidRunNotification=h3cRaidRunNotification, h3cStorageTrapsObjects=h3cStorageTrapsObjects, h3cServerResetButtonState=h3cServerResetButtonState, h3cStorageInterfaceGatewayType=h3cStorageInterfaceGatewayType, h3cExtCriticalVoltageHighThreshold=h3cExtCriticalVoltageHighThreshold, h3cBondingEntry=h3cBondingEntry, h3cRaidRebuildInterruptNotification=h3cRaidRebuildInterruptNotification, h3cScsiAdapterEntry=h3cScsiAdapterEntry, h3cExtVoltagePhysicalIndex=h3cExtVoltagePhysicalIndex, h3cDiskIOErrorNotification=h3cDiskIOErrorNotification, h3cExtVoltageHighThresholdNotification=h3cExtVoltageHighThresholdNotification, h3cDeuEntry=h3cDeuEntry, h3cDiskPowerOnNotification=h3cDiskPowerOnNotification, h3cFcTargetEnable=h3cFcTargetEnable, h3cBondingIndex=h3cBondingIndex, h3cRemoteRepCapability=h3cRemoteRepCapability, h3cExtVoltageEntry=h3cExtVoltageEntry, h3cStorageServerPhysInfo=h3cStorageServerPhysInfo, h3cRaidHideStateNotification=h3cRaidHideStateNotification, h3cExtVoltage=h3cExtVoltage, PYSNMP_MODULE_ID=h3cStorageMIB, h3cStorageServerInfo=h3cStorageServerInfo, h3cFcAdapterModeSwitch=h3cFcAdapterModeSwitch, h3cRaidImportNotification=h3cRaidImportNotification, h3cExtCriticalVoltageLowThresholdNotification=h3cExtCriticalVoltageLowThresholdNotification, h3cFcAdapterInitiatorWwpnName=h3cFcAdapterInitiatorWwpnName, h3cExtVoltageHighThreshold=h3cExtVoltageHighThreshold, h3cExtVoltageTooLow=h3cExtVoltageTooLow, h3cAsyncMirrorCapability=h3cAsyncMirrorCapability, h3cSoftwareModuleFailNotification=h3cSoftwareModuleFailNotification, h3cBondingPortList=h3cBondingPortList, h3cSoftwareInfoString=h3cSoftwareInfoString, h3cLvOnlineFailNotification=h3cLvOnlineFailNotification, h3cExtVoltageNormal=h3cExtVoltageNormal, h3cStorageInterfaceMTU=h3cStorageInterfaceMTU, h3cStorageInterfaceTable=h3cStorageInterfaceTable, h3cStorageTraps=h3cStorageTraps, h3cExtVoltageLowThresholdNotification=h3cExtVoltageLowThresholdNotification, h3cSseCapability=h3cSseCapability, h3cRaidBatteryWillExpireNotification=h3cRaidBatteryWillExpireNotification, h3cExtCriticalVoltageLowThreshold=h3cExtCriticalVoltageLowThreshold, h3cStorageMIB=h3cStorageMIB, h3cStoragePhysicalInfo=h3cStoragePhysicalInfo, h3cExtShutdownVoltageHighThreshold=h3cExtShutdownVoltageHighThreshold, h3cFcAdapterMode=h3cFcAdapterMode, h3cStorageServerCapability=h3cStorageServerCapability, h3cRaidRebuildStartNotification=h3cRaidRebuildStartNotification, h3cRaidCreateNotification=h3cRaidCreateNotification, h3cServerPowerButtonState=h3cServerPowerButtonState, h3cAdapterType=h3cAdapterType, h3cDeuDiskScan=h3cDeuDiskScan, h3cAdaptiveRepCapability=h3cAdaptiveRepCapability, h3cExtCriticalVoltageHighThresholdNotification=h3cExtCriticalVoltageHighThresholdNotification, h3cTimeMarkCapability=h3cTimeMarkCapability, h3cDeuIndex=h3cDeuIndex, h3cStorageMibObjects=h3cStorageMibObjects, h3cLvOfflineFailNotification=h3cLvOfflineFailNotification, h3cRaidCapability=h3cRaidCapability, h3cExtVoltagePhysicalName=h3cExtVoltagePhysicalName, h3cNasCapability=h3cNasCapability, h3cExtVoltageTable=h3cExtVoltageTable, h3cRaidDeleteNotification=h3cRaidDeleteNotification)
#
# PySNMP MIB module COLUBRIS-MAINTENANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-MAINTENANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
systemConfigurationVersion, systemFirmwareRevision = mibBuilder.importSymbols("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion", "systemFirmwareRevision")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, NotificationType, TimeTicks, ObjectIdentity, Counter64, ModuleIdentity, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter64", "ModuleIdentity", "IpAddress", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
colubrisMaintenanceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 2))
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setLastUpdated('200902060000Z')
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setOrganization('Colubris Networks, Inc.')
colubrisMaintenanceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1))
firmwareUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1))
configurationUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2))
certificate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3))
firmwarePeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwarePeriodicUpdate.setStatus('current')
firmwareUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateDay.setStatus('current')
firmwareUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateTime.setStatus('current')
firmwareUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateLocation.setStatus('current')
firmwareUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateInitiate.setStatus('current')
firmwareUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 6), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateNotificationEnabled.setStatus('current')
firmwareUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareUpdateInfo.setStatus('current')
firmwareUpdateStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("inprogress", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareUpdateStatus.setStatus('current')
configurationPeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationPeriodicUpdate.setStatus('current')
configurationUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateDay.setStatus('current')
configurationUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateTime.setStatus('current')
configurationUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateLocation.setStatus('current')
configurationUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateInitiate.setStatus('current')
configurationUpdateOperation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("restore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateOperation.setStatus('current')
configurationUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 7), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateNotificationEnabled.setStatus('current')
configurationLocalUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 8), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationLocalUpdateNotificationEnabled.setStatus('current')
configurationUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationUpdateInfo.setStatus('current')
configurationFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("resetToFactoryDefaults", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationFactoryDefaults.setStatus('current')
configurationRestart = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("restart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationRestart.setStatus('current')
configurationUpdateStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("inprogress", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationUpdateStatus.setStatus('current')
certificateAboutToExpireNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateAboutToExpireNotificationEnabled.setStatus('current')
certificateExpiredNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateExpiredNotificationEnabled.setStatus('current')
certificateExpiryDate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateExpiryDate.setStatus('current')
colubrisMaintenanceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2))
colubrisMaintenanceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0))
firmwareUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 5)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"))
if mibBuilder.loadTexts: firmwareUpdateNotification.setStatus('current')
configurationUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"))
if mibBuilder.loadTexts: configurationUpdateNotification.setStatus('current')
configurationLocalUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"))
if mibBuilder.loadTexts: configurationLocalUpdateNotification.setStatus('current')
certificateAboutToExpireNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 3)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateAboutToExpireNotification.setStatus('current')
certificateExpiredNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 4)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateExpiredNotification.setStatus('current')
colubrisMaintenanceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3))
colubrisMaintenanceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1))
colubrisMaintenanceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2))
colubrisMaintenanceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceMIBGroup"), ("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBCompliance = colubrisMaintenanceMIBCompliance.setStatus('current')
colubrisMaintenanceMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwarePeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateStatus"), ("COLUBRIS-MAINTENANCE-MIB", "configurationPeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateOperation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "configurationFactoryDefaults"), ("COLUBRIS-MAINTENANCE-MIB", "configurationRestart"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateStatus"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBGroup = colubrisMaintenanceMIBGroup.setStatus('current')
colubrisMaintenanceNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceNotificationGroup = colubrisMaintenanceNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-MAINTENANCE-MIB", configurationUpdateLocation=configurationUpdateLocation, colubrisMaintenanceMIB=colubrisMaintenanceMIB, colubrisMaintenanceMIBNotificationPrefix=colubrisMaintenanceMIBNotificationPrefix, configurationUpdateNotification=configurationUpdateNotification, colubrisMaintenanceNotificationGroup=colubrisMaintenanceNotificationGroup, configurationRestart=configurationRestart, firmwareUpdateLocation=firmwareUpdateLocation, firmwareUpdateInitiate=firmwareUpdateInitiate, colubrisMaintenanceMIBCompliance=colubrisMaintenanceMIBCompliance, configurationLocalUpdateNotificationEnabled=configurationLocalUpdateNotificationEnabled, configurationUpdateTime=configurationUpdateTime, firmwareUpdate=firmwareUpdate, configurationFactoryDefaults=configurationFactoryDefaults, configurationUpdateOperation=configurationUpdateOperation, colubrisMaintenanceMIBNotifications=colubrisMaintenanceMIBNotifications, firmwareUpdateNotificationEnabled=firmwareUpdateNotificationEnabled, colubrisMaintenanceMIBCompliances=colubrisMaintenanceMIBCompliances, configurationUpdateInfo=configurationUpdateInfo, configurationUpdateStatus=configurationUpdateStatus, colubrisMaintenanceMIBGroups=colubrisMaintenanceMIBGroups, configurationUpdateDay=configurationUpdateDay, certificateAboutToExpireNotificationEnabled=certificateAboutToExpireNotificationEnabled, certificateExpiredNotificationEnabled=certificateExpiredNotificationEnabled, certificateAboutToExpireNotification=certificateAboutToExpireNotification, PYSNMP_MODULE_ID=colubrisMaintenanceMIB, configurationUpdate=configurationUpdate, firmwareUpdateNotification=firmwareUpdateNotification, firmwareUpdateInfo=firmwareUpdateInfo, configurationUpdateInitiate=configurationUpdateInitiate, colubrisMaintenanceMIBConformance=colubrisMaintenanceMIBConformance, configurationUpdateNotificationEnabled=configurationUpdateNotificationEnabled, firmwarePeriodicUpdate=firmwarePeriodicUpdate, configurationLocalUpdateNotification=configurationLocalUpdateNotification, certificate=certificate, certificateExpiredNotification=certificateExpiredNotification, firmwareUpdateStatus=firmwareUpdateStatus, colubrisMaintenanceMIBObjects=colubrisMaintenanceMIBObjects, certificateExpiryDate=certificateExpiryDate, colubrisMaintenanceMIBGroup=colubrisMaintenanceMIBGroup, firmwareUpdateDay=firmwareUpdateDay, firmwareUpdateTime=firmwareUpdateTime, configurationPeriodicUpdate=configurationPeriodicUpdate)
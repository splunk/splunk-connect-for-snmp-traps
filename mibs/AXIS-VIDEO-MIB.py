#
# PySNMP MIB module AXIS-VIDEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AXIS-VIDEO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
axis, products = mibBuilder.importSymbols("AXIS-ROOT-MIB", "axis", "products")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, MibIdentifier, Unsigned32, IpAddress, TimeTicks, Counter32, Counter64, ObjectIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "MibIdentifier", "Unsigned32", "IpAddress", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
video = ModuleIdentity((1, 3, 6, 1, 4, 1, 368, 4))
video.setRevisions(('2016-09-23 12:18', '2012-12-12 12:02',))
if mibBuilder.loadTexts: video.setLastUpdated('201609231218Z')
if mibBuilder.loadTexts: video.setOrganization('Axis Communications AB')
videoBased = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 1, 1))
videoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 1))
powerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 1), )
if mibBuilder.loadTexts: powerSupplyTable.setStatus('current')
powerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "powerSupplyType"), (0, "AXIS-VIDEO-MIB", "powerSupplyId"))
if mibBuilder.loadTexts: powerSupplyEntry.setStatus('current')
powerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("common", 1), ("internal", 2), ("external", 3))))
if mibBuilder.loadTexts: powerSupplyType.setStatus('current')
powerSupplyId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: powerSupplyId.setStatus('current')
powerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyStatus.setStatus('current')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 2), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "fanType"), (0, "AXIS-VIDEO-MIB", "fanId"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("common", 1), ("housing", 2), ("rack", 3), ("cpu", 4))))
if mibBuilder.loadTexts: fanType.setStatus('current')
fanId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: fanId.setStatus('current')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('current')
tempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 3), )
if mibBuilder.loadTexts: tempSensorTable.setStatus('current')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "tempSensorType"), (0, "AXIS-VIDEO-MIB", "tempSensorId"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('current')
tempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("common", 1), ("housing", 2), ("rack", 3), ("cpu", 4))))
if mibBuilder.loadTexts: tempSensorType.setStatus('current')
tempSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: tempSensorId.setStatus('current')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2), ("outOfBoundary", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
tempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-176, 150))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorValue.setStatus('current')
videoChannelTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 4), )
if mibBuilder.loadTexts: videoChannelTable.setStatus('current')
videoChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "videoChannelId"))
if mibBuilder.loadTexts: videoChannelEntry.setStatus('current')
videoChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)))
if mibBuilder.loadTexts: videoChannelId.setStatus('current')
videoSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalOk", 1), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoSignalStatus.setStatus('current')
audioChannelTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 5), )
if mibBuilder.loadTexts: audioChannelTable.setStatus('current')
audioChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "audioChannelId"))
if mibBuilder.loadTexts: audioChannelEntry.setStatus('current')
audioChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)))
if mibBuilder.loadTexts: audioChannelId.setStatus('current')
audioSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalOk", 1), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioSignalStatus.setStatus('current')
casingTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 6), )
if mibBuilder.loadTexts: casingTable.setStatus('current')
casingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "casingId"))
if mibBuilder.loadTexts: casingEntry.setStatus('current')
casingId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: casingId.setStatus('current')
casingName = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casingName.setStatus('current')
casingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("closed", 1), ("open", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casingStatus.setStatus('current')
storageTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 8), )
if mibBuilder.loadTexts: storageTable.setStatus('current')
storageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "storageId"))
if mibBuilder.loadTexts: storageEntry.setStatus('current')
storageId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: storageId.setStatus('current')
storageName = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageName.setStatus('current')
storageDisruptionDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageDisruptionDetected.setStatus('current')
videoNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 2))
videoNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 2, 0))
alarmID = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmID.setStatus('current')
alarmName = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmName.setStatus('current')
alarmText = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmText.setStatus('current')
videoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3))
videoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3, 1))
videoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3, 2))
alarmNew = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 1)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmNew.setStatus('current')
alarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 2)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmCleared.setStatus('current')
alarmSingle = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 3)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmSingle.setStatus('current')
videoObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 1)).setObjects(("AXIS-VIDEO-MIB", "powerSupplyStatus"), ("AXIS-VIDEO-MIB", "fanStatus"), ("AXIS-VIDEO-MIB", "tempSensorStatus"), ("AXIS-VIDEO-MIB", "tempSensorValue"), ("AXIS-VIDEO-MIB", "videoSignalStatus"), ("AXIS-VIDEO-MIB", "audioSignalStatus"), ("AXIS-VIDEO-MIB", "casingName"), ("AXIS-VIDEO-MIB", "casingStatus"), ("AXIS-VIDEO-MIB", "storageDisruptionDetected"), ("AXIS-VIDEO-MIB", "storageName"), ("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoObjectGroup = videoObjectGroup.setStatus('obsolete')
videoNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 2)).setObjects(("AXIS-VIDEO-MIB", "alarmNew"), ("AXIS-VIDEO-MIB", "alarmCleared"), ("AXIS-VIDEO-MIB", "alarmSingle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoNotificationGroup = videoNotificationGroup.setStatus('current')
tempSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 3)).setObjects(("AXIS-VIDEO-MIB", "tempSensorStatus"), ("AXIS-VIDEO-MIB", "tempSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tempSensorGroup = tempSensorGroup.setStatus('current')
casingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 4)).setObjects(("AXIS-VIDEO-MIB", "casingName"), ("AXIS-VIDEO-MIB", "casingStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casingGroup = casingGroup.setStatus('current')
storageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 5)).setObjects(("AXIS-VIDEO-MIB", "storageDisruptionDetected"), ("AXIS-VIDEO-MIB", "storageName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageGroup = storageGroup.setStatus('current')
videoComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 2)).setObjects(("AXIS-VIDEO-MIB", "videoNotificationGroup"), ("AXIS-VIDEO-MIB", "powerSupplyStatus"), ("AXIS-VIDEO-MIB", "fanStatus"), ("AXIS-VIDEO-MIB", "tempSensorGroup"), ("AXIS-VIDEO-MIB", "videoSignalStatus"), ("AXIS-VIDEO-MIB", "audioSignalStatus"), ("AXIS-VIDEO-MIB", "casingGroup"), ("AXIS-VIDEO-MIB", "storageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoComplianceRev2 = videoComplianceRev2.setStatus('current')
videoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 1)).setObjects(("AXIS-VIDEO-MIB", "videoObjectGroup"), ("AXIS-VIDEO-MIB", "videoNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoCompliance = videoCompliance.setStatus('obsolete')
mibBuilder.exportSymbols("AXIS-VIDEO-MIB", tempSensorId=tempSensorId, alarmNew=alarmNew, audioChannelId=audioChannelId, fanTable=fanTable, storageDisruptionDetected=storageDisruptionDetected, videoObjectGroup=videoObjectGroup, storageTable=storageTable, video=video, videoBased=videoBased, videoObjects=videoObjects, audioSignalStatus=audioSignalStatus, powerSupplyStatus=powerSupplyStatus, videoChannelEntry=videoChannelEntry, alarmName=alarmName, videoConformance=videoConformance, fanEntry=fanEntry, tempSensorValue=tempSensorValue, alarmCleared=alarmCleared, tempSensorTable=tempSensorTable, powerSupplyTable=powerSupplyTable, casingId=casingId, audioChannelTable=audioChannelTable, alarmText=alarmText, alarmID=alarmID, tempSensorGroup=tempSensorGroup, videoCompliance=videoCompliance, fanStatus=fanStatus, powerSupplyType=powerSupplyType, fanType=fanType, casingTable=casingTable, storageName=storageName, videoCompliances=videoCompliances, powerSupplyEntry=powerSupplyEntry, casingEntry=casingEntry, videoNotificationGroup=videoNotificationGroup, videoChannelTable=videoChannelTable, audioChannelEntry=audioChannelEntry, videoSignalStatus=videoSignalStatus, casingGroup=casingGroup, videoChannelId=videoChannelId, tempSensorType=tempSensorType, fanId=fanId, casingStatus=casingStatus, PYSNMP_MODULE_ID=video, alarmSingle=alarmSingle, powerSupplyId=powerSupplyId, videoComplianceRev2=videoComplianceRev2, videoGroups=videoGroups, tempSensorEntry=tempSensorEntry, videoNotificationPrefix=videoNotificationPrefix, storageEntry=storageEntry, storageId=storageId, storageGroup=storageGroup, tempSensorStatus=tempSensorStatus, casingName=casingName, videoNotifications=videoNotifications)
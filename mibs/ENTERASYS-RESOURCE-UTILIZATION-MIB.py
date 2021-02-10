#
# PySNMP MIB module ENTERASYS-RESOURCE-UTILIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-RESOURCE-UTILIZATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, TimeTicks, Unsigned32, iso, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, NotificationType, MibIdentifier, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Unsigned32", "iso", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysResourceUtilizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49))
etsysResourceUtilizationMIB.setRevisions(('2009-11-02 15:41', '2004-11-30 16:33',))
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setLastUpdated('200911021541Z')
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setOrganization('Enterasys Networks, Inc')
class ResourceStorageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("ram", 2), ("flash", 3), ("usbFlash", 4))

class ResourceUtilization(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1000)

etsysResourceUtilizationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1))
etsysResourceUtilizationNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0))
etsysResourceCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1))
etsysResourceProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2))
etsysResourceStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3))
etsysResourceScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4))
etsysResourceCpuTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: etsysResourceCpuTable.setStatus('current')
etsysResourceCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"))
if mibBuilder.loadTexts: etsysResourceCpuEntry.setStatus('current')
etsysResourceCpuId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysResourceCpuId.setStatus('current')
etsysResourceCpuLoad5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 2), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad5sec.setStatus('current')
etsysResourceCpuLoad1min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 3), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad1min.setStatus('current')
etsysResourceCpuLoad5min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 4), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad5min.setStatus('current')
etsysResourceProcessTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1), )
if mibBuilder.loadTexts: etsysResourceProcessTable.setStatus('current')
etsysResourceProcessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessID"))
if mibBuilder.loadTexts: etsysResourceProcessEntry.setStatus('current')
etsysResourceProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysResourceProcessID.setStatus('current')
etsysResourceProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessName.setStatus('current')
etsysResourceProcessLoad5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 3), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad5sec.setStatus('current')
etsysResourceProcessLoad1min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 4), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad1min.setStatus('current')
etsysResourceProcessLoad5min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 5), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad5min.setStatus('current')
etsysResourceStorageTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1), )
if mibBuilder.loadTexts: etsysResourceStorageTable.setStatus('current')
etsysResourceStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageType"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageTypeID"))
if mibBuilder.loadTexts: etsysResourceStorageEntry.setStatus('current')
etsysResourceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 1), ResourceStorageType())
if mibBuilder.loadTexts: etsysResourceStorageType.setStatus('current')
etsysResourceStorageTypeID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: etsysResourceStorageTypeID.setStatus('current')
etsysResourceStorageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageDescr.setStatus('current')
etsysResourceStorageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageSize.setStatus('current')
etsysResourceStorageAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageAvailable.setStatus('current')
etsysResource1minThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4, 1), ResourceUtilization().clone(800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysResource1minThreshold.setStatus('current')
etsysResourceCpuLoad1minThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min"))
if mibBuilder.loadTexts: etsysResourceCpuLoad1minThresholdExceeded.setStatus('current')
etsysResourceUtilizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2))
etsysResourceUtilizationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1))
etsysResourceUtilizationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2))
etsysResourceUtilizationCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5sec"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationCpuGroup = etsysResourceUtilizationCpuGroup.setStatus('current')
etsysResourceUtilizationProcessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 2)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessName"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5sec"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad1min"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationProcessGroup = etsysResourceUtilizationProcessGroup.setStatus('current')
etsysResourceUtilizationStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 3)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageDescr"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageSize"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationStorageGroup = etsysResourceUtilizationStorageGroup.setStatus('current')
etsysResourceUtilizationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 4)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1minThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationNotificationGroup = etsysResourceUtilizationNotificationGroup.setStatus('current')
etsysResourceUtilizationScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 5)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResource1minThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationScalarsGroup = etsysResourceUtilizationScalarsGroup.setStatus('current')
etsysResourceUtilizationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationCpuGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationProcessGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationStorageGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationNotificationGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationScalarsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationCompliance = etsysResourceUtilizationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RESOURCE-UTILIZATION-MIB", etsysResourceUtilizationGroups=etsysResourceUtilizationGroups, etsysResourceProcess=etsysResourceProcess, etsysResourceStorage=etsysResourceStorage, etsysResourceProcessLoad5min=etsysResourceProcessLoad5min, etsysResource1minThreshold=etsysResource1minThreshold, etsysResourceUtilizationProcessGroup=etsysResourceUtilizationProcessGroup, etsysResourceUtilizationCompliance=etsysResourceUtilizationCompliance, PYSNMP_MODULE_ID=etsysResourceUtilizationMIB, etsysResourceUtilizationMIB=etsysResourceUtilizationMIB, etsysResourceCpuLoad1min=etsysResourceCpuLoad1min, ResourceUtilization=ResourceUtilization, etsysResourceUtilizationObjects=etsysResourceUtilizationObjects, etsysResourceStorageType=etsysResourceStorageType, etsysResourceStorageDescr=etsysResourceStorageDescr, etsysResourceStorageSize=etsysResourceStorageSize, etsysResourceUtilizationStorageGroup=etsysResourceUtilizationStorageGroup, etsysResourceCpuId=etsysResourceCpuId, etsysResourceCpuTable=etsysResourceCpuTable, etsysResourceStorageAvailable=etsysResourceStorageAvailable, etsysResourceUtilizationNotificationGroup=etsysResourceUtilizationNotificationGroup, etsysResourceCpuLoad5min=etsysResourceCpuLoad5min, etsysResourceUtilizationCpuGroup=etsysResourceUtilizationCpuGroup, etsysResourceProcessName=etsysResourceProcessName, etsysResourceCpuEntry=etsysResourceCpuEntry, etsysResourceProcessLoad5sec=etsysResourceProcessLoad5sec, etsysResourceUtilizationNotifications=etsysResourceUtilizationNotifications, etsysResourceCpuLoad1minThresholdExceeded=etsysResourceCpuLoad1minThresholdExceeded, etsysResourceUtilizationScalarsGroup=etsysResourceUtilizationScalarsGroup, etsysResourceStorageTable=etsysResourceStorageTable, etsysResourceUtilizationCompliances=etsysResourceUtilizationCompliances, ResourceStorageType=ResourceStorageType, etsysResourceProcessTable=etsysResourceProcessTable, etsysResourceStorageTypeID=etsysResourceStorageTypeID, etsysResourceProcessID=etsysResourceProcessID, etsysResourceUtilizationConformance=etsysResourceUtilizationConformance, etsysResourceProcessLoad1min=etsysResourceProcessLoad1min, etsysResourceScalars=etsysResourceScalars, etsysResourceProcessEntry=etsysResourceProcessEntry, etsysResourceStorageEntry=etsysResourceStorageEntry, etsysResourceCpu=etsysResourceCpu, etsysResourceCpuLoad5sec=etsysResourceCpuLoad5sec)

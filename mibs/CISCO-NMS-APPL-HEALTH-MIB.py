#
# PySNMP MIB module CISCO-NMS-APPL-HEALTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NMS-APPL-HEALTH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, iso, Gauge32, Bits, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "Gauge32", "Bits", "Counter32", "IpAddress", "TimeTicks")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
ciscoNmsApplHealthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 237))
ciscoNmsApplHealthMIB.setRevisions(('2001-10-24 00:00', '2001-10-15 00:00',))
if mibBuilder.loadTexts: ciscoNmsApplHealthMIB.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoNmsApplHealthMIB.setOrganization('Cisco Systems, Inc.')
ciscoNmsApplHealthNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 0))
ciscoNmsApplHealthMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 1))
ciscoNmsApplHealthMIBConforms = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 2))
cnaHealthObj = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1))
cnaHealthNotifSeqNum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthNotifSeqNum.setStatus('current')
cnaHealthTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2), )
if mibBuilder.loadTexts: cnaHealthTable.setStatus('current')
cnaHealthTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"))
if mibBuilder.loadTexts: cnaHealthTableEntry.setStatus('current')
cnaHealthTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthTableIndex.setStatus('current')
cnaHealthStatusChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthStatusChangeTime.setStatus('current')
cnaHealthName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthName.setStatus('current')
cnaHealthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("started", 1), ("stopped", 2), ("busy", 3), ("failed", 4), ("exited", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthStatus.setStatus('current')
cnaHealthSevLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 5), CiscoAlarmSeverity().clone('info')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthSevLevel.setStatus('current')
cnaHealthComLineArgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthComLineArgs.setStatus('current')
cnaHealthStatusDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnaHealthStatusDesc.setStatus('current')
cnaHealthNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 237, 0, 1)).setObjects(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
if mibBuilder.loadTexts: cnaHealthNotif.setStatus('current')
cnaHealthMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1))
cnaHealthMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2))
cnaHealthMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1, 1)).setObjects(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthMIBGroup"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnaHealthMIBCompliance = cnaHealthMIBCompliance.setStatus('current')
cnaHealthMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 1)).setObjects(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"), ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnaHealthMIBGroup = cnaHealthMIBGroup.setStatus('current')
cnaHealthNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 2)).setObjects(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnaHealthNotifGroup = cnaHealthNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NMS-APPL-HEALTH-MIB", cnaHealthMIBCompliance=cnaHealthMIBCompliance, ciscoNmsApplHealthMIBConforms=ciscoNmsApplHealthMIBConforms, cnaHealthTableEntry=cnaHealthTableEntry, cnaHealthName=cnaHealthName, cnaHealthComLineArgs=cnaHealthComLineArgs, cnaHealthStatusDesc=cnaHealthStatusDesc, cnaHealthStatusChangeTime=cnaHealthStatusChangeTime, cnaHealthMIBCompliances=cnaHealthMIBCompliances, cnaHealthMIBGroup=cnaHealthMIBGroup, cnaHealthStatus=cnaHealthStatus, cnaHealthNotifSeqNum=cnaHealthNotifSeqNum, cnaHealthTable=cnaHealthTable, cnaHealthObj=cnaHealthObj, ciscoNmsApplHealthMIB=ciscoNmsApplHealthMIB, cnaHealthTableIndex=cnaHealthTableIndex, cnaHealthSevLevel=cnaHealthSevLevel, ciscoNmsApplHealthNotifs=ciscoNmsApplHealthNotifs, cnaHealthNotifGroup=cnaHealthNotifGroup, ciscoNmsApplHealthMIBObjects=ciscoNmsApplHealthMIBObjects, cnaHealthMIBGroups=cnaHealthMIBGroups, cnaHealthNotif=cnaHealthNotif, PYSNMP_MODULE_ID=ciscoNmsApplHealthMIB)
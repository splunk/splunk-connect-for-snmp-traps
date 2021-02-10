#
# PySNMP MIB module ONEACCESS-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Bits, IpAddress, Counter64, NotificationType, TimeTicks, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "IpAddress", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter32")
TimeInterval, DisplayString, TestAndIncr, AutonomousType, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TestAndIncr", "AutonomousType", "TextualConvention", "TimeStamp")
oacUpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225))
if mibBuilder.loadTexts: oacUpsMIB.setLastUpdated('9402230000Z')
if mibBuilder.loadTexts: oacUpsMIB.setOrganization('IETF UPS MIB Working Group')
oacUpsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1))
oacUpsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1))
oacUpsBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsBatteryStatus.setStatus('current')
oacUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2))
oacUpsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmsPresent.setStatus('current')
oacUpsAlarmDescr = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 2), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmDescr.setStatus('current')
oacUpsAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmTime.setStatus('current')
oacUpsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2))
oacUpsTrapAlarmEntryAdded = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 0)).setObjects(("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr"))
if mibBuilder.loadTexts: oacUpsTrapAlarmEntryAdded.setStatus('current')
oacUpsTrapAlarmEntryRemoved = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 1)).setObjects(("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr"))
if mibBuilder.loadTexts: oacUpsTrapAlarmEntryRemoved.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-UPS-MIB", PYSNMP_MODULE_ID=oacUpsMIB, oacUpsTrapAlarmEntryAdded=oacUpsTrapAlarmEntryAdded, oacUpsAlarmDescr=oacUpsAlarmDescr, oacUpsTrapAlarmEntryRemoved=oacUpsTrapAlarmEntryRemoved, oacUpsTraps=oacUpsTraps, oacUpsAlarmTime=oacUpsAlarmTime, oacUpsAlarm=oacUpsAlarm, oacUpsMIBObjects=oacUpsMIBObjects, oacUpsAlarmsPresent=oacUpsAlarmsPresent, oacUpsBatteryStatus=oacUpsBatteryStatus, oacUpsBattery=oacUpsBattery, oacUpsMIB=oacUpsMIB)

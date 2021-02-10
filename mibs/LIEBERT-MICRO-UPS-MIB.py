#
# PySNMP MIB module LIEBERT-MICRO-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIEBERT-MICRO-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Bits, ModuleIdentity, Counter32, iso, MibIdentifier, Gauge32, NotificationType, enterprises, ObjectIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Counter32", "iso", "MibIdentifier", "Gauge32", "NotificationType", "enterprises", "ObjectIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
emerson = MibIdentifier((1, 3, 6, 1, 4, 1, 476))
liebertCorp = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1))
liebertUps = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1))
luExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1))
luExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 2))
luPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 3))
luCore = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1))
lcUpsIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1))
lcUpsIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentManufacturer.setStatus('optional')
lcUpsIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsIdentModel.setStatus('optional')
lcUpsIdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentSoftwareVersion.setStatus('optional')
lcUpsIdentSpecific = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentSpecific.setStatus('optional')
lcUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6))
lcUpsAlarms = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarms.setStatus('optional')
lcUpsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2), )
if mibBuilder.loadTexts: lcUpsAlarmTable.setStatus('optional')
lcUpsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1), ).setIndexNames((0, "LIEBERT-MICRO-UPS-MIB", "lcUpsAlarmId"))
if mibBuilder.loadTexts: lcUpsAlarmEntry.setStatus('optional')
lcUpsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmId.setStatus('optional')
lcUpsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmDescr.setStatus('optional')
lcUpsAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmTime.setStatus('optional')
lcUpsAlarmConditions = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3))
lcUpsAlarmLowBatteryWarning = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 1))
lcUpsAlarmOnBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10))
lcUpsAlarmStopNoticeIssued = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 11))
lcUpsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8))
lcUpsControlUnixShutdownDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlUnixShutdownDelay.setStatus('optional')
lcUpsControlUnixShutdownTrapDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlUnixShutdownTrapDelay.setStatus('optional')
lcUpsControlCancelCommands = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("cancel", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlCancelCommands.setStatus('optional')
lcUpsControlRebootAgentDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlRebootAgentDelay.setStatus('optional')
lcUpsNominal = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9))
lcUpsNominalOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputVoltage.setStatus('optional')
lcUpsNominalInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalInputVoltage.setStatus('optional')
lcUpsNominalOutputVA = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputVA.setStatus('optional')
lcUpsNominalOutputWatts = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputWatts.setStatus('optional')
lcUpsNominalOutputFreq = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputFreq.setStatus('optional')
lcUpsNominalInputFreq = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalInputFreq.setStatus('optional')
lcUpsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11))
lcUpsOnBatteryTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsLowBatteryWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,11)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUnixShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,16)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUnixShutdownWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,17)).setObjects(("SNMPv2-MIB", "sysUpTime"))
luExternal = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 6))
mibBuilder.exportSymbols("LIEBERT-MICRO-UPS-MIB", lcUpsNominalOutputVoltage=lcUpsNominalOutputVoltage, lcUpsIdentSpecific=lcUpsIdentSpecific, lcUpsAlarmTime=lcUpsAlarmTime, lcUpsIdentModel=lcUpsIdentModel, lcUpsAlarmStopNoticeIssued=lcUpsAlarmStopNoticeIssued, lcUpsControl=lcUpsControl, lcUpsTraps=lcUpsTraps, lcUpsNominalOutputWatts=lcUpsNominalOutputWatts, lcUpsUnixShutdownWarningTrap=lcUpsUnixShutdownWarningTrap, luCore=luCore, lcUpsNominalOutputFreq=lcUpsNominalOutputFreq, lcUpsAlarmEntry=lcUpsAlarmEntry, lcUpsOnBatteryTrap=lcUpsOnBatteryTrap, lcUpsAlarmId=lcUpsAlarmId, emerson=emerson, luExperimental=luExperimental, lcUpsAlarmTable=lcUpsAlarmTable, lcUpsNominalInputVoltage=lcUpsNominalInputVoltage, lcUpsControlRebootAgentDelay=lcUpsControlRebootAgentDelay, luExternal=luExternal, liebertUps=liebertUps, lcUpsNominalOutputVA=lcUpsNominalOutputVA, lcUpsAlarmDescr=lcUpsAlarmDescr, lcUpsAlarmConditions=lcUpsAlarmConditions, lcUpsControlCancelCommands=lcUpsControlCancelCommands, lcUpsIdentSoftwareVersion=lcUpsIdentSoftwareVersion, lcUpsLowBatteryWarningTrap=lcUpsLowBatteryWarningTrap, liebertCorp=liebertCorp, lcUpsUnixShutdownTrap=lcUpsUnixShutdownTrap, lcUpsAlarmTrap=lcUpsAlarmTrap, lcUpsAlarm=lcUpsAlarm, lcUpsControlUnixShutdownTrapDelay=lcUpsControlUnixShutdownTrapDelay, lcUpsControlUnixShutdownDelay=lcUpsControlUnixShutdownDelay, lcUpsAlarms=lcUpsAlarms, lcUpsAlarmOnBattery=lcUpsAlarmOnBattery, lcUpsIdent=lcUpsIdent, lcUpsNominal=lcUpsNominal, lcUpsAlarmLowBatteryWarning=lcUpsAlarmLowBatteryWarning, lcUpsIdentManufacturer=lcUpsIdentManufacturer, lcUpsNominalInputFreq=lcUpsNominalInputFreq, luExtensions=luExtensions, luPrivate=luPrivate)

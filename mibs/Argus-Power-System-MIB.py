#
# PySNMP MIB module Argus-Power-System-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Argus-Power-System-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, ObjectIdentity, iso, TimeTicks, NotificationType, Bits, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Unsigned32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
argus = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309))
argus.setRevisions(('2016-12-09 00:00',))
if mibBuilder.loadTexts: argus.setLastUpdated('201612090000Z')
if mibBuilder.loadTexts: argus.setOrganization('Alpha Technologies Ltd.')
class PositiveInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

upsPower = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6))
upsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1))
upsIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1))
upsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2))
upsInput = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3))
upsOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4))
upsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5))
upsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6))
upsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7))
upsExtra = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8))
upsExtraCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraCount.setStatus('current')
upsExtraTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2), )
if mibBuilder.loadTexts: upsExtraTable.setStatus('current')
upsExtraEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsExtraIndex"))
if mibBuilder.loadTexts: upsExtraEntry.setStatus('current')
upsExtraIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraIndex.setStatus('current')
upsExtraName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraName.setStatus('current')
upsExtraIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1000000000, 1000000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraIntegerValue.setStatus('current')
upsExtraStringValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtraStringValue.setStatus('current')
upsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0))
upsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 1)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAlarmTrap.setStatus('current')
upsAgentStartupTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 2)).setObjects(("Argus-Power-System-MIB", "upsIdentSiteName"))
if mibBuilder.loadTexts: upsAgentStartupTrap.setStatus('current')
upsAgentShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 3)).setObjects(("Argus-Power-System-MIB", "upsIdentSiteName"))
if mibBuilder.loadTexts: upsAgentShutdownTrap.setStatus('current')
upsAgentFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 4)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAgentFaultTrap.setStatus('current')
upsAgentEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 5)).setObjects(("Argus-Power-System-MIB", "upsExtraIntegerValue"), ("Argus-Power-System-MIB", "upsExtraStringValue"), ("Argus-Power-System-MIB", "upsExtraIndex"), ("Argus-Power-System-MIB", "upsExtraName"))
if mibBuilder.loadTexts: upsAgentEventTrap.setStatus('current')
upsIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentManufacturer.setStatus('current')
upsIdentProductCode = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentProductCode.setStatus('current')
upsIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentModel.setStatus('current')
upsIdentUPSSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentUPSSoftwareVersion.setStatus('current')
upsIdentAgentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentAgentSoftwareVersion.setStatus('current')
upsIdentName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentName.setStatus('current')
upsIdentAttachedDevices = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentAttachedDevices.setStatus('current')
upsIdentSiteName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteName.setStatus('current')
upsIdentSiteCity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteCity.setStatus('current')
upsIdentSiteRegion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteRegion.setStatus('current')
upsIdentSiteCountry = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentSiteCountry.setStatus('current')
upsIdentContactName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentContactName.setStatus('current')
upsIdentPhoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentPhoneNumber.setStatus('current')
upsIdentDate = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentDate.setStatus('current')
upsIdentTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentTime.setStatus('current')
upsBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryStatus.setStatus('current')
upsMinutesOnBattery = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 2), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsMinutesOnBattery.setStatus('current')
upsBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 3), Integer32()).setUnits('0.1 Volt DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryVoltage.setStatus('current')
upsBatteryChargingCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 4), Integer32()).setUnits('0.1 Amp DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryChargingCurrent.setStatus('current')
upsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 5), Integer32()).setUnits('0.1 Amp DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryCapacity.setStatus('current')
upsBatteryTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 6), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryTemperature.setStatus('current')
upsBatteryLowWarning = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 7), Integer32()).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsBatteryLowWarning.setStatus('current')
upsInputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputNumLines.setStatus('current')
upsInputTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2), )
if mibBuilder.loadTexts: upsInputTable.setStatus('current')
upsInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsInputLineIndex"))
if mibBuilder.loadTexts: upsInputEntry.setStatus('current')
upsInputLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: upsInputLineIndex.setStatus('current')
upsInputFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 2), Integer32()).setUnits('Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputFrequency.setStatus('current')
upsInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 3), Integer32()).setUnits('0.1 RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputVoltage.setStatus('current')
upsOutputSource = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("standby", 1), ("line", 2), ("boost2", 3), ("boost1", 4), ("buck1", 5), ("buck2", 6), ("inverter", 7), ("retransfer", 8), ("transfer", 9), ("shutdown", 10), ("bypass", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputSource.setStatus('current')
upsOutputFrequency = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 2), Integer32()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputFrequency.setStatus('current')
upsOutputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputNumLines.setStatus('current')
upsOutputTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4), )
if mibBuilder.loadTexts: upsOutputTable.setStatus('current')
upsOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsOutputLineIndex"))
if mibBuilder.loadTexts: upsOutputEntry.setStatus('current')
upsOutputLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: upsOutputLineIndex.setStatus('current')
upsOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 2), Integer32()).setUnits('0.1 RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputVoltage.setStatus('current')
upsOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 3), Integer32()).setUnits('0.1 RMS Amp').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputCurrent.setStatus('current')
upsOutputPowerVA = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 4), Integer32()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPowerVA.setStatus('current')
upsOutputPowerWatt = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 5), Integer32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPowerWatt.setStatus('current')
upsPowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 6), Integer32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsPowerFactor.setStatus('current')
upsOutputPercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPercentLoad.setStatus('current')
upsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmsPresent.setStatus('current')
upsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2), )
if mibBuilder.loadTexts: upsAlarmTable.setStatus('current')
upsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1), ).setIndexNames((0, "Argus-Power-System-MIB", "upsAlarmId"))
if mibBuilder.loadTexts: upsAlarmEntry.setStatus('current')
upsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: upsAlarmId.setStatus('current')
upsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmDescr.setStatus('current')
upsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmStatus.setStatus('current')
upsConfigLineQualifyTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 1), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineQualifyTime.setStatus('current')
upsConfigLineOutputVoltageHighLimit = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 2), Integer32()).setUnits('volttenth').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineOutputVoltageHighLimit.setStatus('current')
upsConfigLineOutputVoltageLowLimit = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 3), Integer32()).setUnits('volttenth').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigLineOutputVoltageLowLimit.setStatus('current')
upsConfigFanOnTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 4), Integer32()).setUnits('degreeC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigFanOnTemperature.setStatus('current')
upsShutdownStatus = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 5), Integer32()).setUnits('').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsShutdownStatus.setStatus('current')
upsInverterOffDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 6), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsInverterOffDelayTime.setStatus('current')
upsConfigIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigIPAddress.setStatus('current')
upsConfigNetMask = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigNetMask.setStatus('current')
upsConfigGateway = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigGateway.setStatus('current')
upsConfigSnmpCommunity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigSnmpCommunity.setStatus('current')
upsConfigSnmpTrapIPDestination = MibScalar((1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigSnmpTrapIPDestination.setStatus('current')
mibBuilder.exportSymbols("Argus-Power-System-MIB", upsExtraEntry=upsExtraEntry, upsConfig=upsConfig, upsTrap=upsTrap, upsInputLineIndex=upsInputLineIndex, upsExtraStringValue=upsExtraStringValue, upsExtra=upsExtra, upsIdentTime=upsIdentTime, upsExtraCount=upsExtraCount, upsInputVoltage=upsInputVoltage, upsAlarmTable=upsAlarmTable, upsPowerFactor=upsPowerFactor, upsAlarmId=upsAlarmId, upsIdentSiteRegion=upsIdentSiteRegion, upsOutputEntry=upsOutputEntry, upsMinutesOnBattery=upsMinutesOnBattery, upsConfigLineQualifyTime=upsConfigLineQualifyTime, upsAlarmStatus=upsAlarmStatus, upsConfigLineOutputVoltageHighLimit=upsConfigLineOutputVoltageHighLimit, upsInput=upsInput, upsBatteryVoltage=upsBatteryVoltage, upsIdentAttachedDevices=upsIdentAttachedDevices, upsIdentSiteCity=upsIdentSiteCity, upsConfigIPAddress=upsConfigIPAddress, upsShutdownStatus=upsShutdownStatus, upsIdentPhoneNumber=upsIdentPhoneNumber, upsIdentSiteName=upsIdentSiteName, upsInputEntry=upsInputEntry, upsInputFrequency=upsInputFrequency, upsConfigSnmpTrapIPDestination=upsConfigSnmpTrapIPDestination, upsInverterOffDelayTime=upsInverterOffDelayTime, upsExtraIndex=upsExtraIndex, upsOutputTable=upsOutputTable, upsIdentProductCode=upsIdentProductCode, upsConfigFanOnTemperature=upsConfigFanOnTemperature, upsOutputCurrent=upsOutputCurrent, upsBatteryCapacity=upsBatteryCapacity, upsIdentAgentSoftwareVersion=upsIdentAgentSoftwareVersion, upsOutputNumLines=upsOutputNumLines, upsOutputSource=upsOutputSource, upsIdentContactName=upsIdentContactName, upsAlarm=upsAlarm, upsExtraIntegerValue=upsExtraIntegerValue, upsBatteryChargingCurrent=upsBatteryChargingCurrent, upsIdentSiteCountry=upsIdentSiteCountry, upsBattery=upsBattery, upsExtraTable=upsExtraTable, upsOutputPowerWatt=upsOutputPowerWatt, upsOutputFrequency=upsOutputFrequency, upsOutputPercentLoad=upsOutputPercentLoad, upsIdentDate=upsIdentDate, upsAgentEventTrap=upsAgentEventTrap, upsInputTable=upsInputTable, upsAgentStartupTrap=upsAgentStartupTrap, argus=argus, upsInputNumLines=upsInputNumLines, upsDevice=upsDevice, NonNegativeInteger=NonNegativeInteger, upsExtraName=upsExtraName, upsAlarmDescr=upsAlarmDescr, upsOutput=upsOutput, upsAlarmTrap=upsAlarmTrap, upsOutputPowerVA=upsOutputPowerVA, upsConfigGateway=upsConfigGateway, PositiveInteger=PositiveInteger, PYSNMP_MODULE_ID=argus, upsConfigNetMask=upsConfigNetMask, upsAlarmEntry=upsAlarmEntry, PhysAddress=PhysAddress, upsConfigSnmpCommunity=upsConfigSnmpCommunity, upsOutputLineIndex=upsOutputLineIndex, upsIdentModel=upsIdentModel, upsIdentName=upsIdentName, upsTraps=upsTraps, DisplayString=DisplayString, upsIdentUPSSoftwareVersion=upsIdentUPSSoftwareVersion, upsBatteryTemperature=upsBatteryTemperature, upsIdent=upsIdent, upsOutputVoltage=upsOutputVoltage, upsBatteryLowWarning=upsBatteryLowWarning, upsAlarmsPresent=upsAlarmsPresent, upsAgentFaultTrap=upsAgentFaultTrap, upsConfigLineOutputVoltageLowLimit=upsConfigLineOutputVoltageLowLimit, upsBatteryStatus=upsBatteryStatus, upsPower=upsPower, upsAgentShutdownTrap=upsAgentShutdownTrap, upsIdentManufacturer=upsIdentManufacturer)
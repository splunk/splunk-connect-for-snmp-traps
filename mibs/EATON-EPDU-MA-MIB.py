#
# PySNMP MIB module EATON-EPDU-MA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EATON-EPDU-MA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
pduAgent, = mibBuilder.importSymbols("EATON-OIDS", "pduAgent")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, MibIdentifier, Integer32, Gauge32, Counter32, TimeTicks, Counter64, ObjectIdentity, iso, ModuleIdentity, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
eatonEpduMa = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 6, 6, 6))
eatonEpduMa.setRevisions(('2008-11-12 00:00', '2008-03-14 00:00', '2007-02-14 00:00',))
if mibBuilder.loadTexts: eatonEpduMa.setLastUpdated('200811120000Z')
if mibBuilder.loadTexts: eatonEpduMa.setOrganization('Eaton Corporation')
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0))
board = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1))
environmental = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2))
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1))
outlets = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2))
unit = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3))
unitReadings = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 1))
groups = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2))
class MilliAmps(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd milliamps'

class MilliVolts(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd millivolts'

class Watts(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd watt'

class VoltAmps(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd volt-amp'

class DegreesCelsius(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd degree Celsius'

class RelativeHumidity(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd %'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class PowerFactorPercentage(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
ipAddress = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddress.setStatus('current')
netmask = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netmask.setStatus('current')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gateway.setStatus('current')
mac = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mac.setStatus('current')
hardwareRev = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareRev.setStatus('current')
userName = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: userName.setStatus('current')
objectName = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 12), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: objectName.setStatus('current')
objectInstance = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: objectInstance.setStatus('current')
targetUser = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: targetUser.setStatus('current')
groupName = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 15), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: groupName.setStatus('current')
imageVersion = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 18), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: imageVersion.setStatus('current')
sensorDescr = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 19), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sensorDescr.setStatus('current')
thresholdDescr = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 20), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: thresholdDescr.setStatus('current')
thresholdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 21), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: thresholdSeverity.setStatus('current')
thresholdEventType = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 22), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: thresholdEventType.setStatus('current')
status = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 23), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: status.setStatus('current')
slaveIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 24), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slaveIpAddress.setStatus('current')
outletCount = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletCount.setStatus('current')
outletTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2), )
if mibBuilder.loadTexts: outletTable.setStatus('current')
outletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1), ).setIndexNames((0, "EATON-EPDU-MA-MIB", "outletIndex"))
if mibBuilder.loadTexts: outletEntry.setStatus('current')
outletIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: outletIndex.setStatus('current')
outletLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletLabel.setStatus('current')
outletOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2))).clone(namedValues=NamedValues(("error", -1), ("off", 0), ("on", 1), ("cycling", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletOperationalState.setStatus('current')
outletCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 4), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletCurrent.setStatus('current')
outletMaxCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 5), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletMaxCurrent.setStatus('current')
outletVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 6), MilliVolts()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletVoltage.setStatus('current')
outletActivePower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 7), Watts()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletActivePower.setStatus('current')
outletApparentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 8), VoltAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletApparentPower.setStatus('current')
outletPowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 9), PowerFactorPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletPowerFactor.setStatus('current')
outletCurrentUpperWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 21), MilliAmps()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletCurrentUpperWarning.setStatus('current')
outletCurrentUpperCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 23), MilliAmps()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletCurrentUpperCritical.setStatus('current')
unitCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 1), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCurrent.setStatus('current')
unitVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 2), MilliVolts()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitVoltage.setStatus('current')
unitActivePower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 3), Watts()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitActivePower.setStatus('current')
unitApparentPower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 4), Watts()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitApparentPower.setStatus('current')
unitCpuTemp = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 5), DegreesCelsius()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCpuTemp.setStatus('current')
unitCircuitBreak0State = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("unavailable", -1), ("ok", 0), ("tripped", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak0State.setStatus('current')
unitCircuitBreak1State = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("unavailable", -1), ("ok", 0), ("tripped", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak1State.setStatus('current')
unitCircuitBreak2State = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("unavailable", -1), ("ok", 0), ("tripped", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak2State.setStatus('current')
unitCircuitBreak0Current = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 40), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak0Current.setStatus('current')
unitCircuitBreak1Current = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 41), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak1Current.setStatus('current')
unitCircuitBreak2Current = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 42), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCircuitBreak2Current.setStatus('current')
unitVoltageLowerWarning = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 60), MilliVolts()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitVoltageLowerWarning.setStatus('current')
unitVoltageLowerCritical = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 61), MilliVolts()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitVoltageLowerCritical.setStatus('current')
unitVoltageUpperWarning = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 62), MilliVolts()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitVoltageUpperWarning.setStatus('current')
unitVoltageUpperCritical = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 63), MilliVolts()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitVoltageUpperCritical.setStatus('current')
unitCurrentUpperWarning = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 70), MilliAmps()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitCurrentUpperWarning.setStatus('current')
unitCurrentUpperCritical = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 71), MilliAmps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitCurrentUpperCritical.setStatus('current')
unitTempLowerWarning = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 80), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitTempLowerWarning.setStatus('current')
unitTempLowerCritical = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 81), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitTempLowerCritical.setStatus('current')
unitTempUpperWarning = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 82), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitTempUpperWarning.setStatus('current')
unitTempUpperCritical = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 83), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitTempUpperCritical.setStatus('current')
tempSensorCount = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorCount.setStatus('current')
tempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2), )
if mibBuilder.loadTexts: tempSensorTable.setStatus('current')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1), ).setIndexNames((0, "EATON-EPDU-MA-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('current')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: tempSensorIndex.setStatus('current')
tempSensorLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempSensorLabel.setStatus('current')
temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 3), DegreesCelsius()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
tempLowerWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 4), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempLowerWarning.setStatus('current')
tempUpperWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 5), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempUpperWarning.setStatus('current')
tempLowerCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 6), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempLowerCritical.setStatus('current')
tempUpperCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 7), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempUpperCritical.setStatus('current')
tempLowerWarningReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 8), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempLowerWarningReset.setStatus('current')
tempUpperWarningReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 9), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempUpperWarningReset.setStatus('current')
tempLowerCriticalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 10), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempLowerCriticalReset.setStatus('current')
tempUpperCriticalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 11), DegreesCelsius()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempUpperCriticalReset.setStatus('current')
humiditySensorCount = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: humiditySensorCount.setStatus('current')
humiditySensorTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4), )
if mibBuilder.loadTexts: humiditySensorTable.setStatus('current')
humiditySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1), ).setIndexNames((0, "EATON-EPDU-MA-MIB", "humiditySensorIndex"))
if mibBuilder.loadTexts: humiditySensorEntry.setStatus('current')
humiditySensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: humiditySensorIndex.setStatus('current')
humiditySensorLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humiditySensorLabel.setStatus('current')
humidity = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 3), RelativeHumidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidity.setStatus('current')
humidityLowerWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 4), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityLowerWarning.setStatus('current')
humidityUpperWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 5), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityUpperWarning.setStatus('current')
humidityLowerCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 6), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityLowerCritical.setStatus('current')
humidityUpperCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 7), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityUpperCritical.setStatus('current')
humidityLowerWarningReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 8), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityLowerWarningReset.setStatus('current')
humidityUpperWarningReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 9), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityUpperWarningReset.setStatus('current')
humidityLowerCriticalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 10), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityLowerCriticalReset.setStatus('current')
humidityUpperCriticalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 11), RelativeHumidity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityUpperCriticalReset.setStatus('current')
rebootStarted = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 1)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"))
if mibBuilder.loadTexts: rebootStarted.setStatus('current')
rebootCompleted = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 2)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"))
if mibBuilder.loadTexts: rebootCompleted.setStatus('current')
userLogin = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 3)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userLogin.setStatus('current')
userLogout = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 4)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userLogout.setStatus('current')
userAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 5)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userAuthenticationFailure.setStatus('current')
userSessionTimeout = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 8)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userSessionTimeout.setStatus('current')
userAdded = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 11)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "targetUser"))
if mibBuilder.loadTexts: userAdded.setStatus('current')
userModified = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 12)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "targetUser"))
if mibBuilder.loadTexts: userModified.setStatus('current')
userDeleted = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 13)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "targetUser"))
if mibBuilder.loadTexts: userDeleted.setStatus('current')
groupAdded = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 14)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "groupName"))
if mibBuilder.loadTexts: groupAdded.setStatus('current')
groupModified = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 15)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "groupName"))
if mibBuilder.loadTexts: groupModified.setStatus('current')
groupDeleted = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 16)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "groupName"))
if mibBuilder.loadTexts: groupDeleted.setStatus('current')
deviceUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 20)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"), ("EATON-EPDU-MA-MIB", "imageVersion"))
if mibBuilder.loadTexts: deviceUpdateStarted.setStatus('current')
userBlocked = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 22)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userBlocked.setStatus('current')
powerControl = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 23)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"), ("EATON-EPDU-MA-MIB", "outletLabel"), ("EATON-EPDU-MA-MIB", "outletOperationalState"))
if mibBuilder.loadTexts: powerControl.setStatus('current')
userPasswordChanged = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 24)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "targetUser"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: userPasswordChanged.setStatus('current')
passwordSettingsChanged = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 28)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "status"))
if mibBuilder.loadTexts: passwordSettingsChanged.setStatus('current')
firmwareFileDiscarded = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 36)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"))
if mibBuilder.loadTexts: firmwareFileDiscarded.setStatus('current')
firmwareValidationFailed = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 38)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"))
if mibBuilder.loadTexts: firmwareValidationFailed.setStatus('current')
securityViolation = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 39)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "ipAddress"))
if mibBuilder.loadTexts: securityViolation.setStatus('current')
logFileCleared = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 41)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "userName"))
if mibBuilder.loadTexts: logFileCleared.setStatus('current')
thresholdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 45)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "ipAddress"), ("EATON-EPDU-MA-MIB", "sensorDescr"), ("EATON-EPDU-MA-MIB", "thresholdDescr"), ("EATON-EPDU-MA-MIB", "thresholdSeverity"), ("EATON-EPDU-MA-MIB", "thresholdEventType"))
if mibBuilder.loadTexts: thresholdAlarm.setStatus('current')
outletGroupingConnectivityLost = NotificationType((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 50)).setObjects(("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "ipAddress"), ("EATON-EPDU-MA-MIB", "slaveIpAddress"))
if mibBuilder.loadTexts: outletGroupingConnectivityLost.setStatus('current')
compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 1, 1)).setObjects(("EATON-EPDU-MA-MIB", "infoGroup"), ("EATON-EPDU-MA-MIB", "outletsGroup"), ("EATON-EPDU-MA-MIB", "unitSensorsGroup"), ("EATON-EPDU-MA-MIB", "externalTemperatureGroup"), ("EATON-EPDU-MA-MIB", "externalHumidityGroup"), ("EATON-EPDU-MA-MIB", "trapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    compliance = compliance.setStatus('current')
infoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 1)).setObjects(("EATON-EPDU-MA-MIB", "firmwareVersion"), ("EATON-EPDU-MA-MIB", "serialNumber"), ("EATON-EPDU-MA-MIB", "ipAddress"), ("EATON-EPDU-MA-MIB", "netmask"), ("EATON-EPDU-MA-MIB", "gateway"), ("EATON-EPDU-MA-MIB", "mac"), ("EATON-EPDU-MA-MIB", "hardwareRev"), ("EATON-EPDU-MA-MIB", "userName"), ("EATON-EPDU-MA-MIB", "objectName"), ("EATON-EPDU-MA-MIB", "objectInstance"), ("EATON-EPDU-MA-MIB", "targetUser"), ("EATON-EPDU-MA-MIB", "groupName"), ("EATON-EPDU-MA-MIB", "imageVersion"), ("EATON-EPDU-MA-MIB", "sensorDescr"), ("EATON-EPDU-MA-MIB", "thresholdDescr"), ("EATON-EPDU-MA-MIB", "thresholdSeverity"), ("EATON-EPDU-MA-MIB", "thresholdEventType"), ("EATON-EPDU-MA-MIB", "status"), ("EATON-EPDU-MA-MIB", "slaveIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    infoGroup = infoGroup.setStatus('current')
outletsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 2)).setObjects(("EATON-EPDU-MA-MIB", "outletCount"), ("EATON-EPDU-MA-MIB", "outletLabel"), ("EATON-EPDU-MA-MIB", "outletOperationalState"), ("EATON-EPDU-MA-MIB", "outletCurrent"), ("EATON-EPDU-MA-MIB", "outletMaxCurrent"), ("EATON-EPDU-MA-MIB", "outletVoltage"), ("EATON-EPDU-MA-MIB", "outletActivePower"), ("EATON-EPDU-MA-MIB", "outletApparentPower"), ("EATON-EPDU-MA-MIB", "outletPowerFactor"), ("EATON-EPDU-MA-MIB", "outletCurrentUpperWarning"), ("EATON-EPDU-MA-MIB", "outletCurrentUpperCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    outletsGroup = outletsGroup.setStatus('current')
unitSensorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 4)).setObjects(("EATON-EPDU-MA-MIB", "unitCurrent"), ("EATON-EPDU-MA-MIB", "unitVoltage"), ("EATON-EPDU-MA-MIB", "unitActivePower"), ("EATON-EPDU-MA-MIB", "unitApparentPower"), ("EATON-EPDU-MA-MIB", "unitCpuTemp"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak0State"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak1State"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak2State"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak0Current"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak1Current"), ("EATON-EPDU-MA-MIB", "unitCircuitBreak2Current"), ("EATON-EPDU-MA-MIB", "unitVoltageLowerWarning"), ("EATON-EPDU-MA-MIB", "unitVoltageUpperWarning"), ("EATON-EPDU-MA-MIB", "unitVoltageLowerCritical"), ("EATON-EPDU-MA-MIB", "unitVoltageUpperCritical"), ("EATON-EPDU-MA-MIB", "unitCurrentUpperWarning"), ("EATON-EPDU-MA-MIB", "unitCurrentUpperCritical"), ("EATON-EPDU-MA-MIB", "unitTempLowerWarning"), ("EATON-EPDU-MA-MIB", "unitTempUpperWarning"), ("EATON-EPDU-MA-MIB", "unitTempLowerCritical"), ("EATON-EPDU-MA-MIB", "unitTempUpperCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unitSensorsGroup = unitSensorsGroup.setStatus('current')
externalTemperatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 6)).setObjects(("EATON-EPDU-MA-MIB", "tempSensorCount"), ("EATON-EPDU-MA-MIB", "tempSensorLabel"), ("EATON-EPDU-MA-MIB", "temperature"), ("EATON-EPDU-MA-MIB", "tempLowerWarning"), ("EATON-EPDU-MA-MIB", "tempUpperWarning"), ("EATON-EPDU-MA-MIB", "tempLowerCritical"), ("EATON-EPDU-MA-MIB", "tempUpperCritical"), ("EATON-EPDU-MA-MIB", "tempLowerWarningReset"), ("EATON-EPDU-MA-MIB", "tempUpperWarningReset"), ("EATON-EPDU-MA-MIB", "tempLowerCriticalReset"), ("EATON-EPDU-MA-MIB", "tempUpperCriticalReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalTemperatureGroup = externalTemperatureGroup.setStatus('current')
externalHumidityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 7)).setObjects(("EATON-EPDU-MA-MIB", "humiditySensorCount"), ("EATON-EPDU-MA-MIB", "humiditySensorLabel"), ("EATON-EPDU-MA-MIB", "humidity"), ("EATON-EPDU-MA-MIB", "humidityLowerWarning"), ("EATON-EPDU-MA-MIB", "humidityUpperWarning"), ("EATON-EPDU-MA-MIB", "humidityLowerCritical"), ("EATON-EPDU-MA-MIB", "humidityUpperCritical"), ("EATON-EPDU-MA-MIB", "humidityLowerWarningReset"), ("EATON-EPDU-MA-MIB", "humidityUpperWarningReset"), ("EATON-EPDU-MA-MIB", "humidityLowerCriticalReset"), ("EATON-EPDU-MA-MIB", "humidityUpperCriticalReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalHumidityGroup = externalHumidityGroup.setStatus('current')
trapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 9)).setObjects(("EATON-EPDU-MA-MIB", "rebootStarted"), ("EATON-EPDU-MA-MIB", "rebootCompleted"), ("EATON-EPDU-MA-MIB", "userLogin"), ("EATON-EPDU-MA-MIB", "userLogout"), ("EATON-EPDU-MA-MIB", "userAuthenticationFailure"), ("EATON-EPDU-MA-MIB", "userSessionTimeout"), ("EATON-EPDU-MA-MIB", "userAdded"), ("EATON-EPDU-MA-MIB", "userModified"), ("EATON-EPDU-MA-MIB", "userDeleted"), ("EATON-EPDU-MA-MIB", "groupAdded"), ("EATON-EPDU-MA-MIB", "groupModified"), ("EATON-EPDU-MA-MIB", "groupDeleted"), ("EATON-EPDU-MA-MIB", "deviceUpdateStarted"), ("EATON-EPDU-MA-MIB", "userBlocked"), ("EATON-EPDU-MA-MIB", "powerControl"), ("EATON-EPDU-MA-MIB", "userPasswordChanged"), ("EATON-EPDU-MA-MIB", "passwordSettingsChanged"), ("EATON-EPDU-MA-MIB", "firmwareFileDiscarded"), ("EATON-EPDU-MA-MIB", "firmwareValidationFailed"), ("EATON-EPDU-MA-MIB", "securityViolation"), ("EATON-EPDU-MA-MIB", "logFileCleared"), ("EATON-EPDU-MA-MIB", "thresholdAlarm"), ("EATON-EPDU-MA-MIB", "outletGroupingConnectivityLost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapsGroup = trapsGroup.setStatus('current')
mibBuilder.exportSymbols("EATON-EPDU-MA-MIB", mac=mac, groupModified=groupModified, unitCurrent=unitCurrent, netmask=netmask, compliances=compliances, outletCount=outletCount, outletGroupingConnectivityLost=outletGroupingConnectivityLost, unitCircuitBreak0Current=unitCircuitBreak0Current, serialNumber=serialNumber, outletMaxCurrent=outletMaxCurrent, unitCircuitBreak1Current=unitCircuitBreak1Current, outletCurrent=outletCurrent, tempSensorIndex=tempSensorIndex, objectInstance=objectInstance, unitTempLowerCritical=unitTempLowerCritical, thresholdSeverity=thresholdSeverity, board=board, humidityLowerWarning=humidityLowerWarning, ipAddress=ipAddress, tempUpperWarningReset=tempUpperWarningReset, userAdded=userAdded, tempLowerWarning=tempLowerWarning, externalHumidityGroup=externalHumidityGroup, rebootCompleted=rebootCompleted, VoltAmps=VoltAmps, outletActivePower=outletActivePower, unitReadings=unitReadings, humidityUpperCritical=humidityUpperCritical, userSessionTimeout=userSessionTimeout, outletCurrentUpperCritical=outletCurrentUpperCritical, powerControl=powerControl, unitActivePower=unitActivePower, unitCircuitBreak0State=unitCircuitBreak0State, securityViolation=securityViolation, groupName=groupName, unitApparentPower=unitApparentPower, userAuthenticationFailure=userAuthenticationFailure, unitVoltageLowerWarning=unitVoltageLowerWarning, thresholdDescr=thresholdDescr, userDeleted=userDeleted, Watts=Watts, userLogin=userLogin, unitTempUpperCritical=unitTempUpperCritical, tempSensorLabel=tempSensorLabel, tempLowerCriticalReset=tempLowerCriticalReset, outletLabel=outletLabel, humidityUpperCriticalReset=humidityUpperCriticalReset, userPasswordChanged=userPasswordChanged, unitVoltageUpperWarning=unitVoltageUpperWarning, userBlocked=userBlocked, targetUser=targetUser, unitCurrentUpperCritical=unitCurrentUpperCritical, humidityLowerWarningReset=humidityLowerWarningReset, gateway=gateway, MilliVolts=MilliVolts, unitVoltageUpperCritical=unitVoltageUpperCritical, imageVersion=imageVersion, unitVoltage=unitVoltage, humidityUpperWarning=humidityUpperWarning, unitTempLowerWarning=unitTempLowerWarning, environmental=environmental, tempLowerCritical=tempLowerCritical, RelativeHumidity=RelativeHumidity, PowerFactorPercentage=PowerFactorPercentage, conformance=conformance, unitCircuitBreak2Current=unitCircuitBreak2Current, tempSensorEntry=tempSensorEntry, rebootStarted=rebootStarted, unitCurrentUpperWarning=unitCurrentUpperWarning, outletIndex=outletIndex, outlets=outlets, unitCircuitBreak2State=unitCircuitBreak2State, deviceUpdateStarted=deviceUpdateStarted, humidityUpperWarningReset=humidityUpperWarningReset, firmwareVersion=firmwareVersion, firmwareFileDiscarded=firmwareFileDiscarded, slaveIpAddress=slaveIpAddress, traps=traps, outletTable=outletTable, eatonEpduMa=eatonEpduMa, objectName=objectName, thresholdEventType=thresholdEventType, tempUpperWarning=tempUpperWarning, tempSensorCount=tempSensorCount, outletCurrentUpperWarning=outletCurrentUpperWarning, tempUpperCritical=tempUpperCritical, humiditySensorTable=humiditySensorTable, humiditySensorIndex=humiditySensorIndex, sensorDescr=sensorDescr, infoGroup=infoGroup, MilliAmps=MilliAmps, thresholdAlarm=thresholdAlarm, userLogout=userLogout, outletsGroup=outletsGroup, humidityLowerCriticalReset=humidityLowerCriticalReset, temperature=temperature, humidity=humidity, outletPowerFactor=outletPowerFactor, PYSNMP_MODULE_ID=eatonEpduMa, humidityLowerCritical=humidityLowerCritical, groupAdded=groupAdded, externalTemperatureGroup=externalTemperatureGroup, unitTempUpperWarning=unitTempUpperWarning, compliance=compliance, DegreesCelsius=DegreesCelsius, groups=groups, unitCircuitBreak1State=unitCircuitBreak1State, unitSensorsGroup=unitSensorsGroup, userModified=userModified, firmwareValidationFailed=firmwareValidationFailed, outletVoltage=outletVoltage, hardwareRev=hardwareRev, unitVoltageLowerCritical=unitVoltageLowerCritical, outletEntry=outletEntry, unit=unit, tempUpperCriticalReset=tempUpperCriticalReset, unitCpuTemp=unitCpuTemp, tempSensorTable=tempSensorTable, trapsGroup=trapsGroup, outletApparentPower=outletApparentPower, passwordSettingsChanged=passwordSettingsChanged, info=info, humiditySensorLabel=humiditySensorLabel, logFileCleared=logFileCleared, status=status, outletOperationalState=outletOperationalState, humiditySensorEntry=humiditySensorEntry, tempLowerWarningReset=tempLowerWarningReset, userName=userName, humiditySensorCount=humiditySensorCount, groupDeleted=groupDeleted)

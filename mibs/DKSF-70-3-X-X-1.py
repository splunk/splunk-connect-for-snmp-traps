#
# PySNMP MIB module DKSF-70-3-X-X-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-70-3-X-X-1
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Unsigned32, iso, Counter32, TimeTicks, Counter64, ObjectIdentity, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Bits, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Bits", "IpAddress", "enterprises")
TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
uniPingServerSolutionV3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 70))
uniPingServerSolutionV3.setRevisions(('2014-11-26 00:00', '2014-02-02 00:00', '2014-01-29 00:00', '2014-01-21 00:00', '2013-04-11 00:00', '2012-05-31 00:00', '2012-04-17 00:00', '2012-03-23 00:00', '2011-09-23 00:00', '2011-03-24 00:00', '2010-10-14 00:00', '2010-09-20 00:00', '2010-05-31 00:00', '2010-04-14 00:00',))
if mibBuilder.loadTexts: uniPingServerSolutionV3.setLastUpdated('201411260000Z')
if mibBuilder.loadTexts: uniPingServerSolutionV3.setOrganization('Alentis Electronics')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 90))
npTrapEmailTo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 90, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npTrapEmailTo.setStatus('current')
npRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5500))
npRelayTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5500, 5), )
if mibBuilder.loadTexts: npRelayTable.setStatus('current')
npRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1), ).setIndexNames((0, "DKSF-70-3-X-X-1", "npRelayN"))
if mibBuilder.loadTexts: npRelayEntry.setStatus('current')
npRelayN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayN.setStatus('current')
npRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 4))).clone(namedValues=NamedValues(("flip", -1), ("off", 0), ("on", 1), ("logic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayMode.setStatus('current')
npRelayStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayStartReset.setStatus('current')
npRelayMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayMemo.setStatus('current')
npRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayState.setStatus('current')
npThermo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800))
npThermoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8800, 1), )
if mibBuilder.loadTexts: npThermoTable.setStatus('current')
npThermoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1), ).setIndexNames((0, "DKSF-70-3-X-X-1", "npThermoSensorN"))
if mibBuilder.loadTexts: npThermoEntry.setStatus('current')
npThermoSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoSensorN.setStatus('current')
npThermoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValue.setStatus('current')
npThermoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoStatus.setStatus('current')
npThermoLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoLow.setStatus('current')
npThermoHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoHigh.setStatus('current')
npThermoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoMemo.setStatus('current')
npThermoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2))
npThermoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0))
npThermoTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapSensorN.setStatus('current')
npThermoTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapValue.setStatus('current')
npThermoTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapStatus.setStatus('current')
npThermoTrapLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapLow.setStatus('current')
npThermoTrapHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapHigh.setStatus('current')
npThermoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapMemo.setStatus('current')
npThermoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)).setObjects(("DKSF-70-3-X-X-1", "npThermoTrapSensorN"), ("DKSF-70-3-X-X-1", "npThermoTrapValue"), ("DKSF-70-3-X-X-1", "npThermoTrapStatus"), ("DKSF-70-3-X-X-1", "npThermoTrapLow"), ("DKSF-70-3-X-X-1", "npThermoTrapHigh"), ("DKSF-70-3-X-X-1", "npThermoTrapMemo"))
if mibBuilder.loadTexts: npThermoTrap.setStatus('current')
npIo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900))
npIoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8900, 1), )
if mibBuilder.loadTexts: npIoTable.setStatus('current')
npIoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1), ).setIndexNames((0, "DKSF-70-3-X-X-1", "npIoLineN"))
if mibBuilder.loadTexts: npIoEntry.setStatus('current')
npIoLineN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLineN.setStatus('current')
npIoLevelIn = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLevelIn.setStatus('current')
npIoLevelOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoLevelOut.setStatus('current')
npIoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoMemo.setStatus('current')
npIoPulseCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoPulseCounter.setStatus('current')
npIoSinglePulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 25500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseDuration.setStatus('current')
npIoSinglePulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseStart.setStatus('current')
npIoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2))
npIoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0))
npIoTrapLineN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLineN.setStatus('current')
npIoTrapLevelIn = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn.setStatus('current')
npIoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapMemo.setStatus('current')
npIoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)).setObjects(("DKSF-70-3-X-X-1", "npIoTrapLineN"), ("DKSF-70-3-X-X-1", "npIoTrapLevelIn"), ("DKSF-70-3-X-X-1", "npIoTrapMemo"))
if mibBuilder.loadTexts: npIoTrap.setStatus('current')
npCurLoop = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300))
npCurLoopTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8300, 1), )
if mibBuilder.loadTexts: npCurLoopTable.setStatus('current')
npCurLoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1), ).setIndexNames((0, "DKSF-70-3-X-X-1", "npCurLoopN"))
if mibBuilder.loadTexts: npCurLoopEntry.setStatus('current')
npCurLoopN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopN.setStatus('current')
npCurLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopStatus.setStatus('current')
npCurLoopI = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopI.setStatus('current')
npCurLoopV = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopV.setStatus('current')
npCurLoopR = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopR.setStatus('current')
npCurLoopPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cyclePower", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopPower.setStatus('current')
npCurLoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2))
npCurLoopTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0))
npCurLoopTrapN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapN.setStatus('current')
npCurLoopTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapStatus.setStatus('current')
npCurLoopTrapI = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapI.setStatus('current')
npCurLoopTrapV = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapV.setStatus('current')
npCurLoopTrapR = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapR.setStatus('current')
npCurLoopTrapPower = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopTrapPower.setStatus('current')
npCurLoopTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)).setObjects(("DKSF-70-3-X-X-1", "npCurLoopTrapN"), ("DKSF-70-3-X-X-1", "npCurLoopTrapStatus"), ("DKSF-70-3-X-X-1", "npCurLoopTrapI"), ("DKSF-70-3-X-X-1", "npCurLoopTrapV"), ("DKSF-70-3-X-X-1", "npCurLoopTrapR"), ("DKSF-70-3-X-X-1", "npCurLoopTrapPower"), ("DKSF-70-3-X-X-1", "npTrapEmailTo"))
if mibBuilder.loadTexts: npCurLoopTrap.setStatus('current')
npRelHumidity = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400))
npRelHumSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 2))
npRelHumSensorStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("error", 0), ("ok", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatus.setStatus('current')
npRelHumSensorValueH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueH.setStatus('current')
npRelHumSensorValueT = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT.setStatus('current')
npRelHumSensorStatusH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatusH.setStatus('current')
npRelHumSafeRangeHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setStatus('current')
npRelHumSafeRangeLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setStatus('current')
npRelHumSensorValueT100 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT100.setStatus('current')
npRelHumTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9))
npRelHumTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0))
npRelHumTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0, 1)).setObjects(("DKSF-70-3-X-X-1", "npRelHumSensorStatusH"), ("DKSF-70-3-X-X-1", "npRelHumSensorValueH"), ("DKSF-70-3-X-X-1", "npRelHumSafeRangeHigh"), ("DKSF-70-3-X-X-1", "npRelHumSafeRangeLow"), ("DKSF-70-3-X-X-1", "npTrapEmailTo"))
if mibBuilder.loadTexts: npRelHumTrap.setStatus('current')
npGsm = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800))
npGsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 1))
npGsmFailed = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ok", 0), ("failed", 1), ("fatalError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmFailed.setStatus('current')
npGsmRegistration = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))).clone(namedValues=NamedValues(("impossible", 0), ("homeNetwork", 1), ("searching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5), ("infoUpdate", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmRegistration.setStatus('current')
npGsmStrength = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmStrength.setStatus('current')
npGsmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2))
npGsmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0))
npGsmTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)).setObjects(("DKSF-70-3-X-X-1", "npGsmFailed"), ("DKSF-70-3-X-X-1", "npGsmRegistration"), ("DKSF-70-3-X-X-1", "npGsmStrength"))
if mibBuilder.loadTexts: npGsmTrap.setStatus('current')
npIr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900))
npIrCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900, 1))
npIrPlayCmd = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrPlayCmd.setStatus('current')
npIrReset = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrReset.setStatus('current')
npIrStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 255))).clone(namedValues=NamedValues(("ok", 0), ("busyCaptureWaitingButton", 1), ("busyCaptureWaitingIr", 2), ("busyPlayback", 3), ("error", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIrStatus.setStatus('current')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
mibBuilder.exportSymbols("DKSF-70-3-X-X-1", npGsm=npGsm, npTrapInfo=npTrapInfo, npThermoStatus=npThermoStatus, npThermoTrapPrefix=npThermoTrapPrefix, npTrapEmailTo=npTrapEmailTo, npThermoMemo=npThermoMemo, npThermoTrapMemo=npThermoTrapMemo, npIoTable=npIoTable, npIoSinglePulseDuration=npIoSinglePulseDuration, npIoLineN=npIoLineN, npIo=npIo, npGsmTraps=npGsmTraps, npRelay=npRelay, npIoTrapLineN=npIoTrapLineN, npIoSinglePulseStart=npIoSinglePulseStart, npThermoTrap=npThermoTrap, npThermoTrapHigh=npThermoTrapHigh, npIrReset=npIrReset, npForcedReboot=npForcedReboot, npCurLoopI=npCurLoopI, npRelayMemo=npRelayMemo, npRelHumSensorValueT100=npRelHumSensorValueT100, npRelayN=npRelayN, npRelHumSafeRangeLow=npRelHumSafeRangeLow, npRelHumSensorValueH=npRelHumSensorValueH, npThermoTrapValue=npThermoTrapValue, npCurLoopTrapV=npCurLoopTrapV, npCurLoopTrapI=npCurLoopTrapI, npIrPlayCmd=npIrPlayCmd, PYSNMP_MODULE_ID=uniPingServerSolutionV3, npIoLevelOut=npIoLevelOut, npCurLoopTraps=npCurLoopTraps, npThermoLow=npThermoLow, npCurLoopTable=npCurLoopTable, npCurLoopTrapN=npCurLoopTrapN, npRelHumTraps=npRelHumTraps, npThermoTrapLow=npThermoTrapLow, lightcom=lightcom, npCurLoopR=npCurLoopR, npCurLoopPower=npCurLoopPower, npCurLoopTrapR=npCurLoopTrapR, npIrCtrl=npIrCtrl, npRelayStartReset=npRelayStartReset, npCurLoopTrap=npCurLoopTrap, npRelHumSensorStatusH=npRelHumSensorStatusH, npThermoTraps=npThermoTraps, npGsmTrap=npGsmTrap, npThermoTrapSensorN=npThermoTrapSensorN, npRelHumidity=npRelHumidity, npRelayState=npRelayState, npGsmRegistration=npGsmRegistration, npIrStatus=npIrStatus, npThermoTable=npThermoTable, npRelHumSensorStatus=npRelHumSensorStatus, npGsmFailed=npGsmFailed, npCurLoopV=npCurLoopV, npIoTrapMemo=npIoTrapMemo, npRelHumSensor=npRelHumSensor, uniPingServerSolutionV3=uniPingServerSolutionV3, npResetStack=npResetStack, npThermoSensorN=npThermoSensorN, npGsmInfo=npGsmInfo, npGsmTrapPrefix=npGsmTrapPrefix, npCurLoopN=npCurLoopN, npRelHumTrapPrefix=npRelHumTrapPrefix, npThermoTrapStatus=npThermoTrapStatus, npIoEntry=npIoEntry, npRelHumSafeRangeHigh=npRelHumSafeRangeHigh, npRelayTable=npRelayTable, npIoTraps=npIoTraps, npCurLoopTrapPrefix=npCurLoopTrapPrefix, npThermoValue=npThermoValue, npCurLoopTrapPower=npCurLoopTrapPower, npRelHumTrap=npRelHumTrap, npCurLoopStatus=npCurLoopStatus, npReboot=npReboot, npRelHumSensorValueT=npRelHumSensorValueT, npIoMemo=npIoMemo, npIoTrapLevelIn=npIoTrapLevelIn, npIoTrapPrefix=npIoTrapPrefix, npIr=npIr, npIoPulseCounter=npIoPulseCounter, npCurLoopEntry=npCurLoopEntry, npIoTrap=npIoTrap, npSoftReboot=npSoftReboot, npThermo=npThermo, npCurLoop=npCurLoop, npGsmStrength=npGsmStrength, npRelayMode=npRelayMode, npCurLoopTrapStatus=npCurLoopTrapStatus, npThermoEntry=npThermoEntry, npRelayEntry=npRelayEntry, npIoLevelIn=npIoLevelIn, npThermoHigh=npThermoHigh)

#
# PySNMP MIB module A3COM-HUAWEI-DOT11-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-DOT11-SA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
H3cDot11ObjectIDType, h3cDot11, H3cDot11RadioScopeType, H3cDot11ChannelScopeType, H3cDot11SaIntfDevType = mibBuilder.importSymbols("A3COM-HUAWEI-DOT11-REF-MIB", "H3cDot11ObjectIDType", "h3cDot11", "H3cDot11RadioScopeType", "H3cDot11ChannelScopeType", "H3cDot11SaIntfDevType")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, TimeTicks, MibIdentifier, Integer32, Gauge32, Unsigned32, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "TimeTicks", "MibIdentifier", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter32", "ModuleIdentity")
DisplayString, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TruthValue", "TextualConvention")
h3cDot11Sa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13))
h3cDot11Sa.setRevisions(('2011-08-26 20:00',))
if mibBuilder.loadTexts: h3cDot11Sa.setLastUpdated('201108262000Z')
if mibBuilder.loadTexts: h3cDot11Sa.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cDot11SaCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1))
h3cDot11SaStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2))
h3cDot11SaNotifyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3))
h3cDot11SaCfgTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1), )
if mibBuilder.loadTexts: h3cDot11SaCfgTable.setStatus('current')
h3cDot11SaCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaCfgRadioType"))
if mibBuilder.loadTexts: h3cDot11SaCfgEntry.setStatus('current')
h3cDot11SaCfgRadioType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot11bg", 1), ("dot11a", 2))))
if mibBuilder.loadTexts: h3cDot11SaCfgRadioType.setStatus('current')
h3cDot11SaEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaEnable.setStatus('current')
h3cDot11SaRptDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 3), Bits().clone(namedValues=NamedValues(("microwave", 0), ("microwaveInverter", 1), ("bluetooth", 2), ("fixedFreqOthers", 3), ("fixedFreqCordlessPhone", 4), ("fixedFreqVideo", 5), ("fixedFreqAudio", 6), ("freqHopperOthers", 7), ("freqHopperCordlessBase", 8), ("freqHopperCordlessNetwork", 9), ("freqHopperXbox", 10), ("genericInterferer", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaRptDevType.setStatus('current')
h3cDot11SaTrapDevEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaTrapDevEnable.setStatus('current')
h3cDot11SaTrapDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("microwave", 0), ("microwaveInverter", 1), ("bluetooth", 2), ("fixedFreqOthers", 3), ("fixedFreqCordlessPhone", 4), ("fixedFreqVideo", 5), ("fixedFreqAudio", 6), ("freqHopperOthers", 7), ("freqHopperCordlessBase", 8), ("freqHopperCordlessNetwork", 9), ("freqHopperXbox", 10), ("genericInterferer", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaTrapDevType.setStatus('current')
h3cDot11SaTrapAQEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaTrapAQEnable.setStatus('current')
h3cDot11SaTrapAQThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaTrapAQThreshold.setStatus('current')
h3cDot11SaDrivenRRMEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaDrivenRRMEnable.setStatus('current')
h3cDot11SaDrivenRRMSnt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11SaDrivenRRMSnt.setStatus('current')
h3cDot11SaRtFFTDataTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1), )
if mibBuilder.loadTexts: h3cDot11SaRtFFTDataTable.setStatus('current')
h3cDot11SaRtFFTDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRtDataGroupID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaFrequency"))
if mibBuilder.loadTexts: h3cDot11SaRtFFTDataEntry.setStatus('current')
h3cDot11SaAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 1), H3cDot11ObjectIDType())
if mibBuilder.loadTexts: h3cDot11SaAPID.setStatus('current')
h3cDot11SaRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 2), H3cDot11RadioScopeType())
if mibBuilder.loadTexts: h3cDot11SaRadioID.setStatus('current')
h3cDot11SaRtDataGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: h3cDot11SaRtDataGroupID.setStatus('current')
h3cDot11SaFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: h3cDot11SaFrequency.setStatus('current')
h3cDot11SaRtFreqPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaRtFreqPower.setStatus('current')
h3cDot11SaRtFreqMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaRtFreqMaxPower.setStatus('current')
h3cDot11SaRtFreqDutyCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaRtFreqDutyCycle.setStatus('current')
h3cDot11SaRtFreqDataSeqNo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaRtFreqDataSeqNo.setStatus('current')
h3cDot11SaIntfDevTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2), )
if mibBuilder.loadTexts: h3cDot11SaIntfDevTable.setStatus('current')
h3cDot11SaIntfDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaDevID"))
if mibBuilder.loadTexts: h3cDot11SaIntfDevEntry.setStatus('current')
h3cDot11SaDevID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11SaDevID.setStatus('current')
h3cDot11SaDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 2), H3cDot11SaIntfDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevType.setStatus('current')
h3cDot11SaDevSI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevSI.setStatus('current')
h3cDot11SaDevRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevRSSI.setStatus('current')
h3cDot11SaDevDutyCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevDutyCycle.setStatus('current')
h3cDot11SaDevAffectedChls = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevAffectedChls.setStatus('current')
h3cDot11SaDevDetectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaDevDetectedTime.setStatus('current')
h3cDot11SaAirQualityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3), )
if mibBuilder.loadTexts: h3cDot11SaAirQualityTable.setStatus('current')
h3cDot11SaAirQualityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"), (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaChlNum"))
if mibBuilder.loadTexts: h3cDot11SaAirQualityEntry.setStatus('current')
h3cDot11SaChlNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 1), H3cDot11ChannelScopeType())
if mibBuilder.loadTexts: h3cDot11SaChlNum.setStatus('current')
h3cDot11SaAvgQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaAvgQuality.setStatus('current')
h3cDot11SaMinQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaMinQuality.setStatus('current')
h3cDot11SaIntfDevNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaIntfDevNum.setStatus('current')
h3cDot11SaWiFiUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaWiFiUtil.setStatus('current')
h3cDot11SaNonWiFiUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaNonWiFiUtil.setStatus('current')
h3cDot11SaNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11SaNoiseFloor.setStatus('current')
h3cDot11SaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0))
h3cDot11SaIntfDevDetected = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 1)).setObjects(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapIntfDevType"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevSI"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevRSSI"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevDC"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevChls"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevDctTime"))
if mibBuilder.loadTexts: h3cDot11SaIntfDevDetected.setStatus('current')
h3cDot11SaIntfDevDisappear = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 2)).setObjects(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapIntfDevType"))
if mibBuilder.loadTexts: h3cDot11SaIntfDevDisappear.setStatus('current')
h3cDot11SaChlQltLow = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 3)).setObjects(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlNum"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlQlt"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlIntfNum"))
if mibBuilder.loadTexts: h3cDot11SaChlQltLow.setStatus('current')
h3cDot11SaChlQltRecover = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 4)).setObjects(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlNum"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlQlt"), ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlIntfNum"))
if mibBuilder.loadTexts: h3cDot11SaChlQltRecover.setStatus('current')
h3cDot11SaTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1))
h3cDot11SaTrapAPID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 1), H3cDot11ObjectIDType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapAPID.setStatus('current')
h3cDot11SaTrapRadioID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 2), H3cDot11RadioScopeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapRadioID.setStatus('current')
h3cDot11SaTrapDevID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapDevID.setStatus('current')
h3cDot11SaTrapIntfDevType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 4), H3cDot11SaIntfDevType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapIntfDevType.setStatus('current')
h3cDot11APTrapDevSI = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11APTrapDevSI.setStatus('current')
h3cDot11SaTrapDevRSSI = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapDevRSSI.setStatus('current')
h3cDot11APTrapDevDC = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 7), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11APTrapDevDC.setStatus('current')
h3cDot11APTrapDevChls = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11APTrapDevChls.setStatus('current')
h3cDot11APTrapDevDctTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 9), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11APTrapDevDctTime.setStatus('current')
h3cDot11SaTrapChlNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 10), H3cDot11ChannelScopeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapChlNum.setStatus('current')
h3cDot11SaTrapChlQlt = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapChlQlt.setStatus('current')
h3cDot11SaTrapChlIntfNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 12), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDot11SaTrapChlIntfNum.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-DOT11-SA-MIB", h3cDot11APTrapDevChls=h3cDot11APTrapDevChls, h3cDot11SaTrapAPID=h3cDot11SaTrapAPID, h3cDot11Sa=h3cDot11Sa, h3cDot11APTrapDevSI=h3cDot11APTrapDevSI, h3cDot11SaAPID=h3cDot11SaAPID, h3cDot11SaNoiseFloor=h3cDot11SaNoiseFloor, h3cDot11SaMinQuality=h3cDot11SaMinQuality, h3cDot11SaRtFreqMaxPower=h3cDot11SaRtFreqMaxPower, h3cDot11SaIntfDevEntry=h3cDot11SaIntfDevEntry, h3cDot11SaRptDevType=h3cDot11SaRptDevType, h3cDot11SaStatusGroup=h3cDot11SaStatusGroup, h3cDot11SaRtFreqDataSeqNo=h3cDot11SaRtFreqDataSeqNo, h3cDot11SaNonWiFiUtil=h3cDot11SaNonWiFiUtil, h3cDot11SaIntfDevDetected=h3cDot11SaIntfDevDetected, h3cDot11SaTrapAQEnable=h3cDot11SaTrapAQEnable, h3cDot11SaDevType=h3cDot11SaDevType, h3cDot11SaTrapDevEnable=h3cDot11SaTrapDevEnable, h3cDot11SaTrapDevType=h3cDot11SaTrapDevType, h3cDot11SaDevID=h3cDot11SaDevID, h3cDot11SaCfgEntry=h3cDot11SaCfgEntry, h3cDot11SaDrivenRRMSnt=h3cDot11SaDrivenRRMSnt, h3cDot11SaWiFiUtil=h3cDot11SaWiFiUtil, h3cDot11SaRtDataGroupID=h3cDot11SaRtDataGroupID, h3cDot11SaTrapChlQlt=h3cDot11SaTrapChlQlt, h3cDot11SaRtFreqPower=h3cDot11SaRtFreqPower, h3cDot11SaDrivenRRMEnable=h3cDot11SaDrivenRRMEnable, h3cDot11SaTrapAQThreshold=h3cDot11SaTrapAQThreshold, h3cDot11SaRtFFTDataTable=h3cDot11SaRtFFTDataTable, h3cDot11APTrapDevDctTime=h3cDot11APTrapDevDctTime, h3cDot11SaTrapDevRSSI=h3cDot11SaTrapDevRSSI, h3cDot11SaTrapChlNum=h3cDot11SaTrapChlNum, h3cDot11SaAirQualityTable=h3cDot11SaAirQualityTable, h3cDot11SaCfgGroup=h3cDot11SaCfgGroup, h3cDot11SaDevDetectedTime=h3cDot11SaDevDetectedTime, h3cDot11SaRtFreqDutyCycle=h3cDot11SaRtFreqDutyCycle, h3cDot11SaCfgTable=h3cDot11SaCfgTable, h3cDot11SaAvgQuality=h3cDot11SaAvgQuality, h3cDot11SaTraps=h3cDot11SaTraps, h3cDot11SaChlNum=h3cDot11SaChlNum, h3cDot11SaDevSI=h3cDot11SaDevSI, h3cDot11SaAirQualityEntry=h3cDot11SaAirQualityEntry, h3cDot11SaIntfDevDisappear=h3cDot11SaIntfDevDisappear, h3cDot11SaFrequency=h3cDot11SaFrequency, h3cDot11SaChlQltRecover=h3cDot11SaChlQltRecover, h3cDot11SaNotifyGroup=h3cDot11SaNotifyGroup, h3cDot11SaTrapVars=h3cDot11SaTrapVars, h3cDot11SaTrapIntfDevType=h3cDot11SaTrapIntfDevType, h3cDot11SaEnable=h3cDot11SaEnable, h3cDot11SaRadioID=h3cDot11SaRadioID, PYSNMP_MODULE_ID=h3cDot11Sa, h3cDot11SaIntfDevTable=h3cDot11SaIntfDevTable, h3cDot11SaChlQltLow=h3cDot11SaChlQltLow, h3cDot11SaTrapDevID=h3cDot11SaTrapDevID, h3cDot11SaCfgRadioType=h3cDot11SaCfgRadioType, h3cDot11SaRtFFTDataEntry=h3cDot11SaRtFFTDataEntry, h3cDot11SaDevDutyCycle=h3cDot11SaDevDutyCycle, h3cDot11SaTrapRadioID=h3cDot11SaTrapRadioID, h3cDot11SaDevAffectedChls=h3cDot11SaDevAffectedChls, h3cDot11APTrapDevDC=h3cDot11APTrapDevDC, h3cDot11SaTrapChlIntfNum=h3cDot11SaTrapChlIntfNum, h3cDot11SaIntfDevNum=h3cDot11SaIntfDevNum, h3cDot11SaDevRSSI=h3cDot11SaDevRSSI)

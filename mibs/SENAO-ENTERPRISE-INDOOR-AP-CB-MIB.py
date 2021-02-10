#
# PySNMP MIB module SENAO-ENTERPRISE-INDOOR-AP-CB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SENAO-ENTERPRISE-INDOOR-AP-CB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Unsigned32, IpAddress, Integer32, Counter64, Counter32, ModuleIdentity, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "Bits", "enterprises")
MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
senao = ModuleIdentity((1, 3, 6, 1, 4, 1, 14125))
if mibBuilder.loadTexts: senao.setLastUpdated('0511250000Z')
if mibBuilder.loadTexts: senao.setOrganization('Senao R&D Dept., S/W Division')
indoorWirelessDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100))
entSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 1))
entLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 2))
entWAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 3))
entMacFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 4))
entWlan = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 5))
entSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 6))
entWlanCommonInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1))
entPassword = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entPassword.setStatus('mandatory')
entSysModel = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSysModel.setStatus('mandatory')
entSysMode = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ap-router", 0), ("repeater", 1), ("ap-bridge", 2), ("client-bridge", 3), ("client-router", 4), ("wds-bridge", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSysMode.setStatus('mandatory')
entSysUpTime = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSysUpTime.setStatus('mandatory')
entHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entHwVersion.setStatus('mandatory')
entSN = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSN.setStatus('mandatory')
entKenelVersion = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entKenelVersion.setStatus('mandatory')
entAppVersion = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entAppVersion.setStatus('mandatory')
entReset = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 10), TruthValue()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entReset.setStatus('mandatory')
entResetToDefault = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 11), TruthValue()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entResetToDefault.setStatus('mandatory')
entApplyModules = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 1, 12), TruthValue()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entApplyModules.setStatus('mandatory')
entLANIP = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entLANIP.setStatus('mandatory')
entLANSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entLANSubnetMask.setStatus('mandatory')
entSTPEnable = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSTPEnable.setStatus('mandatory')
entDHCPEnable = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entDHCPEnable.setStatus('mandatory')
entIPPoolStart = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entIPPoolStart.setStatus('mandatory')
entIPPoolEnd = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entIPPoolEnd.setStatus('mandatory')
entIPLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("half-hour", 0), ("one-hour", 1), ("two-hours", 2), ("half-day", 3), ("one-day", 4), ("two-days", 5), ("one-week", 6), ("two-weeks", 7), ("forever", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entIPLeaseTime.setStatus('mandatory')
entRouterEnable = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entRouterEnable.setStatus('mandatory')
entLanMacFilteringEnable = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entLanMacFilteringEnable.setStatus('mandatory')
entLanMacFilteringMode = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("white-list", 0), ("black-list", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entLanMacFilteringMode.setStatus('mandatory')
entLanMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 4, 3), )
if mibBuilder.loadTexts: entLanMacFilterTable.setStatus('current')
entLanMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entMacAddressIndex"))
if mibBuilder.loadTexts: entLanMacFilterEntry.setStatus('current')
entMacAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entMacAddressIndex.setStatus('current')
entMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entMacAddress.setStatus('current')
entMacFilteringValid = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entMacFilteringValid.setStatus('current')
entOpMode = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ap", 0), ("client-bridge", 1), ("wds-bridge", 2), ("repeater", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entOpMode.setStatus('mandatory')
entRadio = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entRadio.setStatus('mandatory')
entAPMode = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ap", 0), ("wds", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entAPMode.setStatus('mandatory')
entBand = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ieee802dot11-b-g", 0), ("ieee802dot11-b", 1), ("ieee802dot11-a", 2), ("ieee802dot11-g", 4), ("ieee802dot11-n", 6), ("ieee802dot11-g-n", 7), ("ieee802dot11-a-n", 8), ("ieee802dot11-b-g-n", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entBand.setStatus('mandatory')
entESSIDNum = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entESSIDNum.setStatus('mandatory')
entChannel = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entChannel.setStatus('mandatory')
entDataRate = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 11, 6, 9, 12, 18, 24, 36, 48, 54))).clone(namedValues=NamedValues(("auto", 0), ("oneMbps", 1), ("twoMbps", 2), ("fiveNhalfMbps", 5), ("elevenMbps", 11), ("sixMbps", 6), ("nineMbps", 9), ("twelveMbps", 12), ("eighteenMbps", 18), ("twentytwoMbps", 24), ("thirtysixMbps", 36), ("fortyeightMbps", 48), ("fiftyfourMbps", 54)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entDataRate.setStatus('mandatory')
entNDataRate = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entNDataRate.setStatus('mandatory')
entTxPower = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entTxPower.setStatus('mandatory')
entBeaconInterval = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entBeaconInterval.setStatus('mandatory')
entDTIMPeriod = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entDTIMPeriod.setStatus('mandatory')
entFragmentationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 2346))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entFragmentationThreshold.setStatus('mandatory')
entRTSThreshold = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2347))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entRTSThreshold.setStatus('mandatory')
entChannelBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entChannelBandwidth.setStatus('mandatory')
entPreambleType = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("short", 1), ("long", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entPreambleType.setStatus('mandatory')
entCTSProtection = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("always", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCTSProtection.setStatus('mandatory')
entWlanESSIDInfoTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2), )
if mibBuilder.loadTexts: entWlanESSIDInfoTable.setStatus('current')
entWlanESSIDInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanESSIDInfoIndex"))
if mibBuilder.loadTexts: entWlanESSIDInfoEntry.setStatus('current')
entWlanESSIDInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entWlanESSIDInfoIndex.setStatus('current')
entESSID = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entESSID.setStatus('current')
entBroadcastESSID = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entBroadcastESSID.setStatus('mandatory')
entWMM = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWMM.setStatus('mandatory')
entEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entEncryption.setStatus('current')
entWlanAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanAuthenticationType.setStatus('current')
entWlanWepInfoTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3), )
if mibBuilder.loadTexts: entWlanWepInfoTable.setStatus('current')
entWlanWepInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanESSIDIndex"))
if mibBuilder.loadTexts: entWlanWepInfoEntry.setStatus('current')
entWlanESSIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entWlanESSIDIndex.setStatus('current')
entWlanWepKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanWepKeyID.setStatus('current')
entWlanWepKey1Value = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanWepKey1Value.setStatus('current')
entWlanWepKey2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanWepKey2Value.setStatus('current')
entWlanWepKey3Value = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanWepKey3Value.setStatus('current')
entWlanWepKey4Value = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlanWepKey4Value.setStatus('current')
entWlanWPAInfoTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 5, 4), )
if mibBuilder.loadTexts: entWlanWPAInfoTable.setStatus('current')
entWlanWPAInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanWPAESSIDIndex"))
if mibBuilder.loadTexts: entWlanWPAInfoEntry.setStatus('current')
entWlanWPAESSIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entWlanWPAESSIDIndex.setStatus('current')
entPresharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1, 2), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entPresharedKey.setStatus('current')
ent802dot1xInfoTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5), )
if mibBuilder.loadTexts: ent802dot1xInfoTable.setStatus('current')
ent802dot1xInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlan802dot1xESSIDIndex"))
if mibBuilder.loadTexts: ent802dot1xInfoEntry.setStatus('current')
entWlan802dot1xESSIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entWlan802dot1xESSIDIndex.setStatus('current')
entRADIUSServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entRADIUSServerIPAddress.setStatus('current')
entRADIUSServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entRADIUSServerPort.setStatus('current')
entRADIUSServerPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 4), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entRADIUSServerPassword.setStatus('current')
entWlan802dot1xEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entWlan802dot1xEnable.setStatus('current')
entWlanClientListInfoTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6), )
if mibBuilder.loadTexts: entWlanClientListInfoTable.setStatus('current')
entWlanClientListInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entCLInfoIndex"))
if mibBuilder.loadTexts: entWlanClientListInfoEntry.setStatus('current')
entCLInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entCLInfoIndex.setStatus('current')
entCLInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLInterface.setStatus('current')
entCLMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLMAC.setStatus('current')
entCLRx = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLRx.setStatus('current')
entCLTx = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLTx.setStatus('current')
entCLSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLSignal.setStatus('current')
entCLConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLConnectedTime.setStatus('current')
entCLIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCLIdleTime.setStatus('current')
entSNMPStatus = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSNMPStatus.setStatus('mandatory')
entSNMPVerType = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("all", 0), ("v1", 1), ("v2c", 2), ("v3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSNMPVerType.setStatus('mandatory')
entSNMPCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3), )
if mibBuilder.loadTexts: entSNMPCommunityTable.setStatus('current')
entSNMPCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1), ).setIndexNames((0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entSNMPCommunityIndex"))
if mibBuilder.loadTexts: entSNMPCommunityEntry.setStatus('current')
entSNMPCommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSNMPCommunityIndex.setStatus('current')
entSNMPCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSNMPCommunityName.setStatus('current')
entSNMPCommunityType = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read", 1), ("write", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSNMPCommunityType.setStatus('current')
entSNMPCommunityValid = MibTableColumn((1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSNMPCommunityValid.setStatus('current')
entSNMPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 6, 4))
entTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entTrapStatus.setStatus('mandatory')
entTrapVer = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("all", 0), ("v1", 1), ("v2c", 2), ("v3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entTrapVer.setStatus('mandatory')
entTrapReceiverIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entTrapReceiverIPAddress.setStatus('mandatory')
entTrapReceiverCommunityName = MibScalar((1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entTrapReceiverCommunityName.setStatus('mandatory')
entTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 20))
entSystemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 20, 1))
entWanTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 100, 20, 2))
entSystemTrapsReboot = NotificationType((1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 1))
if mibBuilder.loadTexts: entSystemTrapsReboot.setStatus('current')
entSystemTrapsRestoreToDefault = NotificationType((1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 2))
if mibBuilder.loadTexts: entSystemTrapsRestoreToDefault.setStatus('current')
entSystemTrapsReloadModules = NotificationType((1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 3))
if mibBuilder.loadTexts: entSystemTrapsReloadModules.setStatus('current')
entWanTrapsLinkDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 14125, 100, 20, 2, 1)).setObjects(("SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "ifIndex"))
if mibBuilder.loadTexts: entWanTrapsLinkDisconnect.setStatus('current')
entWanTrapsLinkRecover = NotificationType((1, 3, 6, 1, 4, 1, 14125, 100, 20, 2, 2)).setObjects(("SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "ifIndex"))
if mibBuilder.loadTexts: entWanTrapsLinkRecover.setStatus('current')
mibBuilder.exportSymbols("SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", entIPLeaseTime=entIPLeaseTime, entWlanWepKey3Value=entWlanWepKey3Value, entKenelVersion=entKenelVersion, entMacFilteringValid=entMacFilteringValid, entSystemTraps=entSystemTraps, entWlanESSIDInfoIndex=entWlanESSIDInfoIndex, entSNMPCommunityEntry=entSNMPCommunityEntry, entRouterEnable=entRouterEnable, entWlanESSIDInfoEntry=entWlanESSIDInfoEntry, entResetToDefault=entResetToDefault, entMacAddress=entMacAddress, entWlanClientListInfoTable=entWlanClientListInfoTable, entLanMacFilteringEnable=entLanMacFilteringEnable, entBeaconInterval=entBeaconInterval, entWanTrapsLinkDisconnect=entWanTrapsLinkDisconnect, ent802dot1xInfoTable=ent802dot1xInfoTable, entApplyModules=entApplyModules, entCLRx=entCLRx, entTraps=entTraps, entIPPoolEnd=entIPPoolEnd, entRadio=entRadio, entWlanAuthenticationType=entWlanAuthenticationType, entAPMode=entAPMode, entSNMPCommunityName=entSNMPCommunityName, entRADIUSServerPort=entRADIUSServerPort, entSNMPCommunityTable=entSNMPCommunityTable, entLanMacFilterEntry=entLanMacFilterEntry, entLanMacFilterTable=entLanMacFilterTable, indoorWirelessDevice=indoorWirelessDevice, entFragmentationThreshold=entFragmentationThreshold, entWanTrapsLinkRecover=entWanTrapsLinkRecover, entCLInterface=entCLInterface, entTrapReceiverCommunityName=entTrapReceiverCommunityName, entWlanWepKeyID=entWlanWepKeyID, entSNMPCommunityValid=entSNMPCommunityValid, entWlanCommonInfo=entWlanCommonInfo, entReset=entReset, entTxPower=entTxPower, entWlanClientListInfoEntry=entWlanClientListInfoEntry, entTrapVer=entTrapVer, entWlanWepInfoTable=entWlanWepInfoTable, entCLIdleTime=entCLIdleTime, senao=senao, entWAN=entWAN, entLanMacFilteringMode=entLanMacFilteringMode, entChannelBandwidth=entChannelBandwidth, ent802dot1xInfoEntry=ent802dot1xInfoEntry, PYSNMP_MODULE_ID=senao, entHwVersion=entHwVersion, entWlanWPAInfoTable=entWlanWPAInfoTable, entCLMAC=entCLMAC, entWMM=entWMM, entSystemTrapsReloadModules=entSystemTrapsReloadModules, entWlan802dot1xEnable=entWlan802dot1xEnable, entWlanWepKey4Value=entWlanWepKey4Value, entSystemTrapsReboot=entSystemTrapsReboot, entAppVersion=entAppVersion, entSystemTrapsRestoreToDefault=entSystemTrapsRestoreToDefault, entTrapReceiverIPAddress=entTrapReceiverIPAddress, entWlan802dot1xESSIDIndex=entWlan802dot1xESSIDIndex, entWlanWepInfoEntry=entWlanWepInfoEntry, entBroadcastESSID=entBroadcastESSID, entOpMode=entOpMode, entSysUpTime=entSysUpTime, entSysModel=entSysModel, entESSID=entESSID, entCLInfoIndex=entCLInfoIndex, entCTSProtection=entCTSProtection, entPreambleType=entPreambleType, entWlanWepKey2Value=entWlanWepKey2Value, entSN=entSN, entWlanWepKey1Value=entWlanWepKey1Value, entRADIUSServerPassword=entRADIUSServerPassword, entSystem=entSystem, entMacFilter=entMacFilter, entPassword=entPassword, entIPPoolStart=entIPPoolStart, entRTSThreshold=entRTSThreshold, entWlan=entWlan, entSNMPVerType=entSNMPVerType, entChannel=entChannel, entCLSignal=entCLSignal, entDHCPEnable=entDHCPEnable, entSTPEnable=entSTPEnable, entWlanWPAESSIDIndex=entWlanWPAESSIDIndex, entTrapStatus=entTrapStatus, entRADIUSServerIPAddress=entRADIUSServerIPAddress, entWlanESSIDInfoTable=entWlanESSIDInfoTable, entSNMPTrap=entSNMPTrap, entSNMPStatus=entSNMPStatus, entSNMP=entSNMP, entWlanWPAInfoEntry=entWlanWPAInfoEntry, entLANIP=entLANIP, entBand=entBand, entPresharedKey=entPresharedKey, entDataRate=entDataRate, entNDataRate=entNDataRate, entCLTx=entCLTx, entLANSubnetMask=entLANSubnetMask, entWlanESSIDIndex=entWlanESSIDIndex, entSysMode=entSysMode, entLAN=entLAN, entEncryption=entEncryption, entSNMPCommunityIndex=entSNMPCommunityIndex, entSNMPCommunityType=entSNMPCommunityType, entMacAddressIndex=entMacAddressIndex, entDTIMPeriod=entDTIMPeriod, entWanTraps=entWanTraps, entESSIDNum=entESSIDNum, entCLConnectedTime=entCLConnectedTime)

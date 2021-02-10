#
# PySNMP MIB module HH3C-DOT11-STATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DOT11-STATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
Hh3cDot11SSIDEncryptModeType, Hh3cDot11AuthenType, Hh3cDot11AuthorFailType, Hh3cDot11ChannelScopeType, Hh3cDot11RadioType, Hh3cDot11AssocFailType, Hh3cDot11SSIDStringType, hh3cDot11, Hh3cDot11RadioScopeType, Hh3cDot11AKMType, Hh3cDot11SecIEStatusType, Hh3cDot11ObjectIDType, Hh3cDot11CipherType = mibBuilder.importSymbols("HH3C-DOT11-REF-MIB", "Hh3cDot11SSIDEncryptModeType", "Hh3cDot11AuthenType", "Hh3cDot11AuthorFailType", "Hh3cDot11ChannelScopeType", "Hh3cDot11RadioType", "Hh3cDot11AssocFailType", "Hh3cDot11SSIDStringType", "hh3cDot11", "Hh3cDot11RadioScopeType", "Hh3cDot11AKMType", "Hh3cDot11SecIEStatusType", "Hh3cDot11ObjectIDType", "Hh3cDot11CipherType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, NotificationType, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, iso, ObjectIdentity, Integer32, MibIdentifier, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "iso", "ObjectIdentity", "Integer32", "MibIdentifier", "Counter32", "Gauge32")
TextualConvention, DateAndTime, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "MacAddress", "DisplayString")
hh3cDot11STATION = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3))
hh3cDot11STATION.setRevisions(('2010-09-02 18:00', '2009-08-07 18:00', '2009-07-29 18:00', '2009-05-07 20:00', '2008-11-07 17:30', '2008-02-25 18:00', '2007-12-21 18:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 16:00',))
if mibBuilder.loadTexts: hh3cDot11STATION.setLastUpdated('201009021800Z')
if mibBuilder.loadTexts: hh3cDot11STATION.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cDot11StationMtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1))
hh3cDot11StationNotifyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2))
hh3cDot11StationAssociateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1), )
if mibBuilder.loadTexts: hh3cDot11StationAssociateTable.setStatus('current')
hh3cDot11StationAssociateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1), ).setIndexNames((0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"))
if mibBuilder.loadTexts: hh3cDot11StationAssociateEntry.setStatus('current')
hh3cDot11StationMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cDot11StationMAC.setStatus('current')
hh3cDot11StationIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationIPAddress.setStatus('current')
hh3cDot11StationUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationUserName.setStatus('current')
hh3cDot11StationTxRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 4), OctetString()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxRateSet.setStatus('current')
hh3cDot11StationUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 5), Unsigned32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationUpTime.setStatus('current')
hh3cDot11StationSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 6), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSignalStrength.setStatus('current')
hh3cDot11StationRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRSSI.setStatus('current')
hh3cDot11StationChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 8), Hh3cDot11ChannelScopeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationChannel.setStatus('current')
hh3cDot11StationPowerSaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("powersave", 2))).clone('active')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationPowerSaveMode.setStatus('current')
hh3cDot11StationAid = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationAid.setStatus('current')
hh3cDot11StationVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationVlanId.setStatus('current')
hh3cDot11StationSSIDName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 12), Hh3cDot11SSIDStringType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSSIDName.setStatus('current')
hh3cDot11StationAuthenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 13), Hh3cDot11AuthenType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationAuthenMode.setStatus('current')
hh3cDot11StationAKMMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 14), Hh3cDot11AKMType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationAKMMode.setStatus('current')
hh3cDot11StationSecurityCiphers = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 15), Hh3cDot11CipherType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSecurityCiphers.setStatus('current')
hh3cDot11StationSSIDEncryptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 16), Hh3cDot11SSIDEncryptModeType().clone('cipher')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSSIDEncryptMode.setStatus('current')
hh3cDot11StationRxSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 17), Integer32()).setUnits('One Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxSNR.setStatus('current')
hh3cDot11StationTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 18), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxRate.setStatus('current')
hh3cDot11StationRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 19), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxRate.setStatus('current')
hh3cDot11StationVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationVendorName.setStatus('current')
hh3cDot11StationRadioMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 21), Hh3cDot11RadioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRadioMode.setStatus('current')
hh3cDot11StationRxNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxNoise.setStatus('current')
hh3cDot11StationMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 23), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationMACAddress.setStatus('current')
hh3cDot11StationTxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 24), Integer32()).setUnits('byte/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxSpeed.setStatus('current')
hh3cDot11StationRxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 25), Integer32()).setUnits('byte/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxSpeed.setStatus('current')
hh3cDot11StationWmmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wmm", 1), ("nonwmm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationWmmMode.setStatus('current')
hh3cDot11StationSecIEStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 27), Hh3cDot11SecIEStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSecIEStatus.setStatus('current')
hh3cDot11StationUpTimeTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 28), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationUpTimeTicks.setStatus('current')
hh3cDot11StationAPRelationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2), )
if mibBuilder.loadTexts: hh3cDot11StationAPRelationTable.setStatus('current')
hh3cDot11StationAPRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1), ).setIndexNames((0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"))
if mibBuilder.loadTexts: hh3cDot11StationAPRelationEntry.setStatus('current')
hh3cDot11CurrAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 1), Hh3cDot11ObjectIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11CurrAPID.setStatus('current')
hh3cDot11CurrRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 2), Hh3cDot11RadioScopeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11CurrRadioID.setStatus('current')
hh3cDot11CurrWlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11CurrWlanID.setStatus('current')
hh3cDot11StationStatisTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3), )
if mibBuilder.loadTexts: hh3cDot11StationStatisTable.setStatus('current')
hh3cDot11StationStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1), ).setIndexNames((0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"))
if mibBuilder.loadTexts: hh3cDot11StationStatisEntry.setStatus('current')
hh3cDot11StationRxFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxFrameCnt.setStatus('current')
hh3cDot11StationTxFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxFrameCnt.setStatus('current')
hh3cDot11StationDropFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationDropFrameCnt.setStatus('current')
hh3cDot11StationRxFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 4), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxFrameBytes.setStatus('current')
hh3cDot11StationTxFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 5), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxFrameBytes.setStatus('current')
hh3cDot11StationDropFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 6), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationDropFrameBytes.setStatus('current')
hh3cDot11StationRxRetryPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxRetryPkts.setStatus('current')
hh3cDot11StationTxRetryPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxRetryPkts.setStatus('current')
hh3cDot11StationRxRetryBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxRetryBytes.setStatus('current')
hh3cDot11StationTxRetryBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxRetryBytes.setStatus('current')
hh3cDot11StationThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 11), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationThroughput.setStatus('current')
hh3cDot11StationSuccessTxCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSuccessTxCnt.setStatus('current')
hh3cDot11StationSuccessTxDataCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationSuccessTxDataCnt.setStatus('current')
hh3cDot11StationRxDataFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxDataFrameCnt.setStatus('current')
hh3cDot11StationTxDataFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxDataFrameCnt.setStatus('current')
hh3cDot11StationRxDataFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxDataFrameBytes.setStatus('current')
hh3cDot11StationTxDataFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationTxDataFrameBytes.setStatus('current')
hh3cDot11StationRxFragCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StationRxFragCnt.setStatus('current')
hh3cDot11StaRxErrDataFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StaRxErrDataFrameCnt.setStatus('current')
hh3cDot11StaTxRetryDataFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11StaTxRetryDataFrameCnt.setStatus('current')
hh3cDot11StationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0))
hh3cDot11StationMICErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 1)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
if mibBuilder.loadTexts: hh3cDot11StationMICErrorTrap.setStatus('current')
hh3cDot11StationAuthenErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 2)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthenMode"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAKMMode"))
if mibBuilder.loadTexts: hh3cDot11StationAuthenErrorTrap.setStatus('current')
hh3cDot11StationAuthorFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 3)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthorFailCause"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthMode"))
if mibBuilder.loadTexts: hh3cDot11StationAuthorFailTrap.setStatus('current')
hh3cDot11StationAssocFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 4)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAssocFailCause"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"))
if mibBuilder.loadTexts: hh3cDot11StationAssocFailTrap.setStatus('current')
hh3cDot11StationDeAssocTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 5)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
if mibBuilder.loadTexts: hh3cDot11StationDeAssocTrap.setStatus('current')
hh3cDot11StationAuthorSuccTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 6)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionStartTime"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
if mibBuilder.loadTexts: hh3cDot11StationAuthorSuccTrap.setStatus('current')
hh3cDot11StationRoamingTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 7)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationRoamingTime"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPAddress"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPv6Add"))
if mibBuilder.loadTexts: hh3cDot11StationRoamingTrap.setStatus('current')
hh3cDot11StationDisconnectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 8)).setObjects(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StaDisconnectReason"), ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
if mibBuilder.loadTexts: hh3cDot11StationDisconnectTrap.setStatus('current')
hh3cDot11StationTrapVarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1))
hh3cDot11StationTrapBSSID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationTrapBSSID.setStatus('current')
hh3cDot11StationTrapStaMAC = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationTrapStaMAC.setStatus('current')
hh3cDot11StationSessionStartTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationSessionStartTime.setStatus('current')
hh3cDot11StationAssocFailCause = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 4), Hh3cDot11AssocFailType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationAssocFailCause.setStatus('current')
hh3cDot11StationAuthorFailCause = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 5), Hh3cDot11AuthorFailType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationAuthorFailCause.setStatus('current')
hh3cDot11StationFailCauseDesc = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationFailCauseDesc.setStatus('current')
hh3cDot11StationSessionDuration = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 7), Unsigned32()).setUnits('second').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationSessionDuration.setStatus('current')
hh3cDot11StationRoamingTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 8), Unsigned32()).setUnits('second').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationRoamingTime.setStatus('current')
hh3cDot11StationACIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 9), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationACIPAddress.setStatus('current')
hh3cDot11StationAPName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationAPName.setStatus('current')
hh3cDot11StationBSSID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 11), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationBSSID.setStatus('current')
hh3cDot11StaDisconnectReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 12), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StaDisconnectReason.setStatus('current')
hh3cDot11StationAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("opensystem", 1), ("sharedkey", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationAuthMode.setStatus('current')
hh3cDot11StationACIPv6Add = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 14), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDot11StationACIPv6Add.setStatus('current')
mibBuilder.exportSymbols("HH3C-DOT11-STATION-MIB", hh3cDot11StationIPAddress=hh3cDot11StationIPAddress, hh3cDot11StationTxDataFrameBytes=hh3cDot11StationTxDataFrameBytes, hh3cDot11StationRxRetryPkts=hh3cDot11StationRxRetryPkts, hh3cDot11StationTxRetryPkts=hh3cDot11StationTxRetryPkts, hh3cDot11StationMICErrorTrap=hh3cDot11StationMICErrorTrap, hh3cDot11StationTxRate=hh3cDot11StationTxRate, hh3cDot11StationAssociateTable=hh3cDot11StationAssociateTable, hh3cDot11StationStatisTable=hh3cDot11StationStatisTable, hh3cDot11StationTraps=hh3cDot11StationTraps, hh3cDot11StationTrapBSSID=hh3cDot11StationTrapBSSID, hh3cDot11STATION=hh3cDot11STATION, hh3cDot11StationAssocFailTrap=hh3cDot11StationAssocFailTrap, PYSNMP_MODULE_ID=hh3cDot11STATION, hh3cDot11CurrAPID=hh3cDot11CurrAPID, hh3cDot11StationVlanId=hh3cDot11StationVlanId, hh3cDot11StationChannel=hh3cDot11StationChannel, hh3cDot11StationRxNoise=hh3cDot11StationRxNoise, hh3cDot11StationAKMMode=hh3cDot11StationAKMMode, hh3cDot11StationNotifyGroup=hh3cDot11StationNotifyGroup, hh3cDot11StationDropFrameBytes=hh3cDot11StationDropFrameBytes, hh3cDot11StationSessionStartTime=hh3cDot11StationSessionStartTime, hh3cDot11StationAuthenMode=hh3cDot11StationAuthenMode, hh3cDot11StationMtGroup=hh3cDot11StationMtGroup, hh3cDot11StationRxDataFrameBytes=hh3cDot11StationRxDataFrameBytes, hh3cDot11StationTxFrameCnt=hh3cDot11StationTxFrameCnt, hh3cDot11StationAid=hh3cDot11StationAid, hh3cDot11StationRxRate=hh3cDot11StationRxRate, hh3cDot11CurrRadioID=hh3cDot11CurrRadioID, hh3cDot11StationDropFrameCnt=hh3cDot11StationDropFrameCnt, hh3cDot11StationAPName=hh3cDot11StationAPName, hh3cDot11StationAuthorSuccTrap=hh3cDot11StationAuthorSuccTrap, hh3cDot11StaTxRetryDataFrameCnt=hh3cDot11StaTxRetryDataFrameCnt, hh3cDot11StationDeAssocTrap=hh3cDot11StationDeAssocTrap, hh3cDot11StationTxRetryBytes=hh3cDot11StationTxRetryBytes, hh3cDot11StationRSSI=hh3cDot11StationRSSI, hh3cDot11StationAuthorFailTrap=hh3cDot11StationAuthorFailTrap, hh3cDot11StationPowerSaveMode=hh3cDot11StationPowerSaveMode, hh3cDot11StationAuthorFailCause=hh3cDot11StationAuthorFailCause, hh3cDot11CurrWlanID=hh3cDot11CurrWlanID, hh3cDot11StationRadioMode=hh3cDot11StationRadioMode, hh3cDot11StationUpTimeTicks=hh3cDot11StationUpTimeTicks, hh3cDot11StationTrapVarObjects=hh3cDot11StationTrapVarObjects, hh3cDot11StationSSIDEncryptMode=hh3cDot11StationSSIDEncryptMode, hh3cDot11StationRoamingTime=hh3cDot11StationRoamingTime, hh3cDot11StationRxSpeed=hh3cDot11StationRxSpeed, hh3cDot11StationSSIDName=hh3cDot11StationSSIDName, hh3cDot11StationMAC=hh3cDot11StationMAC, hh3cDot11StationACIPv6Add=hh3cDot11StationACIPv6Add, hh3cDot11StationThroughput=hh3cDot11StationThroughput, hh3cDot11StationAuthenErrorTrap=hh3cDot11StationAuthenErrorTrap, hh3cDot11StationRxFragCnt=hh3cDot11StationRxFragCnt, hh3cDot11StationMACAddress=hh3cDot11StationMACAddress, hh3cDot11StationRxDataFrameCnt=hh3cDot11StationRxDataFrameCnt, hh3cDot11StationTxFrameBytes=hh3cDot11StationTxFrameBytes, hh3cDot11StationSuccessTxCnt=hh3cDot11StationSuccessTxCnt, hh3cDot11StationSecurityCiphers=hh3cDot11StationSecurityCiphers, hh3cDot11StaDisconnectReason=hh3cDot11StaDisconnectReason, hh3cDot11StationWmmMode=hh3cDot11StationWmmMode, hh3cDot11StationAssociateEntry=hh3cDot11StationAssociateEntry, hh3cDot11StationAPRelationTable=hh3cDot11StationAPRelationTable, hh3cDot11StationAssocFailCause=hh3cDot11StationAssocFailCause, hh3cDot11StationTxSpeed=hh3cDot11StationTxSpeed, hh3cDot11StationAuthMode=hh3cDot11StationAuthMode, hh3cDot11StationAPRelationEntry=hh3cDot11StationAPRelationEntry, hh3cDot11StationRoamingTrap=hh3cDot11StationRoamingTrap, hh3cDot11StationUserName=hh3cDot11StationUserName, hh3cDot11StationSignalStrength=hh3cDot11StationSignalStrength, hh3cDot11StationTxRateSet=hh3cDot11StationTxRateSet, hh3cDot11StationSessionDuration=hh3cDot11StationSessionDuration, hh3cDot11StationRxFrameCnt=hh3cDot11StationRxFrameCnt, hh3cDot11StationFailCauseDesc=hh3cDot11StationFailCauseDesc, hh3cDot11StationTxDataFrameCnt=hh3cDot11StationTxDataFrameCnt, hh3cDot11StationUpTime=hh3cDot11StationUpTime, hh3cDot11StationTrapStaMAC=hh3cDot11StationTrapStaMAC, hh3cDot11StationSuccessTxDataCnt=hh3cDot11StationSuccessTxDataCnt, hh3cDot11StationStatisEntry=hh3cDot11StationStatisEntry, hh3cDot11StationACIPAddress=hh3cDot11StationACIPAddress, hh3cDot11StationBSSID=hh3cDot11StationBSSID, hh3cDot11StationRxSNR=hh3cDot11StationRxSNR, hh3cDot11StationRxFrameBytes=hh3cDot11StationRxFrameBytes, hh3cDot11StaRxErrDataFrameCnt=hh3cDot11StaRxErrDataFrameCnt, hh3cDot11StationRxRetryBytes=hh3cDot11StationRxRetryBytes, hh3cDot11StationSecIEStatus=hh3cDot11StationSecIEStatus, hh3cDot11StationVendorName=hh3cDot11StationVendorName, hh3cDot11StationDisconnectTrap=hh3cDot11StationDisconnectTrap)

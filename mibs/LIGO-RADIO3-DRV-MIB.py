#
# PySNMP MIB module LIGO-RADIO3-DRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGO-RADIO3-DRV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ligoMgmt, = mibBuilder.importSymbols("LIGOWAVE-MIB", "ligoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Integer32, TimeTicks, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Bits, ModuleIdentity, ObjectIdentity, Counter64, Counter32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "NotificationType")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
ligoRadio3DrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750, 3, 8))
ligoRadio3DrvMIB.setRevisions(('2010-01-06 00:00',))
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setLastUpdated('201001060000Z')
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setOrganization('LigoWave')
ligoRadio3DrvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1))
ligoRdo3DrvNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0))
ligoRdo3DrvInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 1))
ligoRdo3DrvConf = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 2))
ligoRdo3DrvStats = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3))
ligoRdo3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1), )
if mibBuilder.loadTexts: ligoRdo3StatsTable.setStatus('current')
ligoRdo3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LIGO-RADIO3-DRV-MIB", "ligoRdo3Endpoint"))
if mibBuilder.loadTexts: ligoRdo3StatsEntry.setStatus('current')
ligoRdo3Endpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ligoRdo3Endpoint.setStatus('current')
ligoRdo3LastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3LastUpdate.setStatus('current')
ligoRdo3MacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3MacAddress.setStatus('current')
ligoRdo3IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3IpAddress.setStatus('current')
ligoRdo3CountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3CountryCode.setStatus('current')
ligoRdo3Encryption = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Encryption.setStatus('current')
ligoRdo3Parameters = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Parameters.setStatus('current')
ligoRdo3Capabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Capabilities.setStatus('current')
ligoRdo3TxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPower.setStatus('current')
ligoRdo3TxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPackets.setStatus('current')
ligoRdo3TxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxBytes.setStatus('current')
ligoRdo3TxXmitFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxXmitFailed.setStatus('current')
ligoRdo3TxXmitDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxXmitDropped.setStatus('current')
ligoRdo3TxOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxOverruns.setStatus('current')
ligoRdo3TxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxSuccess.setStatus('current')
ligoRdo3TxFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFailed.setStatus('current')
ligoRdo3TxRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxRetried.setStatus('current')
ligoRdo3TxNotRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNotRetried.setStatus('current')
ligoRdo3TxPacketsPerMcs = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPacketsPerMcs.setStatus('current')
ligoRdo3TxMsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMsdus.setStatus('current')
ligoRdo3TxNotAggregated = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNotAggregated.setStatus('current')
ligoRdo3TxAckRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAckRequired.setStatus('current')
ligoRdo3TxNoAckRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNoAckRequired.setStatus('current')
ligoRdo3TxAltRate = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAltRate.setStatus('current')
ligoRdo3TxManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxManagement.setStatus('current')
ligoRdo3TxLegacy = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxLegacy.setStatus('current')
ligoRdo3TxLegacyBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxLegacyBytes.setStatus('current')
ligoRdo3TxAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAmsdus.setStatus('current')
ligoRdo3TxPktsInAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPktsInAmsdus.setStatus('current')
ligoRdo3TxAmsduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAmsduBytes.setStatus('current')
ligoRdo3TxMpdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMpdus.setStatus('current')
ligoRdo3TxMpduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMpduBytes.setStatus('current')
ligoRdo3TxFragmented = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFragmented.setStatus('current')
ligoRdo3TxFragBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFragBytes.setStatus('current')
ligoRdo3RxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPackets.setStatus('current')
ligoRdo3RxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBytes.setStatus('current')
ligoRdo3RxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxDropped.setStatus('current')
ligoRdo3RxCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxCrcErrors.setStatus('current')
ligoRdo3RxIcvErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxIcvErrors.setStatus('current')
ligoRdo3RxMicErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMicErrors.setStatus('current')
ligoRdo3RxKeyNotValid = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxKeyNotValid.setStatus('current')
ligoRdo3RxAclDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAclDiscarded.setStatus('current')
ligoRdo3RxManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxManagement.setStatus('current')
ligoRdo3RxControl = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxControl.setStatus('current')
ligoRdo3RxData = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxData.setStatus('current')
ligoRdo3RxUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxUnknown.setStatus('current')
ligoRdo3RxNullData = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxNullData.setStatus('current')
ligoRdo3RxBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBroadcast.setStatus('current')
ligoRdo3RxMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMulticast.setStatus('current')
ligoRdo3RxUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxUnicast.setStatus('current')
ligoRdo3RxCck = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxCck.setStatus('current')
ligoRdo3RxOfdm = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxOfdm.setStatus('current')
ligoRdo3RxHtMixedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtMixedMode.setStatus('current')
ligoRdo3RxHtGreenfield = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtGreenfield.setStatus('current')
ligoRdo3RxAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAmsdus.setStatus('current')
ligoRdo3RxPacketsInAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPacketsInAmsdus.setStatus('current')
ligoRdo3RxAmpdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAmpdus.setStatus('current')
ligoRdo3RxMpduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMpduBytes.setStatus('current')
ligoRdo3RxRoBufTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufTotal.setStatus('current')
ligoRdo3RxRoBufInSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufInSeq.setStatus('current')
ligoRdo3RxRoBufDup = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufDup.setStatus('current')
ligoRdo3RxRoBufExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufExpired.setStatus('current')
ligoRdo3RxRoBufBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufBuffered.setStatus('current')
ligoRdo3RxRoBufReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufReordered.setStatus('current')
ligoRdo3RxRoBufFlushed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufFlushed.setStatus('current')
ligoRdo3RxRoBufTooBig = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufTooBig.setStatus('current')
ligoRdo3RxL2Pad = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxL2Pad.setStatus('current')
ligoRdo3RxBlockAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBlockAcks.setStatus('current')
ligoRdo3RxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxFragments.setStatus('current')
ligoRdo3RxStbc = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxStbc.setStatus('current')
ligoRdo3RxShortGuardInt = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxShortGuardInt.setStatus('current')
ligoRdo3Rx40MhzBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Rx40MhzBandwidth.setStatus('current')
ligoRdo3RxHtControl = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtControl.setStatus('current')
ligoRdo3RxPacketsPerMcs = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 74), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPacketsPerMcs.setStatus('current')
ligoRdo3RxLastSigLevel0 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 75), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel0.setStatus('current')
ligoRdo3RxLastSigLevel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 76), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel1.setStatus('current')
ligoRdo3RxLastSigLevel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 77), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel2.setStatus('current')
ligoRdo3RxNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 78), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxNoise.setStatus('current')
ligoRdo3RxLastSnr0 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 79), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSnr0.setStatus('current')
ligoRdo3RxLastSnr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 80), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSnr1.setStatus('current')
ligoRdo3RxDropsThreshold = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3RxDropped"))
if mibBuilder.loadTexts: ligoRdo3RxDropsThreshold.setStatus('current')
ligoRdo3TxRetriesThreshold = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3TxRetried"))
if mibBuilder.loadTexts: ligoRdo3TxRetriesThreshold.setStatus('current')
mibBuilder.exportSymbols("LIGO-RADIO3-DRV-MIB", ligoRdo3RxShortGuardInt=ligoRdo3RxShortGuardInt, ligoRdo3TxNotRetried=ligoRdo3TxNotRetried, ligoRdo3TxFragmented=ligoRdo3TxFragmented, ligoRdo3RxBytes=ligoRdo3RxBytes, ligoRdo3Encryption=ligoRdo3Encryption, ligoRdo3TxAltRate=ligoRdo3TxAltRate, ligoRdo3TxBytes=ligoRdo3TxBytes, ligoRdo3RxRoBufExpired=ligoRdo3RxRoBufExpired, ligoRdo3StatsTable=ligoRdo3StatsTable, ligoRdo3RxLastSigLevel2=ligoRdo3RxLastSigLevel2, ligoRdo3RxUnicast=ligoRdo3RxUnicast, ligoRdo3TxMpduBytes=ligoRdo3TxMpduBytes, ligoRdo3RxOfdm=ligoRdo3RxOfdm, ligoRdo3TxPktsInAmsdus=ligoRdo3TxPktsInAmsdus, ligoRdo3RxDropped=ligoRdo3RxDropped, ligoRdo3DrvStats=ligoRdo3DrvStats, ligoRdo3RxLastSnr0=ligoRdo3RxLastSnr0, ligoRdo3RxHtGreenfield=ligoRdo3RxHtGreenfield, ligoRdo3DrvNotifs=ligoRdo3DrvNotifs, ligoRdo3RxUnknown=ligoRdo3RxUnknown, ligoRdo3RxBroadcast=ligoRdo3RxBroadcast, ligoRdo3RxAmsdus=ligoRdo3RxAmsdus, ligoRdo3RxMicErrors=ligoRdo3RxMicErrors, ligoRdo3TxAmsdus=ligoRdo3TxAmsdus, ligoRdo3TxRetried=ligoRdo3TxRetried, ligoRdo3RxCck=ligoRdo3RxCck, ligoRdo3TxXmitDropped=ligoRdo3TxXmitDropped, ligoRdo3Endpoint=ligoRdo3Endpoint, ligoRdo3TxPacketsPerMcs=ligoRdo3TxPacketsPerMcs, ligoRdo3TxOverruns=ligoRdo3TxOverruns, ligoRdo3TxMpdus=ligoRdo3TxMpdus, ligoRdo3RxHtControl=ligoRdo3RxHtControl, ligoRdo3IpAddress=ligoRdo3IpAddress, ligoRdo3RxAmpdus=ligoRdo3RxAmpdus, ligoRdo3DrvConf=ligoRdo3DrvConf, ligoRdo3DrvInfo=ligoRdo3DrvInfo, ligoRdo3Rx40MhzBandwidth=ligoRdo3Rx40MhzBandwidth, ligoRdo3RxKeyNotValid=ligoRdo3RxKeyNotValid, ligoRdo3TxLegacyBytes=ligoRdo3TxLegacyBytes, ligoRdo3RxPacketsPerMcs=ligoRdo3RxPacketsPerMcs, ligoRadio3DrvMIB=ligoRadio3DrvMIB, ligoRdo3TxLegacy=ligoRdo3TxLegacy, ligoRdo3TxPower=ligoRdo3TxPower, ligoRdo3RxRoBufDup=ligoRdo3RxRoBufDup, ligoRdo3TxNotAggregated=ligoRdo3TxNotAggregated, ligoRdo3TxRetriesThreshold=ligoRdo3TxRetriesThreshold, ligoRdo3Capabilities=ligoRdo3Capabilities, ligoRdo3TxFragBytes=ligoRdo3TxFragBytes, ligoRdo3RxRoBufTotal=ligoRdo3RxRoBufTotal, ligoRdo3RxRoBufBuffered=ligoRdo3RxRoBufBuffered, ligoRdo3RxL2Pad=ligoRdo3RxL2Pad, ligoRdo3StatsEntry=ligoRdo3StatsEntry, ligoRdo3RxNoise=ligoRdo3RxNoise, ligoRdo3RxPackets=ligoRdo3RxPackets, ligoRdo3RxRoBufInSeq=ligoRdo3RxRoBufInSeq, ligoRdo3RxStbc=ligoRdo3RxStbc, ligoRdo3RxRoBufReordered=ligoRdo3RxRoBufReordered, ligoRdo3CountryCode=ligoRdo3CountryCode, ligoRdo3RxData=ligoRdo3RxData, ligoRdo3RxRoBufTooBig=ligoRdo3RxRoBufTooBig, ligoRdo3RxIcvErrors=ligoRdo3RxIcvErrors, ligoRdo3RxHtMixedMode=ligoRdo3RxHtMixedMode, ligoRdo3TxPackets=ligoRdo3TxPackets, ligoRdo3RxFragments=ligoRdo3RxFragments, ligoRdo3TxAmsduBytes=ligoRdo3TxAmsduBytes, ligoRdo3Parameters=ligoRdo3Parameters, ligoRdo3TxFailed=ligoRdo3TxFailed, ligoRdo3LastUpdate=ligoRdo3LastUpdate, ligoRdo3RxAclDiscarded=ligoRdo3RxAclDiscarded, ligoRdo3TxXmitFailed=ligoRdo3TxXmitFailed, ligoRdo3TxNoAckRequired=ligoRdo3TxNoAckRequired, ligoRdo3RxLastSigLevel0=ligoRdo3RxLastSigLevel0, ligoRdo3TxMsdus=ligoRdo3TxMsdus, ligoRdo3RxControl=ligoRdo3RxControl, ligoRdo3RxLastSnr1=ligoRdo3RxLastSnr1, ligoRdo3RxMulticast=ligoRdo3RxMulticast, ligoRdo3RxNullData=ligoRdo3RxNullData, ligoRdo3TxManagement=ligoRdo3TxManagement, ligoRdo3TxAckRequired=ligoRdo3TxAckRequired, PYSNMP_MODULE_ID=ligoRadio3DrvMIB, ligoRdo3RxRoBufFlushed=ligoRdo3RxRoBufFlushed, ligoRdo3TxSuccess=ligoRdo3TxSuccess, ligoRdo3RxPacketsInAmsdus=ligoRdo3RxPacketsInAmsdus, ligoRdo3MacAddress=ligoRdo3MacAddress, ligoRdo3RxCrcErrors=ligoRdo3RxCrcErrors, ligoRadio3DrvMIBObjects=ligoRadio3DrvMIBObjects, ligoRdo3RxManagement=ligoRdo3RxManagement, ligoRdo3RxDropsThreshold=ligoRdo3RxDropsThreshold, ligoRdo3RxMpduBytes=ligoRdo3RxMpduBytes, ligoRdo3RxLastSigLevel1=ligoRdo3RxLastSigLevel1, ligoRdo3RxBlockAcks=ligoRdo3RxBlockAcks)

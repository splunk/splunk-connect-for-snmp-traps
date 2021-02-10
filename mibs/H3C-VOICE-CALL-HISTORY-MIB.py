#
# PySNMP MIB module H3C-VOICE-CALL-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOICE-CALL-HISTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AbsoluteCounter32, = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "AbsoluteCounter32")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Gauge32, Integer32, NotificationType, IpAddress, ObjectIdentity, ModuleIdentity, Counter32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "Integer32", "NotificationType", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
h3cVoCallHistory = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16))
h3cVoCallHistory.setRevisions(('2008-02-17 00:00',))
if mibBuilder.loadTexts: h3cVoCallHistory.setLastUpdated('200802170000Z')
if mibBuilder.loadTexts: h3cVoCallHistory.setOrganization('H3C Technologies Co., Ltd.')
class H3cGUid(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class H3cCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("g711a", 1), ("g711u", 2), ("g723r53", 3), ("g723r63", 4), ("g729r8", 5), ("g729a", 6), ("g726r16", 7), ("g726r24", 8), ("g726r32", 9), ("g726r40", 10), ("unknown", 11), ("g729br8", 12))

h3cVoiceCallHistoryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1))
h3cCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1), )
if mibBuilder.loadTexts: h3cCallHistoryTable.setStatus('current')
h3cCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1), ).setIndexNames((0, "H3C-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"))
if mibBuilder.loadTexts: h3cCallHistoryEntry.setStatus('current')
h3cCallHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cCallHistoryIndex.setStatus('current')
h3cCallHistorySetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistorySetupTime.setStatus('current')
h3cCallHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryConnectTime.setStatus('current')
h3cCallHistoryTerminateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryTerminateTime.setStatus('current')
h3cCallHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryPeerAddress.setStatus('current')
h3cCallHistoryPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryPeerId.setStatus('current')
h3cCallHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryLogicalIfIndex.setStatus('current')
h3cCallHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryCallOrigin.setStatus('current')
h3cCallHistoryChargedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 9), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryChargedUnits.setStatus('current')
h3cCallHistoryInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryInfoType.setStatus('current')
h3cCallHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryTransmitPackets.setStatus('current')
h3cCallHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 12), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryTransmitBytes.setStatus('current')
h3cCallHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryReceivePackets.setStatus('current')
h3cCallHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 1, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCallHistoryReceiveBytes.setStatus('current')
h3cVoiceCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2), )
if mibBuilder.loadTexts: h3cVoiceCallHistoryTable.setStatus('current')
h3cVoiceCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1), ).setIndexNames((0, "H3C-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"))
if mibBuilder.loadTexts: h3cVoiceCallHistoryEntry.setStatus('current')
h3cVoCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 1), H3cGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryConnectionId.setStatus('current')
h3cVoCallHistoryTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryTxDuration.setStatus('current')
h3cVoCallHistoryVoiceTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryVoiceTxDuration.setStatus('current')
h3cVoCallHistoryFaxTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryFaxTxDuration.setStatus('current')
h3cVoCallHistoryCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 5), H3cCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryCoderType.setStatus('current')
h3cVoCallHistoryImgPageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHistoryImgPageCount.setStatus('current')
h3cVoiceVoIPCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3), )
if mibBuilder.loadTexts: h3cVoiceVoIPCallHistoryTable.setStatus('current')
h3cVoiceVoIPCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1), ).setIndexNames((0, "H3C-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"))
if mibBuilder.loadTexts: h3cVoiceVoIPCallHistoryEntry.setStatus('current')
h3cVoVoIPCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 1), H3cGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryConnectionId.setStatus('current')
h3cVoVoIPCallHistoryRemSigIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemSigIPType.setStatus('current')
h3cVoVoIPCallHistoryRemSigIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemSigIPAddr.setStatus('current')
h3cVoVoIPCallHistoryRemSigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemSigPort.setStatus('current')
h3cVoVoIPCallHistoryRemMedIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemMedIPType.setStatus('current')
h3cVoVoIPCallHistoryRemMedIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemMedIPAddr.setStatus('current')
h3cVoVoIPCallHistoryRemMedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryRemMedPort.setStatus('current')
h3cVoVoIPCallHistorySessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("h323", 2), ("sip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistorySessProtocol.setStatus('current')
h3cVoVoIPCallHistoryCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 16, 1, 3, 1, 9), H3cCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoVoIPCallHistoryCoderType.setStatus('current')
mibBuilder.exportSymbols("H3C-VOICE-CALL-HISTORY-MIB", h3cCallHistorySetupTime=h3cCallHistorySetupTime, h3cCallHistoryTransmitPackets=h3cCallHistoryTransmitPackets, h3cCallHistoryInfoType=h3cCallHistoryInfoType, h3cCallHistoryTerminateTime=h3cCallHistoryTerminateTime, h3cVoCallHistory=h3cVoCallHistory, H3cCodecType=H3cCodecType, h3cVoVoIPCallHistoryRemMedIPAddr=h3cVoVoIPCallHistoryRemMedIPAddr, h3cCallHistoryReceivePackets=h3cCallHistoryReceivePackets, H3cGUid=H3cGUid, h3cVoCallHistoryTxDuration=h3cVoCallHistoryTxDuration, h3cCallHistoryPeerId=h3cCallHistoryPeerId, h3cVoCallHistoryFaxTxDuration=h3cVoCallHistoryFaxTxDuration, PYSNMP_MODULE_ID=h3cVoCallHistory, h3cCallHistoryTable=h3cCallHistoryTable, h3cVoVoIPCallHistoryCoderType=h3cVoVoIPCallHistoryCoderType, h3cVoVoIPCallHistorySessProtocol=h3cVoVoIPCallHistorySessProtocol, h3cVoVoIPCallHistoryRemSigPort=h3cVoVoIPCallHistoryRemSigPort, h3cVoiceVoIPCallHistoryEntry=h3cVoiceVoIPCallHistoryEntry, h3cCallHistoryCallOrigin=h3cCallHistoryCallOrigin, h3cVoCallHistoryConnectionId=h3cVoCallHistoryConnectionId, h3cCallHistoryChargedUnits=h3cCallHistoryChargedUnits, h3cCallHistoryEntry=h3cCallHistoryEntry, h3cVoVoIPCallHistoryRemSigIPType=h3cVoVoIPCallHistoryRemSigIPType, h3cVoVoIPCallHistoryConnectionId=h3cVoVoIPCallHistoryConnectionId, h3cVoiceCallHistoryEntry=h3cVoiceCallHistoryEntry, h3cVoiceCallHistoryObjects=h3cVoiceCallHistoryObjects, h3cVoCallHistoryVoiceTxDuration=h3cVoCallHistoryVoiceTxDuration, h3cVoVoIPCallHistoryRemMedPort=h3cVoVoIPCallHistoryRemMedPort, h3cCallHistoryIndex=h3cCallHistoryIndex, h3cVoCallHistoryImgPageCount=h3cVoCallHistoryImgPageCount, h3cVoiceCallHistoryTable=h3cVoiceCallHistoryTable, h3cCallHistoryReceiveBytes=h3cCallHistoryReceiveBytes, h3cVoiceVoIPCallHistoryTable=h3cVoiceVoIPCallHistoryTable, h3cVoCallHistoryCoderType=h3cVoCallHistoryCoderType, h3cVoVoIPCallHistoryRemSigIPAddr=h3cVoVoIPCallHistoryRemSigIPAddr, h3cCallHistoryLogicalIfIndex=h3cCallHistoryLogicalIfIndex, h3cVoVoIPCallHistoryRemMedIPType=h3cVoVoIPCallHistoryRemMedIPType, h3cCallHistoryConnectTime=h3cCallHistoryConnectTime, h3cCallHistoryPeerAddress=h3cCallHistoryPeerAddress, h3cCallHistoryTransmitBytes=h3cCallHistoryTransmitBytes)

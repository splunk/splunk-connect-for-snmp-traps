#
# PySNMP MIB module HH3C-POSA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-POSA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Integer32, Gauge32, IpAddress, NotificationType, MibIdentifier, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Integer32", "Gauge32", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "iso", "ObjectIdentity")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
hh3cPosa = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 92))
hh3cPosa.setRevisions(('2014-05-29 00:00', '2008-03-12 09:33',))
if mibBuilder.loadTexts: hh3cPosa.setLastUpdated('201405290000Z')
if mibBuilder.loadTexts: hh3cPosa.setOrganization('Hangzhou H3C Technologies. Co., Ltd.')
class Hh3cAppServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tcp", 1), ("flow", 2))

class Hh3cAppMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("temporary", 2))

class Hh3cPeerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notset", 1), ("down", 2), ("up", 3), ("kept", 4), ("linking", 5), ("linked", 6), ("multilink", 7), ("blocked", 8), ("error", 9))

class Hh3cTerminalAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fcm", 1), ("flow", 2), ("tcp", 3))

class Hh3cTpduChangeStrategy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("changeTpduSrc", 1), ("changeTpduDest", 2))

hh3cPosaControl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1))
hh3cPosaServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaServerEnable.setStatus('current')
hh3cPosaFcmAnswerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(500, 2000)).clone(2000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmAnswerTimeout.setStatus('current')
hh3cPosaFcmTradeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30000, 12000000)).clone(12000000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmTradeTimeout.setStatus('current')
hh3cPosaFcmIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12000)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmIdleTimeout.setStatus('current')
hh3cPosaSrvStateChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaSrvStateChangeTrapEnable.setStatus('current')
hh3cPosaAppStateChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaAppStateChangeTrapEnable.setStatus('current')
hh3cPosaTerminalHangUpTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTerminalHangUpTrapEnable.setStatus('current')
hh3cPosaFcmLnkNegoFailTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmLnkNegoFailTrapEnable.setStatus('current')
hh3cPosaFcmPhyNegoFailTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmPhyNegoFailTrapEnable.setStatus('current')
hh3cPosaTcpConnectionNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpConnectionNumber.setStatus('current')
hh3cPosaFcmConnectionNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaFcmConnectionNumber.setStatus('current')
hh3cPosaTcpConnectionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 12), Integer32().clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTcpConnectionThreshold.setStatus('current')
hh3cPosaFcmConnectionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 13), Integer32().clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmConnectionThreshold.setStatus('current')
hh3cPosaTcpConnectionTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 14), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTcpConnectionTrapEnable.setStatus('current')
hh3cPosaFcmConnectionTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 15), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmConnectionTrapEnable.setStatus('current')
hh3cPosaTcpTradeLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTcpTradeLimit.setStatus('current')
hh3cPosaTcpTradeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 17), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTcpTradeTrapEnable.setStatus('current')
hh3cPosaTcpTradeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 18), Integer32().clone(240)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaTcpTradeTimeout.setStatus('current')
hh3cPosaTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2))
hh3cPosaAppTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1), )
if mibBuilder.loadTexts: hh3cPosaAppTable.setStatus('current')
hh3cPosaAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaAppID"))
if mibBuilder.loadTexts: hh3cPosaAppEntry.setStatus('current')
hh3cPosaAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPosaAppID.setStatus('current')
hh3cPosaAppServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 2), Hh3cAppServiceType().clone('tcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppServiceType.setStatus('current')
hh3cPosaAppIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppIfIndex.setStatus('current')
hh3cPosaAppMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 4), Hh3cAppMode().clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppMode.setStatus('current')
hh3cPosaAppHostIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppHostIPType.setStatus('current')
hh3cPosaAppHostIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppHostIP.setStatus('current')
hh3cPosaAppHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppHostPort.setStatus('current')
hh3cPosaAppRouterIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 8), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppRouterIPType.setStatus('current')
hh3cPosaAppRouterIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 9), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppRouterIP.setStatus('current')
hh3cPosaAppKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7200)).clone(2)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppKeepAliveInterval.setStatus('current')
hh3cPosaAppKeepAliveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 100)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppKeepAliveCount.setStatus('current')
hh3cPosaAppConnectTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(20)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppConnectTimeout.setStatus('current')
hh3cPosaAppState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 13), Hh3cPeerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppState.setStatus('current')
hh3cPosaAppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppRowStatus.setStatus('current')
hh3cPosaAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppName.setStatus('current')
hh3cPosaCallerIDTransEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaCallerIDTransEnable.setStatus('current')
hh3cPosaTpduChangeStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 17), Hh3cTpduChangeStrategy().clone('changeTpduSrc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTpduChangeStrategy.setStatus('current')
hh3cPosaBackupAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaBackupAppID.setStatus('current')
hh3cPosaQuietTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaQuietTimeOut.setStatus('current')
hh3cPosaAppHello = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 20), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppHello.setStatus('current')
hh3cPosaAppHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppHelloInterval.setStatus('current')
hh3cPosaAppRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaAppRouterPort.setStatus('current')
hh3cPosaTerminalTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2), )
if mibBuilder.loadTexts: hh3cPosaTerminalTable.setStatus('current')
hh3cPosaTerminalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaTerminalID"))
if mibBuilder.loadTexts: hh3cPosaTerminalEntry.setStatus('current')
hh3cPosaTerminalID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPosaTerminalID.setStatus('current')
hh3cPosaTerminalAccessType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 2), Hh3cTerminalAccessType().clone('fcm')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalAccessType.setStatus('current')
hh3cPosaTerminalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalIfIndex.setStatus('current')
hh3cPosaTerminalTransAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalTransAppID.setStatus('current')
hh3cPosaTerminalListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalListenPort.setStatus('current')
hh3cPosaTerminalState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 6), Hh3cPeerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalState.setStatus('current')
hh3cPosaTerminalRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalRowStatus.setStatus('current')
hh3cPosaTerminalName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTerminalName.setStatus('current')
hh3cPosaTerminalCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalCfgIfIndex.setStatus('current')
hh3cPosaMapTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3), )
if mibBuilder.loadTexts: hh3cPosaMapTable.setStatus('current')
hh3cPosaMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaMapSrcCode"), (0, "HH3C-POSA-MIB", "hh3cPosaMapDestCode"))
if mibBuilder.loadTexts: hh3cPosaMapEntry.setStatus('current')
hh3cPosaMapDestCode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 7)))
if mibBuilder.loadTexts: hh3cPosaMapDestCode.setStatus('current')
hh3cPosaMapAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaMapAppID.setStatus('current')
hh3cPosaMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaMapRowStatus.setStatus('current')
hh3cPosaMapSrcCode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 7)))
if mibBuilder.loadTexts: hh3cPosaMapSrcCode.setStatus('current')
hh3cPosaFcmStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4), )
if mibBuilder.loadTexts: hh3cPosaFcmStatTable.setStatus('current')
hh3cPosaFcmStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaFcmStatIfIndex"))
if mibBuilder.loadTexts: hh3cPosaFcmStatEntry.setStatus('current')
hh3cPosaFcmStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPosaFcmStatIfIndex.setStatus('current')
hh3cPosaFcmStatTimeoutCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaFcmStatTimeoutCnts.setStatus('current')
hh3cPosaFcmStatConnectFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaFcmStatConnectFailCnts.setStatus('current')
hh3cPosaFcmStatTransCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaFcmStatTransCnts.setStatus('current')
hh3cPosaFcmStatTransSuccessCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaFcmStatTransSuccessCnts.setStatus('current')
hh3cPosaFcmStatTransCntsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmStatTransCntsClear.setStatus('current')
hh3cPosaAppStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5), )
if mibBuilder.loadTexts: hh3cPosaAppStatTable.setStatus('current')
hh3cPosaAppStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaAppID"))
if mibBuilder.loadTexts: hh3cPosaAppStatEntry.setStatus('current')
hh3cPosaAppRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppRecvPkts.setStatus('current')
hh3cPosaAppSendPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppSendPkts.setStatus('current')
hh3cPosaAppErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppErrPkts.setStatus('current')
hh3cPosaAppDistributeErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppDistributeErrCnts.setStatus('current')
hh3cPosaAppInDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppInDiscardedPkts.setStatus('current')
hh3cPosaAppOutDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaAppOutDiscardedPkts.setStatus('current')
hh3cPosaTerminalStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6), )
if mibBuilder.loadTexts: hh3cPosaTerminalStatTable.setStatus('current')
hh3cPosaTerminalStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaTerminalID"))
if mibBuilder.loadTexts: hh3cPosaTerminalStatEntry.setStatus('current')
hh3cPosaTerminalRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalRecvPkts.setStatus('current')
hh3cPosaTerminalSendPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalSendPkts.setStatus('current')
hh3cPosaTerminalErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalErrPkts.setStatus('current')
hh3cPosaTerminalMapErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalMapErrCnts.setStatus('current')
hh3cPosaTerminalInDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalInDiscardedPkts.setStatus('current')
hh3cPosaTerminalOutDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTerminalOutDiscardedPkts.setStatus('current')
hh3cPosaBatchTerminalTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7), )
if mibBuilder.loadTexts: hh3cPosaBatchTerminalTable.setStatus('current')
hh3cPosaBatchTerminalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosaBatchTerminalEntry.setStatus('current')
hh3cPosaBatchTerminalFirstID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaBatchTerminalFirstID.setStatus('current')
hh3cPosaBatchTerminalRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaBatchTerminalRowStatus.setStatus('current')
hh3cPosaTcpTermStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8), )
if mibBuilder.loadTexts: hh3cPosaTcpTermStatTable.setStatus('current')
hh3cPosaTcpTermStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaTcpTermStatIndex"))
if mibBuilder.loadTexts: hh3cPosaTcpTermStatEntry.setStatus('current')
hh3cPosaTcpTermStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cPosaTcpTermStatIndex.setStatus('current')
hh3cPosaTcpTermStatIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTcpTermStatIPType.setStatus('current')
hh3cPosaTcpTermStatIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTcpTermStatIP.setStatus('current')
hh3cPosaTcpTermStatIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTcpTermStatIPMask.setStatus('current')
hh3cPosaTcpTermRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermRecvPkts.setStatus('current')
hh3cPosaTcpTermSendPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermSendPkts.setStatus('current')
hh3cPosaTcpTermErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermErrPkts.setStatus('current')
hh3cPosaTcpTermMapErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermMapErrCnts.setStatus('current')
hh3cPosaTcpTermInDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermInDiscardedPkts.setStatus('current')
hh3cPosaTcpTermOutDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaTcpTermOutDiscardedPkts.setStatus('current')
hh3cPosaTcpTermStatRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaTcpTermStatRowStatus.setStatus('current')
hh3cPosaFcmConfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9), )
if mibBuilder.loadTexts: hh3cPosaFcmConfTable.setStatus('current')
hh3cPosaFcmConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosaFcmConfEntry.setStatus('current')
hh3cPosaFcmNegoHookOff = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 6000)).clone(500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmNegoHookOff.setStatus('current')
hh3cPosaFcmNegoSilence = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmNegoSilence.setStatus('current')
hh3cPosaFcmNegoScrmbBinary1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1500)).clone(250)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmNegoScrmbBinary1.setStatus('current')
hh3cPosaFcmNegoUnscrmbBinary1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1500)).clone(400)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmNegoUnscrmbBinary1.setStatus('current')
hh3cPosaFcmThresholdRlsdOff = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 75)).clone(48)).setUnits('-dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmThresholdRlsdOff.setStatus('current')
hh3cPosaFcmThresholdRlsdOn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 75)).clone(43)).setUnits('-dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmThresholdRlsdOn.setStatus('current')
hh3cPosaFcmThresholdTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 42)).clone(10)).setUnits('-dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmThresholdTxPower.setStatus('current')
hh3cPosaFcmThresholdAnswerTone = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 42)).clone(9)).setUnits('-dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosaFcmThresholdAnswerTone.setStatus('current')
hh3cPosaCallerStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10), )
if mibBuilder.loadTexts: hh3cPosaCallerStatTable.setStatus('current')
hh3cPosaCallerStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1), ).setIndexNames((0, "HH3C-POSA-MIB", "hh3cPosaCallerStatCallerID"))
if mibBuilder.loadTexts: hh3cPosaCallerStatEntry.setStatus('current')
hh3cPosaCallerStatCallerID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: hh3cPosaCallerStatCallerID.setStatus('current')
hh3cPosaCallerRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerRecvPkts.setStatus('current')
hh3cPosaCallerSendPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerSendPkts.setStatus('current')
hh3cPosaCallerErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerErrPkts.setStatus('current')
hh3cPosaCallerMapErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerMapErrCnts.setStatus('current')
hh3cPosaCallerInDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerInDiscardedPkts.setStatus('current')
hh3cPosaCallerOutDiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosaCallerOutDiscardedPkts.setStatus('current')
hh3cPosaCallerStatRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPosaCallerStatRowStatus.setStatus('current')
hh3cPosaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3))
hh3cPosaTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0))
hh3cPosaServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 1)).setObjects(("HH3C-POSA-MIB", "hh3cPosaServerEnable"))
if mibBuilder.loadTexts: hh3cPosaServerStatusChange.setStatus('current')
hh3cPosaAppStateChange = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 2)).setObjects(("HH3C-POSA-MIB", "hh3cPosaAppID"), ("HH3C-POSA-MIB", "hh3cPosaAppStateChangeObject"))
if mibBuilder.loadTexts: hh3cPosaAppStateChange.setStatus('current')
hh3cPosaTerminalHangUp = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosaTerminalHangUp.setStatus('current')
hh3cPosaFcmLinkNegoFailed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosaFcmLinkNegoFailed.setStatus('current')
hh3cPosaFcmPhyNegoFailed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosaFcmPhyNegoFailed.setStatus('current')
hh3cPosaTcpConnectionExceed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 6)).setObjects(("HH3C-POSA-MIB", "hh3cPosaTcpConnectionThreshold"))
if mibBuilder.loadTexts: hh3cPosaTcpConnectionExceed.setStatus('current')
hh3cPosaFcmConnectionExceed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 7)).setObjects(("HH3C-POSA-MIB", "hh3cPosaFcmConnectionThreshold"))
if mibBuilder.loadTexts: hh3cPosaFcmConnectionExceed.setStatus('current')
hh3cPosaTcpTradeExceed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 8)).setObjects(("HH3C-POSA-MIB", "hh3cPosaTcpTradeLimit"), ("HH3C-POSA-MIB", "hh3cPosaTerminalID"))
if mibBuilder.loadTexts: hh3cPosaTcpTradeExceed.setStatus('current')
hh3cPosaTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 1))
hh3cPosaAppStateChangeObject = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPosaAppStateChangeObject.setStatus('current')
mibBuilder.exportSymbols("HH3C-POSA-MIB", hh3cPosaAppKeepAliveCount=hh3cPosaAppKeepAliveCount, hh3cPosaQuietTimeOut=hh3cPosaQuietTimeOut, hh3cPosaMapRowStatus=hh3cPosaMapRowStatus, hh3cPosaTpduChangeStrategy=hh3cPosaTpduChangeStrategy, hh3cPosaBatchTerminalEntry=hh3cPosaBatchTerminalEntry, hh3cPosaTcpTermStatIPMask=hh3cPosaTcpTermStatIPMask, hh3cPosaTerminalStatTable=hh3cPosaTerminalStatTable, hh3cPosaTerminalListenPort=hh3cPosaTerminalListenPort, hh3cPosaTrap=hh3cPosaTrap, hh3cPosaFcmNegoSilence=hh3cPosaFcmNegoSilence, hh3cPosaAppDistributeErrCnts=hh3cPosaAppDistributeErrCnts, hh3cPosaAppHostIPType=hh3cPosaAppHostIPType, hh3cPosaFcmStatTable=hh3cPosaFcmStatTable, hh3cPosa=hh3cPosa, hh3cPosaCallerStatCallerID=hh3cPosaCallerStatCallerID, hh3cPosaTcpConnectionThreshold=hh3cPosaTcpConnectionThreshold, hh3cPosaFcmConfEntry=hh3cPosaFcmConfEntry, hh3cPosaCallerInDiscardedPkts=hh3cPosaCallerInDiscardedPkts, hh3cPosaBatchTerminalTable=hh3cPosaBatchTerminalTable, hh3cPosaServerEnable=hh3cPosaServerEnable, hh3cPosaFcmConnectionTrapEnable=hh3cPosaFcmConnectionTrapEnable, hh3cPosaTerminalStatEntry=hh3cPosaTerminalStatEntry, hh3cPosaAppKeepAliveInterval=hh3cPosaAppKeepAliveInterval, hh3cPosaFcmPhyNegoFailed=hh3cPosaFcmPhyNegoFailed, hh3cPosaTcpTermStatEntry=hh3cPosaTcpTermStatEntry, hh3cPosaCallerMapErrCnts=hh3cPosaCallerMapErrCnts, hh3cPosaBatchTerminalFirstID=hh3cPosaBatchTerminalFirstID, hh3cPosaFcmNegoHookOff=hh3cPosaFcmNegoHookOff, hh3cPosaFcmNegoUnscrmbBinary1=hh3cPosaFcmNegoUnscrmbBinary1, hh3cPosaTerminalHangUp=hh3cPosaTerminalHangUp, hh3cPosaTerminalRowStatus=hh3cPosaTerminalRowStatus, hh3cPosaTcpTermErrPkts=hh3cPosaTcpTermErrPkts, hh3cPosaAppRouterPort=hh3cPosaAppRouterPort, hh3cPosaTcpTradeTimeout=hh3cPosaTcpTradeTimeout, hh3cPosaTcpTermMapErrCnts=hh3cPosaTcpTermMapErrCnts, hh3cPosaServerStatusChange=hh3cPosaServerStatusChange, hh3cPosaAppSendPkts=hh3cPosaAppSendPkts, hh3cPosaAppStateChangeObject=hh3cPosaAppStateChangeObject, hh3cPosaFcmLinkNegoFailed=hh3cPosaFcmLinkNegoFailed, hh3cPosaTerminalInDiscardedPkts=hh3cPosaTerminalInDiscardedPkts, hh3cPosaTcpTermRecvPkts=hh3cPosaTcpTermRecvPkts, hh3cPosaAppHello=hh3cPosaAppHello, hh3cPosaFcmStatTimeoutCnts=hh3cPosaFcmStatTimeoutCnts, hh3cPosaTerminalSendPkts=hh3cPosaTerminalSendPkts, hh3cPosaTcpTradeExceed=hh3cPosaTcpTradeExceed, hh3cPosaTerminalAccessType=hh3cPosaTerminalAccessType, hh3cPosaFcmConnectionThreshold=hh3cPosaFcmConnectionThreshold, hh3cPosaTerminalTransAppID=hh3cPosaTerminalTransAppID, hh3cPosaAppHostPort=hh3cPosaAppHostPort, hh3cPosaAppStateChange=hh3cPosaAppStateChange, hh3cPosaCallerIDTransEnable=hh3cPosaCallerIDTransEnable, hh3cPosaSrvStateChangeTrapEnable=hh3cPosaSrvStateChangeTrapEnable, hh3cPosaBatchTerminalRowStatus=hh3cPosaBatchTerminalRowStatus, hh3cPosaMapDestCode=hh3cPosaMapDestCode, hh3cPosaCallerStatTable=hh3cPosaCallerStatTable, hh3cPosaTerminalTable=hh3cPosaTerminalTable, hh3cPosaTcpConnectionTrapEnable=hh3cPosaTcpConnectionTrapEnable, hh3cPosaTerminalIfIndex=hh3cPosaTerminalIfIndex, hh3cPosaTcpTermStatIPType=hh3cPosaTcpTermStatIPType, hh3cPosaTcpTradeTrapEnable=hh3cPosaTcpTradeTrapEnable, hh3cPosaAppRouterIP=hh3cPosaAppRouterIP, hh3cPosaAppName=hh3cPosaAppName, hh3cPosaTcpConnectionNumber=hh3cPosaTcpConnectionNumber, hh3cPosaFcmStatTransCnts=hh3cPosaFcmStatTransCnts, hh3cPosaTcpTermOutDiscardedPkts=hh3cPosaTcpTermOutDiscardedPkts, hh3cPosaFcmStatTransCntsClear=hh3cPosaFcmStatTransCntsClear, hh3cPosaAppHostIP=hh3cPosaAppHostIP, hh3cPosaFcmTradeTimeout=hh3cPosaFcmTradeTimeout, hh3cPosaFcmStatIfIndex=hh3cPosaFcmStatIfIndex, hh3cPosaMapEntry=hh3cPosaMapEntry, hh3cPosaAppHelloInterval=hh3cPosaAppHelloInterval, hh3cPosaAppErrPkts=hh3cPosaAppErrPkts, PYSNMP_MODULE_ID=hh3cPosa, hh3cPosaTerminalRecvPkts=hh3cPosaTerminalRecvPkts, hh3cPosaTcpTermInDiscardedPkts=hh3cPosaTcpTermInDiscardedPkts, hh3cPosaAppID=hh3cPosaAppID, hh3cPosaTerminalName=hh3cPosaTerminalName, hh3cPosaTables=hh3cPosaTables, hh3cPosaFcmStatConnectFailCnts=hh3cPosaFcmStatConnectFailCnts, hh3cPosaCallerSendPkts=hh3cPosaCallerSendPkts, hh3cPosaMapSrcCode=hh3cPosaMapSrcCode, hh3cPosaAppServiceType=hh3cPosaAppServiceType, hh3cPosaFcmThresholdAnswerTone=hh3cPosaFcmThresholdAnswerTone, hh3cPosaAppEntry=hh3cPosaAppEntry, hh3cPosaFcmThresholdTxPower=hh3cPosaFcmThresholdTxPower, hh3cPosaFcmConfTable=hh3cPosaFcmConfTable, hh3cPosaTcpTermStatIP=hh3cPosaTcpTermStatIP, hh3cPosaTerminalHangUpTrapEnable=hh3cPosaTerminalHangUpTrapEnable, hh3cPosaAppStatTable=hh3cPosaAppStatTable, hh3cPosaAppMode=hh3cPosaAppMode, hh3cPosaFcmPhyNegoFailTrapEnable=hh3cPosaFcmPhyNegoFailTrapEnable, hh3cPosaFcmNegoScrmbBinary1=hh3cPosaFcmNegoScrmbBinary1, hh3cPosaAppInDiscardedPkts=hh3cPosaAppInDiscardedPkts, hh3cPosaTerminalCfgIfIndex=hh3cPosaTerminalCfgIfIndex, hh3cPosaBackupAppID=hh3cPosaBackupAppID, hh3cPosaFcmConnectionExceed=hh3cPosaFcmConnectionExceed, Hh3cTpduChangeStrategy=Hh3cTpduChangeStrategy, hh3cPosaAppStatEntry=hh3cPosaAppStatEntry, hh3cPosaFcmLnkNegoFailTrapEnable=hh3cPosaFcmLnkNegoFailTrapEnable, hh3cPosaCallerStatEntry=hh3cPosaCallerStatEntry, hh3cPosaCallerStatRowStatus=hh3cPosaCallerStatRowStatus, hh3cPosaFcmAnswerTimeout=hh3cPosaFcmAnswerTimeout, hh3cPosaFcmThresholdRlsdOn=hh3cPosaFcmThresholdRlsdOn, hh3cPosaFcmConnectionNumber=hh3cPosaFcmConnectionNumber, hh3cPosaTerminalErrPkts=hh3cPosaTerminalErrPkts, hh3cPosaTerminalOutDiscardedPkts=hh3cPosaTerminalOutDiscardedPkts, hh3cPosaCallerRecvPkts=hh3cPosaCallerRecvPkts, Hh3cAppServiceType=Hh3cAppServiceType, hh3cPosaAppStateChangeTrapEnable=hh3cPosaAppStateChangeTrapEnable, Hh3cPeerState=Hh3cPeerState, hh3cPosaTcpTermStatIndex=hh3cPosaTcpTermStatIndex, hh3cPosaTcpTermSendPkts=hh3cPosaTcpTermSendPkts, hh3cPosaTerminalID=hh3cPosaTerminalID, hh3cPosaFcmIdleTimeout=hh3cPosaFcmIdleTimeout, Hh3cTerminalAccessType=Hh3cTerminalAccessType, hh3cPosaCallerOutDiscardedPkts=hh3cPosaCallerOutDiscardedPkts, hh3cPosaAppIfIndex=hh3cPosaAppIfIndex, hh3cPosaAppConnectTimeout=hh3cPosaAppConnectTimeout, hh3cPosaFcmStatEntry=hh3cPosaFcmStatEntry, hh3cPosaFcmThresholdRlsdOff=hh3cPosaFcmThresholdRlsdOff, hh3cPosaTcpTradeLimit=hh3cPosaTcpTradeLimit, hh3cPosaAppTable=hh3cPosaAppTable, hh3cPosaTrapPrex=hh3cPosaTrapPrex, Hh3cAppMode=Hh3cAppMode, hh3cPosaTerminalState=hh3cPosaTerminalState, hh3cPosaTcpTermStatRowStatus=hh3cPosaTcpTermStatRowStatus, hh3cPosaTerminalEntry=hh3cPosaTerminalEntry, hh3cPosaTcpConnectionExceed=hh3cPosaTcpConnectionExceed, hh3cPosaAppState=hh3cPosaAppState, hh3cPosaAppRecvPkts=hh3cPosaAppRecvPkts, hh3cPosaTerminalMapErrCnts=hh3cPosaTerminalMapErrCnts, hh3cPosaMapTable=hh3cPosaMapTable, hh3cPosaAppRouterIPType=hh3cPosaAppRouterIPType, hh3cPosaAppOutDiscardedPkts=hh3cPosaAppOutDiscardedPkts, hh3cPosaControl=hh3cPosaControl, hh3cPosaFcmStatTransSuccessCnts=hh3cPosaFcmStatTransSuccessCnts, hh3cPosaAppRowStatus=hh3cPosaAppRowStatus, hh3cPosaMapAppID=hh3cPosaMapAppID, hh3cPosaTcpTermStatTable=hh3cPosaTcpTermStatTable, hh3cPosaCallerErrPkts=hh3cPosaCallerErrPkts, hh3cPosaTrapObjects=hh3cPosaTrapObjects)

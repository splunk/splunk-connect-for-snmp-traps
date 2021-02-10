#
# PySNMP MIB module CXLapBConv-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXLapBConv-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
SapIndex, cxLapBConv, Alias = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "cxLapBConv", "Alias")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Integer32, Counter32, TimeTicks, Counter64, ModuleIdentity, Gauge32, MibIdentifier, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PSapIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class SubRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

lapbcnvSysRouteConnectInterval = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 900)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSysRouteConnectInterval.setStatus('mandatory')
lapbcnvSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10), )
if mibBuilder.loadTexts: lapbcnvSapTable.setStatus('mandatory')
lapbcnvSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1), ).setIndexNames((0, "CXLapBConv-MIB", "lapbcnvSapNumber"))
if mibBuilder.loadTexts: lapbcnvSapEntry.setStatus('mandatory')
lapbcnvSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 1), PSapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapNumber.setStatus('mandatory')
lapbcnvSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSapRowStatus.setStatus('mandatory')
lapbcnvSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSapAlias.setStatus('mandatory')
lapbcnvSapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: lapbcnvSapControl.setStatus('mandatory')
lapbcnvSapState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("offLine", 1), ("unbound", 2), ("notConnected", 3), ("inProgress", 4), ("connected", 5))).clone('unbound')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapState.setStatus('mandatory')
lapbcnvSapTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapTxFrames.setStatus('mandatory')
lapbcnvSapRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapRxFrames.setStatus('mandatory')
lapbcnvSapTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapTxOctets.setStatus('mandatory')
lapbcnvSapRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapRxOctets.setStatus('mandatory')
lapbcnvSapOutSuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapOutSuccessfullConnects.setStatus('mandatory')
lapbcnvSapOutUnsuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapOutUnsuccessfullConnects.setStatus('mandatory')
lapbcnvSapInSuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapInSuccessfullConnects.setStatus('mandatory')
lapbcnvSapInUnsuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapInUnsuccessfullConnects.setStatus('mandatory')
lapbcnvSapUnopenedServiceDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapUnopenedServiceDiscards.setStatus('mandatory')
lapbcnvSapTxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapTxResets.setStatus('mandatory')
lapbcnvSapRxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSapRxResets.setStatus('mandatory')
lapbcnvSysRouteTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11), )
if mibBuilder.loadTexts: lapbcnvSysRouteTable.setStatus('mandatory')
lapbcnvSysRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1), ).setIndexNames((0, "CXLapBConv-MIB", "lapbcnvSRSapNumber"))
if mibBuilder.loadTexts: lapbcnvSysRouteEntry.setStatus('mandatory')
lapbcnvSRSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSRSapNumber.setStatus('mandatory')
lapbcnvSRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSRRowStatus.setStatus('mandatory')
lapbcnvSRDestAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSRDestAlias.setStatus('mandatory')
lapbcnvSRSubRef = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 4), SubRef()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbcnvSRSubRef.setStatus('mandatory')
lapbcnvSRRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("offLine", 1), ("notConnected", 2), ("inProgress", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSRRouteStatus.setStatus('mandatory')
lapbcnvSRClearStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("noFailure", 1), ("internalError", 2), ("localAllocFailure", 3), ("remoteAllocFailure", 4), ("localNoAccess", 5), ("remoteNoAccess", 6), ("localPvcDown", 7), ("remotePvcDown", 8), ("localPvcBusy", 9), ("remotePvcBusy", 10), ("localFcnFailure", 11), ("remoteFcnFailure", 12), ("localDsnFailure", 13), ("localRefInUse", 14), ("remoteAliasNotFound", 15), ("remoteNoPvcService", 16), ("mpeInvalidSubref", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbcnvSRClearStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CXLapBConv-MIB", lapbcnvSapRowStatus=lapbcnvSapRowStatus, PSapIndex=PSapIndex, lapbcnvSapState=lapbcnvSapState, lapbcnvSysRouteEntry=lapbcnvSysRouteEntry, lapbcnvSRDestAlias=lapbcnvSRDestAlias, lapbcnvSRClearStatus=lapbcnvSRClearStatus, lapbcnvSRSapNumber=lapbcnvSRSapNumber, lapbcnvSysRouteTable=lapbcnvSysRouteTable, lapbcnvSapUnopenedServiceDiscards=lapbcnvSapUnopenedServiceDiscards, lapbcnvSysRouteConnectInterval=lapbcnvSysRouteConnectInterval, lapbcnvSapInUnsuccessfullConnects=lapbcnvSapInUnsuccessfullConnects, lapbcnvSapRxResets=lapbcnvSapRxResets, SubRef=SubRef, lapbcnvSapRxFrames=lapbcnvSapRxFrames, lapbcnvSapTxFrames=lapbcnvSapTxFrames, lapbcnvSapTxResets=lapbcnvSapTxResets, lapbcnvSapRxOctets=lapbcnvSapRxOctets, lapbcnvSapNumber=lapbcnvSapNumber, lapbcnvSapOutSuccessfullConnects=lapbcnvSapOutSuccessfullConnects, lapbcnvSRRouteStatus=lapbcnvSRRouteStatus, lapbcnvSapAlias=lapbcnvSapAlias, lapbcnvSapOutUnsuccessfullConnects=lapbcnvSapOutUnsuccessfullConnects, lapbcnvSapTxOctets=lapbcnvSapTxOctets, lapbcnvSapEntry=lapbcnvSapEntry, lapbcnvSapControl=lapbcnvSapControl, lapbcnvSapInSuccessfullConnects=lapbcnvSapInSuccessfullConnects, lapbcnvSRRowStatus=lapbcnvSRRowStatus, lapbcnvSRSubRef=lapbcnvSRSubRef, lapbcnvSapTable=lapbcnvSapTable)

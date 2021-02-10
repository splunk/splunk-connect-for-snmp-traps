#
# PySNMP MIB module MITEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, Counter64, Unsigned32, Bits, NotificationType, MibIdentifier, internet, ObjectIdentity, IpAddress, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Counter64", "Unsigned32", "Bits", "NotificationType", "MibIdentifier", "internet", "ObjectIdentity", "IpAddress", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
snmpV2 = MibIdentifier((1, 3, 6, 1, 6))
snmpDomains = MibIdentifier((1, 3, 6, 1, 6, 1))
snmpUDPDomain = MibIdentifier((1, 3, 6, 1, 6, 1, 1))
class InterfaceIndex(Integer32):
    pass

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 2))
mitelExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 3))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5))
mitelIdMgmtPlatforms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdTerminals = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 3))
mitelIdInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 4))
mitelIdCtiPlatforms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 5))
mitelIdMgmtOpsMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 1, 1))
mitelIdCsMc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 1))
mitelIdCs2000Light = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 2))
mitelExtInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 3, 2))
mitelPropApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1))
mitelPropTransmission = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 2))
mitelPropProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 3))
mitelPropUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 4))
mitelPropHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 5))
mitelPropNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 6))
mitelPropReset = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 7))
mitelAppCallServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1))
mitelNotifTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1))
mitelConfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 1))
mitelConfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2))
mitelGrpCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1))
mitelGrpOpsMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 2))
mitelGrpCs2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3))
mitelConfAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 3))
class TDomain(ObjectIdentifier):
    pass

class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class MitelIfType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dnic", 1))

class MitelNotifyTransportType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mitelNotifTransV1Trap", 1), ("mitelNotifTransV2Trap", 2), ("mitelNotifTransInform", 3))

mitelIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 1027, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfNumber.setStatus('mandatory')
mitelIfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2), )
if mibBuilder.loadTexts: mitelIfTable.setStatus('mandatory')
mitelIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIfTableEntry.setStatus('mandatory')
mitelIfTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1), MitelIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfTblType.setStatus('mandatory')
mitelResetReason = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("shutdown", 1), ("coldStart", 2), ("warmStart", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelResetReason.setStatus('mandatory')
mitelResetPlatform = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelResetPlatform.setStatus('mandatory')
mitelResetAgent = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelResetAgent.setStatus('mandatory')
mitelNotifCount = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifCount.setStatus('mandatory')
mitelNotifEnableTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3), )
if mibBuilder.loadTexts: mitelNotifEnableTable.setStatus('mandatory')
mitelNotifEnableTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifEnblTblIndex"))
if mibBuilder.loadTexts: mitelNotifEnableTableEntry.setStatus('mandatory')
mitelNotifEnblTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblIndex.setStatus('mandatory')
mitelNotifEnblTblOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblOid.setStatus('mandatory')
mitelNotifEnblTblEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifEnblTblEnable.setStatus('mandatory')
mitelNotifEnblTblAck = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifEnblTblAck.setStatus('mandatory')
mitelNotifEnblTblOccurrences = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblOccurrences.setStatus('mandatory')
mitelNotifEnblTblDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblDescr.setStatus('mandatory')
mitelNotifManagerTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4), )
if mibBuilder.loadTexts: mitelNotifManagerTable.setStatus('mandatory')
mitelNotifManagerTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifMgrTblIndex"))
if mibBuilder.loadTexts: mitelNotifManagerTableEntry.setStatus('mandatory')
mitelNotifMgrTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifMgrTblIndex.setStatus('mandatory')
mitelNotifMgrTblStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 2), RowStatus().clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblStatus.setStatus('mandatory')
mitelNotifMgrTblTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 3), MitelNotifyTransportType().clone('mitelNotifTransV1Trap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblTransport.setStatus('mandatory')
mitelNotifMgrTblDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 4), TDomain().clone((1, 3, 6, 1, 6, 1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblDomain.setStatus('mandatory')
mitelNotifMgrTblAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 5), TAddress().clone(hexValue="c00002000489")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblAddress.setStatus('mandatory')
mitelNotifMgrTblTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 6), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblTimeout.setStatus('mandatory')
mitelNotifMgrTblRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblRetries.setStatus('mandatory')
mitelNotifMgrTblLife = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 8), TimeInterval().clone(8640000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblLife.setStatus('mandatory')
mitelNotifMgrTblCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 9), OctetString().clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblCommunity.setStatus('mandatory')
mitelNotifMgrTblName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 10), DisplayString().clone('None specified.')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblName.setStatus('mandatory')
mitelNotifHistoryMax = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 5), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifHistoryMax.setStatus('mandatory')
mitelNotifHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistorySize.setStatus('mandatory')
mitelNotifHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7), )
if mibBuilder.loadTexts: mitelNotifHistoryTable.setStatus('mandatory')
mitelNotifHistoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifHistTblIndex"))
if mibBuilder.loadTexts: mitelNotifHistoryTableEntry.setStatus('mandatory')
mitelNotifHistTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblIndex.setStatus('mandatory')
mitelNotifHistTblId = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblId.setStatus('mandatory')
mitelNotifHistTblTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblTime.setStatus('mandatory')
mitelNotifHistTblIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblIfIndex.setStatus('mandatory')
mitelNotifHistTblConfirmed = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblConfirmed.setStatus('mandatory')
mitelNotifUnackTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8), )
if mibBuilder.loadTexts: mitelNotifUnackTable.setStatus('mandatory')
mitelNotifUnackTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifUnackTblIndex"))
if mibBuilder.loadTexts: mitelNotifUnackTableEntry.setStatus('mandatory')
mitelNotifUnackTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblIndex.setStatus('mandatory')
mitelNotifUnackTblStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("destory", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifUnackTblStatus.setStatus('mandatory')
mitelNotifUnackTblHistory = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblHistory.setStatus('mandatory')
mitelNotifUnackTblManager = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblManager.setStatus('mandatory')
mitelNotifUnackTblRetriesLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblRetriesLeft.setStatus('mandatory')
mitelNotifAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 9), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifAgentAddress.setStatus('mandatory')
mitelTrapsCommLost = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1) + (0,1)).setObjects(("MITEL-MIB", "mitelNotifUnackTblStatus"), ("MITEL-MIB", "mitelNotifMgrTblDomain"), ("MITEL-MIB", "mitelNotifMgrTblAddress"))
mitelTrapsReset = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1) + (0,2)).setObjects(("MITEL-MIB", "mitelNotifUnackTblStatus"), ("MITEL-MIB", "mitelResetReason"))
mitelGrpCmnNotifBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 2))
mitelGrpCmnNotifManagers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 3))
mitelGrpCmnNotifHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 4))
mitelGrpCmnNotifAck = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 5))
mitelGrpCmnInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6))
mitelGrpCmnReset = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 7))
mitelComplMitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 1, 1))
mibBuilder.exportSymbols("MITEL-MIB", snmpUDPDomain=snmpUDPDomain, mitelNotifMgrTblLife=mitelNotifMgrTblLife, mitelNotifMgrTblStatus=mitelNotifMgrTblStatus, mitelIdInterfaces=mitelIdInterfaces, TimeStamp=TimeStamp, mitelGrpCommon=mitelGrpCommon, mitelNotifHistoryTableEntry=mitelNotifHistoryTableEntry, mitelExtInterfaces=mitelExtInterfaces, mitelGrpCmnNotifBasic=mitelGrpCmnNotifBasic, TruthValue=TruthValue, mitelPropProtocols=mitelPropProtocols, mitelNotifUnackTableEntry=mitelNotifUnackTableEntry, mitelResetReason=mitelResetReason, mitelNotifEnableTable=mitelNotifEnableTable, mitelNotifMgrTblRetries=mitelNotifMgrTblRetries, RowStatus=RowStatus, MitelNotifyTransportType=MitelNotifyTransportType, mitelNotifHistoryMax=mitelNotifHistoryMax, mitelTrapsCommLost=mitelTrapsCommLost, mitelGrpCmnInterfaces=mitelGrpCmnInterfaces, mitelNotifMgrTblDomain=mitelNotifMgrTblDomain, mitelNotifEnblTblEnable=mitelNotifEnblTblEnable, mitelResetAgent=mitelResetAgent, mitelNotifEnblTblOid=mitelNotifEnblTblOid, snmpV2=snmpV2, mitelNotifHistoryTable=mitelNotifHistoryTable, mitelConformance=mitelConformance, mitelIdMgmtOpsMgr=mitelIdMgmtOpsMgr, mitelResetPlatform=mitelResetPlatform, mitelPropTransmission=mitelPropTransmission, snmpDomains=snmpDomains, mitelPropReset=mitelPropReset, InterfaceIndex=InterfaceIndex, mitelNotifUnackTblStatus=mitelNotifUnackTblStatus, mitelPropHardware=mitelPropHardware, MitelIfType=MitelIfType, mitelGrpCmnReset=mitelGrpCmnReset, mitelGrpOpsMgr=mitelGrpOpsMgr, mitelNotifMgrTblAddress=mitelNotifMgrTblAddress, mitelNotifHistTblConfirmed=mitelNotifHistTblConfirmed, mitelIfTable=mitelIfTable, mitelNotifUnackTblRetriesLeft=mitelNotifUnackTblRetriesLeft, mitelNotifHistTblTime=mitelNotifHistTblTime, mitelNotifHistTblIndex=mitelNotifHistTblIndex, mitelPropApplications=mitelPropApplications, mitelPropNotifications=mitelPropNotifications, mitelNotifMgrTblIndex=mitelNotifMgrTblIndex, mitelConfAgents=mitelConfAgents, mitelNotifTraps=mitelNotifTraps, mitelConfGroups=mitelConfGroups, mitelIfTableEntry=mitelIfTableEntry, mitelGrpCmnNotifHistory=mitelGrpCmnNotifHistory, mitelNotifMgrTblTimeout=mitelNotifMgrTblTimeout, mitelPropUtilities=mitelPropUtilities, mitelNotifHistTblIfIndex=mitelNotifHistTblIfIndex, mitelNotifEnblTblDescr=mitelNotifEnblTblDescr, mitelIdCsMc2=mitelIdCsMc2, mitelExtensions=mitelExtensions, mitelNotifAgentAddress=mitelNotifAgentAddress, mitelNotifMgrTblTransport=mitelNotifMgrTblTransport, mitelNotifManagerTableEntry=mitelNotifManagerTableEntry, TAddress=TAddress, mitelNotifHistorySize=mitelNotifHistorySize, mitelComplMitel=mitelComplMitel, mitelNotifCount=mitelNotifCount, TDomain=TDomain, mitelIdCtiPlatforms=mitelIdCtiPlatforms, mitelIdTerminals=mitelIdTerminals, mitelGrpCmnNotifAck=mitelGrpCmnNotifAck, mitelNotifHistTblId=mitelNotifHistTblId, mitelIdCs2000Light=mitelIdCs2000Light, mitelNotifMgrTblName=mitelNotifMgrTblName, mitelNotifMgrTblCommunity=mitelNotifMgrTblCommunity, mitelConfCompliances=mitelConfCompliances, mitelIdCallServers=mitelIdCallServers, mitelNotifEnableTableEntry=mitelNotifEnableTableEntry, mitelIfNumber=mitelIfNumber, TimeInterval=TimeInterval, mitelProprietary=mitelProprietary, mitelNotifEnblTblOccurrences=mitelNotifEnblTblOccurrences, mitelNotifUnackTblManager=mitelNotifUnackTblManager, mitelNotifUnackTable=mitelNotifUnackTable, mitelIdMgmtPlatforms=mitelIdMgmtPlatforms, mitelIfTblType=mitelIfTblType, mitelNotifUnackTblIndex=mitelNotifUnackTblIndex, mitelTrapsReset=mitelTrapsReset, mitelNotifUnackTblHistory=mitelNotifUnackTblHistory, mitelNotifEnblTblIndex=mitelNotifEnblTblIndex, mitelAppCallServer=mitelAppCallServer, mitel=mitel, mitelNotifEnblTblAck=mitelNotifEnblTblAck, mitelIdentification=mitelIdentification, mitelExperimental=mitelExperimental, mitelNotifManagerTable=mitelNotifManagerTable, mitelGrpCmnNotifManagers=mitelGrpCmnNotifManagers, mitelGrpCs2000=mitelGrpCs2000)

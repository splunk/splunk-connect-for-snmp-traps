#
# PySNMP MIB module Dell-LAN-SYSMNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-LAN-SYSMNG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
dellLanCommon, = mibBuilder.importSymbols("Dell-Vendor-MIB", "dellLanCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, NotificationType, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ModuleIdentity, iso, ObjectIdentity, Bits, NotificationType, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "NotificationType", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Gauge32")
DateAndTime, RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
dellLanSystemMng = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2))
if mibBuilder.loadTexts: dellLanSystemMng.setLastUpdated('201304120000Z')
if mibBuilder.loadTexts: dellLanSystemMng.setOrganization('Dell Inc.')
dellLanMngIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1))
dellLanFileSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2))
dellLanSysMngGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3))
class DellLanMngInfServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allType", 0), ("telnet", 1), ("snmp", 2), ("http", 3), ("https", 4), ("ssh", 5), ("sntp", 6))

class DellLanMngInfActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("permit", 0), ("deny", 1))

dellLanMngInfEnable = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfEnable.setStatus('current')
dellLanMngInfActiveListName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfActiveListName.setStatus('current')
dellLanMngInfListTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3), )
if mibBuilder.loadTexts: dellLanMngInfListTable.setStatus('current')
dellLanMngInfListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1), ).setIndexNames((0, "Dell-LAN-SYSMNG-MIB", "dellLanMngInfListName"), (0, "Dell-LAN-SYSMNG-MIB", "dellLanMngInfListPriority"))
if mibBuilder.loadTexts: dellLanMngInfListEntry.setStatus('current')
dellLanMngInfListName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanMngInfListName.setStatus('current')
dellLanMngInfListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanMngInfListPriority.setStatus('current')
dellLanMngInfListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListIfIndex.setStatus('current')
dellLanMngInfListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListIpAddr.setStatus('current')
dellLanMngInfListIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListIpNetMask.setStatus('current')
dellLanMngInfListService = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 6), DellLanMngInfServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListService.setStatus('current')
dellLanMngInfListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 7), DellLanMngInfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListAction.setStatus('current')
dellLanMngInfListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListRowStatus.setStatus('current')
dellLanMngInfListVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanMngInfListVlanId.setStatus('current')
dellLanFSMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFSMaxSize.setStatus('current')
dellLanFSAvailableSize = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFSAvailableSize.setStatus('current')
dellLanFileTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3), )
if mibBuilder.loadTexts: dellLanFileTable.setStatus('current')
dellLanFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1), ).setIndexNames((0, "Dell-LAN-SYSMNG-MIB", "dellLanFileName"))
if mibBuilder.loadTexts: dellLanFileEntry.setStatus('current')
dellLanFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileName.setStatus('current')
dellLanFilePermission = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("readonly", 1), ("writeonly", 2), ("readWrite", 3), ("noReadNoWrite", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFilePermission.setStatus('current')
dellLanFilePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFilePriority.setStatus('current')
dellLanFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileSize.setStatus('current')
dellLanFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("image", 1), ("config", 2), ("log", 3), ("sys", 4), ("activeImg", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileType.setStatus('current')
dellLanFileModificationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileModificationDate.setStatus('current')
dellLanFileModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileModificationTime.setStatus('current')
dellLanFileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFileDescription.setStatus('current')
dellLanFileActionTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4), )
if mibBuilder.loadTexts: dellLanFileActionTable.setStatus('current')
dellLanFileActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1), ).setIndexNames((0, "Dell-LAN-SYSMNG-MIB", "dellLanFileActionIndex"))
if mibBuilder.loadTexts: dellLanFileActionEntry.setStatus('current')
dellLanFileActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileActionIndex.setStatus('current')
dellLanFileActionSourceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFileActionSourceFile.setStatus('current')
dellLanFileActionDestFile = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFileActionDestFile.setStatus('current')
dellLanFileActionForceAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFileActionForceAction.setStatus('current')
dellLanFileActionCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("copy", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanFileActionCommand.setStatus('current')
dellLanFileActionResultCode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("success", 0), ("statusPending", 1), ("fileNotFound", 2), ("invalidCmd", 3), ("unknownError", 4), ("tftpServerConnectFailed", 5), ("fileSystemFull", 6), ("overwriteNotRequested", 7), ("overwriteFailed", 8), ("permissionDenied", 9), ("incompatFileType", 10), ("invalidDest", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellLanFileActionResultCode.setStatus('current')
dellLanSysActionReload = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanSysActionReload.setStatus('current')
dellLanSysActionSetActiveImage = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLanSysActionSetActiveImage.setStatus('current')
mibBuilder.exportSymbols("Dell-LAN-SYSMNG-MIB", dellLanSysActionReload=dellLanSysActionReload, dellLanFileActionEntry=dellLanFileActionEntry, dellLanFileDescription=dellLanFileDescription, dellLanMngInfListName=dellLanMngInfListName, dellLanFileActionResultCode=dellLanFileActionResultCode, dellLanFileActionTable=dellLanFileActionTable, DellLanMngInfServiceType=DellLanMngInfServiceType, dellLanSystemMng=dellLanSystemMng, dellLanFileActionSourceFile=dellLanFileActionSourceFile, dellLanMngInfListRowStatus=dellLanMngInfListRowStatus, dellLanFileSize=dellLanFileSize, dellLanFileActionIndex=dellLanFileActionIndex, dellLanFilePermission=dellLanFilePermission, dellLanFileType=dellLanFileType, DellLanMngInfActionType=DellLanMngInfActionType, dellLanMngInfListService=dellLanMngInfListService, dellLanMngInfListAction=dellLanMngInfListAction, dellLanMngInfListIpAddr=dellLanMngInfListIpAddr, dellLanFileSysGroup=dellLanFileSysGroup, dellLanFileModificationDate=dellLanFileModificationDate, dellLanMngInfListTable=dellLanMngInfListTable, dellLanFSMaxSize=dellLanFSMaxSize, dellLanFileTable=dellLanFileTable, dellLanMngInfListEntry=dellLanMngInfListEntry, dellLanFileModificationTime=dellLanFileModificationTime, dellLanFileActionCommand=dellLanFileActionCommand, dellLanSysMngGroup=dellLanSysMngGroup, PYSNMP_MODULE_ID=dellLanSystemMng, dellLanFileName=dellLanFileName, dellLanMngInfListVlanId=dellLanMngInfListVlanId, dellLanMngInfListIpNetMask=dellLanMngInfListIpNetMask, dellLanFilePriority=dellLanFilePriority, dellLanMngInfListIfIndex=dellLanMngInfListIfIndex, dellLanSysActionSetActiveImage=dellLanSysActionSetActiveImage, dellLanMngInfListPriority=dellLanMngInfListPriority, dellLanFileActionDestFile=dellLanFileActionDestFile, dellLanFileActionForceAction=dellLanFileActionForceAction, dellLanMngInfActiveListName=dellLanMngInfActiveListName, dellLanMngIfGroup=dellLanMngIfGroup, dellLanFileEntry=dellLanFileEntry, dellLanMngInfEnable=dellLanMngInfEnable, dellLanFSAvailableSize=dellLanFSAvailableSize)

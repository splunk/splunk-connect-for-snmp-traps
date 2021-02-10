#
# PySNMP MIB module HH3C-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-CONFIG-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Counter64, MibIdentifier, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Bits, ModuleIdentity, Integer32, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Bits", "ModuleIdentity", "Integer32", "iso", "Gauge32", "NotificationType")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
hh3cConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 4))
hh3cConfig.setRevisions(('2011-11-26 00:00',))
if mibBuilder.loadTexts: hh3cConfig.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: hh3cConfig.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class ConfigOperationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("running2Startup", 1), ("startup2Running", 2), ("running2Net", 3), ("net2Running", 4), ("net2Startup", 5), ("startup2Net", 6))

class ConfigOperationStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opInvalidOperation", 3), ("opInvalidProtocol", 4), ("opInvalidSourceName", 5), ("opInvalidDestName", 6), ("opInvalidServerAddress", 7), ("opDeviceBusy", 8), ("opDeviceOpenError", 9), ("opDeviceError", 10), ("opDeviceNotProgrammable", 11), ("opDeviceFull", 12), ("opFileOpenError", 13), ("opFileTransferError", 14), ("opFileChecksumError", 15), ("opNoMemory", 16), ("opAuthFail", 17), ("opTimeOut", 18), ("opUnknownFailure", 19), ("opInvalidConfigFile", 20), ("opSlaveFull", 21), ("opCopyToSlaveFailure", 22))

hh3cConfigManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1))
hh3cCfgLog = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1))
hh3cCfgRunModifiedLast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgRunModifiedLast.setStatus('current')
hh3cCfgRunSavedLast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgRunSavedLast.setStatus('current')
hh3cCfgStartModifiedLast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgStartModifiedLast.setStatus('current')
hh3cCfgLogLimitedEntries = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogLimitedEntries.setStatus('current')
hh3cCfgLogDeletedEntries = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogDeletedEntries.setStatus('current')
hh3cCfgLogWantBackup = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgLogWantBackup.setStatus('current')
hh3cCfgLogTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7), )
if mibBuilder.loadTexts: hh3cCfgLogTable.setStatus('current')
hh3cCfgLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1), ).setIndexNames((0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgLogIndex"))
if mibBuilder.loadTexts: hh3cCfgLogEntry.setStatus('current')
hh3cCfgLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cCfgLogIndex.setStatus('current')
hh3cCfgLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogTime.setStatus('current')
hh3cCfgLogSrcCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cmdLine", 1), ("snmp", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogSrcCmd.setStatus('current')
hh3cCfgLogSrcData = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("erase", 1), ("runningData", 2), ("commandSource", 3), ("startupData", 4), ("local", 5), ("netFtp", 6), ("hotPlugging", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogSrcData.setStatus('current')
hh3cCfgLogDesData = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("runningData", 2), ("commandSource", 3), ("startupData", 4), ("local", 5), ("netFtp", 6), ("hotPlugging", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogDesData.setStatus('current')
hh3cCfgLogTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("console", 3), ("terminal", 4), ("virtual", 5), ("auxiliary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogTerminalType.setStatus('current')
hh3cCfgLogTerminalUser = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogTerminalUser.setStatus('current')
hh3cCfgLogTerminalNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogTerminalNum.setStatus('current')
hh3cCfgLogTerminalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogTerminalLocation.setStatus('current')
hh3cCfgLogCmdSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogCmdSrcAddress.setStatus('deprecated')
hh3cCfgLogVirHost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogVirHost.setStatus('current')
hh3cCfgLogUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogUserName.setStatus('current')
hh3cCfgLogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogServerAddress.setStatus('deprecated')
hh3cCfgLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogFile.setStatus('current')
hh3cCfgLogCmdSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 15), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogCmdSrcAddrType.setStatus('current')
hh3cCfgLogCmdSrcAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 16), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogCmdSrcAddrRev.setStatus('current')
hh3cCfgLogCmdSrcAddrVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogCmdSrcAddrVPNName.setStatus('current')
hh3cCfgLogServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 18), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogServerAddrType.setStatus('current')
hh3cCfgLogServerAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 19), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogServerAddrRev.setStatus('current')
hh3cCfgLogServerAddrVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgLogServerAddrVPNName.setStatus('current')
hh3cCfgFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 8), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cCfgFirstTrapTime.setStatus('current')
hh3cCfgOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2))
hh3cCfgOperateGlobalEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateGlobalEntryLimit.setStatus('current')
hh3cCfgOperateEntryAgeOutTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgOperateEntryAgeOutTime.setStatus('current')
hh3cCfgOperateResultGlobalEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgOperateResultGlobalEntryLimit.setStatus('current')
hh3cCfgOperateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4), )
if mibBuilder.loadTexts: hh3cCfgOperateTable.setStatus('current')
hh3cCfgOperateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1), ).setIndexNames((0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateIndex"))
if mibBuilder.loadTexts: hh3cCfgOperateEntry.setStatus('current')
hh3cCfgOperateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cCfgOperateIndex.setStatus('current')
hh3cCfgOperateType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 2), ConfigOperationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateType.setStatus('current')
hh3cCfgOperateProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ftp", 1), ("tftp", 2), ("clusterftp", 3), ("clustertftp", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateProtocol.setStatus('current')
hh3cCfgOperateFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateFileName.setStatus('current')
hh3cCfgOperateServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateServerAddress.setStatus('deprecated')
hh3cCfgOperateUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateUserName.setStatus('current')
hh3cCfgOperateUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateUserPassword.setStatus('current')
hh3cCfgOperateEndNotificationSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateEndNotificationSwitch.setStatus('current')
hh3cCfgOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateRowStatus.setStatus('current')
hh3cCfgOperateServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateServerPort.setStatus('current')
hh3cCfgOperateSrvAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 11), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateSrvAddrType.setStatus('current')
hh3cCfgOperateSrvAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateSrvAddrRev.setStatus('current')
hh3cCfgOperateSrvVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 13), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCfgOperateSrvVPNName.setStatus('current')
hh3cCfgOperateResultTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5), )
if mibBuilder.loadTexts: hh3cCfgOperateResultTable.setStatus('current')
hh3cCfgOperateResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1), ).setIndexNames((0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultIndex"))
if mibBuilder.loadTexts: hh3cCfgOperateResultEntry.setStatus('current')
hh3cCfgOperateResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cCfgOperateResultIndex.setStatus('current')
hh3cCfgOperateResultOptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateResultOptIndex.setStatus('current')
hh3cCfgOperateResultOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 3), ConfigOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateResultOpType.setStatus('current')
hh3cCfgOperateState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 4), ConfigOperationStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateState.setStatus('current')
hh3cCfgOperateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateTime.setStatus('current')
hh3cCfgOperateEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperateEndTime.setStatus('current')
hh3cCfgOperFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgOperFailReason.setStatus('current')
hh3cCfgExecuteOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6))
hh3cCfgExecuteOperateResultEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 20)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgExecuteOperateResultEntryLimit.setStatus('current')
hh3cCfgExecuteResultTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2), )
if mibBuilder.loadTexts: hh3cCfgExecuteResultTable.setStatus('current')
hh3cCfgExecuteResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1), ).setIndexNames((0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgExecuteResultIndex"))
if mibBuilder.loadTexts: hh3cCfgExecuteResultEntry.setStatus('current')
hh3cCfgExecuteResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cCfgExecuteResultIndex.setStatus('current')
hh3cCfgExecuteResultOptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgExecuteResultOptIndex.setStatus('current')
hh3cCfgExecuteResultOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 3), ConfigOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgExecuteResultOpType.setStatus('current')
hh3cCfgExecuteState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 4), ConfigOperationStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgExecuteState.setStatus('current')
hh3cCfgExecuteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgExecuteTime.setStatus('current')
hh3cCfgExecuteEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCfgExecuteEndTime.setStatus('current')
hh3cCfgReset = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgReset.setStatus('current')
hh3cCfgReset2 = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfgReset2.setStatus('current')
hh3cConfigManNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 2))
hh3cCfgManEventlog = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 1)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcCmd"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcData"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDesData"))
if mibBuilder.loadTexts: hh3cCfgManEventlog.setStatus('current')
hh3cCfgOperateCompletion = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 2)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateState"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperFailReason"))
if mibBuilder.loadTexts: hh3cCfgOperateCompletion.setStatus('current')
hh3cCfgInvalidConfigFile = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 3)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateFileName"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgFirstTrapTime"))
if mibBuilder.loadTexts: hh3cCfgInvalidConfigFile.setStatus('current')
hh3cConfigManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3))
hh3cConfigManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 1))
hh3cConfigManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 1, 1)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgManLogGroup"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateGroup"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgManNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cConfigManCompliance = hh3cConfigManCompliance.setStatus('current')
hh3cConfigManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2))
hh3cCfgManLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 1)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgRunModifiedLast"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgRunSavedLast"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgStartModifiedLast"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogLimitedEntries"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDeletedEntries"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcCmd"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalType"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalNum"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalUser"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalLocation"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogCmdSrcAddress"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogVirHost"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogServerAddress"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogFile"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogUserName"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogWantBackup"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcData"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDesData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cCfgManLogGroup = hh3cCfgManLogGroup.setStatus('current')
hh3cCfgOperateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 2)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateGlobalEntryLimit"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEntryAgeOutTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateProtocol"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateFileName"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateServerAddress"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateUserName"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateUserPassword"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndNotificationSwitch"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultGlobalEntryLimit"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateState"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateRowStatus"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultOptIndex"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultOpType"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndTime"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperFailReason"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateServerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cCfgOperateGroup = hh3cCfgOperateGroup.setStatus('current')
hh3cCfgManNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 3)).setObjects(("HH3C-CONFIG-MAN-MIB", "hh3cCfgManEventlog"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateCompletion"), ("HH3C-CONFIG-MAN-MIB", "hh3cCfgInvalidConfigFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cCfgManNotificationGroup = hh3cCfgManNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-CONFIG-MAN-MIB", hh3cCfgExecuteResultOptIndex=hh3cCfgExecuteResultOptIndex, hh3cCfgLogEntry=hh3cCfgLogEntry, hh3cCfgLogWantBackup=hh3cCfgLogWantBackup, hh3cCfgOperateResultGlobalEntryLimit=hh3cCfgOperateResultGlobalEntryLimit, hh3cCfgExecuteResultOpType=hh3cCfgExecuteResultOpType, hh3cCfgOperateGroup=hh3cCfgOperateGroup, hh3cCfgLogTerminalLocation=hh3cCfgLogTerminalLocation, hh3cConfigManGroups=hh3cConfigManGroups, hh3cCfgFirstTrapTime=hh3cCfgFirstTrapTime, hh3cConfigManCompliances=hh3cConfigManCompliances, hh3cCfgExecuteOperate=hh3cCfgExecuteOperate, hh3cCfgLogCmdSrcAddrVPNName=hh3cCfgLogCmdSrcAddrVPNName, hh3cConfigManCompliance=hh3cConfigManCompliance, hh3cCfgOperateSrvAddrRev=hh3cCfgOperateSrvAddrRev, hh3cCfgLogSrcCmd=hh3cCfgLogSrcCmd, hh3cCfgStartModifiedLast=hh3cCfgStartModifiedLast, hh3cConfigManNotifications=hh3cConfigManNotifications, hh3cCfgOperateState=hh3cCfgOperateState, hh3cCfgOperateResultIndex=hh3cCfgOperateResultIndex, hh3cCfgOperateResultOptIndex=hh3cCfgOperateResultOptIndex, ConfigOperationType=ConfigOperationType, hh3cCfgLog=hh3cCfgLog, hh3cCfgLogServerAddrRev=hh3cCfgLogServerAddrRev, hh3cCfgExecuteState=hh3cCfgExecuteState, hh3cCfgOperateResultOpType=hh3cCfgOperateResultOpType, hh3cConfigManObjects=hh3cConfigManObjects, hh3cConfig=hh3cConfig, hh3cCfgReset=hh3cCfgReset, hh3cCfgExecuteOperateResultEntryLimit=hh3cCfgExecuteOperateResultEntryLimit, hh3cCfgOperateGlobalEntryLimit=hh3cCfgOperateGlobalEntryLimit, hh3cCfgOperateTable=hh3cCfgOperateTable, hh3cCfgOperateServerAddress=hh3cCfgOperateServerAddress, hh3cCfgOperateResultEntry=hh3cCfgOperateResultEntry, hh3cCfgOperateEndNotificationSwitch=hh3cCfgOperateEndNotificationSwitch, hh3cCfgOperateServerPort=hh3cCfgOperateServerPort, hh3cCfgOperateEntry=hh3cCfgOperateEntry, hh3cCfgOperate=hh3cCfgOperate, hh3cCfgOperFailReason=hh3cCfgOperFailReason, hh3cCfgLogDesData=hh3cCfgLogDesData, PYSNMP_MODULE_ID=hh3cConfig, hh3cCfgExecuteResultEntry=hh3cCfgExecuteResultEntry, hh3cCfgOperateResultTable=hh3cCfgOperateResultTable, hh3cCfgOperateSrvAddrType=hh3cCfgOperateSrvAddrType, hh3cCfgManLogGroup=hh3cCfgManLogGroup, hh3cCfgOperateEntryAgeOutTime=hh3cCfgOperateEntryAgeOutTime, hh3cCfgLogTerminalNum=hh3cCfgLogTerminalNum, hh3cCfgOperateUserName=hh3cCfgOperateUserName, hh3cCfgManNotificationGroup=hh3cCfgManNotificationGroup, hh3cCfgExecuteResultIndex=hh3cCfgExecuteResultIndex, hh3cCfgExecuteResultTable=hh3cCfgExecuteResultTable, hh3cCfgExecuteTime=hh3cCfgExecuteTime, hh3cCfgInvalidConfigFile=hh3cCfgInvalidConfigFile, hh3cCfgLogServerAddress=hh3cCfgLogServerAddress, hh3cCfgOperateProtocol=hh3cCfgOperateProtocol, hh3cCfgOperateType=hh3cCfgOperateType, hh3cCfgLogSrcData=hh3cCfgLogSrcData, hh3cCfgRunModifiedLast=hh3cCfgRunModifiedLast, hh3cCfgOperateTime=hh3cCfgOperateTime, hh3cCfgLogLimitedEntries=hh3cCfgLogLimitedEntries, hh3cConfigManConformance=hh3cConfigManConformance, hh3cCfgLogTerminalUser=hh3cCfgLogTerminalUser, hh3cCfgLogTime=hh3cCfgLogTime, hh3cCfgLogDeletedEntries=hh3cCfgLogDeletedEntries, hh3cCfgLogCmdSrcAddrType=hh3cCfgLogCmdSrcAddrType, hh3cCfgLogServerAddrVPNName=hh3cCfgLogServerAddrVPNName, hh3cCfgOperateUserPassword=hh3cCfgOperateUserPassword, hh3cCfgLogFile=hh3cCfgLogFile, hh3cCfgOperateSrvVPNName=hh3cCfgOperateSrvVPNName, hh3cCfgLogTable=hh3cCfgLogTable, hh3cCfgLogCmdSrcAddrRev=hh3cCfgLogCmdSrcAddrRev, hh3cCfgRunSavedLast=hh3cCfgRunSavedLast, hh3cCfgLogIndex=hh3cCfgLogIndex, hh3cCfgOperateFileName=hh3cCfgOperateFileName, hh3cCfgReset2=hh3cCfgReset2, ConfigOperationStateType=ConfigOperationStateType, hh3cCfgLogServerAddrType=hh3cCfgLogServerAddrType, hh3cCfgLogUserName=hh3cCfgLogUserName, hh3cCfgManEventlog=hh3cCfgManEventlog, hh3cCfgLogCmdSrcAddress=hh3cCfgLogCmdSrcAddress, hh3cCfgLogTerminalType=hh3cCfgLogTerminalType, hh3cCfgOperateEndTime=hh3cCfgOperateEndTime, hh3cCfgOperateIndex=hh3cCfgOperateIndex, hh3cCfgOperateRowStatus=hh3cCfgOperateRowStatus, hh3cCfgExecuteEndTime=hh3cCfgExecuteEndTime, hh3cCfgOperateCompletion=hh3cCfgOperateCompletion, hh3cCfgLogVirHost=hh3cCfgLogVirHost)

#
# PySNMP MIB module HH3C-FLASH-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FLASH-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Gauge32, TimeTicks, IpAddress, ModuleIdentity, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "ModuleIdentity", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter32", "ObjectIdentity")
TimeStamp, TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hh3cFlash = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 5))
if mibBuilder.loadTexts: hh3cFlash.setLastUpdated('201006050000Z')
if mibBuilder.loadTexts: hh3cFlash.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cFlashOperationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opInvalid", 3), ("opInvalidProtocol", 4), ("opInvalidSourceName", 5), ("opInvalidDestName", 6), ("opInvalidServerAddress", 7), ("opDeviceBusy", 8), ("opDeviceOpenError", 9), ("opDeviceError", 10), ("opDeviceNotProgrammable", 11), ("opDeviceFull", 12), ("opFileOpenError", 13), ("opFileTransferError", 14), ("opFileChecksumError", 15), ("opNoMemory", 16), ("opAuthFail", 17), ("opTimeout", 18), ("opUnknownFailure", 19), ("opDeleteFileOpenError", 20), ("opDeleteInvalidDevice", 21), ("opDeleteInvalidFunction", 22), ("opDeleteOperationError", 23), ("opDeleteInvalidFileName", 24), ("opDeleteDeviceBusy", 25), ("opDeleteParaError", 26), ("opDeleteInvalidPath", 27))

class Hh3cFlashPartitionUpgradeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("rxbootFLH", 2), ("direct", 3))

class Hh3cFlashPartitionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("readOnly", 1), ("runFromFlash", 2), ("readWrite", 3))

hh3cFlashManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1))
hh3cFlashDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1))
hh3cFlhSupportNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhSupportNum.setStatus('current')
hh3cFlashTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cFlashTable.setStatus('current')
hh3cFlashEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1), ).setIndexNames((0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"))
if mibBuilder.loadTexts: hh3cFlashEntry.setStatus('current')
hh3cFlhIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhIndex.setStatus('current')
hh3cFlhSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 2), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhSize.setStatus('current')
hh3cFlhPos = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPos.setStatus('current')
hh3cFlhName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhName.setStatus('current')
hh3cFlhChipNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipNum.setStatus('current')
hh3cFlhDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhDescr.setStatus('current')
hh3cFlhInitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhInitTime.setStatus('current')
hh3cFlhRemovable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhRemovable.setStatus('current')
hh3cFlhPartitionBool = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFlhPartitionBool.setStatus('current')
hh3cFlhMinPartitionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 12), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhMinPartitionSize.setStatus('current')
hh3cFlhMaxPartitions = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhMaxPartitions.setStatus('current')
hh3cFlhPartitionNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartitionNum.setStatus('current')
hh3cFlhKbyteSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 2, 1, 15), Integer32()).setUnits('kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhKbyteSize.setStatus('current')
hh3cFlashChips = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3))
hh3cFlhChipTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1), )
if mibBuilder.loadTexts: hh3cFlhChipTable.setStatus('current')
hh3cFlhChipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1), ).setIndexNames((0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"), (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhChipSerialNo"))
if mibBuilder.loadTexts: hh3cFlhChipEntry.setStatus('current')
hh3cFlhChipSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cFlhChipSerialNo.setStatus('current')
hh3cFlhChipID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipID.setStatus('current')
hh3cFlhChipDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipDescr.setStatus('current')
hh3cFlhChipWriteTimesLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipWriteTimesLimit.setStatus('current')
hh3cFlhChipWriteTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipWriteTimes.setStatus('current')
hh3cFlhChipEraseTimesLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipEraseTimesLimit.setStatus('current')
hh3cFlhChipEraseTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhChipEraseTimes.setStatus('current')
hh3cFlashPartitions = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4))
hh3cFlhPartitionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1), )
if mibBuilder.loadTexts: hh3cFlhPartitionTable.setStatus('current')
hh3cFlhPartitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1), ).setIndexNames((0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"), (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhPartIndex"))
if mibBuilder.loadTexts: hh3cFlhPartitionEntry.setStatus('current')
hh3cFlhPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: hh3cFlhPartIndex.setStatus('current')
hh3cFlhPartFirstChip = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartFirstChip.setStatus('current')
hh3cFlhPartLastChip = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartLastChip.setStatus('current')
hh3cFlhPartSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 4), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartSpace.setStatus('current')
hh3cFlhPartSpaceFree = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartSpaceFree.setStatus('current')
hh3cFlhPartFileNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartFileNum.setStatus('current')
hh3cFlhPartChecksumMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("simpleChecksum", 1), ("undefined", 2), ("simpleCRC", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartChecksumMethod.setStatus('current')
hh3cFlhPartStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 8), Hh3cFlashPartitionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartStatus.setStatus('current')
hh3cFlhPartUpgradeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 9), Hh3cFlashPartitionUpgradeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartUpgradeMode.setStatus('current')
hh3cFlhPartName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartName.setStatus('current')
hh3cFlhPartRequireErase = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartRequireErase.setStatus('current')
hh3cFlhPartFileNameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhPartFileNameLen.setStatus('current')
hh3cFlhFiles = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2))
hh3cFlhFileTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1), )
if mibBuilder.loadTexts: hh3cFlhFileTable.setStatus('current')
hh3cFlhFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1), ).setIndexNames((0, "HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"), (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhPartIndex"), (0, "HH3C-FLASH-MAN-MIB", "hh3cFlhFileIndex"))
if mibBuilder.loadTexts: hh3cFlhFileEntry.setStatus('current')
hh3cFlhFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cFlhFileIndex.setStatus('current')
hh3cFlhFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhFileName.setStatus('current')
hh3cFlhFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhFileSize.setStatus('current')
hh3cFlhFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("deleted", 1), ("invalidChecksum", 2), ("valid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhFileStatus.setStatus('current')
hh3cFlhFileChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 1, 4, 2, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhFileChecksum.setStatus('current')
hh3cFlashOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2))
hh3cFlhOpTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cFlhOpTable.setStatus('current')
hh3cFlhOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-FLASH-MAN-MIB", "hh3cFlhOperIndex"))
if mibBuilder.loadTexts: hh3cFlhOpEntry.setStatus('current')
hh3cFlhOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cFlhOperIndex.setStatus('current')
hh3cFlhOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("net2FlashWithErase", 1), ("net2FlashWithoutErase", 2), ("flash2Net", 3), ("delete", 4), ("rename", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperType.setStatus('current')
hh3cFlhOperProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ftp", 1), ("tftp", 2), ("clusterftp", 3), ("clustertftp", 4))).clone('ftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperProtocol.setStatus('current')
hh3cFlhOperServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 4), IpAddress().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperServerAddress.setStatus('current')
hh3cFlhOperServerUser = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperServerUser.setStatus('current')
hh3cFlhOperPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperPassword.setStatus('current')
hh3cFlhOperSourceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperSourceFile.setStatus('current')
hh3cFlhOperDestinationFile = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperDestinationFile.setStatus('current')
hh3cFlhOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 9), Hh3cFlashOperationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhOperStatus.setStatus('current')
hh3cFlhOperEndNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperEndNotification.setStatus('current')
hh3cFlhOperProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhOperProgress.setStatus('current')
hh3cFlhOperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperRowStatus.setStatus('current')
hh3cFlhOperServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFlhOperServerPort.setStatus('current')
hh3cFlhOperFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 2, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhOperFailReason.setStatus('current')
hh3cFlashNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 3))
hh3cFlhOperNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 5, 1, 3, 1)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhOperStatus"))
if mibBuilder.loadTexts: hh3cFlhOperNotification.setStatus('current')
hh3cFlashMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2))
hh3cFlhMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 1))
hh3cFlhMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 1, 1)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhGroup"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartitionGroup"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileGroup"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperationGroup"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhNotificationGroup"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhMIBCompliance = hh3cFlhMIBCompliance.setStatus('current')
hh3cFlashMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2))
hh3cFlhGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 1)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhSupportNum"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhSize"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPos"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhName"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipNum"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhDescr"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhInitTime"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhRemovable"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartitionBool"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhMinPartitionSize"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhMaxPartitions"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartitionNum"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhIndex"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhKbyteSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhGroup = hh3cFlhGroup.setStatus('current')
hh3cFlhChipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 3)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhChipID"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipDescr"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipWriteTimesLimit"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipWriteTimes"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipEraseTimesLimit"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhChipEraseTimes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhChipGroup = hh3cFlhChipGroup.setStatus('current')
hh3cFlhPartitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 4)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFirstChip"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartLastChip"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartSpace"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartSpaceFree"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFileNum"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartChecksumMethod"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartStatus"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartUpgradeMode"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartName"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartRequireErase"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhPartFileNameLen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhPartitionGroup = hh3cFlhPartitionGroup.setStatus('current')
hh3cFlhFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 5)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhFileName"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileSize"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileStatus"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhFileChecksum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhFileGroup = hh3cFlhFileGroup.setStatus('current')
hh3cFlhOperationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 6)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhOperType"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperProtocol"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerAddress"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerUser"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperPassword"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperSourceFile"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperDestinationFile"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperStatus"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperEndNotification"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperProgress"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperRowStatus"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperServerPort"), ("HH3C-FLASH-MAN-MIB", "hh3cFlhOperFailReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhOperationGroup = hh3cFlhOperationGroup.setStatus('current')
hh3cFlhNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25506, 2, 5, 2, 2, 7)).setObjects(("HH3C-FLASH-MAN-MIB", "hh3cFlhOperNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cFlhNotificationGroup = hh3cFlhNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-FLASH-MAN-MIB", hh3cFlhFileStatus=hh3cFlhFileStatus, hh3cFlashDevice=hh3cFlashDevice, hh3cFlhOperServerPort=hh3cFlhOperServerPort, hh3cFlashManMIBObjects=hh3cFlashManMIBObjects, hh3cFlhChipEraseTimes=hh3cFlhChipEraseTimes, hh3cFlhFileName=hh3cFlhFileName, hh3cFlhFileChecksum=hh3cFlhFileChecksum, hh3cFlhOperNotification=hh3cFlhOperNotification, hh3cFlhIndex=hh3cFlhIndex, hh3cFlhChipNum=hh3cFlhChipNum, hh3cFlashNotification=hh3cFlashNotification, Hh3cFlashPartitionStatus=Hh3cFlashPartitionStatus, hh3cFlhChipWriteTimesLimit=hh3cFlhChipWriteTimesLimit, hh3cFlhChipDescr=hh3cFlhChipDescr, hh3cFlhPartitionTable=hh3cFlhPartitionTable, hh3cFlhOperEndNotification=hh3cFlhOperEndNotification, hh3cFlhChipEraseTimesLimit=hh3cFlhChipEraseTimesLimit, hh3cFlhChipWriteTimes=hh3cFlhChipWriteTimes, hh3cFlhPos=hh3cFlhPos, hh3cFlhName=hh3cFlhName, hh3cFlhSupportNum=hh3cFlhSupportNum, hh3cFlhChipSerialNo=hh3cFlhChipSerialNo, hh3cFlhPartFirstChip=hh3cFlhPartFirstChip, hh3cFlhPartitionGroup=hh3cFlhPartitionGroup, hh3cFlhSize=hh3cFlhSize, hh3cFlashEntry=hh3cFlashEntry, hh3cFlashOperate=hh3cFlashOperate, hh3cFlhChipGroup=hh3cFlhChipGroup, hh3cFlashChips=hh3cFlashChips, hh3cFlhDescr=hh3cFlhDescr, hh3cFlhOperFailReason=hh3cFlhOperFailReason, hh3cFlhPartChecksumMethod=hh3cFlhPartChecksumMethod, hh3cFlhOperProtocol=hh3cFlhOperProtocol, hh3cFlhGroup=hh3cFlhGroup, hh3cFlhMaxPartitions=hh3cFlhMaxPartitions, hh3cFlhPartitionNum=hh3cFlhPartitionNum, hh3cFlhNotificationGroup=hh3cFlhNotificationGroup, hh3cFlhChipID=hh3cFlhChipID, hh3cFlhFileEntry=hh3cFlhFileEntry, hh3cFlhPartitionBool=hh3cFlhPartitionBool, hh3cFlash=hh3cFlash, hh3cFlhFileIndex=hh3cFlhFileIndex, hh3cFlhPartFileNameLen=hh3cFlhPartFileNameLen, hh3cFlhInitTime=hh3cFlhInitTime, hh3cFlhOpTable=hh3cFlhOpTable, hh3cFlhOperServerUser=hh3cFlhOperServerUser, hh3cFlhPartUpgradeMode=hh3cFlhPartUpgradeMode, hh3cFlashPartitions=hh3cFlashPartitions, hh3cFlhFileGroup=hh3cFlhFileGroup, hh3cFlhOperType=hh3cFlhOperType, hh3cFlhRemovable=hh3cFlhRemovable, hh3cFlhOperRowStatus=hh3cFlhOperRowStatus, hh3cFlhPartSpace=hh3cFlhPartSpace, hh3cFlhChipTable=hh3cFlhChipTable, Hh3cFlashOperationStatus=Hh3cFlashOperationStatus, hh3cFlhPartName=hh3cFlhPartName, hh3cFlhFileSize=hh3cFlhFileSize, hh3cFlhFileTable=hh3cFlhFileTable, hh3cFlashTable=hh3cFlashTable, hh3cFlhMIBCompliances=hh3cFlhMIBCompliances, hh3cFlhPartFileNum=hh3cFlhPartFileNum, hh3cFlhMIBCompliance=hh3cFlhMIBCompliance, hh3cFlhPartitionEntry=hh3cFlhPartitionEntry, hh3cFlhFiles=hh3cFlhFiles, hh3cFlhPartSpaceFree=hh3cFlhPartSpaceFree, PYSNMP_MODULE_ID=hh3cFlash, hh3cFlhPartRequireErase=hh3cFlhPartRequireErase, hh3cFlhOperSourceFile=hh3cFlhOperSourceFile, hh3cFlashMIBConformance=hh3cFlashMIBConformance, hh3cFlhOperIndex=hh3cFlhOperIndex, hh3cFlhChipEntry=hh3cFlhChipEntry, hh3cFlhKbyteSize=hh3cFlhKbyteSize, hh3cFlhMinPartitionSize=hh3cFlhMinPartitionSize, hh3cFlhOperStatus=hh3cFlhOperStatus, hh3cFlhOperPassword=hh3cFlhOperPassword, hh3cFlhOperServerAddress=hh3cFlhOperServerAddress, hh3cFlhOperProgress=hh3cFlhOperProgress, hh3cFlhOpEntry=hh3cFlhOpEntry, hh3cFlhPartLastChip=hh3cFlhPartLastChip, hh3cFlashMIBGroups=hh3cFlashMIBGroups, hh3cFlhOperDestinationFile=hh3cFlhOperDestinationFile, hh3cFlhOperationGroup=hh3cFlhOperationGroup, Hh3cFlashPartitionUpgradeMode=Hh3cFlashPartitionUpgradeMode, hh3cFlhPartStatus=hh3cFlhPartStatus, hh3cFlhPartIndex=hh3cFlhPartIndex)
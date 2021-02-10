#
# PySNMP MIB module Dell-File (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-File
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, NotificationType, IpAddress, ObjectIdentity, Unsigned32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "NotificationType", "IpAddress", "ObjectIdentity", "Unsigned32", "iso", "Bits")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
rlFile = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 96))
rlFile.setRevisions(('2013-04-01 00:00',))
if mibBuilder.loadTexts: rlFile.setLastUpdated('201304010000Z')
if mibBuilder.loadTexts: rlFile.setOrganization('Dell')
rlFileMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileMibVersion.setStatus('current')
rlFileTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 2), )
if mibBuilder.loadTexts: rlFileTable.setStatus('current')
rlFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 2, 1), ).setIndexNames((1, "Dell-File", "rlFileName"))
if mibBuilder.loadTexts: rlFileEntry.setStatus('current')
rlFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileName.setStatus('current')
rlFilePermission = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("readWrite", 3), ("noReadNoWrite", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFilePermission.setStatus('current')
rlFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileSize.setStatus('current')
rlFileModificationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationDate.setStatus('current')
rlFileModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationTime.setStatus('current')
rlFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileRowStatus.setStatus('current')
rlFileFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFlashSize.setStatus('current')
rlFileFullNormalizedName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFullNormalizedName.setStatus('current')
rlFileActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 3), )
if mibBuilder.loadTexts: rlFileActionTable.setStatus('current')
rlFileActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 3, 1), ).setIndexNames((0, "Dell-File", "rlFileActionName"))
if mibBuilder.loadTexts: rlFileActionEntry.setStatus('current')
rlFileActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionName.setStatus('current')
rlFileActionNewName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionNewName.setStatus('current')
rlFileActionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionRowStatus.setStatus('current')
rlFileActionCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rename", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionCommand.setStatus('current')
rlFileTotalSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileTotalSizeOfFlash.setStatus('current')
rlFileFreeSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFreeSizeOfFlash.setStatus('current')
rlFileAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileAuditingEnable.setStatus('current')
mibBuilder.exportSymbols("Dell-File", rlFileFullNormalizedName=rlFileFullNormalizedName, PYSNMP_MODULE_ID=rlFile, rlFileActionRowStatus=rlFileActionRowStatus, rlFileTotalSizeOfFlash=rlFileTotalSizeOfFlash, rlFile=rlFile, rlFileFreeSizeOfFlash=rlFileFreeSizeOfFlash, rlFileActionEntry=rlFileActionEntry, rlFileModificationDate=rlFileModificationDate, rlFileActionTable=rlFileActionTable, rlFileModificationTime=rlFileModificationTime, rlFileTable=rlFileTable, rlFileName=rlFileName, rlFileRowStatus=rlFileRowStatus, rlFileSize=rlFileSize, rlFilePermission=rlFilePermission, rlFileActionName=rlFileActionName, rlFileEntry=rlFileEntry, rlFileFlashSize=rlFileFlashSize, rlFileActionNewName=rlFileActionNewName, rlFileMibVersion=rlFileMibVersion, rlFileAuditingEnable=rlFileAuditingEnable, rlFileActionCommand=rlFileActionCommand)

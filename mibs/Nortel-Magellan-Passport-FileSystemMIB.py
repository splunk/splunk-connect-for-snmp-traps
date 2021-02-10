#
# PySNMP MIB module Nortel-Magellan-Passport-FileSystemMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-FileSystemMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:17:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
RowStatus, Integer32, Gauge32, Unsigned32, DisplayString, RowPointer, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "RowStatus", "Integer32", "Gauge32", "Unsigned32", "DisplayString", "RowPointer", "StorageType")
NonReplicated, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "AsciiString")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Gauge32, ModuleIdentity, Unsigned32, iso, ObjectIdentity, Bits, NotificationType, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fileSystemMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16))
fs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15))
fsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1), )
if mibBuilder.loadTexts: fsRowStatusTable.setStatus('mandatory')
fsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"))
if mibBuilder.loadTexts: fsRowStatusEntry.setStatus('mandatory')
fsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsRowStatus.setStatus('mandatory')
fsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsComponentName.setStatus('mandatory')
fsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsStorageType.setStatus('mandatory')
fsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: fsIndex.setStatus('mandatory')
fsStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10), )
if mibBuilder.loadTexts: fsStateTable.setStatus('mandatory')
fsStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"))
if mibBuilder.loadTexts: fsStateEntry.setStatus('mandatory')
fsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsAdminState.setStatus('mandatory')
fsOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsOperationalState.setStatus('mandatory')
fsUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsUsageState.setStatus('mandatory')
fsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11), )
if mibBuilder.loadTexts: fsOperTable.setStatus('mandatory')
fsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"))
if mibBuilder.loadTexts: fsOperEntry.setStatus('mandatory')
fsVolumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsVolumeName.setStatus('mandatory')
fsActiveDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsActiveDisk.setStatus('mandatory')
fsSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("synchronized", 0), ("unSynchronized", 1), ("synchronizing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsSyncStatus.setStatus('mandatory')
fsSyncProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsSyncProgress.setStatus('mandatory')
fsCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsCapacity.setStatus('mandatory')
fsFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsFreeSpace.setStatus('mandatory')
fsUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsUsage.setStatus('mandatory')
fsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2))
fsDiskRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1), )
if mibBuilder.loadTexts: fsDiskRowStatusTable.setStatus('mandatory')
fsDiskRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"))
if mibBuilder.loadTexts: fsDiskRowStatusEntry.setStatus('mandatory')
fsDiskRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskRowStatus.setStatus('mandatory')
fsDiskComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskComponentName.setStatus('mandatory')
fsDiskStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskStorageType.setStatus('mandatory')
fsDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: fsDiskIndex.setStatus('mandatory')
fsDiskStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10), )
if mibBuilder.loadTexts: fsDiskStateTable.setStatus('mandatory')
fsDiskStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"))
if mibBuilder.loadTexts: fsDiskStateEntry.setStatus('mandatory')
fsDiskAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskAdminState.setStatus('mandatory')
fsDiskOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskOperationalState.setStatus('mandatory')
fsDiskUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskUsageState.setStatus('mandatory')
fsDiskOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11), )
if mibBuilder.loadTexts: fsDiskOperTable.setStatus('mandatory')
fsDiskOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"))
if mibBuilder.loadTexts: fsDiskOperEntry.setStatus('mandatory')
fsDiskVolumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDiskVolumeName.setStatus('mandatory')
fsDiskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskCapacity.setStatus('mandatory')
fsDiskFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskFreeSpace.setStatus('mandatory')
fsDiskBadBlocksPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskBadBlocksPercentage.setStatus('mandatory')
fsDiskUnformattedCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskUnformattedCapacity.setStatus('mandatory')
fsDiskTest = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2))
fsDiskTestRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1), )
if mibBuilder.loadTexts: fsDiskTestRowStatusTable.setStatus('mandatory')
fsDiskTestRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"))
if mibBuilder.loadTexts: fsDiskTestRowStatusEntry.setStatus('mandatory')
fsDiskTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestRowStatus.setStatus('mandatory')
fsDiskTestComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestComponentName.setStatus('mandatory')
fsDiskTestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestStorageType.setStatus('mandatory')
fsDiskTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: fsDiskTestIndex.setStatus('mandatory')
fsDiskTestStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10), )
if mibBuilder.loadTexts: fsDiskTestStateTable.setStatus('mandatory')
fsDiskTestStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"))
if mibBuilder.loadTexts: fsDiskTestStateEntry.setStatus('mandatory')
fsDiskTestAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestAdminState.setStatus('mandatory')
fsDiskTestOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestOperationalState.setStatus('mandatory')
fsDiskTestUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestUsageState.setStatus('mandatory')
fsDiskTestSetupTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11), )
if mibBuilder.loadTexts: fsDiskTestSetupTable.setStatus('mandatory')
fsDiskTestSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"))
if mibBuilder.loadTexts: fsDiskTestSetupEntry.setStatus('mandatory')
fsDiskTestTestCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDiskTestTestCount.setStatus('mandatory')
fsDiskTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 35791394)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDiskTestDuration.setStatus('mandatory')
fsDiskTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("filesystemCheck", 0), ("diskRead", 1), ("flakyBitDetection", 2), ("surfaceAnalysis", 3))).clone('filesystemCheck')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDiskTestType.setStatus('mandatory')
fsDiskTestResultsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12), )
if mibBuilder.loadTexts: fsDiskTestResultsTable.setStatus('mandatory')
fsDiskTestResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"), (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"))
if mibBuilder.loadTexts: fsDiskTestResultsEntry.setStatus('mandatory')
fsDiskTestCauseOfTermination = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("testCountReached", 0), ("testTimeExpired", 1), ("stoppedByOperator", 2), ("neverStarted", 3), ("testRunning", 4), ("error", 5), ("internalError", 6), ("unknown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestCauseOfTermination.setStatus('mandatory')
fsDiskTestNatureOfError = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("logical", 0), ("media", 1), ("noErrorDetected", 2), ("failedToComplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestNatureOfError.setStatus('mandatory')
fsDiskTestSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noDataLost", 0), ("dataLost", 1), ("hardwareProblem", 2), ("noError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestSeverity.setStatus('mandatory')
fsDiskTestElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestElapsedTime.setStatus('mandatory')
fsDiskTestTestExecutionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDiskTestTestExecutionCount.setStatus('mandatory')
fileSystemGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1))
fileSystemGroupBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4))
fileSystemGroupBD00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4, 1))
fileSystemGroupBD00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4, 1, 2))
fileSystemCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3))
fileSystemCapabilitiesBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4))
fileSystemCapabilitiesBD00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4, 1))
fileSystemCapabilitiesBD00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-FileSystemMIB", fsDiskTestTestCount=fsDiskTestTestCount, fileSystemGroupBD00A=fileSystemGroupBD00A, fsUsageState=fsUsageState, fsDiskTestIndex=fsDiskTestIndex, fsStateEntry=fsStateEntry, fs=fs, fsOperEntry=fsOperEntry, fsDiskRowStatusTable=fsDiskRowStatusTable, fsDiskUsageState=fsDiskUsageState, fsDiskTestSetupEntry=fsDiskTestSetupEntry, fsActiveDisk=fsActiveDisk, fsOperTable=fsOperTable, fsDiskTestStateEntry=fsDiskTestStateEntry, fsDiskTestOperationalState=fsDiskTestOperationalState, fsOperationalState=fsOperationalState, fsDiskTestDuration=fsDiskTestDuration, fsDiskTestCauseOfTermination=fsDiskTestCauseOfTermination, fsDiskUnformattedCapacity=fsDiskUnformattedCapacity, fsRowStatusEntry=fsRowStatusEntry, fsDiskTestNatureOfError=fsDiskTestNatureOfError, fsDiskRowStatusEntry=fsDiskRowStatusEntry, fsFreeSpace=fsFreeSpace, fsDiskCapacity=fsDiskCapacity, fsComponentName=fsComponentName, fsRowStatusTable=fsRowStatusTable, fsDiskIndex=fsDiskIndex, fsUsage=fsUsage, fsDiskTest=fsDiskTest, fsDiskStateEntry=fsDiskStateEntry, fsDiskFreeSpace=fsDiskFreeSpace, fsDiskTestUsageState=fsDiskTestUsageState, fsDiskTestResultsEntry=fsDiskTestResultsEntry, fsDiskOperationalState=fsDiskOperationalState, fileSystemCapabilitiesBD00A=fileSystemCapabilitiesBD00A, fsSyncProgress=fsSyncProgress, fsCapacity=fsCapacity, fsDiskTestType=fsDiskTestType, fsDiskComponentName=fsDiskComponentName, fsIndex=fsIndex, fsDiskOperTable=fsDiskOperTable, fsDiskTestTestExecutionCount=fsDiskTestTestExecutionCount, fsDiskTestRowStatus=fsDiskTestRowStatus, fsDiskTestRowStatusEntry=fsDiskTestRowStatusEntry, fileSystemMIB=fileSystemMIB, fileSystemCapabilitiesBD=fileSystemCapabilitiesBD, fsDiskTestStateTable=fsDiskTestStateTable, fsDiskTestRowStatusTable=fsDiskTestRowStatusTable, fsDiskAdminState=fsDiskAdminState, fsDiskTestResultsTable=fsDiskTestResultsTable, fileSystemGroup=fileSystemGroup, fsDiskTestComponentName=fsDiskTestComponentName, fileSystemGroupBD00=fileSystemGroupBD00, fileSystemCapabilitiesBD00=fileSystemCapabilitiesBD00, fsDiskRowStatus=fsDiskRowStatus, fsDiskOperEntry=fsDiskOperEntry, fsVolumeName=fsVolumeName, fileSystemCapabilities=fileSystemCapabilities, fileSystemGroupBD=fileSystemGroupBD, fsDiskTestElapsedTime=fsDiskTestElapsedTime, fsStateTable=fsStateTable, fsDiskTestAdminState=fsDiskTestAdminState, fsDiskTestSeverity=fsDiskTestSeverity, fsRowStatus=fsRowStatus, fsStorageType=fsStorageType, fsDiskBadBlocksPercentage=fsDiskBadBlocksPercentage, fsDiskStorageType=fsDiskStorageType, fsDiskTestStorageType=fsDiskTestStorageType, fsDiskVolumeName=fsDiskVolumeName, fsDiskStateTable=fsDiskStateTable, fsSyncStatus=fsSyncStatus, fsAdminState=fsAdminState, fsDisk=fsDisk, fsDiskTestSetupTable=fsDiskTestSetupTable)

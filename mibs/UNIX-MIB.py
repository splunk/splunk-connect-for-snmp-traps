#
# PySNMP MIB module UNIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UNIX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Unsigned32, ObjectIdentity, TimeTicks, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, experimental, IpAddress, Counter32, Bits, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "experimental", "IpAddress", "Counter32", "Bits", "Integer32", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
host = MibIdentifier((1, 3, 6, 1, 3, 999))
machine = MibIdentifier((1, 3, 6, 1, 3, 999, 1))
network = MibIdentifier((1, 3, 6, 1, 3, 999, 2))
processor = MibIdentifier((1, 3, 6, 1, 3, 999, 3))
adapter = MibIdentifier((1, 3, 6, 1, 3, 999, 4))
controller = MibIdentifier((1, 3, 6, 1, 3, 999, 5))
printer = MibIdentifier((1, 3, 6, 1, 3, 999, 6))
disk = MibIdentifier((1, 3, 6, 1, 3, 999, 7))
diskPartition = MibIdentifier((1, 3, 6, 1, 3, 999, 8))
tape = MibIdentifier((1, 3, 6, 1, 3, 999, 9))
queue = MibIdentifier((1, 3, 6, 1, 3, 999, 10))
group = MibIdentifier((1, 3, 6, 1, 3, 999, 11))
user = MibIdentifier((1, 3, 6, 1, 3, 999, 12))
installedsw = MibIdentifier((1, 3, 6, 1, 3, 999, 13))
license = MibIdentifier((1, 3, 6, 1, 3, 999, 14))
filesystem = MibIdentifier((1, 3, 6, 1, 3, 999, 15))
mountinfo = MibIdentifier((1, 3, 6, 1, 3, 999, 16))
machineOsType = MibScalar((1, 3, 6, 1, 3, 999, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineOsType.setStatus('mandatory')
machineName = MibScalar((1, 3, 6, 1, 3, 999, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineName.setStatus('mandatory')
machineTime = MibScalar((1, 3, 6, 1, 3, 999, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineTime.setStatus('mandatory')
machineOsVersion = MibScalar((1, 3, 6, 1, 3, 999, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineOsVersion.setStatus('mandatory')
machineBootRoot = MibScalar((1, 3, 6, 1, 3, 999, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineBootRoot.setStatus('mandatory')
machineBootTime = MibScalar((1, 3, 6, 1, 3, 999, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineBootTime.setStatus('mandatory')
machineHwModel = MibScalar((1, 3, 6, 1, 3, 999, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineHwModel.setStatus('mandatory')
machineHwType = MibScalar((1, 3, 6, 1, 3, 999, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineHwType.setStatus('mandatory')
machineHwVersion = MibScalar((1, 3, 6, 1, 3, 999, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineHwVersion.setStatus('mandatory')
machineVendor = MibScalar((1, 3, 6, 1, 3, 999, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineVendor.setStatus('mandatory')
machineMemorySize = MibScalar((1, 3, 6, 1, 3, 999, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineMemorySize.setStatus('mandatory')
networkTable = MibTable((1, 3, 6, 1, 3, 999, 2), )
if mibBuilder.loadTexts: networkTable.setStatus('mandatory')
networkEntry = MibTableRow((1, 3, 6, 1, 3, 999, 2, 1), ).setIndexNames((0, "UNIX-MIB", "networkIndex"))
if mibBuilder.loadTexts: networkEntry.setStatus('mandatory')
networkIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkIndex.setStatus('mandatory')
networkAddress = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkAddress.setStatus('mandatory')
networkNodeName = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkNodeName.setStatus('mandatory')
networkType = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkType.setStatus('mandatory')
processorTable = MibTable((1, 3, 6, 1, 3, 999, 3), )
if mibBuilder.loadTexts: processorTable.setStatus('mandatory')
processorEntry = MibTableRow((1, 3, 6, 1, 3, 999, 3, 1), ).setIndexNames((0, "UNIX-MIB", "processorIndex"))
if mibBuilder.loadTexts: processorEntry.setStatus('mandatory')
processorIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processorIndex.setStatus('mandatory')
processorActiveState = MibTableColumn((1, 3, 6, 1, 3, 999, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processorActiveState.setStatus('mandatory')
processorPrimary = MibTableColumn((1, 3, 6, 1, 3, 999, 3, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processorPrimary.setStatus('mandatory')
adapterTable = MibTable((1, 3, 6, 1, 3, 999, 4), )
if mibBuilder.loadTexts: adapterTable.setStatus('mandatory')
adapterEntry = MibTableRow((1, 3, 6, 1, 3, 999, 4, 1), ).setIndexNames((0, "UNIX-MIB", "adapterIndex"))
if mibBuilder.loadTexts: adapterEntry.setStatus('mandatory')
adapterIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterIndex.setStatus('mandatory')
adapterName = MibTableColumn((1, 3, 6, 1, 3, 999, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterName.setStatus('mandatory')
adapterType = MibScalar((1, 3, 6, 1, 3, 999, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterType.setStatus('mandatory')
adapterUnitNumber = MibTableColumn((1, 3, 6, 1, 3, 999, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterUnitNumber.setStatus('mandatory')
adapterNexusNumber = MibTableColumn((1, 3, 6, 1, 3, 999, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterNexusNumber.setStatus('mandatory')
adapterRevLevel = MibTableColumn((1, 3, 6, 1, 3, 999, 4, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adapterRevLevel.setStatus('mandatory')
controllerTable = MibTable((1, 3, 6, 1, 3, 999, 5), )
if mibBuilder.loadTexts: controllerTable.setStatus('mandatory')
controllerEntry = MibTableRow((1, 3, 6, 1, 3, 999, 5, 1), ).setIndexNames((0, "UNIX-MIB", "controllerIndex"))
if mibBuilder.loadTexts: controllerEntry.setStatus('mandatory')
controllerIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerIndex.setStatus('mandatory')
controllerName = MibTableColumn((1, 3, 6, 1, 3, 999, 5, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerName.setStatus('mandatory')
controllerType = MibTableColumn((1, 3, 6, 1, 3, 999, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerType.setStatus('mandatory')
controllerUnitNumber = MibTableColumn((1, 3, 6, 1, 3, 999, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerUnitNumber.setStatus('mandatory')
printerTable = MibTable((1, 3, 6, 1, 3, 999, 6), )
if mibBuilder.loadTexts: printerTable.setStatus('mandatory')
printerEntry = MibTableRow((1, 3, 6, 1, 3, 999, 6, 1), ).setIndexNames((0, "UNIX-MIB", "printerIndex"))
if mibBuilder.loadTexts: printerEntry.setStatus('mandatory')
printerIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerIndex.setStatus('mandatory')
printerName = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerName.setStatus('mandatory')
printerQueue = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerQueue.setStatus('mandatory')
printerDeviceDriver = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerDeviceDriver.setStatus('mandatory')
printerDeviceType = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerDeviceType.setStatus('mandatory')
printerUnitNumber = MibTableColumn((1, 3, 6, 1, 3, 999, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerUnitNumber.setStatus('mandatory')
diskTable = MibTable((1, 3, 6, 1, 3, 999, 7), )
if mibBuilder.loadTexts: diskTable.setStatus('mandatory')
diskEntry = MibTableRow((1, 3, 6, 1, 3, 999, 7, 1), ).setIndexNames((0, "UNIX-MIB", "diskIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('mandatory')
diskIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIndex.setStatus('mandatory')
diskDeviceName = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDeviceName.setStatus('mandatory')
diskPrimaryHost = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPrimaryHost.setStatus('mandatory')
diskUnitNumber = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskUnitNumber.setStatus('mandatory')
diskDeviceDriver = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDeviceDriver.setStatus('mandatory')
diskDeviceType = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDeviceType.setStatus('mandatory')
diskPhysicalCapacity = MibTableColumn((1, 3, 6, 1, 3, 999, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPhysicalCapacity.setStatus('mandatory')
diskPartitionTable = MibTable((1, 3, 6, 1, 3, 999, 8), )
if mibBuilder.loadTexts: diskPartitionTable.setStatus('mandatory')
diskPartitionEntry = MibTableRow((1, 3, 6, 1, 3, 999, 8, 1), ).setIndexNames((0, "UNIX-MIB", "diskPartitionIndex"))
if mibBuilder.loadTexts: diskPartitionEntry.setStatus('mandatory')
diskPartitionIndex = MibScalar((1, 3, 6, 1, 3, 999, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionIndex.setStatus('mandatory')
diskPartitionName = MibTableColumn((1, 3, 6, 1, 3, 999, 8, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionName.setStatus('mandatory')
diskPartitionPrimaryHost = MibTableColumn((1, 3, 6, 1, 3, 999, 8, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionPrimaryHost.setStatus('mandatory')
diskPartitionSize = MibScalar((1, 3, 6, 1, 3, 999, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionSize.setStatus('mandatory')
diskPartitionDeviceName = MibScalar((1, 3, 6, 1, 3, 999, 8, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionDeviceName.setStatus('mandatory')
diskPartitionStartSector = MibTableColumn((1, 3, 6, 1, 3, 999, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionStartSector.setStatus('mandatory')
diskPartitionEndSector = MibTableColumn((1, 3, 6, 1, 3, 999, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPartitionEndSector.setStatus('mandatory')
tapeTable = MibTable((1, 3, 6, 1, 3, 999, 9), )
if mibBuilder.loadTexts: tapeTable.setStatus('mandatory')
tapeEntry = MibTableRow((1, 3, 6, 1, 3, 999, 9, 1), ).setIndexNames((0, "UNIX-MIB", "tapeIndex"))
if mibBuilder.loadTexts: tapeEntry.setStatus('mandatory')
tapeIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 9, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeIndex.setStatus('mandatory')
tapeDeviceName = MibTableColumn((1, 3, 6, 1, 3, 999, 9, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeDeviceName.setStatus('mandatory')
tapeTapeUnitNumber = MibScalar((1, 3, 6, 1, 3, 999, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeTapeUnitNumber.setStatus('mandatory')
tapeDeviceDriver = MibTableColumn((1, 3, 6, 1, 3, 999, 9, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeDeviceDriver.setStatus('mandatory')
tapeDeviceType = MibTableColumn((1, 3, 6, 1, 3, 999, 9, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeDeviceType.setStatus('mandatory')
tapeMountPoint = MibTableColumn((1, 3, 6, 1, 3, 999, 9, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tapeMountPoint.setStatus('mandatory')
queueTable = MibTable((1, 3, 6, 1, 3, 999, 10), )
if mibBuilder.loadTexts: queueTable.setStatus('mandatory')
queueEntry = MibTableRow((1, 3, 6, 1, 3, 999, 10, 1), ).setIndexNames((0, "UNIX-MIB", "queueIndex"))
if mibBuilder.loadTexts: queueEntry.setStatus('mandatory')
queueIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueIndex.setStatus('mandatory')
queueName = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueName.setStatus('mandatory')
queueType = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueType.setStatus('mandatory')
queueState = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueState.setStatus('mandatory')
queueDestinationList = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueDestinationList.setStatus('mandatory')
queueCapacity = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueCapacity.setStatus('mandatory')
queuePriority = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queuePriority.setStatus('mandatory')
queueProtection = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueProtection.setStatus('mandatory')
queueUserComment = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueUserComment.setStatus('mandatory')
queuePrintServer = MibTableColumn((1, 3, 6, 1, 3, 999, 10, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queuePrintServer.setStatus('mandatory')
groupTable = MibTable((1, 3, 6, 1, 3, 999, 11), )
if mibBuilder.loadTexts: groupTable.setStatus('mandatory')
groupEntry = MibTableRow((1, 3, 6, 1, 3, 999, 11, 1), ).setIndexNames((0, "UNIX-MIB", "groupIndex"))
if mibBuilder.loadTexts: groupEntry.setStatus('mandatory')
groupIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 11, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupIndex.setStatus('mandatory')
groupId = MibTableColumn((1, 3, 6, 1, 3, 999, 11, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupId.setStatus('mandatory')
groupName = MibTableColumn((1, 3, 6, 1, 3, 999, 11, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupName.setStatus('mandatory')
userTable = MibTable((1, 3, 6, 1, 3, 999, 12), )
if mibBuilder.loadTexts: userTable.setStatus('mandatory')
userEntry = MibTableRow((1, 3, 6, 1, 3, 999, 12, 1), ).setIndexNames((0, "UNIX-MIB", "userIndex"))
if mibBuilder.loadTexts: userEntry.setStatus('mandatory')
userIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userIndex.setStatus('mandatory')
userName = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userName.setStatus('mandatory')
userId = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userId.setStatus('mandatory')
userFullName = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userFullName.setStatus('mandatory')
userLoginShellCli = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userLoginShellCli.setStatus('mandatory')
userLoginDirectory = MibTableColumn((1, 3, 6, 1, 3, 999, 12, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userLoginDirectory.setStatus('mandatory')
installedSwTable = MibTable((1, 3, 6, 1, 3, 999, 13), )
if mibBuilder.loadTexts: installedSwTable.setStatus('mandatory')
installedSwEntry = MibTableRow((1, 3, 6, 1, 3, 999, 13, 1), ).setIndexNames((0, "UNIX-MIB", "installedSwIndex"))
if mibBuilder.loadTexts: installedSwEntry.setStatus('mandatory')
installedSwIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwIndex.setStatus('mandatory')
installedSwName = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwName.setStatus('mandatory')
installedSwVendorAuthor = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwVendorAuthor.setStatus('mandatory')
installedSwVersion = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwVersion.setStatus('mandatory')
installedSwVendorPatches = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwVendorPatches.setStatus('mandatory')
installedSwUserPatches = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwUserPatches.setStatus('mandatory')
installedSwLicInstalled = MibTableColumn((1, 3, 6, 1, 3, 999, 13, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSwLicInstalled.setStatus('mandatory')
licenseTable = MibTable((1, 3, 6, 1, 3, 999, 14), )
if mibBuilder.loadTexts: licenseTable.setStatus('mandatory')
licenseEntry = MibTableRow((1, 3, 6, 1, 3, 999, 14, 1), ).setIndexNames((0, "UNIX-MIB", "licenseIndex"))
if mibBuilder.loadTexts: licenseEntry.setStatus('mandatory')
licenseIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseIndex.setStatus('mandatory')
licenseProductName = MibScalar((1, 3, 6, 1, 3, 999, 14, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseProductName.setStatus('mandatory')
licenseVendorAuthor = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseVendorAuthor.setStatus('mandatory')
licenseExpirationDate = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseExpirationDate.setStatus('mandatory')
licenseVersion = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseVersion.setStatus('mandatory')
licenseCapacity = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseCapacity.setStatus('mandatory')
licenseAuthorization = MibTableColumn((1, 3, 6, 1, 3, 999, 14, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseAuthorization.setStatus('mandatory')
filesystemTable = MibTable((1, 3, 6, 1, 3, 999, 15), )
if mibBuilder.loadTexts: filesystemTable.setStatus('mandatory')
filesystemEntry = MibTableRow((1, 3, 6, 1, 3, 999, 15, 1), ).setIndexNames((0, "UNIX-MIB", "filesystemIndex"))
if mibBuilder.loadTexts: filesystemEntry.setStatus('mandatory')
filesystemIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filesystemIndex.setStatus('mandatory')
filesystemName = MibTableColumn((1, 3, 6, 1, 3, 999, 15, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filesystemName.setStatus('mandatory')
filesystemFreeCapacity = MibTableColumn((1, 3, 6, 1, 3, 999, 15, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filesystemFreeCapacity.setStatus('mandatory')
filesystemFormattedCap = MibTableColumn((1, 3, 6, 1, 3, 999, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filesystemFormattedCap.setStatus('mandatory')
mountInfoTable = MibTable((1, 3, 6, 1, 3, 999, 16), )
if mibBuilder.loadTexts: mountInfoTable.setStatus('mandatory')
mountInfoEntry = MibTableRow((1, 3, 6, 1, 3, 999, 16, 1), ).setIndexNames((0, "UNIX-MIB", "mountInfoIndex"))
if mibBuilder.loadTexts: mountInfoEntry.setStatus('mandatory')
mountInfoIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoIndex.setStatus('mandatory')
mountInfoFileSystemName = MibScalar((1, 3, 6, 1, 3, 999, 16, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoFileSystemName.setStatus('mandatory')
mountInfoDeviceName = MibTableColumn((1, 3, 6, 1, 3, 999, 16, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoDeviceName.setStatus('mandatory')
mountInfoMountPoint = MibTableColumn((1, 3, 6, 1, 3, 999, 16, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoMountPoint.setStatus('mandatory')
mountInfoMountType = MibTableColumn((1, 3, 6, 1, 3, 999, 16, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoMountType.setStatus('mandatory')
mountInfoRelVolNum = MibTableColumn((1, 3, 6, 1, 3, 999, 16, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountInfoRelVolNum.setStatus('mandatory')
mibBuilder.exportSymbols("UNIX-MIB", controllerUnitNumber=controllerUnitNumber, filesystemIndex=filesystemIndex, mountInfoRelVolNum=mountInfoRelVolNum, networkType=networkType, controllerTable=controllerTable, diskPartitionPrimaryHost=diskPartitionPrimaryHost, diskPartitionDeviceName=diskPartitionDeviceName, queueCapacity=queueCapacity, mountInfoTable=mountInfoTable, tapeMountPoint=tapeMountPoint, networkTable=networkTable, processorActiveState=processorActiveState, printerEntry=printerEntry, diskPartitionEntry=diskPartitionEntry, filesystemTable=filesystemTable, queuePrintServer=queuePrintServer, licenseVersion=licenseVersion, tapeDeviceDriver=tapeDeviceDriver, adapterNexusNumber=adapterNexusNumber, installedSwIndex=installedSwIndex, adapterRevLevel=adapterRevLevel, tapeTapeUnitNumber=tapeTapeUnitNumber, licenseProductName=licenseProductName, installedSwName=installedSwName, printerQueue=printerQueue, networkEntry=networkEntry, controllerIndex=controllerIndex, printerDeviceDriver=printerDeviceDriver, diskPartitionStartSector=diskPartitionStartSector, userEntry=userEntry, installedSwEntry=installedSwEntry, mountinfo=mountinfo, printer=printer, diskDeviceDriver=diskDeviceDriver, installedSwTable=installedSwTable, controller=controller, userIndex=userIndex, adapterTable=adapterTable, mountInfoMountType=mountInfoMountType, tape=tape, processor=processor, printerIndex=printerIndex, mountInfoMountPoint=mountInfoMountPoint, networkIndex=networkIndex, diskTable=diskTable, licenseCapacity=licenseCapacity, diskPartitionTable=diskPartitionTable, installedSwVendorPatches=installedSwVendorPatches, queueTable=queueTable, groupName=groupName, installedSwLicInstalled=installedSwLicInstalled, printerUnitNumber=printerUnitNumber, groupIndex=groupIndex, groupTable=groupTable, mountInfoEntry=mountInfoEntry, tapeIndex=tapeIndex, adapter=adapter, userLoginShellCli=userLoginShellCli, installedSwVersion=installedSwVersion, mountInfoDeviceName=mountInfoDeviceName, userFullName=userFullName, installedSwUserPatches=installedSwUserPatches, userLoginDirectory=userLoginDirectory, queueProtection=queueProtection, machineBootTime=machineBootTime, networkAddress=networkAddress, queue=queue, installedSwVendorAuthor=installedSwVendorAuthor, filesystemFreeCapacity=filesystemFreeCapacity, machineName=machineName, diskPartitionSize=diskPartitionSize, filesystem=filesystem, tapeDeviceName=tapeDeviceName, processorIndex=processorIndex, diskPrimaryHost=diskPrimaryHost, licenseEntry=licenseEntry, processorPrimary=processorPrimary, tapeDeviceType=tapeDeviceType, diskPartitionIndex=diskPartitionIndex, network=network, machineHwModel=machineHwModel, machineTime=machineTime, licenseTable=licenseTable, machineMemorySize=machineMemorySize, mountInfoIndex=mountInfoIndex, controllerName=controllerName, licenseVendorAuthor=licenseVendorAuthor, adapterName=adapterName, diskPhysicalCapacity=diskPhysicalCapacity, queueIndex=queueIndex, machineHwVersion=machineHwVersion, machineHwType=machineHwType, adapterType=adapterType, adapterUnitNumber=adapterUnitNumber, controllerEntry=controllerEntry, controllerType=controllerType, processorTable=processorTable, printerDeviceType=printerDeviceType, machineBootRoot=machineBootRoot, diskEntry=diskEntry, userId=userId, printerTable=printerTable, processorEntry=processorEntry, host=host, licenseAuthorization=licenseAuthorization, licenseExpirationDate=licenseExpirationDate, filesystemEntry=filesystemEntry, diskDeviceName=diskDeviceName, installedsw=installedsw, queueUserComment=queueUserComment, queueState=queueState, queueEntry=queueEntry, machine=machine, licenseIndex=licenseIndex, userTable=userTable, diskDeviceType=diskDeviceType, queueType=queueType, adapterEntry=adapterEntry, user=user, license=license, disk=disk, machineOsType=machineOsType, networkNodeName=networkNodeName, queuePriority=queuePriority, filesystemFormattedCap=filesystemFormattedCap, queueName=queueName, printerName=printerName, diskIndex=diskIndex, filesystemName=filesystemName, userName=userName, group=group, adapterIndex=adapterIndex, diskPartitionEndSector=diskPartitionEndSector, machineOsVersion=machineOsVersion, tapeTable=tapeTable, machineVendor=machineVendor, queueDestinationList=queueDestinationList, tapeEntry=tapeEntry, groupId=groupId, groupEntry=groupEntry, mountInfoFileSystemName=mountInfoFileSystemName, diskUnitNumber=diskUnitNumber, diskPartition=diskPartition, diskPartitionName=diskPartitionName)

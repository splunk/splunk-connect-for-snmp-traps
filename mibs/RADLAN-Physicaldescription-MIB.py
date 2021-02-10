#
# PySNMP MIB module RADLAN-Physicaldescription-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-Physicaldescription-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
EntitySensorStatus, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorStatus", "EntitySensorValue")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
JackType, = mibBuilder.importSymbols("MAU-MIB", "JackType")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
RlEnvMonState, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "RlEnvMonState")
rndNotifications, rnd = mibBuilder.importSymbols("RADLAN-MIB", "rndNotifications", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, ObjectIdentity, IpAddress, Integer32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter64", "Counter32", "ModuleIdentity")
PhysAddress, RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
rlPhysicalDescription = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 53))
rlPhysicalDescription.setRevisions(('2006-02-12 00:00', '2003-10-18 00:00',))
if mibBuilder.loadTexts: rlPhysicalDescription.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlPhysicalDescription.setOrganization('Radlan Computer Communications Ltd.')
class CascadePortState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("error", 0), ("init", 1), ("down", 2), ("active", 3), ("standby", 4))

class CascadePortSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 6, 8, 9, 13, 14))
    namedValues = NamedValues(("port-speed-unknown", 0), ("port-speed-100M", 1), ("port-speed-1G", 2), ("port-speed-10G", 3), ("port-speed-5G", 6), ("port-speed-20G", 8), ("port-speed-40G", 9), ("port-speed-100G", 13), ("port-speed-auto", 14))

rlPhdMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMibVersion.setStatus('current')
rlPhdModuleTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 2), )
if mibBuilder.loadTexts: rlPhdModuleTable.setStatus('current')
rlPhdModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 2, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleEntry.setStatus('current')
rlPhdModuleStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStackUnit.setStatus('current')
rlPhdModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleIndex.setStatus('current')
rlPhdModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleType.setStatus('current')
rlPhdModuleStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStartingPort.setStatus('current')
rlPhdModuleNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleNumberOfPorts.setStatus('current')
rlPhdModuleRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRow.setStatus('current')
rlPhdModuleColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleColumn.setStatus('current')
rlPhdModuleRole = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 1), ("master", 2), ("backup", 3), ("slave", 4))).clone('standalone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRole.setStatus('current')
rlPhdPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 3), )
if mibBuilder.loadTexts: rlPhdPortsTable.setStatus('current')
rlPhdPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 3, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdPortsIfIndex"))
if mibBuilder.loadTexts: rlPhdPortsEntry.setStatus('current')
rlPhdPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndex.setStatus('current')
rlPhdPortsIfIndexName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndexName.setStatus('current')
rlPhdPortsMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("copper", 1), ("optic-fiber", 2), ("combo", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsMediaType.setStatus('current')
rlPhdPortsStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsStackUnit.setStatus('current')
rlPhdPortsModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsModuleNumber.setStatus('current')
rlPhdPortsRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsRow.setStatus('current')
rlPhdPortsColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsColumn.setStatus('current')
rlPhdConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 8), JackType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdConnectorType.setStatus('current')
rlPhdPortHaul = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-relevant", 1), ("short", 2), ("long", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortHaul.setStatus('current')
rlPhdStackTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 4), )
if mibBuilder.loadTexts: rlPhdStackTable.setStatus('current')
rlPhdStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 4, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdStackUnit"))
if mibBuilder.loadTexts: rlPhdStackEntry.setStatus('current')
rlPhdStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackUnit.setStatus('current')
rlPhdStackType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackType.setStatus('current')
rlPhdStackConnect1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect1.setStatus('current')
rlPhdStackConnect2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect2.setStatus('current')
rlPhdStackSofrwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackSofrwareVer.setStatus('current')
rlPhdStackProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackProductID.setStatus('current')
rlPhdStackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackMacAddr.setStatus('current')
rlPhdModuleHotSwapTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 5), )
if mibBuilder.loadTexts: rlPhdModuleHotSwapTable.setStatus('current')
rlPhdModuleHotSwapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 5, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleHotSwapEntry.setStatus('current')
rlPhdModuleHotSwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdModuleHotSwapAdminStatus.setStatus('current')
rlPhdModuleHotSwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleHotSwapOperStatus.setStatus('current')
rlPhdStackOrderTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 6), )
if mibBuilder.loadTexts: rlPhdStackOrderTable.setStatus('current')
rlPhdStackOrderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 6, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdStackOrderCurrentUnitPosition"))
if mibBuilder.loadTexts: rlPhdStackOrderEntry.setStatus('current')
rlPhdStackOrderCurrentUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderCurrentUnitPosition.setStatus('current')
rlPhdStackOrderDesiredUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderDesiredUnitPosition.setStatus('current')
rlPhdStackOrderUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderUnitIndex.setStatus('current')
rlPhdStackOrderUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackOrderUnitType.setStatus('current')
rlPhdStackReorder = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reorder", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReorder.setStatus('current')
rlPhdNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfUnits.setStatus('current')
rlPhdMaxNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMaxNumberOfUnits.setStatus('current')
rlPhdForceMasterUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdForceMasterUnit.setStatus('current')
rlPhdStackFixedUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnit.setStatus('current')
rlPhdStackFixedUnitLocation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bottom", 1), ("top", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnitLocation.setStatus('current')
rlPhdStackReloadUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReloadUnit.setStatus('current')
rlPhdUnitGenParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 14), )
if mibBuilder.loadTexts: rlPhdUnitGenParamTable.setStatus('current')
rlPhdUnitGenParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 14, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdUnitGenParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitGenParamEntry.setStatus('current')
rlPhdUnitGenParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamStackUnit.setStatus('current')
rlPhdUnitGenParamSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamSoftwareVersion.setStatus('current')
rlPhdUnitGenParamFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamFirmwareVersion.setStatus('current')
rlPhdUnitGenParamHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamHardwareVersion.setStatus('current')
rlPhdUnitGenParamSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamSerialNum.setStatus('current')
rlPhdUnitGenParamAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamAssetTag.setStatus('current')
rlPhdUnitGenParamServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamServiceTag.setStatus('current')
rlPhdUnitGenParamSoftwareDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamSoftwareDate.setStatus('current')
rlPhdUnitGenParamFirmwareDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamFirmwareDate.setStatus('current')
rlPhdUnitGenParamManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamManufacturer.setStatus('current')
rlPhdUnitGenParamModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamModelName.setStatus('current')
rlPhdUnitGenParamMd5ChksumBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumBoot.setStatus('current')
rlPhdUnitGenParamMd5ChksumImage1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumImage1.setStatus('current')
rlPhdUnitGenParamMd5ChksumImage2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumImage2.setStatus('current')
rlPhdUnitGenParamRegistrationDone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamRegistrationDone.setStatus('current')
rlPhdUnitGenParamRegistrationSuppressed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamRegistrationSuppressed.setStatus('current')
rlPhdUnitEnvParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 15), )
if mibBuilder.loadTexts: rlPhdUnitEnvParamTable.setStatus('current')
rlPhdUnitEnvParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 15, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdUnitEnvParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitEnvParamEntry.setStatus('current')
rlPhdUnitEnvParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamStackUnit.setStatus('current')
rlPhdUnitEnvParamMainPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 2), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMainPSStatus.setStatus('current')
rlPhdUnitEnvParamRedundantPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamRedundantPSStatus.setStatus('current')
rlPhdUnitEnvParamFan1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 4), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan1Status.setStatus('current')
rlPhdUnitEnvParamFan2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 5), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan2Status.setStatus('current')
rlPhdUnitEnvParamFan3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 6), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan3Status.setStatus('current')
rlPhdUnitEnvParamFan4Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 7), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan4Status.setStatus('current')
rlPhdUnitEnvParamFan5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 8), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan5Status.setStatus('current')
rlPhdUnitEnvParamFan6Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 9), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan6Status.setStatus('current')
rlPhdUnitEnvParamTempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 10), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorValue.setStatus('current')
rlPhdUnitEnvParamTempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 11), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorStatus.setStatus('current')
rlPhdUnitEnvParamTempSensorWarningThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 12), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorWarningThresholdValue.setStatus('current')
rlPhdUnitEnvParamTempSensorCriticalThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 13), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorCriticalThresholdValue.setStatus('current')
rlPhdUnitEnvParamUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamUpTime.setStatus('current')
rlPhdUnitEnvParamMonitorAutoRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorAutoRecoveryEnable.setStatus('current')
rlPhdUnitEnvParamMonitorTemperatureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("overTemperatureThreshold", 2), ("overCriticalTemperatureThreshold", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorTemperatureStatus.setStatus('current')
rlPhdUnitEnvParamMonitorOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorOperStatus.setStatus('current')
rlPhdStackOrderTopUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderTopUnit.setStatus('current')
rlPhdStackOrderBottomUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderBottomUnit.setStatus('current')
rlPhdStackOrderPermutation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderPermutation.setStatus('current')
rlPhdNumberOfPoeUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfPoeUnits.setStatus('current')
rlPhdPoeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 20), )
if mibBuilder.loadTexts: rlPhdPoeTable.setStatus('current')
rlPhdPoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 20, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdPoeStackUnit"))
if mibBuilder.loadTexts: rlPhdPoeEntry.setStatus('current')
rlPhdPoeStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoeStackUnit.setStatus('current')
rlPhdPoePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoePresent.setStatus('current')
rlPhdPhyLedStackUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedStackUnit.setStatus('current')
rlPhdPhyLedTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedTimeout.setStatus('current')
rlCascadeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 23), )
if mibBuilder.loadTexts: rlCascadeTable.setStatus('current')
rlCascadeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 23, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlCascadeEntry.setStatus('current')
rlCascadeNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborIfIndex.setStatus('current')
rlCascadeNeighborUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborUnit.setStatus('current')
rlCascadeTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeTrunkId.setStatus('current')
rlCascadeUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeUnitId.setStatus('current')
rlCascadePortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 5), CascadePortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadePortSpeed.setStatus('current')
rlCascadePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 6), CascadePortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadePortState.setStatus('current')
rlCascadeAdminTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 24), )
if mibBuilder.loadTexts: rlCascadeAdminTable.setStatus('current')
rlCascadeAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 24, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlCascadeAdminUnitId"))
if mibBuilder.loadTexts: rlCascadeAdminEntry.setStatus('current')
rlCascadeAdminUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )))
if mibBuilder.loadTexts: rlCascadeAdminUnitId.setStatus('current')
rlCascadeAdminIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadeAdminIndexList.setStatus('current')
rlCascadeAdminSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 3), CascadePortSpeed()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadeAdminSpeed.setStatus('current')
rlStackUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 186)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitRemoved.setStatus('current')
rlStackConfigChangedRingChain = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 187)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackConfigChangedRingChain.setStatus('current')
rlStackBackupUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 188)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackBackupUnitRemoved.setStatus('current')
rlStackMasterSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 189)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackMasterSwitchover.setStatus('current')
rlStackUnitDifferentSwVersion = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 190)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitDifferentSwVersion.setStatus('current')
rlStackDuplicateUnitNotJoin = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 191)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackDuplicateUnitNotJoin.setStatus('current')
rlStackLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 195)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackLinkChange.setStatus('current')
class StackPortType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("port-type-100M", 0), ("port-type-1G", 1), ("port-type-5G", 2), ("port-type-10G", 3), ("port-type-40G", 4))

class ConnectionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("copper", 1), ("combo-copper", 2), ("combo-fiber", 3), ("fiber", 4), ("direct-attached", 5))

rlPhdUnitStackPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 25), )
if mibBuilder.loadTexts: rlPhdUnitStackPortTable.setStatus('current')
rlPhdUnitStackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 25, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlPhdUnitStackPortEntry.setStatus('current')
rlPhdUnitStackPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortName.setStatus('current')
rlPhdUnitStackPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 2), StackPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortType.setStatus('current')
rlPhdUnitStackPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 3), ConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortConnectionType.setStatus('current')
rlPhdUnitStackPortRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortRow.setStatus('current')
rlPhdUnitStackPortColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortColumn.setStatus('current')
mibBuilder.exportSymbols("RADLAN-Physicaldescription-MIB", rlPhdUnitGenParamRegistrationDone=rlPhdUnitGenParamRegistrationDone, rlPhdModuleHotSwapEntry=rlPhdModuleHotSwapEntry, StackPortType=StackPortType, rlCascadeUnitId=rlCascadeUnitId, rlPhdUnitEnvParamMonitorTemperatureStatus=rlPhdUnitEnvParamMonitorTemperatureStatus, rlPhdStackOrderBottomUnit=rlPhdStackOrderBottomUnit, rlPhdUnitEnvParamFan6Status=rlPhdUnitEnvParamFan6Status, rlPhdStackOrderDesiredUnitPosition=rlPhdStackOrderDesiredUnitPosition, rlCascadePortSpeed=rlCascadePortSpeed, rlPhdUnitEnvParamStackUnit=rlPhdUnitEnvParamStackUnit, rlPhdPortsIfIndexName=rlPhdPortsIfIndexName, rlPhdModuleStartingPort=rlPhdModuleStartingPort, rlPhdUnitGenParamModelName=rlPhdUnitGenParamModelName, rlStackBackupUnitRemoved=rlStackBackupUnitRemoved, rlPhdPortsStackUnit=rlPhdPortsStackUnit, rlPhdStackReloadUnit=rlPhdStackReloadUnit, rlPhdUnitStackPortColumn=rlPhdUnitStackPortColumn, rlPhdUnitGenParamEntry=rlPhdUnitGenParamEntry, rlPhdUnitEnvParamFan5Status=rlPhdUnitEnvParamFan5Status, rlPhdStackFixedUnitLocation=rlPhdStackFixedUnitLocation, rlPhdUnitEnvParamRedundantPSStatus=rlPhdUnitEnvParamRedundantPSStatus, rlPhdNumberOfPoeUnits=rlPhdNumberOfPoeUnits, rlPhdPortsEntry=rlPhdPortsEntry, rlPhdUnitEnvParamTempSensorValue=rlPhdUnitEnvParamTempSensorValue, rlPhdUnitEnvParamFan2Status=rlPhdUnitEnvParamFan2Status, rlPhdPortsModuleNumber=rlPhdPortsModuleNumber, rlPhdUnitStackPortTable=rlPhdUnitStackPortTable, rlPhdUnitGenParamMd5ChksumImage1=rlPhdUnitGenParamMd5ChksumImage1, rlPhdUnitGenParamFirmwareVersion=rlPhdUnitGenParamFirmwareVersion, rlPhdPhyLedStackUnit=rlPhdPhyLedStackUnit, rlPhdModuleRow=rlPhdModuleRow, rlPhdModuleType=rlPhdModuleType, rlPhdPoePresent=rlPhdPoePresent, CascadePortSpeed=CascadePortSpeed, rlPhdStackEntry=rlPhdStackEntry, rlCascadeTrunkId=rlCascadeTrunkId, rlPhdStackConnect1=rlPhdStackConnect1, CascadePortState=CascadePortState, rlPhdUnitGenParamFirmwareDate=rlPhdUnitGenParamFirmwareDate, rlPhdStackOrderUnitType=rlPhdStackOrderUnitType, rlPhdStackConnect2=rlPhdStackConnect2, rlPhdPortsIfIndex=rlPhdPortsIfIndex, rlPhdStackOrderEntry=rlPhdStackOrderEntry, rlPhdNumberOfUnits=rlPhdNumberOfUnits, rlPhdStackSofrwareVer=rlPhdStackSofrwareVer, rlPhdStackUnit=rlPhdStackUnit, rlCascadeAdminUnitId=rlCascadeAdminUnitId, rlStackUnitDifferentSwVersion=rlStackUnitDifferentSwVersion, rlPhdStackReorder=rlPhdStackReorder, rlPhdStackOrderTopUnit=rlPhdStackOrderTopUnit, rlPhdUnitGenParamMd5ChksumImage2=rlPhdUnitGenParamMd5ChksumImage2, rlStackDuplicateUnitNotJoin=rlStackDuplicateUnitNotJoin, rlCascadePortState=rlCascadePortState, rlPhdUnitGenParamSoftwareVersion=rlPhdUnitGenParamSoftwareVersion, rlPhdStackOrderUnitIndex=rlPhdStackOrderUnitIndex, rlPhdPoeTable=rlPhdPoeTable, rlPhdModuleTable=rlPhdModuleTable, rlPhdModuleHotSwapTable=rlPhdModuleHotSwapTable, rlPhdUnitGenParamSoftwareDate=rlPhdUnitGenParamSoftwareDate, rlPhdPhyLedTimeout=rlPhdPhyLedTimeout, rlPhdUnitEnvParamMonitorAutoRecoveryEnable=rlPhdUnitEnvParamMonitorAutoRecoveryEnable, rlPhdStackOrderCurrentUnitPosition=rlPhdStackOrderCurrentUnitPosition, rlCascadeEntry=rlCascadeEntry, rlPhdUnitEnvParamMonitorOperStatus=rlPhdUnitEnvParamMonitorOperStatus, rlPhdUnitEnvParamFan4Status=rlPhdUnitEnvParamFan4Status, rlPhdModuleStackUnit=rlPhdModuleStackUnit, rlPhdModuleIndex=rlPhdModuleIndex, rlPhdUnitGenParamSerialNum=rlPhdUnitGenParamSerialNum, ConnectionType=ConnectionType, rlCascadeNeighborUnit=rlCascadeNeighborUnit, rlPhdStackProductID=rlPhdStackProductID, rlPhdUnitGenParamTable=rlPhdUnitGenParamTable, rlPhdUnitStackPortEntry=rlPhdUnitStackPortEntry, rlPhdPortsColumn=rlPhdPortsColumn, rlPhdModuleHotSwapOperStatus=rlPhdModuleHotSwapOperStatus, rlPhdUnitEnvParamTable=rlPhdUnitEnvParamTable, rlPhdMibVersion=rlPhdMibVersion, rlPhdStackTable=rlPhdStackTable, rlPhdStackFixedUnit=rlPhdStackFixedUnit, rlPhdPoeEntry=rlPhdPoeEntry, rlCascadeTable=rlCascadeTable, rlPhdMaxNumberOfUnits=rlPhdMaxNumberOfUnits, rlPhdUnitGenParamManufacturer=rlPhdUnitGenParamManufacturer, rlPhdUnitStackPortType=rlPhdUnitStackPortType, PYSNMP_MODULE_ID=rlPhysicalDescription, rlPhdStackOrderPermutation=rlPhdStackOrderPermutation, rlPhdUnitStackPortRow=rlPhdUnitStackPortRow, rlPhdUnitEnvParamUpTime=rlPhdUnitEnvParamUpTime, rlCascadeNeighborIfIndex=rlCascadeNeighborIfIndex, rlPhdStackOrderTable=rlPhdStackOrderTable, rlPhdUnitEnvParamTempSensorCriticalThresholdValue=rlPhdUnitEnvParamTempSensorCriticalThresholdValue, rlPhdPortsTable=rlPhdPortsTable, rlCascadeAdminIndexList=rlCascadeAdminIndexList, rlPhdModuleEntry=rlPhdModuleEntry, rlPhdUnitEnvParamTempSensorStatus=rlPhdUnitEnvParamTempSensorStatus, rlCascadeAdminTable=rlCascadeAdminTable, rlPhdUnitEnvParamMainPSStatus=rlPhdUnitEnvParamMainPSStatus, rlPhdPoeStackUnit=rlPhdPoeStackUnit, rlPhdModuleRole=rlPhdModuleRole, rlStackConfigChangedRingChain=rlStackConfigChangedRingChain, rlPhdModuleNumberOfPorts=rlPhdModuleNumberOfPorts, rlPhdUnitEnvParamFan3Status=rlPhdUnitEnvParamFan3Status, rlPhdModuleColumn=rlPhdModuleColumn, rlPhdModuleHotSwapAdminStatus=rlPhdModuleHotSwapAdminStatus, rlPhdStackMacAddr=rlPhdStackMacAddr, rlPhysicalDescription=rlPhysicalDescription, rlPhdUnitStackPortName=rlPhdUnitStackPortName, rlCascadeAdminSpeed=rlCascadeAdminSpeed, rlPhdUnitGenParamRegistrationSuppressed=rlPhdUnitGenParamRegistrationSuppressed, rlPhdPortHaul=rlPhdPortHaul, rlPhdForceMasterUnit=rlPhdForceMasterUnit, rlCascadeAdminEntry=rlCascadeAdminEntry, rlPhdUnitGenParamStackUnit=rlPhdUnitGenParamStackUnit, rlPhdStackType=rlPhdStackType, rlPhdUnitEnvParamTempSensorWarningThresholdValue=rlPhdUnitEnvParamTempSensorWarningThresholdValue, rlStackUnitRemoved=rlStackUnitRemoved, rlPhdPortsRow=rlPhdPortsRow, rlStackLinkChange=rlStackLinkChange, rlPhdUnitGenParamServiceTag=rlPhdUnitGenParamServiceTag, rlPhdUnitStackPortConnectionType=rlPhdUnitStackPortConnectionType, rlPhdUnitGenParamHardwareVersion=rlPhdUnitGenParamHardwareVersion, rlPhdPortsMediaType=rlPhdPortsMediaType, rlPhdUnitGenParamMd5ChksumBoot=rlPhdUnitGenParamMd5ChksumBoot, rlStackMasterSwitchover=rlStackMasterSwitchover, rlPhdUnitEnvParamEntry=rlPhdUnitEnvParamEntry, rlPhdUnitGenParamAssetTag=rlPhdUnitGenParamAssetTag, rlPhdConnectorType=rlPhdConnectorType, rlPhdUnitEnvParamFan1Status=rlPhdUnitEnvParamFan1Status)

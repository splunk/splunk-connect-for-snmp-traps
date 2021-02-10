#
# PySNMP MIB module HM2-PWRMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PWRMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, Counter32, iso, Gauge32, Counter64, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "iso", "Gauge32", "Counter64", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PowerMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 11))
hm2PowerMgmtMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2PowerMgmtMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2PowerMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2PowerMgmtMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 0))
hm2PowerMgmtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 1))
hm2PowerSupplyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1))
hm2PSTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1), )
if mibBuilder.loadTexts: hm2PSTable.setStatus('current')
hm2PSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSID"))
if mibBuilder.loadTexts: hm2PSEntry.setStatus('current')
hm2PSID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSID.setStatus('current')
hm2PSState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("present", 1), ("defective", 2), ("notInstalled", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSState.setStatus('current')
hm2PSUSlotInfoTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10), )
if mibBuilder.loadTexts: hm2PSUSlotInfoTable.setStatus('current')
hm2PSUSlotInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"))
if mibBuilder.loadTexts: hm2PSUSlotInfoEntry.setStatus('current')
hm2PSUSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hm2PSUSlotIndex.setStatus('current')
hm2PSUSlotChassisTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 0), ("mach1020", 1), ("mach4000", 2), ("railswitch", 3), ("grs", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotChassisTypeId.setStatus('current')
hm2PSUSlotManufacturerId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("other", 0), ("hirschmann", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotManufacturerId.setStatus('current')
hm2PSUSlotManufacturerDate = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotManufacturerDate.setStatus('obsolete')
hm2PSUSlotSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotSerialNumber.setStatus('current')
hm2PSUSlotProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotProductCode.setStatus('current')
hm2PSUSlotDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotDescription.setStatus('current')
hm2PSUSlotCombinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("only-on-psu1", 0), ("psu1-sys-psu2-poe", 1), ("psu1-poe-psu2-sys", 2), ("two-separate-psus", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotCombinationType.setStatus('current')
hm2PSUSlotTemperatureRange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("tr-0-60", 0), ("tr-minus40-60", 1), ("tr-minus40-70", 2), ("tr-minus40-70cc", 3), ("tr-minus40-85", 4), ("tr-minus40-85cc", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotTemperatureRange.setStatus('current')
hm2PSUSlotRevisionId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotRevisionId.setStatus('current')
hm2PSUUnitInfoTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20), )
if mibBuilder.loadTexts: hm2PSUUnitInfoTable.setStatus('current')
hm2PSUUnitInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"), (0, "HM2-PWRMGMT-MIB", "hm2PSUUnitIndex"))
if mibBuilder.loadTexts: hm2PSUUnitInfoEntry.setStatus('current')
hm2PSUUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: hm2PSUUnitIndex.setStatus('current')
hm2PSUUnitConverterType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("dc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitConverterType.setStatus('current')
hm2PSUUnitNumberOfInputs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitNumberOfInputs.setStatus('current')
hm2PSUUnitOutputType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("system", 1), ("both", 2), ("poe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitOutputType.setStatus('current')
hm2PSUUnitSystemBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitSystemBudget.setStatus('current')
hm2PSUUnitPoeBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitPoeBudget.setStatus('current')
hm2PSUUnitFanCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitFanCount.setStatus('current')
hm2PSUUnitVoltageRange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("vr-18-60vdc", 0), ("vr-24-60vdc", 1), ("vr-24-48vdc", 2), ("vr-60-250vdc-110-240vac", 3), ("vr-48-54vdc-poe", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitVoltageRange.setStatus('current')
hm2PSUUnitPowerInterruption = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitPowerInterruption.setStatus('current')
hm2PowerSupplyTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 11, 0, 1)).setObjects(("HM2-PWRMGMT-MIB", "hm2PSID"), ("HM2-PWRMGMT-MIB", "hm2PSState"))
if mibBuilder.loadTexts: hm2PowerSupplyTrap.setStatus('current')
mibBuilder.exportSymbols("HM2-PWRMGMT-MIB", hm2PSUUnitIndex=hm2PSUUnitIndex, hm2PSUSlotCombinationType=hm2PSUSlotCombinationType, hm2PSUUnitConverterType=hm2PSUUnitConverterType, hm2PSUSlotIndex=hm2PSUSlotIndex, hm2PSUSlotChassisTypeId=hm2PSUSlotChassisTypeId, hm2PSUUnitNumberOfInputs=hm2PSUUnitNumberOfInputs, hm2PSUUnitInfoTable=hm2PSUUnitInfoTable, hm2PSUSlotInfoTable=hm2PSUSlotInfoTable, hm2PowerMgmtMibNotifications=hm2PowerMgmtMibNotifications, PYSNMP_MODULE_ID=hm2PowerMgmtMib, hm2PowerSupplyGroup=hm2PowerSupplyGroup, hm2PSUUnitOutputType=hm2PSUUnitOutputType, hm2PSUUnitSystemBudget=hm2PSUUnitSystemBudget, hm2PSUUnitPowerInterruption=hm2PSUUnitPowerInterruption, hm2PSUSlotManufacturerDate=hm2PSUSlotManufacturerDate, hm2PSUSlotDescription=hm2PSUSlotDescription, hm2PSUUnitVoltageRange=hm2PSUUnitVoltageRange, hm2PSTable=hm2PSTable, hm2PSState=hm2PSState, hm2PowerMgmtMib=hm2PowerMgmtMib, hm2PSUSlotManufacturerId=hm2PSUSlotManufacturerId, hm2PSUUnitPoeBudget=hm2PSUUnitPoeBudget, hm2PSUSlotInfoEntry=hm2PSUSlotInfoEntry, hm2PowerMgmtMibObjects=hm2PowerMgmtMibObjects, hm2PowerSupplyTrap=hm2PowerSupplyTrap, hm2PSEntry=hm2PSEntry, hm2PSUSlotRevisionId=hm2PSUSlotRevisionId, hm2PSUUnitFanCount=hm2PSUUnitFanCount, hm2PSID=hm2PSID, hm2PSUSlotTemperatureRange=hm2PSUSlotTemperatureRange, hm2PSUUnitInfoEntry=hm2PSUUnitInfoEntry, hm2PSUSlotProductCode=hm2PSUSlotProductCode, hm2PSUSlotSerialNumber=hm2PSUSlotSerialNumber)

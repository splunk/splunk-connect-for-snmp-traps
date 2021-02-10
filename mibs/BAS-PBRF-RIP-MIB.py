#
# PySNMP MIB module BAS-PBRF-RIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-PBRF-RIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
BasLogicalPortId, BasChassisId, BasSlotId, BasInterfaceId, basPbrfRIP = mibBuilder.importSymbols("BAS-MIB", "BasLogicalPortId", "BasChassisId", "BasSlotId", "BasInterfaceId", "basPbrfRIP")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, ObjectIdentity, IpAddress, iso, Counter64, TimeTicks, MibIdentifier, Unsigned32, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress", "iso", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
basPbrfRIPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1))
if mibBuilder.loadTexts: basPbrfRIPMIB.setLastUpdated('9812220800Z')
if mibBuilder.loadTexts: basPbrfRIPMIB.setOrganization('Broadband Access Systems, Inc.')
basPbrfRIPImport = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1))
basPbrfRIPExport = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2))
basPbrfRIPImportTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1), )
if mibBuilder.loadTexts: basPbrfRIPImportTable.setStatus('current')
basPbrfRIPImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIndex"))
if mibBuilder.loadTexts: basPbrfRIPImportEntry.setStatus('current')
basPbrfRIPImportChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportChassis.setStatus('current')
basPbrfRIPImportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportSlot.setStatus('current')
basPbrfRIPImportIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportIf.setStatus('current')
basPbrfRIPImportLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportLPort.setStatus('current')
basPbrfRIPImportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportIndex.setStatus('current')
basPbrfRIPImportTemplateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateCount.setStatus('current')
basPbrfRIPImportRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportRowStatus.setStatus('current')
basPbrfRIPImportDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportDescr.setStatus('current')
basPbrfRIPImportFilterTempTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2), )
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTable.setStatus('current')
basPbrfRIPImportFilterTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIndex"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempTemplate"))
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempEntry.setStatus('current')
basPbrfRIPImportFilterTempChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempChassis.setStatus('current')
basPbrfRIPImportFilterTempSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempSlot.setStatus('current')
basPbrfRIPImportFilterTempIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIf.setStatus('current')
basPbrfRIPImportFilterTempLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempLPort.setStatus('current')
basPbrfRIPImportFilterTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIndex.setStatus('current')
basPbrfRIPImportFilterTempTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 6), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTemplate.setStatus('current')
basPbrfRIPImportFilterTempOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempOrder.setStatus('current')
basPbrfRIPImportFilterTempRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempRowStatus.setStatus('current')
basPbrfRIPImportTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3), )
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTable.setStatus('current')
basPbrfRIPImportTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIndex"))
if mibBuilder.loadTexts: basPbrfRIPImportTemplateEntry.setStatus('current')
basPbrfRIPImportTemplateChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateChassis.setStatus('current')
basPbrfRIPImportTemplateSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateSlot.setStatus('current')
basPbrfRIPImportTemplateIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIf.setStatus('current')
basPbrfRIPImportTemplateLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateLPort.setStatus('current')
basPbrfRIPImportTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIndex.setStatus('current')
basPbrfRIPImportTemplateRouteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteAddr.setStatus('current')
basPbrfRIPImportTemplateRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteMask.setStatus('current')
basPbrfRIPImportTemplatePeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerAddr.setStatus('current')
basPbrfRIPImportTemplatePeerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerMask.setStatus('current')
basPbrfRIPImportTemplateTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTag.setStatus('current')
basPbrfRIPImportTemplateKeyBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateKeyBits.setStatus('current')
basPbrfRIPImportTemplatePref = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePref.setStatus('current')
basPbrfRIPImportTemplateMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateMetric.setStatus('current')
basPbrfRIPImportTemplateFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateFlags.setStatus('current')
basPbrfRIPImportTemplateActionTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateActionTag.setStatus('current')
basPbrfRIPImportTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRowStatus.setStatus('current')
basPbrfRIPImportTemplateDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateDescr.setStatus('current')
basPbrfRIPExportTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1), )
if mibBuilder.loadTexts: basPbrfRIPExportTable.setStatus('current')
basPbrfRIPExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIndex"))
if mibBuilder.loadTexts: basPbrfRIPExportEntry.setStatus('current')
basPbrfRIPExportChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportChassis.setStatus('current')
basPbrfRIPExportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportSlot.setStatus('current')
basPbrfRIPExportIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportIf.setStatus('current')
basPbrfRIPExportLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportLPort.setStatus('current')
basPbrfRIPExportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportIndex.setStatus('current')
basPbrfRIPExportTemplateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateCount.setStatus('current')
basPbrfRIPExportRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportRowStatus.setStatus('current')
basPbrfRIPExportDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportDescr.setStatus('current')
basPbrfRIPExportFilterTempTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2), )
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTable.setStatus('current')
basPbrfRIPExportFilterTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIndex"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempTemplate"))
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempEntry.setStatus('current')
basPbrfRIPExportFilterTempChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempChassis.setStatus('current')
basPbrfRIPExportFilterTempSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempSlot.setStatus('current')
basPbrfRIPExportFilterTempIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIf.setStatus('current')
basPbrfRIPExportFilterTempLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempLPort.setStatus('current')
basPbrfRIPExportFilterTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIndex.setStatus('current')
basPbrfRIPExportFilterTempTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 6), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTemplate.setStatus('current')
basPbrfRIPExportFilterTempOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempOrder.setStatus('current')
basPbrfRIPExportFilterTempRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempRowStatus.setStatus('current')
basPbrfRIPExportTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3), )
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTable.setStatus('current')
basPbrfRIPExportTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIndex"))
if mibBuilder.loadTexts: basPbrfRIPExportTemplateEntry.setStatus('current')
basPbrfRIPExportTemplateChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateChassis.setStatus('current')
basPbrfRIPExportTemplateSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSlot.setStatus('current')
basPbrfRIPExportTemplateIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIf.setStatus('current')
basPbrfRIPExportTemplateLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateLPort.setStatus('current')
basPbrfRIPExportTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIndex.setStatus('current')
basPbrfRIPExportTemplateRouteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteAddr.setStatus('current')
basPbrfRIPExportTemplateRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteMask.setStatus('current')
basPbrfRIPExportTemplateIntfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIntfAddr.setStatus('current')
basPbrfRIPExportTemplateProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateProtocol.setStatus('current')
basPbrfRIPExportTemplateSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSpecific.setStatus('current')
basPbrfRIPExportTemplatePeerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplatePeerMask.setStatus('current')
basPbrfRIPExportTemplateTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTag.setStatus('current')
basPbrfRIPExportTemplateKeyBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateKeyBits.setStatus('current')
basPbrfRIPExportTemplateMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateMetric.setStatus('current')
basPbrfRIPExportTemplateFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateFlags.setStatus('current')
basPbrfRIPExportTemplateActionTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateActionTag.setStatus('current')
basPbrfRIPExportTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRowStatus.setStatus('current')
basPbrfRIPExportTemplateDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateDescr.setStatus('current')
mibBuilder.exportSymbols("BAS-PBRF-RIP-MIB", basPbrfRIPExportTemplateRouteMask=basPbrfRIPExportTemplateRouteMask, basPbrfRIPImportFilterTempOrder=basPbrfRIPImportFilterTempOrder, basPbrfRIPImportTemplatePeerAddr=basPbrfRIPImportTemplatePeerAddr, basPbrfRIPImportTemplateChassis=basPbrfRIPImportTemplateChassis, basPbrfRIPExportTemplateDescr=basPbrfRIPExportTemplateDescr, basPbrfRIPExportTemplateMetric=basPbrfRIPExportTemplateMetric, basPbrfRIPExportTemplateTable=basPbrfRIPExportTemplateTable, basPbrfRIPExportFilterTempEntry=basPbrfRIPExportFilterTempEntry, basPbrfRIPImportTable=basPbrfRIPImportTable, basPbrfRIPImportTemplatePref=basPbrfRIPImportTemplatePref, basPbrfRIPExportRowStatus=basPbrfRIPExportRowStatus, basPbrfRIPImportChassis=basPbrfRIPImportChassis, basPbrfRIPExportFilterTempSlot=basPbrfRIPExportFilterTempSlot, basPbrfRIPExportFilterTempLPort=basPbrfRIPExportFilterTempLPort, basPbrfRIPImportRowStatus=basPbrfRIPImportRowStatus, basPbrfRIPImportTemplateKeyBits=basPbrfRIPImportTemplateKeyBits, basPbrfRIPExportEntry=basPbrfRIPExportEntry, basPbrfRIPImportTemplateRouteAddr=basPbrfRIPImportTemplateRouteAddr, basPbrfRIPExportSlot=basPbrfRIPExportSlot, basPbrfRIPExportFilterTempTemplate=basPbrfRIPExportFilterTempTemplate, basPbrfRIPImportTemplateTable=basPbrfRIPImportTemplateTable, basPbrfRIPExportTemplateLPort=basPbrfRIPExportTemplateLPort, basPbrfRIPExportFilterTempChassis=basPbrfRIPExportFilterTempChassis, basPbrfRIPExportTemplateSpecific=basPbrfRIPExportTemplateSpecific, basPbrfRIPImportTemplateTag=basPbrfRIPImportTemplateTag, basPbrfRIPExportTemplateActionTag=basPbrfRIPExportTemplateActionTag, basPbrfRIPExportTemplateRowStatus=basPbrfRIPExportTemplateRowStatus, basPbrfRIPExportFilterTempIndex=basPbrfRIPExportFilterTempIndex, basPbrfRIPImportTemplateCount=basPbrfRIPImportTemplateCount, basPbrfRIPExportChassis=basPbrfRIPExportChassis, basPbrfRIPImportFilterTempSlot=basPbrfRIPImportFilterTempSlot, basPbrfRIPImportTemplateActionTag=basPbrfRIPImportTemplateActionTag, basPbrfRIPMIB=basPbrfRIPMIB, basPbrfRIPExportTemplateIf=basPbrfRIPExportTemplateIf, PYSNMP_MODULE_ID=basPbrfRIPMIB, basPbrfRIPImportTemplateLPort=basPbrfRIPImportTemplateLPort, basPbrfRIPImportLPort=basPbrfRIPImportLPort, basPbrfRIPExportTemplateProtocol=basPbrfRIPExportTemplateProtocol, basPbrfRIPImportFilterTempTable=basPbrfRIPImportFilterTempTable, basPbrfRIPExportTemplateTag=basPbrfRIPExportTemplateTag, basPbrfRIPExportLPort=basPbrfRIPExportLPort, basPbrfRIPExportTemplateCount=basPbrfRIPExportTemplateCount, basPbrfRIPImportFilterTempIndex=basPbrfRIPImportFilterTempIndex, basPbrfRIPImportTemplateIf=basPbrfRIPImportTemplateIf, basPbrfRIPExportTemplateIndex=basPbrfRIPExportTemplateIndex, basPbrfRIPExportTemplateRouteAddr=basPbrfRIPExportTemplateRouteAddr, basPbrfRIPExport=basPbrfRIPExport, basPbrfRIPImport=basPbrfRIPImport, basPbrfRIPExportTemplateFlags=basPbrfRIPExportTemplateFlags, basPbrfRIPExportFilterTempTable=basPbrfRIPExportFilterTempTable, basPbrfRIPImportTemplateFlags=basPbrfRIPImportTemplateFlags, basPbrfRIPImportDescr=basPbrfRIPImportDescr, basPbrfRIPImportFilterTempRowStatus=basPbrfRIPImportFilterTempRowStatus, basPbrfRIPExportDescr=basPbrfRIPExportDescr, basPbrfRIPImportTemplateRowStatus=basPbrfRIPImportTemplateRowStatus, basPbrfRIPExportIndex=basPbrfRIPExportIndex, basPbrfRIPImportTemplatePeerMask=basPbrfRIPImportTemplatePeerMask, basPbrfRIPExportTemplateSlot=basPbrfRIPExportTemplateSlot, basPbrfRIPExportIf=basPbrfRIPExportIf, basPbrfRIPExportTemplatePeerMask=basPbrfRIPExportTemplatePeerMask, basPbrfRIPImportTemplateRouteMask=basPbrfRIPImportTemplateRouteMask, basPbrfRIPImportTemplateEntry=basPbrfRIPImportTemplateEntry, basPbrfRIPImportIf=basPbrfRIPImportIf, basPbrfRIPExportFilterTempRowStatus=basPbrfRIPExportFilterTempRowStatus, basPbrfRIPExportTemplateKeyBits=basPbrfRIPExportTemplateKeyBits, basPbrfRIPImportSlot=basPbrfRIPImportSlot, basPbrfRIPExportFilterTempIf=basPbrfRIPExportFilterTempIf, basPbrfRIPImportTemplateDescr=basPbrfRIPImportTemplateDescr, basPbrfRIPExportTemplateEntry=basPbrfRIPExportTemplateEntry, basPbrfRIPImportFilterTempChassis=basPbrfRIPImportFilterTempChassis, basPbrfRIPImportFilterTempLPort=basPbrfRIPImportFilterTempLPort, basPbrfRIPImportEntry=basPbrfRIPImportEntry, basPbrfRIPExportTable=basPbrfRIPExportTable, basPbrfRIPImportTemplateIndex=basPbrfRIPImportTemplateIndex, basPbrfRIPImportFilterTempIf=basPbrfRIPImportFilterTempIf, basPbrfRIPImportTemplateSlot=basPbrfRIPImportTemplateSlot, basPbrfRIPImportFilterTempEntry=basPbrfRIPImportFilterTempEntry, basPbrfRIPExportTemplateChassis=basPbrfRIPExportTemplateChassis, basPbrfRIPExportTemplateIntfAddr=basPbrfRIPExportTemplateIntfAddr, basPbrfRIPExportFilterTempOrder=basPbrfRIPExportFilterTempOrder, basPbrfRIPImportIndex=basPbrfRIPImportIndex, basPbrfRIPImportFilterTempTemplate=basPbrfRIPImportFilterTempTemplate, basPbrfRIPImportTemplateMetric=basPbrfRIPImportTemplateMetric)

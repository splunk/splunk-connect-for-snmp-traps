#
# PySNMP MIB module CYAN-AUG64-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-AUG64-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanOpStateQualTc, CyanSecServiceStateTc, CyanAdminStateTc, CyanOpStateTc, CyanAugStructureTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanOpStateQualTc", "CyanSecServiceStateTc", "CyanAdminStateTc", "CyanOpStateTc", "CyanAugStructureTc")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, MibIdentifier, Unsigned32, NotificationType, Counter32, Gauge32, Counter64, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "Counter64", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanAUG64Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240))
cyanAUG64Module.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanAUG64Module.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanAUG64Module.setOrganization('Cyan, Inc.')
cyanAUG64MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1))
cyanAUG64Table = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1), )
if mibBuilder.loadTexts: cyanAUG64Table.setStatus('current')
cyanAUG64Entry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1), ).setIndexNames((0, "CYAN-AUG64-MIB", "cyanAUG64ShelfId"), (0, "CYAN-AUG64-MIB", "cyanAUG64ModuleId"), (0, "CYAN-AUG64-MIB", "cyanAUG64AUG64Id"))
if mibBuilder.loadTexts: cyanAUG64Entry.setStatus('current')
cyanAUG64ShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanAUG64ShelfId.setStatus('current')
cyanAUG64ModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanAUG64ModuleId.setStatus('current')
cyanAUG64AUG64Id = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanAUG64AUG64Id.setStatus('current')
cyanAUG64AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64AdminState.setStatus('current')
cyanAUG64AutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64AutoinserviceSoakTimeSec.setStatus('current')
cyanAUG64Description = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64Description.setStatus('current')
cyanAUG64OperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 7), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64OperState.setStatus('current')
cyanAUG64OperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 8), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64OperStateQual.setStatus('current')
cyanAUG64SecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 9), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64SecServState.setStatus('current')
cyanAUG64StsaugStructure = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 10), CyanAugStructureTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64StsaugStructure.setStatus('current')
cyanAUG64ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 20)).setObjects(("CYAN-AUG64-MIB", "cyanAUG64AdminState"), ("CYAN-AUG64-MIB", "cyanAUG64AutoinserviceSoakTimeSec"), ("CYAN-AUG64-MIB", "cyanAUG64Description"), ("CYAN-AUG64-MIB", "cyanAUG64OperState"), ("CYAN-AUG64-MIB", "cyanAUG64OperStateQual"), ("CYAN-AUG64-MIB", "cyanAUG64SecServState"), ("CYAN-AUG64-MIB", "cyanAUG64StsaugStructure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanAUG64ObjectGroup = cyanAUG64ObjectGroup.setStatus('current')
cyanAUG64Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 30)).setObjects(("CYAN-AUG64-MIB", "cyanAUG64ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanAUG64Compliance = cyanAUG64Compliance.setStatus('current')
mibBuilder.exportSymbols("CYAN-AUG64-MIB", cyanAUG64AUG64Id=cyanAUG64AUG64Id, cyanAUG64ModuleId=cyanAUG64ModuleId, cyanAUG64AdminState=cyanAUG64AdminState, cyanAUG64ShelfId=cyanAUG64ShelfId, cyanAUG64Description=cyanAUG64Description, cyanAUG64OperStateQual=cyanAUG64OperStateQual, cyanAUG64OperState=cyanAUG64OperState, cyanAUG64StsaugStructure=cyanAUG64StsaugStructure, cyanAUG64ObjectGroup=cyanAUG64ObjectGroup, cyanAUG64Compliance=cyanAUG64Compliance, cyanAUG64Table=cyanAUG64Table, cyanAUG64Entry=cyanAUG64Entry, cyanAUG64MibObjects=cyanAUG64MibObjects, cyanAUG64SecServState=cyanAUG64SecServState, PYSNMP_MODULE_ID=cyanAUG64Module, cyanAUG64Module=cyanAUG64Module, cyanAUG64AutoinserviceSoakTimeSec=cyanAUG64AutoinserviceSoakTimeSec)

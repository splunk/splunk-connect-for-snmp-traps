#
# PySNMP MIB module NNCEXTE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCEXTE3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, IpAddress, Counter64, Unsigned32, NotificationType, TimeTicks, MibIdentifier, ModuleIdentity, Integer32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "IpAddress", "Counter64", "Unsigned32", "NotificationType", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncExtE3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 40))
if mibBuilder.loadTexts: nncExtE3.setLastUpdated('9611251500Z')
if mibBuilder.loadTexts: nncExtE3.setOrganization('Newbridge Networks Corporation')
nncExtE3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 40, 1))
nncExtE3Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 40, 2))
nncExtE3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 40, 3))
nncExtE3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 40, 4))
nncExtE3Current15MinTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1), )
if mibBuilder.loadTexts: nncExtE3Current15MinTable.setStatus('current')
nncExtE3Current15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncExtE3Current15MinEntry.setStatus('current')
nncExtE3Current15MinESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Current15MinESs.setStatus('current')
nncExtE3Current15MinSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Current15MinSESs.setStatus('current')
nncExtE3Current15MinSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Current15MinSEFs.setStatus('current')
nncExtE3Interval15MinTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2), )
if mibBuilder.loadTexts: nncExtE3Interval15MinTable.setStatus('current')
nncExtE3Interval15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NNCEXTE3-MIB", "nncExtE3Interval15MinNumber"))
if mibBuilder.loadTexts: nncExtE3Interval15MinEntry.setStatus('current')
nncExtE3Interval15MinNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: nncExtE3Interval15MinNumber.setStatus('current')
nncExtE3Interval15MinESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Interval15MinESs.setStatus('current')
nncExtE3Interval15MinSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Interval15MinSESs.setStatus('current')
nncExtE3Interval15MinSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Interval15MinSEFs.setStatus('current')
nncExtE3Total24HrTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3), )
if mibBuilder.loadTexts: nncExtE3Total24HrTable.setStatus('current')
nncExtE3Total24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncExtE3Total24HrEntry.setStatus('current')
nncExtE3Total24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Total24HrESs.setStatus('current')
nncExtE3Total24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Total24HrSESs.setStatus('current')
nncExtE3Total24HrSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3Total24HrSEFs.setStatus('current')
nncExtE3FarEndCurrent15MinTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4), )
if mibBuilder.loadTexts: nncExtE3FarEndCurrent15MinTable.setStatus('current')
nncExtE3FarEndCurrent15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncExtE3FarEndCurrent15MinEntry.setStatus('current')
nncExtE3FarEndCurrent15MinFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndCurrent15MinFEBEs.setStatus('current')
nncExtE3FarEndCurrent15MinESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndCurrent15MinESs.setStatus('current')
nncExtE3FarEndCurrent15MinSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndCurrent15MinSESs.setStatus('current')
nncExtE3FarEndInterval15MinTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5), )
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinTable.setStatus('current')
nncExtE3FarEndInterval15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinNumber"))
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinEntry.setStatus('current')
nncExtE3FarEndInterval15MinNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinNumber.setStatus('current')
nncExtE3FarEndInterval15MinFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinFEBEs.setStatus('current')
nncExtE3FarEndInterval15MinESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinESs.setStatus('current')
nncExtE3FarEndInterval15MinSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndInterval15MinSESs.setStatus('current')
nncExtE3FarEndTotal24HrTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6), )
if mibBuilder.loadTexts: nncExtE3FarEndTotal24HrTable.setStatus('current')
nncExtE3FarEndTotal24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncExtE3FarEndTotal24HrEntry.setStatus('current')
nncExtE3FarEndTotal24HrFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndTotal24HrFEBEs.setStatus('current')
nncExtE3FarEndTotal24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndTotal24HrESs.setStatus('current')
nncExtE3FarEndTotal24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtE3FarEndTotal24HrSESs.setStatus('current')
nncExtE3Current15MinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 1)).setObjects(("NNCEXTE3-MIB", "nncExtE3Current15MinESs"), ("NNCEXTE3-MIB", "nncExtE3Current15MinSESs"), ("NNCEXTE3-MIB", "nncExtE3Current15MinSEFs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3Current15MinGroup = nncExtE3Current15MinGroup.setStatus('current')
nncExtE3Interval15MinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 2)).setObjects(("NNCEXTE3-MIB", "nncExtE3Interval15MinNumber"), ("NNCEXTE3-MIB", "nncExtE3Interval15MinESs"), ("NNCEXTE3-MIB", "nncExtE3Interval15MinSESs"), ("NNCEXTE3-MIB", "nncExtE3Interval15MinSEFs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3Interval15MinGroup = nncExtE3Interval15MinGroup.setStatus('current')
nncExtE3Total24HrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 3)).setObjects(("NNCEXTE3-MIB", "nncExtE3Total24HrESs"), ("NNCEXTE3-MIB", "nncExtE3Total24HrSESs"), ("NNCEXTE3-MIB", "nncExtE3Total24HrSEFs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3Total24HrGroup = nncExtE3Total24HrGroup.setStatus('current')
nncExtE3FarEndCurrent15MinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 4)).setObjects(("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinFEBEs"), ("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinESs"), ("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinSESs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3FarEndCurrent15MinGroup = nncExtE3FarEndCurrent15MinGroup.setStatus('current')
nncExtE3FarEndInterval15MinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 5)).setObjects(("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinNumber"), ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinFEBEs"), ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinESs"), ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinSESs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3FarEndInterval15MinGroup = nncExtE3FarEndInterval15MinGroup.setStatus('current')
nncExtE3FarEndTotal24HrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 6)).setObjects(("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrFEBEs"), ("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrESs"), ("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrSESs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3FarEndTotal24HrGroup = nncExtE3FarEndTotal24HrGroup.setStatus('current')
nncExtE3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 40, 4, 1)).setObjects(("NNCEXTE3-MIB", "nncExtE3Current15MinGroup"), ("NNCEXTE3-MIB", "nncExtE3Interval15MinGroup"), ("NNCEXTE3-MIB", "nncExtE3Total24HrGroup"), ("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinGroup"), ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinGroup"), ("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtE3Compliance = nncExtE3Compliance.setStatus('current')
mibBuilder.exportSymbols("NNCEXTE3-MIB", nncExtE3FarEndCurrent15MinSESs=nncExtE3FarEndCurrent15MinSESs, nncExtE3FarEndInterval15MinESs=nncExtE3FarEndInterval15MinESs, nncExtE3Current15MinESs=nncExtE3Current15MinESs, nncExtE3FarEndInterval15MinGroup=nncExtE3FarEndInterval15MinGroup, nncExtE3FarEndTotal24HrGroup=nncExtE3FarEndTotal24HrGroup, nncExtE3Interval15MinGroup=nncExtE3Interval15MinGroup, nncExtE3Current15MinSEFs=nncExtE3Current15MinSEFs, nncExtE3FarEndTotal24HrESs=nncExtE3FarEndTotal24HrESs, nncExtE3Interval15MinESs=nncExtE3Interval15MinESs, nncExtE3Interval15MinEntry=nncExtE3Interval15MinEntry, nncExtE3FarEndCurrent15MinFEBEs=nncExtE3FarEndCurrent15MinFEBEs, nncExtE3Compliances=nncExtE3Compliances, nncExtE3Interval15MinTable=nncExtE3Interval15MinTable, nncExtE3FarEndTotal24HrFEBEs=nncExtE3FarEndTotal24HrFEBEs, nncExtE3FarEndCurrent15MinGroup=nncExtE3FarEndCurrent15MinGroup, nncExtE3Groups=nncExtE3Groups, nncExtE3FarEndCurrent15MinTable=nncExtE3FarEndCurrent15MinTable, nncExtE3Current15MinEntry=nncExtE3Current15MinEntry, nncExtE3Interval15MinNumber=nncExtE3Interval15MinNumber, nncExtE3Total24HrESs=nncExtE3Total24HrESs, nncExtE3FarEndCurrent15MinESs=nncExtE3FarEndCurrent15MinESs, nncExtE3Interval15MinSESs=nncExtE3Interval15MinSESs, nncExtE3FarEndTotal24HrEntry=nncExtE3FarEndTotal24HrEntry, nncExtE3Current15MinGroup=nncExtE3Current15MinGroup, nncExtE3=nncExtE3, nncExtE3Total24HrGroup=nncExtE3Total24HrGroup, nncExtE3Current15MinSESs=nncExtE3Current15MinSESs, nncExtE3FarEndInterval15MinNumber=nncExtE3FarEndInterval15MinNumber, nncExtE3Current15MinTable=nncExtE3Current15MinTable, nncExtE3Traps=nncExtE3Traps, nncExtE3Interval15MinSEFs=nncExtE3Interval15MinSEFs, nncExtE3Total24HrSESs=nncExtE3Total24HrSESs, nncExtE3FarEndInterval15MinEntry=nncExtE3FarEndInterval15MinEntry, nncExtE3FarEndTotal24HrSESs=nncExtE3FarEndTotal24HrSESs, PYSNMP_MODULE_ID=nncExtE3, nncExtE3Total24HrSEFs=nncExtE3Total24HrSEFs, nncExtE3FarEndInterval15MinTable=nncExtE3FarEndInterval15MinTable, nncExtE3FarEndInterval15MinSESs=nncExtE3FarEndInterval15MinSESs, nncExtE3Total24HrEntry=nncExtE3Total24HrEntry, nncExtE3Total24HrTable=nncExtE3Total24HrTable, nncExtE3FarEndTotal24HrTable=nncExtE3FarEndTotal24HrTable, nncExtE3Compliance=nncExtE3Compliance, nncExtE3FarEndCurrent15MinEntry=nncExtE3FarEndCurrent15MinEntry, nncExtE3FarEndInterval15MinFEBEs=nncExtE3FarEndInterval15MinFEBEs, nncExtE3Objects=nncExtE3Objects)

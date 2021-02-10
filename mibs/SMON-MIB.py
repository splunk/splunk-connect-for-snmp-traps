#
# PySNMP MIB module SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rmon, OwnerString = mibBuilder.importSymbols("RMON-MIB", "rmon", "OwnerString")
probeConfig, rmonConformance, DataSource, LastCreateTime = mibBuilder.importSymbols("RMON2-MIB", "probeConfig", "rmonConformance", "DataSource", "LastCreateTime")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter64, ObjectIdentity, MibIdentifier, Gauge32, NotificationType, iso, Unsigned32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "NotificationType", "iso", "Unsigned32", "Counter32", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
switchRMON = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 22))
if mibBuilder.loadTexts: switchRMON.setLastUpdated('9812160000Z')
if mibBuilder.loadTexts: switchRMON.setOrganization('IETF RMON MIB Working Group')
smonMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1))
dataSourceCaps = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1, 1))
smonStats = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1, 2))
portCopyConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1, 3))
smonRegistrationPoints = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1, 4))
class SmonDataSource(TextualConvention, ObjectIdentifier):
    status = 'current'

smonCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 16, 19, 15), Bits().clone(namedValues=NamedValues(("smonVlanStats", 0), ("smonPrioStats", 1), ("dataSource", 2), ("smonUnusedBit", 3), ("portCopy", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smonCapabilities.setStatus('current')
dataSourceCapsTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1), )
if mibBuilder.loadTexts: dataSourceCapsTable.setStatus('current')
dataSourceCapsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1), ).setIndexNames((1, "SMON-MIB", "dataSourceCapsObject"))
if mibBuilder.loadTexts: dataSourceCapsEntry.setStatus('current')
dataSourceCapsObject = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 1), SmonDataSource())
if mibBuilder.loadTexts: dataSourceCapsObject.setStatus('current')
dataSourceRmonCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("countErrFrames", 0), ("countAllGoodFrames", 1), ("countAnyRmonTables", 2), ("babyGiantsCountAsGood", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSourceRmonCaps.setStatus('current')
dataSourceCopyCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 3), Bits().clone(namedValues=NamedValues(("copySourcePort", 0), ("copyDestPort", 1), ("copySrcTxTraffic", 2), ("copySrcRxTraffic", 3), ("countDestDropEvents", 4), ("copyErrFrames", 5), ("copyUnalteredFrames", 6), ("copyAllGoodFrames", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSourceCopyCaps.setStatus('current')
dataSourceCapsIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSourceCapsIfIndex.setStatus('current')
smonVlanStatsControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1), )
if mibBuilder.loadTexts: smonVlanStatsControlTable.setStatus('current')
smonVlanStatsControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1), ).setIndexNames((0, "SMON-MIB", "smonVlanStatsControlIndex"))
if mibBuilder.loadTexts: smonVlanStatsControlEntry.setStatus('current')
smonVlanStatsControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: smonVlanStatsControlIndex.setStatus('current')
smonVlanStatsControlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 2), DataSource()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonVlanStatsControlDataSource.setStatus('current')
smonVlanStatsControlCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 3), LastCreateTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanStatsControlCreateTime.setStatus('current')
smonVlanStatsControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 4), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonVlanStatsControlOwner.setStatus('current')
smonVlanStatsControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonVlanStatsControlStatus.setStatus('current')
smonVlanIdStatsTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2), )
if mibBuilder.loadTexts: smonVlanIdStatsTable.setStatus('current')
smonVlanIdStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1), ).setIndexNames((0, "SMON-MIB", "smonVlanStatsControlIndex"), (0, "SMON-MIB", "smonVlanIdStatsId"))
if mibBuilder.loadTexts: smonVlanIdStatsEntry.setStatus('current')
smonVlanIdStatsId = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: smonVlanIdStatsId.setStatus('current')
smonVlanIdStatsTotalPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalPkts.setStatus('current')
smonVlanIdStatsTotalOverflowPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalOverflowPkts.setStatus('current')
smonVlanIdStatsTotalHCPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalHCPkts.setStatus('current')
smonVlanIdStatsTotalOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 5), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalOctets.setStatus('current')
smonVlanIdStatsTotalOverflowOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 6), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalOverflowOctets.setStatus('current')
smonVlanIdStatsTotalHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 7), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsTotalHCOctets.setStatus('current')
smonVlanIdStatsNUcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastPkts.setStatus('current')
smonVlanIdStatsNUcastOverflowPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastOverflowPkts.setStatus('current')
smonVlanIdStatsNUcastHCPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 10), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastHCPkts.setStatus('current')
smonVlanIdStatsNUcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 11), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastOctets.setStatus('current')
smonVlanIdStatsNUcastOverflowOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 12), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastOverflowOctets.setStatus('current')
smonVlanIdStatsNUcastHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 13), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsNUcastHCOctets.setStatus('current')
smonVlanIdStatsCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 14), LastCreateTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smonVlanIdStatsCreateTime.setStatus('current')
smonPrioStatsControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3), )
if mibBuilder.loadTexts: smonPrioStatsControlTable.setStatus('current')
smonPrioStatsControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1), ).setIndexNames((0, "SMON-MIB", "smonPrioStatsControlIndex"))
if mibBuilder.loadTexts: smonPrioStatsControlEntry.setStatus('current')
smonPrioStatsControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: smonPrioStatsControlIndex.setStatus('current')
smonPrioStatsControlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 2), DataSource()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonPrioStatsControlDataSource.setStatus('current')
smonPrioStatsControlCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 3), LastCreateTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsControlCreateTime.setStatus('current')
smonPrioStatsControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 4), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonPrioStatsControlOwner.setStatus('current')
smonPrioStatsControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smonPrioStatsControlStatus.setStatus('current')
smonPrioStatsTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4), )
if mibBuilder.loadTexts: smonPrioStatsTable.setStatus('current')
smonPrioStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1), ).setIndexNames((0, "SMON-MIB", "smonPrioStatsControlIndex"), (0, "SMON-MIB", "smonPrioStatsId"))
if mibBuilder.loadTexts: smonPrioStatsEntry.setStatus('current')
smonPrioStatsId = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: smonPrioStatsId.setStatus('current')
smonPrioStatsPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsPkts.setStatus('current')
smonPrioStatsOverflowPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsOverflowPkts.setStatus('current')
smonPrioStatsHCPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsHCPkts.setStatus('current')
smonPrioStatsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 5), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsOctets.setStatus('current')
smonPrioStatsOverflowOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 6), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsOverflowOctets.setStatus('current')
smonPrioStatsHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 7), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: smonPrioStatsHCOctets.setStatus('current')
portCopyTable = MibTable((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1), )
if mibBuilder.loadTexts: portCopyTable.setStatus('current')
portCopyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1), ).setIndexNames((0, "SMON-MIB", "portCopySource"), (0, "SMON-MIB", "portCopyDest"))
if mibBuilder.loadTexts: portCopyEntry.setStatus('current')
portCopySource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: portCopySource.setStatus('current')
portCopyDest = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: portCopyDest.setStatus('current')
portCopyDestDropEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 3), Counter32()).setUnits('events').setMaxAccess("readonly")
if mibBuilder.loadTexts: portCopyDestDropEvents.setStatus('current')
portCopyDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("copyRxOnly", 1), ("copyTxOnly", 2), ("copyBoth", 3))).clone('copyBoth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portCopyDirection.setStatus('current')
portCopyStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portCopyStatus.setStatus('current')
smonVlanDataSource = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 22, 1, 4, 1))
smonMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20, 3))
smonMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20, 4))
smonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 20, 3, 1)).setObjects(("SMON-MIB", "dataSourceCapsGroup"), ("SMON-MIB", "smonVlanStatsGroup"), ("SMON-MIB", "smonPrioStatsGroup"), ("SMON-MIB", "portCopyConfigGroup"), ("SMON-MIB", "smonInformationGroup"), ("SMON-MIB", "smonHcTo100mbGroup"), ("SMON-MIB", "smonHc100mbPlusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonMIBCompliance = smonMIBCompliance.setStatus('current')
smonMIBVlanStatsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 20, 3, 2)).setObjects(("SMON-MIB", "dataSourceCapsGroup"), ("SMON-MIB", "smonVlanStatsGroup"), ("SMON-MIB", "smonInformationGroup"), ("SMON-MIB", "hcVlanTo100mbGroup"), ("SMON-MIB", "hcVlan100mbPlusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonMIBVlanStatsCompliance = smonMIBVlanStatsCompliance.setStatus('current')
smonMIBPrioStatsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 20, 3, 3)).setObjects(("SMON-MIB", "dataSourceCapsGroup"), ("SMON-MIB", "smonPrioStatsGroup"), ("SMON-MIB", "smonInformationGroup"), ("SMON-MIB", "hcPrioTo100mbGroup"), ("SMON-MIB", "hcPrio100mbPlusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonMIBPrioStatsCompliance = smonMIBPrioStatsCompliance.setStatus('current')
portCopyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 20, 3, 4)).setObjects(("SMON-MIB", "dataSourceCapsGroup"), ("SMON-MIB", "portCopyConfigGroup"), ("SMON-MIB", "smonInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portCopyCompliance = portCopyCompliance.setStatus('current')
dataSourceCapsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 1)).setObjects(("SMON-MIB", "dataSourceRmonCaps"), ("SMON-MIB", "dataSourceCopyCaps"), ("SMON-MIB", "dataSourceCapsIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataSourceCapsGroup = dataSourceCapsGroup.setStatus('current')
smonVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 2)).setObjects(("SMON-MIB", "smonVlanStatsControlDataSource"), ("SMON-MIB", "smonVlanStatsControlCreateTime"), ("SMON-MIB", "smonVlanStatsControlOwner"), ("SMON-MIB", "smonVlanStatsControlStatus"), ("SMON-MIB", "smonVlanIdStatsTotalPkts"), ("SMON-MIB", "smonVlanIdStatsTotalOctets"), ("SMON-MIB", "smonVlanIdStatsNUcastPkts"), ("SMON-MIB", "smonVlanIdStatsCreateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonVlanStatsGroup = smonVlanStatsGroup.setStatus('current')
smonPrioStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 3)).setObjects(("SMON-MIB", "smonPrioStatsControlDataSource"), ("SMON-MIB", "smonPrioStatsControlCreateTime"), ("SMON-MIB", "smonPrioStatsControlOwner"), ("SMON-MIB", "smonPrioStatsControlStatus"), ("SMON-MIB", "smonPrioStatsPkts"), ("SMON-MIB", "smonPrioStatsOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonPrioStatsGroup = smonPrioStatsGroup.setStatus('current')
smonHcTo100mbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 4)).setObjects(("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"), ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"), ("SMON-MIB", "smonPrioStatsOverflowOctets"), ("SMON-MIB", "smonPrioStatsHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonHcTo100mbGroup = smonHcTo100mbGroup.setStatus('current')
smonHc100mbPlusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 5)).setObjects(("SMON-MIB", "smonVlanIdStatsTotalOverflowPkts"), ("SMON-MIB", "smonVlanIdStatsTotalHCPkts"), ("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"), ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"), ("SMON-MIB", "smonVlanIdStatsNUcastOverflowPkts"), ("SMON-MIB", "smonVlanIdStatsNUcastHCPkts"), ("SMON-MIB", "smonPrioStatsOverflowPkts"), ("SMON-MIB", "smonPrioStatsHCPkts"), ("SMON-MIB", "smonPrioStatsOverflowOctets"), ("SMON-MIB", "smonPrioStatsHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonHc100mbPlusGroup = smonHc100mbPlusGroup.setStatus('current')
hcVlanTo100mbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 6)).setObjects(("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"), ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcVlanTo100mbGroup = hcVlanTo100mbGroup.setStatus('current')
hcVlan100mbPlusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 7)).setObjects(("SMON-MIB", "smonVlanIdStatsTotalOverflowPkts"), ("SMON-MIB", "smonVlanIdStatsTotalHCPkts"), ("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"), ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"), ("SMON-MIB", "smonVlanIdStatsNUcastOverflowPkts"), ("SMON-MIB", "smonVlanIdStatsNUcastHCPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcVlan100mbPlusGroup = hcVlan100mbPlusGroup.setStatus('current')
hcPrioTo100mbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 8)).setObjects(("SMON-MIB", "smonPrioStatsOverflowOctets"), ("SMON-MIB", "smonPrioStatsHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcPrioTo100mbGroup = hcPrioTo100mbGroup.setStatus('current')
hcPrio100mbPlusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 9)).setObjects(("SMON-MIB", "smonPrioStatsOverflowPkts"), ("SMON-MIB", "smonPrioStatsHCPkts"), ("SMON-MIB", "smonPrioStatsOverflowOctets"), ("SMON-MIB", "smonPrioStatsHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcPrio100mbPlusGroup = hcPrio100mbPlusGroup.setStatus('current')
smonVlanStatsExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 10)).setObjects(("SMON-MIB", "smonVlanIdStatsNUcastOctets"), ("SMON-MIB", "smonVlanIdStatsNUcastOverflowOctets"), ("SMON-MIB", "smonVlanIdStatsNUcastHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonVlanStatsExtGroup = smonVlanStatsExtGroup.setStatus('current')
smonInformationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 11)).setObjects(("SMON-MIB", "smonCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smonInformationGroup = smonInformationGroup.setStatus('current')
portCopyConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 4, 12)).setObjects(("SMON-MIB", "portCopyDestDropEvents"), ("SMON-MIB", "portCopyDirection"), ("SMON-MIB", "portCopyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portCopyConfigGroup = portCopyConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SMON-MIB", dataSourceRmonCaps=dataSourceRmonCaps, smonVlanStatsControlIndex=smonVlanStatsControlIndex, smonPrioStatsPkts=smonPrioStatsPkts, smonVlanIdStatsTable=smonVlanIdStatsTable, smonVlanIdStatsNUcastHCPkts=smonVlanIdStatsNUcastHCPkts, dataSourceCapsObject=dataSourceCapsObject, smonPrioStatsEntry=smonPrioStatsEntry, smonVlanIdStatsId=smonVlanIdStatsId, smonVlanIdStatsTotalOverflowOctets=smonVlanIdStatsTotalOverflowOctets, smonPrioStatsControlDataSource=smonPrioStatsControlDataSource, smonMIBObjects=smonMIBObjects, smonVlanStatsGroup=smonVlanStatsGroup, smonPrioStatsTable=smonPrioStatsTable, smonMIBGroups=smonMIBGroups, dataSourceCapsEntry=dataSourceCapsEntry, smonMIBPrioStatsCompliance=smonMIBPrioStatsCompliance, smonVlanIdStatsNUcastOverflowOctets=smonVlanIdStatsNUcastOverflowOctets, smonVlanIdStatsTotalOverflowPkts=smonVlanIdStatsTotalOverflowPkts, smonVlanIdStatsTotalHCOctets=smonVlanIdStatsTotalHCOctets, smonPrioStatsControlIndex=smonPrioStatsControlIndex, switchRMON=switchRMON, dataSourceCopyCaps=dataSourceCopyCaps, portCopyConfig=portCopyConfig, smonPrioStatsControlStatus=smonPrioStatsControlStatus, smonVlanIdStatsNUcastHCOctets=smonVlanIdStatsNUcastHCOctets, smonVlanIdStatsCreateTime=smonVlanIdStatsCreateTime, portCopyDestDropEvents=portCopyDestDropEvents, portCopyDirection=portCopyDirection, smonMIBVlanStatsCompliance=smonMIBVlanStatsCompliance, dataSourceCapsTable=dataSourceCapsTable, smonVlanIdStatsTotalOctets=smonVlanIdStatsTotalOctets, hcVlanTo100mbGroup=hcVlanTo100mbGroup, portCopyCompliance=portCopyCompliance, smonPrioStatsId=smonPrioStatsId, smonVlanStatsControlTable=smonVlanStatsControlTable, portCopyTable=portCopyTable, smonVlanStatsControlDataSource=smonVlanStatsControlDataSource, smonVlanStatsControlEntry=smonVlanStatsControlEntry, smonVlanIdStatsTotalHCPkts=smonVlanIdStatsTotalHCPkts, smonVlanIdStatsNUcastPkts=smonVlanIdStatsNUcastPkts, smonVlanStatsControlCreateTime=smonVlanStatsControlCreateTime, dataSourceCapsGroup=dataSourceCapsGroup, smonPrioStatsOverflowPkts=smonPrioStatsOverflowPkts, smonPrioStatsControlOwner=smonPrioStatsControlOwner, smonPrioStatsGroup=smonPrioStatsGroup, smonVlanStatsControlStatus=smonVlanStatsControlStatus, smonVlanIdStatsNUcastOverflowPkts=smonVlanIdStatsNUcastOverflowPkts, smonStats=smonStats, smonHcTo100mbGroup=smonHcTo100mbGroup, smonPrioStatsControlTable=smonPrioStatsControlTable, hcVlan100mbPlusGroup=hcVlan100mbPlusGroup, smonVlanIdStatsEntry=smonVlanIdStatsEntry, smonPrioStatsHCPkts=smonPrioStatsHCPkts, portCopyStatus=portCopyStatus, smonHc100mbPlusGroup=smonHc100mbPlusGroup, smonVlanIdStatsTotalPkts=smonVlanIdStatsTotalPkts, smonPrioStatsControlEntry=smonPrioStatsControlEntry, portCopyDest=portCopyDest, hcPrioTo100mbGroup=hcPrioTo100mbGroup, smonVlanDataSource=smonVlanDataSource, smonRegistrationPoints=smonRegistrationPoints, smonPrioStatsOctets=smonPrioStatsOctets, dataSourceCaps=dataSourceCaps, dataSourceCapsIfIndex=dataSourceCapsIfIndex, portCopySource=portCopySource, smonPrioStatsHCOctets=smonPrioStatsHCOctets, hcPrio100mbPlusGroup=hcPrio100mbPlusGroup, portCopyConfigGroup=portCopyConfigGroup, smonInformationGroup=smonInformationGroup, smonMIBCompliances=smonMIBCompliances, smonVlanStatsExtGroup=smonVlanStatsExtGroup, PYSNMP_MODULE_ID=switchRMON, smonPrioStatsControlCreateTime=smonPrioStatsControlCreateTime, smonMIBCompliance=smonMIBCompliance, smonCapabilities=smonCapabilities, smonPrioStatsOverflowOctets=smonPrioStatsOverflowOctets, smonVlanIdStatsNUcastOctets=smonVlanIdStatsNUcastOctets, smonVlanStatsControlOwner=smonVlanStatsControlOwner, SmonDataSource=SmonDataSource, portCopyEntry=portCopyEntry)

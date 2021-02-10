#
# PySNMP MIB module TUBS-IBR-XEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-XEN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, IpAddress, Gauge32, ModuleIdentity, Bits, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "IpAddress", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
xenMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 14))
xenMIB.setRevisions(('2006-02-20 00:00',))
if mibBuilder.loadTexts: xenMIB.setLastUpdated('200602200000Z')
if mibBuilder.loadTexts: xenMIB.setOrganization('TU Braunschweig')
xenObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1))
xenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 2))
xenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3))
class XenDomainState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("running", 2), ("blocked", 3), ("paused", 4), ("crashed", 5), ("dying", 6), ("shutdown", 7))

xenHost = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1))
xenHostXenVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostXenVersion.setStatus('current')
xenHostTotalMemKBytes = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostTotalMemKBytes.setStatus('current')
xenHostCPUs = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUs.setStatus('current')
xenHostCPUMHz = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUMHz.setStatus('current')
xenDomainTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2), )
if mibBuilder.loadTexts: xenDomainTable.setStatus('current')
xenDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"))
if mibBuilder.loadTexts: xenDomainEntry.setStatus('current')
xenDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: xenDomainName.setStatus('current')
xenDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 2), XenDomainState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainState.setStatus('current')
xenDomainMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMemKBytes.setStatus('current')
xenDomainMaxMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMaxMemKBytes.setStatus('current')
xenVCPUTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3), )
if mibBuilder.loadTexts: xenVCPUTable.setStatus('current')
xenVCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenVCPUIndex"))
if mibBuilder.loadTexts: xenVCPUEntry.setStatus('current')
xenVCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: xenVCPUIndex.setStatus('current')
xenVCPUMilliseconds = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenVCPUMilliseconds.setStatus('current')
xenNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4), )
if mibBuilder.loadTexts: xenNetworkTable.setStatus('current')
xenNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenNetworkIndex"))
if mibBuilder.loadTexts: xenNetworkEntry.setStatus('current')
xenNetworkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: xenNetworkIndex.setStatus('current')
xenNetworkInKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInKBytes.setStatus('current')
xenNetworkInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInPkts.setStatus('current')
xenNetworkInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInErrors.setStatus('current')
xenNetworkInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInDiscards.setStatus('current')
xenNetworkOutKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutKBytes.setStatus('current')
xenNetworkOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutPkts.setStatus('current')
xenNetworkOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutErrors.setStatus('current')
xenNetworkOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutDiscards.setStatus('current')
xenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1))
xenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2))
xenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1, 1)).setObjects(("TUBS-IBR-XEN-MIB", "xenGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xenCompliance = xenCompliance.setStatus('current')
xenGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2, 1)).setObjects(("TUBS-IBR-XEN-MIB", "xenHostXenVersion"), ("TUBS-IBR-XEN-MIB", "xenHostTotalMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenHostCPUs"), ("TUBS-IBR-XEN-MIB", "xenHostCPUMHz"), ("TUBS-IBR-XEN-MIB", "xenDomainState"), ("TUBS-IBR-XEN-MIB", "xenDomainMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenDomainMaxMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenVCPUMilliseconds"), ("TUBS-IBR-XEN-MIB", "xenNetworkInKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkInPkts"), ("TUBS-IBR-XEN-MIB", "xenNetworkInErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkInDiscards"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutPkts"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xenGeneralGroup = xenGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", xenMIB=xenMIB, xenNetworkTable=xenNetworkTable, xenHostXenVersion=xenHostXenVersion, xenHostCPUs=xenHostCPUs, xenGeneralGroup=xenGeneralGroup, xenConformance=xenConformance, xenObjects=xenObjects, xenVCPUMilliseconds=xenVCPUMilliseconds, xenCompliance=xenCompliance, xenNetworkInKBytes=xenNetworkInKBytes, xenCompliances=xenCompliances, XenDomainState=XenDomainState, xenVCPUTable=xenVCPUTable, xenNetworkOutErrors=xenNetworkOutErrors, xenGroups=xenGroups, xenDomainMemKBytes=xenDomainMemKBytes, xenDomainState=xenDomainState, xenNetworkEntry=xenNetworkEntry, xenHostCPUMHz=xenHostCPUMHz, xenNetworkInErrors=xenNetworkInErrors, xenDomainMaxMemKBytes=xenDomainMaxMemKBytes, xenVCPUIndex=xenVCPUIndex, xenNetworkOutDiscards=xenNetworkOutDiscards, PYSNMP_MODULE_ID=xenMIB, xenNetworkOutKBytes=xenNetworkOutKBytes, xenNetworkOutPkts=xenNetworkOutPkts, xenNetworkIndex=xenNetworkIndex, xenVCPUEntry=xenVCPUEntry, xenDomainTable=xenDomainTable, xenHostTotalMemKBytes=xenHostTotalMemKBytes, xenHost=xenHost, xenDomainEntry=xenDomainEntry, xenNetworkInDiscards=xenNetworkInDiscards, xenDomainName=xenDomainName, xenTraps=xenTraps, xenNetworkInPkts=xenNetworkInPkts)

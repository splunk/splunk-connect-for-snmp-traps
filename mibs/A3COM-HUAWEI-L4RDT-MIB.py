#
# PySNMP MIB module A3COM-HUAWEI-L4RDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-L4RDT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, IpAddress, iso, ObjectIdentity, Counter64, ModuleIdentity, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Unsigned32", "MibIdentifier")
RowStatus, MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
h3cL4Redirect = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10))
if mibBuilder.loadTexts: h3cL4Redirect.setLastUpdated('200409210000Z')
if mibBuilder.loadTexts: h3cL4Redirect.setOrganization('Huawei 3Com Tech, Inc.')
h3cL4RedirectCacheTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1), )
if mibBuilder.loadTexts: h3cL4RedirectCacheTable.setStatus('current')
h3cL4RedirectCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectCacheIpAddress"))
if mibBuilder.loadTexts: h3cL4RedirectCacheEntry.setStatus('current')
h3cL4RedirectCacheIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cL4RedirectCacheIpAddress.setStatus('current')
h3cL4RedirectCacheRedirectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabledNotRedirecting", 1), ("enabledNoHealthChecker", 2), ("enabledHealthChecking", 3), ("enabledHealthCheckOKNotRedirecting", 4), ("enabledHealthCheckFailed", 5), ("enabledRedirecting", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectCacheRedirectionStatus.setStatus('current')
h3cL4RedirectCachePort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCachePort.setStatus('current')
h3cL4RedirectCacheRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheRowStatus.setStatus('current')
h3cL4RedirectCacheMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheMacAddress.setStatus('current')
h3cL4RedirectCacheVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheVlan.setStatus('current')
h3cL4RedirectCacheTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheTcpPort.setStatus('current')
h3cL4RedirectIpExclusionTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2), )
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionTable.setStatus('current')
h3cL4RedirectIpExclusionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectIpExclusionIpAddress"))
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionEntry.setStatus('current')
h3cL4RedirectIpExclusionIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionIpAddress.setStatus('current')
h3cL4RedirectIpExclusionMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionMaskLen.setStatus('current')
h3cL4RedirectIpExclusionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionRowStatus.setStatus('current')
h3cL4RedirectVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3), )
if mibBuilder.loadTexts: h3cL4RedirectVlanTable.setStatus('current')
h3cL4RedirectVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectVlanID"))
if mibBuilder.loadTexts: h3cL4RedirectVlanEntry.setStatus('current')
h3cL4RedirectVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cL4RedirectVlanID.setStatus('current')
h3cL4RedirectVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectVlanRowStatus.setStatus('current')
h3cL4RedirectInformationString = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectInformationString.setStatus('current')
h3cL4RedirectFreeCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeCacheEntries.setStatus('current')
h3cL4RedirectFreeIpExclusionEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeIpExclusionEntries.setStatus('current')
h3cL4RedirectFreeVlanEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeVlanEntries.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-L4RDT-MIB", h3cL4RedirectCacheVlan=h3cL4RedirectCacheVlan, h3cL4RedirectIpExclusionEntry=h3cL4RedirectIpExclusionEntry, h3cL4RedirectIpExclusionRowStatus=h3cL4RedirectIpExclusionRowStatus, h3cL4RedirectCacheMacAddress=h3cL4RedirectCacheMacAddress, h3cL4RedirectCacheIpAddress=h3cL4RedirectCacheIpAddress, h3cL4RedirectFreeVlanEntries=h3cL4RedirectFreeVlanEntries, h3cL4RedirectInformationString=h3cL4RedirectInformationString, h3cL4RedirectVlanEntry=h3cL4RedirectVlanEntry, h3cL4RedirectFreeCacheEntries=h3cL4RedirectFreeCacheEntries, h3cL4RedirectVlanID=h3cL4RedirectVlanID, h3cL4Redirect=h3cL4Redirect, h3cL4RedirectCachePort=h3cL4RedirectCachePort, h3cL4RedirectIpExclusionMaskLen=h3cL4RedirectIpExclusionMaskLen, h3cL4RedirectCacheEntry=h3cL4RedirectCacheEntry, h3cL4RedirectCacheTable=h3cL4RedirectCacheTable, PYSNMP_MODULE_ID=h3cL4Redirect, h3cL4RedirectIpExclusionIpAddress=h3cL4RedirectIpExclusionIpAddress, h3cL4RedirectCacheTcpPort=h3cL4RedirectCacheTcpPort, h3cL4RedirectFreeIpExclusionEntries=h3cL4RedirectFreeIpExclusionEntries, h3cL4RedirectCacheRowStatus=h3cL4RedirectCacheRowStatus, h3cL4RedirectIpExclusionTable=h3cL4RedirectIpExclusionTable, h3cL4RedirectCacheRedirectionStatus=h3cL4RedirectCacheRedirectionStatus, h3cL4RedirectVlanTable=h3cL4RedirectVlanTable, h3cL4RedirectVlanRowStatus=h3cL4RedirectVlanRowStatus)

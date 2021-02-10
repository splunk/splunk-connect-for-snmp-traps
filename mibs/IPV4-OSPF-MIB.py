#
# PySNMP MIB module IPV4-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4-OSPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Ospf, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Ospf")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, IpAddress, TimeTicks, Bits, ModuleIdentity, Counter64, MibIdentifier, NotificationType, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "IpAddress", "TimeTicks", "Bits", "ModuleIdentity", "Counter64", "MibIdentifier", "NotificationType", "iso", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
apIpv4OspfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 1))
if mibBuilder.loadTexts: apIpv4OspfMib.setLastUpdated('9805112000Z')
if mibBuilder.loadTexts: apIpv4OspfMib.setOrganization('ArrowPoint Communications Inc.')
apIpv4OspfRedistributeLocal = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRedistributeLocal.setStatus('current')
apIpv4OspfLocalType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfLocalType.setStatus('current')
apIpv4OspfLocalMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfLocalMetric.setStatus('current')
apIpv4OspfLocalTag = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfLocalTag.setStatus('current')
apIpv4OspfRedistributeStatic = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRedistributeStatic.setStatus('current')
apIpv4OspfStaticType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfStaticType.setStatus('current')
apIpv4OspfStaticMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfStaticMetric.setStatus('current')
apIpv4OspfStaticTag = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfStaticTag.setStatus('current')
apIpv4OspfRedistributeRip = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRedistributeRip.setStatus('current')
apIpv4OspfRipType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRipType.setStatus('current')
apIpv4OspfRipMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRipMetric.setStatus('current')
apIpv4OspfRipTag = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRipTag.setStatus('current')
apIpv4OspfOriginateDefault = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfOriginateDefault.setStatus('current')
apIpv4OspfDefaultType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfDefaultType.setStatus('current')
apIpv4OspfDefaultMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfDefaultMetric.setStatus('current')
apIpv4OspfDefaultTag = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfDefaultTag.setStatus('current')
apIpv4OspfRedistributeFirewall = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfRedistributeFirewall.setStatus('current')
apIpv4OspfFirewallType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfFirewallType.setStatus('current')
apIpv4OspfFirewallMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfFirewallMetric.setStatus('current')
apIpv4OspfFirewallTag = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfFirewallTag.setStatus('current')
apIpv4OspfAdvRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22), )
if mibBuilder.loadTexts: apIpv4OspfAdvRouteTable.setStatus('current')
apIpv4OspfAdvRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1), ).setIndexNames((0, "IPV4-OSPF-MIB", "apIpv4OspfAdvRoutePrefix"), (0, "IPV4-OSPF-MIB", "apIpv4OspfAdvRoutePrefixLen"))
if mibBuilder.loadTexts: apIpv4OspfAdvRouteEntry.setStatus('current')
apIpv4OspfAdvRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4OspfAdvRoutePrefix.setStatus('current')
apIpv4OspfAdvRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4OspfAdvRoutePrefixLen.setStatus('current')
apIpv4OspfAdvRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfAdvRouteType.setStatus('current')
apIpv4OspfAdvRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfAdvRouteMetric.setStatus('current')
apIpv4OspfAdvRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfAdvRouteTag.setStatus('current')
apIpv4OspfAdvRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfAdvRouteStatus.setStatus('current')
apIpv4OspfIfAdvRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23), )
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteTable.setStatus('current')
apIpv4OspfIfAdvRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1), ).setIndexNames((0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRouteAddress"), (0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRoutePrefix"), (0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRoutePrefixLen"))
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteEntry.setStatus('current')
apIpv4OspfIfAdvRouteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteAddress.setStatus('current')
apIpv4OspfIfAdvRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRoutePrefix.setStatus('current')
apIpv4OspfIfAdvRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRoutePrefixLen.setStatus('current')
apIpv4OspfIfAdvRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aseType1", 1), ("aseType2", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteType.setStatus('current')
apIpv4OspfIfAdvRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteMetric.setStatus('current')
apIpv4OspfIfAdvRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteTag.setStatus('current')
apIpv4OspfIfAdvRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4OspfIfAdvRouteStatus.setStatus('current')
apIpv4OspfEqualCostRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OspfEqualCostRoutes.setStatus('current')
mibBuilder.exportSymbols("IPV4-OSPF-MIB", apIpv4OspfIfAdvRouteTag=apIpv4OspfIfAdvRouteTag, apIpv4OspfIfAdvRoutePrefixLen=apIpv4OspfIfAdvRoutePrefixLen, apIpv4OspfOriginateDefault=apIpv4OspfOriginateDefault, apIpv4OspfAdvRouteStatus=apIpv4OspfAdvRouteStatus, apIpv4OspfLocalMetric=apIpv4OspfLocalMetric, apIpv4OspfRedistributeStatic=apIpv4OspfRedistributeStatic, apIpv4OspfRedistributeFirewall=apIpv4OspfRedistributeFirewall, apIpv4OspfMib=apIpv4OspfMib, apIpv4OspfAdvRoutePrefixLen=apIpv4OspfAdvRoutePrefixLen, PYSNMP_MODULE_ID=apIpv4OspfMib, apIpv4OspfDefaultMetric=apIpv4OspfDefaultMetric, apIpv4OspfAdvRouteType=apIpv4OspfAdvRouteType, apIpv4OspfRipMetric=apIpv4OspfRipMetric, apIpv4OspfIfAdvRouteType=apIpv4OspfIfAdvRouteType, apIpv4OspfLocalType=apIpv4OspfLocalType, apIpv4OspfStaticTag=apIpv4OspfStaticTag, apIpv4OspfDefaultTag=apIpv4OspfDefaultTag, apIpv4OspfRedistributeLocal=apIpv4OspfRedistributeLocal, apIpv4OspfAdvRoutePrefix=apIpv4OspfAdvRoutePrefix, apIpv4OspfIfAdvRouteAddress=apIpv4OspfIfAdvRouteAddress, apIpv4OspfAdvRouteTable=apIpv4OspfAdvRouteTable, apIpv4OspfFirewallTag=apIpv4OspfFirewallTag, apIpv4OspfIfAdvRouteEntry=apIpv4OspfIfAdvRouteEntry, apIpv4OspfIfAdvRoutePrefix=apIpv4OspfIfAdvRoutePrefix, apIpv4OspfFirewallMetric=apIpv4OspfFirewallMetric, apIpv4OspfRipType=apIpv4OspfRipType, apIpv4OspfFirewallType=apIpv4OspfFirewallType, apIpv4OspfStaticMetric=apIpv4OspfStaticMetric, apIpv4OspfIfAdvRouteTable=apIpv4OspfIfAdvRouteTable, apIpv4OspfIfAdvRouteMetric=apIpv4OspfIfAdvRouteMetric, apIpv4OspfStaticType=apIpv4OspfStaticType, apIpv4OspfAdvRouteTag=apIpv4OspfAdvRouteTag, apIpv4OspfDefaultType=apIpv4OspfDefaultType, apIpv4OspfLocalTag=apIpv4OspfLocalTag, apIpv4OspfEqualCostRoutes=apIpv4OspfEqualCostRoutes, apIpv4OspfAdvRouteMetric=apIpv4OspfAdvRouteMetric, apIpv4OspfRipTag=apIpv4OspfRipTag, apIpv4OspfAdvRouteEntry=apIpv4OspfAdvRouteEntry, apIpv4OspfRedistributeRip=apIpv4OspfRedistributeRip, apIpv4OspfIfAdvRouteStatus=apIpv4OspfIfAdvRouteStatus)

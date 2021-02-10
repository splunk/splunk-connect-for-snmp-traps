#
# PySNMP MIB module IPFRR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFRR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
inetCidrRoutePfxLen, inetCidrRouteDestType, inetCidrRouteNextHop, inetCidrRoutePolicy, inetCidrRouteNextHopType, inetCidrRouteDest = mibBuilder.importSymbols("IP-FORWARD-MIB", "inetCidrRoutePfxLen", "inetCidrRouteDestType", "inetCidrRouteNextHop", "inetCidrRoutePolicy", "inetCidrRouteNextHopType", "inetCidrRouteDest")
ip, = mibBuilder.importSymbols("IP-MIB", "ip")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Counter64, Gauge32, Integer32, Bits, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Counter64", "Gauge32", "Integer32", "Bits", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ipFrrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 4, 999))
ipFrrMIB.setRevisions(('2005-02-18 12:00', '2005-02-13 12:00',))
if mibBuilder.loadTexts: ipFrrMIB.setLastUpdated('200502181200Z')
if mibBuilder.loadTexts: ipFrrMIB.setOrganization('draft-ietf-ipfrr-ip-mib-00.txt')
ipFrrMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 999, 1))
ipFrrProtectStats = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 999, 1, 1))
ipFrrTotalRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrTotalRoutes.setStatus('current')
ipFrrUnprotectedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrUnprotectedRoutes.setStatus('current')
ipFrrProtectedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrProtectedRoutes.setStatus('current')
ipFrrLinkProtectedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrLinkProtectedRoutes.setStatus('current')
ipFrrNodeProtectedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrNodeProtectedRoutes.setStatus('current')
ipFrrAltTable = MibTable((1, 3, 6, 1, 2, 1, 4, 999, 1, 2), )
if mibBuilder.loadTexts: ipFrrAltTable.setStatus('current')
ipFrrAltEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1), ).setIndexNames((0, "IP-FORWARD-MIB", "inetCidrRouteDestType"), (0, "IP-FORWARD-MIB", "inetCidrRouteDest"), (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"), (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"), (0, "IPFRR-MIB", "ipFrrAltNextHopType"), (0, "IPFRR-MIB", "ipFrrAltNextHop"))
if mibBuilder.loadTexts: ipFrrAltEntry.setStatus('current')
ipFrrAltNextHopType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: ipFrrAltNextHopType.setStatus('current')
ipFrrAltNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: ipFrrAltNextHop.setStatus('current')
ipFrrAltIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipFrrAltIfIndex.setStatus('current')
ipFrrAltType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("equalCost", 2), ("loopFree", 3), ("uTurn", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipFrrAltType.setStatus('current')
ipFrrAltProtectionAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("nodeProtect", 0), ("linkProtect", 1), ("unknownProtection", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipFrrAltProtectionAvailable.setStatus('current')
ipFrrAltMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipFrrAltMetric1.setStatus('current')
ipFrrAltStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipFrrAltStatus.setStatus('current')
ipFrrNoAltTable = MibTable((1, 3, 6, 1, 2, 1, 4, 999, 1, 3), )
if mibBuilder.loadTexts: ipFrrNoAltTable.setStatus('current')
ipFrrNoAltEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 999, 1, 3, 1), ).setIndexNames((0, "IP-FORWARD-MIB", "inetCidrRouteDestType"), (0, "IP-FORWARD-MIB", "inetCidrRouteDest"), (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"))
if mibBuilder.loadTexts: ipFrrNoAltEntry.setStatus('current')
ipFrrNoAltCause = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 999, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ipFrrUnavailable", 1), ("localAddress", 2), ("ipFrrDisabled", 3), ("ipFrrUturnDisabled", 4), ("other", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFrrNoAltCause.setStatus('current')
ipFrrMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 999, 2))
ipFrrMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 999, 2, 1))
ipFrrMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 999, 2, 2))
ipFrrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 1)).setObjects(("IPFRR-MIB", "ipFrrBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipFrrMIBCompliance = ipFrrMIBCompliance.setStatus('deprecated')
ipFrrMIBInetCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 2)).setObjects(("IPFRR-MIB", "ipFrrBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipFrrMIBInetCompliance = ipFrrMIBInetCompliance.setStatus('current')
ipFrrReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 3)).setObjects(("IPFRR-MIB", "ipFrrBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipFrrReadOnlyCompliance = ipFrrReadOnlyCompliance.setStatus('current')
ipFrrBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 999, 2, 2, 1)).setObjects(("IPFRR-MIB", "ipFrrTotalRoutes"), ("IPFRR-MIB", "ipFrrUnprotectedRoutes"), ("IPFRR-MIB", "ipFrrProtectedRoutes"), ("IPFRR-MIB", "ipFrrLinkProtectedRoutes"), ("IPFRR-MIB", "ipFrrNodeProtectedRoutes"), ("IPFRR-MIB", "ipFrrAltIfIndex"), ("IPFRR-MIB", "ipFrrAltType"), ("IPFRR-MIB", "ipFrrAltProtectionAvailable"), ("IPFRR-MIB", "ipFrrAltMetric1"), ("IPFRR-MIB", "ipFrrAltStatus"), ("IPFRR-MIB", "ipFrrNoAltCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipFrrBasicGroup = ipFrrBasicGroup.setStatus('current')
mibBuilder.exportSymbols("IPFRR-MIB", ipFrrAltTable=ipFrrAltTable, ipFrrMIBObjects=ipFrrMIBObjects, ipFrrAltIfIndex=ipFrrAltIfIndex, ipFrrProtectStats=ipFrrProtectStats, ipFrrProtectedRoutes=ipFrrProtectedRoutes, ipFrrAltProtectionAvailable=ipFrrAltProtectionAvailable, ipFrrNoAltTable=ipFrrNoAltTable, ipFrrMIBConformance=ipFrrMIBConformance, ipFrrTotalRoutes=ipFrrTotalRoutes, ipFrrMIBGroups=ipFrrMIBGroups, ipFrrNoAltEntry=ipFrrNoAltEntry, ipFrrBasicGroup=ipFrrBasicGroup, ipFrrAltStatus=ipFrrAltStatus, ipFrrNodeProtectedRoutes=ipFrrNodeProtectedRoutes, ipFrrUnprotectedRoutes=ipFrrUnprotectedRoutes, PYSNMP_MODULE_ID=ipFrrMIB, ipFrrMIBCompliance=ipFrrMIBCompliance, ipFrrMIBCompliances=ipFrrMIBCompliances, ipFrrNoAltCause=ipFrrNoAltCause, ipFrrAltEntry=ipFrrAltEntry, ipFrrAltType=ipFrrAltType, ipFrrMIBInetCompliance=ipFrrMIBInetCompliance, ipFrrReadOnlyCompliance=ipFrrReadOnlyCompliance, ipFrrAltMetric1=ipFrrAltMetric1, ipFrrLinkProtectedRoutes=ipFrrLinkProtectedRoutes, ipFrrAltNextHop=ipFrrAltNextHop, ipFrrMIB=ipFrrMIB, ipFrrAltNextHopType=ipFrrAltNextHopType)

#
# PySNMP MIB module MITEL-ROUTERGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-ROUTERGROUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Integer32, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Unsigned32, TimeTicks, MibIdentifier, iso, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Integer32", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
mitelRouterIpRouterGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5))
mitelRouterIpRouterGroup.setRevisions(('2003-03-24 10:45', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setLastUpdated('200303241045Z')
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1), )
if mibBuilder.loadTexts: mitelIpRouteTable.setStatus('current')
mitelIpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1), ).setIndexNames((0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblDestAddress"), (0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblGateAddress"))
if mibBuilder.loadTexts: mitelIpRouteEntry.setStatus('current')
mitelIpRouteTblDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblDestAddress.setStatus('current')
mitelIpRouteTblGateAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblGateAddress.setStatus('current')
mitelIpRouteTblNetmaskAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblNetmaskAddress.setStatus('current')
mitelIpRouteTblIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblIfIndex.setStatus('current')
mitelIpRouteTblMetric1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric1.setStatus('current')
mitelIpRouteTblMetric2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric2.setStatus('current')
mitelIpRouteTblMetric3 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric3.setStatus('current')
mitelIpRouteTblMetric4 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric4.setStatus('current')
mitelIpRouteTblMetric5 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric5.setStatus('current')
mitelIpRouteTblRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteType.setStatus('current')
mitelIpRouteTblRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteProto.setStatus('current')
mitelIpRouteTblRouteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteAge.setStatus('current')
mitelIpRouteTblBlockLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblBlockLearning.setStatus('current')
mitelIpRouteTblInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblInUse.setStatus('current')
mitelIpRouteTblDisableLearned = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblDisableLearned.setStatus('current')
mitelIpRouteTblConvertStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblConvertStatic.setStatus('current')
mitelIpRouteTblRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIpRouteTblRowStatus.setStatus('current')
mibBuilder.exportSymbols("MITEL-ROUTERGROUP-MIB", mitelIpRouteTblDisableLearned=mitelIpRouteTblDisableLearned, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitelIpRouteTblDestAddress=mitelIpRouteTblDestAddress, mitelIpRouteTblMetric3=mitelIpRouteTblMetric3, mitelIpRouteTblBlockLearning=mitelIpRouteTblBlockLearning, mitelIpRouteTblConvertStatic=mitelIpRouteTblConvertStatic, mitelIpRouteTblRouteAge=mitelIpRouteTblRouteAge, mitelIpRouteTblRouteProto=mitelIpRouteTblRouteProto, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpRouteTblMetric5=mitelIpRouteTblMetric5, mitelIpRouteTblNetmaskAddress=mitelIpRouteTblNetmaskAddress, mitelIpRouteTblMetric2=mitelIpRouteTblMetric2, mitelIpRouteTblInUse=mitelIpRouteTblInUse, mitelIpRouteTblGateAddress=mitelIpRouteTblGateAddress, mitelIpRouteTblRowStatus=mitelIpRouteTblRowStatus, mitelIpRouteTblMetric4=mitelIpRouteTblMetric4, mitelIpRouteEntry=mitelIpRouteEntry, PYSNMP_MODULE_ID=mitelRouterIpRouterGroup, mitelIpRouteTblRouteType=mitelIpRouteTblRouteType, mitelIpRouteTable=mitelIpRouteTable, mitelIpNetRouter=mitelIpNetRouter, mitelIpRouteTblIfIndex=mitelIpRouteTblIfIndex, mitelIpRouteTblMetric1=mitelIpRouteTblMetric1, mitelProprietary=mitelProprietary, mitel=mitel)

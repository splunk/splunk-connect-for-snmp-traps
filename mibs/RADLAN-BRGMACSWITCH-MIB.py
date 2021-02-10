#
# PySNMP MIB module RADLAN-BRGMACSWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-BRGMACSWITCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:37:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Integer32, Counter64, iso, Counter32, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Integer32", "Counter64", "iso", "Counter32", "IpAddress", "ModuleIdentity", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlBrgMacSwitch = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 50))
rlBrgMacSwitch.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlBrgMacSwitch.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlBrgMacSwitch.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlBrgMacSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwVersion.setStatus('current')
rlBrgMacSwMaxTableNumber = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwMaxTableNumber.setStatus('current')
rlBrgMacSwDynamicTables = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwDynamicTables.setStatus('current')
rlBrgMacSwOldEntryDeleteMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("refreshFlag", 1), ("agingFlag", 2), ("agingTime", 3), ("boundaries", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwOldEntryDeleteMode.setStatus('current')
rlBrgMacSwSpanningTree = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwSpanningTree.setStatus('current')
rlBrgMacSwKeyType = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("macOnly", 1), ("tagAndMac", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwKeyType.setStatus('current')
rlBrgMacSwYellowBoundary = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMacSwYellowBoundary.setStatus('current')
rlBrgMacSwRedBoundary = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMacSwRedBoundary.setStatus('current')
rlBrgMacSwTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMacSwTrapEnable.setStatus('current')
rlBrgMacSwOperTrapCount = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMacSwOperTrapCount.setStatus('current')
rlBrgMacSwAdminTrapFrequency = MibScalar((1, 3, 6, 1, 4, 1, 89, 50, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMacSwAdminTrapFrequency.setStatus('current')
mibBuilder.exportSymbols("RADLAN-BRGMACSWITCH-MIB", rlBrgMacSwMaxTableNumber=rlBrgMacSwMaxTableNumber, rlBrgMacSwSpanningTree=rlBrgMacSwSpanningTree, rlBrgMacSwitch=rlBrgMacSwitch, rlBrgMacSwAdminTrapFrequency=rlBrgMacSwAdminTrapFrequency, rlBrgMacSwOldEntryDeleteMode=rlBrgMacSwOldEntryDeleteMode, rlBrgMacSwKeyType=rlBrgMacSwKeyType, PYSNMP_MODULE_ID=rlBrgMacSwitch, rlBrgMacSwYellowBoundary=rlBrgMacSwYellowBoundary, rlBrgMacSwRedBoundary=rlBrgMacSwRedBoundary, rlBrgMacSwOperTrapCount=rlBrgMacSwOperTrapCount, rlBrgMacSwTrapEnable=rlBrgMacSwTrapEnable, rlBrgMacSwDynamicTables=rlBrgMacSwDynamicTables, rlBrgMacSwVersion=rlBrgMacSwVersion)
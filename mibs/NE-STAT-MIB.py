#
# PySNMP MIB module NE-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NE-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
allotCom, = mibBuilder.importSymbols("COMPANY-MIB", "allotCom")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, iso, ObjectIdentity, TimeTicks, IpAddress, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
neStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 2603, 1))
if mibBuilder.loadTexts: neStatistics.setLastUpdated('0103130000Z')
if mibBuilder.loadTexts: neStatistics.setOrganization('Allot Communications')
neStatMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 1))
neStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1))
neByteCountIn = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neByteCountIn.setStatus('current')
neByteCountOut = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neByteCountOut.setStatus('current')
neByteCountTotal = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neByteCountTotal.setStatus('current')
neLiveConnections = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neLiveConnections.setStatus('current')
neNewConnections = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neNewConnections.setStatus('current')
nePacketsIn = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nePacketsIn.setStatus('current')
nePacketsOut = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nePacketsOut.setStatus('current')
nePacketsTotal = MibScalar((1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nePacketsTotal.setStatus('current')
neByteCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2603, 1, 1, 2)).setObjects(("NE-STAT-MIB", "neByteCountIn"), ("NE-STAT-MIB", "neByteCountOut"), ("NE-STAT-MIB", "neByteCountTotal"), ("NE-STAT-MIB", "neLiveConnections"), ("NE-STAT-MIB", "neNewConnections"), ("NE-STAT-MIB", "nePacketsIn"), ("NE-STAT-MIB", "nePacketsOut"), ("NE-STAT-MIB", "nePacketsTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neByteCountersGroup = neByteCountersGroup.setStatus('current')
mibBuilder.exportSymbols("NE-STAT-MIB", neLiveConnections=neLiveConnections, nePacketsOut=nePacketsOut, nePacketsIn=nePacketsIn, neByteCountOut=neByteCountOut, PYSNMP_MODULE_ID=neStatistics, neStatistics=neStatistics, neByteCountersGroup=neByteCountersGroup, neNewConnections=neNewConnections, neStat=neStat, neStatMIB=neStatMIB, neByteCountIn=neByteCountIn, neByteCountTotal=neByteCountTotal, nePacketsTotal=nePacketsTotal)

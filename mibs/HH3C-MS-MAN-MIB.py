#
# PySNMP MIB module HH3C-MS-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MS-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hh3cSurveillanceMIB, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cSurveillanceMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, iso, ObjectIdentity, Counter64, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cMSMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 9, 3))
if mibBuilder.loadTexts: hh3cMSMan.setLastUpdated('200708130000Z')
if mibBuilder.loadTexts: hh3cMSMan.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cMSManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 3, 1))
hh3cMSStatisticalPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 9, 3, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMSStatisticalPeriod.setStatus('current')
hh3cMSManMIBTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2))
hh3cMSForwardTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1), )
if mibBuilder.loadTexts: hh3cMSForwardTable.setStatus('current')
hh3cMSForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1), ).setIndexNames((0, "HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"))
if mibBuilder.loadTexts: hh3cMSForwardEntry.setStatus('current')
hh3cMSForwardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMSForwardIndex.setStatus('current')
hh3cMSForwardMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSForwardMaxConnection.setStatus('current')
hh3cMSForwardConnectionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMSForwardConnectionThreshold.setStatus('current')
hh3cMSCurrentForwardConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSCurrentForwardConnection.setStatus('current')
hh3cMSPeriodForwardConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSPeriodForwardConnection.setStatus('current')
hh3cMSForwardTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSForwardTotalTime.setStatus('current')
hh3cMSForwardTotalConn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSForwardTotalConn.setStatus('current')
hh3cMSVODTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2), )
if mibBuilder.loadTexts: hh3cMSVODTable.setStatus('current')
hh3cMSVODEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1), ).setIndexNames((0, "HH3C-MS-MAN-MIB", "hh3cMSVODIndex"))
if mibBuilder.loadTexts: hh3cMSVODEntry.setStatus('current')
hh3cMSVODIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMSVODIndex.setStatus('current')
hh3cMSVODMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSVODMaxConnection.setStatus('current')
hh3cMSVODConnectionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMSVODConnectionThreshold.setStatus('current')
hh3cMSCurrentVODConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSCurrentVODConnection.setStatus('current')
hh3cMSPeriodVODMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSPeriodVODMaxConnection.setStatus('current')
hh3cMSVODTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSVODTotalTime.setStatus('current')
hh3cMSVODTotalConn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSVODTotalConn.setStatus('current')
hh3cMSRecordTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3), )
if mibBuilder.loadTexts: hh3cMSRecordTable.setStatus('current')
hh3cMSRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1), ).setIndexNames((0, "HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"))
if mibBuilder.loadTexts: hh3cMSRecordEntry.setStatus('current')
hh3cMSRecordIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMSRecordIndex.setStatus('current')
hh3cMSRecordMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSRecordMaxConnection.setStatus('current')
hh3cMSRecordConnectionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMSRecordConnectionThreshold.setStatus('current')
hh3cMSCurrentRecordConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSCurrentRecordConnection.setStatus('current')
hh3cMSPeriodRecordMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSPeriodRecordMaxConnection.setStatus('current')
hh3cMSRecordTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSRecordTotalTime.setStatus('current')
hh3cMSRecordTotalConn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMSRecordTotalConn.setStatus('current')
hh3cMSManMIBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3))
hh3cMSManTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0))
hh3cMSManVODConnectionThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 1)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSVODIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentVODConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSVODConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManVODConnectionThresholdTrap.setStatus('current')
hh3cMSManVODConnectionRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 2)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSVODIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentVODConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSVODConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManVODConnectionRecoverTrap.setStatus('current')
hh3cMSManForwardConnectionThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 3)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentForwardConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSForwardConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManForwardConnectionThresholdTrap.setStatus('current')
hh3cMSManForwardConnectionRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 4)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentForwardConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSForwardConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManForwardConnectionRecoverTrap.setStatus('current')
hh3cMSManRecordConnectionThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 5)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentRecordConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSRecordConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManRecordConnectionThresholdTrap.setStatus('current')
hh3cMSManRecordConnectionRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 6)).setObjects(("HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"), ("HH3C-MS-MAN-MIB", "hh3cMSCurrentRecordConnection"), ("HH3C-MS-MAN-MIB", "hh3cMSRecordConnectionThreshold"))
if mibBuilder.loadTexts: hh3cMSManRecordConnectionRecoverTrap.setStatus('current')
mibBuilder.exportSymbols("HH3C-MS-MAN-MIB", hh3cMSForwardConnectionThreshold=hh3cMSForwardConnectionThreshold, hh3cMSVODIndex=hh3cMSVODIndex, PYSNMP_MODULE_ID=hh3cMSMan, hh3cMSForwardTotalConn=hh3cMSForwardTotalConn, hh3cMSVODConnectionThreshold=hh3cMSVODConnectionThreshold, hh3cMSRecordTotalConn=hh3cMSRecordTotalConn, hh3cMSManRecordConnectionThresholdTrap=hh3cMSManRecordConnectionThresholdTrap, hh3cMSManForwardConnectionRecoverTrap=hh3cMSManForwardConnectionRecoverTrap, hh3cMSForwardMaxConnection=hh3cMSForwardMaxConnection, hh3cMSVODTable=hh3cMSVODTable, hh3cMSVODTotalConn=hh3cMSVODTotalConn, hh3cMSManMIBTables=hh3cMSManMIBTables, hh3cMSMan=hh3cMSMan, hh3cMSForwardEntry=hh3cMSForwardEntry, hh3cMSVODTotalTime=hh3cMSVODTotalTime, hh3cMSRecordTotalTime=hh3cMSRecordTotalTime, hh3cMSPeriodVODMaxConnection=hh3cMSPeriodVODMaxConnection, hh3cMSRecordEntry=hh3cMSRecordEntry, hh3cMSManForwardConnectionThresholdTrap=hh3cMSManForwardConnectionThresholdTrap, hh3cMSCurrentRecordConnection=hh3cMSCurrentRecordConnection, hh3cMSManMIBObjects=hh3cMSManMIBObjects, hh3cMSManMIBTrap=hh3cMSManMIBTrap, hh3cMSRecordMaxConnection=hh3cMSRecordMaxConnection, hh3cMSManTrapPrex=hh3cMSManTrapPrex, hh3cMSCurrentForwardConnection=hh3cMSCurrentForwardConnection, hh3cMSForwardIndex=hh3cMSForwardIndex, hh3cMSForwardTotalTime=hh3cMSForwardTotalTime, hh3cMSManVODConnectionRecoverTrap=hh3cMSManVODConnectionRecoverTrap, hh3cMSCurrentVODConnection=hh3cMSCurrentVODConnection, hh3cMSManVODConnectionThresholdTrap=hh3cMSManVODConnectionThresholdTrap, hh3cMSVODMaxConnection=hh3cMSVODMaxConnection, hh3cMSStatisticalPeriod=hh3cMSStatisticalPeriod, hh3cMSVODEntry=hh3cMSVODEntry, hh3cMSManRecordConnectionRecoverTrap=hh3cMSManRecordConnectionRecoverTrap, hh3cMSPeriodRecordMaxConnection=hh3cMSPeriodRecordMaxConnection, hh3cMSRecordTable=hh3cMSRecordTable, hh3cMSRecordIndex=hh3cMSRecordIndex, hh3cMSRecordConnectionThreshold=hh3cMSRecordConnectionThreshold, hh3cMSPeriodForwardConnection=hh3cMSPeriodForwardConnection, hh3cMSForwardTable=hh3cMSForwardTable)

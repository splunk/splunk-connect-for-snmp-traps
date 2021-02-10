#
# PySNMP MIB module CISCO-SERVICE-CONTROL-RDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SERVICE-CONTROL-RDR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalName")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ObjectIdentity, NotificationType, Integer32, Counter64, ModuleIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ObjectIdentity", "NotificationType", "Integer32", "Counter64", "ModuleIdentity", "Gauge32", "Unsigned32")
TruthValue, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeStamp", "DisplayString")
ciscoServiceControlRdrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 637))
ciscoServiceControlRdrMIB.setRevisions(('2007-08-14 00:00',))
if mibBuilder.loadTexts: ciscoServiceControlRdrMIB.setLastUpdated('200708140000Z')
if mibBuilder.loadTexts: ciscoServiceControlRdrMIB.setOrganization('Cisco Systems, Inc.')
ciscoSCRdrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 0))
ciscoSCRdrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 1))
ciscoSCRdrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 2))
cscRdrFormatterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1), )
if mibBuilder.loadTexts: cscRdrFormatterTable.setStatus('current')
cscRdrFormatterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cscRdrFormatterEntry.setStatus('current')
cscRdrFormatterEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterEnable.setStatus('current')
cscRdrFormatterNumSentReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 2), Counter32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterNumSentReports.setStatus('current')
cscRdrFormatterNumDiscardedReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 3), Counter32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterNumDiscardedReports.setStatus('current')
cscRdrFormatterReportRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 4), Gauge32()).setUnits('reports per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterReportRate.setStatus('current')
cscRdrFormatterReportRatePeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 5), Gauge32()).setUnits('reports per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterReportRatePeak.setStatus('current')
cscRdrFormatterReportRatePeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrFormatterReportRatePeakTime.setStatus('current')
cscRdrFormatterProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rdrv1", 2), ("netflowV9", 3))).clone('rdrv1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscRdrFormatterProtocol.setStatus('current')
cscRdrFormatterForwardingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("redundancy", 2), ("simpleLoadBalancing", 3), ("multicast", 4))).clone('redundancy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscRdrFormatterForwardingMode.setStatus('current')
cscRdrDestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2), )
if mibBuilder.loadTexts: cscRdrDestTable.setStatus('current')
cscRdrDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestIndex"))
if mibBuilder.loadTexts: cscRdrDestEntry.setStatus('current')
cscRdrDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cscRdrDestIndex.setStatus('current')
cscRdrDestInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestInetAddressType.setStatus('current')
cscRdrDestInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestInetAddress.setStatus('current')
cscRdrDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestPort.setStatus('current')
cscRdrDestPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestPriority.setStatus('current')
cscRdrDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestStatus.setStatus('current')
cscRdrDestConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestConnectionStatus.setStatus('current')
cscRdrDestNumSentReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 8), Counter32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestNumSentReports.setStatus('current')
cscRdrDestNumDiscardedReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestNumDiscardedReports.setStatus('current')
cscRdrDestReportRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 10), Gauge32()).setUnits('reports per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrDestReportRate.setStatus('current')
cscRdrCategoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3), )
if mibBuilder.loadTexts: cscRdrCategoryTable.setStatus('current')
cscRdrCategoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryIndex"))
if mibBuilder.loadTexts: cscRdrCategoryEntry.setStatus('current')
cscRdrCategoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: cscRdrCategoryIndex.setStatus('current')
cscRdrCategoryID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryID.setStatus('current')
cscRdrCategoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryName.setStatus('current')
cscRdrCategoryNumSentReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 4), Counter32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryNumSentReports.setStatus('current')
cscRdrCategoryNumDiscardedReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 5), Counter32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryNumDiscardedReports.setStatus('current')
cscRdrCategoryReportRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 6), Gauge32()).setUnits('reports per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryReportRate.setStatus('current')
cscRdrCategoryNumQueuedReports = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 7), Gauge32()).setUnits('reports').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryNumQueuedReports.setStatus('current')
cscRdrCategoryDestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4), )
if mibBuilder.loadTexts: cscRdrCategoryDestTable.setStatus('current')
cscRdrCategoryDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryIndex"), (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"), (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"))
if mibBuilder.loadTexts: cscRdrCategoryDestEntry.setStatus('current')
cscRdrCategoryDestPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryDestPriority.setStatus('current')
cscRdrCategoryDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCategoryDestStatus.setStatus('current')
cscRdrNotifsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 5))
cscRdrCounterDiscontinuityTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscRdrCounterDiscontinuityTime.setStatus('current')
cscRdrReportsEnableNotifs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscRdrReportsEnableNotifs.setStatus('current')
cscRdrCategoryStoppedDiscardingReportsTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
if mibBuilder.loadTexts: cscRdrCategoryStoppedDiscardingReportsTrap.setStatus('current')
cscRdrCategoryDiscardingReportsTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
if mibBuilder.loadTexts: cscRdrCategoryDiscardingReportsTrap.setStatus('current')
cscRdrNoActiveConnectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: cscRdrNoActiveConnectionTrap.setStatus('current')
cscRdrConnectionStatusDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
if mibBuilder.loadTexts: cscRdrConnectionStatusDownTrap.setStatus('current')
cscRdrActiveConnectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
if mibBuilder.loadTexts: cscRdrActiveConnectionTrap.setStatus('current')
cscRdrConnectionStatusUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 6)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
if mibBuilder.loadTexts: cscRdrConnectionStatusUpTrap.setStatus('current')
cscRdrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 1))
cscRdrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2))
cscRdrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrObjectGroup"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrNotificationGroup"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCounterDiscontinuityGroup"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrNotifsControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscRdrCompliance = cscRdrCompliance.setStatus('current')
cscRdrObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterEnable"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterNumSentReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterNumDiscardedReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRate"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterProtocol"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterForwardingMode"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddressType"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPriority"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestConnectionStatus"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestNumSentReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestNumDiscardedReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestReportRate"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryName"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumSentReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumDiscardedReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryReportRate"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumQueuedReports"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDestPriority"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDestStatus"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRatePeak"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRatePeakTime"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscRdrObjectGroup = cscRdrObjectGroup.setStatus('current')
cscRdrNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrActiveConnectionTrap"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryStoppedDiscardingReportsTrap"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDiscardingReportsTrap"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrNoActiveConnectionTrap"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrConnectionStatusDownTrap"), ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrConnectionStatusUpTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscRdrNotificationGroup = cscRdrNotificationGroup.setStatus('current')
cscRdrNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrReportsEnableNotifs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscRdrNotifsControlGroup = cscRdrNotifsControlGroup.setStatus('current')
cscRdrCounterDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 4)).setObjects(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCounterDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscRdrCounterDiscontinuityGroup = cscRdrCounterDiscontinuityGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-RDR-MIB", cscRdrActiveConnectionTrap=cscRdrActiveConnectionTrap, cscRdrDestNumDiscardedReports=cscRdrDestNumDiscardedReports, cscRdrDestReportRate=cscRdrDestReportRate, cscRdrCategoryDestStatus=cscRdrCategoryDestStatus, cscRdrDestStatus=cscRdrDestStatus, cscRdrCompliance=cscRdrCompliance, ciscoSCRdrMIBConform=ciscoSCRdrMIBConform, cscRdrNotifsControlGroup=cscRdrNotifsControlGroup, cscRdrCategoryIndex=cscRdrCategoryIndex, cscRdrDestPriority=cscRdrDestPriority, cscRdrCategoryNumQueuedReports=cscRdrCategoryNumQueuedReports, cscRdrFormatterReportRatePeakTime=cscRdrFormatterReportRatePeakTime, cscRdrFormatterEnable=cscRdrFormatterEnable, cscRdrFormatterEntry=cscRdrFormatterEntry, cscRdrReportsEnableNotifs=cscRdrReportsEnableNotifs, cscRdrCounterDiscontinuityGroup=cscRdrCounterDiscontinuityGroup, cscRdrConnectionStatusDownTrap=cscRdrConnectionStatusDownTrap, cscRdrNotificationGroup=cscRdrNotificationGroup, cscRdrCategoryNumSentReports=cscRdrCategoryNumSentReports, cscRdrDestEntry=cscRdrDestEntry, cscRdrDestInetAddressType=cscRdrDestInetAddressType, cscRdrCategoryName=cscRdrCategoryName, cscRdrFormatterForwardingMode=cscRdrFormatterForwardingMode, cscRdrFormatterProtocol=cscRdrFormatterProtocol, cscRdrDestInetAddress=cscRdrDestInetAddress, cscRdrCategoryID=cscRdrCategoryID, cscRdrCategoryDestEntry=cscRdrCategoryDestEntry, cscRdrFormatterReportRatePeak=cscRdrFormatterReportRatePeak, cscRdrCategoryTable=cscRdrCategoryTable, cscRdrCategoryEntry=cscRdrCategoryEntry, ciscoSCRdrMIBNotifs=ciscoSCRdrMIBNotifs, cscRdrCategoryReportRate=cscRdrCategoryReportRate, cscRdrDestTable=cscRdrDestTable, cscRdrDestIndex=cscRdrDestIndex, cscRdrDestNumSentReports=cscRdrDestNumSentReports, cscRdrCategoryDestPriority=cscRdrCategoryDestPriority, PYSNMP_MODULE_ID=ciscoServiceControlRdrMIB, cscRdrFormatterNumSentReports=cscRdrFormatterNumSentReports, ciscoServiceControlRdrMIB=ciscoServiceControlRdrMIB, cscRdrFormatterTable=cscRdrFormatterTable, cscRdrDestPort=cscRdrDestPort, cscRdrMIBGroups=cscRdrMIBGroups, cscRdrCategoryStoppedDiscardingReportsTrap=cscRdrCategoryStoppedDiscardingReportsTrap, cscRdrMIBCompliances=cscRdrMIBCompliances, cscRdrObjectGroup=cscRdrObjectGroup, cscRdrCategoryNumDiscardedReports=cscRdrCategoryNumDiscardedReports, ciscoSCRdrMIBObjects=ciscoSCRdrMIBObjects, cscRdrConnectionStatusUpTrap=cscRdrConnectionStatusUpTrap, cscRdrCategoryDiscardingReportsTrap=cscRdrCategoryDiscardingReportsTrap, cscRdrDestConnectionStatus=cscRdrDestConnectionStatus, cscRdrNoActiveConnectionTrap=cscRdrNoActiveConnectionTrap, cscRdrFormatterReportRate=cscRdrFormatterReportRate, cscRdrFormatterNumDiscardedReports=cscRdrFormatterNumDiscardedReports, cscRdrCounterDiscontinuityTime=cscRdrCounterDiscontinuityTime, cscRdrNotifsConfig=cscRdrNotifsConfig, cscRdrCategoryDestTable=cscRdrCategoryDestTable)

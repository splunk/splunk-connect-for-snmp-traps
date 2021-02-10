#
# PySNMP MIB module CISCO-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, = mibBuilder.importSymbols("CISCO-TC", "Unsigned64")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, TimeTicks, iso, Bits, MibIdentifier, Unsigned32, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "Bits", "MibIdentifier", "Unsigned32", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ModuleIdentity", "ObjectIdentity")
DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
ciscoConfigManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 43))
ciscoConfigManMIB.setRevisions(('2007-04-27 00:00', '2006-08-17 00:00', '2004-06-18 00:00', '2002-06-07 00:00', '2002-03-12 00:00', '1995-11-28 00:00',))
if mibBuilder.loadTexts: ciscoConfigManMIB.setLastUpdated('200704270000Z')
if mibBuilder.loadTexts: ciscoConfigManMIB.setOrganization('Cisco Systems, Inc.')
ciscoConfigManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1))
ccmHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1))
ccmCLIHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2))
ccmCLICfg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3))
ccmCTIDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4))
class HistoryEventMedium(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("erase", 1), ("commandSource", 2), ("running", 3), ("startup", 4), ("local", 5), ("networkTftp", 6), ("networkRcp", 7), ("networkFtp", 8), ("networkScp", 9))

ccmHistoryRunningLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastChanged.setStatus('current')
ccmHistoryRunningLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastSaved.setStatus('current')
ccmHistoryStartupLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryStartupLastChanged.setStatus('current')
ccmHistoryMaxEventEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryMaxEventEntries.setStatus('current')
ccmHistoryEventEntriesBumped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventEntriesBumped.setStatus('current')
ccmHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6), )
if mibBuilder.loadTexts: ccmHistoryEventTable.setStatus('current')
ccmHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"))
if mibBuilder.loadTexts: ccmHistoryEventEntry.setStatus('current')
ccmHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccmHistoryEventIndex.setStatus('current')
ccmHistoryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTime.setStatus('current')
ccmHistoryEventCommandSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("commandLine", 1), ("snmp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSource.setStatus('current')
ccmHistoryEventConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 4), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigSource.setStatus('current')
ccmHistoryEventConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 5), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigDestination.setStatus('current')
ccmHistoryEventTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("console", 3), ("terminal", 4), ("virtual", 5), ("auxiliary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalType.setStatus('current')
ccmHistoryEventTerminalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalNumber.setStatus('current')
ccmHistoryEventTerminalUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalUser.setStatus('current')
ccmHistoryEventTerminalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalLocation.setStatus('current')
ccmHistoryEventCommandSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddress.setStatus('deprecated')
ccmHistoryEventVirtualHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventVirtualHostName.setStatus('current')
ccmHistoryEventServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddress.setStatus('deprecated')
ccmHistoryEventFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventFile.setStatus('current')
ccmHistoryEventRcpUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventRcpUser.setStatus('current')
ccmHistoryCLICmdEntriesBumped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryCLICmdEntriesBumped.setStatus('current')
ccmHistoryEventCommandSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 16), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrType.setStatus('current')
ccmHistoryEventCommandSourceAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 17), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrRev1.setStatus('current')
ccmHistoryEventServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 18), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrType.setStatus('current')
ccmHistoryEventServerAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 19), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrRev1.setStatus('current')
ccmCLIHistoryMaxCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLIHistoryMaxCmdEntries.setStatus('current')
ccmCLIHistoryCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntries.setStatus('current')
ccmCLIHistoryCmdEntriesAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntriesAllowed.setStatus('current')
ccmCLIHistoryCommandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4), )
if mibBuilder.loadTexts: ccmCLIHistoryCommandTable.setStatus('current')
ccmCLIHistoryCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"), (0, "CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommandIndex"))
if mibBuilder.loadTexts: ccmCLIHistoryCommandEntry.setStatus('current')
ccmCLIHistoryCommandIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ccmCLIHistoryCommandIndex.setStatus('current')
ccmCLIHistoryCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCommand.setStatus('current')
ccmCLICfgRunConfNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLICfgRunConfNotifEnable.setStatus('current')
ccmCTID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTID.setStatus('current')
ccmCTIDLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDLastChangeTime.setStatus('current')
ccmCTIDWhoChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDWhoChanged.setStatus('current')
ccmCTIDRolledOverNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCTIDRolledOverNotifEnable.setStatus('current')
ciscoConfigManMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2))
ciscoConfigManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0))
ciscoConfigManEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"))
if mibBuilder.loadTexts: ciscoConfigManEvent.setStatus('current')
ccmCLIRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"))
if mibBuilder.loadTexts: ccmCLIRunningConfigChanged.setStatus('current')
ccmCTIDRolledOver = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 3))
if mibBuilder.loadTexts: ccmCTIDRolledOver.setStatus('current')
ciscoConfigManMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3))
ciscoConfigManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1))
ciscoConfigManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2))
ciscoConfigManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBCompliance = ciscoConfigManMIBCompliance.setStatus('deprecated')
ciscoConfigManMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev1"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev2 = ciscoConfigManMIBComplianceRev2.setStatus('deprecated')
ciscoConfigManMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 3)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev3 = ciscoConfigManMIBComplianceRev3.setStatus('deprecated')
ciscoConfigManMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 4)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev4 = ciscoConfigManMIBComplianceRev4.setStatus('current')
ciscoConfigManHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroup = ciscoConfigManHistoryGroup.setStatus('deprecated')
ciscoConfigManHistoryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroupRev1 = ciscoConfigManHistoryGroupRev1.setStatus('deprecated')
ciscoConfigManHistNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 3)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManEvent"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIRunningConfigChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistNotifyGroup = ciscoConfigManHistNotifyGroup.setStatus('current')
ciscoConfigManHistoryGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 5)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrRev1"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroupRev2 = ciscoConfigManHistoryGroupRev2.setStatus('current')
ciscoConfigManCLIHistCmdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 4)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryMaxCmdEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntriesAllowed"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommand"), ("CISCO-CONFIG-MAN-MIB", "ccmCLICfgRunConfNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCLIHistCmdGroup = ciscoConfigManCLIHistCmdGroup.setStatus('current')
ciscoConfigManCTIDNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 6)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOver"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCTIDNotifyGroup = ciscoConfigManCTIDNotifyGroup.setStatus('current')
ciscoConfigManCTIDObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 7)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCTID"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDLastChangeTime"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDWhoChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOverNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCTIDObjectGroup = ciscoConfigManCTIDObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ccmCTIDWhoChanged=ccmCTIDWhoChanged, ciscoConfigManHistoryGroupRev2=ciscoConfigManHistoryGroupRev2, ccmHistoryEventCommandSource=ccmHistoryEventCommandSource, ccmHistoryEventServerAddrRev1=ccmHistoryEventServerAddrRev1, ccmHistoryMaxEventEntries=ccmHistoryMaxEventEntries, ccmCLIHistory=ccmCLIHistory, ccmCTIDObjects=ccmCTIDObjects, HistoryEventMedium=HistoryEventMedium, ccmHistoryEventServerAddress=ccmHistoryEventServerAddress, ccmCLIHistoryCommandTable=ccmCLIHistoryCommandTable, ciscoConfigManMIBCompliance=ciscoConfigManMIBCompliance, ccmHistoryEventEntry=ccmHistoryEventEntry, ccmHistoryEventTerminalType=ccmHistoryEventTerminalType, ccmHistoryRunningLastChanged=ccmHistoryRunningLastChanged, ccmHistoryRunningLastSaved=ccmHistoryRunningLastSaved, ccmHistoryEventCommandSourceAddrType=ccmHistoryEventCommandSourceAddrType, ciscoConfigManMIBConformance=ciscoConfigManMIBConformance, ccmHistoryEventVirtualHostName=ccmHistoryEventVirtualHostName, ciscoConfigManMIBComplianceRev2=ciscoConfigManMIBComplianceRev2, ccmCLIHistoryMaxCmdEntries=ccmCLIHistoryMaxCmdEntries, ciscoConfigManMIBNotifications=ciscoConfigManMIBNotifications, ccmCLIHistoryCommand=ccmCLIHistoryCommand, ccmHistoryEventTerminalUser=ccmHistoryEventTerminalUser, ccmCTIDRolledOver=ccmCTIDRolledOver, ccmHistoryEventConfigSource=ccmHistoryEventConfigSource, ccmHistoryEventIndex=ccmHistoryEventIndex, ccmHistoryEventTable=ccmHistoryEventTable, PYSNMP_MODULE_ID=ciscoConfigManMIB, ccmCLICfg=ccmCLICfg, ccmCTIDLastChangeTime=ccmCTIDLastChangeTime, ccmHistoryEventEntriesBumped=ccmHistoryEventEntriesBumped, ccmCLICfgRunConfNotifEnable=ccmCLICfgRunConfNotifEnable, ciscoConfigManCLIHistCmdGroup=ciscoConfigManCLIHistCmdGroup, ciscoConfigManEvent=ciscoConfigManEvent, ccmHistoryEventConfigDestination=ccmHistoryEventConfigDestination, ccmCLIHistoryCmdEntriesAllowed=ccmCLIHistoryCmdEntriesAllowed, ccmHistoryEventTime=ccmHistoryEventTime, ccmHistoryEventCommandSourceAddress=ccmHistoryEventCommandSourceAddress, ciscoConfigManMIBComplianceRev3=ciscoConfigManMIBComplianceRev3, ciscoConfigManMIBObjects=ciscoConfigManMIBObjects, ccmHistoryEventFile=ccmHistoryEventFile, ccmCTIDRolledOverNotifEnable=ccmCTIDRolledOverNotifEnable, ciscoConfigManCTIDObjectGroup=ciscoConfigManCTIDObjectGroup, ciscoConfigManMIBGroups=ciscoConfigManMIBGroups, ciscoConfigManHistoryGroup=ciscoConfigManHistoryGroup, ccmCLIHistoryCommandIndex=ccmCLIHistoryCommandIndex, ciscoConfigManMIBCompliances=ciscoConfigManMIBCompliances, ccmCLIRunningConfigChanged=ccmCLIRunningConfigChanged, ccmHistoryEventCommandSourceAddrRev1=ccmHistoryEventCommandSourceAddrRev1, ccmHistory=ccmHistory, ciscoConfigManCTIDNotifyGroup=ciscoConfigManCTIDNotifyGroup, ciscoConfigManMIBComplianceRev4=ciscoConfigManMIBComplianceRev4, ciscoConfigManMIBNotificationPrefix=ciscoConfigManMIBNotificationPrefix, ciscoConfigManHistNotifyGroup=ciscoConfigManHistNotifyGroup, ccmCTID=ccmCTID, ccmHistoryEventTerminalNumber=ccmHistoryEventTerminalNumber, ccmCLIHistoryCmdEntries=ccmCLIHistoryCmdEntries, ciscoConfigManHistoryGroupRev1=ciscoConfigManHistoryGroupRev1, ccmHistoryEventServerAddrType=ccmHistoryEventServerAddrType, ccmHistoryCLICmdEntriesBumped=ccmHistoryCLICmdEntriesBumped, ccmHistoryEventRcpUser=ccmHistoryEventRcpUser, ccmCLIHistoryCommandEntry=ccmCLIHistoryCommandEntry, ciscoConfigManMIB=ciscoConfigManMIB, ccmHistoryEventTerminalLocation=ccmHistoryEventTerminalLocation, ccmHistoryStartupLastChanged=ccmHistoryStartupLastChanged)

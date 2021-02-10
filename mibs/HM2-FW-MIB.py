#
# PySNMP MIB module HM2-FW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-FW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hm2ConfigurationMibs, HmActionValue, HmTimeSeconds1970, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs", "HmActionValue", "HmTimeSeconds1970", "HmEnabledStatus")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Unsigned32, IpAddress, Gauge32, TimeTicks, ModuleIdentity, Bits, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Unsigned32", "IpAddress", "Gauge32", "TimeTicks", "ModuleIdentity", "Bits", "NotificationType", "Counter32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
hm2FwMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 79))
hm2FwMib.setRevisions(('2011-09-13 00:00', '2011-07-01 00:00', '2011-06-14 00:00', '2011-05-31 00:00',))
if mibBuilder.loadTexts: hm2FwMib.setLastUpdated('201109130000Z')
if mibBuilder.loadTexts: hm2FwMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2FwNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 0))
hm2FwObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1))
hm2FwConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 2))
hm2FwGeneralSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1))
hm2DynFw = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2))
hm2L3Fw = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3))
hm2FwLearningMode = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4))
hm2DynFwMaxRules = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwMaxRules.setStatus('current')
hm2L3MaxRules = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3MaxRules.setStatus('current')
hm2ResetStatistics = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 3), HmActionValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2ResetStatistics.setStatus('current')
hm2FlushTables = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 4), HmActionValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FlushTables.setStatus('current')
hm2DefaultPolicy = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("accept", 1), ("drop", 2), ("reject", 3))).clone('accept')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DefaultPolicy.setStatus('current')
hm2ConnTrackValidateCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2ConnTrackValidateCheckSum.setStatus('current')
hm2DynFwRuleAppliedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 1)).setObjects(("HM2-FW-MIB", "hm2DynFwRuleIndex"))
if mibBuilder.loadTexts: hm2DynFwRuleAppliedTrap.setStatus('current')
hm2DynFwRuleAppliedAndLoggedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 2)).setObjects(("HM2-FW-MIB", "hm2DynFwRuleIndex"))
if mibBuilder.loadTexts: hm2DynFwRuleAppliedAndLoggedTrap.setStatus('current')
hm2DynFwRuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1))
hm2DynFwRuleCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwRuleCount.setStatus('current')
hm2DynFwIfMappingRuleCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwIfMappingRuleCount.setStatus('current')
hm2DynFwRulePendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwRulePendingActions.setStatus('current')
hm2DynFwCommitPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 4), HmActionValue().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DynFwCommitPendingActions.setStatus('current')
hm2DynFwRuleTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2))
hm2DynFwRuleTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1), )
if mibBuilder.loadTexts: hm2DynFwRuleTable.setStatus('current')
hm2DynFwRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2DynFwRuleIndex"))
if mibBuilder.loadTexts: hm2DynFwRuleEntry.setStatus('current')
hm2DynFwRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2DynFwRuleIndex.setStatus('current')
hm2DynFwSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwSourceAddress.setStatus('current')
hm2DynFwSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwSourcePort.setStatus('current')
hm2DynFwTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwTargetAddress.setStatus('current')
hm2DynFwTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwTargetPort.setStatus('current')
hm2DynFwProto = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("icmp", 1), ("igmp", 2), ("ipip", 3), ("tcp", 4), ("udp", 5), ("esp", 6), ("ah", 7), ("icmpv6", 8), ("any", 9))).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwProto.setStatus('current')
hm2DynFwRuleParams = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwRuleParams.setStatus('current')
hm2DynFwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("accept", 1), ("drop", 2), ("reject", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwAction.setStatus('current')
hm2DynFwLog = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwLog.setStatus('current')
hm2DynFwTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwTrap.setStatus('current')
hm2DynFwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwRowStatus.setStatus('current')
hm2DynFwDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwDescription.setStatus('current')
hm2DynFwRuleIfMappingTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2), )
if mibBuilder.loadTexts: hm2DynFwRuleIfMappingTable.setStatus('current')
hm2DynFwRuleIfMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2DynFwIfmInterface"), (0, "HM2-FW-MIB", "hm2DynFwIfmDirection"), (0, "HM2-FW-MIB", "hm2DynFwIfmRuleIndex"))
if mibBuilder.loadTexts: hm2DynFwRuleIfMappingEntry.setStatus('current')
hm2DynFwIfmRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: hm2DynFwIfmRuleIndex.setStatus('current')
hm2DynFwIfmDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2), ("both", 3))))
if mibBuilder.loadTexts: hm2DynFwIfmDirection.setStatus('current')
hm2DynFwIfmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwIfmPriority.setStatus('current')
hm2DynFwIfmInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: hm2DynFwIfmInterface.setStatus('current')
hm2DynFwIfmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DynFwIfmRowStatus.setStatus('current')
hm2DynFwStats = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4))
hm2DynFwGeneralStats = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1))
hm2DynFwStatsTtPck = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsTtPck.setStatus('current')
hm2DynFwStatsTtPckSize = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsTtPckSize.setStatus('current')
hm2DynFwStatsTtPckDenDrop = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsTtPckDenDrop.setStatus('current')
hm2DynFwStatsTtPckAccepted = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsTtPckAccepted.setStatus('current')
hm2DynFwStatsTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2))
hm2DynFwStatsRuleTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1), )
if mibBuilder.loadTexts: hm2DynFwStatsRuleTable.setStatus('current')
hm2DynFwStatsRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2DynFwRuleIndex"))
if mibBuilder.loadTexts: hm2DynFwStatsRuleEntry.setStatus('current')
hm2DynFwStatsPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsPacketCount.setStatus('current')
hm2DynFwStatsPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsPacketSize.setStatus('current')
hm2DynFwStatsLastApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 3), HmTimeSeconds1970()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DynFwStatsLastApplied.setStatus('current')
hm2L3RuleAppliedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 3)).setObjects(("HM2-FW-MIB", "hm2L3RuleIndex"))
if mibBuilder.loadTexts: hm2L3RuleAppliedTrap.setStatus('current')
hm2L3RuleAppliedAndLoggedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 4)).setObjects(("HM2-FW-MIB", "hm2L3RuleIndex"))
if mibBuilder.loadTexts: hm2L3RuleAppliedAndLoggedTrap.setStatus('current')
hm2L3RuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1))
hm2L3RuleCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3RuleCount.setStatus('current')
hm2L3IfMappingRuleCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3IfMappingRuleCount.setStatus('current')
hm2L3RulePendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3RulePendingActions.setStatus('current')
hm2L3CommitPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 4), HmActionValue().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2L3CommitPendingActions.setStatus('current')
hm2L3RuleTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2))
hm2L3RuleTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1), )
if mibBuilder.loadTexts: hm2L3RuleTable.setStatus('current')
hm2L3RuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2L3RuleIndex"))
if mibBuilder.loadTexts: hm2L3RuleEntry.setStatus('current')
hm2L3RuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2L3RuleIndex.setStatus('current')
hm2L3SourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3SourceAddress.setStatus('current')
hm2L3SourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3SourcePort.setStatus('current')
hm2L3TargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3TargetAddress.setStatus('current')
hm2L3TargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3TargetPort.setStatus('current')
hm2L3Proto = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("icmp", 1), ("igmp", 2), ("ipip", 3), ("tcp", 4), ("udp", 5), ("esp", 6), ("ah", 7), ("icmpv6", 8), ("any", 9))).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3Proto.setStatus('current')
hm2L3RuleParams = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3RuleParams.setStatus('current')
hm2L3Action = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("accept", 1), ("drop", 2), ("reject", 3), ("enforce-modbus", 4), ("enforce-opc", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3Action.setStatus('current')
hm2L3Log = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3Log.setStatus('current')
hm2L3Trap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3Trap.setStatus('current')
hm2L3RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3RowStatus.setStatus('current')
hm2L3Description = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3Description.setStatus('current')
hm2DPIProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileIndex.setStatus('current')
hm2L3RuleIfMappingTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2), )
if mibBuilder.loadTexts: hm2L3RuleIfMappingTable.setStatus('current')
hm2L3RuleIfMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2L3IfmInterface"), (0, "HM2-FW-MIB", "hm2L3IfmDirection"), (0, "HM2-FW-MIB", "hm2L3IfmRuleIndex"))
if mibBuilder.loadTexts: hm2L3RuleIfMappingEntry.setStatus('current')
hm2L3IfmRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: hm2L3IfmRuleIndex.setStatus('current')
hm2L3IfmDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2), ("both", 3))))
if mibBuilder.loadTexts: hm2L3IfmDirection.setStatus('current')
hm2L3IfmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3IfmPriority.setStatus('current')
hm2L3IfmInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: hm2L3IfmInterface.setStatus('current')
hm2L3IfmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2L3IfmRowStatus.setStatus('current')
hm2L3Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4))
hm2L3GeneralStats = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1))
hm2L3StatsTotalPck = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsTotalPck.setStatus('current')
hm2L3StatsTotalPckSize = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsTotalPckSize.setStatus('current')
hm2L3StatsTotalPckDenDrop = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsTotalPckDenDrop.setStatus('current')
hm2L3StatsTotalPckAccepted = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsTotalPckAccepted.setStatus('current')
hm2L3StatsTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2))
hm2L3StatsRuleTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1), )
if mibBuilder.loadTexts: hm2L3StatsRuleTable.setStatus('current')
hm2L3StatsRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2L3RuleIndex"))
if mibBuilder.loadTexts: hm2L3StatsRuleEntry.setStatus('current')
hm2L3StatsPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsPacketCount.setStatus('current')
hm2L3StatsPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsPacketSize.setStatus('current')
hm2L3StatsLastApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 3), HmTimeSeconds1970()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2L3StatsLastApplied.setStatus('current')
hm2DPIProfileModbusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11))
hm2DPIProfileModbusPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DPIProfileModbusPendingActions.setStatus('current')
hm2DPIProfileModbusCommitPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11, 2), HmActionValue().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DPIProfileModbusCommitPendingActions.setStatus('current')
hm2DPIProfileOpcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12))
hm2DPIProfileOpcPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DPIProfileOpcPendingActions.setStatus('current')
hm2DPIProfileOpcCommitPendingActions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12, 2), HmActionValue().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DPIProfileOpcCommitPendingActions.setStatus('current')
hm2DPIProfileTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21))
hm2DPIProfileModbusTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1), )
if mibBuilder.loadTexts: hm2DPIProfileModbusTable.setStatus('current')
hm2DPIProfileModbusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2DPIProfileModbusIndex"))
if mibBuilder.loadTexts: hm2DPIProfileModbusEntry.setStatus('current')
hm2DPIProfileModbusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2DPIProfileModbusIndex.setStatus('current')
hm2DPIProfileModbusDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('modbus')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusDescription.setStatus('current')
hm2DPIProfileModbusFunctionType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("readonly", 1), ("readwrite", 2), ("programming", 3), ("all", 4), ("advanced", 5))).clone('readonly')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusFunctionType.setStatus('current')
hm2DPIProfileModbusFunctionCodeList = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1400)).clone('1,2,3,4,7,11,12,17,20,24')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusFunctionCodeList.setStatus('current')
hm2DPIProfileModbusUnitIdentifierList = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1400)).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusUnitIdentifierList.setStatus('current')
hm2DPIProfileModbusSanityCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusSanityCheck.setStatus('current')
hm2DPIProfileModbusException = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusException.setStatus('current')
hm2DPIProfileModbusReset = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusReset.setStatus('current')
hm2DPIProfileModbusRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileModbusRowStatus.setStatus('current')
hm2DPIProfileOpcTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2), )
if mibBuilder.loadTexts: hm2DPIProfileOpcTable.setStatus('current')
hm2DPIProfileOpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2DPIProfileOpcIndex"))
if mibBuilder.loadTexts: hm2DPIProfileOpcEntry.setStatus('current')
hm2DPIProfileOpcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2DPIProfileOpcIndex.setStatus('current')
hm2DPIProfileOpcDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('opc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileOpcDescription.setStatus('current')
hm2DPIProfileOpcSanityCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileOpcSanityCheck.setStatus('current')
hm2DPIProfileOpcFragmentCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileOpcFragmentCheck.setStatus('current')
hm2DPIProfileOpcTimeoutConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileOpcTimeoutConnect.setStatus('current')
hm2DPIProfileOpcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DPIProfileOpcRowStatus.setStatus('current')
hm2FLMObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1))
hm2FLMAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FLMAdminState.setStatus('current')
hm2FLMAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("start", 2), ("stop", 3), ("continue", 4), ("clear", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FLMAction.setStatus('current')
hm2FLMAppState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 1), ("stopped-data-notpresent", 2), ("stopped-data-present", 3), ("learning", 4), ("pending", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLMAppState.setStatus('current')
hm2FLMAppInfoEnum = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("normal", 2), ("low-memory", 3), ("out-of-memory", 4), ("connection-drop", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLMAppInfoEnum.setStatus('current')
hm2FLMAppInfoString = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLMAppInfoString.setStatus('current')
hm2FLML3Entries = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLML3Entries.setStatus('current')
hm2FLMFreeMem = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLMFreeMem.setStatus('current')
hm2FLMMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2FLMMaxEntries.setStatus('current')
hm2FLMTables = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2))
hm2FLMInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1), )
if mibBuilder.loadTexts: hm2FLMInterfaceTable.setStatus('current')
hm2FLMInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1), ).setIndexNames((0, "HM2-FW-MIB", "hm2FLMInterfaceIndex"))
if mibBuilder.loadTexts: hm2FLMInterfaceEntry.setStatus('current')
hm2FLMInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2FLMInterfaceIndex.setStatus('current')
hm2FLMInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2FLMInterfaceRowStatus.setStatus('current')
hm2FwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 1))
hm2FwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2))
hm2FwCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 1, 1)).setObjects(("HM2-FW-MIB", "hm2FwGeneralGroup"), ("HM2-FW-MIB", "hm2FwNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hm2FwCompliance = hm2FwCompliance.setStatus('current')
hm2FwGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2, 1)).setObjects(("HM2-FW-MIB", "hm2DynFwMaxRules"), ("HM2-FW-MIB", "hm2L3MaxRules"), ("HM2-FW-MIB", "hm2ResetStatistics"), ("HM2-FW-MIB", "hm2FlushTables"), ("HM2-FW-MIB", "hm2DefaultPolicy"), ("HM2-FW-MIB", "hm2DynFwRuleCount"), ("HM2-FW-MIB", "hm2DynFwIfMappingRuleCount"), ("HM2-FW-MIB", "hm2DynFwRulePendingActions"), ("HM2-FW-MIB", "hm2DynFwCommitPendingActions"), ("HM2-FW-MIB", "hm2DynFwRuleIndex"), ("HM2-FW-MIB", "hm2DynFwSourceAddress"), ("HM2-FW-MIB", "hm2DynFwSourcePort"), ("HM2-FW-MIB", "hm2DynFwTargetAddress"), ("HM2-FW-MIB", "hm2DynFwTargetPort"), ("HM2-FW-MIB", "hm2DynFwProto"), ("HM2-FW-MIB", "hm2DynFwRuleParams"), ("HM2-FW-MIB", "hm2DynFwAction"), ("HM2-FW-MIB", "hm2DynFwLog"), ("HM2-FW-MIB", "hm2DynFwTrap"), ("HM2-FW-MIB", "hm2DynFwDescription"), ("HM2-FW-MIB", "hm2DynFwRowStatus"), ("HM2-FW-MIB", "hm2DynFwIfmPriority"), ("HM2-FW-MIB", "hm2DynFwIfmRowStatus"), ("HM2-FW-MIB", "hm2DynFwStatsPacketCount"), ("HM2-FW-MIB", "hm2DynFwStatsPacketSize"), ("HM2-FW-MIB", "hm2DynFwStatsLastApplied"), ("HM2-FW-MIB", "hm2DynFwStatsTtPck"), ("HM2-FW-MIB", "hm2DynFwStatsTtPckSize"), ("HM2-FW-MIB", "hm2DynFwStatsTtPckDenDrop"), ("HM2-FW-MIB", "hm2DynFwStatsTtPckAccepted"), ("HM2-FW-MIB", "hm2L3RuleCount"), ("HM2-FW-MIB", "hm2L3IfMappingRuleCount"), ("HM2-FW-MIB", "hm2L3RulePendingActions"), ("HM2-FW-MIB", "hm2L3CommitPendingActions"), ("HM2-FW-MIB", "hm2L3RuleIndex"), ("HM2-FW-MIB", "hm2L3SourceAddress"), ("HM2-FW-MIB", "hm2L3SourcePort"), ("HM2-FW-MIB", "hm2L3TargetAddress"), ("HM2-FW-MIB", "hm2L3TargetPort"), ("HM2-FW-MIB", "hm2L3Proto"), ("HM2-FW-MIB", "hm2L3Action"), ("HM2-FW-MIB", "hm2L3RuleParams"), ("HM2-FW-MIB", "hm2L3Log"), ("HM2-FW-MIB", "hm2L3Trap"), ("HM2-FW-MIB", "hm2L3Description"), ("HM2-FW-MIB", "hm2L3RowStatus"), ("HM2-FW-MIB", "hm2DPIProfileIndex"), ("HM2-FW-MIB", "hm2L3IfmPriority"), ("HM2-FW-MIB", "hm2L3IfmRowStatus"), ("HM2-FW-MIB", "hm2L3StatsPacketCount"), ("HM2-FW-MIB", "hm2L3StatsPacketSize"), ("HM2-FW-MIB", "hm2L3StatsLastApplied"), ("HM2-FW-MIB", "hm2L3StatsTotalPck"), ("HM2-FW-MIB", "hm2L3StatsTotalPckSize"), ("HM2-FW-MIB", "hm2L3StatsTotalPckDenDrop"), ("HM2-FW-MIB", "hm2L3StatsTotalPckAccepted"), ("HM2-FW-MIB", "hm2DPIProfileModbusPendingActions"), ("HM2-FW-MIB", "hm2DPIProfileModbusCommitPendingActions"), ("HM2-FW-MIB", "hm2DPIProfileModbusIndex"), ("HM2-FW-MIB", "hm2DPIProfileModbusDescription"), ("HM2-FW-MIB", "hm2DPIProfileModbusFunctionType"), ("HM2-FW-MIB", "hm2DPIProfileModbusFunctionCodeList"), ("HM2-FW-MIB", "hm2DPIProfileModbusUnitIdentifierList"), ("HM2-FW-MIB", "hm2DPIProfileModbusSanityCheck"), ("HM2-FW-MIB", "hm2DPIProfileModbusException"), ("HM2-FW-MIB", "hm2DPIProfileModbusReset"), ("HM2-FW-MIB", "hm2DPIProfileModbusRowStatus"), ("HM2-FW-MIB", "hm2DPIProfileOpcPendingActions"), ("HM2-FW-MIB", "hm2DPIProfileOpcCommitPendingActions"), ("HM2-FW-MIB", "hm2DPIProfileOpcIndex"), ("HM2-FW-MIB", "hm2DPIProfileOpcDescription"), ("HM2-FW-MIB", "hm2DPIProfileOpcSanityCheck"), ("HM2-FW-MIB", "hm2DPIProfileOpcFragmentCheck"), ("HM2-FW-MIB", "hm2DPIProfileOpcTimeoutConnect"), ("HM2-FW-MIB", "hm2DPIProfileOpcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hm2FwGeneralGroup = hm2FwGeneralGroup.setStatus('current')
hm2FwNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2, 2)).setObjects(("HM2-FW-MIB", "hm2DynFwRuleAppliedTrap"), ("HM2-FW-MIB", "hm2DynFwRuleAppliedAndLoggedTrap"), ("HM2-FW-MIB", "hm2L3RuleAppliedTrap"), ("HM2-FW-MIB", "hm2L3RuleAppliedAndLoggedTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hm2FwNotificationsGroup = hm2FwNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("HM2-FW-MIB", hm2DPIProfileOpcTimeoutConnect=hm2DPIProfileOpcTimeoutConnect, hm2DynFwStatsRuleEntry=hm2DynFwStatsRuleEntry, hm2L3RuleIfMappingEntry=hm2L3RuleIfMappingEntry, hm2DynFwSourceAddress=hm2DynFwSourceAddress, hm2FwCompliances=hm2FwCompliances, hm2DPIProfileModbusException=hm2DPIProfileModbusException, hm2L3StatsRuleEntry=hm2L3StatsRuleEntry, hm2DPIProfileOpcTable=hm2DPIProfileOpcTable, hm2FwNotifications=hm2FwNotifications, hm2DPIProfileOpcFragmentCheck=hm2DPIProfileOpcFragmentCheck, hm2FwGeneralGroup=hm2FwGeneralGroup, hm2L3IfmRuleIndex=hm2L3IfmRuleIndex, hm2L3StatsPacketSize=hm2L3StatsPacketSize, hm2FLMObjects=hm2FLMObjects, PYSNMP_MODULE_ID=hm2FwMib, hm2DynFwRuleIfMappingEntry=hm2DynFwRuleIfMappingEntry, hm2DPIProfileModbusFunctionCodeList=hm2DPIProfileModbusFunctionCodeList, hm2L3IfMappingRuleCount=hm2L3IfMappingRuleCount, hm2DPIProfileTables=hm2DPIProfileTables, hm2L3RuleIndex=hm2L3RuleIndex, hm2FwMib=hm2FwMib, hm2DynFwCommitPendingActions=hm2DynFwCommitPendingActions, hm2DPIProfileModbusFunctionType=hm2DPIProfileModbusFunctionType, hm2FLMAppInfoEnum=hm2FLMAppInfoEnum, hm2ResetStatistics=hm2ResetStatistics, hm2L3SourcePort=hm2L3SourcePort, hm2DPIProfileModbusCommitPendingActions=hm2DPIProfileModbusCommitPendingActions, hm2FlushTables=hm2FlushTables, hm2FLMFreeMem=hm2FLMFreeMem, hm2DynFwDescription=hm2DynFwDescription, hm2DynFwRuleIfMappingTable=hm2DynFwRuleIfMappingTable, hm2DynFwProto=hm2DynFwProto, hm2DynFwRowStatus=hm2DynFwRowStatus, hm2L3SourceAddress=hm2L3SourceAddress, hm2DPIProfileModbusPendingActions=hm2DPIProfileModbusPendingActions, hm2DPIProfileOpcCommitPendingActions=hm2DPIProfileOpcCommitPendingActions, hm2L3CommitPendingActions=hm2L3CommitPendingActions, hm2L3RuleIfMappingTable=hm2L3RuleIfMappingTable, hm2L3TargetPort=hm2L3TargetPort, hm2DynFwRulePendingActions=hm2DynFwRulePendingActions, hm2FLMInterfaceIndex=hm2FLMInterfaceIndex, hm2DynFwIfmPriority=hm2DynFwIfmPriority, hm2L3Proto=hm2L3Proto, hm2L3IfmInterface=hm2L3IfmInterface, hm2DynFwRuleIndex=hm2DynFwRuleIndex, hm2L3StatsTotalPckDenDrop=hm2L3StatsTotalPckDenDrop, hm2L3Stats=hm2L3Stats, hm2L3RowStatus=hm2L3RowStatus, hm2DynFwTargetPort=hm2DynFwTargetPort, hm2L3RulePendingActions=hm2L3RulePendingActions, hm2L3TargetAddress=hm2L3TargetAddress, hm2L3Description=hm2L3Description, hm2L3IfmPriority=hm2L3IfmPriority, hm2DynFwStatsPacketCount=hm2DynFwStatsPacketCount, hm2DefaultPolicy=hm2DefaultPolicy, hm2DynFwIfmDirection=hm2DynFwIfmDirection, hm2DynFwRuleTable=hm2DynFwRuleTable, hm2DynFwTrap=hm2DynFwTrap, hm2L3Log=hm2L3Log, hm2DynFwRuleParams=hm2DynFwRuleParams, hm2FLMInterfaceTable=hm2FLMInterfaceTable, hm2DynFwStatsTtPckAccepted=hm2DynFwStatsTtPckAccepted, hm2L3Action=hm2L3Action, hm2FLMAdminState=hm2FLMAdminState, hm2DynFwStatsTtPck=hm2DynFwStatsTtPck, hm2DynFwStatsTtPckDenDrop=hm2DynFwStatsTtPckDenDrop, hm2DPIProfileOpcSanityCheck=hm2DPIProfileOpcSanityCheck, hm2DynFwRuleTables=hm2DynFwRuleTables, hm2DynFwAction=hm2DynFwAction, hm2DPIProfileOpcObjects=hm2DPIProfileOpcObjects, hm2FwGroups=hm2FwGroups, hm2DynFwTargetAddress=hm2DynFwTargetAddress, hm2DynFwStatsPacketSize=hm2DynFwStatsPacketSize, hm2FLMMaxEntries=hm2FLMMaxEntries, hm2DynFwStatsTables=hm2DynFwStatsTables, hm2FwGeneralSettings=hm2FwGeneralSettings, hm2L3StatsTotalPckAccepted=hm2L3StatsTotalPckAccepted, hm2DynFwRuleAppliedAndLoggedTrap=hm2DynFwRuleAppliedAndLoggedTrap, hm2L3IfmRowStatus=hm2L3IfmRowStatus, hm2L3StatsRuleTable=hm2L3StatsRuleTable, hm2DPIProfileModbusReset=hm2DPIProfileModbusReset, hm2FLML3Entries=hm2FLML3Entries, hm2DPIProfileOpcEntry=hm2DPIProfileOpcEntry, hm2FLMAppInfoString=hm2FLMAppInfoString, hm2DPIProfileModbusSanityCheck=hm2DPIProfileModbusSanityCheck, hm2L3StatsTotalPckSize=hm2L3StatsTotalPckSize, hm2L3StatsLastApplied=hm2L3StatsLastApplied, hm2DynFwStatsRuleTable=hm2DynFwStatsRuleTable, hm2DynFwRuleAppliedTrap=hm2DynFwRuleAppliedTrap, hm2DynFwIfmRuleIndex=hm2DynFwIfmRuleIndex, hm2FwObjects=hm2FwObjects, hm2DynFw=hm2DynFw, hm2L3RuleAppliedTrap=hm2L3RuleAppliedTrap, hm2L3StatsTotalPck=hm2L3StatsTotalPck, hm2L3RuleCount=hm2L3RuleCount, hm2DynFwIfmRowStatus=hm2DynFwIfmRowStatus, hm2DynFwRuleObjects=hm2DynFwRuleObjects, hm2DPIProfileModbusIndex=hm2DPIProfileModbusIndex, hm2FLMInterfaceRowStatus=hm2FLMInterfaceRowStatus, hm2DPIProfileModbusUnitIdentifierList=hm2DPIProfileModbusUnitIdentifierList, hm2L3Fw=hm2L3Fw, hm2L3Trap=hm2L3Trap, hm2ConnTrackValidateCheckSum=hm2ConnTrackValidateCheckSum, hm2L3GeneralStats=hm2L3GeneralStats, hm2L3RuleObjects=hm2L3RuleObjects, hm2L3RuleTables=hm2L3RuleTables, hm2DynFwStatsLastApplied=hm2DynFwStatsLastApplied, hm2DynFwRuleEntry=hm2DynFwRuleEntry, hm2DPIProfileOpcIndex=hm2DPIProfileOpcIndex, hm2DPIProfileIndex=hm2DPIProfileIndex, hm2L3StatsPacketCount=hm2L3StatsPacketCount, hm2L3RuleTable=hm2L3RuleTable, hm2FLMInterfaceEntry=hm2FLMInterfaceEntry, hm2L3StatsTables=hm2L3StatsTables, hm2DPIProfileOpcRowStatus=hm2DPIProfileOpcRowStatus, hm2DynFwIfmInterface=hm2DynFwIfmInterface, hm2DPIProfileModbusTable=hm2DPIProfileModbusTable, hm2DPIProfileModbusEntry=hm2DPIProfileModbusEntry, hm2DynFwMaxRules=hm2DynFwMaxRules, hm2DynFwLog=hm2DynFwLog, hm2DPIProfileModbusObjects=hm2DPIProfileModbusObjects, hm2DynFwStatsTtPckSize=hm2DynFwStatsTtPckSize, hm2L3IfmDirection=hm2L3IfmDirection, hm2DPIProfileOpcPendingActions=hm2DPIProfileOpcPendingActions, hm2FLMAction=hm2FLMAction, hm2L3RuleEntry=hm2L3RuleEntry, hm2FLMTables=hm2FLMTables, hm2L3MaxRules=hm2L3MaxRules, hm2FwNotificationsGroup=hm2FwNotificationsGroup, hm2DPIProfileModbusDescription=hm2DPIProfileModbusDescription, hm2DynFwGeneralStats=hm2DynFwGeneralStats, hm2FwCompliance=hm2FwCompliance, hm2L3RuleParams=hm2L3RuleParams, hm2FwConformance=hm2FwConformance, hm2DPIProfileOpcDescription=hm2DPIProfileOpcDescription, hm2DynFwIfMappingRuleCount=hm2DynFwIfMappingRuleCount, hm2DPIProfileModbusRowStatus=hm2DPIProfileModbusRowStatus, hm2DynFwSourcePort=hm2DynFwSourcePort, hm2DynFwRuleCount=hm2DynFwRuleCount, hm2FwLearningMode=hm2FwLearningMode, hm2FLMAppState=hm2FLMAppState, hm2DynFwStats=hm2DynFwStats, hm2L3RuleAppliedAndLoggedTrap=hm2L3RuleAppliedAndLoggedTrap)

#
# PySNMP MIB module HUAWEI-USERLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-USERLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, Counter32, ObjectIdentity, Gauge32, ModuleIdentity, iso, IpAddress, MibIdentifier, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "iso", "IpAddress", "MibIdentifier", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwUserLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18))
if mibBuilder.loadTexts: hwUserLogMIB.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hwUserLogMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwUserlogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1))
hwUserlogNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1))
hwUserlogNatVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatVersion.setStatus('current')
hwUserlogNatSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSyslog.setStatus('current')
hwUserlogNatSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSourceIP.setStatus('current')
hwUserlogNatFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatFlowBegin.setStatus('current')
hwUserlogNatActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatActiveTime.setStatus('current')
hwUserlogNatSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6), )
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoTable.setStatus('current')
hwUserlogNatSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoEntry.setStatus('current')
hwUserlogNatCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatCfgSlotNumber.setStatus('current')
hwUserlogNatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatEnable.setStatus('current')
hwUserlogNatAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatAclNumber.setStatus('current')
hwUserlogNatHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatHostAddress.setStatus('current')
hwUserlogNatUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatUdpPort.setStatus('current')
hwUserlogNatSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7), )
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoTable.setStatus('current')
hwUserlogNatSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogNatRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoEntry.setStatus('current')
hwUserlogNatRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatRunSlotNumber.setStatus('current')
hwUserlogNatTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalEntries.setStatus('current')
hwUserlogNatTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalPackets.setStatus('current')
hwUserlogNatFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedEntries.setStatus('current')
hwUserlogNatFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedPackets.setStatus('current')
hwUserlogNatClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatClearRunStat.setStatus('current')
hwUserlogFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2))
hwUserlogFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowVersion.setStatus('current')
hwUserlogFlowSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSyslog.setStatus('current')
hwUserlogFlowSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSourceIP.setStatus('current')
hwUserlogFlowFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowFlowBegin.setStatus('current')
hwUserlogFlowActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowActiveTime.setStatus('current')
hwUserlogFlowSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6), )
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoTable.setStatus('current')
hwUserlogFlowSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoEntry.setStatus('current')
hwUserlogFlowCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowCfgSlotNumber.setStatus('current')
hwUserlogFlowEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowEnable.setStatus('current')
hwUserlogFlowAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowAclNumber.setStatus('current')
hwUserlogFlowHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowHostAddress.setStatus('current')
hwUserlogFlowUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowUdpPort.setStatus('current')
hwUserlogFlowSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7), )
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoTable.setStatus('current')
hwUserlogFlowSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogFlowRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoEntry.setStatus('current')
hwUserlogFlowRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowRunSlotNumber.setStatus('current')
hwUserlogFlowTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalEntries.setStatus('current')
hwUserlogFlowTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalPackets.setStatus('current')
hwUserlogFlowFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedEntries.setStatus('current')
hwUserlogFlowFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedPackets.setStatus('current')
hwUserlogFlowClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowClearRunStat.setStatus('current')
hwUserlogAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3))
hwUserlogAccessVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessVersion.setStatus('current')
hwUserlogAccessSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSyslog.setStatus('current')
hwUserlogAccessSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSourceIP.setStatus('current')
hwUserlogAccessSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4), )
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoTable.setStatus('current')
hwUserlogAccessSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoEntry.setStatus('current')
hwUserlogAccessCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessCfgSlotNumber.setStatus('current')
hwUserlogAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessEnable.setStatus('current')
hwUserlogAccessHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessHostAddress.setStatus('current')
hwUserlogAccessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessUdpPort.setStatus('current')
hwUserlogAccessSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5), )
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoTable.setStatus('current')
hwUserlogAccessSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogAccessRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoEntry.setStatus('current')
hwUserlogAccessRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessRunSlotNumber.setStatus('current')
hwUserlogAccessTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalEntries.setStatus('current')
hwUserlogAccessTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalPackets.setStatus('current')
hwUserlogAccessFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedEntries.setStatus('current')
hwUserlogAccessFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedPackets.setStatus('current')
hwUserlogAccessClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessClearRunStat.setStatus('current')
hwUserlogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 2))
hwUserlogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3))
hwUserlogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 1))
hwUserlogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 1, 1)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogCompliance = hwUserlogCompliance.setStatus('current')
hwUserlogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2))
hwUserlogMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 1)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogMandatoryGroup = hwUserlogMandatoryGroup.setStatus('current')
hwUserlogConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 2)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFlowBegin"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatActiveTime"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatAclNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFlowBegin"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowActiveTime"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowAclNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogConfigGroup = hwUserlogConfigGroup.setStatus('current')
hwUserlogInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 3)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFailedPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogInfoGroup = hwUserlogInfoGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-USERLOG-MIB", hwUserlogFlowVersion=hwUserlogFlowVersion, hwUserlogAccessFailedPackets=hwUserlogAccessFailedPackets, hwUserlogAccessFailedEntries=hwUserlogAccessFailedEntries, hwUserlogAccessObjects=hwUserlogAccessObjects, hwUserlogNatRunSlotNumber=hwUserlogNatRunSlotNumber, hwUserlogNatClearRunStat=hwUserlogNatClearRunStat, hwUserlogObjects=hwUserlogObjects, hwUserlogFlowSlotCfgInfoEntry=hwUserlogFlowSlotCfgInfoEntry, hwUserlogAccessSlotCfgInfoEntry=hwUserlogAccessSlotCfgInfoEntry, hwUserlogNatSourceIP=hwUserlogNatSourceIP, hwUserlogNatFlowBegin=hwUserlogNatFlowBegin, hwUserlogFlowSlotCfgInfoTable=hwUserlogFlowSlotCfgInfoTable, hwUserlogCompliance=hwUserlogCompliance, hwUserlogNatSlotCfgInfoEntry=hwUserlogNatSlotCfgInfoEntry, hwUserlogNatObjects=hwUserlogNatObjects, hwUserlogFlowHostAddress=hwUserlogFlowHostAddress, hwUserlogCompliances=hwUserlogCompliances, hwUserlogFlowSlotRunInfoTable=hwUserlogFlowSlotRunInfoTable, hwUserlogFlowUdpPort=hwUserlogFlowUdpPort, hwUserlogFlowSlotRunInfoEntry=hwUserlogFlowSlotRunInfoEntry, hwUserlogNatTotalPackets=hwUserlogNatTotalPackets, hwUserlogFlowTotalPackets=hwUserlogFlowTotalPackets, hwUserlogFlowFailedEntries=hwUserlogFlowFailedEntries, hwUserlogAccessUdpPort=hwUserlogAccessUdpPort, hwUserLogMIB=hwUserLogMIB, hwUserlogNatFailedEntries=hwUserlogNatFailedEntries, hwUserlogAccessSourceIP=hwUserlogAccessSourceIP, hwUserlogAccessHostAddress=hwUserlogAccessHostAddress, hwUserlogFlowFlowBegin=hwUserlogFlowFlowBegin, hwUserlogAccessSlotRunInfoEntry=hwUserlogAccessSlotRunInfoEntry, hwUserlogConformance=hwUserlogConformance, hwUserlogNatSlotCfgInfoTable=hwUserlogNatSlotCfgInfoTable, hwUserlogNatVersion=hwUserlogNatVersion, hwUserlogNatSlotRunInfoTable=hwUserlogNatSlotRunInfoTable, hwUserlogNatFailedPackets=hwUserlogNatFailedPackets, hwUserlogAccessSyslog=hwUserlogAccessSyslog, hwUserlogNatTotalEntries=hwUserlogNatTotalEntries, hwUserlogMandatoryGroup=hwUserlogMandatoryGroup, PYSNMP_MODULE_ID=hwUserLogMIB, hwUserlogNatHostAddress=hwUserlogNatHostAddress, hwUserlogFlowRunSlotNumber=hwUserlogFlowRunSlotNumber, hwUserlogGroups=hwUserlogGroups, hwUserlogNatSyslog=hwUserlogNatSyslog, hwUserlogAccessSlotCfgInfoTable=hwUserlogAccessSlotCfgInfoTable, hwUserlogAccessEnable=hwUserlogAccessEnable, hwUserlogAccessVersion=hwUserlogAccessVersion, hwUserlogAccessCfgSlotNumber=hwUserlogAccessCfgSlotNumber, hwUserlogAccessSlotRunInfoTable=hwUserlogAccessSlotRunInfoTable, hwUserlogFlowAclNumber=hwUserlogFlowAclNumber, hwUserlogAccessRunSlotNumber=hwUserlogAccessRunSlotNumber, hwUserlogNatActiveTime=hwUserlogNatActiveTime, hwUserlogInfoGroup=hwUserlogInfoGroup, hwUserlogFlowActiveTime=hwUserlogFlowActiveTime, hwUserlogNatAclNumber=hwUserlogNatAclNumber, hwUserlogFlowFailedPackets=hwUserlogFlowFailedPackets, hwUserlogNotifications=hwUserlogNotifications, hwUserlogNatEnable=hwUserlogNatEnable, hwUserlogNatUdpPort=hwUserlogNatUdpPort, hwUserlogAccessTotalPackets=hwUserlogAccessTotalPackets, hwUserlogNatCfgSlotNumber=hwUserlogNatCfgSlotNumber, hwUserlogAccessClearRunStat=hwUserlogAccessClearRunStat, hwUserlogFlowClearRunStat=hwUserlogFlowClearRunStat, hwUserlogFlowEnable=hwUserlogFlowEnable, hwUserlogFlowTotalEntries=hwUserlogFlowTotalEntries, hwUserlogAccessTotalEntries=hwUserlogAccessTotalEntries, hwUserlogFlowSyslog=hwUserlogFlowSyslog, hwUserlogConfigGroup=hwUserlogConfigGroup, hwUserlogFlowObjects=hwUserlogFlowObjects, hwUserlogNatSlotRunInfoEntry=hwUserlogNatSlotRunInfoEntry, hwUserlogFlowSourceIP=hwUserlogFlowSourceIP, hwUserlogFlowCfgSlotNumber=hwUserlogFlowCfgSlotNumber)

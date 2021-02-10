#
# PySNMP MIB module CENTILLION-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-MCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
PortId, Boolean, EnableIndicator, CardId, StatusIndicator, sysConfig = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "PortId", "Boolean", "EnableIndicator", "CardId", "StatusIndicator", "sysConfig")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, Counter32, NotificationType, Unsigned32, iso, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "Counter32", "NotificationType", "Unsigned32", "iso", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

vlan = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31))
vlanMcastProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1))
vlanIGMPProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1))
vlanIGMPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1))
igmpGeneralConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1), )
if mibBuilder.loadTexts: igmpGeneralConfigTable.setStatus('mandatory')
igmpGeneralConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpGeneralConfigVlanId"))
if mibBuilder.loadTexts: igmpGeneralConfigEntry.setStatus('mandatory')
igmpGeneralConfigVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGeneralConfigVlanId.setStatus('mandatory')
igmpGeneralConfigPseudoQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 2), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigPseudoQuery.setStatus('mandatory')
igmpGeneralConfigIrapQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 3), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigIrapQuery.setStatus('mandatory')
igmpGeneralConfigIgmpSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 4), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigIgmpSupport.setStatus('mandatory')
igmpGeneralConfigMaxGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigMaxGroup.setStatus('mandatory')
igmpTimerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2), )
if mibBuilder.loadTexts: igmpTimerConfigTable.setStatus('mandatory')
igmpTimerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpTimerConfigVlanId"))
if mibBuilder.loadTexts: igmpTimerConfigEntry.setStatus('mandatory')
igmpTimerConfigVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpTimerConfigVlanId.setStatus('mandatory')
igmpTimerConfigTimerRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 2), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigTimerRobustness.setStatus('mandatory')
igmpTimerConfigQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 3), Integer32().clone(125)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigQueryInterval.setStatus('mandatory')
igmpTimerConfigQueryResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 4), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigQueryResponse.setStatus('mandatory')
igmpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3), )
if mibBuilder.loadTexts: igmpGroupTable.setStatus('mandatory')
igmpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpGroupVlanId"), (0, "CENTILLION-MCAST-MIB", "igmpGroupStatic"), (0, "CENTILLION-MCAST-MIB", "igmpGroupAddress"))
if mibBuilder.loadTexts: igmpGroupEntry.setStatus('mandatory')
igmpGroupVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupVlanId.setStatus('mandatory')
igmpGroupStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 2), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupStatic.setStatus('mandatory')
igmpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupAddress.setStatus('mandatory')
igmpGroupIncluded = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGroupIncluded.setStatus('mandatory')
igmpGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 5), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGroupStatus.setStatus('mandatory')
igmpRouterPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4), )
if mibBuilder.loadTexts: igmpRouterPortTable.setStatus('mandatory')
igmpRouterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpRouterPortVlanId"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortStatic"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortCard"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortPort"))
if mibBuilder.loadTexts: igmpRouterPortEntry.setStatus('mandatory')
igmpRouterPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortVlanId.setStatus('mandatory')
igmpRouterPortStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 2), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortStatic.setStatus('mandatory')
igmpRouterPortCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortCard.setStatus('mandatory')
igmpRouterPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortPort.setStatus('mandatory')
igmpRouterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 5), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpRouterPortStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-MCAST-MIB", igmpGroupStatus=igmpGroupStatus, igmpTimerConfigTimerRobustness=igmpTimerConfigTimerRobustness, igmpTimerConfigQueryInterval=igmpTimerConfigQueryInterval, igmpRouterPortTable=igmpRouterPortTable, igmpTimerConfigTable=igmpTimerConfigTable, igmpGeneralConfigMaxGroup=igmpGeneralConfigMaxGroup, igmpGroupEntry=igmpGroupEntry, igmpRouterPortStatus=igmpRouterPortStatus, VlanId=VlanId, igmpGeneralConfigPseudoQuery=igmpGeneralConfigPseudoQuery, igmpGroupStatic=igmpGroupStatic, igmpGeneralConfigEntry=igmpGeneralConfigEntry, igmpGroupTable=igmpGroupTable, vlan=vlan, vlanIGMPConfig=vlanIGMPConfig, igmpTimerConfigVlanId=igmpTimerConfigVlanId, igmpRouterPortVlanId=igmpRouterPortVlanId, igmpRouterPortEntry=igmpRouterPortEntry, igmpGeneralConfigIgmpSupport=igmpGeneralConfigIgmpSupport, igmpGroupVlanId=igmpGroupVlanId, igmpGroupIncluded=igmpGroupIncluded, igmpTimerConfigEntry=igmpTimerConfigEntry, vlanIGMPProtocolGroup=vlanIGMPProtocolGroup, vlanMcastProtocolGroup=vlanMcastProtocolGroup, igmpTimerConfigQueryResponse=igmpTimerConfigQueryResponse, igmpGroupAddress=igmpGroupAddress, igmpRouterPortPort=igmpRouterPortPort, igmpRouterPortStatic=igmpRouterPortStatic, igmpGeneralConfigIrapQuery=igmpGeneralConfigIrapQuery, igmpRouterPortCard=igmpRouterPortCard, igmpGeneralConfigTable=igmpGeneralConfigTable, igmpGeneralConfigVlanId=igmpGeneralConfigVlanId)
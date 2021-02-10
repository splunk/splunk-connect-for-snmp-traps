#
# PySNMP MIB module ATI-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATI-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Unsigned32, NotificationType, Bits, TimeTicks, enterprises, ObjectIdentity, MibIdentifier, Counter64, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Unsigned32", "NotificationType", "Bits", "TimeTicks", "enterprises", "ObjectIdentity", "MibIdentifier", "Counter64", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

alliedTelesyn = MibIdentifier((1, 3, 6, 1, 4, 1, 207))
mibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8))
switchMib = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5))
atiBridgeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10))
atbrBase = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1))
atbrStp = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2))
atbrSr = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 3))
atbrTp = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4))
atbrStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5))
atbrBaseTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1), )
if mibBuilder.loadTexts: atbrBaseTable.setStatus('mandatory')
atbrBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrBaseLanId"))
if mibBuilder.loadTexts: atbrBaseEntry.setStatus('mandatory')
atbrBaseLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBaseLanId.setStatus('mandatory')
atbrBaseBridgeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBaseBridgeAddress.setStatus('mandatory')
atbrBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBaseNumPorts.setStatus('mandatory')
atbrBaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBaseType.setStatus('mandatory')
atbrBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4), )
if mibBuilder.loadTexts: atbrBasePortTable.setStatus('mandatory')
atbrBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrBasePortLanId"), (0, "ATI-BRIDGE-MIB", "atbrBasePort"))
if mibBuilder.loadTexts: atbrBasePortEntry.setStatus('mandatory')
atbrBasePortLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePortLanId.setStatus('mandatory')
atbrBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePort.setStatus('mandatory')
atbrBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePortIfIndex.setStatus('mandatory')
atbrBasePortCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePortCircuit.setStatus('mandatory')
atbrBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePortDelayExceededDiscards.setStatus('mandatory')
atbrBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrBasePortMtuExceededDiscards.setStatus('mandatory')
atbrStpTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1), )
if mibBuilder.loadTexts: atbrStpTable.setStatus('mandatory')
atbrStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrStpLanId"))
if mibBuilder.loadTexts: atbrStpEntry.setStatus('mandatory')
atbrStpLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpLanId.setStatus('mandatory')
atbrStpProtocolSpecification = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpProtocolSpecification.setStatus('mandatory')
atbrStpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpPriority.setStatus('mandatory')
atbrStpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpTimeSinceTopologyChange.setStatus('mandatory')
atbrStpTopChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpTopChanges.setStatus('mandatory')
atbrStpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpDesignatedRoot.setStatus('mandatory')
atbrStpRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpRootCost.setStatus('mandatory')
atbrStpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpRootPort.setStatus('mandatory')
atbrStpMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 9), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpMaxAge.setStatus('mandatory')
atbrStpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 10), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpHelloTime.setStatus('mandatory')
atbrStpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpHoldTime.setStatus('mandatory')
atbrStpForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 12), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpForwardDelay.setStatus('mandatory')
atbrStpBridgeMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpBridgeMaxAge.setStatus('mandatory')
atbrStpBridgeHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpBridgeHelloTime.setStatus('mandatory')
atbrStpBridgeForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 15), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpBridgeForwardDelay.setStatus('mandatory')
atbrStpPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15), )
if mibBuilder.loadTexts: atbrStpPortTable.setStatus('mandatory')
atbrStpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrStpPortLanId"), (0, "ATI-BRIDGE-MIB", "atbrStpPort"))
if mibBuilder.loadTexts: atbrStpPortEntry.setStatus('mandatory')
atbrStpPortLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortLanId.setStatus('mandatory')
atbrStpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPort.setStatus('mandatory')
atbrStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpPortPriority.setStatus('mandatory')
atbrStpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortState.setStatus('mandatory')
atbrStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpPortEnable.setStatus('mandatory')
atbrStpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStpPortPathCost.setStatus('mandatory')
atbrStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 7), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortDesignatedRoot.setStatus('mandatory')
atbrStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortDesignatedCost.setStatus('mandatory')
atbrStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 9), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortDesignatedBridge.setStatus('mandatory')
atbrStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortDesignatedPort.setStatus('mandatory')
atbrStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStpPortForwardTransitions.setStatus('mandatory')
atbrTpTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1), )
if mibBuilder.loadTexts: atbrTpTable.setStatus('mandatory')
atbrTpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrTpLanId"))
if mibBuilder.loadTexts: atbrTpEntry.setStatus('mandatory')
atbrTpLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpLanId.setStatus('mandatory')
atbrTpLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpLearnedEntryDiscards.setStatus('mandatory')
atbrTpAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrTpAgingTime.setStatus('mandatory')
atbrTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3), )
if mibBuilder.loadTexts: atbrTpFdbTable.setStatus('mandatory')
atbrTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrTpFdbLanId"), (0, "ATI-BRIDGE-MIB", "atbrTpFdbAddress"))
if mibBuilder.loadTexts: atbrTpFdbEntry.setStatus('mandatory')
atbrTpFdbLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpFdbLanId.setStatus('mandatory')
atbrTpFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpFdbAddress.setStatus('mandatory')
atbrTpFdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpFdbPort.setStatus('mandatory')
atbrTpFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("inactive", 1), ("le-arp-pending", 2), ("vcc-setup-pending", 3), ("vlan-resolve-pending", 4), ("join-pending", 5), ("active", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpFdbStatus.setStatus('mandatory')
atbrTpPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4), )
if mibBuilder.loadTexts: atbrTpPortTable.setStatus('mandatory')
atbrTpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrTpPortLanId"), (0, "ATI-BRIDGE-MIB", "atbrTpPort"))
if mibBuilder.loadTexts: atbrTpPortEntry.setStatus('mandatory')
atbrTpPortLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPortLanId.setStatus('mandatory')
atbrTpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPort.setStatus('mandatory')
atbrTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPortMaxInfo.setStatus('mandatory')
atbrTpPortInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPortInFrames.setStatus('mandatory')
atbrTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPortOutFrames.setStatus('mandatory')
atbrTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrTpPortInDiscards.setStatus('mandatory')
atbrStaticTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1), )
if mibBuilder.loadTexts: atbrStaticTable.setStatus('mandatory')
atbrStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1), ).setIndexNames((0, "ATI-BRIDGE-MIB", "atbrStaticLanId"), (0, "ATI-BRIDGE-MIB", "atbrStaticAddress"), (0, "ATI-BRIDGE-MIB", "atbrStaticReceivePort"))
if mibBuilder.loadTexts: atbrStaticEntry.setStatus('mandatory')
atbrStaticLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atbrStaticLanId.setStatus('mandatory')
atbrStaticAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStaticAddress.setStatus('mandatory')
atbrStaticReceivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStaticReceivePort.setStatus('mandatory')
atbrStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStaticAllowedToGoTo.setStatus('mandatory')
atbrStaticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atbrStaticStatus.setStatus('mandatory')
newRoot = NotificationType((1, 3, 6, 1, 4, 1, 207) + (0,101))
topologyChange = NotificationType((1, 3, 6, 1, 4, 1, 207) + (0,102))
mibBuilder.exportSymbols("ATI-BRIDGE-MIB", atbrStpRootCost=atbrStpRootCost, atbrStpPortPathCost=atbrStpPortPathCost, atbrStpHelloTime=atbrStpHelloTime, atbrTpLanId=atbrTpLanId, atbrTpAgingTime=atbrTpAgingTime, atbrTpPortMaxInfo=atbrTpPortMaxInfo, atbrStpHoldTime=atbrStpHoldTime, atbrTpPortInDiscards=atbrTpPortInDiscards, atbrTpEntry=atbrTpEntry, atbrStpPortForwardTransitions=atbrStpPortForwardTransitions, Timeout=Timeout, atbrTpPort=atbrTpPort, atbrStp=atbrStp, atbrStpPortEntry=atbrStpPortEntry, atbrStpDesignatedRoot=atbrStpDesignatedRoot, atbrBaseLanId=atbrBaseLanId, atbrTpPortInFrames=atbrTpPortInFrames, atbrBaseEntry=atbrBaseEntry, atbrStpPortDesignatedPort=atbrStpPortDesignatedPort, atbrStpLanId=atbrStpLanId, atbrTpPortEntry=atbrTpPortEntry, atbrBasePortDelayExceededDiscards=atbrBasePortDelayExceededDiscards, atbrStpPriority=atbrStpPriority, atbrBase=atbrBase, atbrStaticReceivePort=atbrStaticReceivePort, atbrTpFdbTable=atbrTpFdbTable, atbrBaseType=atbrBaseType, atbrTpFdbAddress=atbrTpFdbAddress, atbrStpBridgeHelloTime=atbrStpBridgeHelloTime, atbrSr=atbrSr, atbrStpBridgeMaxAge=atbrStpBridgeMaxAge, atbrStpPortState=atbrStpPortState, atbrBasePortEntry=atbrBasePortEntry, atbrTpPortLanId=atbrTpPortLanId, atbrBasePortCircuit=atbrBasePortCircuit, MacAddress=MacAddress, atbrStaticAllowedToGoTo=atbrStaticAllowedToGoTo, atbrTpTable=atbrTpTable, atbrStpProtocolSpecification=atbrStpProtocolSpecification, atbrStpRootPort=atbrStpRootPort, atbrStaticTable=atbrStaticTable, atbrBaseNumPorts=atbrBaseNumPorts, atbrBasePortIfIndex=atbrBasePortIfIndex, alliedTelesyn=alliedTelesyn, atbrStatic=atbrStatic, atbrStpPortPriority=atbrStpPortPriority, atbrStaticLanId=atbrStaticLanId, atbrStpPortTable=atbrStpPortTable, atbrStpPortLanId=atbrStpPortLanId, atbrTpFdbLanId=atbrTpFdbLanId, atbrStpPortDesignatedRoot=atbrStpPortDesignatedRoot, atbrStpTopChanges=atbrStpTopChanges, newRoot=newRoot, atbrTpLearnedEntryDiscards=atbrTpLearnedEntryDiscards, atbrStaticEntry=atbrStaticEntry, atbrTpPortOutFrames=atbrTpPortOutFrames, atbrStpMaxAge=atbrStpMaxAge, atbrStpForwardDelay=atbrStpForwardDelay, mibObject=mibObject, switchMib=switchMib, atbrBaseBridgeAddress=atbrBaseBridgeAddress, atbrTp=atbrTp, BridgeId=BridgeId, atbrStpPortDesignatedBridge=atbrStpPortDesignatedBridge, atbrTpFdbEntry=atbrTpFdbEntry, atbrStpPortEnable=atbrStpPortEnable, atbrStpPort=atbrStpPort, topologyChange=topologyChange, atbrStpTable=atbrStpTable, atbrStaticStatus=atbrStaticStatus, atbrBasePortMtuExceededDiscards=atbrBasePortMtuExceededDiscards, atiBridgeMib=atiBridgeMib, atbrTpFdbPort=atbrTpFdbPort, atbrBasePortLanId=atbrBasePortLanId, atbrStpEntry=atbrStpEntry, atbrTpFdbStatus=atbrTpFdbStatus, atbrBaseTable=atbrBaseTable, atbrStpTimeSinceTopologyChange=atbrStpTimeSinceTopologyChange, atbrTpPortTable=atbrTpPortTable, atbrStpPortDesignatedCost=atbrStpPortDesignatedCost, atbrStpBridgeForwardDelay=atbrStpBridgeForwardDelay, atbrStaticAddress=atbrStaticAddress, atbrBasePortTable=atbrBasePortTable, atbrBasePort=atbrBasePort)

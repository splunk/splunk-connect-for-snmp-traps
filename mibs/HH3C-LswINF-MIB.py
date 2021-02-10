#
# PySNMP MIB module HH3C-LswINF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswINF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, NotificationType, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, Gauge32, IpAddress, TimeTicks, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "MibIdentifier", "Integer32")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
hh3cLswL2InfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5))
hh3cLswL2InfMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hh3cLswL2InfMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswL2InfMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class PortList(TextualConvention, OctetString):
    status = 'current'

class VlanIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class DropDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disable", 1), ("enableInbound", 2), ("enableOutbound", 3), ("enableBoth", 4))

class SpeedModeFlag(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("s10M", 0), ("s100M", 1), ("s1000M", 2), ("s10000M", 3), ("s24000M", 4))

hh3cLswExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1))
hh3cifXXTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1), )
if mibBuilder.loadTexts: hh3cifXXTable.setStatus('current')
hh3cifXXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1), )
ifEntry.registerAugmentions(("HH3C-LswINF-MIB", "hh3cifXXEntry"))
hh3cifXXEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cifXXEntry.setStatus('current')
hh3cifUnBoundPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifUnBoundPort.setStatus('current')
hh3cifISPhyPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifISPhyPort.setStatus('current')
hh3cifAggregatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifAggregatePort.setStatus('current')
hh3cifMirrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifMirrorPort.setStatus('current')
hh3cifVLANType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vLANTrunk", 1), ("access", 2), ("hybrid", 3), ("fabric", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVLANType.setStatus('current')
hh3cifMcastControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifMcastControl.setStatus('current')
hh3cifFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifFlowControl.setStatus('current')
hh3cifSrcMacControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifSrcMacControl.setStatus('current')
hh3cifClearStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifClearStat.setStatus('current')
hh3cifXXBasePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifXXBasePortIndex.setStatus('current')
hh3cifXXDevPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifXXDevPortIndex.setStatus('current')
hh3cifPpsMcastControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifPpsMcastControl.setStatus('current')
hh3cifPpsBcastDisValControl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifPpsBcastDisValControl.setStatus('current')
hh3cifUniSuppressionStep = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifUniSuppressionStep.setStatus('current')
hh3cifPpsUniSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifPpsUniSuppressionMax.setStatus('current')
hh3cifMulSuppressionStep = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifMulSuppressionStep.setStatus('current')
hh3cifPpsMulSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifPpsMulSuppressionMax.setStatus('current')
hh3cifUniSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifUniSuppression.setStatus('current')
hh3cifPpsUniSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifPpsUniSuppression.setStatus('current')
hh3cifMulSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifMulSuppression.setStatus('current')
hh3cifPpsMulSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifPpsMulSuppression.setStatus('current')
hh3cifComboActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fiber", 1), ("copper", 2), ("na", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifComboActivePort.setStatus('obsolete')
hh3cifBMbpsMulSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBMbpsMulSuppressionMax.setStatus('current')
hh3cifBMbpsMulSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifBMbpsMulSuppression.setStatus('current')
hh3cifBKbpsMulSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBKbpsMulSuppressionMax.setStatus('current')
hh3cifBKbpsMulSuppressionStep = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBKbpsMulSuppressionStep.setStatus('current')
hh3cifBKbpsMulSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifBKbpsMulSuppression.setStatus('current')
hh3cifUnknownPacketDropMul = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 28), DropDirection().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifUnknownPacketDropMul.setStatus('current')
hh3cifUnknownPacketDropUni = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 29), DropDirection().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifUnknownPacketDropUni.setStatus('current')
hh3cifBMbpsUniSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBMbpsUniSuppressionMax.setStatus('current')
hh3cifBMbpsUniSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifBMbpsUniSuppression.setStatus('current')
hh3cifBKbpsUniSuppressionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBKbpsUniSuppressionMax.setStatus('current')
hh3cifBKbpsUniSuppressionStep = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifBKbpsUniSuppressionStep.setStatus('current')
hh3cifBKbpsUniSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifBKbpsUniSuppression.setStatus('current')
hh3cifOutPayloadOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifOutPayloadOctets.setStatus('current')
hh3cifInPayloadOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifInPayloadOctets.setStatus('current')
hh3cifInErrorPktsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifInErrorPktsRate.setStatus('current')
hh3cifInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifInPkts.setStatus('current')
hh3cifInNormalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifInNormalPkts.setStatus('current')
hh3cifOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifOutPkts.setStatus('current')
hh3cifAggregateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2), )
if mibBuilder.loadTexts: hh3cifAggregateTable.setStatus('current')
hh3cifAggregateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1), ).setIndexNames((0, "HH3C-LswINF-MIB", "hh3cifAggregatePortIndex"))
if mibBuilder.loadTexts: hh3cifAggregateEntry.setStatus('current')
hh3cifAggregatePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifAggregatePortIndex.setStatus('current')
hh3cifAggregatePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifAggregatePortName.setStatus('current')
hh3cifAggregatePortListPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifAggregatePortListPorts.setStatus('current')
hh3cifAggregateModel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("both", 2), ("round-robin", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifAggregateModel.setStatus('current')
hh3cifAggregateOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cifAggregateOperStatus.setStatus('current')
hh3cifHybridPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3), )
if mibBuilder.loadTexts: hh3cifHybridPortTable.setStatus('current')
hh3cifHybridPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1), ).setIndexNames((0, "HH3C-LswINF-MIB", "hh3cifHybridPortIndex"))
if mibBuilder.loadTexts: hh3cifHybridPortEntry.setStatus('current')
hh3cifHybridPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifHybridPortIndex.setStatus('current')
hh3cifHybridTaggedVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifHybridTaggedVlanListLow.setStatus('current')
hh3cifHybridTaggedVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifHybridTaggedVlanListHigh.setStatus('current')
hh3cifHybridUnTaggedVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifHybridUnTaggedVlanListLow.setStatus('current')
hh3cifHybridUnTaggedVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifHybridUnTaggedVlanListHigh.setStatus('current')
hh3cifComboPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4), )
if mibBuilder.loadTexts: hh3cifComboPortTable.setStatus('current')
hh3cifComboPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1), ).setIndexNames((0, "HH3C-LswINF-MIB", "hh3cifComboPortIndex"))
if mibBuilder.loadTexts: hh3cifComboPortEntry.setStatus('current')
hh3cifComboPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifComboPortIndex.setStatus('current')
hh3cifComboPortCurActive = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fiber", 1), ("copper", 2), ("na", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifComboPortCurActive.setStatus('current')
hh3cLswL2InfMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1))
hh3cSlotPortMax = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSlotPortMax.setStatus('current')
hh3cSwitchPortMax = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSwitchPortMax.setStatus('current')
hh3cifVLANTrunkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3), )
if mibBuilder.loadTexts: hh3cifVLANTrunkStatusTable.setStatus('current')
hh3cifVLANTrunkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1), ).setIndexNames((0, "HH3C-LswINF-MIB", "hh3cifVLANTrunkIndex"))
if mibBuilder.loadTexts: hh3cifVLANTrunkStatusEntry.setStatus('current')
hh3cifVLANTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifVLANTrunkIndex.setStatus('current')
hh3cifVLANTrunkGvrpRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("fixed", 2), ("forbidden", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVLANTrunkGvrpRegistration.setStatus('current')
hh3cifVLANTrunkPassListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifVLANTrunkPassListLow.setStatus('current')
hh3cifVLANTrunkPassListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifVLANTrunkPassListHigh.setStatus('current')
hh3cifVLANTrunkAllowListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVLANTrunkAllowListLow.setStatus('current')
hh3cifVLANTrunkAllowListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVLANTrunkAllowListHigh.setStatus('current')
hh3cethernetTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4), )
if mibBuilder.loadTexts: hh3cethernetTable.setStatus('current')
hh3cethernetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1), )
ifEntry.registerAugmentions(("HH3C-LswINF-MIB", "hh3cethernetEntry"))
hh3cethernetEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cethernetEntry.setStatus('current')
hh3cifEthernetDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetDuplex.setStatus('current')
hh3cifEthernetMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetMTU.setStatus('current')
hh3cifEthernetSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 10, 100, 1000, 10000, 24000))).clone(namedValues=NamedValues(("auto", 0), ("s10M", 10), ("s100M", 100), ("s1000M", 1000), ("s10000M", 10000), ("s24000M", 24000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetSpeed.setStatus('current')
hh3cifEthernetMdi = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mdi-ii", 1), ("mdi-x", 2), ("mdi-auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetMdi.setStatus('current')
hh3cMaxMacLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMaxMacLearn.setStatus('current')
hh3cifMacAddressLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifMacAddressLearn.setStatus('current')
hh3cifEthernetTest = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("test", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetTest.setStatus('current')
hh3cifMacAddrLearnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("iVL", 1), ("sVL", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifMacAddrLearnMode.setStatus('current')
hh3cifEthernetFlowInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetFlowInterval.setStatus('current')
hh3cifEthernetIsolate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 13), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetIsolate.setStatus('current')
hh3cifVlanVPNStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVlanVPNStatus.setStatus('current')
hh3cifVlanVPNUplinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVlanVPNUplinkStatus.setStatus('current')
hh3cifVlanVPNTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifVlanVPNTPID.setStatus('current')
hh3cifIsolateGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifIsolateGroupID.setStatus('current')
hh3cifisUplinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifisUplinkPort.setStatus('current')
hh3cifEthernetAutoSpeedMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 19), SpeedModeFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifEthernetAutoSpeedMask.setStatus('current')
hh3cifEthernetAutoSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 20), SpeedModeFlag()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifEthernetAutoSpeed.setStatus('current')
hh3cIsolateGroupMax = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIsolateGroupMax.setStatus('current')
hh3cGlobalBroadcastMaxPps = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14881000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cGlobalBroadcastMaxPps.setStatus('current')
hh3cGlobalBroadcastMaxRatio = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cGlobalBroadcastMaxRatio.setStatus('current')
hh3cBpduTunnelStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cBpduTunnelStatus.setStatus('current')
hh3cVlanVPNTPIDMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port-based", 1), ("global", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanVPNTPIDMode.setStatus('current')
hh3cVlanVPNTPID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanVPNTPID.setStatus('current')
hh3cPortIsolateGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11), )
if mibBuilder.loadTexts: hh3cPortIsolateGroupTable.setStatus('current')
hh3cPortIsolateGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1), ).setIndexNames((0, "HH3C-LswINF-MIB", "hh3cPortIsolateGroupIndex"))
if mibBuilder.loadTexts: hh3cPortIsolateGroupEntry.setStatus('current')
hh3cPortIsolateGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cPortIsolateGroupIndex.setStatus('current')
hh3cPortIsolateUplinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortIsolateUplinkIfIndex.setStatus('current')
hh3cPortIsolateGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortIsolateGroupRowStatus.setStatus('current')
hh3cPortIsolateGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortIsolateGroupDescription.setStatus('current')
hh3cMaxMacLearnRange = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMaxMacLearnRange.setStatus('current')
mibBuilder.exportSymbols("HH3C-LswINF-MIB", hh3cifUnknownPacketDropMul=hh3cifUnknownPacketDropMul, hh3cifAggregateModel=hh3cifAggregateModel, hh3cifEthernetAutoSpeedMask=hh3cifEthernetAutoSpeedMask, hh3cifPpsMcastControl=hh3cifPpsMcastControl, hh3cPortIsolateGroupDescription=hh3cPortIsolateGroupDescription, hh3cifVLANTrunkStatusEntry=hh3cifVLANTrunkStatusEntry, hh3cifBMbpsMulSuppressionMax=hh3cifBMbpsMulSuppressionMax, hh3cifMirrorPort=hh3cifMirrorPort, hh3cifMulSuppression=hh3cifMulSuppression, hh3cifAggregatePortListPorts=hh3cifAggregatePortListPorts, hh3cifIsolateGroupID=hh3cifIsolateGroupID, hh3cPortIsolateGroupTable=hh3cPortIsolateGroupTable, hh3cGlobalBroadcastMaxPps=hh3cGlobalBroadcastMaxPps, hh3cifBKbpsMulSuppressionMax=hh3cifBKbpsMulSuppressionMax, hh3cifAggregateOperStatus=hh3cifAggregateOperStatus, hh3cifBKbpsUniSuppressionMax=hh3cifBKbpsUniSuppressionMax, hh3cIsolateGroupMax=hh3cIsolateGroupMax, hh3cifMacAddrLearnMode=hh3cifMacAddrLearnMode, hh3cifHybridTaggedVlanListLow=hh3cifHybridTaggedVlanListLow, hh3cifEthernetTest=hh3cifEthernetTest, PYSNMP_MODULE_ID=hh3cLswL2InfMib, hh3cifUnBoundPort=hh3cifUnBoundPort, hh3cifVlanVPNUplinkStatus=hh3cifVlanVPNUplinkStatus, hh3cifBKbpsMulSuppressionStep=hh3cifBKbpsMulSuppressionStep, VlanIndex=VlanIndex, hh3cifClearStat=hh3cifClearStat, hh3cifVLANType=hh3cifVLANType, hh3cifHybridPortEntry=hh3cifHybridPortEntry, hh3cifEthernetIsolate=hh3cifEthernetIsolate, hh3cifAggregateTable=hh3cifAggregateTable, hh3cifVLANTrunkAllowListHigh=hh3cifVLANTrunkAllowListHigh, hh3cifAggregatePortIndex=hh3cifAggregatePortIndex, hh3cLswL2InfMib=hh3cLswL2InfMib, hh3cifHybridUnTaggedVlanListLow=hh3cifHybridUnTaggedVlanListLow, hh3cifBMbpsUniSuppressionMax=hh3cifBMbpsUniSuppressionMax, hh3cifMulSuppressionStep=hh3cifMulSuppressionStep, hh3cMaxMacLearn=hh3cMaxMacLearn, hh3cifFlowControl=hh3cifFlowControl, hh3cifMacAddressLearn=hh3cifMacAddressLearn, hh3cifISPhyPort=hh3cifISPhyPort, hh3cLswExtInterface=hh3cLswExtInterface, hh3cPortIsolateUplinkIfIndex=hh3cPortIsolateUplinkIfIndex, InterfaceIndex=InterfaceIndex, hh3cifHybridUnTaggedVlanListHigh=hh3cifHybridUnTaggedVlanListHigh, hh3cifComboPortTable=hh3cifComboPortTable, hh3cifComboPortEntry=hh3cifComboPortEntry, hh3cethernetTable=hh3cethernetTable, hh3cifHybridTaggedVlanListHigh=hh3cifHybridTaggedVlanListHigh, hh3cifComboActivePort=hh3cifComboActivePort, hh3cifBMbpsUniSuppression=hh3cifBMbpsUniSuppression, hh3cifInErrorPktsRate=hh3cifInErrorPktsRate, hh3cifComboPortIndex=hh3cifComboPortIndex, hh3cLswL2InfMibObject=hh3cLswL2InfMibObject, hh3cifVlanVPNStatus=hh3cifVlanVPNStatus, hh3cifVLANTrunkPassListLow=hh3cifVLANTrunkPassListLow, hh3cVlanVPNTPIDMode=hh3cVlanVPNTPIDMode, hh3cifAggregateEntry=hh3cifAggregateEntry, hh3cifAggregatePort=hh3cifAggregatePort, hh3cifPpsUniSuppressionMax=hh3cifPpsUniSuppressionMax, hh3cifPpsMulSuppression=hh3cifPpsMulSuppression, hh3cifInPkts=hh3cifInPkts, hh3cifBKbpsUniSuppression=hh3cifBKbpsUniSuppression, hh3cifEthernetMTU=hh3cifEthernetMTU, hh3cifPpsUniSuppression=hh3cifPpsUniSuppression, PortList=PortList, hh3cifEthernetAutoSpeed=hh3cifEthernetAutoSpeed, hh3cifComboPortCurActive=hh3cifComboPortCurActive, hh3cSwitchPortMax=hh3cSwitchPortMax, hh3cSlotPortMax=hh3cSlotPortMax, hh3cifPpsBcastDisValControl=hh3cifPpsBcastDisValControl, hh3cifHybridPortTable=hh3cifHybridPortTable, SpeedModeFlag=SpeedModeFlag, hh3cifSrcMacControl=hh3cifSrcMacControl, hh3cifEthernetSpeed=hh3cifEthernetSpeed, hh3cifEthernetFlowInterval=hh3cifEthernetFlowInterval, hh3cifXXDevPortIndex=hh3cifXXDevPortIndex, hh3cifUnknownPacketDropUni=hh3cifUnknownPacketDropUni, hh3cifHybridPortIndex=hh3cifHybridPortIndex, hh3cifBMbpsMulSuppression=hh3cifBMbpsMulSuppression, hh3cifisUplinkPort=hh3cifisUplinkPort, hh3cifUniSuppressionStep=hh3cifUniSuppressionStep, hh3cifPpsMulSuppressionMax=hh3cifPpsMulSuppressionMax, hh3cifBKbpsUniSuppressionStep=hh3cifBKbpsUniSuppressionStep, hh3cifBKbpsMulSuppression=hh3cifBKbpsMulSuppression, hh3cifXXBasePortIndex=hh3cifXXBasePortIndex, hh3cifVLANTrunkAllowListLow=hh3cifVLANTrunkAllowListLow, hh3cPortIsolateGroupEntry=hh3cPortIsolateGroupEntry, hh3cifInPayloadOctets=hh3cifInPayloadOctets, hh3cifOutPayloadOctets=hh3cifOutPayloadOctets, hh3cifEthernetDuplex=hh3cifEthernetDuplex, hh3cVlanVPNTPID=hh3cVlanVPNTPID, hh3cifVLANTrunkPassListHigh=hh3cifVLANTrunkPassListHigh, hh3cifXXTable=hh3cifXXTable, hh3cifUniSuppression=hh3cifUniSuppression, hh3cethernetEntry=hh3cethernetEntry, hh3cBpduTunnelStatus=hh3cBpduTunnelStatus, hh3cifXXEntry=hh3cifXXEntry, hh3cGlobalBroadcastMaxRatio=hh3cGlobalBroadcastMaxRatio, hh3cifInNormalPkts=hh3cifInNormalPkts, hh3cMaxMacLearnRange=hh3cMaxMacLearnRange, hh3cifAggregatePortName=hh3cifAggregatePortName, hh3cifVLANTrunkIndex=hh3cifVLANTrunkIndex, hh3cifVlanVPNTPID=hh3cifVlanVPNTPID, hh3cifMcastControl=hh3cifMcastControl, hh3cifOutPkts=hh3cifOutPkts, hh3cifEthernetMdi=hh3cifEthernetMdi, hh3cifVLANTrunkGvrpRegistration=hh3cifVLANTrunkGvrpRegistration, DropDirection=DropDirection, hh3cifVLANTrunkStatusTable=hh3cifVLANTrunkStatusTable, hh3cPortIsolateGroupRowStatus=hh3cPortIsolateGroupRowStatus, hh3cPortIsolateGroupIndex=hh3cPortIsolateGroupIndex)
#
# PySNMP MIB module FDRY-DAI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-DAI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
DisplayString, = mibBuilder.importSymbols("FOUNDRY-SN-AGENT-MIB", "DisplayString")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibIdentifier, NotificationType, Counter32, IpAddress, ObjectIdentity, Bits, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibIdentifier", "NotificationType", "Counter32", "IpAddress", "ObjectIdentity", "Bits", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "ModuleIdentity")
MacAddress, TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
fdryDaiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35))
fdryDaiMIB.setRevisions(('2010-07-26 00:00', '2010-02-22 00:00',))
if mibBuilder.loadTexts: fdryDaiMIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryDaiMIB.setOrganization('Brocade Communications Systems, Inc.')
class ArpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("static", 2), ("dynamic", 3), ("inspect", 4), ("dhcp", 5), ("dynamicDhcp", 6), ("staticDhcp", 7), ("host", 8))

class ArpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("valid", 2), ("pend", 3))

fdryDaiVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1))
fdryDaiInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2))
fdryDaiArpInspect = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3))
fdryDaiVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1), )
if mibBuilder.loadTexts: fdryDaiVlanConfigTable.setStatus('current')
fdryDaiVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1), ).setIndexNames((0, "FDRY-DAI-MIB", "fdryDaiVlanVLanId"))
if mibBuilder.loadTexts: fdryDaiVlanConfigEntry.setStatus('current')
fdryDaiVlanVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: fdryDaiVlanVLanId.setStatus('current')
fdryDaiVlanDynArpInspEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDaiVlanDynArpInspEnable.setStatus('current')
fdryDaiIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1), )
if mibBuilder.loadTexts: fdryDaiIfConfigTable.setStatus('current')
fdryDaiIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fdryDaiIfConfigEntry.setStatus('current')
fdryDaiIfTrustValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDaiIfTrustValue.setStatus('current')
fdryDaiArpInspectTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1), )
if mibBuilder.loadTexts: fdryDaiArpInspectTable.setStatus('current')
fdryDaiArpInspectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1), ).setIndexNames((0, "FDRY-DAI-MIB", "fdryDaiArpInspectIpAddr"))
if mibBuilder.loadTexts: fdryDaiArpInspectEntry.setStatus('current')
fdryDaiArpInspectIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: fdryDaiArpInspectIpAddr.setStatus('current')
fdryDaiArpInspectMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryDaiArpInspectMacAddr.setStatus('current')
fdryDaiArpInspectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryDaiArpInspectRowStatus.setStatus('current')
fdryDaiArpInspectType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 4), ArpType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDaiArpInspectType.setStatus('current')
fdryDaiArpInspectState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 5), ArpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDaiArpInspectState.setStatus('current')
fdryDaiArpInspectAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDaiArpInspectAge.setStatus('current')
fdryDaiArpInspectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDaiArpInspectPort.setStatus('current')
mibBuilder.exportSymbols("FDRY-DAI-MIB", ArpType=ArpType, fdryDaiInterface=fdryDaiInterface, fdryDaiVlanDynArpInspEnable=fdryDaiVlanDynArpInspEnable, fdryDaiIfConfigTable=fdryDaiIfConfigTable, fdryDaiMIB=fdryDaiMIB, fdryDaiVlanConfigTable=fdryDaiVlanConfigTable, fdryDaiArpInspectPort=fdryDaiArpInspectPort, fdryDaiArpInspectType=fdryDaiArpInspectType, fdryDaiArpInspectState=fdryDaiArpInspectState, fdryDaiIfTrustValue=fdryDaiIfTrustValue, fdryDaiVlanVLanId=fdryDaiVlanVLanId, fdryDaiArpInspectEntry=fdryDaiArpInspectEntry, fdryDaiIfConfigEntry=fdryDaiIfConfigEntry, fdryDaiArpInspectTable=fdryDaiArpInspectTable, fdryDaiArpInspectAge=fdryDaiArpInspectAge, fdryDaiArpInspectRowStatus=fdryDaiArpInspectRowStatus, fdryDaiArpInspectIpAddr=fdryDaiArpInspectIpAddr, fdryDaiArpInspect=fdryDaiArpInspect, PYSNMP_MODULE_ID=fdryDaiMIB, fdryDaiVlanConfigEntry=fdryDaiVlanConfigEntry, fdryDaiArpInspectMacAddr=fdryDaiArpInspectMacAddr, ArpState=ArpState, fdryDaiVlan=fdryDaiVlan)

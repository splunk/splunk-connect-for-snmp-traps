#
# PySNMP MIB module Dlink-IMPB-MNG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-IMPB-MNG
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
rlImpbManagment, = mibBuilder.importSymbols("Dlink-IMPB-FEATURES", "rlImpbManagment")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Unsigned32, MibIdentifier, Counter32, Bits, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "Bits", "iso", "TimeTicks")
TextualConvention, RowStatus, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "MacAddress", "DisplayString")
class IMPBPacketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ip", 1), ("arp", 2), ("iparp", 3))

class IMPBLockMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unlocked", 1), ("locked", 2))

class IMPBDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("host", 1), ("dhcpSrv", 2), ("router", 3), ("routerDhcp", 4))

rlIMPBMngTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1), )
if mibBuilder.loadTexts: rlIMPBMngTable.setStatus('current')
rlIMPBMngEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1), ).setIndexNames((0, "Dlink-IMPB-MNG", "rlIMPBMngIPAddress"))
if mibBuilder.loadTexts: rlIMPBMngEntry.setStatus('current')
rlIMPBMngIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlIMPBMngIPAddress.setStatus('current')
rlIMPBMngPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 2), IMPBPacketType().clone('ip')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngPacketType.setStatus('current')
rlIMPBMngPMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngPMACAddress.setStatus('current')
rlIMPBMngDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 4), IMPBDeviceType().clone('host')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngDeviceType.setStatus('current')
rlIMPBMngPortlist = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngPortlist.setStatus('current')
rlIMPBMngMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 6), IMPBLockMode().clone('locked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngMode.setStatus('current')
rlIMPBMngRouterBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 1000000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngRouterBandwidth.setStatus('current')
rlIMPBMngRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngRowStatus.setStatus('current')
rlIMPBMngAction = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAction", 1), ("lockAll", 2), ("unlockAll", 3), ("deleteUnlock", 4), ("deleteAll", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngAction.setStatus('current')
rlIMPBMngPortBandwidthTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3), )
if mibBuilder.loadTexts: rlIMPBMngPortBandwidthTable.setStatus('current')
rlIMPBMngPortBandwidthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlIMPBMngPortBandwidthEntry.setStatus('current')
rlIMPBMngBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIMPBMngBandwidth.setStatus('current')
rlIMPBMngRouterBandwidthTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4), )
if mibBuilder.loadTexts: rlIMPBMngRouterBandwidthTable.setStatus('current')
rlIMPBMngRouterBandwidthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1), ).setIndexNames((0, "Dlink-IMPB-MNG", "rlIMPBRouterIPAddress"))
if mibBuilder.loadTexts: rlIMPBMngRouterBandwidthEntry.setStatus('current')
rlIMPBRouterIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlIMPBRouterIPAddress.setStatus('current')
rlIMPBRouterPortlist = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIMPBRouterPortlist.setStatus('current')
rlIMPBRouterBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIMPBRouterBandwidth.setStatus('current')
rlIMPBMngDiscoveryLearningStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("learning", 1), ("noLearning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIMPBMngDiscoveryLearningStatus.setStatus('current')
rlIMPBMngUncheckPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 6), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngUncheckPorts.setStatus('current')
rlIMPBMngLockedStations = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIMPBMngLockedStations.setStatus('current')
rlIMPBMngGratARPPeriodTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 300), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIMPBMngGratARPPeriodTimeout.setStatus('current')
mibBuilder.exportSymbols("Dlink-IMPB-MNG", rlIMPBMngUncheckPorts=rlIMPBMngUncheckPorts, rlIMPBMngEntry=rlIMPBMngEntry, IMPBLockMode=IMPBLockMode, rlIMPBRouterPortlist=rlIMPBRouterPortlist, rlIMPBRouterBandwidth=rlIMPBRouterBandwidth, rlIMPBMngRowStatus=rlIMPBMngRowStatus, rlIMPBMngLockedStations=rlIMPBMngLockedStations, IMPBPacketType=IMPBPacketType, rlIMPBMngPMACAddress=rlIMPBMngPMACAddress, rlIMPBMngRouterBandwidth=rlIMPBMngRouterBandwidth, rlIMPBMngAction=rlIMPBMngAction, rlIMPBMngDeviceType=rlIMPBMngDeviceType, rlIMPBMngPortBandwidthTable=rlIMPBMngPortBandwidthTable, rlIMPBMngIPAddress=rlIMPBMngIPAddress, IMPBDeviceType=IMPBDeviceType, rlIMPBMngTable=rlIMPBMngTable, rlIMPBMngBandwidth=rlIMPBMngBandwidth, rlIMPBMngPortlist=rlIMPBMngPortlist, rlIMPBRouterIPAddress=rlIMPBRouterIPAddress, rlIMPBMngGratARPPeriodTimeout=rlIMPBMngGratARPPeriodTimeout, rlIMPBMngDiscoveryLearningStatus=rlIMPBMngDiscoveryLearningStatus, rlIMPBMngMode=rlIMPBMngMode, rlIMPBMngRouterBandwidthTable=rlIMPBMngRouterBandwidthTable, rlIMPBMngPacketType=rlIMPBMngPacketType, rlIMPBMngRouterBandwidthEntry=rlIMPBMngRouterBandwidthEntry, rlIMPBMngPortBandwidthEntry=rlIMPBMngPortBandwidthEntry)

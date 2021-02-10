#
# PySNMP MIB module ES-GroupManagement-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ES-GroupManagement-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, IpAddress, iso, MibIdentifier, TimeTicks, Gauge32, NotificationType, Integer32, enterprises, ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "IpAddress", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "NotificationType", "Integer32", "enterprises", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
class MacAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = ''

zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
ethernetSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15))
groupManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4))
groupParam = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1))
neighborDiscovery = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2))
topologyCollect = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3))
memberManage = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4))
gmEnterpriseTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 15, 4, 5))
gmHandtime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gmHandtime.setStatus('current')
gmHoldtime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gmHoldtime.setStatus('current')
gmName = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gmName.setStatus('current')
gmSwitchRole = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("commandSwitch", 1), ("memberSwitch", 2), ("candidateSwitch", 3), ("independentSwitch", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gmSwitchRole.setStatus('current')
gmIpPool = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gmIpPool.setStatus('current')
tftpServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerIpAddr.setStatus('current')
belongedCmdMac = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: belongedCmdMac.setStatus('current')
dpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpAdminStatus.setStatus('current')
dpTimer = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimer.setStatus('current')
dpHoldtime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpHoldtime.setStatus('current')
dpPortTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4), )
if mibBuilder.loadTexts: dpPortTable.setStatus('current')
dpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "dpPortId"))
if mibBuilder.loadTexts: dpPortEntry.setStatus('current')
dpPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: dpPortId.setStatus('current')
dpPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpPortAdminStatus.setStatus('current')
dpTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5), )
if mibBuilder.loadTexts: dpTrunkTable.setStatus('current')
dpTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "dpTrunkId"))
if mibBuilder.loadTexts: dpTrunkEntry.setStatus('current')
dpTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: dpTrunkId.setStatus('current')
dpTrunkAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTrunkAdminStatus.setStatus('current')
tpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpAdminStatus.setStatus('current')
tpVlan = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpVlan.setStatus('current')
tpHop = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpHop.setStatus('current')
tpTimer = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpTimer.setStatus('current')
tpHopDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpHopDelay.setStatus('current')
tpPortDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortDelay.setStatus('current')
tpStart = MibScalar((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("start", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStart.setStatus('current')
tpPortTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8), )
if mibBuilder.loadTexts: tpPortTable.setStatus('current')
tpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "tpPortId"))
if mibBuilder.loadTexts: tpPortEntry.setStatus('current')
tpPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: tpPortId.setStatus('current')
tpPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortAdminStatus.setStatus('current')
tpTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9), )
if mibBuilder.loadTexts: tpTrunkTable.setStatus('current')
tpTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "tpTrunkId"))
if mibBuilder.loadTexts: tpTrunkEntry.setStatus('current')
tpTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: tpTrunkId.setStatus('current')
tpTrunkAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpTrunkAdminStatus.setStatus('current')
tpDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10), )
if mibBuilder.loadTexts: tpDeviceTable.setStatus('current')
tpDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "deviceMac"))
if mibBuilder.loadTexts: tpDeviceEntry.setStatus('current')
deviceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceMac.setStatus('current')
deviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceId.setStatus('current')
deviceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceIpAddr.setStatus('current')
deviceHop = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHop.setStatus('current')
devicePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devicePlatform.setStatus('current')
deviceRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("commandSwitch", 1), ("memberSwitch", 2), ("candidateSwitch", 3), ("independentSwitch", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceRole.setStatus('current')
devicePeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devicePeerPort.setStatus('current')
deviceBelongedMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceBelongedMac.setStatus('current')
deviceBelongedIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceBelongedIpAddr.setStatus('current')
memberTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1), )
if mibBuilder.loadTexts: memberTable.setStatus('current')
memberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1), ).setIndexNames((0, "ES-GroupManagement-MIB", "memMac"))
if mibBuilder.loadTexts: memberEntry.setStatus('current')
memMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memMac.setStatus('current')
memId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memId.setStatus('current')
memIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIpAddr.setStatus('current')
memMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memMask.setStatus('current')
memStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memStatus.setStatus('current')
memRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("memberSwitch", 1), ("candidateSwitch", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: memRole.setStatus('current')
snmpPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpPortMap.setStatus('current')
httpPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: httpPortMap.setStatus('current')
ftpPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpPortMap.setStatus('current')
tftpPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpPortMap.setStatus('current')
telnetPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telnetPortMap.setStatus('current')
sshPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshPortMap.setStatus('current')
gmTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 3902, 15, 4, 5, 1))
if mibBuilder.loadTexts: gmTopologyChange.setStatus('current')
gmMemberUpDown = NotificationType((1, 3, 6, 1, 4, 1, 3902, 15, 4, 5, 2)).setObjects(("ES-GroupManagement-MIB", "memMac"), ("ES-GroupManagement-MIB", "memId"), ("ES-GroupManagement-MIB", "memIpAddr"), ("ES-GroupManagement-MIB", "memStatus"))
if mibBuilder.loadTexts: gmMemberUpDown.setStatus('current')
mibBuilder.exportSymbols("ES-GroupManagement-MIB", groupManagement=groupManagement, httpPortMap=httpPortMap, tftpPortMap=tftpPortMap, memMask=memMask, belongedCmdMac=belongedCmdMac, tpTimer=tpTimer, tpTrunkId=tpTrunkId, tpPortEntry=tpPortEntry, MacAddress=MacAddress, dpTrunkId=dpTrunkId, tpPortTable=tpPortTable, memStatus=memStatus, dpPortId=dpPortId, memIpAddr=memIpAddr, telnetPortMap=telnetPortMap, tpPortAdminStatus=tpPortAdminStatus, dpPortEntry=dpPortEntry, tpHop=tpHop, deviceRole=deviceRole, tpTrunkTable=tpTrunkTable, memId=memId, dpTrunkTable=dpTrunkTable, tpVlan=tpVlan, deviceMac=deviceMac, memberTable=memberTable, deviceIpAddr=deviceIpAddr, gmTopologyChange=gmTopologyChange, tpHopDelay=tpHopDelay, tpAdminStatus=tpAdminStatus, tpTrunkAdminStatus=tpTrunkAdminStatus, gmMemberUpDown=gmMemberUpDown, gmHoldtime=gmHoldtime, deviceHop=deviceHop, gmHandtime=gmHandtime, deviceBelongedMac=deviceBelongedMac, tpPortId=tpPortId, memRole=memRole, groupParam=groupParam, gmIpPool=gmIpPool, dpTrunkAdminStatus=dpTrunkAdminStatus, ethernetSwitch=ethernetSwitch, tpStart=tpStart, devicePeerPort=devicePeerPort, dpTimer=dpTimer, tpPortDelay=tpPortDelay, deviceBelongedIpAddr=deviceBelongedIpAddr, dpAdminStatus=dpAdminStatus, memberManage=memberManage, zte=zte, dpTrunkEntry=dpTrunkEntry, dpHoldtime=dpHoldtime, memMac=memMac, dpPortAdminStatus=dpPortAdminStatus, ftpPortMap=ftpPortMap, deviceId=deviceId, dpPortTable=dpPortTable, devicePlatform=devicePlatform, tftpServerIpAddr=tftpServerIpAddr, snmpPortMap=snmpPortMap, tpDeviceTable=tpDeviceTable, tpTrunkEntry=tpTrunkEntry, gmEnterpriseTrap=gmEnterpriseTrap, gmSwitchRole=gmSwitchRole, topologyCollect=topologyCollect, sshPortMap=sshPortMap, neighborDiscovery=neighborDiscovery, gmName=gmName, tpDeviceEntry=tpDeviceEntry, memberEntry=memberEntry)

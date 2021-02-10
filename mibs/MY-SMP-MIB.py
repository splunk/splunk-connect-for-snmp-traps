#
# PySNMP MIB module MY-SMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-SMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
Community, = mibBuilder.importSymbols("MY-SNMP-AGENT-MIB", "Community")
IfIndex, ConfigStatus = mibBuilder.importSymbols("MY-TC", "IfIndex", "ConfigStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Bits, Integer32, Counter64, TimeTicks, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
MacAddress, RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
mySMPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39))
mySMPMIB.setRevisions(('2004-09-09 00:00',))
if mibBuilder.loadTexts: mySMPMIB.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: mySMPMIB.setOrganization('D-Link Crop.')
mySMPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1))
mySMPServer = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPServer.setStatus('current')
mySMPServerKey = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 2), Community()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPServerKey.setStatus('current')
mySMPEventSendSlice = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPEventSendSlice.setStatus('current')
mySMPPolicyDelete = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyDelete.setStatus('current')
mySMPPolicyChecksum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySMPPolicyChecksum.setStatus('current')
mySMPPolicyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyTimeout.setStatus('current')
mySMPPolicyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9), )
if mibBuilder.loadTexts: mySMPPolicyGroupTable.setStatus('current')
mySMPPolicyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1), ).setIndexNames((0, "MY-SMP-MIB", "mySMPPolicyGroupIndex"))
if mibBuilder.loadTexts: mySMPPolicyGroupEntry.setStatus('current')
mySMPPolicyGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySMPPolicyGroupIndex.setStatus('current')
mySMPPolicyGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyGroupCount.setStatus('current')
mySMPPolicyGroupChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyGroupChecksum.setStatus('current')
mySMPPolicyGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mySMPPolicyGroupStatus.setStatus('current')
mySMPPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8), )
if mibBuilder.loadTexts: mySMPPolicyTable.setStatus('current')
mySMPPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1), ).setIndexNames((0, "MY-SMP-MIB", "mySMPGroupIndex"), (0, "MY-SMP-MIB", "mySMPPolicyIndex"))
if mibBuilder.loadTexts: mySMPPolicyEntry.setStatus('current')
mySMPGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySMPGroupIndex.setStatus('current')
mySMPPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySMPPolicyIndex.setStatus('current')
mySMPPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 3), ConfigStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyStatus.setStatus('current')
mySMPPolicyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyNumber.setStatus('current')
mySMPPolicyInstallPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 5), IfIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyInstallPort.setStatus('current')
mySMPPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("hi-isolate", 1), ("isolate", 2), ("blocked", 3), ("addrBind", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyType.setStatus('current')
mySMPPolicyContent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyContent.setStatus('current')
mySMPPolicyMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyMask.setStatus('current')
mySMPPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPPolicyName.setStatus('current')
mySMPFrameRelayTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7), )
if mibBuilder.loadTexts: mySMPFrameRelayTable.setStatus('current')
mySMPFrameRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1), ).setIndexNames((0, "MY-SMP-MIB", "mySMPFrameRelayIndex"))
if mibBuilder.loadTexts: mySMPFrameRelayEntry.setStatus('current')
mySMPFrameRelayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySMPFrameRelayIndex.setStatus('current')
mySMPFrameRelayContent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPFrameRelayContent.setStatus('current')
mySMPFrameRelayLength = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPFrameRelayLength.setStatus('current')
mySMPFrameRelayDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 4), IfIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPFrameRelayDestPort.setStatus('current')
mySMPFrameRelayDestVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 5), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySMPFrameRelayDestVlan.setStatus('current')
mySMPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535))
mySMPSwitchIP = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPSwitchIP.setStatus('current')
mySMPSwitchInterfaceID = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 2), IfIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPSwitchInterfaceID.setStatus('current')
mySMPSwitchInterfaceVLANID = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 3), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPSwitchInterfaceVLANID.setStatus('current')
mySMPFrameContentLength = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPFrameContentLength.setStatus('current')
mySMPFrameContent = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPFrameContent.setStatus('current')
mySMPFrameRelayTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 6)).setObjects(("MY-SMP-MIB", "mySMPSwitchIP"), ("MY-SMP-MIB", "mySMPSwitchInterfaceID"), ("MY-SMP-MIB", "mySMPSwitchInterfaceVLANID"), ("MY-SMP-MIB", "mySMPFrameContentLength"), ("MY-SMP-MIB", "mySMPFrameContent"))
if mibBuilder.loadTexts: mySMPFrameRelayTrap.setStatus('current')
mySMPArpAttackSubnetIP = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackSubnetIP.setStatus('current')
mySMPArpAttackSubnetIPNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 8), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackSubnetIPNum.setStatus('current')
mySMPArpAttackInterfaceSlot = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackInterfaceSlot.setStatus('current')
mySMPArpAttackInterfacePort = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackInterfacePort.setStatus('current')
mySMPArpAttackInterfaceVlanID = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 11), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackInterfaceVlanID.setStatus('current')
mySMPArpAttackFrameContent = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackFrameContent.setStatus('current')
mySMPArpAttackStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 13), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackStatus.setStatus('current')
mySMPArpAttackCriticalStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("emergencies", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackCriticalStatus.setStatus('current')
mySMPArpAttackMac = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 15), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackMac.setStatus('current')
mySMPArpAttackInterfaceIndex = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 16), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mySMPArpAttackInterfaceIndex.setStatus('current')
mySMPArpAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 17)).setObjects(("MY-SMP-MIB", "mySMPArpAttackSubnetIP"), ("MY-SMP-MIB", "mySMPArpAttackSubnetIPNum"), ("MY-SMP-MIB", "mySMPArpAttackInterfaceSlot"), ("MY-SMP-MIB", "mySMPArpAttackInterfacePort"), ("MY-SMP-MIB", "mySMPArpAttackInterfaceVlanID"), ("MY-SMP-MIB", "mySMPArpAttackFrameContent"), ("MY-SMP-MIB", "mySMPArpAttackStatus"), ("MY-SMP-MIB", "mySMPArpAttackCriticalStatus"), ("MY-SMP-MIB", "mySMPArpAttackMac"), ("MY-SMP-MIB", "mySMPArpAttackInterfaceIndex"))
if mibBuilder.loadTexts: mySMPArpAttackTrap.setStatus('current')
mySMPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3))
mySMPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 1))
mySMPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2))
myDeviceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 1, 1)).setObjects(("MY-SMP-MIB", "mySMPServerMibGroup"), ("MY-SMP-MIB", "mySMPClientMibGroup"), ("MY-SMP-MIB", "mySMPPolicyMibGroup"), ("MY-SMP-MIB", "mySMPFrameRelayMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myDeviceMIBCompliance = myDeviceMIBCompliance.setStatus('current')
mySMPServerMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 1)).setObjects(("MY-SMP-MIB", "mySMPServer"), ("MY-SMP-MIB", "mySMPServerKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySMPServerMibGroup = mySMPServerMibGroup.setStatus('current')
mySMPClientMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 2)).setObjects(("MY-SMP-MIB", "mySMPEventSendSlice"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySMPClientMibGroup = mySMPClientMibGroup.setStatus('current')
mySMPPolicyMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 3)).setObjects(("MY-SMP-MIB", "mySMPPolicyDelete"), ("MY-SMP-MIB", "mySMPPolicyChecksum"), ("MY-SMP-MIB", "mySMPPolicyIndex"), ("MY-SMP-MIB", "mySMPPolicyStatus"), ("MY-SMP-MIB", "mySMPPolicyInstallPort"), ("MY-SMP-MIB", "mySMPPolicyType"), ("MY-SMP-MIB", "mySMPPolicyContent"), ("MY-SMP-MIB", "mySMPPolicyMask"), ("MY-SMP-MIB", "mySMPPolicyName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySMPPolicyMibGroup = mySMPPolicyMibGroup.setStatus('current')
mySMPFrameRelayMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 4)).setObjects(("MY-SMP-MIB", "mySMPFrameRelayIndex"), ("MY-SMP-MIB", "mySMPFrameRelayContent"), ("MY-SMP-MIB", "mySMPFrameRelayLength"), ("MY-SMP-MIB", "mySMPFrameRelayDestPort"), ("MY-SMP-MIB", "mySMPFrameRelayDestVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySMPFrameRelayMibGroup = mySMPFrameRelayMibGroup.setStatus('current')
mibBuilder.exportSymbols("MY-SMP-MIB", mySMPServerMibGroup=mySMPServerMibGroup, mySMPEventSendSlice=mySMPEventSendSlice, mySMPFrameRelayDestVlan=mySMPFrameRelayDestVlan, mySMPGroupIndex=mySMPGroupIndex, mySMPFrameRelayIndex=mySMPFrameRelayIndex, mySMPFrameRelayEntry=mySMPFrameRelayEntry, mySMPMIBCompliances=mySMPMIBCompliances, mySMPPolicyDelete=mySMPPolicyDelete, mySMPPolicyGroupCount=mySMPPolicyGroupCount, PYSNMP_MODULE_ID=mySMPMIB, mySMPPolicyName=mySMPPolicyName, mySMPSwitchInterfaceID=mySMPSwitchInterfaceID, mySMPPolicyInstallPort=mySMPPolicyInstallPort, mySMPPolicyMibGroup=mySMPPolicyMibGroup, mySMPFrameContentLength=mySMPFrameContentLength, mySMPMIBObjects=mySMPMIBObjects, mySMPFrameRelayContent=mySMPFrameRelayContent, mySMPMIBGroups=mySMPMIBGroups, mySMPPolicyNumber=mySMPPolicyNumber, mySMPPolicyGroupStatus=mySMPPolicyGroupStatus, mySMPPolicyTable=mySMPPolicyTable, mySMPFrameRelayTable=mySMPFrameRelayTable, mySMPArpAttackTrap=mySMPArpAttackTrap, mySMPFrameContent=mySMPFrameContent, mySMPPolicyIndex=mySMPPolicyIndex, mySMPPolicyMask=mySMPPolicyMask, mySMPServer=mySMPServer, mySMPSwitchIP=mySMPSwitchIP, mySMPArpAttackSubnetIP=mySMPArpAttackSubnetIP, mySMPArpAttackStatus=mySMPArpAttackStatus, mySMPArpAttackInterfaceSlot=mySMPArpAttackInterfaceSlot, mySMPArpAttackCriticalStatus=mySMPArpAttackCriticalStatus, mySMPPolicyGroupIndex=mySMPPolicyGroupIndex, mySMPPolicyChecksum=mySMPPolicyChecksum, mySMPPolicyContent=mySMPPolicyContent, mySMPArpAttackInterfaceIndex=mySMPArpAttackInterfaceIndex, mySMPFrameRelayLength=mySMPFrameRelayLength, mySMPMIBConformance=mySMPMIBConformance, mySMPServerKey=mySMPServerKey, myDeviceMIBCompliance=myDeviceMIBCompliance, mySMPFrameRelayMibGroup=mySMPFrameRelayMibGroup, mySMPPolicyTimeout=mySMPPolicyTimeout, mySMPPolicyType=mySMPPolicyType, mySMPClientMibGroup=mySMPClientMibGroup, mySMPPolicyGroupEntry=mySMPPolicyGroupEntry, mySMPArpAttackMac=mySMPArpAttackMac, mySMPSwitchInterfaceVLANID=mySMPSwitchInterfaceVLANID, mySMPMIB=mySMPMIB, mySMPPolicyStatus=mySMPPolicyStatus, mySMPFrameRelayDestPort=mySMPFrameRelayDestPort, mySMPPolicyGroupTable=mySMPPolicyGroupTable, mySMPPolicyEntry=mySMPPolicyEntry, mySMPTraps=mySMPTraps, mySMPArpAttackSubnetIPNum=mySMPArpAttackSubnetIPNum, mySMPArpAttackInterfaceVlanID=mySMPArpAttackInterfaceVlanID, mySMPPolicyGroupChecksum=mySMPPolicyGroupChecksum, mySMPFrameRelayTrap=mySMPFrameRelayTrap, mySMPArpAttackInterfacePort=mySMPArpAttackInterfacePort, mySMPArpAttackFrameContent=mySMPArpAttackFrameContent)
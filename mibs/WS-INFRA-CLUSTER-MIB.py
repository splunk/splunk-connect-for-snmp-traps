#
# PySNMP MIB module WS-INFRA-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WS-INFRA-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Bits, Integer32, Counter64, IpAddress, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, NotificationType, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Bits", "Integer32", "Counter64", "IpAddress", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "NotificationType", "iso", "ObjectIdentity")
TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
wsInfraCluster, = mibBuilder.importSymbols("WS-INFRA-SMI-MIB", "wsInfraCluster")
DoActionNow, = mibBuilder.importSymbols("WS-TYPE-MIB", "DoActionNow")
wsInfraClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1))
wsInfraClusterMIB.setRevisions(('2008-08-08 09:46', '2008-06-17 17:13', '2008-04-29 10:13', '2007-06-26 13:26', '2007-06-26 12:15', '2006-05-24 13:58', '2005-12-27 14:05', '2005-12-16 12:29', '2005-09-12 20:39', '2005-08-17 13:25', '2005-08-15 16:27', '2005-08-15 14:20', '2005-08-11 18:53', '2005-07-07 18:36', '2005-07-07 16:39',))
if mibBuilder.loadTexts: wsInfraClusterMIB.setLastUpdated('200808080946Z')
if mibBuilder.loadTexts: wsInfraClusterMIB.setOrganization('Symbol Technologies')
wsInfraClusterSwitchIP = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterSwitchIP.setStatus('current')
wsInfraClusterEnable = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterEnable.setStatus('current')
wsInfraClusterMode = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("standby", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterMode.setStatus('current')
wsInfraClusterId = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterId.setStatus('current')
wsInfraClusterDiscoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDiscoveryInterval.setStatus('current')
wsInfraClusterHoldInterval = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterHoldInterval.setStatus('current')
wsInfraClusterHBInterval = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterHBInterval.setStatus('current')
wsInfraClusterHandleSTP = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterHandleSTP.setStatus('current')
wsInfraClusterSwitchState = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("startup", 2), ("discovery", 3), ("online", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterSwitchState.setStatus('current')
wsInfraClusterLicNum = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterLicNum.setStatus('current')
wsInfraClusterInstalledLicNum = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterInstalledLicNum.setStatus('current')
wsInfraClusterApCnt = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterApCnt.setStatus('current')
wsInfraClusterVersion = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterVersion.setStatus('current')
wsInfraClusterHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14))
wsInfraClusterHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1), )
if mibBuilder.loadTexts: wsInfraClusterHistoryTable.setStatus('current')
wsInfraClusterHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1), ).setIndexNames((0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryIndex"))
if mibBuilder.loadTexts: wsInfraClusterHistoryEntry.setStatus('current')
wsInfraClusterHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wsInfraClusterHistoryIndex.setStatus('current')
wsInfraClusterHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("startup", 2), ("discovery", 3), ("online", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterHistoryState.setStatus('current')
wsInfraClusterHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterHistoryTime.setStatus('current')
wsInfraClusterHistoryEventTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("startupDone", 3), ("discoveryDone", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterHistoryEventTrigger.setStatus('current')
wsInfraClusterHistoryDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterHistoryDesc.setStatus('current')
wsInfraClusterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15))
wsInfraClusterConfigTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1), )
if mibBuilder.loadTexts: wsInfraClusterConfigTable.setStatus('current')
wsInfraClusterConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1), ).setIndexNames((0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"), (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"))
if mibBuilder.loadTexts: wsInfraClusterConfigEntry.setStatus('current')
wsInfraClusterConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterConfigIndex.setStatus('current')
wsInfraClusterMemberIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterMemberIpAddr.setStatus('current')
wsInfraClusterCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wsInfraClusterCfgRowStatus.setStatus('current')
wsInfraClustertNumHBSent = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClustertNumHBSent.setStatus('current')
wsInfraClusterNumHBRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumHBRcvd.setStatus('current')
wsInfraClusterLastSeen = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterLastSeen.setStatus('current')
wsInfraClusterFirstSeen = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterFirstSeen.setStatus('current')
wsInfraClusterNumUpdMesgSent = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumUpdMesgSent.setStatus('current')
wsInfraClusterNumUpdMesgRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumUpdMesgRecd.setStatus('current')
wsInfraClusterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("peerConfigured", 1), ("peerInvalid", 2), ("peerSeen", 3), ("peerNotSeen", 4), ("peerEstablished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterStatus.setStatus('current')
wsInfraClusterAdoptionCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterAdoptionCnt.setStatus('current')
wsInfraClusterSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterSwitchMode.setStatus('current')
wsInfraClusterInstalLicValue = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterInstalLicValue.setStatus('current')
wsInfraClusterUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterUptime.setStatus('current')
wsInfraClusterNumMusAdopted = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumMusAdopted.setStatus('current')
wsInfraClusterNumRadiosAdopted = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumRadiosAdopted.setStatus('current')
wsInfraClusterNumSelfHealingRadios = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumSelfHealingRadios.setStatus('current')
wsInfraClusterNumRogueAps = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterNumRogueAps.setStatus('current')
wsInfraClusterCfgRunningImgVer = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterCfgRunningImgVer.setStatus('current')
wsInfraClusterCfgPortAdoptionCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterCfgPortAdoptionCapacity.setStatus('current')
wsInfraClusterPeerStatTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2), )
if mibBuilder.loadTexts: wsInfraClusterPeerStatTable.setStatus('obsolete')
wsInfraClusterPeerStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2, 1), ).setIndexNames((0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"), (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"))
if mibBuilder.loadTexts: wsInfraClusterPeerStatEntry.setStatus('obsolete')
wsInfraClusterStatNumHBSent = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterStatNumHBSent.setStatus('obsolete')
wsInfraClusterUpAndFullyConnected = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterUpAndFullyConnected.setStatus('current')
wsInfraClusterTotalApsAdopted = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalApsAdopted.setStatus('current')
wsInfraClusterTotalRadiosAdopted = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalRadiosAdopted.setStatus('current')
wsInfraClusterTotalMusAssociated = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalMusAssociated.setStatus('current')
wsInfraClusterTotalRogueAps = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalRogueAps.setStatus('current')
wsInfraClusterTotalPortAdoptionCapacity = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalPortAdoptionCapacity.setStatus('current')
wsInfraClusterTotalSelfHealingRadios = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterTotalSelfHealingRadios.setStatus('current')
wsInfraClusterMusAdoptedCnt = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterMusAdoptedCnt.setStatus('current')
wsInfraClusterRadiosAdoptedCnt = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterRadiosAdoptedCnt.setStatus('current')
wsInfraClusterSelfHealingRadioCnt = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterSelfHealingRadioCnt.setStatus('current')
wsInfraClusterRogueApCnt = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterRogueApCnt.setStatus('current')
wsInfraClusterRunningImgVer = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterRunningImgVer.setStatus('current')
wsInfraClusterPortAdoptionCapacity = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterPortAdoptionCapacity.setStatus('current')
wsInfraClusterAutoRevert = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterAutoRevert.setStatus('current')
wsInfraClusterAutoRevertDelay = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 30), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1800))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterAutoRevertDelay.setStatus('current')
wsInfraClusterManualRevert = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("manualRevertNow", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterManualRevert.setStatus('current')
wsInfraClusterDhcpRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDhcpRedundancy.setStatus('current')
wsInfraClusterActiveDhcpServerSwitch = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraClusterActiveDhcpServerSwitch.setStatus('current')
wsInfraClusterResetActiveDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetActiveDhcpServer", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterResetActiveDhcpServer.setStatus('current')
wsInfraCriticalResourceIp = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 35), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraCriticalResourceIp.setStatus('current')
wsInfraClusterDynApLoadBal = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36))
wsInfraClusterDynApLoadBalEnable = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalEnable.setStatus('current')
wsInfraClusterDynApLoadBalApproach = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("schedule", 1), ("runtime", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalApproach.setStatus('current')
wsInfraClusterDynApLoadBalSched = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3))
wsInfraClusterDynApLoadBalSchedStartTime = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalSchedStartTime.setStatus('current')
wsInfraClusterDynApLoadBalSchedInterval = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 180))).setUnits('days').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalSchedInterval.setStatus('current')
wsInfraClusterDynApLoadBalStart = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 4), DoActionNow()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalStart.setStatus('current')
wsInfraClusterDynApLoadBalMUThrshld = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setUnits('MUs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterDynApLoadBalMUThrshld.setStatus('current')
wsInfraClusterLicensingAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("max", 1), ("aggregation", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraClusterLicensingAlgorithm.setStatus('current')
wsInfrastructureMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100))
wsInfrastructureMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 1))
wsInfrastructureMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 1, 1)).setObjects(("WS-INFRA-CLUSTER-MIB", "wsInfrastructureMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfrastructureMIBCompliance = wsInfrastructureMIBCompliance.setStatus('current')
wsInfrastructureMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2))
wsInfrastructureMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2, 1)).setObjects(("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchIP"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterEnable"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMode"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterId"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHBInterval"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHandleSTP"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchState"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLicNum"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterInstalledLicNum"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterApCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterVersion"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryIndex"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryState"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryTime"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryEventTrigger"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryDesc"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgRowStatus"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHoldInterval"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDiscoveryInterval"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterUpAndFullyConnected"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalApsAdopted"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalRadiosAdopted"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalMusAssociated"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalRogueAps"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalPortAdoptionCapacity"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalSelfHealingRadios"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMusAdoptedCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRadiosAdoptedCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSelfHealingRadioCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRogueApCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRunningImgVer"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterPortAdoptionCapacity"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAutoRevert"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAutoRevertDelay"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterResetActiveDhcpServer"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterActiveDhcpServerSwitch"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDhcpRedundancy"), ("WS-INFRA-CLUSTER-MIB", "wsInfraCriticalResourceIp"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalEnable"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalApproach"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalMUThrshld"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalStart"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLicensingAlgorithm"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterManualRevert"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClustertNumHBSent"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumHBRcvd"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLastSeen"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterFirstSeen"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumUpdMesgSent"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumUpdMesgRecd"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterStatus"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAdoptionCnt"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchMode"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterInstalLicValue"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterUptime"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumMusAdopted"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumRadiosAdopted"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumSelfHealingRadios"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumRogueAps"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgRunningImgVer"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgPortAdoptionCapacity"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalSchedStartTime"), ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalSchedInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfrastructureMIBGroup = wsInfrastructureMIBGroup.setStatus('current')
wsInfrastructureMIBObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2, 2)).setObjects(("WS-INFRA-CLUSTER-MIB", "wsInfraClusterStatNumHBSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfrastructureMIBObsoleteGroup = wsInfrastructureMIBObsoleteGroup.setStatus('obsolete')
mibBuilder.exportSymbols("WS-INFRA-CLUSTER-MIB", wsInfraClusterDynApLoadBalSched=wsInfraClusterDynApLoadBalSched, wsInfraClusterMode=wsInfraClusterMode, wsInfraClusterPeerStatTable=wsInfraClusterPeerStatTable, wsInfrastructureMIBGroups=wsInfrastructureMIBGroups, wsInfraClusterSelfHealingRadioCnt=wsInfraClusterSelfHealingRadioCnt, wsInfraClusterDynApLoadBalEnable=wsInfraClusterDynApLoadBalEnable, wsInfraClusterActiveDhcpServerSwitch=wsInfraClusterActiveDhcpServerSwitch, wsInfraClusterMemberIpAddr=wsInfraClusterMemberIpAddr, wsInfraClusterHandleSTP=wsInfraClusterHandleSTP, wsInfrastructureMIBCompliances=wsInfrastructureMIBCompliances, wsInfraClusterId=wsInfraClusterId, wsInfrastructureMIBConformance=wsInfrastructureMIBConformance, wsInfraClusterHistoryEventTrigger=wsInfraClusterHistoryEventTrigger, wsInfraClusterInstalledLicNum=wsInfraClusterInstalledLicNum, wsInfraClusterStatus=wsInfraClusterStatus, wsInfraClusterResetActiveDhcpServer=wsInfraClusterResetActiveDhcpServer, wsInfraClusterVersion=wsInfraClusterVersion, wsInfraClusterLastSeen=wsInfraClusterLastSeen, wsInfraClusterConfigEntry=wsInfraClusterConfigEntry, wsInfraClusterFirstSeen=wsInfraClusterFirstSeen, wsInfraClusterMusAdoptedCnt=wsInfraClusterMusAdoptedCnt, wsInfraClusterCfgPortAdoptionCapacity=wsInfraClusterCfgPortAdoptionCapacity, wsInfraClusterAutoRevertDelay=wsInfraClusterAutoRevertDelay, wsInfraClusterConfigIndex=wsInfraClusterConfigIndex, wsInfraClusterDynApLoadBalApproach=wsInfraClusterDynApLoadBalApproach, wsInfraClusterDynApLoadBalMUThrshld=wsInfraClusterDynApLoadBalMUThrshld, wsInfraClusterManualRevert=wsInfraClusterManualRevert, wsInfraClusterDiscoveryInterval=wsInfraClusterDiscoveryInterval, wsInfraClusterHistoryIndex=wsInfraClusterHistoryIndex, wsInfraClusterEnable=wsInfraClusterEnable, wsInfraClusterDynApLoadBalSchedInterval=wsInfraClusterDynApLoadBalSchedInterval, wsInfraClusterSwitchIP=wsInfraClusterSwitchIP, wsInfraClusterNumRadiosAdopted=wsInfraClusterNumRadiosAdopted, wsInfraClusterHistoryDesc=wsInfraClusterHistoryDesc, wsInfraClusterNumUpdMesgSent=wsInfraClusterNumUpdMesgSent, wsInfraClusterMIB=wsInfraClusterMIB, wsInfraClusterHistory=wsInfraClusterHistory, wsInfraClusterConfig=wsInfraClusterConfig, wsInfraClusterPeerStatEntry=wsInfraClusterPeerStatEntry, wsInfraClusterRunningImgVer=wsInfraClusterRunningImgVer, wsInfraClusterStatNumHBSent=wsInfraClusterStatNumHBSent, wsInfraClusterAdoptionCnt=wsInfraClusterAdoptionCnt, wsInfraClusterApCnt=wsInfraClusterApCnt, wsInfrastructureMIBGroup=wsInfrastructureMIBGroup, wsInfraClusterDynApLoadBalStart=wsInfraClusterDynApLoadBalStart, wsInfraClusterTotalMusAssociated=wsInfraClusterTotalMusAssociated, wsInfraClusterNumSelfHealingRadios=wsInfraClusterNumSelfHealingRadios, wsInfraClusterRogueApCnt=wsInfraClusterRogueApCnt, wsInfrastructureMIBCompliance=wsInfrastructureMIBCompliance, wsInfraClusterHoldInterval=wsInfraClusterHoldInterval, wsInfraClusterTotalPortAdoptionCapacity=wsInfraClusterTotalPortAdoptionCapacity, wsInfraClusterTotalSelfHealingRadios=wsInfraClusterTotalSelfHealingRadios, wsInfraClusterCfgRowStatus=wsInfraClusterCfgRowStatus, wsInfraClusterHistoryTable=wsInfraClusterHistoryTable, wsInfraClusterDhcpRedundancy=wsInfraClusterDhcpRedundancy, wsInfraCriticalResourceIp=wsInfraCriticalResourceIp, wsInfraClusterTotalRogueAps=wsInfraClusterTotalRogueAps, wsInfraClusterRadiosAdoptedCnt=wsInfraClusterRadiosAdoptedCnt, wsInfraClusterDynApLoadBal=wsInfraClusterDynApLoadBal, wsInfrastructureMIBObsoleteGroup=wsInfrastructureMIBObsoleteGroup, wsInfraClusterTotalRadiosAdopted=wsInfraClusterTotalRadiosAdopted, wsInfraClusterPortAdoptionCapacity=wsInfraClusterPortAdoptionCapacity, wsInfraClusterSwitchState=wsInfraClusterSwitchState, wsInfraClusterUptime=wsInfraClusterUptime, wsInfraClusterUpAndFullyConnected=wsInfraClusterUpAndFullyConnected, wsInfraClustertNumHBSent=wsInfraClustertNumHBSent, wsInfraClusterDynApLoadBalSchedStartTime=wsInfraClusterDynApLoadBalSchedStartTime, wsInfraClusterSwitchMode=wsInfraClusterSwitchMode, wsInfraClusterAutoRevert=wsInfraClusterAutoRevert, wsInfraClusterHistoryEntry=wsInfraClusterHistoryEntry, wsInfraClusterNumUpdMesgRecd=wsInfraClusterNumUpdMesgRecd, wsInfraClusterHBInterval=wsInfraClusterHBInterval, wsInfraClusterHistoryState=wsInfraClusterHistoryState, wsInfraClusterLicensingAlgorithm=wsInfraClusterLicensingAlgorithm, PYSNMP_MODULE_ID=wsInfraClusterMIB, wsInfraClusterNumMusAdopted=wsInfraClusterNumMusAdopted, wsInfraClusterConfigTable=wsInfraClusterConfigTable, wsInfraClusterHistoryTime=wsInfraClusterHistoryTime, wsInfraClusterNumHBRcvd=wsInfraClusterNumHBRcvd, wsInfraClusterTotalApsAdopted=wsInfraClusterTotalApsAdopted, wsInfraClusterInstalLicValue=wsInfraClusterInstalLicValue, wsInfraClusterNumRogueAps=wsInfraClusterNumRogueAps, wsInfraClusterLicNum=wsInfraClusterLicNum, wsInfraClusterCfgRunningImgVer=wsInfraClusterCfgRunningImgVer)

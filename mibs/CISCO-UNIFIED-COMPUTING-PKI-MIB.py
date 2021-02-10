#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-PKI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-PKI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:00:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, CiscoInetAddressMask, CiscoNetworkAddress, TimeIntervalSec, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "CiscoInetAddressMask", "CiscoNetworkAddress", "TimeIntervalSec", "Unsigned64")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectId, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId", "CucsManagedObjectDn")
CucsFsmFsmStageStatus, CucsPkiEpFsmCurrentFsm, CucsPkiKeyringState, CucsPolicyPolicyOwner, CucsPkiEpFsmTaskItem, CucsPkiModulus, CucsConditionRemoteInvRslt, CucsPkiEpFsmStageName, CucsPkiCertStatus, CucsFsmFlags, CucsFsmCompletion, CucsAaaConfigState = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsFsmFsmStageStatus", "CucsPkiEpFsmCurrentFsm", "CucsPkiKeyringState", "CucsPolicyPolicyOwner", "CucsPkiEpFsmTaskItem", "CucsPkiModulus", "CucsConditionRemoteInvRslt", "CucsPkiEpFsmStageName", "CucsPkiCertStatus", "CucsFsmFlags", "CucsFsmCompletion", "CucsAaaConfigState")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, iso, ModuleIdentity, Gauge32, Bits, ObjectIdentity, IpAddress, Unsigned32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "iso", "ModuleIdentity", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "TimeTicks")
TruthValue, DisplayString, TextualConvention, TimeInterval, TimeStamp, MacAddress, RowPointer, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeInterval", "TimeStamp", "MacAddress", "RowPointer", "DateAndTime")
cucsPkiObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37))
if mibBuilder.loadTexts: cucsPkiObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsPkiObjects.setOrganization('Cisco Systems Inc.')
cucsPkiCertReqTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1), )
if mibBuilder.loadTexts: cucsPkiCertReqTable.setStatus('current')
cucsPkiCertReqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiCertReqInstanceId"))
if mibBuilder.loadTexts: cucsPkiCertReqEntry.setStatus('current')
cucsPkiCertReqInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiCertReqInstanceId.setStatus('current')
cucsPkiCertReqDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqDn.setStatus('current')
cucsPkiCertReqRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqRn.setStatus('current')
cucsPkiCertReqIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIp.setStatus('current')
cucsPkiCertReqPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqPwd.setStatus('current')
cucsPkiCertReqReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqReq.setStatus('current')
cucsPkiCertReqSubjName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqSubjName.setStatus('current')
cucsPkiCertReqCountry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqCountry.setStatus('current')
cucsPkiCertReqDns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqDns.setStatus('current')
cucsPkiCertReqEmail = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqEmail.setStatus('current')
cucsPkiCertReqLocality = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqLocality.setStatus('current')
cucsPkiCertReqOrgName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqOrgName.setStatus('current')
cucsPkiCertReqOrgUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqOrgUnitName.setStatus('current')
cucsPkiCertReqState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqState.setStatus('current')
cucsPkiCertReqIpA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 15), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIpA.setStatus('current')
cucsPkiCertReqIpB = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 16), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIpB.setStatus('current')
cucsPkiCertReqIpv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 17), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIpv6.setStatus('current')
cucsPkiCertReqIpv6A = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 18), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIpv6A.setStatus('current')
cucsPkiCertReqIpv6B = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 19), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiCertReqIpv6B.setStatus('current')
cucsPkiEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2), )
if mibBuilder.loadTexts: cucsPkiEpTable.setStatus('current')
cucsPkiEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpInstanceId"))
if mibBuilder.loadTexts: cucsPkiEpEntry.setStatus('current')
cucsPkiEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiEpInstanceId.setStatus('current')
cucsPkiEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpDn.setStatus('current')
cucsPkiEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpRn.setStatus('current')
cucsPkiEpDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpDescr.setStatus('current')
cucsPkiEpFsmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmDescr.setStatus('current')
cucsPkiEpFsmPrev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmPrev.setStatus('current')
cucsPkiEpFsmProgr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmProgr.setStatus('current')
cucsPkiEpFsmRmtInvErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtInvErrCode.setStatus('current')
cucsPkiEpFsmRmtInvErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtInvErrDescr.setStatus('current')
cucsPkiEpFsmRmtInvRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 10), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtInvRslt.setStatus('current')
cucsPkiEpFsmStageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageDescr.setStatus('current')
cucsPkiEpFsmStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStamp.setStatus('current')
cucsPkiEpFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStatus.setStatus('current')
cucsPkiEpFsmTry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTry.setStatus('current')
cucsPkiEpIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpIntId.setStatus('current')
cucsPkiEpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpName.setStatus('current')
cucsPkiEpPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpPolicyLevel.setStatus('current')
cucsPkiEpPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 18), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpPolicyOwner.setStatus('current')
cucsPkiEpFsmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6), )
if mibBuilder.loadTexts: cucsPkiEpFsmTable.setStatus('current')
cucsPkiEpFsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmInstanceId"))
if mibBuilder.loadTexts: cucsPkiEpFsmEntry.setStatus('current')
cucsPkiEpFsmInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiEpFsmInstanceId.setStatus('current')
cucsPkiEpFsmDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmDn.setStatus('current')
cucsPkiEpFsmRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRn.setStatus('current')
cucsPkiEpFsmCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmCompletionTime.setStatus('current')
cucsPkiEpFsmCurrentFsm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 5), CucsPkiEpFsmCurrentFsm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmCurrentFsm.setStatus('current')
cucsPkiEpFsmDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmDescrData.setStatus('current')
cucsPkiEpFsmFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 7), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmFsmStatus.setStatus('current')
cucsPkiEpFsmProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmProgress.setStatus('current')
cucsPkiEpFsmRmtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtErrCode.setStatus('current')
cucsPkiEpFsmRmtErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtErrDescr.setStatus('current')
cucsPkiEpFsmRmtRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmRmtRslt.setStatus('current')
cucsPkiEpFsmStageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7), )
if mibBuilder.loadTexts: cucsPkiEpFsmStageTable.setStatus('current')
cucsPkiEpFsmStageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmStageInstanceId"))
if mibBuilder.loadTexts: cucsPkiEpFsmStageEntry.setStatus('current')
cucsPkiEpFsmStageInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiEpFsmStageInstanceId.setStatus('current')
cucsPkiEpFsmStageDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageDn.setStatus('current')
cucsPkiEpFsmStageRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageRn.setStatus('current')
cucsPkiEpFsmStageDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageDescrData.setStatus('current')
cucsPkiEpFsmStageLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageLastUpdateTime.setStatus('current')
cucsPkiEpFsmStageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 6), CucsPkiEpFsmStageName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageName.setStatus('current')
cucsPkiEpFsmStageOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageOrder.setStatus('current')
cucsPkiEpFsmStageRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageRetry.setStatus('current')
cucsPkiEpFsmStageStageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmStageStageStatus.setStatus('current')
cucsPkiEpFsmTaskTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3), )
if mibBuilder.loadTexts: cucsPkiEpFsmTaskTable.setStatus('current')
cucsPkiEpFsmTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmTaskInstanceId"))
if mibBuilder.loadTexts: cucsPkiEpFsmTaskEntry.setStatus('current')
cucsPkiEpFsmTaskInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiEpFsmTaskInstanceId.setStatus('current')
cucsPkiEpFsmTaskDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskDn.setStatus('current')
cucsPkiEpFsmTaskRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskRn.setStatus('current')
cucsPkiEpFsmTaskCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 4), CucsFsmCompletion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskCompletion.setStatus('current')
cucsPkiEpFsmTaskFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 5), CucsFsmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskFlags.setStatus('current')
cucsPkiEpFsmTaskItem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 6), CucsPkiEpFsmTaskItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskItem.setStatus('current')
cucsPkiEpFsmTaskSeqId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiEpFsmTaskSeqId.setStatus('current')
cucsPkiKeyRingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4), )
if mibBuilder.loadTexts: cucsPkiKeyRingTable.setStatus('current')
cucsPkiKeyRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiKeyRingInstanceId"))
if mibBuilder.loadTexts: cucsPkiKeyRingEntry.setStatus('current')
cucsPkiKeyRingInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiKeyRingInstanceId.setStatus('current')
cucsPkiKeyRingDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingDn.setStatus('current')
cucsPkiKeyRingRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingRn.setStatus('current')
cucsPkiKeyRingAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 4), CucsPkiKeyringState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingAdminState.setStatus('current')
cucsPkiKeyRingCert = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingCert.setStatus('current')
cucsPkiKeyRingDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingDescr.setStatus('current')
cucsPkiKeyRingIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingIntId.setStatus('current')
cucsPkiKeyRingKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingKey.setStatus('current')
cucsPkiKeyRingModulus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 9), CucsPkiModulus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingModulus.setStatus('current')
cucsPkiKeyRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingName.setStatus('current')
cucsPkiKeyRingRegen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingRegen.setStatus('current')
cucsPkiKeyRingTp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingTp.setStatus('current')
cucsPkiKeyRingCertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 13), CucsPkiCertStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingCertStatus.setStatus('current')
cucsPkiKeyRingConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 14), CucsAaaConfigState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingConfigState.setStatus('current')
cucsPkiKeyRingConfigStatusMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingConfigStatusMessage.setStatus('current')
cucsPkiKeyRingPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingPolicyLevel.setStatus('current')
cucsPkiKeyRingPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 17), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiKeyRingPolicyOwner.setStatus('current')
cucsPkiTPTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5), )
if mibBuilder.loadTexts: cucsPkiTPTable.setStatus('current')
cucsPkiTPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiTPInstanceId"))
if mibBuilder.loadTexts: cucsPkiTPEntry.setStatus('current')
cucsPkiTPInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPkiTPInstanceId.setStatus('current')
cucsPkiTPDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPDn.setStatus('current')
cucsPkiTPRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPRn.setStatus('current')
cucsPkiTPCertChain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPCertChain.setStatus('current')
cucsPkiTPDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPDescr.setStatus('current')
cucsPkiTPFp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPFp.setStatus('current')
cucsPkiTPIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPIntId.setStatus('current')
cucsPkiTPName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPName.setStatus('current')
cucsPkiTPNumCerts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPNumCerts.setStatus('current')
cucsPkiTPCertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 10), CucsPkiCertStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPCertStatus.setStatus('current')
cucsPkiTPPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPPolicyLevel.setStatus('current')
cucsPkiTPPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 12), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPkiTPPolicyOwner.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-PKI-MIB", cucsPkiCertReqTable=cucsPkiCertReqTable, cucsPkiEpFsmFsmStatus=cucsPkiEpFsmFsmStatus, cucsPkiEpFsmTable=cucsPkiEpFsmTable, cucsPkiKeyRingRegen=cucsPkiKeyRingRegen, cucsPkiKeyRingConfigStatusMessage=cucsPkiKeyRingConfigStatusMessage, cucsPkiEpDescr=cucsPkiEpDescr, cucsPkiEpFsmRmtInvErrDescr=cucsPkiEpFsmRmtInvErrDescr, cucsPkiEpFsmRn=cucsPkiEpFsmRn, cucsPkiEpFsmRmtRslt=cucsPkiEpFsmRmtRslt, cucsPkiTPDescr=cucsPkiTPDescr, cucsPkiTPIntId=cucsPkiTPIntId, cucsPkiEpFsmStageLastUpdateTime=cucsPkiEpFsmStageLastUpdateTime, cucsPkiEpFsmTaskRn=cucsPkiEpFsmTaskRn, cucsPkiKeyRingDescr=cucsPkiKeyRingDescr, cucsPkiKeyRingPolicyOwner=cucsPkiKeyRingPolicyOwner, cucsPkiKeyRingCert=cucsPkiKeyRingCert, cucsPkiEpFsmTaskItem=cucsPkiEpFsmTaskItem, cucsPkiTPDn=cucsPkiTPDn, cucsPkiCertReqInstanceId=cucsPkiCertReqInstanceId, cucsPkiCertReqReq=cucsPkiCertReqReq, cucsPkiKeyRingCertStatus=cucsPkiKeyRingCertStatus, cucsPkiEpFsmEntry=cucsPkiEpFsmEntry, cucsPkiTPCertChain=cucsPkiTPCertChain, cucsPkiEpFsmDescrData=cucsPkiEpFsmDescrData, cucsPkiEpFsmStageOrder=cucsPkiEpFsmStageOrder, cucsPkiCertReqState=cucsPkiCertReqState, cucsPkiCertReqPwd=cucsPkiCertReqPwd, cucsPkiEpFsmStageEntry=cucsPkiEpFsmStageEntry, cucsPkiTPPolicyLevel=cucsPkiTPPolicyLevel, cucsPkiCertReqIpv6B=cucsPkiCertReqIpv6B, cucsPkiEpFsmCompletionTime=cucsPkiEpFsmCompletionTime, cucsPkiCertReqIp=cucsPkiCertReqIp, cucsPkiEpPolicyOwner=cucsPkiEpPolicyOwner, cucsPkiCertReqIpv6A=cucsPkiCertReqIpv6A, cucsPkiEpFsmRmtErrCode=cucsPkiEpFsmRmtErrCode, cucsPkiEpFsmPrev=cucsPkiEpFsmPrev, cucsPkiEpFsmStageDn=cucsPkiEpFsmStageDn, cucsPkiKeyRingAdminState=cucsPkiKeyRingAdminState, cucsPkiKeyRingRn=cucsPkiKeyRingRn, cucsPkiEpFsmInstanceId=cucsPkiEpFsmInstanceId, cucsPkiTPRn=cucsPkiTPRn, cucsPkiKeyRingInstanceId=cucsPkiKeyRingInstanceId, cucsPkiKeyRingDn=cucsPkiKeyRingDn, cucsPkiTPCertStatus=cucsPkiTPCertStatus, cucsPkiEpInstanceId=cucsPkiEpInstanceId, cucsPkiTPTable=cucsPkiTPTable, cucsPkiEpFsmStageDescr=cucsPkiEpFsmStageDescr, cucsPkiCertReqOrgUnitName=cucsPkiCertReqOrgUnitName, cucsPkiTPInstanceId=cucsPkiTPInstanceId, cucsPkiKeyRingEntry=cucsPkiKeyRingEntry, cucsPkiEpPolicyLevel=cucsPkiEpPolicyLevel, cucsPkiCertReqIpv6=cucsPkiCertReqIpv6, cucsPkiCertReqIpB=cucsPkiCertReqIpB, cucsPkiEpDn=cucsPkiEpDn, cucsPkiKeyRingModulus=cucsPkiKeyRingModulus, cucsPkiEpFsmTry=cucsPkiEpFsmTry, cucsPkiEpFsmProgr=cucsPkiEpFsmProgr, cucsPkiTPNumCerts=cucsPkiTPNumCerts, cucsPkiCertReqSubjName=cucsPkiCertReqSubjName, cucsPkiCertReqEntry=cucsPkiCertReqEntry, cucsPkiTPEntry=cucsPkiTPEntry, cucsPkiEpTable=cucsPkiEpTable, cucsPkiTPFp=cucsPkiTPFp, cucsPkiEpFsmTaskTable=cucsPkiEpFsmTaskTable, cucsPkiKeyRingTable=cucsPkiKeyRingTable, cucsPkiEpFsmStageDescrData=cucsPkiEpFsmStageDescrData, cucsPkiKeyRingName=cucsPkiKeyRingName, cucsPkiTPName=cucsPkiTPName, cucsPkiCertReqRn=cucsPkiCertReqRn, cucsPkiEpFsmStageTable=cucsPkiEpFsmStageTable, cucsPkiEpFsmStageStageStatus=cucsPkiEpFsmStageStageStatus, cucsPkiKeyRingPolicyLevel=cucsPkiKeyRingPolicyLevel, cucsPkiEpFsmTaskCompletion=cucsPkiEpFsmTaskCompletion, cucsPkiKeyRingConfigState=cucsPkiKeyRingConfigState, cucsPkiEpFsmStageName=cucsPkiEpFsmStageName, cucsPkiKeyRingTp=cucsPkiKeyRingTp, PYSNMP_MODULE_ID=cucsPkiObjects, cucsPkiCertReqCountry=cucsPkiCertReqCountry, cucsPkiEpFsmDn=cucsPkiEpFsmDn, cucsPkiEpFsmProgress=cucsPkiEpFsmProgress, cucsPkiObjects=cucsPkiObjects, cucsPkiTPPolicyOwner=cucsPkiTPPolicyOwner, cucsPkiCertReqIpA=cucsPkiCertReqIpA, cucsPkiEpFsmDescr=cucsPkiEpFsmDescr, cucsPkiCertReqOrgName=cucsPkiCertReqOrgName, cucsPkiEpFsmRmtInvErrCode=cucsPkiEpFsmRmtInvErrCode, cucsPkiEpFsmStamp=cucsPkiEpFsmStamp, cucsPkiEpRn=cucsPkiEpRn, cucsPkiKeyRingIntId=cucsPkiKeyRingIntId, cucsPkiCertReqEmail=cucsPkiCertReqEmail, cucsPkiEpFsmTaskSeqId=cucsPkiEpFsmTaskSeqId, cucsPkiEpFsmTaskFlags=cucsPkiEpFsmTaskFlags, cucsPkiCertReqLocality=cucsPkiCertReqLocality, cucsPkiCertReqDns=cucsPkiCertReqDns, cucsPkiEpName=cucsPkiEpName, cucsPkiEpEntry=cucsPkiEpEntry, cucsPkiCertReqDn=cucsPkiCertReqDn, cucsPkiEpFsmStatus=cucsPkiEpFsmStatus, cucsPkiEpFsmRmtErrDescr=cucsPkiEpFsmRmtErrDescr, cucsPkiEpFsmCurrentFsm=cucsPkiEpFsmCurrentFsm, cucsPkiEpIntId=cucsPkiEpIntId, cucsPkiEpFsmTaskEntry=cucsPkiEpFsmTaskEntry, cucsPkiKeyRingKey=cucsPkiKeyRingKey, cucsPkiEpFsmStageRetry=cucsPkiEpFsmStageRetry, cucsPkiEpFsmStageInstanceId=cucsPkiEpFsmStageInstanceId, cucsPkiEpFsmTaskInstanceId=cucsPkiEpFsmTaskInstanceId, cucsPkiEpFsmRmtInvRslt=cucsPkiEpFsmRmtInvRslt, cucsPkiEpFsmTaskDn=cucsPkiEpFsmTaskDn, cucsPkiEpFsmStageRn=cucsPkiEpFsmStageRn)

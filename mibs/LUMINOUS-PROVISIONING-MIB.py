#
# PySNMP MIB module LUMINOUS-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-PROVISIONING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
LumTdmType, LumSlotNum, LumPortNum, LumName, LumDescr = mibBuilder.importSymbols("LUMINOUS-TC-MIB", "LumTdmType", "LumSlotNum", "LumPortNum", "LumName", "LumDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, enterprises, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, ObjectIdentity, IpAddress, iso, Counter64, Bits, ModuleIdentity, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "enterprises", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "IpAddress", "iso", "Counter64", "Bits", "ModuleIdentity", "ObjectName")
TextualConvention, RowStatus, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DateAndTime", "DisplayString")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumProvisioningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 2))
lumProvisioningMIB.setRevisions(('1901-06-13 00:00', '1900-08-22 00:00', '1900-07-11 00:00',))
if mibBuilder.loadTexts: lumProvisioningMIB.setLastUpdated('0008220000Z')
if mibBuilder.loadTexts: lumProvisioningMIB.setOrganization('Luminous Networks')
lumTdmCrossConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2))
lumTdmCrossConnectTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1), )
if mibBuilder.loadTexts: lumTdmCrossConnectTable.setStatus('current')
lumTdmCrossConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1), ).setIndexNames((0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalCardSlotId"), (0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalPortNumber"))
if mibBuilder.loadTexts: lumTdmCrossConnectEntry.setStatus('current')
lumTdmLocalCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 1), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmLocalCardSlotId.setStatus('current')
lumTdmLocalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 2), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmLocalPortNumber.setStatus('current')
lumTdmConnectNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 3), IpAddress().clone('0.0.0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectNodeIP.setStatus('current')
lumTdmConnectCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 4), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectCardSlotId.setStatus('current')
lumTdmConnectPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 5), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectPortNumber.setStatus('current')
lumTdmConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 6), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectNumber.setStatus('current')
lumTdmConnectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 7), LumDescr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionName.setStatus('current')
lumTdmConnectionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 8), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionStartTime.setStatus('current')
lumTdmConnectionStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 9), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionStopTime.setStatus('current')
lumTdmConnectConfigParam = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("slc96", 2))).clone('pointToPoint')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectConfigParam.setStatus('current')
lumTdmConnectionUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumTdmConnectionUpTime.setStatus('current')
lumTdmConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumTdmConnectionStatus.setStatus('current')
lumTdmConnectType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 13), LumTdmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumTdmConnectType.setStatus('current')
lumDPProvision = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3))
lumDPProvisionTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1), )
if mibBuilder.loadTexts: lumDPProvisionTable.setStatus('current')
lumDPProvisionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1), ).setIndexNames((0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalCardSlotId"), (0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalPortNumber"), (0, "LUMINOUS-PROVISIONING-MIB", "lumDPConnectNumber"))
if mibBuilder.loadTexts: lumDPProvisionEntry.setStatus('current')
lumDPLocalCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 1), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPLocalCardSlotId.setStatus('current')
lumDPLocalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 2), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPLocalPortNumber.setStatus('current')
lumDPConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectNumber.setStatus('current')
lumDPConnectNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectNodeIP.setStatus('current')
lumDPConnectCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 5), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectCardSlotId.setStatus('current')
lumDPConnectPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 6), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectPortNumber.setStatus('current')
lumDPConnectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 7), LumDescr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionName.setStatus('current')
lumDPConnectionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 8), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionStartTime.setStatus('current')
lumDPConnectionStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 9), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionStopTime.setStatus('current')
lumDPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("wireModel", 1), ("staticIP", 2), ("dynamicIP", 3))).clone('wireModel')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPCategory.setStatus('current')
lumDPClassOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bestEffort", 1), ("expressForwarding", 2), ("assuredForwarding", 3))).clone('bestEffort')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPClassOfService.setStatus('current')
lumDPPeakBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPPeakBandwidth.setStatus('current')
lumDPSustainedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPSustainedBandwidth.setStatus('current')
lumDPMaximumBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPMaximumBurstSize.setStatus('current')
lumDPNonConformingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("markDown", 2), ("drop", 3))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPNonConformingAction.setStatus('current')
lumDPProtectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unprotected", 1), ("protected", 2))).clone('protected')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPProtectionType.setStatus('current')
lumDPFacilityProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPFacilityProtection.setStatus('current')
lumDPIpPrefix1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix1.setStatus('current')
lumDPIpPrefix2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix2.setStatus('current')
lumDPIpPrefix3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix3.setStatus('current')
lumDPConfigFile = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 21), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConfigFile.setStatus('current')
lumDPVLANId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPVLANId.setStatus('current')
lumDPBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPBufferSize.setStatus('current')
lumDPConnectionUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 24), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumDPConnectionUpTime.setStatus('current')
lumDPConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 25), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDPConnectionStatus.setStatus('current')
mibBuilder.exportSymbols("LUMINOUS-PROVISIONING-MIB", lumDPSustainedBandwidth=lumDPSustainedBandwidth, lumDPConnectionStatus=lumDPConnectionStatus, lumTdmConnectCardSlotId=lumTdmConnectCardSlotId, lumDPLocalPortNumber=lumDPLocalPortNumber, lumDPConnectPortNumber=lumDPConnectPortNumber, lumDPProvisionTable=lumDPProvisionTable, lumTdmCrossConnectTable=lumTdmCrossConnectTable, lumDPConnectNumber=lumDPConnectNumber, lumDPProtectionType=lumDPProtectionType, lumDPIpPrefix3=lumDPIpPrefix3, lumTdmLocalCardSlotId=lumTdmLocalCardSlotId, lumDPPeakBandwidth=lumDPPeakBandwidth, lumTdmConnectionStartTime=lumTdmConnectionStartTime, lumDPProvision=lumDPProvision, lumTdmConnectConfigParam=lumTdmConnectConfigParam, lumTdmCrossConnectEntry=lumTdmCrossConnectEntry, lumDPConfigFile=lumDPConfigFile, lumTdmConnectionUpTime=lumTdmConnectionUpTime, lumDPCategory=lumDPCategory, lumDPBufferSize=lumDPBufferSize, lumDPFacilityProtection=lumDPFacilityProtection, PYSNMP_MODULE_ID=lumProvisioningMIB, lumDPLocalCardSlotId=lumDPLocalCardSlotId, lumDPClassOfService=lumDPClassOfService, lumTdmConnectPortNumber=lumTdmConnectPortNumber, lumDPConnectionStartTime=lumDPConnectionStartTime, luminous=luminous, lumDPMaximumBurstSize=lumDPMaximumBurstSize, lumDPConnectionStopTime=lumDPConnectionStopTime, lumDPIpPrefix1=lumDPIpPrefix1, lumDPVLANId=lumDPVLANId, lumTdmCrossConnect=lumTdmCrossConnect, lumDPConnectionName=lumDPConnectionName, lumDPIpPrefix2=lumDPIpPrefix2, lumDPNonConformingAction=lumDPNonConformingAction, lumADM=lumADM, lumDPConnectNodeIP=lumDPConnectNodeIP, lumTdmConnectNumber=lumTdmConnectNumber, lumTdmConnectNodeIP=lumTdmConnectNodeIP, lumTdmLocalPortNumber=lumTdmLocalPortNumber, lumTdmConnectType=lumTdmConnectType, lumDPProvisionEntry=lumDPProvisionEntry, lumDPConnectionUpTime=lumDPConnectionUpTime, lumProvisioningMIB=lumProvisioningMIB, lumTdmConnectionStopTime=lumTdmConnectionStopTime, lumTdmConnectionStatus=lumTdmConnectionStatus, lumTdmConnectionName=lumTdmConnectionName, lumDPConnectCardSlotId=lumDPConnectCardSlotId)
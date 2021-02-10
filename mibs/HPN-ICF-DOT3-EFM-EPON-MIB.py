#
# PySNMP MIB module HPN-ICF-DOT3-EFM-EPON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DOT3-EFM-EPON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hpnicfEpon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfEpon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, IpAddress, ObjectIdentity, TimeTicks, iso, NotificationType, Unsigned32, Integer32, Bits, Gauge32, MibIdentifier, mib_2, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "ObjectIdentity", "TimeTicks", "iso", "NotificationType", "Unsigned32", "Integer32", "Bits", "Gauge32", "MibIdentifier", "mib-2", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
hpnicfDot3EfmeponMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2))
hpnicfDot3EfmeponMIB.setRevisions(('2004-09-21 00:00',))
if mibBuilder.loadTexts: hpnicfDot3EfmeponMIB.setLastUpdated('200409210000Z')
if mibBuilder.loadTexts: hpnicfDot3EfmeponMIB.setOrganization('')
hpnicfDot3MpcpMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1))
hpnicfDot3MpcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1))
hpnicfDot3MpcpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2))
hpnicfDot3MpcpTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot3MpcpTable.setStatus('current')
hpnicfDot3MpcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3MpcpEntry.setStatus('current')
hpnicfDot3MpcpID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpID.setStatus('current')
hpnicfDot3MpcpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpOperStatus.setStatus('current')
hpnicfDot3MpcpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("olt", 1), ("onu", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3MpcpMode.setStatus('current')
hpnicfDot3MpcpLinkID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpLinkID.setStatus('current')
hpnicfDot3MpcpRemoteMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRemoteMACAddress.setStatus('current')
hpnicfDot3MpcpRegistrationState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unregistered", 1), ("registering", 2), ("registered", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRegistrationState.setStatus('current')
hpnicfDot3MpcpTransmitElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 7), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTransmitElapsed.setStatus('current')
hpnicfDot3MpcpReceiveElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 8), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpReceiveElapsed.setStatus('current')
hpnicfDot3MpcpRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 9), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRoundTripTime.setStatus('current')
hpnicfDot3MpcpMaximumPendingGrants = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpMaximumPendingGrants.setStatus('current')
hpnicfDot3MpcpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3MpcpAdminState.setStatus('current')
hpnicfDot3MpcpOnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 12), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpOnTime.setStatus('current')
hpnicfDot3MpcpOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 13), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpOffTime.setStatus('current')
hpnicfDot3MpcpSyncTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 14), Integer32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpSyncTime.setStatus('current')
hpnicfDot3MpcpStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot3MpcpStatTable.setStatus('current')
hpnicfDot3MpcpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3MpcpStatEntry.setStatus('current')
hpnicfDot3MpcpMACCtrlFramesTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 1), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpMACCtrlFramesTransmitted.setStatus('current')
hpnicfDot3MpcpMACCtrlFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 2), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpMACCtrlFramesReceived.setStatus('current')
hpnicfDot3MpcpDiscoveryWindowsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpDiscoveryWindowsSent.setStatus('current')
hpnicfDot3MpcpDiscoveryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpDiscoveryTimeout.setStatus('current')
hpnicfDot3MpcpTxRegRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 5), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTxRegRequest.setStatus('current')
hpnicfDot3MpcpRxRegRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 6), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxRegRequest.setStatus('current')
hpnicfDot3MpcpTxRegAck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 7), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTxRegAck.setStatus('current')
hpnicfDot3MpcpRxRegAck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 8), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxRegAck.setStatus('current')
hpnicfDot3MpcpTxReport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 9), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTxReport.setStatus('current')
hpnicfDot3MpcpRxReport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 10), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxReport.setStatus('current')
hpnicfDot3MpcpTxGate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 11), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTxGate.setStatus('current')
hpnicfDot3MpcpRxGate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 12), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxGate.setStatus('current')
hpnicfDot3MpcpTxRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 13), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpTxRegister.setStatus('current')
hpnicfDot3MpcpRxRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 14), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxRegister.setStatus('current')
hpnicfDot3MpcpRxNotSupportedMPCP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 15), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3MpcpRxNotSupportedMPCP.setStatus('current')
hpnicfDot3MpcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1))
hpnicfDot3MpcpGroupBase = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOperStatus"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMode"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpLinkID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRemoteMACAddress"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRegistrationState"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMaximumPendingGrants"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3MpcpGroupBase = hpnicfDot3MpcpGroupBase.setStatus('current')
hpnicfDot3MpcpGroupParam = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 2)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTransmitElapsed"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpReceiveElapsed"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRoundTripTime"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOnTime"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOffTime"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpSyncTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3MpcpGroupParam = hpnicfDot3MpcpGroupParam.setStatus('current')
hpnicfDot3MpcpGroupStat = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 3)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMACCtrlFramesTransmitted"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMACCtrlFramesReceived"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpDiscoveryWindowsSent"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpDiscoveryTimeout"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegRequest"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegRequest"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegAck"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegAck"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxReport"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxReport"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxGate"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxGate"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegister"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegister"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxNotSupportedMPCP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3MpcpGroupStat = hpnicfDot3MpcpGroupStat.setStatus('current')
hpnicfDot3MpcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 2))
hpnicfDot3MpcpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 2, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpGroupBase"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpGroupParam"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpGroupStat"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3MpcpCompliance = hpnicfDot3MpcpCompliance.setStatus('current')
hpnicfDot3OmpEmulationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2))
hpnicfDot3OmpEmulationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1))
hpnicfDot3OmpeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2))
hpnicfDot3OmpEmulationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationTable.setStatus('current')
hpnicfDot3OmpEmulationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationEntry.setStatus('current')
hpnicfDot3OmpEmulationID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationID.setStatus('current')
hpnicfDot3OmpEmulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("olt", 2), ("onu", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationType.setStatus('current')
hpnicfDot3OmpEmulationStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationStatTable.setStatus('current')
hpnicfDot3OmpEmulationStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationStatEntry.setStatus('current')
hpnicfDot3OmpEmulationSLDErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 1), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationSLDErrors.setStatus('current')
hpnicfDot3OmpEmulationCRC8Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 2), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationCRC8Errors.setStatus('current')
hpnicfDot3OmpEmulationBadLLID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 3), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationBadLLID.setStatus('current')
hpnicfDot3OmpEmulationGoodLLID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 4), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationGoodLLID.setStatus('current')
hpnicfDot3OmpEmulationOnuPonCastLLID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 5), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationOnuPonCastLLID.setStatus('current')
hpnicfDot3OmpEmulationOltPonCastLLID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 6), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationOltPonCastLLID.setStatus('current')
hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 7), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus('current')
hpnicfDot3OmpEmulationOnuLLIDNotBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 8), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setStatus('current')
hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 9), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus('current')
hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 10), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus('current')
hpnicfDot3OmpeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1))
hpnicfDot3OmpeGroupID = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OmpeGroupID = hpnicfDot3OmpeGroupID.setStatus('current')
hpnicfDot3OmpeGroupStat = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1, 2)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationSLDErrors"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationCRC8Errors"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBadLLID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationGoodLLID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOnuPonCastLLID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOltPonCastLLID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOnuLLIDNotBroadcast"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OmpeGroupStat = hpnicfDot3OmpeGroupStat.setStatus('current')
hpnicfDot3OmpeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 2))
hpnicfDot3OmpeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 2, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpeGroupID"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpeGroupStat"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OmpeCompliance = hpnicfDot3OmpeCompliance.setStatus('current')
hpnicfDot3EponMauMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3))
hpnicfDot3EponMauObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1))
hpnicfDot3EponMauConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2))
hpnicfDot3EponMauTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot3EponMauTable.setStatus('current')
hpnicfDot3EponMauEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3EponMauEntry.setStatus('current')
hpnicfDot3EponMauPCSCodingViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 1), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3EponMauPCSCodingViolation.setStatus('current')
hpnicfDot3EponMauFecAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("nonsupported", 2), ("supported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3EponMauFecAbility.setStatus('current')
hpnicfDot3EponMauFecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3EponMauFecMode.setStatus('current')
hpnicfDot3EponMauFECCorrectedBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3EponMauFECCorrectedBlocks.setStatus('current')
hpnicfDot3EponMauFECUncorrectableBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3EponMauFECUncorrectableBlocks.setStatus('current')
hpnicfDot3EponMauBufferHeadCodingViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 6), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3EponMauBufferHeadCodingViolation.setStatus('current')
hpnicfDot3EponMauType = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3))
hpnicfEponMauType1000BasePXOLT = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 1))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePXOLT.setStatus('current')
hpnicfEponMauType1000BasePXONU = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 2))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePXONU.setStatus('current')
hpnicfEponMauType1000BasePX10DOLT = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 3))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX10DOLT.setStatus('current')
hpnicfEponMauType1000BasePX10DONU = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 4))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX10DONU.setStatus('current')
hpnicfEponMauType1000BasePX10UOLT = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 5))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX10UOLT.setStatus('current')
hpnicfEponMauType1000BasePX10UONU = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 6))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX10UONU.setStatus('current')
hpnicfEponMauType1000BasePX20DOLT = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 7))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX20DOLT.setStatus('current')
hpnicfEponMauType1000BasePX20DONU = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 8))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX20DONU.setStatus('current')
hpnicfEponMauType1000BasePX20UOLT = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 9))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX20UOLT.setStatus('current')
hpnicfEponMauType1000BasePX20UONU = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 10))
if mibBuilder.loadTexts: hpnicfEponMauType1000BasePX20UONU.setStatus('current')
hpnicfDot3EponMauGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1))
hpnicfDot3EponMauGroupAll = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauPCSCodingViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3EponMauGroupAll = hpnicfDot3EponMauGroupAll.setStatus('current')
hpnicfDot3EponMauGroupFEC = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1, 2)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFecAbility"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFecMode"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFECCorrectedBlocks"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFECUncorrectableBlocks"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauBufferHeadCodingViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3EponMauGroupFEC = hpnicfDot3EponMauGroupFEC.setStatus('current')
hpnicfDot3EponMauCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 2))
hpnicfDot3EponMauCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 2, 1)).setObjects(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauGroupAll"), ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauGroupFEC"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3EponMauCompliance = hpnicfDot3EponMauCompliance.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-DOT3-EFM-EPON-MIB", hpnicfDot3MpcpRemoteMACAddress=hpnicfDot3MpcpRemoteMACAddress, hpnicfDot3MpcpRegistrationState=hpnicfDot3MpcpRegistrationState, hpnicfDot3MpcpCompliance=hpnicfDot3MpcpCompliance, hpnicfEponMauType1000BasePX20DOLT=hpnicfEponMauType1000BasePX20DOLT, hpnicfDot3MpcpRxRegRequest=hpnicfDot3MpcpRxRegRequest, hpnicfDot3EponMauFECCorrectedBlocks=hpnicfDot3EponMauFECCorrectedBlocks, hpnicfDot3MpcpCompliances=hpnicfDot3MpcpCompliances, hpnicfDot3MpcpMIB=hpnicfDot3MpcpMIB, hpnicfDot3OmpeGroupStat=hpnicfDot3OmpeGroupStat, hpnicfDot3MpcpTxGate=hpnicfDot3MpcpTxGate, hpnicfDot3EponMauMIB=hpnicfDot3EponMauMIB, hpnicfDot3EponMauGroups=hpnicfDot3EponMauGroups, hpnicfDot3MpcpOnTime=hpnicfDot3MpcpOnTime, hpnicfEponMauType1000BasePX20DONU=hpnicfEponMauType1000BasePX20DONU, hpnicfDot3MpcpTransmitElapsed=hpnicfDot3MpcpTransmitElapsed, hpnicfDot3EponMauBufferHeadCodingViolation=hpnicfDot3EponMauBufferHeadCodingViolation, hpnicfDot3OmpEmulationEntry=hpnicfDot3OmpEmulationEntry, hpnicfDot3OmpEmulationStatEntry=hpnicfDot3OmpEmulationStatEntry, hpnicfDot3MpcpRxRegister=hpnicfDot3MpcpRxRegister, hpnicfDot3OmpEmulationSLDErrors=hpnicfDot3OmpEmulationSLDErrors, hpnicfDot3MpcpRoundTripTime=hpnicfDot3MpcpRoundTripTime, hpnicfEponMauType1000BasePX20UONU=hpnicfEponMauType1000BasePX20UONU, hpnicfDot3MpcpDiscoveryWindowsSent=hpnicfDot3MpcpDiscoveryWindowsSent, hpnicfEponMauType1000BasePX10DONU=hpnicfEponMauType1000BasePX10DONU, hpnicfEponMauType1000BasePX20UOLT=hpnicfEponMauType1000BasePX20UOLT, hpnicfDot3EponMauType=hpnicfDot3EponMauType, hpnicfDot3MpcpLinkID=hpnicfDot3MpcpLinkID, hpnicfDot3EponMauGroupAll=hpnicfDot3EponMauGroupAll, hpnicfEponMauType1000BasePX10UONU=hpnicfEponMauType1000BasePX10UONU, hpnicfDot3OmpEmulationTable=hpnicfDot3OmpEmulationTable, hpnicfDot3OmpeGroupID=hpnicfDot3OmpeGroupID, hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID=hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID, hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId=hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId, hpnicfEponMauType1000BasePXOLT=hpnicfEponMauType1000BasePXOLT, hpnicfDot3MpcpOffTime=hpnicfDot3MpcpOffTime, hpnicfDot3EponMauGroupFEC=hpnicfDot3EponMauGroupFEC, hpnicfDot3MpcpGroupStat=hpnicfDot3MpcpGroupStat, hpnicfDot3MpcpID=hpnicfDot3MpcpID, hpnicfDot3OmpEmulationOltPonCastLLID=hpnicfDot3OmpEmulationOltPonCastLLID, hpnicfDot3EponMauObjects=hpnicfDot3EponMauObjects, hpnicfDot3MpcpAdminState=hpnicfDot3MpcpAdminState, hpnicfEponMauType1000BasePX10DOLT=hpnicfEponMauType1000BasePX10DOLT, hpnicfDot3MpcpRxGate=hpnicfDot3MpcpRxGate, hpnicfDot3OmpEmulationMIB=hpnicfDot3OmpEmulationMIB, hpnicfDot3EponMauFECUncorrectableBlocks=hpnicfDot3EponMauFECUncorrectableBlocks, hpnicfDot3MpcpGroups=hpnicfDot3MpcpGroups, hpnicfDot3MpcpSyncTime=hpnicfDot3MpcpSyncTime, hpnicfDot3OmpeGroups=hpnicfDot3OmpeGroups, PYSNMP_MODULE_ID=hpnicfDot3EfmeponMIB, hpnicfDot3EponMauConformance=hpnicfDot3EponMauConformance, hpnicfDot3EponMauFecMode=hpnicfDot3EponMauFecMode, hpnicfDot3EponMauTable=hpnicfDot3EponMauTable, hpnicfDot3MpcpConformance=hpnicfDot3MpcpConformance, hpnicfDot3MpcpTxRegister=hpnicfDot3MpcpTxRegister, hpnicfDot3MpcpGroupParam=hpnicfDot3MpcpGroupParam, hpnicfDot3MpcpTable=hpnicfDot3MpcpTable, hpnicfDot3EponMauEntry=hpnicfDot3EponMauEntry, hpnicfDot3MpcpMACCtrlFramesReceived=hpnicfDot3MpcpMACCtrlFramesReceived, hpnicfDot3OmpEmulationStatTable=hpnicfDot3OmpEmulationStatTable, hpnicfDot3OmpEmulationCRC8Errors=hpnicfDot3OmpEmulationCRC8Errors, hpnicfDot3MpcpDiscoveryTimeout=hpnicfDot3MpcpDiscoveryTimeout, hpnicfDot3OmpeCompliance=hpnicfDot3OmpeCompliance, hpnicfDot3MpcpRxRegAck=hpnicfDot3MpcpRxRegAck, hpnicfDot3OmpEmulationID=hpnicfDot3OmpEmulationID, hpnicfDot3MpcpMaximumPendingGrants=hpnicfDot3MpcpMaximumPendingGrants, hpnicfDot3MpcpStatTable=hpnicfDot3MpcpStatTable, hpnicfDot3OmpEmulationOnuLLIDNotBroadcast=hpnicfDot3OmpEmulationOnuLLIDNotBroadcast, hpnicfDot3EponMauCompliance=hpnicfDot3EponMauCompliance, hpnicfDot3MpcpGroupBase=hpnicfDot3MpcpGroupBase, hpnicfDot3MpcpTxReport=hpnicfDot3MpcpTxReport, hpnicfDot3OmpEmulationOnuPonCastLLID=hpnicfDot3OmpEmulationOnuPonCastLLID, hpnicfDot3MpcpMode=hpnicfDot3MpcpMode, hpnicfDot3MpcpTxRegRequest=hpnicfDot3MpcpTxRegRequest, hpnicfDot3OmpeConformance=hpnicfDot3OmpeConformance, hpnicfDot3EponMauFecAbility=hpnicfDot3EponMauFecAbility, hpnicfDot3EponMauPCSCodingViolation=hpnicfDot3EponMauPCSCodingViolation, hpnicfDot3OmpEmulationBadLLID=hpnicfDot3OmpEmulationBadLLID, hpnicfDot3MpcpObjects=hpnicfDot3MpcpObjects, hpnicfDot3EfmeponMIB=hpnicfDot3EfmeponMIB, hpnicfDot3EponMauCompliances=hpnicfDot3EponMauCompliances, hpnicfDot3OmpeCompliances=hpnicfDot3OmpeCompliances, hpnicfEponMauType1000BasePXONU=hpnicfEponMauType1000BasePXONU, hpnicfDot3MpcpRxNotSupportedMPCP=hpnicfDot3MpcpRxNotSupportedMPCP, hpnicfDot3MpcpEntry=hpnicfDot3MpcpEntry, hpnicfDot3MpcpReceiveElapsed=hpnicfDot3MpcpReceiveElapsed, hpnicfDot3OmpEmulationGoodLLID=hpnicfDot3OmpEmulationGoodLLID, hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId=hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId, hpnicfDot3OmpEmulationObjects=hpnicfDot3OmpEmulationObjects, hpnicfDot3MpcpStatEntry=hpnicfDot3MpcpStatEntry, hpnicfEponMauType1000BasePX10UOLT=hpnicfEponMauType1000BasePX10UOLT, hpnicfDot3MpcpMACCtrlFramesTransmitted=hpnicfDot3MpcpMACCtrlFramesTransmitted, hpnicfDot3MpcpOperStatus=hpnicfDot3MpcpOperStatus, hpnicfDot3MpcpRxReport=hpnicfDot3MpcpRxReport, hpnicfDot3OmpEmulationType=hpnicfDot3OmpEmulationType, hpnicfDot3MpcpTxRegAck=hpnicfDot3MpcpTxRegAck)

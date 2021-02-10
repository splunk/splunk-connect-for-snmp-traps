#
# PySNMP MIB module PCE-DISC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCE-DISC-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, IpAddress, ObjectIdentity, iso, Bits, Counter64, MibIdentifier, NotificationType, experimental, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "IpAddress", "ObjectIdentity", "iso", "Bits", "Counter64", "MibIdentifier", "NotificationType", "experimental", "Integer32", "Counter32")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
pceDiscStdMIB = ModuleIdentity((1, 3, 6, 1, 3, 10000))
if mibBuilder.loadTexts: pceDiscStdMIB.setLastUpdated('200610150000Z')
if mibBuilder.loadTexts: pceDiscStdMIB.setOrganization('Path Computation Element (PCE) Working Group')
class PceRoutingDomainID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

pceDiscNotifications = MibIdentifier((1, 3, 6, 1, 3, 10000, 0))
pceDiscMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1))
pceDiscoveryObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 1))
pceDiscoveryAdminStatus = MibScalar((1, 3, 6, 1, 3, 10000, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pceDiscoveryAdminStatus.setStatus('current')
pceDiscoveryKnowPCEs = MibScalar((1, 3, 6, 1, 3, 10000, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryKnowPCEs.setStatus('current')
pceDiscoveryActivePCEs = MibScalar((1, 3, 6, 1, 3, 10000, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryActivePCEs.setStatus('current')
pceDiscoveryTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 1, 4), )
if mibBuilder.loadTexts: pceDiscoveryTable.setStatus('current')
pceDiscoveryEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"))
if mibBuilder.loadTexts: pceDiscoveryEntry.setStatus('current')
pceDiscoveryIndex = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pceDiscoveryIndex.setStatus('current')
pceDiscoveryMechanism = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 2), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryMechanism.setStatus('current')
pceDiscoveryIPv4Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryIPv4Address.setStatus('current')
pceDiscoveryIPv6Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 4), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryIPv6Address.setStatus('current')
pceDiscoveryTime = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryTime.setStatus('current')
pceDiscoveryLastUpdated = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryLastUpdated.setStatus('current')
pceDiscoveryCongestion = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryCongestion.setStatus('current')
pceDiscoveryCongestionDuration = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscoveryCongestionDuration.setStatus('current')
pceDiscCapabilityObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 2))
pceDiscCapPathScopeTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 2, 1), )
if mibBuilder.loadTexts: pceDiscCapPathScopeTable.setStatus('current')
pceDiscCapPathScopeEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"))
if mibBuilder.loadTexts: pceDiscCapPathScopeEntry.setStatus('current')
pceDiscCapPathScopeIntraArea = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeIntraArea.setStatus('current')
pceDiscCapPathScopeInterArea = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeInterArea.setStatus('current')
pceDiscCapPathScopeDefInterArea = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeDefInterArea.setStatus('current')
pceDiscCapPathScopeInterAS = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeInterAS.setStatus('current')
pceDiscCapPathScopeDefInterAS = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeDefInterAS.setStatus('current')
pceDiscCapPathScopeInterLayer = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopeInterLayer.setStatus('current')
pceDiscCapPathScopePrefIntraArea = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopePrefIntraArea.setStatus('current')
pceDiscCapPathScopePrefInterArea = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopePrefInterArea.setStatus('current')
pceDiscCapPathScopePrefInterAS = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopePrefInterAS.setStatus('current')
pceDiscCapPathScopePrefIntLayer = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapPathScopePrefIntLayer.setStatus('current')
pceDiscCapDomainTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 2, 2), )
if mibBuilder.loadTexts: pceDiscCapDomainTable.setStatus('current')
pceDiscCapDomainEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 2, 2, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"), (0, "PCE-DISC-STD-MIB", "pceDiscCapDomainIndex"))
if mibBuilder.loadTexts: pceDiscCapDomainEntry.setStatus('current')
pceDiscCapDomainIndex = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pceDiscCapDomainIndex.setStatus('current')
pceDiscCapDomainIDType = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 2), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapDomainIDType.setStatus('current')
pceDiscCapDomainID = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 3), PceRoutingDomainID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapDomainID.setStatus('current')
pceDiscCapDestDomainTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 2, 3), )
if mibBuilder.loadTexts: pceDiscCapDestDomainTable.setStatus('current')
pceDiscCapDestDomainEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 2, 3, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"), (0, "PCE-DISC-STD-MIB", "pceDiscCapDestDomainIndex"))
if mibBuilder.loadTexts: pceDiscCapDestDomainEntry.setStatus('current')
pceDiscCapDestDomainIndex = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pceDiscCapDestDomainIndex.setStatus('current')
pceDiscCapDestDomainIDType = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 2), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapDestDomainIDType.setStatus('current')
pceDiscCapDestDomainID = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 3), PceRoutingDomainID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCapDestDomainID.setStatus('current')
pceDiscComputationOptionsObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 3))
pceDiscComputationOptionsTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 3, 1), )
if mibBuilder.loadTexts: pceDiscComputationOptionsTable.setStatus('current')
pceDiscComputationOptionsEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 3, 1, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"))
if mibBuilder.loadTexts: pceDiscComputationOptionsEntry.setStatus('current')
pceDiscCompOptionsRpriority = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCompOptionsRpriority.setStatus('current')
pceDiscCompOptionsMmessages = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pceDiscCompOptionsMmessages.setStatus('current')
pceDiscActivityObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 4))
pceDiscActivityTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 4, 1), )
if mibBuilder.loadTexts: pceDiscActivityTable.setStatus('current')
pceDiscActivityEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 4, 1, 1), ).setIndexNames((0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"))
if mibBuilder.loadTexts: pceDiscActivityEntry.setStatus('current')
pceDiscActivityTlvsRecv = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pceDiscActivityTlvsRecv.setStatus('current')
pceDiscActivityErroredTlvsRecv = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pceDiscActivityErroredTlvsRecv.setStatus('current')
pceDiscConformance = MibIdentifier((1, 3, 6, 1, 3, 10000, 2))
pceDiscGroups = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 1))
pceDiscCompliances = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 2))
pceDiscGeneralPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pceDiscGeneralPceInformation = pceDiscGeneralPceInformation.setStatus('current')
pceDiscDetailledPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 2)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pceDiscDetailledPceInformation = pceDiscDetailledPceInformation.setStatus('current')
mibBuilder.exportSymbols("PCE-DISC-STD-MIB", pceDiscoveryActivePCEs=pceDiscoveryActivePCEs, pceDiscCapDomainTable=pceDiscCapDomainTable, pceDiscMIBObjects=pceDiscMIBObjects, pceDiscoveryAdminStatus=pceDiscoveryAdminStatus, pceDiscComputationOptionsTable=pceDiscComputationOptionsTable, pceDiscCapDestDomainIDType=pceDiscCapDestDomainIDType, pceDiscCapDestDomainTable=pceDiscCapDestDomainTable, pceDiscoveryObjects=pceDiscoveryObjects, pceDiscStdMIB=pceDiscStdMIB, pceDiscActivityTable=pceDiscActivityTable, pceDiscActivityTlvsRecv=pceDiscActivityTlvsRecv, pceDiscCompliances=pceDiscCompliances, pceDiscoveryIPv4Address=pceDiscoveryIPv4Address, pceDiscoveryIndex=pceDiscoveryIndex, pceDiscCapPathScopePrefInterAS=pceDiscCapPathScopePrefInterAS, pceDiscConformance=pceDiscConformance, pceDiscDetailledPceInformation=pceDiscDetailledPceInformation, pceDiscCapPathScopeIntraArea=pceDiscCapPathScopeIntraArea, pceDiscoveryKnowPCEs=pceDiscoveryKnowPCEs, pceDiscGroups=pceDiscGroups, pceDiscCompOptionsRpriority=pceDiscCompOptionsRpriority, pceDiscCapPathScopeDefInterArea=pceDiscCapPathScopeDefInterArea, pceDiscoveryLastUpdated=pceDiscoveryLastUpdated, pceDiscCapDomainEntry=pceDiscCapDomainEntry, pceDiscoveryCongestionDuration=pceDiscoveryCongestionDuration, pceDiscoveryTable=pceDiscoveryTable, PceRoutingDomainID=PceRoutingDomainID, pceDiscComputationOptionsObjects=pceDiscComputationOptionsObjects, pceDiscGeneralPceInformation=pceDiscGeneralPceInformation, pceDiscCapPathScopeEntry=pceDiscCapPathScopeEntry, pceDiscCapDestDomainIndex=pceDiscCapDestDomainIndex, pceDiscCapPathScopeTable=pceDiscCapPathScopeTable, pceDiscoveryMechanism=pceDiscoveryMechanism, pceDiscCapabilityObjects=pceDiscCapabilityObjects, pceDiscCapPathScopePrefIntraArea=pceDiscCapPathScopePrefIntraArea, pceDiscCapDomainIDType=pceDiscCapDomainIDType, pceDiscCapPathScopeInterArea=pceDiscCapPathScopeInterArea, pceDiscCapDestDomainID=pceDiscCapDestDomainID, pceDiscCapPathScopeInterAS=pceDiscCapPathScopeInterAS, pceDiscCapDomainIndex=pceDiscCapDomainIndex, pceDiscActivityErroredTlvsRecv=pceDiscActivityErroredTlvsRecv, pceDiscoveryCongestion=pceDiscoveryCongestion, pceDiscCapDomainID=pceDiscCapDomainID, pceDiscCompOptionsMmessages=pceDiscCompOptionsMmessages, pceDiscActivityEntry=pceDiscActivityEntry, pceDiscComputationOptionsEntry=pceDiscComputationOptionsEntry, pceDiscoveryIPv6Address=pceDiscoveryIPv6Address, pceDiscCapPathScopePrefIntLayer=pceDiscCapPathScopePrefIntLayer, pceDiscoveryTime=pceDiscoveryTime, PYSNMP_MODULE_ID=pceDiscStdMIB, pceDiscCapPathScopeDefInterAS=pceDiscCapPathScopeDefInterAS, pceDiscCapPathScopePrefInterArea=pceDiscCapPathScopePrefInterArea, pceDiscCapPathScopeInterLayer=pceDiscCapPathScopeInterLayer, pceDiscoveryEntry=pceDiscoveryEntry, pceDiscActivityObjects=pceDiscActivityObjects, pceDiscNotifications=pceDiscNotifications, pceDiscCapDestDomainEntry=pceDiscCapDestDomainEntry)

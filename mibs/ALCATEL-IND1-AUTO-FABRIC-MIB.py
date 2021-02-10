#
# PySNMP MIB module ALCATEL-IND1-AUTO-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-AUTO-FABRIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1AutoFabric, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1AutoFabric")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, Unsigned32, iso, Counter32, MibIdentifier, Counter64, IpAddress, TimeTicks, Gauge32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatelIND1AUTOFABRICMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1))
alcatelIND1AUTOFABRICMIB.setRevisions(('2012-11-25 00:00',))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIB.setLastUpdated('201211260000Z')
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1AUTOFABRICMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBObjects.setStatus('current')
alcatelIND1AUTOFABRICMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBConformance.setStatus('current')
alcatelIND1AUTOFABRICMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBGroups.setStatus('current')
alcatelIND1AUTOFABRICMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBCompliances.setStatus('current')
alaAutoFabricGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalStatus.setStatus('current')
alaAutoFabricGlobalDiscovery = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("restart", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalDiscovery.setStatus('current')
alaAutoFabricGlobalLACPProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalLACPProtocolStatus.setStatus('current')
alaAutoFabricGlobalSPBProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalSPBProtocolStatus.setStatus('current')
alaAutoFabricGlobalMVRPProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalMVRPProtocolStatus.setStatus('current')
alaAutoFabricGlobalConfigSaveTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalConfigSaveTimer.setStatus('current')
alaAutoFabricGlobalConfigSaveTimerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalConfigSaveTimerStatus.setStatus('current')
alaAutoFabricGlobalDiscoveryTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(1)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalDiscoveryTimer.setStatus('current')
alaAutoFabricRemoveGlobalConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("removeGlobalConfig", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricRemoveGlobalConfig.setStatus('current')
alaAutoFabricPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9))
alaAutoFabricPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1), )
if mibBuilder.loadTexts: alaAutoFabricPortConfigTable.setStatus('current')
alaAutoFabricPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigIfIndex"))
if mibBuilder.loadTexts: alaAutoFabricPortConfigEntry.setStatus('current')
alaAutoFabricPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: alaAutoFabricPortConfigIfIndex.setStatus('current')
alaAutoFabricPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortConfigStatus.setStatus('current')
alaAutoFabricPortLACPProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortLACPProtocolStatus.setStatus('current')
alaAutoFabricPortSPBProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortSPBProtocolStatus.setStatus('current')
alaAutoFabricPortMVRPProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortMVRPProtocolStatus.setStatus('current')
alaAutoFabricPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("pending", 2), ("complete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaAutoFabricPortStatus.setStatus('current')
alcatelIND1AUTOFABRICMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricBaseGroup"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1AUTOFABRICMIBCompliance = alcatelIND1AUTOFABRICMIBCompliance.setStatus('current')
alaAutoFabricBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscovery"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalLACPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalSPBProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalMVRPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimer"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimerStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscoveryTimer"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricRemoveGlobalConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricBaseGroup = alaAutoFabricBaseGroup.setStatus('current')
alaAutoFabricPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortLACPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortSPBProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortMVRPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricPortConfigGroup = alaAutoFabricPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-AUTO-FABRIC-MIB", alcatelIND1AUTOFABRICMIB=alcatelIND1AUTOFABRICMIB, PYSNMP_MODULE_ID=alcatelIND1AUTOFABRICMIB, alaAutoFabricGlobalLACPProtocolStatus=alaAutoFabricGlobalLACPProtocolStatus, alaAutoFabricPortConfigGroup=alaAutoFabricPortConfigGroup, alaAutoFabricPortConfigStatus=alaAutoFabricPortConfigStatus, alcatelIND1AUTOFABRICMIBConformance=alcatelIND1AUTOFABRICMIBConformance, alaAutoFabricPortConfigEntry=alaAutoFabricPortConfigEntry, alaAutoFabricRemoveGlobalConfig=alaAutoFabricRemoveGlobalConfig, alaAutoFabricPortStatus=alaAutoFabricPortStatus, alaAutoFabricPortConfigTable=alaAutoFabricPortConfigTable, alcatelIND1AUTOFABRICMIBGroups=alcatelIND1AUTOFABRICMIBGroups, alaAutoFabricPortLACPProtocolStatus=alaAutoFabricPortLACPProtocolStatus, alaAutoFabricGlobalConfigSaveTimer=alaAutoFabricGlobalConfigSaveTimer, alcatelIND1AUTOFABRICMIBObjects=alcatelIND1AUTOFABRICMIBObjects, alaAutoFabricGlobalMVRPProtocolStatus=alaAutoFabricGlobalMVRPProtocolStatus, alaAutoFabricGlobalConfigSaveTimerStatus=alaAutoFabricGlobalConfigSaveTimerStatus, alaAutoFabricPortConfigIfIndex=alaAutoFabricPortConfigIfIndex, alaAutoFabricPortConfig=alaAutoFabricPortConfig, alaAutoFabricBaseGroup=alaAutoFabricBaseGroup, alaAutoFabricGlobalDiscovery=alaAutoFabricGlobalDiscovery, alaAutoFabricGlobalStatus=alaAutoFabricGlobalStatus, alcatelIND1AUTOFABRICMIBCompliance=alcatelIND1AUTOFABRICMIBCompliance, alcatelIND1AUTOFABRICMIBCompliances=alcatelIND1AUTOFABRICMIBCompliances, alaAutoFabricGlobalSPBProtocolStatus=alaAutoFabricGlobalSPBProtocolStatus, alaAutoFabricPortMVRPProtocolStatus=alaAutoFabricPortMVRPProtocolStatus, alaAutoFabricPortSPBProtocolStatus=alaAutoFabricPortSPBProtocolStatus, alaAutoFabricGlobalDiscoveryTimer=alaAutoFabricGlobalDiscoveryTimer)

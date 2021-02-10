#
# PySNMP MIB module ALCATEL-IND1-VIRTUALROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Vrf, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Vrf")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, Unsigned32, Gauge32, IpAddress, ObjectIdentity, NotificationType, ModuleIdentity, iso, Counter64, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "Unsigned32", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "ModuleIdentity", "iso", "Counter64", "TimeTicks", "MibIdentifier")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
alcatelIND1VirtualRouterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1))
alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setLastUpdated('201308230000Z')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setOrganization('Alcatel-Lucent')
alcatelIND1VirtualRouterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1))
alaVirtualRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1))
alaVirtualRouterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setStatus('current')
alaVirtualRouterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"))
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setStatus('current')
alaVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: alaVirtualRouterName.setStatus('current')
alaVirtualRouterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setStatus('current')
alaVirtualRouterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setStatus('current')
alaVirtualRouterProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterProfile.setStatus('current')
alaVirtualRouterMaxRouteMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxRouteMaps.setStatus('current')
alaVirtualRouterMaxSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxSequences.setStatus('current')
alaVirtualRouterMaxTlvs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxTlvs.setStatus('current')
alaVirtualRouterMaxAccessLists = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxAccessLists.setStatus('current')
alaVirtualRouterMaxAddressBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxAddressBlocks.setStatus('current')
alaVirtualRouterMaxMatchInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxMatchInterfaces.setStatus('current')
alaVirtualRouterNoAutoLoadVrrp = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNoAutoLoadVrrp.setStatus('current')
alaVrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2), )
if mibBuilder.loadTexts: alaVrConfigTable.setStatus('current')
alaVrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIndex"))
if mibBuilder.loadTexts: alaVrConfigEntry.setStatus('current')
alaVrConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: alaVrConfigIndex.setStatus('current')
alaVrConfigRipStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigRipStatus.setStatus('current')
alaVrConfigOspfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigOspfStatus.setStatus('current')
alaVrConfigIsisStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigIsisStatus.setStatus('current')
alaVrConfigBgpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigBgpStatus.setStatus('current')
alaVrConfigPimStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigPimStatus.setStatus('current')
alaVrConfigDvmrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigDvmrpStatus.setStatus('current')
alaVrConfigRipngStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigRipngStatus.setStatus('current')
alaVrConfigOspf3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigOspf3Status.setStatus('current')
alaVrConfigMplsLdpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrConfigMplsLdpStatus.setStatus('current')
alaVrConfigVrrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigVrrpStatus.setStatus('current')
alaVirtualRouterProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3), )
if mibBuilder.loadTexts: alaVirtualRouterProfileTable.setStatus('current')
alaVirtualRouterProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileName"))
if mibBuilder.loadTexts: alaVirtualRouterProfileEntry.setStatus('current')
alaVirtualRouterProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: alaVirtualRouterProfileName.setStatus('current')
alaVirtualRouterProfileMaxRouteMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxRouteMaps.setStatus('current')
alaVirtualRouterProfileMaxSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxSequences.setStatus('current')
alaVirtualRouterProfileMaxTlvs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxTlvs.setStatus('current')
alaVirtualRouterProfileMaxAccessLists = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAccessLists.setStatus('current')
alaVirtualRouterProfileMaxAddressBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAddressBlocks.setStatus('current')
alaVirtualRouterProfileMaxMatchInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxMatchInterfaces.setStatus('current')
alcatelIND1VirtualRouterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2))
alcatelIND1VirtualRouterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1))
alcatelIND1VirtualRouterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2))
alaVirtualRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterCompliance = alaVirtualRouterCompliance.setStatus('current')
alaVirtualRouterConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfile"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxRouteMaps"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxSequences"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxTlvs"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAccessLists"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAddressBlocks"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxMatchInterfaces"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNoAutoLoadVrrp"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspfStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIsisStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigBgpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigPimStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigDvmrpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipngStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspf3Status"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigMplsLdpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigVrrpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxRouteMaps"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxSequences"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxTlvs"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAccessLists"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAddressBlocks"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxMatchInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterConfigMIBGroup = alaVirtualRouterConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", alaVrConfigIndex=alaVrConfigIndex, alaVrConfigDvmrpStatus=alaVrConfigDvmrpStatus, alaVirtualRouterMaxAddressBlocks=alaVirtualRouterMaxAddressBlocks, alaVrConfigEntry=alaVrConfigEntry, alaVirtualRouterMaxRouteMaps=alaVirtualRouterMaxRouteMaps, alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alaVirtualRouterCompliance=alaVirtualRouterCompliance, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects, alaVrConfigOspfStatus=alaVrConfigOspfStatus, alaVrConfigRipngStatus=alaVrConfigRipngStatus, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alaVirtualRouterProfileMaxSequences=alaVirtualRouterProfileMaxSequences, alaVirtualRouterProfileMaxTlvs=alaVirtualRouterProfileMaxTlvs, alaVrConfigTable=alaVrConfigTable, alaVirtualRouterMaxSequences=alaVirtualRouterMaxSequences, alaVirtualRouterMaxTlvs=alaVirtualRouterMaxTlvs, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alaVrConfigIsisStatus=alaVrConfigIsisStatus, alaVirtualRouterNoAutoLoadVrrp=alaVirtualRouterNoAutoLoadVrrp, alaVirtualRouterProfileMaxRouteMaps=alaVirtualRouterProfileMaxRouteMaps, alaVirtualRouterName=alaVirtualRouterName, alaVrConfigVrrpStatus=alaVrConfigVrrpStatus, alaVirtualRouterProfileMaxAccessLists=alaVirtualRouterProfileMaxAccessLists, PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alaVirtualRouterProfileTable=alaVirtualRouterProfileTable, alaVirtualRouterProfileMaxAddressBlocks=alaVirtualRouterProfileMaxAddressBlocks, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alaVrConfigMplsLdpStatus=alaVrConfigMplsLdpStatus, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alaVrConfigOspf3Status=alaVrConfigOspf3Status, alaVirtualRouterConfig=alaVirtualRouterConfig, alaVirtualRouterProfileName=alaVirtualRouterProfileName, alaVrConfigBgpStatus=alaVrConfigBgpStatus, alaVrConfigPimStatus=alaVrConfigPimStatus, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups, alaVirtualRouterProfileEntry=alaVirtualRouterProfileEntry, alaVrConfigRipStatus=alaVrConfigRipStatus, alaVirtualRouterProfileMaxMatchInterfaces=alaVirtualRouterProfileMaxMatchInterfaces, alaVirtualRouterMaxAccessLists=alaVirtualRouterMaxAccessLists, alaVirtualRouterMaxMatchInterfaces=alaVirtualRouterMaxMatchInterfaces, alaVirtualRouterProfile=alaVirtualRouterProfile)

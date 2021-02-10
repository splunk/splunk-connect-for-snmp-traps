#
# PySNMP MIB module H3C-DSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DSP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, iso, Gauge32, Counter64, NotificationType, Bits, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "iso", "Gauge32", "Counter64", "NotificationType", "Bits", "Unsigned32", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cDSP = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89))
h3cDSP.setRevisions(('2008-01-16 13:00',))
if mibBuilder.loadTexts: h3cDSP.setLastUpdated('200801161300Z')
if mibBuilder.loadTexts: h3cDSP.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cVPMStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1), )
if mibBuilder.loadTexts: h3cVPMStatusTable.setStatus('current')
h3cVPMStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1), ).setIndexNames((0, "H3C-DSP-MIB", "h3cVPMIndex"))
if mibBuilder.loadTexts: h3cVPMStatusEntry.setStatus('current')
h3cVPMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cVPMIndex.setStatus('current')
h3cVPMEnPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVPMEnPhysicalIndex.setStatus('current')
h3cVPMState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("fatal", 3), ("offLine", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVPMState.setStatus('current')
h3cVPMResourceUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVPMResourceUtilization.setStatus('current')
h3cVPMHiWaterUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVPMHiWaterUtilization.setStatus('current')
h3cVPMMaxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVPMMaxChannel.setStatus('current')
h3cDSPStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2), )
if mibBuilder.loadTexts: h3cDSPStatusTable.setStatus('current')
h3cDSPStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1), ).setIndexNames((0, "H3C-DSP-MIB", "h3cDSPIndex"))
if mibBuilder.loadTexts: h3cDSPStatusEntry.setStatus('current')
h3cDSPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDSPIndex.setStatus('current')
h3cDSPVPMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPVPMIndex.setStatus('current')
h3cDSPEnPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPEnPhysicalIndex.setStatus('current')
h3cDSPResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPResetTime.setStatus('current')
h3cDSPMaxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPMaxChannel.setStatus('current')
h3cDSPState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("fatal", 3), ("offLine", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPState.setStatus('current')
h3cDSPInUseChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDSPInUseChannel.setStatus('current')
h3cDSPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3))
h3cDSPTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0))
h3cVPMStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0, 1)).setObjects(("H3C-DSP-MIB", "h3cVPMIndex"), ("H3C-DSP-MIB", "h3cVPMEnPhysicalIndex"), ("H3C-DSP-MIB", "h3cVPMState"))
if mibBuilder.loadTexts: h3cVPMStateChange.setStatus('current')
h3cDSPStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0, 2)).setObjects(("H3C-DSP-MIB", "h3cDSPIndex"), ("H3C-DSP-MIB", "h3cDSPVPMIndex"), ("H3C-DSP-MIB", "h3cDSPEnPhysicalIndex"), ("H3C-DSP-MIB", "h3cDSPState"))
if mibBuilder.loadTexts: h3cDSPStateChange.setStatus('current')
mibBuilder.exportSymbols("H3C-DSP-MIB", h3cVPMEnPhysicalIndex=h3cVPMEnPhysicalIndex, PYSNMP_MODULE_ID=h3cDSP, h3cDSPStatusTable=h3cDSPStatusTable, h3cVPMState=h3cVPMState, h3cDSPResetTime=h3cDSPResetTime, h3cVPMStateChange=h3cVPMStateChange, h3cVPMStatusEntry=h3cVPMStatusEntry, h3cVPMHiWaterUtilization=h3cVPMHiWaterUtilization, h3cDSP=h3cDSP, h3cDSPVPMIndex=h3cDSPVPMIndex, h3cDSPTrapPrex=h3cDSPTrapPrex, h3cDSPIndex=h3cDSPIndex, h3cDSPStateChange=h3cDSPStateChange, h3cVPMMaxChannel=h3cVPMMaxChannel, h3cDSPTrap=h3cDSPTrap, h3cVPMStatusTable=h3cVPMStatusTable, h3cVPMIndex=h3cVPMIndex, h3cDSPStatusEntry=h3cDSPStatusEntry, h3cDSPState=h3cDSPState, h3cDSPInUseChannel=h3cDSPInUseChannel, h3cDSPEnPhysicalIndex=h3cDSPEnPhysicalIndex, h3cDSPMaxChannel=h3cDSPMaxChannel, h3cVPMResourceUtilization=h3cVPMResourceUtilization)

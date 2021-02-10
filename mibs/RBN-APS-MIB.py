#
# PySNMP MIB module RBN-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-APS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, TimeTicks, MibIdentifier, Gauge32, Bits, Counter32, Integer32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Gauge32", "Bits", "Counter32", "Integer32", "ModuleIdentity", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rbnApsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 5))
rbnApsMIB.setRevisions(('1999-05-07 23:00',))
if mibBuilder.loadTexts: rbnApsMIB.setLastUpdated('9905072300Z')
if mibBuilder.loadTexts: rbnApsMIB.setOrganization('RedBack Networks, Inc.')
rbnApsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 0))
rbnApsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1))
rbnApsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2))
class ApsK1K2(TextualConvention, Integer32):
    status = 'current'

apsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1))
apsConfigGroups = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsConfigGroups.setStatus('current')
apsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2), )
if mibBuilder.loadTexts: apsConfigTable.setStatus('current')
apsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1), ).setIndexNames((1, "RBN-APS-MIB", "apsConfigName"))
if mibBuilder.loadTexts: apsConfigEntry.setStatus('current')
apsConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: apsConfigName.setStatus('current')
apsConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("onePlusOne", 0), ("oneToN", 1), ("revertive", 2), ("bidirectional", 3), ("extraTrafficAllowed", 4))).clone(hexValue="1")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apsConfigMode.setStatus('current')
apsConfigSdBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apsConfigSdBerThreshold.setStatus('current')
apsConfigSfBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apsConfigSfBerThreshold.setStatus('current')
apsConfigWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 720)).clone(600)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apsConfigWaitToRestore.setStatus('current')
apsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apsConfigRowStatus.setStatus('current')
apsCommandTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2), )
if mibBuilder.loadTexts: apsCommandTable.setStatus('current')
apsCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1), ).setIndexNames((1, "RBN-APS-MIB", "apsConfigName"))
if mibBuilder.loadTexts: apsCommandEntry.setStatus('current')
apsCommandSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCommandSwitch.setStatus('current')
apsCommandControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCommandControl.setStatus('current')
apsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3), )
if mibBuilder.loadTexts: apsStatusTable.setStatus('current')
apsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1), ).setIndexNames((1, "RBN-APS-MIB", "apsConfigName"))
if mibBuilder.loadTexts: apsStatusEntry.setStatus('current')
apsStatusK1K2Rcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 1), ApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusK1K2Rcv.setStatus('current')
apsStatusK1K2Trans = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 2), ApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusK1K2Trans.setStatus('current')
apsStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("modeMismatch", 0), ("channelMismatch", 1), ("psbf", 2), ("extraTraffic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusCurrent.setStatus('current')
apsStatusModeMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusModeMismatches.setStatus('current')
apsStatusChannelMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusChannelMismatches.setStatus('current')
apsStatusPSBFs = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusPSBFs.setStatus('current')
apsStatusCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusCreationTime.setStatus('current')
apsChan = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4))
apsChanLTEs = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanLTEs.setStatus('current')
apsChanTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2), )
if mibBuilder.loadTexts: apsChanTable.setStatus('current')
apsChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1), ).setIndexNames((0, "RBN-APS-MIB", "apsChanIfIndex"))
if mibBuilder.loadTexts: apsChanEntry.setStatus('current')
apsChanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: apsChanIfIndex.setStatus('current')
apsChanGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsChanGroupName.setStatus('current')
apsChanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsChanNumber.setStatus('current')
apsChanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsChanPriority.setStatus('current')
apsChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 5), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sd", 1), ("sf", 2), ("switched", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanStatus.setStatus('current')
apsChanSignalDegrades = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanSignalDegrades.setStatus('current')
apsChanSignalFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanSignalFailures.setStatus('current')
apsChanSwitchovers = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanSwitchovers.setStatus('current')
apsChanLastSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsChanLastSwitchover.setStatus('current')
apsTrapSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 1)).setObjects(("RBN-APS-MIB", "apsChanSwitchovers"), ("RBN-APS-MIB", "apsChanStatus"))
if mibBuilder.loadTexts: apsTrapSwitchover.setStatus('current')
apsTrapModeMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 2)).setObjects(("RBN-APS-MIB", "apsStatusModeMismatches"), ("RBN-APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: apsTrapModeMismatch.setStatus('current')
apsTrapChannelMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 3)).setObjects(("RBN-APS-MIB", "apsStatusChannelMismatches"), ("RBN-APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: apsTrapChannelMismatch.setStatus('current')
apsTrapPSBF = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 4)).setObjects(("RBN-APS-MIB", "apsStatusPSBFs"), ("RBN-APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: apsTrapPSBF.setStatus('current')
apsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1))
apsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 2))
apsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 2, 1)).setObjects(("RBN-APS-MIB", "apsConfigGeneral"), ("RBN-APS-MIB", "apsStatusGeneral"), ("RBN-APS-MIB", "apsChanGeneral"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsCompliance = apsCompliance.setStatus('current')
apsConfigGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 1)).setObjects(("RBN-APS-MIB", "apsConfigMode"), ("RBN-APS-MIB", "apsConfigSdBerThreshold"), ("RBN-APS-MIB", "apsConfigSfBerThreshold"), ("RBN-APS-MIB", "apsConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsConfigGeneral = apsConfigGeneral.setStatus('current')
apsConfigOneToN = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 2)).setObjects(("RBN-APS-MIB", "apsConfigWaitToRestore"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsConfigOneToN = apsConfigOneToN.setStatus('current')
apsCommandOnePlusOne = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 3)).setObjects(("RBN-APS-MIB", "apsCommandSwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsCommandOnePlusOne = apsCommandOnePlusOne.setStatus('current')
apsCommandOneToN = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 4)).setObjects(("RBN-APS-MIB", "apsCommandSwitch"), ("RBN-APS-MIB", "apsCommandControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsCommandOneToN = apsCommandOneToN.setStatus('current')
apsStatusGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 5)).setObjects(("RBN-APS-MIB", "apsStatusK1K2Rcv"), ("RBN-APS-MIB", "apsStatusK1K2Trans"), ("RBN-APS-MIB", "apsStatusCurrent"), ("RBN-APS-MIB", "apsStatusModeMismatches"), ("RBN-APS-MIB", "apsStatusChannelMismatches"), ("RBN-APS-MIB", "apsStatusPSBFs"), ("RBN-APS-MIB", "apsStatusCreationTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsStatusGeneral = apsStatusGeneral.setStatus('current')
apsChanGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 6)).setObjects(("RBN-APS-MIB", "apsChanGroupName"), ("RBN-APS-MIB", "apsChanNumber"), ("RBN-APS-MIB", "apsChanStatus"), ("RBN-APS-MIB", "apsChanSignalDegrades"), ("RBN-APS-MIB", "apsChanSignalFailures"), ("RBN-APS-MIB", "apsChanSwitchovers"), ("RBN-APS-MIB", "apsChanLastSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsChanGeneral = apsChanGeneral.setStatus('current')
apsChanOneToN = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 7)).setObjects(("RBN-APS-MIB", "apsChanPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsChanOneToN = apsChanOneToN.setStatus('current')
apsTotalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 8)).setObjects(("RBN-APS-MIB", "apsConfigGroups"), ("RBN-APS-MIB", "apsChanLTEs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsTotalsGroup = apsTotalsGroup.setStatus('current')
apsTrapOptional = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 9)).setObjects(("RBN-APS-MIB", "apsTrapSwitchover"), ("RBN-APS-MIB", "apsTrapModeMismatch"), ("RBN-APS-MIB", "apsTrapChannelMismatch"), ("RBN-APS-MIB", "apsTrapPSBF"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apsTrapOptional = apsTrapOptional.setStatus('current')
mibBuilder.exportSymbols("RBN-APS-MIB", apsChanStatus=apsChanStatus, apsConfigMode=apsConfigMode, apsChan=apsChan, apsStatusModeMismatches=apsStatusModeMismatches, apsStatusChannelMismatches=apsStatusChannelMismatches, apsConfigTable=apsConfigTable, apsCommandTable=apsCommandTable, apsChanLTEs=apsChanLTEs, apsStatusTable=apsStatusTable, apsTrapModeMismatch=apsTrapModeMismatch, apsStatusK1K2Trans=apsStatusK1K2Trans, apsCommandControl=apsCommandControl, rbnApsMIBNotifications=rbnApsMIBNotifications, apsStatusPSBFs=apsStatusPSBFs, apsTotalsGroup=apsTotalsGroup, apsChanOneToN=apsChanOneToN, apsConfigWaitToRestore=apsConfigWaitToRestore, apsStatusEntry=apsStatusEntry, apsConfigName=apsConfigName, apsChanGroupName=apsChanGroupName, apsCommandEntry=apsCommandEntry, apsConfigOneToN=apsConfigOneToN, apsChanTable=apsChanTable, ApsK1K2=ApsK1K2, apsConfigSdBerThreshold=apsConfigSdBerThreshold, apsChanIfIndex=apsChanIfIndex, apsChanGeneral=apsChanGeneral, apsCompliances=apsCompliances, apsCompliance=apsCompliance, rbnApsMIBObjects=rbnApsMIBObjects, apsConfigSfBerThreshold=apsConfigSfBerThreshold, apsChanSignalDegrades=apsChanSignalDegrades, apsChanEntry=apsChanEntry, apsTrapSwitchover=apsTrapSwitchover, apsCommandOnePlusOne=apsCommandOnePlusOne, apsConfigEntry=apsConfigEntry, apsChanSwitchovers=apsChanSwitchovers, apsChanPriority=apsChanPriority, apsTrapChannelMismatch=apsTrapChannelMismatch, apsTrapPSBF=apsTrapPSBF, apsGroups=apsGroups, apsStatusGeneral=apsStatusGeneral, apsConfig=apsConfig, apsStatusK1K2Rcv=apsStatusK1K2Rcv, rbnApsMIB=rbnApsMIB, apsChanLastSwitchover=apsChanLastSwitchover, apsConfigGeneral=apsConfigGeneral, PYSNMP_MODULE_ID=rbnApsMIB, apsConfigRowStatus=apsConfigRowStatus, apsTrapOptional=apsTrapOptional, apsChanSignalFailures=apsChanSignalFailures, apsConfigGroups=apsConfigGroups, rbnApsMIBConformance=rbnApsMIBConformance, apsCommandSwitch=apsCommandSwitch, apsStatusCreationTime=apsStatusCreationTime, apsStatusCurrent=apsStatusCurrent, apsCommandOneToN=apsCommandOneToN, apsChanNumber=apsChanNumber)

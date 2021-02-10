#
# PySNMP MIB module SBFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SBFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
private, NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress, TimeTicks, Bits, Counter32, ObjectIdentity, iso, Counter64, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "private", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "iso", "Counter64", "enterprises", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stonesoft = MibIdentifier((1, 3, 6, 1, 4, 1, 1369))
stoneSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2))
fullCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2))
sbfcModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4))
sbfcDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5))
agentDescr = MibScalar((1, 3, 6, 1, 4, 1, 1369, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDescr.setStatus('mandatory')
agentVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentVersion.setStatus('mandatory')
sbfcClusterID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcClusterID.setStatus('mandatory')
sbfcMemberID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcMemberID.setStatus('mandatory')
sbfcModuleVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcModuleVersion.setStatus('mandatory')
sbfcModulePatchLevel = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcModulePatchLevel.setStatus('mandatory')
sbfcDriverPatchLevel = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcDriverPatchLevel.setStatus('mandatory')
sbfcDriverVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcDriverVersion.setStatus('mandatory')
sbfcMaxNodeID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcMaxNodeID.setStatus('mandatory')
sbfcOSName = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcOSName.setStatus('mandatory')
sbfcOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcOSVersion.setStatus('mandatory')
sbfcAgeOfStatus = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcAgeOfStatus.setStatus('mandatory')
sbfcNodeTable = MibTable((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9), )
if mibBuilder.loadTexts: sbfcNodeTable.setStatus('mandatory')
sbfcNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1), )
if mibBuilder.loadTexts: sbfcNodeEntry.setStatus('mandatory')
sbfcNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeID.setStatus('mandatory')
sbfcNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("offline", 1), ("going-online", 2), ("online", 3), ("going-offline", 4), ("unknown", 5), ("offline-ready-for-restart", 6), ("online-ready-for-restart", 7), ("locked-offline", 8), ("going-locked-offline", 9), ("locked-online", 10), ("going-locked-online", 11), ("locked-offline-ready-for-restart", 12), ("locked-online-ready-for-restart", 13), ("standby", 14), ("going-standby", 15), ("standby-ready-for-restart", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeStatus.setStatus('mandatory')
sbfcNodeLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeLoad.setStatus('mandatory')
sbfcNodeCapacity = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeCapacity.setStatus('mandatory')
sbfcNodeControlIp = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeControlIp.setStatus('mandatory')
sbfcNodeControlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeControlPort.setStatus('mandatory')
mibBuilder.exportSymbols("SBFC-MIB", products=products, sbfcModule=sbfcModule, sbfcNodeControlPort=sbfcNodeControlPort, stonesoft=stonesoft, sbfcNodeStatus=sbfcNodeStatus, agentVersion=agentVersion, sbfcDriverPatchLevel=sbfcDriverPatchLevel, sbfcMaxNodeID=sbfcMaxNodeID, sbfcModuleVersion=sbfcModuleVersion, agentDescr=agentDescr, stoneSystem=stoneSystem, sbfcNodeControlIp=sbfcNodeControlIp, sbfcModulePatchLevel=sbfcModulePatchLevel, sbfcMemberID=sbfcMemberID, sbfcOSVersion=sbfcOSVersion, sbfcNodeCapacity=sbfcNodeCapacity, sbfcNodeLoad=sbfcNodeLoad, fullCluster=fullCluster, sbfcDriver=sbfcDriver, sbfcClusterID=sbfcClusterID, sbfcDriverVersion=sbfcDriverVersion, sbfcNodeEntry=sbfcNodeEntry, sbfcAgeOfStatus=sbfcAgeOfStatus, sbfcNodeTable=sbfcNodeTable, sbfcNodeID=sbfcNodeID, sbfcOSName=sbfcOSName)

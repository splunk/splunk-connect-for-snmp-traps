#
# PySNMP MIB module PDN-SONETEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SONETEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
pdnSonetMIB, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnSonetMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, NotificationType, Counter32, ModuleIdentity, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, TimeTicks, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "TimeTicks", "NotificationType", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonetPathCurrentStatus, sonetSectionCurrentStatus, sonetLineCurrentStatus = mibBuilder.importSymbols("SONET-MIB", "sonetPathCurrentStatus", "sonetSectionCurrentStatus", "sonetLineCurrentStatus")
devSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1))
devSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2))
devSonetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1), )
if mibBuilder.loadTexts: devSonetConfigTable.setStatus('mandatory')
devSonetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1), ).setIndexNames((0, "PDN-SONETEXT-MIB", "devSonetIfIndex"))
if mibBuilder.loadTexts: devSonetConfigEntry.setStatus('mandatory')
devSonetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetIfIndex.setStatus('mandatory')
devSonetXmitClkSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetXmitClkSrc.setStatus('mandatory')
devSonetStatusLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetStatusLastChange.setStatus('mandatory')
devSonetStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetStatusChangeTrapEnable.setStatus('mandatory')
devSonetStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2) + (0,1)).setObjects(("PDN-SONETEXT-MIB", "devSonetStatusLastChange"), ("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetPathCurrentStatus"))
mibBuilder.exportSymbols("PDN-SONETEXT-MIB", devSonetStatusChange=devSonetStatusChange, devSonetConfigEntry=devSonetConfigEntry, devSonetTraps=devSonetTraps, devSonetConfig=devSonetConfig, devSonetStatusChangeTrapEnable=devSonetStatusChangeTrapEnable, devSonetConfigTable=devSonetConfigTable, devSonetXmitClkSrc=devSonetXmitClkSrc, devSonetIfIndex=devSonetIfIndex, devSonetStatusLastChange=devSonetStatusLastChange)

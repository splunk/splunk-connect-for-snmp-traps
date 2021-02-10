#
# PySNMP MIB module BAY-STACK-LLDP-EXT-DOT3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-LLDP-EXT-DOT3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
lldpXdot3RemPowerEntry, lldpXdot3LocPowerEntry = mibBuilder.importSymbols("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerEntry", "lldpXdot3LocPowerEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, NotificationType, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ModuleIdentity, Integer32, MibIdentifier, Bits, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "NotificationType", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackLldpXDot3Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 47))
bayStackLldpXDot3Mib.setRevisions(('2014-10-22 00:00',))
if mibBuilder.loadTexts: bayStackLldpXDot3Mib.setLastUpdated('201410220000Z')
if mibBuilder.loadTexts: bayStackLldpXDot3Mib.setOrganization('Avaya Inc.')
bsLldpXDot3Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 47, 0))
bsLldpXDot3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 47, 1))
bsLldpXdot3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 1))
bsLldpXdot3LocalData = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2))
bsLldpXdot3RemoteData = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3))
bsLldpXdot3LocPowerTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1), )
if mibBuilder.loadTexts: bsLldpXdot3LocPowerTable.setStatus('current')
bsLldpXdot3LocPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1), )
lldpXdot3LocPowerEntry.registerAugmentions(("BAY-STACK-LLDP-EXT-DOT3-MIB", "bsLldpXdot3LocPowerEntry"))
bsLldpXdot3LocPowerEntry.setIndexNames(*lldpXdot3LocPowerEntry.getIndexNames())
if mibBuilder.loadTexts: bsLldpXdot3LocPowerEntry.setStatus('current')
bsLldpXdot3LocPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("type2pse", 1), ("type2pd", 2), ("type1pse", 3), ("type1pd", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3LocPowerType.setStatus('current')
bsLldpXdot3LocPowerSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("primaryPs", 2), ("backupPs", 3), ("reserved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3LocPowerSource.setStatus('current')
bsLldpXdot3LocPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("critical", 2), ("high", 3), ("low", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3LocPowerPriority.setStatus('current')
bsLldpXdot3LocPDRequestedPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('tenth of watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3LocPDRequestedPowerValue.setStatus('current')
bsLldpXdot3LocPSEAllocatedPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('tenth of watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3LocPSEAllocatedPowerValue.setStatus('current')
bsLldpXdot3RemPowerTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1), )
if mibBuilder.loadTexts: bsLldpXdot3RemPowerTable.setStatus('current')
bsLldpXdot3RemPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1), )
lldpXdot3RemPowerEntry.registerAugmentions(("BAY-STACK-LLDP-EXT-DOT3-MIB", "bsLldpXdot3RemPowerEntry"))
bsLldpXdot3RemPowerEntry.setIndexNames(*lldpXdot3RemPowerEntry.getIndexNames())
if mibBuilder.loadTexts: bsLldpXdot3RemPowerEntry.setStatus('current')
bsLldpXdot3RemPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("type2pse", 1), ("type2pd", 2), ("type1pse", 3), ("type1pd", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3RemPowerType.setStatus('current')
bsLldpXdot3RemPowerSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("pse", 2), ("reserved", 3), ("pseAndLocal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3RemPowerSource.setStatus('current')
bsLldpXdot3RemPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("critical", 2), ("high", 3), ("low", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3RemPowerPriority.setStatus('current')
bsLldpXdot3RemPDRequestedPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('tenth of watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3RemPDRequestedPowerValue.setStatus('current')
bsLldpXdot3RemPSEAllocatedPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('tenth of watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLldpXdot3RemPSEAllocatedPowerValue.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-LLDP-EXT-DOT3-MIB", bsLldpXdot3RemPowerType=bsLldpXdot3RemPowerType, bsLldpXdot3LocPowerType=bsLldpXdot3LocPowerType, bsLldpXdot3LocPSEAllocatedPowerValue=bsLldpXdot3LocPSEAllocatedPowerValue, bsLldpXdot3LocPowerEntry=bsLldpXdot3LocPowerEntry, bsLldpXDot3Notifications=bsLldpXDot3Notifications, bsLldpXDot3Objects=bsLldpXDot3Objects, PYSNMP_MODULE_ID=bayStackLldpXDot3Mib, bsLldpXdot3RemPowerTable=bsLldpXdot3RemPowerTable, bsLldpXdot3RemPDRequestedPowerValue=bsLldpXdot3RemPDRequestedPowerValue, bsLldpXdot3RemPSEAllocatedPowerValue=bsLldpXdot3RemPSEAllocatedPowerValue, bsLldpXdot3LocalData=bsLldpXdot3LocalData, bsLldpXdot3RemPowerEntry=bsLldpXdot3RemPowerEntry, bsLldpXdot3Config=bsLldpXdot3Config, bsLldpXdot3LocPowerTable=bsLldpXdot3LocPowerTable, bsLldpXdot3LocPDRequestedPowerValue=bsLldpXdot3LocPDRequestedPowerValue, bayStackLldpXDot3Mib=bayStackLldpXDot3Mib, bsLldpXdot3RemPowerPriority=bsLldpXdot3RemPowerPriority, bsLldpXdot3RemoteData=bsLldpXdot3RemoteData, bsLldpXdot3LocPowerSource=bsLldpXdot3LocPowerSource, bsLldpXdot3RemPowerSource=bsLldpXdot3RemPowerSource, bsLldpXdot3LocPowerPriority=bsLldpXdot3LocPowerPriority)

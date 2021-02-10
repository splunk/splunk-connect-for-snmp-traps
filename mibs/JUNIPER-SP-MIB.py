#
# PySNMP MIB module JUNIPER-SP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, iso, Counter64, Integer32, Gauge32, NotificationType, Bits, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "iso", "Counter64", "Integer32", "Gauge32", "NotificationType", "Bits", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxSpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32))
jnxSpMIB.setRevisions(('2005-04-02 00:00',))
if mibBuilder.loadTexts: jnxSpMIB.setLastUpdated('200504050000Z')
if mibBuilder.loadTexts: jnxSpMIB.setOrganization('Juniper Networks, Inc.')
jnxSpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0))
jnxFlowLimitTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2))
jnxSpSvcSet = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1))
if mibBuilder.loadTexts: jnxSpSvcSet.setStatus('current')
jnxSpSvcSetTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1), )
if mibBuilder.loadTexts: jnxSpSvcSetTable.setStatus('current')
jnxSpSvcSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"))
if mibBuilder.loadTexts: jnxSpSvcSetEntry.setStatus('current')
jnxSpSvcSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)))
if mibBuilder.loadTexts: jnxSpSvcSetName.setStatus('current')
jnxSpSvcSetSvcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcType.setStatus('current')
jnxSpSvcSetTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetTypeIndex.setStatus('current')
jnxSpSvcSetIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfName.setStatus('current')
jnxSpSvcSetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfIndex.setStatus('current')
jnxSpSvcSetMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 6), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetMemoryUsage.setStatus('current')
jnxSpSvcSetCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 7), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetCpuUtil.setStatus('current')
jnxSpSvcSetSvcStyle = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("interface-service", 2), ("next-hop-service", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcStyle.setStatus('current')
jnxSpSvcSetMemLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetMemLimitPktDrops.setStatus('current')
jnxSpSvcSetCpuLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetCpuLimitPktDrops.setStatus('current')
jnxSpSvcSetFlowLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitPktDrops.setStatus('current')
jnxSpSvcSetSvcTypeTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2), )
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeTable.setStatus('current')
jnxSpSvcSetSvcTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-SP-MIB", "jnxSpSvcSetSvcTypeIndex"))
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeEntry.setStatus('current')
jnxSpSvcSetSvcTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIndex.setStatus('current')
jnxSpSvcSetSvcTypeIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIfName.setStatus('current')
jnxSpSvcSetSvcTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeName.setStatus('current')
jnxSpSvcSetSvcTypeSvcSets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeSvcSets.setStatus('current')
jnxSpSvcSetSvcTypeMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage.setStatus('current')
jnxSpSvcSetSvcTypePctMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 6), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypePctMemoryUsage.setStatus('current')
jnxSpSvcSetSvcTypeCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 7), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeCpuUtil.setStatus('current')
jnxSpSvcSetSvcTypeMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 8), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage64.setStatus('current')
jnxSpSvcSetIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3), )
if mibBuilder.loadTexts: jnxSpSvcSetIfTable.setStatus('current')
jnxSpSvcSetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxSpSvcSetIfEntry.setStatus('current')
jnxSpSvcSetIfTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfTableName.setStatus('current')
jnxSpSvcSetIfSvcSets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfSvcSets.setStatus('current')
jnxSpSvcSetIfMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 3), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage.setStatus('current')
jnxSpSvcSetIfPctMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 4), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPctMemoryUsage.setStatus('current')
jnxSpSvcSetIfPolMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage.setStatus('current')
jnxSpSvcSetIfPctPolMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 6), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPctPolMemoryUsage.setStatus('current')
jnxSpSvcSetIfMemoryZone = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2), ("orange", 3), ("red", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryZone.setStatus('current')
jnxSpSvcSetIfCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 8), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfCpuUtil.setStatus('current')
jnxSpSvcSetIfMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 9), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage64.setStatus('current')
jnxSpSvcSetIfPolMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 10), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage64.setStatus('current')
jnxSpNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0))
if mibBuilder.loadTexts: jnxSpNotificationPrefix.setStatus('current')
jnxSpSvcSetZoneEntered = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 1)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetZoneEntered.setStatus('current')
jnxSpSvcSetZoneExited = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 2)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetZoneExited.setStatus('current')
jnxSpSvcSetCpuExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 3)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetCpuExceeded.setStatus('current')
jnxSpSvcSetCpuOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 4)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetCpuOk.setStatus('current')
jnxSpSvcSetFlowLimitUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtil.setStatus('current')
jnxSpSvcSetNameUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 96))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSpSvcSetNameUtil.setStatus('current')
jnxSpSvcSetFlowLimitUtilized = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 1)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetFlowLimitUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetNameUtil"))
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtilized.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-SP-MIB", jnxSpSvcSetCpuUtil=jnxSpSvcSetCpuUtil, jnxSpSvcSetNameUtil=jnxSpSvcSetNameUtil, jnxSpSvcSetIfPctMemoryUsage=jnxSpSvcSetIfPctMemoryUsage, jnxSpSvcSetSvcStyle=jnxSpSvcSetSvcStyle, jnxSpSvcSetFlowLimitUtilized=jnxSpSvcSetFlowLimitUtilized, jnxSpSvcSetIfSvcSets=jnxSpSvcSetIfSvcSets, jnxSpSvcSetIfCpuUtil=jnxSpSvcSetIfCpuUtil, jnxSpSvcSetIfMemoryUsage64=jnxSpSvcSetIfMemoryUsage64, jnxSpSvcSetSvcTypePctMemoryUsage=jnxSpSvcSetSvcTypePctMemoryUsage, jnxSpSvcSetIfEntry=jnxSpSvcSetIfEntry, jnxSpSvcSetIfMemoryUsage=jnxSpSvcSetIfMemoryUsage, jnxSpSvcSetIfMemoryZone=jnxSpSvcSetIfMemoryZone, jnxSpSvcSetMemoryUsage=jnxSpSvcSetMemoryUsage, jnxSpNotifications=jnxSpNotifications, jnxSpSvcSetSvcTypeIfName=jnxSpSvcSetSvcTypeIfName, jnxSpSvcSetIfTable=jnxSpSvcSetIfTable, jnxFlowLimitTrapVars=jnxFlowLimitTrapVars, jnxSpSvcSetSvcTypeTable=jnxSpSvcSetSvcTypeTable, jnxSpSvcSetSvcTypeMemoryUsage64=jnxSpSvcSetSvcTypeMemoryUsage64, jnxSpSvcSetIfName=jnxSpSvcSetIfName, jnxSpSvcSet=jnxSpSvcSet, jnxSpSvcSetSvcTypeCpuUtil=jnxSpSvcSetSvcTypeCpuUtil, jnxSpSvcSetZoneEntered=jnxSpSvcSetZoneEntered, jnxSpSvcSetZoneExited=jnxSpSvcSetZoneExited, jnxSpSvcSetCpuExceeded=jnxSpSvcSetCpuExceeded, jnxSpSvcSetSvcType=jnxSpSvcSetSvcType, jnxSpSvcSetCpuLimitPktDrops=jnxSpSvcSetCpuLimitPktDrops, jnxSpSvcSetIfTableName=jnxSpSvcSetIfTableName, jnxSpSvcSetTable=jnxSpSvcSetTable, jnxSpSvcSetSvcTypeSvcSets=jnxSpSvcSetSvcTypeSvcSets, jnxSpSvcSetIfIndex=jnxSpSvcSetIfIndex, jnxSpSvcSetEntry=jnxSpSvcSetEntry, jnxSpSvcSetIfPctPolMemoryUsage=jnxSpSvcSetIfPctPolMemoryUsage, jnxSpSvcSetCpuOk=jnxSpSvcSetCpuOk, jnxSpSvcSetMemLimitPktDrops=jnxSpSvcSetMemLimitPktDrops, jnxSpSvcSetIfPolMemoryUsage=jnxSpSvcSetIfPolMemoryUsage, jnxSpSvcSetFlowLimitUtil=jnxSpSvcSetFlowLimitUtil, PYSNMP_MODULE_ID=jnxSpMIB, jnxSpMIB=jnxSpMIB, jnxSpSvcSetTypeIndex=jnxSpSvcSetTypeIndex, jnxSpSvcSetIfPolMemoryUsage64=jnxSpSvcSetIfPolMemoryUsage64, jnxSpSvcSetFlowLimitPktDrops=jnxSpSvcSetFlowLimitPktDrops, jnxSpSvcSetSvcTypeName=jnxSpSvcSetSvcTypeName, jnxSpSvcSetSvcTypeMemoryUsage=jnxSpSvcSetSvcTypeMemoryUsage, jnxSpNotificationPrefix=jnxSpNotificationPrefix, jnxSpSvcSetName=jnxSpSvcSetName, jnxSpSvcSetSvcTypeEntry=jnxSpSvcSetSvcTypeEntry, jnxSpSvcSetSvcTypeIndex=jnxSpSvcSetSvcTypeIndex)

#
# PySNMP MIB module AT-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, MibIdentifier, ObjectIdentity, TimeTicks, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Gauge32, iso, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
dhcp = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70))
dhcp.setRevisions(('2009-04-01 02:00', '2006-06-28 12:22',))
if mibBuilder.loadTexts: dhcp.setLastUpdated('200904010200Z')
if mibBuilder.loadTexts: dhcp.setOrganization('Allied Telesis, Inc')
dhcpRangeTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1), )
if mibBuilder.loadTexts: dhcpRangeTable.setStatus('current')
dhcpRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1), ).setIndexNames((0, "AT-DHCP-MIB", "dhcpRangeIndex"))
if mibBuilder.loadTexts: dhcpRangeEntry.setStatus('current')
dhcpRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeIndex.setStatus('current')
dhcpRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeName.setStatus('current')
dhcpRangeBaseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeBaseAddress.setStatus('current')
dhcpRangeNumberOfAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeNumberOfAddresses.setStatus('current')
dhcpRangeGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeGateway.setStatus('current')
dhcpTrapVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2))
dhcpRangeExhaustedGateway = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExhaustedGateway.setStatus('current')
dhcpRangeExhaustedInterface = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExhaustedInterface.setStatus('current')
dhcpRangeExceededRange = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExceededRange.setStatus('current')
dhcpRangeExceededClients = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExceededClients.setStatus('current')
dhcpRangeExceededRemaining = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExceededRemaining.setStatus('current')
dhcpRangeExceededPercentage = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeExceededPercentage.setStatus('current')
dhcpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0))
dhcpRangeExhaustedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 1)).setObjects(("AT-DHCP-MIB", "dhcpRangeExhaustedGateway"), ("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"))
if mibBuilder.loadTexts: dhcpRangeExhaustedTrap.setStatus('current')
dhcpRangeExceededThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 2)).setObjects(("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"), ("AT-DHCP-MIB", "dhcpRangeExceededRange"), ("AT-DHCP-MIB", "dhcpRangeExceededClients"), ("AT-DHCP-MIB", "dhcpRangeExceededRemaining"), ("AT-DHCP-MIB", "dhcpRangeExceededPercentage"))
if mibBuilder.loadTexts: dhcpRangeExceededThresholdTrap.setStatus('current')
dhcpRangeExceededThresholdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 3)).setObjects(("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"), ("AT-DHCP-MIB", "dhcpRangeExceededRange"), ("AT-DHCP-MIB", "dhcpRangeExceededClients"), ("AT-DHCP-MIB", "dhcpRangeExceededRemaining"), ("AT-DHCP-MIB", "dhcpRangeExceededPercentage"))
if mibBuilder.loadTexts: dhcpRangeExceededThresholdClearTrap.setStatus('current')
dhcpClientTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3), )
if mibBuilder.loadTexts: dhcpClientTable.setStatus('current')
dhcpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1), ).setIndexNames((0, "AT-DHCP-MIB", "dhcpRangeIndex"), (0, "AT-DHCP-MIB", "dhcpClientIpAddress"))
if mibBuilder.loadTexts: dhcpClientEntry.setStatus('current')
dhcpClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientIpAddress.setStatus('current')
dhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientID.setStatus('current')
dhcpClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unused", 0), ("reclaiming", 1), ("inuse", 2), ("offered", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientState.setStatus('current')
dhcpClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("dyn", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientType.setStatus('current')
dhcpClientExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientExpiry.setStatus('current')
mibBuilder.exportSymbols("AT-DHCP-MIB", dhcpClientState=dhcpClientState, dhcpRangeExhaustedGateway=dhcpRangeExhaustedGateway, dhcpTrapVariable=dhcpTrapVariable, dhcpRangeName=dhcpRangeName, dhcpRangeNumberOfAddresses=dhcpRangeNumberOfAddresses, dhcpRangeExceededThresholdTrap=dhcpRangeExceededThresholdTrap, dhcpClientType=dhcpClientType, dhcpRangeExceededRange=dhcpRangeExceededRange, dhcpRangeExhaustedInterface=dhcpRangeExhaustedInterface, dhcpClientTable=dhcpClientTable, dhcpRangeExceededClients=dhcpRangeExceededClients, dhcp=dhcp, dhcpRangeTable=dhcpRangeTable, dhcpRangeExhaustedTrap=dhcpRangeExhaustedTrap, dhcpClientID=dhcpClientID, dhcpClientIpAddress=dhcpClientIpAddress, dhcpRangeExceededRemaining=dhcpRangeExceededRemaining, dhcpClientExpiry=dhcpClientExpiry, dhcpRangeEntry=dhcpRangeEntry, PYSNMP_MODULE_ID=dhcp, dhcpRangeExceededPercentage=dhcpRangeExceededPercentage, dhcpTraps=dhcpTraps, dhcpRangeGateway=dhcpRangeGateway, dhcpClientEntry=dhcpClientEntry, dhcpRangeIndex=dhcpRangeIndex, dhcpRangeExceededThresholdClearTrap=dhcpRangeExceededThresholdClearTrap, dhcpRangeBaseAddress=dhcpRangeBaseAddress)

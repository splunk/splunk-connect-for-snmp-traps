#
# PySNMP MIB module JUNIPER-MOBILE-GATEWAY-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MOBILE-GATEWAY-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
InetAddress, InetAddressType, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetAddressPrefixLength")
jnxMobileGatewayMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMobileGatewayMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, MibIdentifier, iso, ModuleIdentity, Bits, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "Bits", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter32", "Gauge32", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
jnxMbgDhcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8))
jnxMbgDhcpMib.setRevisions(('2011-03-30 12:00',))
if mibBuilder.loadTexts: jnxMbgDhcpMib.setLastUpdated('201103301200Z')
if mibBuilder.loadTexts: jnxMbgDhcpMib.setOrganization('Juniper Networks, Inc.')
jnxMbgDhcpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0))
jnxMbgDhcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1))
jnxMbgDhcpNotificationVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1))
jnxMbgDhcpServerIP = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpServerIP.setStatus('current')
jnxMbgDhcpLogicalSystemName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpLogicalSystemName.setStatus('current')
jnxMbgDhcpRoutingInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpRoutingInstanceName.setStatus('current')
jnxMbgDhcpProfileName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpProfileName.setStatus('current')
jnxMbgDhcpPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpPoolName.setStatus('current')
jnxMbgDhcpReachability = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 6), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgDhcpReachability.setStatus('current')
jnxMbgDhcpServerReachability = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0, 1)).setObjects(("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpServerIP"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpLogicalSystemName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpRoutingInstanceName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpProfileName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpReachability"))
if mibBuilder.loadTexts: jnxMbgDhcpServerReachability.setStatus('current')
jnxMbgDhcpAddrPoolExhaust = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0, 2)).setObjects(("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpServerIP"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpLogicalSystemName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpRoutingInstanceName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpProfileName"), ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpPoolName"))
if mibBuilder.loadTexts: jnxMbgDhcpAddrPoolExhaust.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", jnxMbgDhcpReachability=jnxMbgDhcpReachability, jnxMbgDhcpAddrPoolExhaust=jnxMbgDhcpAddrPoolExhaust, PYSNMP_MODULE_ID=jnxMbgDhcpMib, jnxMbgDhcpNotifications=jnxMbgDhcpNotifications, jnxMbgDhcpRoutingInstanceName=jnxMbgDhcpRoutingInstanceName, jnxMbgDhcpObjects=jnxMbgDhcpObjects, jnxMbgDhcpLogicalSystemName=jnxMbgDhcpLogicalSystemName, jnxMbgDhcpNotificationVars=jnxMbgDhcpNotificationVars, jnxMbgDhcpMib=jnxMbgDhcpMib, jnxMbgDhcpPoolName=jnxMbgDhcpPoolName, jnxMbgDhcpServerReachability=jnxMbgDhcpServerReachability, jnxMbgDhcpServerIP=jnxMbgDhcpServerIP, jnxMbgDhcpProfileName=jnxMbgDhcpProfileName)

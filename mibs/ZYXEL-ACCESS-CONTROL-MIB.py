#
# PySNMP MIB module ZYXEL-ACCESS-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ACCESS-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter64, ObjectIdentity, iso, Integer32, IpAddress, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter64", "ObjectIdentity", "iso", "Integer32", "IpAddress", "ModuleIdentity", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelAccessControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9))
if mibBuilder.loadTexts: zyxelAccessControl.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelAccessControl.setOrganization('Enterprise Solution ZyXEL')
zyxelAccessControlSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1))
zyxelAccessControlTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1), )
if mibBuilder.loadTexts: zyxelAccessControlTable.setStatus('current')
zyxelAccessControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1), ).setIndexNames((0, "ZYXEL-ACCESS-CONTROL-MIB", "zyAccessControlService"))
if mibBuilder.loadTexts: zyxelAccessControlEntry.setStatus('current')
zyAccessControlService = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("ftp", 3), ("http", 4), ("https", 5), ("icmp", 6), ("snmp", 7), ("console", 8))))
if mibBuilder.loadTexts: zyAccessControlService.setStatus('current')
zyAccessControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAccessControlState.setStatus('current')
zyAccessControlServicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAccessControlServicePort.setStatus('current')
zyAccessControlTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAccessControlTimeout.setStatus('current')
zyxelSecuredClientTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2), )
if mibBuilder.loadTexts: zyxelSecuredClientTable.setStatus('current')
zyxelSecuredClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1), ).setIndexNames((0, "ZYXEL-ACCESS-CONTROL-MIB", "zySecuredClientIndex"))
if mibBuilder.loadTexts: zyxelSecuredClientEntry.setStatus('current')
zySecuredClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zySecuredClientIndex.setStatus('current')
zySecuredClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySecuredClientState.setStatus('current')
zySecuredClientStartIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySecuredClientStartIpAddress.setStatus('current')
zySecuredClientEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySecuredClientEndIpAddress.setStatus('current')
zySecuredClientService = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 9, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("telnet", 0), ("ftp", 1), ("http", 2), ("icmp", 3), ("snmp", 4), ("ssh", 5), ("https", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySecuredClientService.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ACCESS-CONTROL-MIB", zySecuredClientState=zySecuredClientState, zyxelAccessControlSetup=zyxelAccessControlSetup, zySecuredClientService=zySecuredClientService, zySecuredClientEndIpAddress=zySecuredClientEndIpAddress, zyAccessControlTimeout=zyAccessControlTimeout, zyxelSecuredClientEntry=zyxelSecuredClientEntry, zySecuredClientIndex=zySecuredClientIndex, zyAccessControlServicePort=zyAccessControlServicePort, zyxelAccessControl=zyxelAccessControl, zyxelAccessControlEntry=zyxelAccessControlEntry, zySecuredClientStartIpAddress=zySecuredClientStartIpAddress, PYSNMP_MODULE_ID=zyxelAccessControl, zyxelSecuredClientTable=zyxelSecuredClientTable, zyxelAccessControlTable=zyxelAccessControlTable, zyAccessControlService=zyAccessControlService, zyAccessControlState=zyAccessControlState)

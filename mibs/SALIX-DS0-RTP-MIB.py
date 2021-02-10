#
# PySNMP MIB module SALIX-DS0-RTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-DS0-RTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
platform1, = mibBuilder.importSymbols("SALIX-MIB", "platform1")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Bits, ObjectIdentity, Unsigned32, Integer32, ModuleIdentity, Counter32, iso, TimeTicks, Counter64, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "ModuleIdentity", "Counter32", "iso", "TimeTicks", "Counter64", "Gauge32", "NotificationType")
DisplayString, TextualConvention, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "RowStatus")
salixDsx0RtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3))
if mibBuilder.loadTexts: salixDsx0RtpMIB.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixDsx0RtpMIB.setOrganization('SALIX Technologies')
salixDsx0RtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1))
salixDsx0RtpMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 2))
salixDsx0RtpMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3))
salixDsx0RtpMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 2, 0))
salixDsx0RtpConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1), )
if mibBuilder.loadTexts: salixDsx0RtpConnectionTable.setStatus('current')
salixDsx0RtpConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1), ).setIndexNames((0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionInterface"), (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionSrcIpAddress"), (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionSrcPort"), (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDestIpAddress"), (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDestPort"))
if mibBuilder.loadTexts: salixDsx0RtpConnectionEntry.setStatus('current')
salixDsx0RtpConnectionInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: salixDsx0RtpConnectionInterface.setStatus('current')
salixDsx0RtpConnectionSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: salixDsx0RtpConnectionSrcIpAddress.setStatus('current')
salixDsx0RtpConnectionSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: salixDsx0RtpConnectionSrcPort.setStatus('current')
salixDsx0RtpConnectionDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: salixDsx0RtpConnectionDestIpAddress.setStatus('current')
salixDsx0RtpConnectionDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: salixDsx0RtpConnectionDestPort.setStatus('current')
salixDsx0RtpConnectionDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rtp2dsx0", 1), ("dsx02rtp", 2), ("bidirectional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixDsx0RtpConnectionDirection.setStatus('current')
salixDsx0RtpConnectionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixDsx0RtpConnectionOperStatus.setStatus('current')
salixDsx0RtpConnectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx0RtpConnectionRowStatus.setStatus('current')
salixDsx0RtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 1))
salixDsx0RtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 2))
salixDsx0RtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 1, 3)).setObjects(("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDirection"), ("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionOperStatus"), ("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixDsx0RtpGroup = salixDsx0RtpGroup.setStatus('current')
salixDsx0RtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 2, 1)).setObjects(("SALIX-DS0-RTP-MIB", "salixDsx0RtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixDsx0RtpCompliance = salixDsx0RtpCompliance.setStatus('current')
mibBuilder.exportSymbols("SALIX-DS0-RTP-MIB", salixDsx0RtpConnectionOperStatus=salixDsx0RtpConnectionOperStatus, salixDsx0RtpMIB=salixDsx0RtpMIB, salixDsx0RtpConnectionDestPort=salixDsx0RtpConnectionDestPort, salixDsx0RtpGroup=salixDsx0RtpGroup, salixDsx0RtpConnectionInterface=salixDsx0RtpConnectionInterface, salixDsx0RtpConnectionSrcIpAddress=salixDsx0RtpConnectionSrcIpAddress, salixDsx0RtpMIBTraps=salixDsx0RtpMIBTraps, salixDsx0RtpConnectionRowStatus=salixDsx0RtpConnectionRowStatus, salixDsx0RtpConnectionSrcPort=salixDsx0RtpConnectionSrcPort, salixDsx0RtpMIBObjects=salixDsx0RtpMIBObjects, salixDsx0RtpConnectionDirection=salixDsx0RtpConnectionDirection, salixDsx0RtpCompliances=salixDsx0RtpCompliances, salixDsx0RtpCompliance=salixDsx0RtpCompliance, salixDsx0RtpConnectionDestIpAddress=salixDsx0RtpConnectionDestIpAddress, PYSNMP_MODULE_ID=salixDsx0RtpMIB, salixDsx0RtpMIBCompliance=salixDsx0RtpMIBCompliance, salixDsx0RtpMIBTrapPrefix=salixDsx0RtpMIBTrapPrefix, salixDsx0RtpConnectionTable=salixDsx0RtpConnectionTable, salixDsx0RtpConnectionEntry=salixDsx0RtpConnectionEntry, salixDsx0RtpGroups=salixDsx0RtpGroups)

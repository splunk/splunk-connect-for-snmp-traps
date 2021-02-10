#
# PySNMP MIB module DHCPCLIENT-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DHCPCLIENT-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, ObjectIdentity, Unsigned32, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Counter64, MibIdentifier, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Counter64", "MibIdentifier", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dhcpClientPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 100))
if mibBuilder.loadTexts: dhcpClientPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: dhcpClientPrivate.setOrganization('QCI')
agentdhcp4ClientLeaseParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1))
agentdhcp4ClientLeaseParametersTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1), )
if mibBuilder.loadTexts: agentdhcp4ClientLeaseParametersTable.setStatus('current')
agentdhcp4ClientLeaseParametersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1), ).setIndexNames((0, "DHCPCLIENT-PRIVATE-MIB", "agentdhcp4ClientInterfaceIndex"))
if mibBuilder.loadTexts: agentdhcp4ClientLeaseParametersEntry.setStatus('current')
agentdhcp4ClientInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentdhcp4ClientInterfaceIndex.setStatus('current')
agentdhcp4ClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientIpAddress.setStatus('current')
agentdhcp4ClientSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientSubnetMask.setStatus('current')
agentdhcp4ClientDhcpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientDhcpServerAddress.setStatus('current')
agentdhcp4ClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("init", 1), ("selecting", 2), ("requesting", 3), ("request-recv", 4), ("bound", 5), ("renewing", 6), ("renew-recv", 7), ("rebinding", 8), ("rebind-recv", 9), ("bootp-fallback", 10), ("not-bound", 11), ("failed", 12), ("do-release", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientState.setStatus('current')
agentdhcp4ClientTransactionID = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientTransactionID.setStatus('current')
agentdhcp4ClientLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientLeaseTime.setStatus('current')
agentdhcp4ClientRenewTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientRenewTime.setStatus('current')
agentdhcp4ClientRebindTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientRebindTime.setStatus('current')
agentdhcp4ClientRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentdhcp4ClientRetryCount.setStatus('current')
mibBuilder.exportSymbols("DHCPCLIENT-PRIVATE-MIB", PYSNMP_MODULE_ID=dhcpClientPrivate, dhcpClientPrivate=dhcpClientPrivate, agentdhcp4ClientInterfaceIndex=agentdhcp4ClientInterfaceIndex, agentdhcp4ClientState=agentdhcp4ClientState, agentdhcp4ClientRebindTime=agentdhcp4ClientRebindTime, agentdhcp4ClientRetryCount=agentdhcp4ClientRetryCount, agentdhcp4ClientLeaseParameters=agentdhcp4ClientLeaseParameters, agentdhcp4ClientRenewTime=agentdhcp4ClientRenewTime, agentdhcp4ClientDhcpServerAddress=agentdhcp4ClientDhcpServerAddress, agentdhcp4ClientTransactionID=agentdhcp4ClientTransactionID, agentdhcp4ClientLeaseTime=agentdhcp4ClientLeaseTime, agentdhcp4ClientLeaseParametersEntry=agentdhcp4ClientLeaseParametersEntry, agentdhcp4ClientLeaseParametersTable=agentdhcp4ClientLeaseParametersTable, agentdhcp4ClientIpAddress=agentdhcp4ClientIpAddress, agentdhcp4ClientSubnetMask=agentdhcp4ClientSubnetMask)

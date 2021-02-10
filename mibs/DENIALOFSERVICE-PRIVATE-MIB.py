#
# PySNMP MIB module DENIALOFSERVICE-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DENIALOFSERVICE-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:23:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity, Unsigned32, Gauge32, Counter32, Integer32, MibIdentifier, IpAddress, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter32", "Integer32", "MibIdentifier", "IpAddress", "TimeTicks", "ModuleIdentity")
DisplayString, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "RowStatus")
denialOfService = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 31))
if mibBuilder.loadTexts: denialOfService.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: denialOfService.setOrganization('QCI')
agentSwitchDenialOfServiceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1))
agentSwitchDenialOfServiceSIPDIPMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceSIPDIPMode.setStatus('current')
agentSwitchDenialOfServiceSMACDMACMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceSMACDMACMode.setStatus('current')
agentSwitchDenialOfServiceFirstFragMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceFirstFragMode.setStatus('current')
agentSwitchDenialOfServiceTCPHdrSize = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPHdrSize.setStatus('current')
agentSwitchDenialOfServiceTCPFragMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPFragMode.setStatus('current')
agentSwitchDenialOfServiceTCPOffsetMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPOffsetMode.setStatus('current')
agentSwitchDenialOfServiceTCPFlagMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPFlagMode.setStatus('current')
agentSwitchDenialOfServiceTCPFlagSeqMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPFlagSeqMode.setStatus('current')
agentSwitchDenialOfServiceTCPSynMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPSynMode.setStatus('current')
agentSwitchDenialOfServiceTCPSynFinMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPSynFinMode.setStatus('current')
agentSwitchDenialOfServiceTCPFinUrgPshMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPFinUrgPshMode.setStatus('current')
agentSwitchDenialOfServiceL4PortMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceL4PortMode.setStatus('current')
agentSwitchDenialOfServiceTCPPortMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceTCPPortMode.setStatus('current')
agentSwitchDenialOfServiceUDPPortMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceUDPPortMode.setStatus('current')
agentSwitchDenialOfServiceICMPMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceICMPMode.setStatus('current')
agentSwitchDenialOfServiceICMPv6Mode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceICMPv6Mode.setStatus('current')
agentSwitchDenialOfServiceICMPSize = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16376)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceICMPSize.setStatus('current')
agentSwitchDenialOfServiceICMPv6Size = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16376)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceICMPv6Size.setStatus('current')
agentSwitchDenialOfServiceICMPFragMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 31, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchDenialOfServiceICMPFragMode.setStatus('current')
mibBuilder.exportSymbols("DENIALOFSERVICE-PRIVATE-MIB", agentSwitchDenialOfServiceTCPHdrSize=agentSwitchDenialOfServiceTCPHdrSize, PYSNMP_MODULE_ID=denialOfService, agentSwitchDenialOfServiceUDPPortMode=agentSwitchDenialOfServiceUDPPortMode, agentSwitchDenialOfServiceTCPFragMode=agentSwitchDenialOfServiceTCPFragMode, agentSwitchDenialOfServiceICMPFragMode=agentSwitchDenialOfServiceICMPFragMode, agentSwitchDenialOfServiceTCPSynFinMode=agentSwitchDenialOfServiceTCPSynFinMode, agentSwitchDenialOfServiceTCPFinUrgPshMode=agentSwitchDenialOfServiceTCPFinUrgPshMode, agentSwitchDenialOfServiceTCPSynMode=agentSwitchDenialOfServiceTCPSynMode, denialOfService=denialOfService, agentSwitchDenialOfServiceICMPv6Mode=agentSwitchDenialOfServiceICMPv6Mode, agentSwitchDenialOfServiceICMPMode=agentSwitchDenialOfServiceICMPMode, agentSwitchDenialOfServiceL4PortMode=agentSwitchDenialOfServiceL4PortMode, agentSwitchDenialOfServiceTCPOffsetMode=agentSwitchDenialOfServiceTCPOffsetMode, agentSwitchDenialOfServiceTCPPortMode=agentSwitchDenialOfServiceTCPPortMode, agentSwitchDenialOfServiceICMPv6Size=agentSwitchDenialOfServiceICMPv6Size, agentSwitchDenialOfServiceICMPSize=agentSwitchDenialOfServiceICMPSize, agentSwitchDenialOfServiceGroup=agentSwitchDenialOfServiceGroup, agentSwitchDenialOfServiceTCPFlagMode=agentSwitchDenialOfServiceTCPFlagMode, agentSwitchDenialOfServiceSMACDMACMode=agentSwitchDenialOfServiceSMACDMACMode, agentSwitchDenialOfServiceFirstFragMode=agentSwitchDenialOfServiceFirstFragMode, agentSwitchDenialOfServiceTCPFlagSeqMode=agentSwitchDenialOfServiceTCPFlagSeqMode, agentSwitchDenialOfServiceSIPDIPMode=agentSwitchDenialOfServiceSIPDIPMode)

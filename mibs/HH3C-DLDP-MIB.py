#
# PySNMP MIB module HH3C-DLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, TimeTicks, Unsigned32, Counter64, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity, ObjectIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter64", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Bits")
TruthValue, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "MacAddress")
hh3cDldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 43))
hh3cDldp.setRevisions(('2004-12-13 00:00',))
if mibBuilder.loadTexts: hh3cDldp.setLastUpdated('200412130000Z')
if mibBuilder.loadTexts: hh3cDldp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class DLDPStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 1), ("inactive", 2), ("active", 3), ("advertisement", 4), ("probe", 5), ("disable", 6))

class DLDPNeighborStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unidirection", 1), ("bidirection", 2), ("unknown", 3))

hh3cDLDPMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1))
hh3cDLDPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1))
hh3cDLDPWorkMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("enhance", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPWorkMode.setStatus('current')
hh3cDLDPSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPSystemEnable.setStatus('current')
hh3cDLDPSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPSystemReset.setStatus('current')
hh3cDLDPInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPInterval.setStatus('current')
hh3cDLDPAuthenticationMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPAuthenticationMode.setStatus('current')
hh3cDLDPAuthenticationPassword = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPAuthenticationPassword.setStatus('current')
hh3cDLDPUnidirectionalShutdown = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPUnidirectionalShutdown.setStatus('current')
hh3cDLDPPortStateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2), )
if mibBuilder.loadTexts: hh3cDLDPPortStateTable.setStatus('current')
hh3cDLDPPortStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDLDPPortStateEntry.setStatus('current')
hh3cDLDPPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPPortState.setStatus('current')
hh3cDLDPPortDLDPTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3), )
if mibBuilder.loadTexts: hh3cDLDPPortDLDPTable.setStatus('current')
hh3cDLDPPortDLDPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDLDPPortDLDPEntry.setStatus('current')
hh3cDLDPPortDLDPState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 1), DLDPStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDLDPPortDLDPState.setStatus('current')
hh3cDLDPLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDLDPLinkState.setStatus('current')
hh3cDLDPPortDLDPReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDLDPPortDLDPReset.setStatus('current')
hh3cDLDPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4), )
if mibBuilder.loadTexts: hh3cDLDPNeighborTable.setStatus('current')
hh3cDLDPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DLDP-MIB", "hh3cDLDPNeighborBridgeMac"), (0, "HH3C-DLDP-MIB", "hh3cDLDPNeighborPortIndex"))
if mibBuilder.loadTexts: hh3cDLDPNeighborEntry.setStatus('current')
hh3cDLDPNeighborBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cDLDPNeighborBridgeMac.setStatus('current')
hh3cDLDPNeighborPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: hh3cDLDPNeighborPortIndex.setStatus('current')
hh3cDLDPNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 3), DLDPNeighborStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDLDPNeighborState.setStatus('current')
hh3cDLDPNeighborAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDLDPNeighborAgingTime.setStatus('current')
hh3cDLDPTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 43, 2))
hh3cDLDPNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 43, 2, 1))
hh3cDLDPUnidirectionalPort = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 43, 2, 1, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDLDPUnidirectionalPort.setStatus('current')
mibBuilder.exportSymbols("HH3C-DLDP-MIB", hh3cDLDPMibObject=hh3cDLDPMibObject, hh3cDLDPPortDLDPReset=hh3cDLDPPortDLDPReset, hh3cDLDPPortDLDPTable=hh3cDLDPPortDLDPTable, hh3cDLDPTrapObject=hh3cDLDPTrapObject, hh3cDLDPNeighborBridgeMac=hh3cDLDPNeighborBridgeMac, hh3cDLDPNeighborTable=hh3cDLDPNeighborTable, hh3cDLDPNeighborState=hh3cDLDPNeighborState, hh3cDLDPInterval=hh3cDLDPInterval, hh3cDLDPPortState=hh3cDLDPPortState, hh3cDLDPUnidirectionalPort=hh3cDLDPUnidirectionalPort, hh3cDLDPWorkMode=hh3cDLDPWorkMode, hh3cDLDPPortStateTable=hh3cDLDPPortStateTable, hh3cDLDPNeighborPortIndex=hh3cDLDPNeighborPortIndex, EnabledStatus=EnabledStatus, hh3cDLDPNeighborAgingTime=hh3cDLDPNeighborAgingTime, hh3cDLDPLinkState=hh3cDLDPLinkState, hh3cDLDPUnidirectionalShutdown=hh3cDLDPUnidirectionalShutdown, hh3cDLDPAuthenticationMode=hh3cDLDPAuthenticationMode, hh3cDLDPPortStateEntry=hh3cDLDPPortStateEntry, DLDPNeighborStatus=DLDPNeighborStatus, hh3cDldp=hh3cDldp, hh3cDLDPAuthenticationPassword=hh3cDLDPAuthenticationPassword, PYSNMP_MODULE_ID=hh3cDldp, DLDPStatus=DLDPStatus, hh3cDLDPConfigGroup=hh3cDLDPConfigGroup, hh3cDLDPSystemEnable=hh3cDLDPSystemEnable, hh3cDLDPNotification=hh3cDLDPNotification, hh3cDLDPPortDLDPState=hh3cDLDPPortDLDPState, hh3cDLDPSystemReset=hh3cDLDPSystemReset, hh3cDLDPPortDLDPEntry=hh3cDLDPPortDLDPEntry, hh3cDLDPNeighborEntry=hh3cDLDPNeighborEntry)

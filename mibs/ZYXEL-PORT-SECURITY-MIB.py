#
# PySNMP MIB module ZYXEL-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-PORT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, iso, Gauge32, MibIdentifier, Counter64, Unsigned32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "Gauge32", "MibIdentifier", "Counter64", "Unsigned32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "TimeTicks", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPortSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66))
if mibBuilder.loadTexts: zyxelPortSecurity.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPortSecurity.setOrganization('Enterprise Solution ZyXEL')
zyxelPortSecuritySetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1))
zyPortSecurityState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityState.setStatus('current')
zyxelPortSecurityPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2), )
if mibBuilder.loadTexts: zyxelPortSecurityPortTable.setStatus('current')
zyxelPortSecurityPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortSecurityPortEntry.setStatus('current')
zyPortSecurityPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityPortState.setStatus('current')
zyPortSecurityPortLearnState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityPortLearnState.setStatus('current')
zyPortSecurityPortMacLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityPortMacLimit.setStatus('current')
zyPortSecurityMacFreeze = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityMacFreeze.setStatus('current')
zyPortSecurityMaxNumberOfVMLs = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPortSecurityMaxNumberOfVMLs.setStatus('current')
zyxelPortSecurityVMLTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5), )
if mibBuilder.loadTexts: zyxelPortSecurityVMLTable.setStatus('current')
zyxelPortSecurityVMLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1), ).setIndexNames((0, "ZYXEL-PORT-SECURITY-MIB", "zyPortSecurityVMLPort"), (0, "ZYXEL-PORT-SECURITY-MIB", "zyPortSecurityVMLVID"))
if mibBuilder.loadTexts: zyxelPortSecurityVMLEntry.setStatus('current')
zyPortSecurityVMLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: zyPortSecurityVMLPort.setStatus('current')
zyPortSecurityVMLVID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: zyPortSecurityVMLVID.setStatus('current')
zyPortSecurityVMLMacLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortSecurityVMLMacLimit.setStatus('current')
zyPortSecurityVMLRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyPortSecurityVMLRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-SECURITY-MIB", PYSNMP_MODULE_ID=zyxelPortSecurity, zyPortSecurityVMLMacLimit=zyPortSecurityVMLMacLimit, zyxelPortSecurity=zyxelPortSecurity, zyxelPortSecurityVMLTable=zyxelPortSecurityVMLTable, zyPortSecurityMacFreeze=zyPortSecurityMacFreeze, zyPortSecurityPortState=zyPortSecurityPortState, zyxelPortSecurityPortEntry=zyxelPortSecurityPortEntry, zyPortSecurityMaxNumberOfVMLs=zyPortSecurityMaxNumberOfVMLs, zyPortSecurityPortMacLimit=zyPortSecurityPortMacLimit, zyxelPortSecurityVMLEntry=zyxelPortSecurityVMLEntry, zyxelPortSecurityPortTable=zyxelPortSecurityPortTable, zyPortSecurityVMLVID=zyPortSecurityVMLVID, zyPortSecurityVMLRowStatus=zyPortSecurityVMLRowStatus, zyxelPortSecuritySetup=zyxelPortSecuritySetup, zyPortSecurityState=zyPortSecurityState, zyPortSecurityVMLPort=zyPortSecurityVMLPort, zyPortSecurityPortLearnState=zyPortSecurityPortLearnState)

#
# PySNMP MIB module HPN-ICF-EPON-FB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EPON-FB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hpnicfEpon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfEpon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Gauge32, Bits, Counter64, NotificationType, MibIdentifier, Integer32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Gauge32", "Bits", "Counter64", "NotificationType", "MibIdentifier", "Integer32", "TimeTicks", "Counter32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpnicfEponFBMibObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6))
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setLastUpdated('200711271008Z')
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setOrganization('')
hpnicfEponFBMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1))
hpnicfEponFBMIBTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1), )
if mibBuilder.loadTexts: hpnicfEponFBMIBTable.setStatus('current')
hpnicfEponFBMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-EPON-FB-MIB", "hpnicfEponFBGroupIndex"))
if mibBuilder.loadTexts: hpnicfEponFBMIBEntry.setStatus('current')
hpnicfEponFBGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfEponFBGroupIndex.setStatus('current')
hpnicfEponFBGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBGroupRowStatus.setStatus('current')
hpnicfEponFBMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBMasterPort.setStatus('current')
hpnicfEponFBSlavePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBSlavePort.setStatus('current')
hpnicfEponFBMasterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEponFBMasterPortStatus.setStatus('current')
hpnicfEponFBSlavePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEponFBSlavePortStatus.setStatus('current')
hpnicfEponFBSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBSwitchover.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-EPON-FB-MIB", hpnicfEponFBMIBEntry=hpnicfEponFBMIBEntry, hpnicfEponFBGroupIndex=hpnicfEponFBGroupIndex, hpnicfEponFBGroupRowStatus=hpnicfEponFBGroupRowStatus, hpnicfEponFBMasterPortStatus=hpnicfEponFBMasterPortStatus, hpnicfEponFBMasterPort=hpnicfEponFBMasterPort, hpnicfEponFBMIB=hpnicfEponFBMIB, hpnicfEponFBMIBTable=hpnicfEponFBMIBTable, hpnicfEponFBSlavePortStatus=hpnicfEponFBSlavePortStatus, hpnicfEponFBMibObjects=hpnicfEponFBMibObjects, hpnicfEponFBSlavePort=hpnicfEponFBSlavePort, hpnicfEponFBSwitchover=hpnicfEponFBSwitchover, PYSNMP_MODULE_ID=hpnicfEponFBMibObjects)

#
# PySNMP MIB module PANDATEL-GMS-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-GMS-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mdmSpecifics, device_id = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "mdmSpecifics", "device-id")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Counter32, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, enterprises, Bits, Gauge32, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter32", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "enterprises", "Bits", "Gauge32", "iso", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gms_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 204)).setLabel("gms-modem")
gms = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204))
gmsModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1), )
if mibBuilder.loadTexts: gmsModemTable.setStatus('mandatory')
gmsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1), ).setIndexNames((0, "PANDATEL-GMS-MODEM-MIB", "mdmRack"), (0, "PANDATEL-GMS-MODEM-MIB", "mdmModem"), (0, "PANDATEL-GMS-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: gmsTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmDataEquipmentEmulation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmDataEquipmentEmulation.setStatus('mandatory')
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
mdmHDSLUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ntu", 2), ("ltu", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmHDSLUnit.setStatus('mandatory')
mdmClockSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dual", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSystem.setStatus('mandatory')
mdmClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("external", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSource.setStatus('mandatory')
mdmDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 204, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRate.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-GMS-MODEM-MIB", mdmModemProperty=mdmModemProperty, mdmClockSystem=mdmClockSystem, mdmClockSource=mdmClockSource, mdmModemName=mdmModemName, mdmHDSLUnit=mdmHDSLUnit, mdmPosition=mdmPosition, mdmRack=mdmRack, mdmDataRate=mdmDataRate, gms=gms, gmsTableEntry=gmsTableEntry, mdmDataEquipmentEmulation=mdmDataEquipmentEmulation, gmsModemTable=gmsModemTable, mdmModem=mdmModem, gms_modem=gms_modem)
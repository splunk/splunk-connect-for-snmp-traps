#
# PySNMP MIB module BN-IF-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BN-IF-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
s5IfExt, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5IfExt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, Counter64, NotificationType, TimeTicks, ObjectIdentity, Gauge32, MibIdentifier, iso, Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "Gauge32", "MibIdentifier", "iso", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bnIfExtensionsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 2))
bnIfExtensionsMib.setRevisions(('2013-07-26 00:00', '2011-10-05 00:00', '2011-09-16 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: bnIfExtensionsMib.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: bnIfExtensionsMib.setOrganization('Avaya')
bnIfExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1))
bnIfExtnTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1), )
if mibBuilder.loadTexts: bnIfExtnTable.setStatus('current')
bnIfExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1), ).setIndexNames((0, "BN-IF-EXTENSIONS-MIB", "bnIfExtnIndex"))
if mibBuilder.loadTexts: bnIfExtnEntry.setStatus('current')
bnIfExtnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnIfExtnIndex.setStatus('current')
bnIfExtnSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnIfExtnSlot.setStatus('current')
bnIfExtnPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnIfExtnPort.setStatus('current')
bnIfExtnIsPortShared = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portShared", 1), ("portNotShared", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnIfExtnIsPortShared.setStatus('current')
bnIfExtnPortActiveComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fixedPort", 1), ("gbicPort", 2), ("mdaPort", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnIfExtnPortActiveComponent.setStatus('current')
bnIfExtnPoweredDeviceDetectType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("compliantWith802dot3af", 1), ("compliantWith802dot3afAndLegacySupport", 2), ("compliantWith802dot3at", 3), ("compliantWith802dot3atAndLegacySupport", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnIfExtnPoweredDeviceDetectType.setStatus('current')
bnIfExtnAutoNegotiationExtAdv = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 7), Bits().clone(namedValues=NamedValues(("advertise10Half", 0), ("advertise10Full", 1), ("advertise100Half", 2), ("advertise100Full", 3), ("advertise1000Half", 4), ("advertise1000Full", 5), ("advertisePauseFrame", 6), ("advertiseAsymmPauseFrame", 7), ("advertise10000Full", 8), ("advertise40000Full", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnIfExtnAutoNegotiationExtAdv.setStatus('current')
bnIfExtnExtHwAdvCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("advertise10Half", 0), ("advertise10Full", 1), ("advertise100Half", 2), ("advertise100Full", 3), ("advertise1000Half", 4), ("advertise1000Full", 5), ("advertisePauseFrame", 6), ("advertiseAsymmPauseFrame", 7), ("advertise10000Full", 8), ("advertise40000Full", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnIfExtnExtHwAdvCapability.setStatus('current')
mibBuilder.exportSymbols("BN-IF-EXTENSIONS-MIB", bnIfExtnIsPortShared=bnIfExtnIsPortShared, bnIfExtnAutoNegotiationExtAdv=bnIfExtnAutoNegotiationExtAdv, bnIfExtnEntry=bnIfExtnEntry, bnIfExtensions=bnIfExtensions, bnIfExtnPortActiveComponent=bnIfExtnPortActiveComponent, bnIfExtnPoweredDeviceDetectType=bnIfExtnPoweredDeviceDetectType, bnIfExtnIndex=bnIfExtnIndex, bnIfExtnPort=bnIfExtnPort, bnIfExtnExtHwAdvCapability=bnIfExtnExtHwAdvCapability, bnIfExtensionsMib=bnIfExtensionsMib, PYSNMP_MODULE_ID=bnIfExtensionsMib, bnIfExtnSlot=bnIfExtnSlot, bnIfExtnTable=bnIfExtnTable)

#
# PySNMP MIB module XEDIA-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
atmInterfaceConfEntry, aal5VccEntry, atmTrafficDescrParamEntry, atmInterfaceDs3PlcpEntry = mibBuilder.importSymbols("ATM-MIB", "atmInterfaceConfEntry", "aal5VccEntry", "atmTrafficDescrParamEntry", "atmInterfaceDs3PlcpEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter32, Integer32, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, NotificationType, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "NotificationType", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaAtmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 12))
if mibBuilder.loadTexts: xediaAtmMIB.setLastUpdated('9801142155Z')
if mibBuilder.loadTexts: xediaAtmMIB.setOrganization('Xedia Corp.')
xAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 12, 1))
xAtmTables = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 12, 2))
xAtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 12, 3))
xAtmInterfaceConfTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1), )
if mibBuilder.loadTexts: xAtmInterfaceConfTable.setStatus('current')
xAtmInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1, 1), )
atmInterfaceConfEntry.registerAugmentions(("XEDIA-ATM-MIB", "xAtmInterfaceConfEntry"))
xAtmInterfaceConfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts: xAtmInterfaceConfEntry.setStatus('current')
xAtmInterfaceEmptyCells = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("unassigned", 2))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xAtmInterfaceEmptyCells.setStatus('current')
xAtmInterfaceDs3PlcpTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2), )
if mibBuilder.loadTexts: xAtmInterfaceDs3PlcpTable.setStatus('current')
xAtmInterfaceDs3PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2, 1), )
atmInterfaceDs3PlcpEntry.registerAugmentions(("XEDIA-ATM-MIB", "xAtmInterfaceDs3PlcpEntry"))
xAtmInterfaceDs3PlcpEntry.setIndexNames(*atmInterfaceDs3PlcpEntry.getIndexNames())
if mibBuilder.loadTexts: xAtmInterfaceDs3PlcpEntry.setStatus('current')
xAtmInterfaceDs3PlcpCellAlign = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hec", 1), ("plcp", 2))).clone('hec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xAtmInterfaceDs3PlcpCellAlign.setStatus('current')
xAtmTrafficDescrTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3), )
if mibBuilder.loadTexts: xAtmTrafficDescrTable.setStatus('current')
xAtmTrafficDescrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("XEDIA-ATM-MIB", "xAtmTrafficDescrEntry"))
xAtmTrafficDescrEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: xAtmTrafficDescrEntry.setStatus('current')
xAtmTrafficDescrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xAtmTrafficDescrDescr.setStatus('current')
xAtmTrafficDescrQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ubr", 0), ("cbr", 1), ("vbrAudioVideo", 2), ("vbrConnData", 3), ("vbrConnlessData", 4))).clone('ubr')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xAtmTrafficDescrQoSClass.setStatus('current')
xAtmAal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4), )
if mibBuilder.loadTexts: xAtmAal5VccTable.setStatus('current')
xAtmAal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1), )
aal5VccEntry.registerAugmentions(("XEDIA-ATM-MIB", "xAtmAal5VccEntry"))
xAtmAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
if mibBuilder.loadTexts: xAtmAal5VccEntry.setStatus('current')
xAtmAal5VccTxPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccTxPdus.setStatus('current')
xAtmAal5VccTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccTxOctets.setStatus('current')
xAtmAal5VccTxPduFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccTxPduFailures.setStatus('current')
xAtmAal5VccRxPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccRxPdus.setStatus('current')
xAtmAal5VccRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccRxOctets.setStatus('current')
xAtmAal5VccRxPduDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xAtmAal5VccRxPduDiscards.setStatus('current')
xAtmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 1))
xAtmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 2))
xAtmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 1, 1)).setObjects(("XEDIA-ATM-MIB", "xAtmAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xAtmCompliance = xAtmCompliance.setStatus('current')
xAtmAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 2, 1)).setObjects(("XEDIA-ATM-MIB", "xAtmInterfaceEmptyCells"), ("XEDIA-ATM-MIB", "xAtmInterfaceDs3PlcpCellAlign"), ("XEDIA-ATM-MIB", "xAtmTrafficDescrDescr"), ("XEDIA-ATM-MIB", "xAtmTrafficDescrQoSClass"), ("XEDIA-ATM-MIB", "xAtmAal5VccTxPdus"), ("XEDIA-ATM-MIB", "xAtmAal5VccTxOctets"), ("XEDIA-ATM-MIB", "xAtmAal5VccTxPduFailures"), ("XEDIA-ATM-MIB", "xAtmAal5VccRxPdus"), ("XEDIA-ATM-MIB", "xAtmAal5VccRxOctets"), ("XEDIA-ATM-MIB", "xAtmAal5VccRxPduDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xAtmAllGroup = xAtmAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-ATM-MIB", xAtmInterfaceConfEntry=xAtmInterfaceConfEntry, xAtmAal5VccRxOctets=xAtmAal5VccRxOctets, PYSNMP_MODULE_ID=xediaAtmMIB, xAtmInterfaceDs3PlcpCellAlign=xAtmInterfaceDs3PlcpCellAlign, xAtmCompliances=xAtmCompliances, xAtmInterfaceDs3PlcpEntry=xAtmInterfaceDs3PlcpEntry, xAtmTrafficDescrTable=xAtmTrafficDescrTable, xAtmAal5VccEntry=xAtmAal5VccEntry, xAtmAal5VccTable=xAtmAal5VccTable, xAtmAal5VccRxPduDiscards=xAtmAal5VccRxPduDiscards, xAtmTrafficDescrEntry=xAtmTrafficDescrEntry, xAtmTrafficDescrQoSClass=xAtmTrafficDescrQoSClass, xediaAtmMIB=xediaAtmMIB, xAtmAal5VccRxPdus=xAtmAal5VccRxPdus, xAtmInterfaceDs3PlcpTable=xAtmInterfaceDs3PlcpTable, xAtmObjects=xAtmObjects, xAtmTables=xAtmTables, xAtmAal5VccTxOctets=xAtmAal5VccTxOctets, xAtmTrafficDescrDescr=xAtmTrafficDescrDescr, xAtmAal5VccTxPduFailures=xAtmAal5VccTxPduFailures, xAtmInterfaceEmptyCells=xAtmInterfaceEmptyCells, xAtmGroups=xAtmGroups, xAtmAllGroup=xAtmAllGroup, xAtmAal5VccTxPdus=xAtmAal5VccTxPdus, xAtmInterfaceConfTable=xAtmInterfaceConfTable, xAtmCompliance=xAtmCompliance, xAtmConformance=xAtmConformance)

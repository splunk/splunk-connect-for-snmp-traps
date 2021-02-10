#
# PySNMP MIB module HH3C-EVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-EVC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, Unsigned32, ModuleIdentity, Bits, Integer32, MibIdentifier, Counter32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Bits", "Integer32", "MibIdentifier", "Counter32", "TimeTicks", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hh3cEvc = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 106))
hh3cEvc.setRevisions(('2009-08-08 10:00',))
if mibBuilder.loadTexts: hh3cEvc.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: hh3cEvc.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cEvcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1))
hh3cEvcScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1))
hh3cEvcSrvInstEncapCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 1), Bits().clone(namedValues=NamedValues(("encapPortBased", 0), ("encapUntagged", 1), ("encapTagged", 2), ("encapSvlanId", 3), ("encapSvlanIdList", 4), ("encapSvlanIdOnlyTagged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cEvcSrvInstEncapCapabilities.setStatus('current')
hh3cEvcPortMaxSrvInstNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cEvcPortMaxSrvInstNum.setStatus('current')
hh3cEvcSrvInstTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2), )
if mibBuilder.loadTexts: hh3cEvcSrvInstTable.setStatus('current')
hh3cEvcSrvInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-EVC-MIB", "hh3cEvcSrvInstId"))
if mibBuilder.loadTexts: hh3cEvcSrvInstEntry.setStatus('current')
hh3cEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cEvcSrvInstId.setStatus('current')
hh3cEvcSrvInstEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("portBased", 1), ("untagged", 2), ("tagged", 3), ("svlanIdList", 4), ("svlanIdListOnlyTagged", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvcSrvInstEncap.setStatus('current')
hh3cEvcSrvInstSvlanIdListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvcSrvInstSvlanIdListLow.setStatus('current')
hh3cEvcSrvInstSvlanIdListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvcSrvInstSvlanIdListHigh.setStatus('current')
hh3cEvcSrvInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvcSrvInstRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-EVC-MIB", hh3cEvcObjects=hh3cEvcObjects, hh3cEvcScalarGroup=hh3cEvcScalarGroup, hh3cEvcPortMaxSrvInstNum=hh3cEvcPortMaxSrvInstNum, hh3cEvcSrvInstRowStatus=hh3cEvcSrvInstRowStatus, hh3cEvcSrvInstEncapCapabilities=hh3cEvcSrvInstEncapCapabilities, hh3cEvcSrvInstSvlanIdListLow=hh3cEvcSrvInstSvlanIdListLow, hh3cEvcSrvInstEntry=hh3cEvcSrvInstEntry, hh3cEvcSrvInstSvlanIdListHigh=hh3cEvcSrvInstSvlanIdListHigh, hh3cEvcSrvInstEncap=hh3cEvcSrvInstEncap, hh3cEvcSrvInstTable=hh3cEvcSrvInstTable, PYSNMP_MODULE_ID=hh3cEvc, hh3cEvcSrvInstId=hh3cEvcSrvInstId, hh3cEvc=hh3cEvc)

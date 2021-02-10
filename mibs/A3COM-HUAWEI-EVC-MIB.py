#
# PySNMP MIB module A3COM-HUAWEI-EVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-EVC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, Counter32, TimeTicks, ModuleIdentity, Bits, Counter64, NotificationType, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "NotificationType", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
h3cEvc = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106))
h3cEvc.setRevisions(('2009-08-08 10:00',))
if mibBuilder.loadTexts: h3cEvc.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: h3cEvc.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cEvcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1))
h3cEvcScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1))
h3cEvcSrvInstEncapCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1, 1), Bits().clone(namedValues=NamedValues(("encapPortBased", 0), ("encapUntagged", 1), ("encapTagged", 2), ("encapSvlanId", 3), ("encapSvlanIdList", 4), ("encapSvlanIdOnlyTagged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstEncapCapabilities.setStatus('current')
h3cEvcPortMaxSrvInstNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcPortMaxSrvInstNum.setStatus('current')
h3cEvcSrvInstTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2), )
if mibBuilder.loadTexts: h3cEvcSrvInstTable.setStatus('current')
h3cEvcSrvInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"))
if mibBuilder.loadTexts: h3cEvcSrvInstEntry.setStatus('current')
h3cEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cEvcSrvInstId.setStatus('current')
h3cEvcSrvInstEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("portBased", 1), ("untagged", 2), ("tagged", 3), ("svlanIdList", 4), ("svlanIdListOnlyTagged", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstEncap.setStatus('current')
h3cEvcSrvInstSvlanIdListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstSvlanIdListLow.setStatus('current')
h3cEvcSrvInstSvlanIdListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstSvlanIdListHigh.setStatus('current')
h3cEvcSrvInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstRowStatus.setStatus('current')
h3cEvcSrvInstEnableInStat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstEnableInStat.setStatus('current')
h3cEvcSrvInstEnableOutStat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEvcSrvInstEnableOutStat.setStatus('current')
h3cEvcSrvInstCarTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3), )
if mibBuilder.loadTexts: h3cEvcSrvInstCarTable.setStatus('current')
h3cEvcSrvInstCarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"))
if mibBuilder.loadTexts: h3cEvcSrvInstCarEntry.setStatus('current')
h3cEvcSrvInstInCarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cEvcSrvInstInCarIndex.setStatus('current')
h3cEvcSrvInstOutCarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cEvcSrvInstOutCarIndex.setStatus('current')
h3cEvcSrvInstStatInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4), )
if mibBuilder.loadTexts: h3cEvcSrvInstStatInfoTable.setStatus('current')
h3cEvcSrvInstStatInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"))
if mibBuilder.loadTexts: h3cEvcSrvInstStatInfoEntry.setStatus('current')
h3cEvcSrvInstInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstInPackets.setStatus('current')
h3cEvcSrvInstInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 2), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstInBytes.setStatus('current')
h3cEvcSrvInstOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 3), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstOutPackets.setStatus('current')
h3cEvcSrvInstOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 4), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEvcSrvInstOutBytes.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-EVC-MIB", h3cEvcSrvInstEnableInStat=h3cEvcSrvInstEnableInStat, h3cEvcSrvInstInBytes=h3cEvcSrvInstInBytes, h3cEvcSrvInstStatInfoTable=h3cEvcSrvInstStatInfoTable, h3cEvcSrvInstOutCarIndex=h3cEvcSrvInstOutCarIndex, h3cEvcSrvInstEncapCapabilities=h3cEvcSrvInstEncapCapabilities, h3cEvcSrvInstSvlanIdListLow=h3cEvcSrvInstSvlanIdListLow, h3cEvcSrvInstInPackets=h3cEvcSrvInstInPackets, PYSNMP_MODULE_ID=h3cEvc, h3cEvcSrvInstEncap=h3cEvcSrvInstEncap, h3cEvcObjects=h3cEvcObjects, h3cEvcSrvInstId=h3cEvcSrvInstId, h3cEvcSrvInstInCarIndex=h3cEvcSrvInstInCarIndex, h3cEvcScalarGroup=h3cEvcScalarGroup, h3cEvc=h3cEvc, h3cEvcSrvInstEntry=h3cEvcSrvInstEntry, h3cEvcSrvInstRowStatus=h3cEvcSrvInstRowStatus, h3cEvcSrvInstEnableOutStat=h3cEvcSrvInstEnableOutStat, h3cEvcSrvInstCarEntry=h3cEvcSrvInstCarEntry, h3cEvcSrvInstStatInfoEntry=h3cEvcSrvInstStatInfoEntry, h3cEvcPortMaxSrvInstNum=h3cEvcPortMaxSrvInstNum, h3cEvcSrvInstTable=h3cEvcSrvInstTable, h3cEvcSrvInstOutPackets=h3cEvcSrvInstOutPackets, h3cEvcSrvInstCarTable=h3cEvcSrvInstCarTable, h3cEvcSrvInstSvlanIdListHigh=h3cEvcSrvInstSvlanIdListHigh, h3cEvcSrvInstOutBytes=h3cEvcSrvInstOutBytes)

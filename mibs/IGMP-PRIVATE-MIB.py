#
# PySNMP MIB module IGMP-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IGMP-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cjnProtocol, = mibBuilder.importSymbols("Cajun-ROOT", "cjnProtocol")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, IpAddress, Unsigned32, NotificationType, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ModuleIdentity, Integer32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ModuleIdentity", "Integer32", "Counter32", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
cjnIgmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11))
if mibBuilder.loadTexts: cjnIgmp.setLastUpdated('9909210000Z')
if mibBuilder.loadTexts: cjnIgmp.setOrganization("Lucent's Concord Technology Center (CTC)")
cjnIgmpGblGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1))
cjnIgmpIsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIsEnabled.setStatus('current')
cjnIpIgmpGblStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpIgmpGblStatsReset.setStatus('current')
cjnIgmpGblStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2))
cjnIgmpRxReport = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpRxReport.setStatus('current')
cjnIgmpRxQuery = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpRxQuery.setStatus('current')
cjnIgmpTxQuery = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpTxQuery.setStatus('current')
cjnIgmpRxUnknownCode = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpRxUnknownCode.setStatus('current')
cjnIgmpIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3))
cjnIgmpIfTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1), )
if mibBuilder.loadTexts: cjnIgmpIfTable.setStatus('current')
cjnIgmpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1), ).setIndexNames((0, "IGMP-PRIVATE-MIB", "cjnIgmpIfIndex"))
if mibBuilder.loadTexts: cjnIgmpIfEntry.setStatus('current')
cjnIgmpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIgmpIfIndex.setStatus('current')
cjnIgmpIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfRowStatus.setStatus('current')
cjnIgmpIfIsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2))).clone('v2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfIsVersion.setStatus('current')
cjnIgmpIfMaxGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfMaxGroups.setStatus('current')
cjnIgmpIfIsQuerier = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfIsQuerier.setStatus('current')
cjnIgmpIfProcessLeaves = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfProcessLeaves.setStatus('current')
cjnIgmpIfQueryReqIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(125)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfQueryReqIntvl.setStatus('current')
cjnIgmpIfQueryRspIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfQueryRspIntvl.setStatus('current')
cjnIgmpIfNbrQueryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 300)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfNbrQueryTimeout.setStatus('current')
cjnIgmpIfRobustVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfRobustVariable.setStatus('current')
cjnIgmpIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("down", 0), ("init", 1), ("querier", 2), ("nonQuerier", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIgmpIfState.setStatus('current')
cjnIgmpIfStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4))
cjnIgmpIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1), )
if mibBuilder.loadTexts: cjnIgmpIfStatTable.setStatus('current')
cjnIgmpIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1), ).setIndexNames((0, "IGMP-PRIVATE-MIB", "cjnIgmpIfIndex"))
if mibBuilder.loadTexts: cjnIgmpIfStatEntry.setStatus('current')
cjnIgmpIfQval = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfQval.setStatus('current')
cjnIgmpIfQpval = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfQpval.setStatus('current')
cjnIgmpIfJoins = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfJoins.setStatus('current')
cjnIgmpIfLeaves = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfLeaves.setStatus('current')
cjnIgmpIfRptRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfRptRcvd.setStatus('current')
cjnIgmpIfQueryRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfQueryRcvd.setStatus('current')
cjnIgmpIfQueryXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfQueryXmit.setStatus('current')
cjnIgmpIfWrongVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfWrongVer.setStatus('current')
cjnIgmpIfCurGrps = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIgmpIfCurGrps.setStatus('current')
mibBuilder.exportSymbols("IGMP-PRIVATE-MIB", cjnIgmpIsEnabled=cjnIgmpIsEnabled, cjnIgmpIfGroup=cjnIgmpIfGroup, cjnIgmpIfEntry=cjnIgmpIfEntry, cjnIgmpIfIndex=cjnIgmpIfIndex, cjnIgmpIfQueryRspIntvl=cjnIgmpIfQueryRspIntvl, cjnIgmpIfIsVersion=cjnIgmpIfIsVersion, cjnIgmpIfRobustVariable=cjnIgmpIfRobustVariable, cjnIgmpRxUnknownCode=cjnIgmpRxUnknownCode, cjnIgmpIfMaxGroups=cjnIgmpIfMaxGroups, cjnIgmpIfQval=cjnIgmpIfQval, cjnIgmpIfState=cjnIgmpIfState, cjnIgmpIfJoins=cjnIgmpIfJoins, cjnIgmpIfTable=cjnIgmpIfTable, cjnIgmpRxQuery=cjnIgmpRxQuery, cjnIgmpIfStatTable=cjnIgmpIfStatTable, cjnIgmpIfRowStatus=cjnIgmpIfRowStatus, cjnIgmpIfIsQuerier=cjnIgmpIfIsQuerier, cjnIgmpIfRptRcvd=cjnIgmpIfRptRcvd, cjnIgmpIfQueryRcvd=cjnIgmpIfQueryRcvd, cjnIgmpGblStatsGroup=cjnIgmpGblStatsGroup, PYSNMP_MODULE_ID=cjnIgmp, cjnIgmpIfStatGroup=cjnIgmpIfStatGroup, cjnIgmpIfNbrQueryTimeout=cjnIgmpIfNbrQueryTimeout, cjnIgmpTxQuery=cjnIgmpTxQuery, cjnIgmpIfStatEntry=cjnIgmpIfStatEntry, cjnIgmpIfProcessLeaves=cjnIgmpIfProcessLeaves, cjnIgmpIfQpval=cjnIgmpIfQpval, cjnIpIgmpGblStatsReset=cjnIpIgmpGblStatsReset, cjnIgmpGblGroup=cjnIgmpGblGroup, cjnIgmpIfQueryXmit=cjnIgmpIfQueryXmit, cjnIgmp=cjnIgmp, cjnIgmpIfWrongVer=cjnIgmpIfWrongVer, cjnIgmpIfCurGrps=cjnIgmpIfCurGrps, cjnIgmpRxReport=cjnIgmpRxReport, cjnIgmpIfQueryReqIntvl=cjnIgmpIfQueryReqIntvl, cjnIgmpIfLeaves=cjnIgmpIfLeaves)

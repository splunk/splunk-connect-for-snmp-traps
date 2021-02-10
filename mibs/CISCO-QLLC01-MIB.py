#
# PySNMP MIB module CISCO-QLLC01-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QLLC01-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ModuleIdentity, MibIdentifier, Counter32, Integer32, Bits, TimeTicks, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "Counter32", "Integer32", "Bits", "TimeTicks", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snaqllc01 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 6))
if mibBuilder.loadTexts: snaqllc01.setLastUpdated('9411090000Z')
if mibBuilder.loadTexts: snaqllc01.setOrganization('Cisco Systems, Inc.')
qllc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 6, 1))
class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class X121Address(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 17)

qllcLSAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1), )
if mibBuilder.loadTexts: qllcLSAdminTable.setStatus('current')
qllcLSAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1), ).setIndexNames((0, "CISCO-QLLC01-MIB", "qllcLSAdminIfIndex"), (0, "CISCO-QLLC01-MIB", "qllcLSAdminLciVcIndex"))
if mibBuilder.loadTexts: qllcLSAdminEntry.setStatus('current')
qllcLSAdminIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 1), IfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminIfIndex.setStatus('current')
qllcLSAdminLciVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 2), IfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminLciVcIndex.setStatus('current')
qllcLSAdminCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchedVC", 1), ("permanentVC", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminCircuitType.setStatus('current')
qllcLSAdminRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("peerToPeer", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminRole.setStatus('current')
qllcLSAdminX25Add = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 5), X121Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminX25Add.setStatus('current')
qllcLSAdminModulo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2))).clone('modulo8')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminModulo.setStatus('current')
qllcLSAdminLgX25 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qllcLSAdminLgX25.setStatus('current')
qllcLSOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2), )
if mibBuilder.loadTexts: qllcLSOperTable.setStatus('current')
qllcLSOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1), ).setIndexNames((0, "CISCO-QLLC01-MIB", "qllcLSOperIfIndex"), (0, "CISCO-QLLC01-MIB", "qllcLSOperLciVcIndex"))
if mibBuilder.loadTexts: qllcLSOperEntry.setStatus('current')
qllcLSOperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperIfIndex.setStatus('current')
qllcLSOperLciVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 2), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperLciVcIndex.setStatus('current')
qllcLSOperCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchedVC", 1), ("permanentVC", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperCircuitType.setStatus('current')
qllcLSOperRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("peerToPeer", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperRole.setStatus('current')
qllcLSOperX25Add = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 5), X121Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperX25Add.setStatus('current')
qllcLSOperModulo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2))).clone('modulo8')).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperModulo.setStatus('current')
qllcLSOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("lsStateInop", 1), ("lsStateClosed", 2), ("lsStateOpening", 3), ("lsStateClosing", 4), ("lsStateRecovery", 5), ("lsStateOpened", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperState.setStatus('current')
qllcLSOperLgX25 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSOperLgX25.setStatus('current')
qllcLSStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3), )
if mibBuilder.loadTexts: qllcLSStatsTable.setStatus('current')
qllcLSStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1), ).setIndexNames((0, "CISCO-QLLC01-MIB", "qllcLSStatsIfIndex"), (0, "CISCO-QLLC01-MIB", "qllcLSStatsLciVcIndex"))
if mibBuilder.loadTexts: qllcLSStatsEntry.setStatus('current')
qllcLSStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsIfIndex.setStatus('current')
qllcLSStatsLciVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 2), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsLciVcIndex.setStatus('current')
qllcLSStatsXidIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsXidIn.setStatus('current')
qllcLSStatsXidOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsXidOut.setStatus('current')
qllcLSStatsTestIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsTestIn.setStatus('current')
qllcLSStatsTestOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsTestOut.setStatus('current')
qllcLSStatsQuenchOff = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsQuenchOff.setStatus('current')
qllcLSStatsQuenchOn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsQuenchOn.setStatus('current')
qllcLSStatsInPaks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsInPaks.setStatus('current')
qllcLSStatsOutPaks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsOutPaks.setStatus('current')
qllcLSStatsInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsInBytes.setStatus('current')
qllcLSStatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsOutBytes.setStatus('current')
qllcLSStatsNumRcvQsms = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumRcvQsms.setStatus('current')
qllcLSStatsNumSndQsms = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumSndQsms.setStatus('current')
qllcLSStatsNumRcvDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumRcvDiscs.setStatus('current')
qllcLSStatsNumSndDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumSndDiscs.setStatus('current')
qllcLSStatsNumRcvDms = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumRcvDms.setStatus('current')
qllcLSStatsNumSndDms = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumSndDms.setStatus('current')
qllcLSStatsNumRcvFrmrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumRcvFrmrs.setStatus('current')
qllcLSStatsNumSndFrmrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumSndFrmrs.setStatus('current')
qllcLSStatsNumDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumDrops.setStatus('current')
qllcLSStatsNumErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qllcLSStatsNumErrs.setStatus('current')
qllcMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 6, 2))
qllcMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 1))
qllcMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2))
qllcMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 1, 1)).setObjects(("CISCO-QLLC01-MIB", "qllcLSAdminGroup"), ("CISCO-QLLC01-MIB", "qllcLSOperGroup"), ("CISCO-QLLC01-MIB", "qllcLSStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qllcMibCompliance = qllcMibCompliance.setStatus('current')
qllcLSAdminGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 1)).setObjects(("CISCO-QLLC01-MIB", "qllcLSAdminIfIndex"), ("CISCO-QLLC01-MIB", "qllcLSAdminLciVcIndex"), ("CISCO-QLLC01-MIB", "qllcLSAdminRole"), ("CISCO-QLLC01-MIB", "qllcLSAdminCircuitType"), ("CISCO-QLLC01-MIB", "qllcLSAdminX25Add"), ("CISCO-QLLC01-MIB", "qllcLSAdminModulo"), ("CISCO-QLLC01-MIB", "qllcLSAdminLgX25"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qllcLSAdminGroup = qllcLSAdminGroup.setStatus('current')
qllcLSOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 2)).setObjects(("CISCO-QLLC01-MIB", "qllcLSOperIfIndex"), ("CISCO-QLLC01-MIB", "qllcLSOperLciVcIndex"), ("CISCO-QLLC01-MIB", "qllcLSOperCircuitType"), ("CISCO-QLLC01-MIB", "qllcLSOperRole"), ("CISCO-QLLC01-MIB", "qllcLSOperX25Add"), ("CISCO-QLLC01-MIB", "qllcLSOperModulo"), ("CISCO-QLLC01-MIB", "qllcLSOperState"), ("CISCO-QLLC01-MIB", "qllcLSOperLgX25"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qllcLSOperGroup = qllcLSOperGroup.setStatus('current')
qllcLSStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 3)).setObjects(("CISCO-QLLC01-MIB", "qllcLSStatsIfIndex"), ("CISCO-QLLC01-MIB", "qllcLSStatsLciVcIndex"), ("CISCO-QLLC01-MIB", "qllcLSStatsXidIn"), ("CISCO-QLLC01-MIB", "qllcLSStatsXidOut"), ("CISCO-QLLC01-MIB", "qllcLSStatsTestIn"), ("CISCO-QLLC01-MIB", "qllcLSStatsTestOut"), ("CISCO-QLLC01-MIB", "qllcLSStatsQuenchOff"), ("CISCO-QLLC01-MIB", "qllcLSStatsQuenchOn"), ("CISCO-QLLC01-MIB", "qllcLSStatsInPaks"), ("CISCO-QLLC01-MIB", "qllcLSStatsOutPaks"), ("CISCO-QLLC01-MIB", "qllcLSStatsInBytes"), ("CISCO-QLLC01-MIB", "qllcLSStatsOutBytes"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvQsms"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndQsms"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvDiscs"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndDiscs"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvDms"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndDms"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvFrmrs"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndFrmrs"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumDrops"), ("CISCO-QLLC01-MIB", "qllcLSStatsNumErrs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qllcLSStatsGroup = qllcLSStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QLLC01-MIB", qllcLSAdminModulo=qllcLSAdminModulo, qllcLSOperX25Add=qllcLSOperX25Add, qllcLSStatsQuenchOff=qllcLSStatsQuenchOff, qllcLSStatsNumRcvDiscs=qllcLSStatsNumRcvDiscs, qllcLSOperLgX25=qllcLSOperLgX25, qllcLSAdminX25Add=qllcLSAdminX25Add, qllcLSOperRole=qllcLSOperRole, qllcLSStatsEntry=qllcLSStatsEntry, qllcLSStatsNumSndQsms=qllcLSStatsNumSndQsms, qllcMibGroups=qllcMibGroups, qllcLSStatsGroup=qllcLSStatsGroup, qllcLSStatsTestOut=qllcLSStatsTestOut, qllcLSStatsIfIndex=qllcLSStatsIfIndex, qllcMibCompliances=qllcMibCompliances, qllcLSStatsNumErrs=qllcLSStatsNumErrs, qllcLSStatsNumDrops=qllcLSStatsNumDrops, qllcLSOperState=qllcLSOperState, qllcLSAdminIfIndex=qllcLSAdminIfIndex, qllcLSOperTable=qllcLSOperTable, qllcLSOperCircuitType=qllcLSOperCircuitType, qllcLSStatsLciVcIndex=qllcLSStatsLciVcIndex, PYSNMP_MODULE_ID=snaqllc01, qllcLSOperIfIndex=qllcLSOperIfIndex, X121Address=X121Address, qllcLSAdminRole=qllcLSAdminRole, qllcLSAdminLciVcIndex=qllcLSAdminLciVcIndex, qllcLSAdminTable=qllcLSAdminTable, qllcLSStatsInPaks=qllcLSStatsInPaks, qllcLSStatsOutPaks=qllcLSStatsOutPaks, qllcLSAdminLgX25=qllcLSAdminLgX25, IfIndexType=IfIndexType, qllcLSOperEntry=qllcLSOperEntry, qllcLSOperModulo=qllcLSOperModulo, qllc=qllc, qllcLSStatsQuenchOn=qllcLSStatsQuenchOn, qllcLSOperGroup=qllcLSOperGroup, qllcLSStatsTestIn=qllcLSStatsTestIn, qllcLSStatsNumRcvFrmrs=qllcLSStatsNumRcvFrmrs, qllcMibCompliance=qllcMibCompliance, qllcLSStatsNumRcvDms=qllcLSStatsNumRcvDms, qllcLSAdminCircuitType=qllcLSAdminCircuitType, snaqllc01=snaqllc01, qllcLSStatsTable=qllcLSStatsTable, qllcLSStatsNumSndDms=qllcLSStatsNumSndDms, qllcLSAdminGroup=qllcLSAdminGroup, qllcLSAdminEntry=qllcLSAdminEntry, qllcLSStatsXidIn=qllcLSStatsXidIn, qllcMibConformance=qllcMibConformance, qllcLSStatsXidOut=qllcLSStatsXidOut, qllcLSStatsOutBytes=qllcLSStatsOutBytes, qllcLSOperLciVcIndex=qllcLSOperLciVcIndex, qllcLSStatsInBytes=qllcLSStatsInBytes, qllcLSStatsNumSndDiscs=qllcLSStatsNumSndDiscs, qllcLSStatsNumSndFrmrs=qllcLSStatsNumSndFrmrs, qllcLSStatsNumRcvQsms=qllcLSStatsNumRcvQsms)
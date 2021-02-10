#
# PySNMP MIB module CISCO-ATM-TRUNK-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-TRUNK-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
AtmVcIdentifier, AtmVpIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, MibIdentifier, ObjectIdentity, Bits, NotificationType, Counter64, ModuleIdentity, Counter32, iso, IpAddress, Integer32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType", "Counter64", "ModuleIdentity", "Counter32", "iso", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention", "TruthValue")
ciscoAtmTrunkStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 407))
ciscoAtmTrunkStatMIB.setRevisions(('2005-08-10 00:00', '2004-05-12 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrunkStatMIB.setLastUpdated('200508100000Z')
if mibBuilder.loadTexts: ciscoAtmTrunkStatMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmTrunkStatNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 0))
ciscoAtmTrunkStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 1))
catsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1))
catsPvcHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1), )
if mibBuilder.loadTexts: catsPvcHistoryTable.setStatus('current')
catsPvcHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcVpi"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcVci"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcIntervalIndex"))
if mibBuilder.loadTexts: catsPvcHistoryEntry.setStatus('current')
catsPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 1), AtmVpIdentifier())
if mibBuilder.loadTexts: catsPvcVpi.setStatus('current')
catsPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 2), AtmVcIdentifier())
if mibBuilder.loadTexts: catsPvcVci.setStatus('current')
catsPvcIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: catsPvcIntervalIndex.setStatus('current')
catsPvcValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcValidFlag.setStatus('current')
catsPvcDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcDiscontinuityTime.setStatus('current')
catsPvcAtmXmtCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcAtmXmtCells.setStatus('current')
catsPvcAtmRcvCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcAtmRcvCells.setStatus('current')
catsPvcAvgAtmXmtCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 8), Counter32()).setUnits('cells-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcAvgAtmXmtCells.setStatus('current')
catsPvcAvgAtmRcvCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 9), Counter32()).setUnits('cells-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcAvgAtmRcvCells.setStatus('current')
catsPvcPeakAtmXmtCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 10), Counter32()).setUnits('cells-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcPeakAtmXmtCells.setStatus('current')
catsPvcPeakAtmRcvCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 11), Counter32()).setUnits('cells-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcPeakAtmRcvCells.setStatus('current')
catsPvcOamXmtEndLpbkCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamXmtEndLpbkCells.setStatus('current')
catsPvcOamRcvEndLpbkCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamRcvEndLpbkCells.setStatus('current')
catsPvcOamXmtSegLpbkCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamXmtSegLpbkCells.setStatus('current')
catsPvcOamRcvSegLpbkCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamRcvSegLpbkCells.setStatus('current')
catsPvcOamLpbkLostCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamLpbkLostCells.setStatus('current')
catsPvcDiscardedRcvOamCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcDiscardedRcvOamCells.setStatus('current')
catsPvcAisSuppressCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcAisSuppressCnts.setStatus('current')
catsPvcXmtAisCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcXmtAisCnts.setStatus('current')
catsPvcRcvAisCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcRcvAisCnts.setStatus('current')
catsPvcXmtFerfCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcXmtFerfCnts.setStatus('current')
catsPvcRcvFerfCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcRcvFerfCnts.setStatus('current')
catsPvcXmtAisCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcXmtAisCells.setStatus('current')
catsPvcRcvAisCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcRcvAisCells.setStatus('current')
catsPvcXmtFerfCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcXmtFerfCells.setStatus('current')
catsPvcRcvFerfCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcRcvFerfCells.setStatus('current')
catsPvcOamLpbkTimeoutCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamLpbkTimeoutCnts.setStatus('current')
catsPvcNewOamLpbkTimeoutDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 28), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcNewOamLpbkTimeoutDur.setStatus('current')
catsPvcActiveOamLpbkTimeoutDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 29), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcActiveOamLpbkTimeoutDur.setStatus('current')
catsPvcOamLpbkTimeoutThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 30), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsPvcOamLpbkTimeoutThreshold.setStatus('current')
catsAal2PvcHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2), )
if mibBuilder.loadTexts: catsAal2PvcHistoryTable.setStatus('current')
catsAal2PvcHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcVpi"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcVci"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcIntervalIndex"))
if mibBuilder.loadTexts: catsAal2PvcHistoryEntry.setStatus('current')
catsAal2PvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 1), AtmVpIdentifier())
if mibBuilder.loadTexts: catsAal2PvcVpi.setStatus('current')
catsAal2PvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 2), AtmVcIdentifier())
if mibBuilder.loadTexts: catsAal2PvcVci.setStatus('current')
catsAal2PvcIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: catsAal2PvcIntervalIndex.setStatus('current')
catsAal2PvcValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcValidFlag.setStatus('current')
catsAal2PvcDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcDiscontinuityTime.setStatus('current')
catsAal2PvcCpsSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCpsSentPkts.setStatus('current')
catsAal2PvcCpsRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCpsRcvdPkts.setStatus('current')
catsAal2PvcHecErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcHecErrors.setStatus('current')
catsAal2PvcCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCrcErrors.setStatus('current')
catsAal2PvcInvOsfCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcInvOsfCells.setStatus('current')
catsAal2PvcInvParCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcInvParCells.setStatus('current')
catsAal2PvcCpsInvCidPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCpsInvCidPkts.setStatus('current')
catsAal2PvcCpsInvUuiPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCpsInvUuiPkts.setStatus('current')
catsAal2PvcCpsInvLenPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal2PvcCpsInvLenPkts.setStatus('current')
catsAal5PvcHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3), )
if mibBuilder.loadTexts: catsAal5PvcHistoryTable.setStatus('current')
catsAal5PvcHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcVpi"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcVci"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcIntervalIndex"))
if mibBuilder.loadTexts: catsAal5PvcHistoryEntry.setStatus('current')
catsAal5PvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 1), AtmVpIdentifier())
if mibBuilder.loadTexts: catsAal5PvcVpi.setStatus('current')
catsAal5PvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 2), AtmVcIdentifier())
if mibBuilder.loadTexts: catsAal5PvcVci.setStatus('current')
catsAal5PvcIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: catsAal5PvcIntervalIndex.setStatus('current')
catsAal5PvcValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcValidFlag.setStatus('current')
catsAal5PvcDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcDiscontinuityTime.setStatus('current')
catsAal5PvcPduSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcPduSentPkts.setStatus('current')
catsAal5PvcPduRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcPduRcvdPkts.setStatus('current')
catsAal5PvcInvCpiPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcInvCpiPdus.setStatus('current')
catsAal5PvcOverSizedSDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcOverSizedSDUs.setStatus('current')
catsAal5PvcInvLenPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcInvLenPdus.setStatus('current')
catsAal5PvcCrc32ErrorPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcCrc32ErrorPdus.setStatus('current')
catsAal5PvcReassemTimerExpiryPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsAal5PvcReassemTimerExpiryPdus.setStatus('current')
catsCidHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4), )
if mibBuilder.loadTexts: catsCidHistoryTable.setStatus('current')
catsCidHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidVpi"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidVci"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCid"), (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidIntervalIndex"))
if mibBuilder.loadTexts: catsCidHistoryEntry.setStatus('current')
catsCidVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 1), AtmVpIdentifier())
if mibBuilder.loadTexts: catsCidVpi.setStatus('current')
catsCidVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 2), AtmVcIdentifier())
if mibBuilder.loadTexts: catsCidVci.setStatus('current')
catsCid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: catsCid.setStatus('current')
catsCidIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: catsCidIntervalIndex.setStatus('current')
catsCidValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidValidFlag.setStatus('current')
catsCidDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidDiscontinuityTime.setStatus('current')
catsCidAvgSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 7), Counter32()).setUnits('packets-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidAvgSentPkts.setStatus('current')
catsCidAvgRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 8), Counter32()).setUnits('packets-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidAvgRcvdPkts.setStatus('current')
catsCidSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidSentPkts.setStatus('current')
catsCidRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidRcvdPkts.setStatus('current')
catsCidSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidSentOctets.setStatus('current')
catsCidRcvdOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidRcvdOctets.setStatus('current')
catsCidSentPeakPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 13), Counter32()).setUnits('packets-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidSentPeakPkts.setStatus('current')
catsCidRcvdPeakPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 14), Counter32()).setUnits('packets-per-sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidRcvdPeakPkts.setStatus('current')
catsCidExtAISRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtAISRcvdPkts.setStatus('current')
catsCidExtRAIRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtRAIRcvdPkts.setStatus('current')
catsCidExtConnAISRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtConnAISRcvdPkts.setStatus('current')
catsCidExtConnRDIRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtConnRDIRcvdPkts.setStatus('current')
catsCidExtAISRcvCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtAISRcvCnts.setStatus('current')
catsCidExtRAIRcvCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtRAIRcvCnts.setStatus('current')
catsCidExtConnAISCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtConnAISCnts.setStatus('current')
catsCidExtConnRDICnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtConnRDICnts.setStatus('current')
catsCidExtAISXmtCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtAISXmtCnts.setStatus('current')
catsCidExtRAIXmtCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: catsCidExtRAIXmtCnts.setStatus('current')
catsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 2))
catsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1))
catsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2))
ciscoAtmPvcStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2, 1)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcStatGroup"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcStatGroup"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcStatGroup"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidHistoryStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmPvcStatMIBCompliance = ciscoAtmPvcStatMIBCompliance.setStatus('deprecated')
ciscoAtmPvcStatMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2, 2)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcStatGroupRev1"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcStatGroup"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcStatGroup"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidHistoryStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmPvcStatMIBComplianceRev1 = ciscoAtmPvcStatMIBComplianceRev1.setStatus('current')
catsPvcStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 1)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcValidFlag"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscontinuityTime"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtEndLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvEndLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtSegLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvSegLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkLostCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscardedRcvOamCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAisSuppressCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    catsPvcStatGroup = catsPvcStatGroup.setStatus('deprecated')
catsAal2PvcStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 2)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcValidFlag"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcDiscontinuityTime"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsSentPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcHecErrors"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCrcErrors"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcInvOsfCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcInvParCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvCidPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvUuiPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvLenPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    catsAal2PvcStatGroup = catsAal2PvcStatGroup.setStatus('current')
catsAal5PvcStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 3)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcValidFlag"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcDiscontinuityTime"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcPduSentPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcPduRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcInvCpiPdus"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcOverSizedSDUs"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcInvLenPdus"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcCrc32ErrorPdus"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcReassemTimerExpiryPdus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    catsAal5PvcStatGroup = catsAal5PvcStatGroup.setStatus('current')
catsCidHistoryStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 4)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsCidValidFlag"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidDiscontinuityTime"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidAvgSentPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidAvgRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentOctets"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdOctets"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentPeakPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdPeakPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnAISRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnRDIRcvdPkts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISRcvCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIRcvCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnAISCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnRDICnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISXmtCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIXmtCnts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    catsCidHistoryStatGroup = catsCidHistoryStatGroup.setStatus('current')
catsPvcStatGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 5)).setObjects(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcValidFlag"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscontinuityTime"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmXmtCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmRcvCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtEndLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvEndLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtSegLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvSegLpbkCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkLostCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscardedRcvOamCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAisSuppressCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCells"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkTimeoutCnts"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcNewOamLpbkTimeoutDur"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcActiveOamLpbkTimeoutDur"), ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkTimeoutThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    catsPvcStatGroupRev1 = catsPvcStatGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRUNK-STAT-MIB", catsAal2PvcCpsInvCidPkts=catsAal2PvcCpsInvCidPkts, catsAal2PvcCpsSentPkts=catsAal2PvcCpsSentPkts, catsPvcOamXmtEndLpbkCells=catsPvcOamXmtEndLpbkCells, catsAal5PvcStatGroup=catsAal5PvcStatGroup, catsCidExtConnAISRcvdPkts=catsCidExtConnAISRcvdPkts, catsPvcOamLpbkTimeoutCnts=catsPvcOamLpbkTimeoutCnts, catsCidExtRAIRcvCnts=catsCidExtRAIRcvCnts, ciscoAtmTrunkStatNotifs=ciscoAtmTrunkStatNotifs, catsPvcXmtAisCells=catsPvcXmtAisCells, catsPvcOamLpbkTimeoutThreshold=catsPvcOamLpbkTimeoutThreshold, catsPvcOamLpbkLostCells=catsPvcOamLpbkLostCells, catsAal2PvcVci=catsAal2PvcVci, catsCidExtRAIRcvdPkts=catsCidExtRAIRcvdPkts, ciscoAtmPvcStatMIBCompliance=ciscoAtmPvcStatMIBCompliance, PYSNMP_MODULE_ID=ciscoAtmTrunkStatMIB, catsPvcOamXmtSegLpbkCells=catsPvcOamXmtSegLpbkCells, catsPvcXmtAisCnts=catsPvcXmtAisCnts, catsPvcNewOamLpbkTimeoutDur=catsPvcNewOamLpbkTimeoutDur, catsPvcOamRcvSegLpbkCells=catsPvcOamRcvSegLpbkCells, catsAal2PvcValidFlag=catsAal2PvcValidFlag, catsCidExtRAIXmtCnts=catsCidExtRAIXmtCnts, catsPvcPeakAtmRcvCells=catsPvcPeakAtmRcvCells, ciscoAtmPvcStatMIBComplianceRev1=ciscoAtmPvcStatMIBComplianceRev1, catsMIBConformance=catsMIBConformance, catsCidIntervalIndex=catsCidIntervalIndex, catsAal5PvcPduRcvdPkts=catsAal5PvcPduRcvdPkts, catsCidSentOctets=catsCidSentOctets, catsAal2PvcInvOsfCells=catsAal2PvcInvOsfCells, ciscoAtmTrunkStatObjects=ciscoAtmTrunkStatObjects, catsAal5PvcHistoryTable=catsAal5PvcHistoryTable, catsAal5PvcHistoryEntry=catsAal5PvcHistoryEntry, catsCidExtConnRDICnts=catsCidExtConnRDICnts, catsCidDiscontinuityTime=catsCidDiscontinuityTime, catsPvcAvgAtmRcvCells=catsPvcAvgAtmRcvCells, catsCidAvgRcvdPkts=catsCidAvgRcvdPkts, catsPvcXmtFerfCells=catsPvcXmtFerfCells, catsPvcRcvAisCells=catsPvcRcvAisCells, catsPvcDiscardedRcvOamCells=catsPvcDiscardedRcvOamCells, catsPvcPeakAtmXmtCells=catsPvcPeakAtmXmtCells, catsCid=catsCid, catsCidExtConnAISCnts=catsCidExtConnAISCnts, catsPvcStatGroupRev1=catsPvcStatGroupRev1, catsAal2PvcCpsInvUuiPkts=catsAal2PvcCpsInvUuiPkts, catsPvcHistoryTable=catsPvcHistoryTable, catsAal2PvcCpsRcvdPkts=catsAal2PvcCpsRcvdPkts, catsPvcAtmRcvCells=catsPvcAtmRcvCells, catsPvcRcvAisCnts=catsPvcRcvAisCnts, catsPvcRcvFerfCnts=catsPvcRcvFerfCnts, catsAal2PvcHistoryEntry=catsAal2PvcHistoryEntry, catsAal5PvcInvLenPdus=catsAal5PvcInvLenPdus, catsPvcRcvFerfCells=catsPvcRcvFerfCells, catsPvcAisSuppressCnts=catsPvcAisSuppressCnts, catsCidVpi=catsCidVpi, catsAal2PvcHecErrors=catsAal2PvcHecErrors, catsCidExtAISXmtCnts=catsCidExtAISXmtCnts, catsAal2PvcVpi=catsAal2PvcVpi, catsAal2PvcCrcErrors=catsAal2PvcCrcErrors, catsCidRcvdPeakPkts=catsCidRcvdPeakPkts, catsAal5PvcPduSentPkts=catsAal5PvcPduSentPkts, catsAal2PvcHistoryTable=catsAal2PvcHistoryTable, catsAal5PvcIntervalIndex=catsAal5PvcIntervalIndex, ciscoAtmTrunkStatMIB=ciscoAtmTrunkStatMIB, catsCidSentPkts=catsCidSentPkts, catsCidHistoryStatGroup=catsCidHistoryStatGroup, catsCidExtAISRcvdPkts=catsCidExtAISRcvdPkts, catsPvcIntervalIndex=catsPvcIntervalIndex, catsPvcStatGroup=catsPvcStatGroup, catsAal5PvcOverSizedSDUs=catsAal5PvcOverSizedSDUs, catsAal2PvcStatGroup=catsAal2PvcStatGroup, catsAal5PvcReassemTimerExpiryPdus=catsAal5PvcReassemTimerExpiryPdus, catsPvcAtmXmtCells=catsPvcAtmXmtCells, catsAal2PvcCpsInvLenPkts=catsAal2PvcCpsInvLenPkts, catsCidSentPeakPkts=catsCidSentPeakPkts, catsPvcActiveOamLpbkTimeoutDur=catsPvcActiveOamLpbkTimeoutDur, catsAal5PvcInvCpiPdus=catsAal5PvcInvCpiPdus, catsCidExtConnRDIRcvdPkts=catsCidExtConnRDIRcvdPkts, catsPvcOamRcvEndLpbkCells=catsPvcOamRcvEndLpbkCells, catsAal2PvcIntervalIndex=catsAal2PvcIntervalIndex, catsPvcXmtFerfCnts=catsPvcXmtFerfCnts, catsAal2PvcInvParCells=catsAal2PvcInvParCells, catsAal5PvcVpi=catsAal5PvcVpi, catsPvcValidFlag=catsPvcValidFlag, catsCidHistoryTable=catsCidHistoryTable, catsAal5PvcCrc32ErrorPdus=catsAal5PvcCrc32ErrorPdus, catsMIBGroups=catsMIBGroups, catsCidValidFlag=catsCidValidFlag, catsAal2PvcDiscontinuityTime=catsAal2PvcDiscontinuityTime, catsPvcVpi=catsPvcVpi, catsCidRcvdOctets=catsCidRcvdOctets, catsAal5PvcVci=catsAal5PvcVci, catsStatistics=catsStatistics, catsPvcVci=catsPvcVci, catsCidExtAISRcvCnts=catsCidExtAISRcvCnts, catsCidVci=catsCidVci, catsAal5PvcDiscontinuityTime=catsAal5PvcDiscontinuityTime, catsCidRcvdPkts=catsCidRcvdPkts, catsPvcDiscontinuityTime=catsPvcDiscontinuityTime, catsCidHistoryEntry=catsCidHistoryEntry, catsPvcAvgAtmXmtCells=catsPvcAvgAtmXmtCells, catsMIBCompliances=catsMIBCompliances, catsPvcHistoryEntry=catsPvcHistoryEntry, catsAal5PvcValidFlag=catsAal5PvcValidFlag, catsCidAvgSentPkts=catsCidAvgSentPkts)
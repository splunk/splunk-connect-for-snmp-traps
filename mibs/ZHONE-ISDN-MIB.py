#
# PySNMP MIB module ZHONE-ISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-ISDN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PerfTotalCount, PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfIntervalCount", "PerfCurrentCount")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, ModuleIdentity, Counter32, Gauge32, IpAddress, Bits, MibIdentifier, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress", "Bits", "MibIdentifier", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhonePhysical, zhoneTrapModules = mibBuilder.importSymbols("Zhone", "zhonePhysical", "zhoneTrapModules")
zhoneIsdn = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 5, 7))
zhoneIsdn.setRevisions(('2003-03-03 11:58', '2003-02-04 18:04', '2000-09-27 10:57', '2000-09-27 19:42',))
if mibBuilder.loadTexts: zhoneIsdn.setLastUpdated('200303031944Z')
if mibBuilder.loadTexts: zhoneIsdn.setOrganization('Zhone Technologies.')
zhoneIsdnTrap = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3))
if mibBuilder.loadTexts: zhoneIsdnTrap.setStatus('current')
isdnMibV2Traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1))
if mibBuilder.loadTexts: isdnMibV2Traps.setStatus('current')
isdnTrapFrameSynchLoss = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnTrapFrameSynchLoss.setStatus('current')
isdnTrapFECV = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnTrapFECV.setStatus('current')
isdnTrapAmiViolations = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnTrapAmiViolations.setStatus('current')
isdnTrapUnbalancedFrame = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 4))
if mibBuilder.loadTexts: isdnTrapUnbalancedFrame.setStatus('current')
zhoneIsdnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1))
isdnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1), )
if mibBuilder.loadTexts: isdnConfigTable.setStatus('current')
isdnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnConfigEntry.setStatus('current')
isdnLineTermClass = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("class1", 1), ("class2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnLineTermClass.setStatus('current')
isdnActivationTimer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t2-50ms", 1), ("t2-100ms", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnActivationTimer2.setStatus('current')
isdnLineLoopBack = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("loop-back-none", 1), ("loop-back-b1-st-tr", 2), ("loop-back-b1-st-nt", 3), ("loop-back-b2-st-tr", 4), ("loop-back-b2-st-nt", 5), ("loop-back-b1-idl2-tr", 6), ("loop-back-b1-idl2-nt", 7), ("loop-back-b2-idl2-tr", 8), ("loop-back-b2-idl2-nt", 9), ("loop-back-2bd-idl2-tr", 10), ("loop-back-2bd-idl2-nt", 11), ("loop-back-2bd-u-interface-tr", 12), ("loop-back-2bd-u-interface-nt", 13), ("loop-back-2bd-external-analog", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnLineLoopBack.setStatus('current')
isdnLinePower = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("sealing", 2), ("powering", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnLinePower.setStatus('current')
isdnPerfDataCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2), )
if mibBuilder.loadTexts: isdnPerfDataCurrentTable.setStatus('current')
isdnPerfDataCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1), )
isdnConfigEntry.registerAugmentions(("ZHONE-ISDN-MIB", "isdnPerfDataCurrentEntry"))
isdnPerfDataCurrentEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: isdnPerfDataCurrentEntry.setStatus('current')
isdnPerfCurBadAmiViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfCurBadAmiViolation.setStatus('current')
isdnPerfCurUnbalancedFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfCurUnbalancedFrame.setStatus('current')
isdnPerCurErrorSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 3), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerCurErrorSeconds.setStatus('current')
isdnPerCurFsyncSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 4), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerCurFsyncSeconds.setStatus('current')
isdnPerfCurTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfCurTimeElapsed.setStatus('current')
isdnPerfDataPreviousTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3), )
if mibBuilder.loadTexts: isdnPerfDataPreviousTable.setStatus('current')
isdnPerfDataPreviousEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1), )
isdnConfigEntry.registerAugmentions(("ZHONE-ISDN-MIB", "isdnPerfDataPreviousEntry"))
isdnPerfDataPreviousEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: isdnPerfDataPreviousEntry.setStatus('current')
isdnPerfPrevBadAmiViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfPrevBadAmiViolation.setStatus('current')
isdnPerfPrevUnbalancedFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfPrevUnbalancedFrame.setStatus('current')
isdnPerPrevFsyncSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 3), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerPrevFsyncSeconds.setStatus('current')
isdnPerfPrevErrorSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 4), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfPrevErrorSeconds.setStatus('current')
isdnPerfDataTotalTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4), )
if mibBuilder.loadTexts: isdnPerfDataTotalTable.setStatus('current')
isdnPerfDataTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1), )
isdnConfigEntry.registerAugmentions(("ZHONE-ISDN-MIB", "isdnPerfDataTotalEntry"))
isdnPerfDataTotalEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: isdnPerfDataTotalEntry.setStatus('current')
isdnPerfTotalBadAmiViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 1), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfTotalBadAmiViolation.setStatus('current')
isdnPerfTotalUnbalancedFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfTotalUnbalancedFrame.setStatus('current')
isdnPerTotalFsyncSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 3), PerfTotalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerTotalFsyncSeconds.setStatus('current')
isdnPerfTotalErrorSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 4), PerfTotalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfTotalErrorSeconds.setStatus('current')
isdnPerfTotalTimePeriodsElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnPerfTotalTimePeriodsElapsed.setStatus('current')
isdnAlarmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5), )
if mibBuilder.loadTexts: isdnAlarmProfileTable.setStatus('current')
isdnAlarmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1), )
isdnConfigEntry.registerAugmentions(("ZHONE-ISDN-MIB", "isdnAlarmProfileEntry"))
isdnAlarmProfileEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: isdnAlarmProfileEntry.setStatus('current')
isdnThresholdAmiViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnThresholdAmiViolations.setStatus('current')
isdnThresholdUnbalancedFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnThresholdUnbalancedFrame.setStatus('current')
mibBuilder.exportSymbols("ZHONE-ISDN-MIB", isdnPerfTotalTimePeriodsElapsed=isdnPerfTotalTimePeriodsElapsed, isdnConfigTable=isdnConfigTable, isdnPerCurErrorSeconds=isdnPerCurErrorSeconds, isdnPerfDataPreviousEntry=isdnPerfDataPreviousEntry, isdnPerfCurTimeElapsed=isdnPerfCurTimeElapsed, isdnPerTotalFsyncSeconds=isdnPerTotalFsyncSeconds, isdnActivationTimer2=isdnActivationTimer2, isdnThresholdUnbalancedFrame=isdnThresholdUnbalancedFrame, isdnLineTermClass=isdnLineTermClass, isdnTrapUnbalancedFrame=isdnTrapUnbalancedFrame, isdnLineLoopBack=isdnLineLoopBack, isdnAlarmProfileTable=isdnAlarmProfileTable, zhoneIsdnMib=zhoneIsdnMib, isdnLinePower=isdnLinePower, isdnPerfPrevUnbalancedFrame=isdnPerfPrevUnbalancedFrame, isdnPerfDataTotalEntry=isdnPerfDataTotalEntry, PYSNMP_MODULE_ID=zhoneIsdn, isdnAlarmProfileEntry=isdnAlarmProfileEntry, isdnPerfPrevErrorSeconds=isdnPerfPrevErrorSeconds, isdnPerfCurUnbalancedFrame=isdnPerfCurUnbalancedFrame, isdnPerfTotalBadAmiViolation=isdnPerfTotalBadAmiViolation, isdnPerfCurBadAmiViolation=isdnPerfCurBadAmiViolation, isdnTrapFECV=isdnTrapFECV, isdnPerPrevFsyncSeconds=isdnPerPrevFsyncSeconds, isdnThresholdAmiViolations=isdnThresholdAmiViolations, isdnConfigEntry=isdnConfigEntry, isdnPerfTotalUnbalancedFrame=isdnPerfTotalUnbalancedFrame, isdnMibV2Traps=isdnMibV2Traps, isdnPerfDataCurrentTable=isdnPerfDataCurrentTable, isdnPerfDataCurrentEntry=isdnPerfDataCurrentEntry, isdnPerfTotalErrorSeconds=isdnPerfTotalErrorSeconds, isdnPerCurFsyncSeconds=isdnPerCurFsyncSeconds, isdnPerfDataPreviousTable=isdnPerfDataPreviousTable, isdnPerfPrevBadAmiViolation=isdnPerfPrevBadAmiViolation, zhoneIsdn=zhoneIsdn, isdnPerfDataTotalTable=isdnPerfDataTotalTable, isdnTrapFrameSynchLoss=isdnTrapFrameSynchLoss, isdnTrapAmiViolations=isdnTrapAmiViolations, zhoneIsdnTrap=zhoneIsdnTrap)
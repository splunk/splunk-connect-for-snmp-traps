#
# PySNMP MIB module XYLAN-ATM-CE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-ATM-CE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, NotificationType, iso, Counter32, Integer32, ObjectIdentity, Unsigned32, TimeTicks, Gauge32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "NotificationType", "iso", "Counter32", "Integer32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Gauge32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanAtmArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanAtmArch")
atmxCesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10))
atmxCesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1))
atmxCesMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2))
atmxCesService = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1))
atmxCesVccGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2))
atmxCesVccStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3))
atmxCesSvcConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4))
atmxCesServiceTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1), )
if mibBuilder.loadTexts: atmxCesServiceTable.setStatus('mandatory')
atmxCesServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1), ).setIndexNames((0, "XYLAN-ATM-CE-MIB", "atmxCesServiceSlotIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesServicePortIndex"))
if mibBuilder.loadTexts: atmxCesServiceEntry.setStatus('mandatory')
atmxCesServiceSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesServiceSlotIndex.setStatus('mandatory')
atmxCesServicePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesServicePortIndex.setStatus('mandatory')
atmxCesServiceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesServiceDescription.setStatus('mandatory')
atmxCesServiceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesServiceAdminStatus.setStatus('mandatory')
atmxCesServiceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesServiceOperStatus.setStatus('mandatory')
atmxCesServiceServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unstructured", 1), ("structured", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesServiceServiceMode.setStatus('mandatory')
atmxCesServiceServiceClock = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("synchronous", 1), ("srts", 2), ("adaptive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesServiceServiceClock.setStatus('mandatory')
atmxCesServiceAvailTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesServiceAvailTimeSlot.setStatus('mandatory')
atmxCesVccTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1), )
if mibBuilder.loadTexts: atmxCesVccTable.setStatus('mandatory')
atmxCesVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1), ).setIndexNames((0, "XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesVccVci"))
if mibBuilder.loadTexts: atmxCesVccEntry.setStatus('mandatory')
atmxCesVccSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccSlotIndex.setStatus('mandatory')
atmxCesVccPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccPortIndex.setStatus('mandatory')
atmxCesVccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccVpi.setStatus('mandatory')
atmxCesVccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccVci.setStatus('mandatory')
atmxCesVccAtmUplinkSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccAtmUplinkSlotIndex.setStatus('mandatory')
atmxCesVccAtmUplinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccAtmUplinkPortIndex.setStatus('mandatory')
atmxCesVccDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccDescription.setStatus('mandatory')
atmxCesVccAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccAdminStatus.setStatus('mandatory')
atmxCesVccOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccOperStatus.setStatus('mandatory')
atmxCesVccConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("pvc", 2), ("activeSvc", 3), ("passiveSvc", 4), ("initialSvc", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccConnType.setStatus('mandatory')
atmxCesVccPartialFill = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 47))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccPartialFill.setStatus('mandatory')
atmxCesVccBufMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccBufMaxSize.setStatus('mandatory')
atmxCesVccCDVT = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccCDVT.setStatus('mandatory')
atmxCesVccCellLossIntegrationPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccCellLossIntegrationPeriod.setStatus('mandatory')
atmxCesVccIdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccIdleCode.setStatus('mandatory')
atmxCesVccTimeSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccTimeSlots.setStatus('mandatory')
atmxCesVccAtmUplinkVccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccAtmUplinkVccVpi.setStatus('mandatory')
atmxCesVccAtmUplinkVccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccAtmUplinkVccVci.setStatus('mandatory')
atmxCesVccLocalAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesVccLocalAtmAddr.setStatus('mandatory')
atmxCesVccStatsTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1), )
if mibBuilder.loadTexts: atmxCesVccStatsTable.setStatus('mandatory')
atmxCesVccStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1), ).setIndexNames((0, "XYLAN-ATM-CE-MIB", "atmxCesVccStatsSlotIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesVccStatsPortIndex"), (0, "XYLAN-ATM-CE-MIB", "atmCesVccStatsVci"))
if mibBuilder.loadTexts: atmxCesVccStatsEntry.setStatus('mandatory')
atmxCesVccStatsSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsSlotIndex.setStatus('mandatory')
atmxCesVccStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsPortIndex.setStatus('mandatory')
atmCesVccStatsVci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCesVccStatsVci.setStatus('mandatory')
atmxCesVccStatsTxDataCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsTxDataCells.setStatus('mandatory')
atmxCesVccStatsTxCondCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsTxCondCells.setStatus('mandatory')
atmxCesVccStatsSuppressedTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsSuppressedTxCells.setStatus('mandatory')
atmxCesVccStatsRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsRxCells.setStatus('mandatory')
atmxCesVccStatsSnpErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsSnpErrors.setStatus('mandatory')
atmxCesVccStatsSeqNumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsSeqNumErrors.setStatus('mandatory')
atmxCesVccStatsDroppedRxCellUnderrun = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsDroppedRxCellUnderrun.setStatus('mandatory')
atmxCesVccStatsDroppedRxCellOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsDroppedRxCellOverrun.setStatus('mandatory')
atmxCesVccStatsCellLossStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noLoss", 1), ("loss", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccStatsCellLossStatus.setStatus('mandatory')
atmxCesVccRateTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2), )
if mibBuilder.loadTexts: atmxCesVccRateTable.setStatus('mandatory')
atmxCesVccRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1), ).setIndexNames((0, "XYLAN-ATM-CE-MIB", "atmxCesVccRateSlotIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesVccRatePortIndex"), (0, "XYLAN-ATM-CE-MIB", "atmCesVccRateVci"))
if mibBuilder.loadTexts: atmxCesVccRateEntry.setStatus('mandatory')
atmxCesVccRateSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateSlotIndex.setStatus('mandatory')
atmxCesVccRatePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRatePortIndex.setStatus('mandatory')
atmCesVccRateVci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCesVccRateVci.setStatus('mandatory')
atmxCesVccRateTxDataCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateTxDataCells.setStatus('mandatory')
atmxCesVccRateTxCondCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateTxCondCells.setStatus('mandatory')
atmxCesVccRateSuppressedTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateSuppressedTxCells.setStatus('mandatory')
atmxCesVccRateRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateRxCells.setStatus('mandatory')
atmxCesVccRateSnpErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateSnpErrors.setStatus('mandatory')
atmxCesVccRateSeqNumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateSeqNumErrors.setStatus('mandatory')
atmxCesVccRateDroppedRxCellUnderrun = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateDroppedRxCellUnderrun.setStatus('mandatory')
atmxCesVccRateDroppedRxCellOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesVccRateDroppedRxCellOverrun.setStatus('mandatory')
atmxCesSvcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1), )
if mibBuilder.loadTexts: atmxCesSvcConfigTable.setStatus('mandatory')
atmxCesSvcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1), ).setIndexNames((0, "XYLAN-ATM-CE-MIB", "atmxCesSvcSlotIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesSvcPortIndex"), (0, "XYLAN-ATM-CE-MIB", "atmxCesSvcVciIndex"))
if mibBuilder.loadTexts: atmxCesSvcConfigEntry.setStatus('mandatory')
atmxCesSvcSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcSlotIndex.setStatus('mandatory')
atmxCesSvcPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcPortIndex.setStatus('mandatory')
atmxCesSvcVciIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcVciIndex.setStatus('mandatory')
atmxCesSvcRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcRemoteAddr.setStatus('mandatory')
atmxCesSvcRemoteVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcRemoteVpi.setStatus('mandatory')
atmxCesSvcRemoteVci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcRemoteVci.setStatus('mandatory')
atmxCesSvcFirstRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcFirstRetryInterval.setStatus('mandatory')
atmxCesSvcRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcRetryTimer.setStatus('mandatory')
atmxCesSvcRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcRetryLimit.setStatus('mandatory')
atmxCesSvcRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcRetryFailures.setStatus('mandatory')
atmxCesSvcConfigRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxCesSvcConfigRestart.setStatus('mandatory')
atmxCesSvcConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("establishmentInProgress", 2), ("connected", 3), ("retriesExhausted", 4), ("noAddressSupplied", 5), ("lowerLayerDown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcConfigOperStatus.setStatus('mandatory')
atmxCesSvcLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcLastReleaseCause.setStatus('mandatory')
atmxCesSvcLastReleaseDiagnostics = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmxCesSvcLastReleaseDiagnostics.setStatus('mandatory')
atmxCesVccTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1))
atmCesVccCreate = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1) + (0,1)).setObjects(("XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccVpi"), ("XYLAN-ATM-CE-MIB", "atmxCesVccVci"), ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkSlotIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkPortIndex"))
atmCesVccDelete = NotificationType((1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1) + (0,2)).setObjects(("XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccVpi"), ("XYLAN-ATM-CE-MIB", "atmxCesVccVci"), ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkSlotIndex"), ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkPortIndex"))
mibBuilder.exportSymbols("XYLAN-ATM-CE-MIB", atmCesVccDelete=atmCesVccDelete, atmxCesVccSlotIndex=atmxCesVccSlotIndex, atmxCesVccAtmUplinkSlotIndex=atmxCesVccAtmUplinkSlotIndex, atmxCesVccRateSnpErrors=atmxCesVccRateSnpErrors, atmxCesVccRateSeqNumErrors=atmxCesVccRateSeqNumErrors, atmxCesVccRateTxDataCells=atmxCesVccRateTxDataCells, atmxCesVccDescription=atmxCesVccDescription, atmxCesSvcLastReleaseDiagnostics=atmxCesSvcLastReleaseDiagnostics, atmxCesSvcRetryTimer=atmxCesSvcRetryTimer, atmxCesVccIdleCode=atmxCesVccIdleCode, atmxCesVccRateSlotIndex=atmxCesVccRateSlotIndex, atmxCesServiceServiceMode=atmxCesServiceServiceMode, atmxCesVccRatePortIndex=atmxCesVccRatePortIndex, atmxCesVccRateDroppedRxCellOverrun=atmxCesVccRateDroppedRxCellOverrun, atmxCesVccEntry=atmxCesVccEntry, atmxCesVccCellLossIntegrationPeriod=atmxCesVccCellLossIntegrationPeriod, atmxCesVccGroup=atmxCesVccGroup, atmxCesVccPortIndex=atmxCesVccPortIndex, atmxCesSvcRetryLimit=atmxCesSvcRetryLimit, atmxCesServiceAvailTimeSlot=atmxCesServiceAvailTimeSlot, atmxCesVccConnType=atmxCesVccConnType, atmxCesSvcRemoteVpi=atmxCesSvcRemoteVpi, atmxCesVccStatsPortIndex=atmxCesVccStatsPortIndex, atmxCesVccStatsEntry=atmxCesVccStatsEntry, atmxCesSvcConfigOperStatus=atmxCesSvcConfigOperStatus, atmxCesVccCDVT=atmxCesVccCDVT, atmxCesVccStatsCellLossStatus=atmxCesVccStatsCellLossStatus, atmxCesSvcRemoteVci=atmxCesSvcRemoteVci, atmxCesVccRateTable=atmxCesVccRateTable, atmxCesVccStatsTxCondCells=atmxCesVccStatsTxCondCells, atmxCesVccVci=atmxCesVccVci, atmxCesServiceDescription=atmxCesServiceDescription, atmxCesService=atmxCesService, atmxCesServiceEntry=atmxCesServiceEntry, atmxCesVccStatsDroppedRxCellOverrun=atmxCesVccStatsDroppedRxCellOverrun, atmCesVccCreate=atmCesVccCreate, atmxCesVccRateTxCondCells=atmxCesVccRateTxCondCells, atmxCesSvcConfigRestart=atmxCesSvcConfigRestart, atmxCesServiceOperStatus=atmxCesServiceOperStatus, atmxCesGroup=atmxCesGroup, atmxCesVccAdminStatus=atmxCesVccAdminStatus, atmxCesServicePortIndex=atmxCesServicePortIndex, atmxCesVccRateEntry=atmxCesVccRateEntry, atmxCesSvcLastReleaseCause=atmxCesSvcLastReleaseCause, atmxCesVccStatsSuppressedTxCells=atmxCesVccStatsSuppressedTxCells, atmxCesSvcPortIndex=atmxCesSvcPortIndex, atmxCesSvcRemoteAddr=atmxCesSvcRemoteAddr, atmxCesVccStatsRxCells=atmxCesVccStatsRxCells, atmxCesSvcRetryFailures=atmxCesSvcRetryFailures, atmxCesVccStatsSlotIndex=atmxCesVccStatsSlotIndex, atmxCesSvcConfigTable=atmxCesSvcConfigTable, atmxCesSvcSlotIndex=atmxCesSvcSlotIndex, atmxCesVccLocalAtmAddr=atmxCesVccLocalAtmAddr, atmxCesVccRateDroppedRxCellUnderrun=atmxCesVccRateDroppedRxCellUnderrun, atmxCesSvcFirstRetryInterval=atmxCesSvcFirstRetryInterval, atmxCesMIBTraps=atmxCesMIBTraps, atmxCesServiceTable=atmxCesServiceTable, atmxCesVccOperStatus=atmxCesVccOperStatus, atmxCesVccStatsSnpErrors=atmxCesVccStatsSnpErrors, atmxCesServiceAdminStatus=atmxCesServiceAdminStatus, atmxCesVccVpi=atmxCesVccVpi, atmxCesMIBObjects=atmxCesMIBObjects, atmxCesVccStatsTable=atmxCesVccStatsTable, atmCesVccStatsVci=atmCesVccStatsVci, atmxCesVccTimeSlots=atmxCesVccTimeSlots, atmxCesServiceSlotIndex=atmxCesServiceSlotIndex, atmxCesVccStatsSeqNumErrors=atmxCesVccStatsSeqNumErrors, atmxCesSvcVciIndex=atmxCesSvcVciIndex, atmxCesVccRateSuppressedTxCells=atmxCesVccRateSuppressedTxCells, atmxCesVccAtmUplinkVccVpi=atmxCesVccAtmUplinkVccVpi, atmxCesVccStatsDroppedRxCellUnderrun=atmxCesVccStatsDroppedRxCellUnderrun, atmxCesVccStatsGroup=atmxCesVccStatsGroup, atmxCesVccPartialFill=atmxCesVccPartialFill, atmxCesSvcConfigEntry=atmxCesSvcConfigEntry, atmxCesVccAtmUplinkVccVci=atmxCesVccAtmUplinkVccVci, atmxCesServiceServiceClock=atmxCesServiceServiceClock, atmxCesVccRateRxCells=atmxCesVccRateRxCells, atmxCesVccBufMaxSize=atmxCesVccBufMaxSize, atmxCesSvcConfigGroup=atmxCesSvcConfigGroup, atmCesVccRateVci=atmCesVccRateVci, atmxCesVccTable=atmxCesVccTable, atmxCesVccTraps=atmxCesVccTraps, atmxCesVccStatsTxDataCells=atmxCesVccStatsTxDataCells, atmxCesVccAtmUplinkPortIndex=atmxCesVccAtmUplinkPortIndex)

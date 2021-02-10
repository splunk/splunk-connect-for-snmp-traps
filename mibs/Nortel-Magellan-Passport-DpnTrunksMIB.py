#
# PySNMP MIB module Nortel-Magellan-Passport-DpnTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-DpnTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:17:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
PassportCounter64, RowStatus, InterfaceIndex, Unsigned32, DisplayString, Integer32, StorageType, Gauge32, Counter32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "PassportCounter64", "RowStatus", "InterfaceIndex", "Unsigned32", "DisplayString", "Integer32", "StorageType", "Gauge32", "Counter32")
FixedPoint1, AsciiString, NonReplicated = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "FixedPoint1", "AsciiString", "NonReplicated")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Bits, TimeTicks, ModuleIdentity, Counter64, Unsigned32, Integer32, iso, NotificationType, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "Integer32", "iso", "NotificationType", "ObjectIdentity", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dpnTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40))
dpnGate = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61))
dpnGateRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1), )
if mibBuilder.loadTexts: dpnGateRowStatusTable.setStatus('mandatory')
dpnGateRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateRowStatusEntry.setStatus('mandatory')
dpnGateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateRowStatus.setStatus('mandatory')
dpnGateComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateComponentName.setStatus('mandatory')
dpnGateStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateStorageType.setStatus('mandatory')
dpnGateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: dpnGateIndex.setStatus('mandatory')
dpnGateIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100), )
if mibBuilder.loadTexts: dpnGateIfEntryTable.setStatus('mandatory')
dpnGateIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateIfEntryEntry.setStatus('mandatory')
dpnGateIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateIfAdminStatus.setStatus('mandatory')
dpnGateIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateIfIndex.setStatus('mandatory')
dpnGateProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101), )
if mibBuilder.loadTexts: dpnGateProvTable.setStatus('mandatory')
dpnGateProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateProvEntry.setStatus('mandatory')
dpnGateExpectedRemoteNamsId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateExpectedRemoteNamsId.setStatus('mandatory')
dpnGateRemoteValidationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("continue", 0), ("disable", 1))).clone('continue')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateRemoteValidationAction.setStatus('mandatory')
dpnGateLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3))).clone(namedValues=NamedValues(("dedicated", 0), ("dialIn", 3))).clone('dedicated')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateLinkType.setStatus('mandatory')
dpnGateOverridesTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102), )
if mibBuilder.loadTexts: dpnGateOverridesTable.setStatus('mandatory')
dpnGateOverridesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateOverridesEntry.setStatus('mandatory')
dpnGateOverrideTransmitSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 1), Gauge32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1000, 4294967295), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateOverrideTransmitSpeed.setStatus('mandatory')
dpnGateOldOverrideRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateOldOverrideRoundTripDelay.setStatus('obsolete')
dpnGateOverrideRoundTripUsec = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 3), FixedPoint1().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateOverrideRoundTripUsec.setStatus('mandatory')
dpnGateStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103), )
if mibBuilder.loadTexts: dpnGateStateTable.setStatus('mandatory')
dpnGateStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateStateEntry.setStatus('mandatory')
dpnGateAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateAdminState.setStatus('mandatory')
dpnGateOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateOperationalState.setStatus('mandatory')
dpnGateUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUsageState.setStatus('mandatory')
dpnGateAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateAvailabilityStatus.setStatus('mandatory')
dpnGateProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateProceduralStatus.setStatus('mandatory')
dpnGateControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateControlStatus.setStatus('mandatory')
dpnGateAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateAlarmStatus.setStatus('mandatory')
dpnGateStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateStandbyStatus.setStatus('mandatory')
dpnGateUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUnknownStatus.setStatus('mandatory')
dpnGateOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104), )
if mibBuilder.loadTexts: dpnGateOperStatusTable.setStatus('mandatory')
dpnGateOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateOperStatusEntry.setStatus('mandatory')
dpnGateSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateSnmpOperStatus.setStatus('mandatory')
dpnGateOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105), )
if mibBuilder.loadTexts: dpnGateOperTable.setStatus('mandatory')
dpnGateOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateOperEntry.setStatus('mandatory')
dpnGateRemoteComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 26))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateRemoteComponentName.setStatus('mandatory')
dpnGateRemoteNamsMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 2), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateRemoteNamsMnemonic.setStatus('mandatory')
dpnGateLinkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("trunk", 0), ("networkLink", 1), ("unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateLinkMode.setStatus('mandatory')
dpnGateActivateReason = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 15))).clone(namedValues=NamedValues(("dedicated", 0), ("dnl", 1), ("dbnl", 2), ("dialIn", 3), ("bwod", 5), ("unknown", 15))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateActivateReason.setStatus('mandatory')
dpnGateTransportTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106), )
if mibBuilder.loadTexts: dpnGateTransportTable.setStatus('mandatory')
dpnGateTransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateTransportEntry.setStatus('mandatory')
dpnGateMeasuredSpeedToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateMeasuredSpeedToIf.setStatus('mandatory')
dpnGateMeasuredRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateMeasuredRoundTripDelay.setStatus('obsolete')
dpnGateMaxTxUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateMaxTxUnit.setStatus('mandatory')
dpnGateMeasuredRoundTripDelayUsec = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 4), FixedPoint1().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateMeasuredRoundTripDelayUsec.setStatus('mandatory')
dpnGateStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107), )
if mibBuilder.loadTexts: dpnGateStatsTable.setStatus('mandatory')
dpnGateStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"))
if mibBuilder.loadTexts: dpnGateStatsEntry.setStatus('mandatory')
dpnGatePktFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 1), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGatePktFromIf.setStatus('mandatory')
dpnGateTrunkPktFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateTrunkPktFromIf.setStatus('mandatory')
dpnGateTrunkPktToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateTrunkPktToIf.setStatus('mandatory')
dpnGateDiscardUnforward = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 4), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateDiscardUnforward.setStatus('mandatory')
dpnGateDiscardTrunkPktFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateDiscardTrunkPktFromIf.setStatus('mandatory')
dpnGateStagingAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateStagingAttempts.setStatus('mandatory')
dpnGateDiscardTrunkPktToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateDiscardTrunkPktToIf.setStatus('mandatory')
dpnGateFwdStats = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3))
dpnGateFwdStatsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1), )
if mibBuilder.loadTexts: dpnGateFwdStatsRowStatusTable.setStatus('mandatory')
dpnGateFwdStatsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateFwdStatsIndex"))
if mibBuilder.loadTexts: dpnGateFwdStatsRowStatusEntry.setStatus('mandatory')
dpnGateFwdStatsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsRowStatus.setStatus('mandatory')
dpnGateFwdStatsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsComponentName.setStatus('mandatory')
dpnGateFwdStatsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsStorageType.setStatus('mandatory')
dpnGateFwdStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateFwdStatsIndex.setStatus('mandatory')
dpnGateFwdStatsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10), )
if mibBuilder.loadTexts: dpnGateFwdStatsOperTable.setStatus('mandatory')
dpnGateFwdStatsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateFwdStatsIndex"))
if mibBuilder.loadTexts: dpnGateFwdStatsOperEntry.setStatus('mandatory')
dpnGateFwdStatsFwdPktFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 1), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsFwdPktFromIf.setStatus('mandatory')
dpnGateFwdStatsFwdDiscUnforwardFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 2), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsFwdDiscUnforwardFromIf.setStatus('mandatory')
dpnGateFwdStatsFwdOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 3), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFwdStatsFwdOctetFromIf.setStatus('mandatory')
dpnTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1))
dpnTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5))
dpnTrunksGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5, 2))
dpnTrunksGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5, 2, 2))
dpnTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3))
dpnTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5))
dpnTrunksCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5, 2))
dpnTrunksCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-DpnTrunksMIB", dpnGateStateTable=dpnGateStateTable, dpnGateFwdStats=dpnGateFwdStats, dpnGateFwdStatsRowStatusTable=dpnGateFwdStatsRowStatusTable, dpnGateUnknownStatus=dpnGateUnknownStatus, dpnGateRowStatusTable=dpnGateRowStatusTable, dpnGateOverridesTable=dpnGateOverridesTable, dpnGateOperationalState=dpnGateOperationalState, dpnGateOverrideRoundTripUsec=dpnGateOverrideRoundTripUsec, dpnGateActivateReason=dpnGateActivateReason, dpnTrunksMIB=dpnTrunksMIB, dpnGateFwdStatsOperEntry=dpnGateFwdStatsOperEntry, dpnGateFwdStatsFwdDiscUnforwardFromIf=dpnGateFwdStatsFwdDiscUnforwardFromIf, dpnGateTrunkPktFromIf=dpnGateTrunkPktFromIf, dpnGateTransportEntry=dpnGateTransportEntry, dpnGateProceduralStatus=dpnGateProceduralStatus, dpnGateIfIndex=dpnGateIfIndex, dpnGateOverridesEntry=dpnGateOverridesEntry, dpnGateProvTable=dpnGateProvTable, dpnGateOldOverrideRoundTripDelay=dpnGateOldOverrideRoundTripDelay, dpnGateOperStatusEntry=dpnGateOperStatusEntry, dpnTrunksCapabilitiesBE01A=dpnTrunksCapabilitiesBE01A, dpnGateMeasuredSpeedToIf=dpnGateMeasuredSpeedToIf, dpnGateIfAdminStatus=dpnGateIfAdminStatus, dpnGate=dpnGate, dpnTrunksGroupBE01A=dpnTrunksGroupBE01A, dpnGateDiscardTrunkPktToIf=dpnGateDiscardTrunkPktToIf, dpnGateIndex=dpnGateIndex, dpnGateOperStatusTable=dpnGateOperStatusTable, dpnGateOverrideTransmitSpeed=dpnGateOverrideTransmitSpeed, dpnGateTrunkPktToIf=dpnGateTrunkPktToIf, dpnGateOperTable=dpnGateOperTable, dpnGateFwdStatsComponentName=dpnGateFwdStatsComponentName, dpnGateAdminState=dpnGateAdminState, dpnGateFwdStatsFwdOctetFromIf=dpnGateFwdStatsFwdOctetFromIf, dpnGatePktFromIf=dpnGatePktFromIf, dpnGateLinkType=dpnGateLinkType, dpnGateControlStatus=dpnGateControlStatus, dpnGateLinkMode=dpnGateLinkMode, dpnGateRowStatus=dpnGateRowStatus, dpnGateFwdStatsStorageType=dpnGateFwdStatsStorageType, dpnGateRemoteValidationAction=dpnGateRemoteValidationAction, dpnTrunksCapabilities=dpnTrunksCapabilities, dpnTrunksGroupBE01=dpnTrunksGroupBE01, dpnGateMeasuredRoundTripDelayUsec=dpnGateMeasuredRoundTripDelayUsec, dpnGateProvEntry=dpnGateProvEntry, dpnGateStatsTable=dpnGateStatsTable, dpnTrunksGroup=dpnTrunksGroup, dpnTrunksGroupBE=dpnTrunksGroupBE, dpnGateDiscardUnforward=dpnGateDiscardUnforward, dpnTrunksCapabilitiesBE=dpnTrunksCapabilitiesBE, dpnGateStorageType=dpnGateStorageType, dpnGateExpectedRemoteNamsId=dpnGateExpectedRemoteNamsId, dpnGateFwdStatsRowStatusEntry=dpnGateFwdStatsRowStatusEntry, dpnGateStandbyStatus=dpnGateStandbyStatus, dpnGateComponentName=dpnGateComponentName, dpnGateDiscardTrunkPktFromIf=dpnGateDiscardTrunkPktFromIf, dpnGateSnmpOperStatus=dpnGateSnmpOperStatus, dpnGateFwdStatsRowStatus=dpnGateFwdStatsRowStatus, dpnGateRowStatusEntry=dpnGateRowStatusEntry, dpnGateIfEntryTable=dpnGateIfEntryTable, dpnGateOperEntry=dpnGateOperEntry, dpnGateRemoteNamsMnemonic=dpnGateRemoteNamsMnemonic, dpnGateTransportTable=dpnGateTransportTable, dpnGateFwdStatsOperTable=dpnGateFwdStatsOperTable, dpnGateAvailabilityStatus=dpnGateAvailabilityStatus, dpnGateStagingAttempts=dpnGateStagingAttempts, dpnGateFwdStatsFwdPktFromIf=dpnGateFwdStatsFwdPktFromIf, dpnGateRemoteComponentName=dpnGateRemoteComponentName, dpnGateAlarmStatus=dpnGateAlarmStatus, dpnTrunksCapabilitiesBE01=dpnTrunksCapabilitiesBE01, dpnGateStateEntry=dpnGateStateEntry, dpnGateMeasuredRoundTripDelay=dpnGateMeasuredRoundTripDelay, dpnGateMaxTxUnit=dpnGateMaxTxUnit, dpnGateIfEntryEntry=dpnGateIfEntryEntry, dpnGateStatsEntry=dpnGateStatsEntry, dpnGateUsageState=dpnGateUsageState, dpnGateFwdStatsIndex=dpnGateFwdStatsIndex)

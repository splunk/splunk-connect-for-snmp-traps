#
# PySNMP MIB module EDGELINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EDGELINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:44:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, ObjectName, Counter32, Bits, ModuleIdentity, enterprises, Unsigned32, Gauge32, ObjectIdentity, IpAddress, NotificationType, iso, ObjectSyntax, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ObjectName", "Counter32", "Bits", "ModuleIdentity", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "iso", "ObjectSyntax", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
telco = MibIdentifier((1, 3, 6, 1, 4, 1, 564))
edgeLink = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101))
elM13v1 = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1))
elDS1CM = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 1))
elCM = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 2))
elCMIfc = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 3))
elPM = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 4))
elDS1PM = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 5))
elDS1PMCur = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 6))
elDS1PMIvl = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 7))
elDS1PMTot = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 8))
elFM = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 9))
elFMAlmLog = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 10))
elFMCurAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 11))
elFMTrapFields = MibIdentifier((1, 3, 6, 1, 4, 1, 564, 101, 1, 12))
elDS1CMTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1), )
if mibBuilder.loadTexts: elDS1CMTable.setStatus('mandatory')
elDS1CMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elDS1CMChannelNumber"))
if mibBuilder.loadTexts: elDS1CMEntry.setStatus('mandatory')
elDS1CMChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1CMChannelNumber.setStatus('mandatory')
elDS1CMLineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds1LineCodeAMI", 0), ("ds1LineCodeB8ZS", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMLineCode.setStatus('mandatory')
elDS1CMLineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ds1LineBuildout0to133ft", 0), ("ds1LineBuildout133to266ft", 1), ("ds1LineBuildout266to399ft", 2), ("ds1LineBuildout399to533ft", 3), ("ds1LineBuildout533to655ft", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMLineBuildout.setStatus('mandatory')
elDS1CMLoopbackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ds1LpbkNone", 1), ("ds1LpbkTerminal", 2), ("ds1LpbkFacility", 3), ("ds1LpbkRemoteTerminal", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMLoopbackMode.setStatus('mandatory')
elDS1CMServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds1SetOutOfService", 0), ("ds1SetInService", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMServiceMode.setStatus('mandatory')
elDS1CMInterfaceEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("ds1Equipped", 0), ("ds1Unequipped", 1), ("ds1Disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMInterfaceEquipped.setStatus('mandatory')
elDS1CMChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMChannelName.setStatus('mandatory')
elDS1CMInputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds1InputPresent", 0), ("ds1NoInputpresent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1CMInputStatus.setStatus('mandatory')
elDS1CMMaskState = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ds1InputInit", 1), ("ds1WaitingForInput", 2), ("ds1TimerRunning", 3), ("ds1MonitorActivated", 4), ("ds1UnEquipped", 5), ("ds1StatusReported", 6), ("ds1AlarmedState", 7), ("ds1DisabledState", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1CMMaskState.setStatus('mandatory')
elDS1CMInterfaceRescan = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ds1AllChannelsAutoSenseEnable", 1), ("ds1AllChannelsAutoSenseDisable", 2), ("ds1ChannelRescan", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elDS1CMInterfaceRescan.setStatus('mandatory')
elALLDS1CMLineCode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ds1LineCodeAMI", 0), ("ds1LineCodeB8ZS", 1), ("indeterminate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elALLDS1CMLineCode.setStatus('mandatory')
elALLDS1CMLineBuildout = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds1LineBuildout0to133ft", 0), ("ds1LineBuildout133to266ft", 1), ("ds1LineBuildout266to399ft", 2), ("ds1LineBuildout399to533ft", 3), ("ds1LineBuildout533to655ft", 4), ("indeterminate", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elALLDS1CMLineBuildout.setStatus('mandatory')
elALLDS1CMLoopbackMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds1LpbkNone", 1), ("ds1LpbkTerminal", 2), ("ds1LpbkFacility", 3), ("ds1LpbkRemoteTerminal", 4), ("indeterminate", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elALLDS1CMLoopbackMode.setStatus('mandatory')
elALLDS1CMServiceMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ds1SetOutOfService", 0), ("ds1SetInService", 1), ("indeterminate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elALLDS1CMServiceMode.setStatus('mandatory')
elALLDS1CMInterfaceEquipped = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ds1Equipped", 0), ("ds1Unequipped", 1), ("indeterminate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elALLDS1CMInterfaceEquipped.setStatus('mandatory')
elCMSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elCMSystemStatus.setStatus('mandatory')
elCMDS3ParityMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("ds3pBitParityMode", 2), ("ds3cBitParityMode", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMDS3ParityMode.setStatus('mandatory')
elCMDS3LineBuildout = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ds3LineBuildout0to100ft", 0), ("ds3LineBuildout100to200ft", 1), ("ds3LineBuildout200to450ft", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMDS3LineBuildout.setStatus('mandatory')
elCMDS3TxTiming = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3TxTimingLooped", 1), ("ds3TxTimingLocal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMDS3TxTiming.setStatus('mandatory')
elCMProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("protModeProtected", 0), ("protModeUnprotected", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMProtectionMode.setStatus('mandatory')
elCMCardSelect = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("cardAOnline", 0), ("cardBOnline", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMCardSelect.setStatus('mandatory')
elCMClearTooManySwitches = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("indeterminate", 1), ("clearTooManySwitchesLock", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMClearTooManySwitches.setStatus('mandatory')
elCMDS3LoopbackMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ds3LpbkNone", 1), ("ds3LpbkTerminal", 2), ("ds3LpbkFacility", 3), ("ds3LpbkRemoteFacility", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMDS3LoopbackMode.setStatus('mandatory')
elCMDS3ServiceMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds3SetOutOfService", 0), ("ds3SetInService", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMDS3ServiceMode.setStatus('mandatory')
elCMCurTimeDate = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMCurTimeDate.setStatus('mandatory')
elCMBerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ds3BerThreshold10-6", 1), ("ds3BerThreshold10-7", 2), ("ds3BerThreshold10-8", 3), ("ds3BerThreshold10-9", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMBerThreshold.setStatus('mandatory')
elCMSystemInfo = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elCMSystemInfo.setStatus('mandatory')
elCMPPPPortBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("baud300", 1), ("baud1200", 2), ("baud2400", 3), ("baud4800", 4), ("baud9600", 5), ("baud14400", 6), ("baud19200", 7), ("baud28800", 8), ("baud38400", 9), ("baud57600", 10), ("baud115200", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elCMPPPPortBaudRate.setStatus('mandatory')
elCMRemoteCBitIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMRemoteCBitIPAddress.setStatus('mandatory')
elCMLocalCBitIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMLocalCBitIPAddress.setStatus('mandatory')
elCMCBitIPSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMCBitIPSubnetMask.setStatus('mandatory')
elCMRemotePPPIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMRemotePPPIPAddress.setStatus('mandatory')
elCMIfcTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5), )
if mibBuilder.loadTexts: elCMIfcTable.setStatus('mandatory')
elCMIfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1), ).setIndexNames((0, "EDGELINK-MIB", "elCMIfcInterfaceNumber"))
if mibBuilder.loadTexts: elCMIfcEntry.setStatus('mandatory')
elCMIfcInterfaceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ifEthernet", 1), ("ifPPP", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elCMIfcInterfaceNumber.setStatus('mandatory')
elCMIfcMyIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcMyIPAddr.setStatus('mandatory')
elCMIfcMyIPSubnetAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcMyIPSubnetAddrMask.setStatus('mandatory')
elCMIfcMyDefaultGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcMyDefaultGatewayAddr.setStatus('mandatory')
elCMIfcTrapSendAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcTrapSendAddr1.setStatus('mandatory')
elCMIfcTrapSendAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcTrapSendAddr2.setStatus('mandatory')
elCMIfcTrapSendAddr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcTrapSendAddr3.setStatus('mandatory')
elCMIfcTrapSendAddr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elCMIfcTrapSendAddr4.setStatus('mandatory')
elPMDS3TotalSwitches = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elPMDS3TotalSwitches.setStatus('mandatory')
elPMClearAllPMMetrics = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("indeterminate", 1), ("clearAllPMMetrics", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elPMClearAllPMMetrics.setStatus('mandatory')
elDS1PMTimeElapsed = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMTimeElapsed.setStatus('mandatory')
elDS1PMValidIntervals = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMValidIntervals.setStatus('mandatory')
elDS1PMCurTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1), )
if mibBuilder.loadTexts: elDS1PMCurTable.setStatus('mandatory')
elDS1PMCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elDS1PMCurChannelNumber"))
if mibBuilder.loadTexts: elDS1PMCurEntry.setStatus('mandatory')
elDS1PMCurChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMCurChannelNumber.setStatus('mandatory')
elDS1PMCurLineCodeViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMCurLineCodeViolations.setStatus('mandatory')
elDS1PMCurErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMCurErroredSeconds.setStatus('mandatory')
elDS1PMIvlTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1), )
if mibBuilder.loadTexts: elDS1PMIvlTable.setStatus('mandatory')
elDS1PMIvlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elDS1PMIvlChannelNumber"), (0, "EDGELINK-MIB", "elDS1PMIvlIntervalNumber"))
if mibBuilder.loadTexts: elDS1PMIvlEntry.setStatus('mandatory')
elDS1PMIvlChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMIvlChannelNumber.setStatus('mandatory')
elDS1PMIvlIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMIvlIntervalNumber.setStatus('mandatory')
elDS1PMIvlLineCodeViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMIvlLineCodeViolations.setStatus('mandatory')
elDS1PMIvlErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMIvlErroredSeconds.setStatus('mandatory')
elDS1PMTotTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1), )
if mibBuilder.loadTexts: elDS1PMTotTable.setStatus('mandatory')
elDS1PMTotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elDS1PMTotChannelNumber"))
if mibBuilder.loadTexts: elDS1PMTotEntry.setStatus('mandatory')
elDS1PMTotChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMTotChannelNumber.setStatus('mandatory')
elDS1PMTotLineCodeViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMTotLineCodeViolations.setStatus('mandatory')
elDS1PMTotErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elDS1PMTotErroredSeconds.setStatus('mandatory')
elFMFillAlarmLogTable = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("indeterminate", 1), ("fillAlarmLogTable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elFMFillAlarmLogTable.setStatus('mandatory')
elFMClearAlarmLog = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("indeterminate", 1), ("clearAlarmLog", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elFMClearAlarmLog.setStatus('mandatory')
elFMDS1AutoSenseMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableDs1AutoSense", 1), ("disableDs1AutoSense", 2), ("rescanAllDs1Inputs", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elFMDS1AutoSenseMode.setStatus('mandatory')
elFMDS1InputAlarmMode = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("statusOnDs1InputLos", 0), ("alarmOnDs1InputLos", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elFMDS1InputAlarmMode.setStatus('mandatory')
elFMAlmLogTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1), )
if mibBuilder.loadTexts: elFMAlmLogTable.setStatus('mandatory')
elFMAlmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elFMAlmLogEntryNumber"))
if mibBuilder.loadTexts: elFMAlmLogEntry.setStatus('mandatory')
elFMAlmLogEntryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogEntryNumber.setStatus('mandatory')
elFMAlmLogTableAlarmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogTableAlarmNumber.setStatus('mandatory')
elFMAlmLogTableDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogTableDescription.setStatus('mandatory')
elFMAlmLogTableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("set", 1), ("clear", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogTableStatus.setStatus('mandatory')
elFMAlmLogTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogTableTimestamp.setStatus('mandatory')
elFMAlmLogTableChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMAlmLogTableChannel.setStatus('mandatory')
elFMCurAlmTable = MibTable((1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1), )
if mibBuilder.loadTexts: elFMCurAlmTable.setStatus('mandatory')
elFMCurAlmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1), ).setIndexNames((0, "EDGELINK-MIB", "elFMCurAlmTableAlarmNumber"), (0, "EDGELINK-MIB", "elFMCurAlmTableChannel"))
if mibBuilder.loadTexts: elFMCurAlmEntry.setStatus('mandatory')
elFMCurAlmTableAlarmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMCurAlmTableAlarmNumber.setStatus('mandatory')
elFMCurAlmTableChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMCurAlmTableChannel.setStatus('mandatory')
elFMCurAlmTableDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMCurAlmTableDescription.setStatus('mandatory')
elFMTrapAlarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMTrapAlarmNumber.setStatus('mandatory')
elFMTrapAlarmText = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMTrapAlarmText.setStatus('mandatory')
elFMTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMTrapTimeStamp.setStatus('mandatory')
elFMTrapAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMTrapAlarmStatus.setStatus('mandatory')
elFMTrapChannelNumber = MibScalar((1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elFMTrapChannelNumber.setStatus('mandatory')
edgeLinkEvent = NotificationType((1, 3, 6, 1, 4, 1, 564, 101, 1) + (0,1)).setObjects(("EDGELINK-MIB", "elFMTrapAlarmNumber"), ("EDGELINK-MIB", "elFMTrapAlarmText"), ("EDGELINK-MIB", "elFMTrapTimeStamp"), ("EDGELINK-MIB", "elFMTrapAlarmStatus"), ("EDGELINK-MIB", "elFMTrapChannelNumber"), ("EDGELINK-MIB", "elCMSystemStatus"))
mibBuilder.exportSymbols("EDGELINK-MIB", elFMDS1InputAlarmMode=elFMDS1InputAlarmMode, elDS1CMInterfaceRescan=elDS1CMInterfaceRescan, elDS1CMLineBuildout=elDS1CMLineBuildout, elDS1CMChannelName=elDS1CMChannelName, elCMSystemInfo=elCMSystemInfo, elCMDS3TxTiming=elCMDS3TxTiming, elDS1PM=elDS1PM, elPMClearAllPMMetrics=elPMClearAllPMMetrics, elDS1PMTotLineCodeViolations=elDS1PMTotLineCodeViolations, elM13v1=elM13v1, elCMIfcTrapSendAddr4=elCMIfcTrapSendAddr4, edgeLink=edgeLink, elCMSystemStatus=elCMSystemStatus, elFMCurAlmTableDescription=elFMCurAlmTableDescription, elDS1PMCurLineCodeViolations=elDS1PMCurLineCodeViolations, elDS1CMChannelNumber=elDS1CMChannelNumber, elDS1CMEntry=elDS1CMEntry, elFMAlmLogTableDescription=elFMAlmLogTableDescription, elDS1CMServiceMode=elDS1CMServiceMode, elFMClearAlarmLog=elFMClearAlarmLog, elCMRemoteCBitIPAddress=elCMRemoteCBitIPAddress, elCMBerThreshold=elCMBerThreshold, elALLDS1CMLoopbackMode=elALLDS1CMLoopbackMode, elDS1PMTotErroredSeconds=elDS1PMTotErroredSeconds, elCMDS3ParityMode=elCMDS3ParityMode, elDS1PMIvlEntry=elDS1PMIvlEntry, elCMIfcMyIPAddr=elCMIfcMyIPAddr, elDS1PMIvlTable=elDS1PMIvlTable, elFMAlmLogEntryNumber=elFMAlmLogEntryNumber, elALLDS1CMInterfaceEquipped=elALLDS1CMInterfaceEquipped, elALLDS1CMLineBuildout=elALLDS1CMLineBuildout, elDS1CMInterfaceEquipped=elDS1CMInterfaceEquipped, elCMProtectionMode=elCMProtectionMode, elCMIfcEntry=elCMIfcEntry, elCMIfcMyDefaultGatewayAddr=elCMIfcMyDefaultGatewayAddr, edgeLinkEvent=edgeLinkEvent, elPMDS3TotalSwitches=elPMDS3TotalSwitches, elDS1PMTotChannelNumber=elDS1PMTotChannelNumber, elDS1PMValidIntervals=elDS1PMValidIntervals, elCMIfcMyIPSubnetAddrMask=elCMIfcMyIPSubnetAddrMask, elFMAlmLogEntry=elFMAlmLogEntry, elDS1PMCur=elDS1PMCur, elFMTrapFields=elFMTrapFields, elCMIfcTrapSendAddr3=elCMIfcTrapSendAddr3, elDS1PMIvlLineCodeViolations=elDS1PMIvlLineCodeViolations, elDS1PMCurErroredSeconds=elDS1PMCurErroredSeconds, elCMIfcTrapSendAddr2=elCMIfcTrapSendAddr2, elFMAlmLogTableChannel=elFMAlmLogTableChannel, elCMLocalCBitIPAddress=elCMLocalCBitIPAddress, elCMPPPPortBaudRate=elCMPPPPortBaudRate, elDS1PMIvl=elDS1PMIvl, elDS1CMMaskState=elDS1CMMaskState, elPM=elPM, elCM=elCM, elFMAlmLog=elFMAlmLog, elCMDS3ServiceMode=elCMDS3ServiceMode, elFMAlmLogTableAlarmNumber=elFMAlmLogTableAlarmNumber, elCMClearTooManySwitches=elCMClearTooManySwitches, elFMCurAlmTable=elFMCurAlmTable, elDS1CMTable=elDS1CMTable, telco=telco, elDS1PMCurChannelNumber=elDS1PMCurChannelNumber, elDS1CMLineCode=elDS1CMLineCode, elCMRemotePPPIPAddress=elCMRemotePPPIPAddress, elDS1PMIvlIntervalNumber=elDS1PMIvlIntervalNumber, elFMAlmLogTable=elFMAlmLogTable, elDS1PMCurEntry=elDS1PMCurEntry, elFMDS1AutoSenseMode=elFMDS1AutoSenseMode, elDS1CM=elDS1CM, elCMIfcTable=elCMIfcTable, elCMCurTimeDate=elCMCurTimeDate, elDS1CMLoopbackMode=elDS1CMLoopbackMode, elALLDS1CMLineCode=elALLDS1CMLineCode, elCMDS3LoopbackMode=elCMDS3LoopbackMode, elFMTrapAlarmText=elFMTrapAlarmText, elDS1PMTimeElapsed=elDS1PMTimeElapsed, elCMCardSelect=elCMCardSelect, elCMIfc=elCMIfc, elFM=elFM, elFMCurAlmTableAlarmNumber=elFMCurAlmTableAlarmNumber, elDS1PMIvlChannelNumber=elDS1PMIvlChannelNumber, elFMCurAlm=elFMCurAlm, elCMDS3LineBuildout=elCMDS3LineBuildout, elCMIfcTrapSendAddr1=elCMIfcTrapSendAddr1, elCMCBitIPSubnetMask=elCMCBitIPSubnetMask, elFMAlmLogTableStatus=elFMAlmLogTableStatus, elDS1PMIvlErroredSeconds=elDS1PMIvlErroredSeconds, elFMCurAlmEntry=elFMCurAlmEntry, elALLDS1CMServiceMode=elALLDS1CMServiceMode, elCMIfcInterfaceNumber=elCMIfcInterfaceNumber, elFMTrapTimeStamp=elFMTrapTimeStamp, elFMTrapAlarmNumber=elFMTrapAlarmNumber, elFMCurAlmTableChannel=elFMCurAlmTableChannel, elFMTrapChannelNumber=elFMTrapChannelNumber, elDS1CMInputStatus=elDS1CMInputStatus, elFMFillAlarmLogTable=elFMFillAlarmLogTable, elFMAlmLogTableTimestamp=elFMAlmLogTableTimestamp, elDS1PMTot=elDS1PMTot, elDS1PMCurTable=elDS1PMCurTable, elDS1PMTotTable=elDS1PMTotTable, elFMTrapAlarmStatus=elFMTrapAlarmStatus, elDS1PMTotEntry=elDS1PMTotEntry)

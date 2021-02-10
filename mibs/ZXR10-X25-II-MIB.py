#
# PySNMP MIB module ZXR10-X25-II-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-X25-II-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, Bits, ObjectIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, enterprises, TimeTicks, mgmt, MibIdentifier, Gauge32, Unsigned32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Bits", "ObjectIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "enterprises", "TimeTicks", "mgmt", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10X25MIBII = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4001))
class DisplayString(OctetString):
    pass

class UShort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class UChar(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class UCHAR(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class X25Address(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

zxr10X25II = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1))
zxr10X25PVCTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4), )
if mibBuilder.loadTexts: zxr10X25PVCTable.setStatus('current')
zxr10X25PVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25PVCNo"))
if mibBuilder.loadTexts: zxr10X25PVCEntry.setStatus('current')
zxr10X25PVCRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25PVCRowStatus.setStatus('current')
zxr10X25PVCNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 2), UShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25PVCNo.setStatus('current')
zxr10X25PVCStartLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 3), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25PVCStartLcn.setStatus('current')
zxr10X25PVCNextLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 4), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25PVCNextLcn.setStatus('current')
zxr10X25PVCStartPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25PVCStartPortName.setStatus('current')
zxr10X25PVCNextPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25PVCNextPortName.setStatus('current')
zxr10X25PVCStartPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25PVCStartPortIfIndex.setStatus('current')
zxr10X25PVCNextPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25PVCNextPortIfIndex.setStatus('current')
zxr10X25OperTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6), )
if mibBuilder.loadTexts: zxr10X25OperTable.setStatus('current')
zxr10X25OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25OperIfIndex"))
if mibBuilder.loadTexts: zxr10X25OperEntry.setStatus('current')
zxr10X25OperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("active", 1), ("modify", 4), ("resetDefault", 6), ("encapFrx25", 7), ("encapX25", 8), ("noencap", 9), ("enable", 10), ("noenable", 11)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperStatus.setStatus('current')
zxr10X25OperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25OperIfIndex.setStatus('current')
zxr10X25OperLapbMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 3), UCHAR()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbMode.setStatus('current')
zxr10X25OperLapbPSSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 4), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPSSize.setStatus('current')
zxr10X25OperLapbWinSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 5), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbWinSize.setStatus('current')
zxr10X25OperLapbRetranCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 6), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbRetranCount.setStatus('current')
zxr10X25OperLapbTimeoutT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 7), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbTimeoutT1.setStatus('current')
zxr10X25OperLapbTimeoutT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 8), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbTimeoutT2.setStatus('current')
zxr10X25OperLapbTimeoutT3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 9), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbTimeoutT3.setStatus('current')
zxr10X25OperLapbPktMaxVC = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 10), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktMaxVC.setStatus('current')
zxr10X25OperLapbPktT20 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 11), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktT20.setStatus('current')
zxr10X25OperLapbPktT21 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 12), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktT21.setStatus('current')
zxr10X25OperLapbPktT22 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 13), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktT22.setStatus('current')
zxr10X25OperLapbPktT23 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 14), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktT23.setStatus('current')
zxr10X25OperLapbPktWinSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 15), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktWinSize.setStatus('current')
zxr10X25OperLapbPktPSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 16), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktPSize.setStatus('current')
zxr10X25OperLapbPktSvcIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 17), UShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbPktSvcIdleTime.setStatus('current')
zxr10X25OperLapbDteDce = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 18), UCHAR()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbDteDce.setStatus('current')
zxr10X25OperLapbUserOrTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 19), UCHAR()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25OperLapbUserOrTrunk.setStatus('current')
zxr10X25OperIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25OperIfName.setStatus('current')
zxr10X25OperLabpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 21), UCHAR()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25OperLabpStatus.setStatus('current')
zxr10X25OperInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 6, 1, 22), UCHAR()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25OperInterfaceType.setStatus('current')
zxr10X25SVCTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7), )
if mibBuilder.loadTexts: zxr10X25SVCTable.setStatus('current')
zxr10X25SVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25SVCNo"))
if mibBuilder.loadTexts: zxr10X25SVCEntry.setStatus('current')
zxr10X25SVCNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 1), UShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCNo.setStatus('current')
zxr10X25SVCStartLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 2), UShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCStartLcn.setStatus('current')
zxr10X25SVCNextLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 3), UShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCNextLcn.setStatus('current')
zxr10X25SVCStartPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCStartPortName.setStatus('current')
zxr10X25SVCNextPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCNextPortName.setStatus('current')
zxr10X25SVCStartPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCStartPortIfIndex.setStatus('current')
zxr10X25SVCNextPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 7, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25SVCNextPortIfIndex.setStatus('current')
zxr10X25LapbFlowTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8), )
if mibBuilder.loadTexts: zxr10X25LapbFlowTable.setStatus('current')
zxr10X25LapbFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25LapbStatIfIndex"))
if mibBuilder.loadTexts: zxr10X25LapbFlowEntry.setStatus('current')
zxr10X25LapbFlowBusyDefers = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 1), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowBusyDefers.setStatus('current')
zxr10X25LapbFlowRejOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRejOutPkts.setStatus('current')
zxr10X25LapbFlowRejInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRejInPkts.setStatus('current')
zxr10X25LapbFlowT1Timeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowT1Timeouts.setStatus('current')
zxr10X25LapbFlowRROutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRROutPkts.setStatus('current')
zxr10X25LapbFlowRRInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRRInPkts.setStatus('current')
zxr10X25LapbFlowRNROutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRNROutPkts.setStatus('current')
zxr10X25LapbFlowRNRInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowRNRInPkts.setStatus('current')
zxr10X25LapbFlowIOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowIOutPkts.setStatus('current')
zxr10X25LapbFlowIInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowIInPkts.setStatus('current')
zxr10X25LapbFlowDMOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowDMOutPkts.setStatus('current')
zxr10X25LapbFlowDMInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowDMInPkts.setStatus('current')
zxr10X25LapbFlowSABOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 13), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowSABOutPkts.setStatus('current')
zxr10X25LapbFlowSABInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 14), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowSABInPkts.setStatus('current')
zxr10X25LapbFlowUAOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowUAOutPkts.setStatus('current')
zxr10X25LapbFlowUAInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 16), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowUAInPkts.setStatus('current')
zxr10X25LapbFlowDISCOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 17), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowDISCOutPkts.setStatus('current')
zxr10X25LapbFlowDISCInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 18), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowDISCInPkts.setStatus('current')
zxr10X25LapbFlowFRMROutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 19), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowFRMROutPkts.setStatus('current')
zxr10X25LapbFlowFRMRInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 20), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowFRMRInPkts.setStatus('current')
zxr10X25LapbFlowOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 21), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowOutPkts.setStatus('current')
zxr10X25LapbFlowInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 22), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowInPkts.setStatus('current')
zxr10X25LapbFlowStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 23), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbFlowStateChanges.setStatus('current')
zxr10X25LapbStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 8, 1, 24), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25LapbStatIfIndex.setStatus('current')
zxr10X25StatTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9), )
if mibBuilder.loadTexts: zxr10X25StatTable.setStatus('current')
zxr10X25StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25StatLapbIndex"))
if mibBuilder.loadTexts: zxr10X25StatEntry.setStatus('current')
zxr10X25StatLapbIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25StatLapbIndex.setStatus('current')
zxr10StatRecvX25CALLREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25CALLREQUESTCnt.setStatus('current')
zxr10StatRecvX25CALLACCEPTEDCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25CALLACCEPTEDCnt.setStatus('current')
zxr10StatRecvX25CLEARREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25CLEARREQUESTCnt.setStatus('current')
zxr10StatRecvX25CLEARCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25CLEARCONFIRMATIONCnt.setStatus('current')
zxr10StatRecvX25DATACnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25DATACnt.setStatus('current')
zxr10StatRecvX25INTERRUPTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25INTERRUPTCnt.setStatus('current')
zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt.setStatus('current')
zxr10StatRecvX25RRCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RRCnt.setStatus('current')
zxr10StatRecvX25RNRCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RNRCnt.setStatus('current')
zxr10StatRecvX25REJCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25REJCnt.setStatus('current')
zxr10StatRecvX25RESETREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RESETREQUESTCnt.setStatus('current')
zxr10StatRecvX25RESETCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RESETCONFIRMATIONCnt.setStatus('current')
zxr10StatRecvX25REGISTRATIONREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25REGISTRATIONREQUESTCnt.setStatus('current')
zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt.setStatus('current')
zxr10StatRecvX25RESTARTREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RESTARTREQUESTCnt.setStatus('current')
zxr10StatRecvX25RESTARTCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25RESTARTCONFIRMATIONCnt.setStatus('current')
zxr10StatRecvX25DIAGNOSTICCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25DIAGNOSTICCnt.setStatus('current')
zxr10StatRecvX25ILLEGALCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25ILLEGALCnt.setStatus('current')
zxr10StatRecvX25TotalDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatRecvX25TotalDataSize.setStatus('current')
zxr10StatSendX25CALLREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25CALLREQUESTCnt.setStatus('current')
zxr10StatSendX25CALLACCEPTEDCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25CALLACCEPTEDCnt.setStatus('current')
zxr10StatSendX25CLEARREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25CLEARREQUESTCnt.setStatus('current')
zxr10StatSendX25CLEARCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25CLEARCONFIRMATIONCnt.setStatus('current')
zxr10StatSendX25DATACnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25DATACnt.setStatus('current')
zxr10StatSendX25INTERRUPTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25INTERRUPTCnt.setStatus('current')
zxr10StatSendX25INTERRUPTCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25INTERRUPTCONFIRMATIONCnt.setStatus('current')
zxr10StatSendX25RRCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RRCnt.setStatus('current')
zxr10StatSendX25RNRCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 29), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RNRCnt.setStatus('current')
zxr10StatSendX25REJCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 30), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25REJCnt.setStatus('current')
zxr10StatSendX25RESETREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 31), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RESETREQUESTCnt.setStatus('current')
zxr10StatSendX25RESETCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 32), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RESETCONFIRMATIONCnt.setStatus('current')
zxr10StatSendX25REGISTRATIONREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25REGISTRATIONREQUESTCnt.setStatus('current')
zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 34), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt.setStatus('current')
zxr10StatSendX25RESTARTREQUESTCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 35), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RESTARTREQUESTCnt.setStatus('current')
zxr10StatSendX25RESTARTCONFIRMATIONCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 36), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25RESTARTCONFIRMATIONCnt.setStatus('current')
zxr10StatSendX25DIAGNOSTICCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 37), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25DIAGNOSTICCnt.setStatus('current')
zxr10StatSendX25ILLEGALCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 38), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25ILLEGALCnt.setStatus('current')
zxr10StatSendX25TotalDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 9, 1, 39), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StatSendX25TotalDataSize.setStatus('current')
zxr10X25UserAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10), )
if mibBuilder.loadTexts: zxr10X25UserAddrTable.setStatus('current')
zxr10X25UserAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25UserIfIndex"))
if mibBuilder.loadTexts: zxr10X25UserAddrEntry.setStatus('current')
zxr10X25UserX121Address = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25UserX121Address.setStatus('current')
zxr10X25UserIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25UserIfIndex.setStatus('current')
zxr10X25UserIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25UserIfName.setStatus('current')
zxr10X25UserQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("high", 1), ("medium", 2), ("low", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25UserQoS.setStatus('current')
zxr10X25UserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 10, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25UserRowStatus.setStatus('current')
zxr10X25TrunkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11), )
if mibBuilder.loadTexts: zxr10X25TrunkTable.setStatus('current')
zxr10X25TrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1), ).setIndexNames((0, "ZXR10-X25-II-MIB", "zxr10X25TrunkIfIndex"), (0, "ZXR10-X25-II-MIB", "zxr10X25TrunkX121Address"))
if mibBuilder.loadTexts: zxr10X25TrunkEntry.setStatus('current')
zxr10X25TrunkX121Address = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25TrunkX121Address.setStatus('current')
zxr10X25TrunkIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25TrunkIfName.setStatus('current')
zxr10X25TrunkQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("first-select-trunk", 1), ("second-select-trunk", 2), ("third-select-trunk", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25TrunkQoS.setStatus('current')
zxr10X25TrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25TrunkRowStatus.setStatus('current')
zxr10X25TrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 11, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10X25TrunkIfIndex.setStatus('current')
zxr10X25StationAddress = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25StationAddress.setStatus('current')
zxr10X25DefaultTrunk = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 4001, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10X25DefaultTrunk.setStatus('current')
mibBuilder.exportSymbols("ZXR10-X25-II-MIB", zxr10StatRecvX25RESTARTREQUESTCnt=zxr10StatRecvX25RESTARTREQUESTCnt, zxr10StatSendX25REGISTRATIONREQUESTCnt=zxr10StatSendX25REGISTRATIONREQUESTCnt, zxr10StatSendX25DIAGNOSTICCnt=zxr10StatSendX25DIAGNOSTICCnt, zxr10StatSendX25REJCnt=zxr10StatSendX25REJCnt, zxr10X25TrunkIfIndex=zxr10X25TrunkIfIndex, zxr10X25OperLapbPktT23=zxr10X25OperLapbPktT23, zxr10X25LapbFlowSABInPkts=zxr10X25LapbFlowSABInPkts, zxr10X25MIBII=zxr10X25MIBII, zxr10X25PVCTable=zxr10X25PVCTable, zxr10X25SVCNextLcn=zxr10X25SVCNextLcn, zxr10X25LapbFlowRRInPkts=zxr10X25LapbFlowRRInPkts, zxr10X25PVCStartLcn=zxr10X25PVCStartLcn, zxr10StatSendX25RESETREQUESTCnt=zxr10StatSendX25RESETREQUESTCnt, zxr10X25OperLapbPktSvcIdleTime=zxr10X25OperLapbPktSvcIdleTime, zxr10StatSendX25ILLEGALCnt=zxr10StatSendX25ILLEGALCnt, zxr10X25PVCNextPortName=zxr10X25PVCNextPortName, zxr10X25LapbFlowFRMRInPkts=zxr10X25LapbFlowFRMRInPkts, zxr10X25LapbFlowT1Timeouts=zxr10X25LapbFlowT1Timeouts, zxr10StatRecvX25TotalDataSize=zxr10StatRecvX25TotalDataSize, zxr10X25LapbFlowDMOutPkts=zxr10X25LapbFlowDMOutPkts, zxr10StatRecvX25CLEARREQUESTCnt=zxr10StatRecvX25CLEARREQUESTCnt, zxr10X25OperLapbPktT22=zxr10X25OperLapbPktT22, zxr10StatSendX25DATACnt=zxr10StatSendX25DATACnt, zxr10X25LapbFlowEntry=zxr10X25LapbFlowEntry, zxr10X25OperTable=zxr10X25OperTable, zxr10X25UserQoS=zxr10X25UserQoS, zxr10X25LapbFlowRROutPkts=zxr10X25LapbFlowRROutPkts, zxr10X25SVCStartPortName=zxr10X25SVCStartPortName, zxr10X25II=zxr10X25II, X25Address=X25Address, zxr10X25SVCStartLcn=zxr10X25SVCStartLcn, zxr10StatRecvX25REJCnt=zxr10StatRecvX25REJCnt, zxr10StatRecvX25ILLEGALCnt=zxr10StatRecvX25ILLEGALCnt, zxr10X25OperLapbDteDce=zxr10X25OperLapbDteDce, zxr10X25OperLapbMode=zxr10X25OperLapbMode, zxr10X25OperLapbPSSize=zxr10X25OperLapbPSSize, zxr10X25LapbFlowRNRInPkts=zxr10X25LapbFlowRNRInPkts, zxr10X25OperEntry=zxr10X25OperEntry, zxr10X25LapbFlowOutPkts=zxr10X25LapbFlowOutPkts, zxr10X25LapbFlowDMInPkts=zxr10X25LapbFlowDMInPkts, zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt=zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt, zxr10X25UserRowStatus=zxr10X25UserRowStatus, zxr10StatRecvX25RESTARTCONFIRMATIONCnt=zxr10StatRecvX25RESTARTCONFIRMATIONCnt, zxr10X25LapbFlowRejInPkts=zxr10X25LapbFlowRejInPkts, zxr10X25LapbFlowStateChanges=zxr10X25LapbFlowStateChanges, zxr10StatRecvX25RNRCnt=zxr10StatRecvX25RNRCnt, zxr10StatRecvX25REGISTRATIONREQUESTCnt=zxr10StatRecvX25REGISTRATIONREQUESTCnt, UChar=UChar, zxr10X25OperLapbWinSize=zxr10X25OperLapbWinSize, UCHAR=UCHAR, zxr10X25UserAddrTable=zxr10X25UserAddrTable, zxr10StatSendX25TotalDataSize=zxr10StatSendX25TotalDataSize, zxr10StatRecvX25RRCnt=zxr10StatRecvX25RRCnt, zxr10X25OperInterfaceType=zxr10X25OperInterfaceType, zxr10X25UserIfName=zxr10X25UserIfName, zxr10X25LapbFlowInPkts=zxr10X25LapbFlowInPkts, zxr10StatRecvX25RESETCONFIRMATIONCnt=zxr10StatRecvX25RESETCONFIRMATIONCnt, zxr10X25UserX121Address=zxr10X25UserX121Address, zxr10StatSendX25CLEARCONFIRMATIONCnt=zxr10StatSendX25CLEARCONFIRMATIONCnt, zxr10X25OperLapbPktT21=zxr10X25OperLapbPktT21, zxr10X25SVCNo=zxr10X25SVCNo, zxr10=zxr10, zxr10X25StatLapbIndex=zxr10X25StatLapbIndex, zxr10StatRecvX25INTERRUPTCnt=zxr10StatRecvX25INTERRUPTCnt, zxr10X25TrunkTable=zxr10X25TrunkTable, zxr10X25UserIfIndex=zxr10X25UserIfIndex, zxr10StatSendX25CLEARREQUESTCnt=zxr10StatSendX25CLEARREQUESTCnt, zxr10X25OperIfIndex=zxr10X25OperIfIndex, zxr10StatSendX25RESETCONFIRMATIONCnt=zxr10StatSendX25RESETCONFIRMATIONCnt, zxr10StatSendX25RESTARTREQUESTCnt=zxr10StatSendX25RESTARTREQUESTCnt, zxr10X25TrunkIfName=zxr10X25TrunkIfName, zxr10X25OperLapbPktMaxVC=zxr10X25OperLapbPktMaxVC, zxr10X25LapbFlowIOutPkts=zxr10X25LapbFlowIOutPkts, zxr10X25PVCStartPortName=zxr10X25PVCStartPortName, zxr10X25SVCTable=zxr10X25SVCTable, zxr10StatSendX25INTERRUPTCnt=zxr10StatSendX25INTERRUPTCnt, zxr10X25LapbFlowDISCOutPkts=zxr10X25LapbFlowDISCOutPkts, zxr10X25OperLapbPktPSize=zxr10X25OperLapbPktPSize, zxr10StatRecvX25CALLACCEPTEDCnt=zxr10StatRecvX25CALLACCEPTEDCnt, zxr10X25PVCRowStatus=zxr10X25PVCRowStatus, zxr10X25LapbFlowFRMROutPkts=zxr10X25LapbFlowFRMROutPkts, DisplayString=DisplayString, zxr10X25TrunkQoS=zxr10X25TrunkQoS, zxr10X25TrunkRowStatus=zxr10X25TrunkRowStatus, zxr10X25OperIfName=zxr10X25OperIfName, zxr10X25OperLapbRetranCount=zxr10X25OperLapbRetranCount, zxr10X25OperLabpStatus=zxr10X25OperLabpStatus, zxr10X25SVCNextPortIfIndex=zxr10X25SVCNextPortIfIndex, zxr10X25StatTable=zxr10X25StatTable, zxr10X25StationAddress=zxr10X25StationAddress, zxr10X25PVCStartPortIfIndex=zxr10X25PVCStartPortIfIndex, zxr10X25OperLapbTimeoutT3=zxr10X25OperLapbTimeoutT3, zxr10X25LapbFlowRejOutPkts=zxr10X25LapbFlowRejOutPkts, UShort=UShort, zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt=zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt, zxr10StatRecvX25DATACnt=zxr10StatRecvX25DATACnt, zxr10X25PVCNextPortIfIndex=zxr10X25PVCNextPortIfIndex, zxr10X25OperLapbTimeoutT2=zxr10X25OperLapbTimeoutT2, zxr10X25SVCEntry=zxr10X25SVCEntry, zxr10X25OperLapbPktWinSize=zxr10X25OperLapbPktWinSize, zxr10X25LapbStatIfIndex=zxr10X25LapbStatIfIndex, zxr10X25OperLapbUserOrTrunk=zxr10X25OperLapbUserOrTrunk, zxr10X25PVCEntry=zxr10X25PVCEntry, zxr10StatSendX25RESTARTCONFIRMATIONCnt=zxr10StatSendX25RESTARTCONFIRMATIONCnt, zxr10StatSendX25CALLREQUESTCnt=zxr10StatSendX25CALLREQUESTCnt, zxr10X25SVCNextPortName=zxr10X25SVCNextPortName, zxr10X25TrunkEntry=zxr10X25TrunkEntry, zxr10StatSendX25CALLACCEPTEDCnt=zxr10StatSendX25CALLACCEPTEDCnt, zxr10X25LapbFlowSABOutPkts=zxr10X25LapbFlowSABOutPkts, zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt=zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt, zxr10StatSendX25RNRCnt=zxr10StatSendX25RNRCnt, zxr10X25LapbFlowBusyDefers=zxr10X25LapbFlowBusyDefers, zxr10X25LapbFlowUAInPkts=zxr10X25LapbFlowUAInPkts, zxr10X25LapbFlowRNROutPkts=zxr10X25LapbFlowRNROutPkts, zxr10X25StatEntry=zxr10X25StatEntry, zxr10X25TrunkX121Address=zxr10X25TrunkX121Address, zxr10StatSendX25RRCnt=zxr10StatSendX25RRCnt, zxr10StatRecvX25DIAGNOSTICCnt=zxr10StatRecvX25DIAGNOSTICCnt, zxr10X25LapbFlowUAOutPkts=zxr10X25LapbFlowUAOutPkts, zxr10StatRecvX25CLEARCONFIRMATIONCnt=zxr10StatRecvX25CLEARCONFIRMATIONCnt, zxr10X25LapbFlowTable=zxr10X25LapbFlowTable, zxr10StatRecvX25RESETREQUESTCnt=zxr10StatRecvX25RESETREQUESTCnt, zxr10StatSendX25INTERRUPTCONFIRMATIONCnt=zxr10StatSendX25INTERRUPTCONFIRMATIONCnt, zxr10X25UserAddrEntry=zxr10X25UserAddrEntry, zxr10X25DefaultTrunk=zxr10X25DefaultTrunk, zxr10X25SVCStartPortIfIndex=zxr10X25SVCStartPortIfIndex, zxr10X25PVCNo=zxr10X25PVCNo, zxr10X25PVCNextLcn=zxr10X25PVCNextLcn, zxr10X25OperStatus=zxr10X25OperStatus, zte=zte, zxr10X25OperLapbPktT20=zxr10X25OperLapbPktT20, zxr10X25LapbFlowDISCInPkts=zxr10X25LapbFlowDISCInPkts, zxr10X25OperLapbTimeoutT1=zxr10X25OperLapbTimeoutT1, zxr10X25LapbFlowIInPkts=zxr10X25LapbFlowIInPkts, zxr10StatRecvX25CALLREQUESTCnt=zxr10StatRecvX25CALLREQUESTCnt)

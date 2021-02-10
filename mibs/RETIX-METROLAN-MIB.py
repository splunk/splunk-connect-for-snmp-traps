#
# PySNMP MIB module RETIX-METROLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RETIX-METROLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
DisplayString, = mibBuilder.importSymbols("RFC1155-SMI", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, TimeTicks, Bits, iso, NotificationType, ModuleIdentity, Integer32, Unsigned32, enterprises, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, mib_2, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "TimeTicks", "Bits", "iso", "NotificationType", "ModuleIdentity", "Integer32", "Unsigned32", "enterprises", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "mib-2", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
retix = MibIdentifier((1, 3, 6, 1, 4, 1, 72))
metroLanDS3ATM = MibIdentifier((1, 3, 6, 1, 2, 1, 37))
metroLanSS = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20))
atmBandwithGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1))
atmLogicalPort = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 2))
ds3FrameDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3))
ssUnitProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 1))
ssBaseUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 2))
ssStakBus = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 3))
ssVirtualLan = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 4))
ssSlip = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 5))
atmBWGBandwidth = MibScalar((1, 3, 6, 1, 2, 1, 37, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmBWGBandwidth.setStatus('mandatory')
atmBWGConfig = MibScalar((1, 3, 6, 1, 2, 1, 37, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("go", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: atmBWGConfig.setStatus('mandatory')
atmRX_VCI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(35, 1023))).setLabel("atmRX-VCI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRX_VCI.setStatus('mandatory')
atmRX_VPI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setLabel("atmRX-VPI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRX_VPI.setStatus('mandatory')
atmTX_VCI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(35, 1023))).setLabel("atmTX-VCI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmTX_VCI.setStatus('mandatory')
atmTX_VPI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setLabel("atmTX-VPI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmTX_VPI.setStatus('mandatory')
atmBWG = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmBWG.setStatus('mandatory')
atmEncaps = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 7))).clone(namedValues=NamedValues(("vcBridged8023", 2), ("llcEncaps", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmEncaps.setStatus('mandatory')
atmPortConfig = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortConfig.setStatus('mandatory')
ds3NoSignalCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3NoSignalCntr.setStatus('mandatory')
ds3NoDS3FrameCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3NoDS3FrameCntr.setStatus('mandatory')
ds3AISDetectCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AISDetectCntr.setStatus('mandatory')
ds3YellowAlarmCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3YellowAlarmCntr.setStatus('mandatory')
ds3FErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FErrCntr.setStatus('mandatory')
ds3PErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PErrCntr.setStatus('mandatory')
ds3CPErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CPErrCntr.setStatus('mandatory')
ds3FEBlockErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FEBlockErrCntr.setStatus('mandatory')
ds3BPVErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3BPVErrCntr.setStatus('mandatory')
ds3ATMOCD = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ATMOCD.setStatus('mandatory')
ds3FIFOOverflow = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FIFOOverflow.setStatus('mandatory')
ds3RAI = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3RAI.setStatus('mandatory')
ds3RAICntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3RAICntr.setStatus('mandatory')
ds3SignalLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3SignalLoss.setStatus('mandatory')
ds3FrameLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FrameLoss.setStatus('mandatory')
ds3SyncLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3SyncLoss.setStatus('mandatory')
ds3YellowAlarm = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3YellowAlarm.setStatus('mandatory')
ds3AISDetect = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AISDetect.setStatus('mandatory')
ds3ClearErrorCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("set", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: ds3ClearErrorCntr.setStatus('mandatory')
ds3GFCInsertion = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3GFCInsertion.setStatus('mandatory')
ds3BipolarSerialIO = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3BipolarSerialIO.setStatus('mandatory')
ds3PayloadScrambling = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PayloadScrambling.setStatus('mandatory')
ds3PLCPOverheadProc = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PLCPOverheadProc.setStatus('mandatory')
ds3FEBEGeneration = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3FEBEGeneration.setStatus('mandatory')
ds3LoopBack = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LoopBack.setStatus('mandatory')
ds3FEACGenNDetect = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3FEACGenNDetect.setStatus('mandatory')
ds3RcvEQ = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3RcvEQ.setStatus('mandatory')
ds3XmitLevel = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3XmitLevel.setStatus('mandatory')
ssBaseModule = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseModule.setStatus('mandatory')
ssIO1Module = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vacant", 1), ("pcnet-6-card-id", 2), ("feast-card-id", 3), ("stakBus-card-id", 4), ("atm-card-id", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIO1Module.setStatus('mandatory')
ssIO2Module = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vacant", 1), ("pcnet-6-card-id", 2), ("feast-card-id", 3), ("stakBus-card-id", 4), ("atm-card-id", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIO2Module.setStatus('mandatory')
ssBaseBootFWVer = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseBootFWVer.setStatus('mandatory')
ssBaseSoftVer = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseSoftVer.setStatus('mandatory')
ssErrorLog = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssErrorLog.setStatus('mandatory')
ssStkBusIOPort = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on-IO1", 1), ("on-IO2", 2), ("not-installed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusIOPort.setStatus('mandatory')
ssStkBusSpeed = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusSpeed.setStatus('mandatory')
ssStkBusNodeAddr = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusNodeAddr.setStatus('mandatory')
ssStkBusRingOp = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ringOperational", 1), ("ringNotOperational", 2), ("notInstalled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusRingOp.setStatus('mandatory')
ssVLANEnDisable = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEnDisable.setStatus('mandatory')
portVLANTable = MibTable((1, 3, 6, 1, 4, 1, 72, 20, 4, 2), )
if mibBuilder.loadTexts: portVLANTable.setStatus('mandatory')
portVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1), ).setIndexNames((0, "RETIX-METROLAN-MIB", "ssVLANEntryPortID"), (0, "RETIX-METROLAN-MIB", "ssVLANEntryVLANID"))
if mibBuilder.loadTexts: portVLANEntry.setStatus('mandatory')
ssVLANEntryPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryPortID.setStatus('mandatory')
ssVLANEntryVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryVLANID.setStatus('mandatory')
ssVLANEntryEdit = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable-add", 1), ("disable", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryEdit.setStatus('mandatory')
slipEnable = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slipEnable.setStatus('mandatory')
slipHostIP = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 5, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slipHostIP.setStatus('mandatory')
mibBuilder.exportSymbols("RETIX-METROLAN-MIB", atmRX_VPI=atmRX_VPI, ds3FrameDevice=ds3FrameDevice, ssBaseBootFWVer=ssBaseBootFWVer, ssStkBusSpeed=ssStkBusSpeed, ssVLANEntryEdit=ssVLANEntryEdit, atmTX_VCI=atmTX_VCI, ds3GFCInsertion=ds3GFCInsertion, ds3BipolarSerialIO=ds3BipolarSerialIO, ds3PErrCntr=ds3PErrCntr, ds3YellowAlarm=ds3YellowAlarm, atmEncaps=atmEncaps, atmBandwithGroup=atmBandwithGroup, atmPortConfig=atmPortConfig, ssIO2Module=ssIO2Module, atmRX_VCI=atmRX_VCI, portVLANTable=portVLANTable, ds3SyncLoss=ds3SyncLoss, ds3BPVErrCntr=ds3BPVErrCntr, slipHostIP=slipHostIP, ds3RAI=ds3RAI, ds3AISDetect=ds3AISDetect, ds3RcvEQ=ds3RcvEQ, metroLanDS3ATM=metroLanDS3ATM, atmBWGConfig=atmBWGConfig, portVLANEntry=portVLANEntry, ssBaseSoftVer=ssBaseSoftVer, ssVLANEntryPortID=ssVLANEntryPortID, ssBaseUnit=ssBaseUnit, ds3NoDS3FrameCntr=ds3NoDS3FrameCntr, ds3PayloadScrambling=ds3PayloadScrambling, ds3XmitLevel=ds3XmitLevel, ds3FEBlockErrCntr=ds3FEBlockErrCntr, ds3FErrCntr=ds3FErrCntr, ds3ATMOCD=ds3ATMOCD, ds3ClearErrorCntr=ds3ClearErrorCntr, ds3PLCPOverheadProc=ds3PLCPOverheadProc, metroLanSS=metroLanSS, ds3RAICntr=ds3RAICntr, ds3AISDetectCntr=ds3AISDetectCntr, ssBaseModule=ssBaseModule, ssErrorLog=ssErrorLog, atmLogicalPort=atmLogicalPort, ssSlip=ssSlip, ssStkBusNodeAddr=ssStkBusNodeAddr, ssStkBusRingOp=ssStkBusRingOp, ssIO1Module=ssIO1Module, ssUnitProfile=ssUnitProfile, ssStkBusIOPort=ssStkBusIOPort, ds3FEACGenNDetect=ds3FEACGenNDetect, ssVLANEnDisable=ssVLANEnDisable, atmTX_VPI=atmTX_VPI, atmBWGBandwidth=atmBWGBandwidth, ds3FIFOOverflow=ds3FIFOOverflow, ds3SignalLoss=ds3SignalLoss, ssVirtualLan=ssVirtualLan, ds3NoSignalCntr=ds3NoSignalCntr, ds3YellowAlarmCntr=ds3YellowAlarmCntr, ssVLANEntryVLANID=ssVLANEntryVLANID, slipEnable=slipEnable, ds3FrameLoss=ds3FrameLoss, retix=retix, ds3LoopBack=ds3LoopBack, ds3CPErrCntr=ds3CPErrCntr, atmBWG=atmBWG, ssStakBus=ssStakBus, ds3FEBEGeneration=ds3FEBEGeneration)

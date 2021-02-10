#
# PySNMP MIB module ASTERISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASTERISK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
digium, = mibBuilder.importSymbols("DIGIUM-MIB", "digium")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, IpAddress, ModuleIdentity, Bits, Counter64, ObjectIdentity, iso, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
asterisk = ModuleIdentity((1, 3, 6, 1, 4, 1, 22736, 1))
asterisk.setRevisions(('2008-06-20 20:25', '2007-08-21 14:50', '2006-03-06 18:40', '2006-02-04 19:00',))
if mibBuilder.loadTexts: asterisk.setLastUpdated('200806202025Z')
if mibBuilder.loadTexts: asterisk.setOrganization('Digium, Inc.')
asteriskVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 1))
asteriskConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 2))
asteriskModules = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 3))
asteriskIndications = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 4))
asteriskChannels = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 5))
astVersionString = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astVersionString.setStatus('current')
astVersionTag = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astVersionTag.setStatus('current')
astConfigUpTime = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigUpTime.setStatus('current')
astConfigReloadTime = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigReloadTime.setStatus('current')
astConfigPid = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigPid.setStatus('current')
astConfigSocket = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigSocket.setStatus('current')
astConfigCallsActive = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigCallsActive.setStatus('current')
astConfigCallsProcessed = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigCallsProcessed.setStatus('current')
astNumModules = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumModules.setStatus('current')
astNumIndications = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumIndications.setStatus('current')
astCurrentIndication = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astCurrentIndication.setStatus('current')
astIndicationsTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3), )
if mibBuilder.loadTexts: astIndicationsTable.setStatus('current')
astIndicationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1), ).setIndexNames((0, "ASTERISK-MIB", "astIndIndex"))
if mibBuilder.loadTexts: astIndicationsEntry.setStatus('current')
astIndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndIndex.setStatus('current')
astIndCountry = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndCountry.setStatus('current')
astIndAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndAlias.setStatus('current')
astIndDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndDescription.setStatus('current')
astNumChannels = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChannels.setStatus('current')
astChanTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2), )
if mibBuilder.loadTexts: astChanTable.setStatus('current')
astChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1), ).setIndexNames((0, "ASTERISK-MIB", "astChanIndex"))
if mibBuilder.loadTexts: astChanEntry.setStatus('current')
astChanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanIndex.setStatus('current')
astChanName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanName.setStatus('current')
astChanLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanLanguage.setStatus('current')
astChanType = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanType.setStatus('current')
astChanMusicClass = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMusicClass.setStatus('current')
astChanBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanBridge.setStatus('current')
astChanMasq = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMasq.setStatus('current')
astChanMasqr = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMasqr.setStatus('current')
astChanWhenHangup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanWhenHangup.setStatus('current')
astChanApp = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanApp.setStatus('current')
astChanData = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanData.setStatus('current')
astChanContext = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanContext.setStatus('current')
astChanMacroContext = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroContext.setStatus('current')
astChanMacroExten = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroExten.setStatus('current')
astChanMacroPri = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroPri.setStatus('current')
astChanExten = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanExten.setStatus('current')
astChanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanPri.setStatus('current')
astChanAccountCode = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanAccountCode.setStatus('current')
astChanForwardTo = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanForwardTo.setStatus('current')
astChanUniqueId = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanUniqueId.setStatus('current')
astChanCallGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCallGroup.setStatus('current')
astChanPickupGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanPickupGroup.setStatus('current')
astChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("stateDown", 0), ("stateReserved", 1), ("stateOffHook", 2), ("stateDialing", 3), ("stateRing", 4), ("stateRinging", 5), ("stateUp", 6), ("stateBusy", 7), ("stateDialingOffHook", 8), ("statePreRing", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanState.setStatus('current')
astChanMuted = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMuted.setStatus('current')
astChanRings = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanRings.setStatus('current')
astChanCidDNID = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidDNID.setStatus('current')
astChanCidNum = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidNum.setStatus('current')
astChanCidName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidName.setStatus('current')
astChanCidANI = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidANI.setStatus('current')
astChanCidRDNIS = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidRDNIS.setStatus('current')
astChanCidPresentation = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidPresentation.setStatus('current')
astChanCidANI2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidANI2.setStatus('current')
astChanCidTON = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidTON.setStatus('current')
astChanCidTNS = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidTNS.setStatus('current')
astChanAMAFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("default", 0), ("omit", 1), ("billing", 2), ("documentation", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanAMAFlags.setStatus('current')
astChanADSI = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("available", 1), ("unavailable", 2), ("offHookOnly", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanADSI.setStatus('current')
astChanToneZone = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanToneZone.setStatus('current')
astChanHangupCause = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 16, 17, 19, 34, 38, 66))).clone(namedValues=NamedValues(("notDefined", 0), ("unregistered", 3), ("normal", 16), ("busy", 17), ("noAnswer", 19), ("congestion", 34), ("failure", 38), ("noSuchDriver", 66)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanHangupCause.setStatus('current')
astChanVariables = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanVariables.setStatus('current')
astChanFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 40), Bits().clone(namedValues=NamedValues(("wantsJitter", 0), ("deferDTMF", 1), ("writeInterrupt", 2), ("blocking", 3), ("zombie", 4), ("exception", 5), ("musicOnHold", 6), ("spying", 7), ("nativeBridge", 8), ("autoIncrementingLoop", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanFlags.setStatus('current')
astChanTransferCap = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8, 9, 16, 17, 24))).clone(namedValues=NamedValues(("speech", 0), ("digital", 8), ("restrictedDigital", 9), ("audio3k", 16), ("digitalWithTones", 17), ("video", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTransferCap.setStatus('current')
astNumChanTypes = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChanTypes.setStatus('current')
astChanTypeTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4), )
if mibBuilder.loadTexts: astChanTypeTable.setStatus('current')
astChanTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1), ).setIndexNames((0, "ASTERISK-MIB", "astChanTypeIndex"))
if mibBuilder.loadTexts: astChanTypeEntry.setStatus('current')
astChanTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeIndex.setStatus('current')
astChanTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeName.setStatus('current')
astChanTypeDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeDesc.setStatus('current')
astChanTypeDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeDeviceState.setStatus('current')
astChanTypeIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeIndications.setStatus('current')
astChanTypeTransfer = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeTransfer.setStatus('current')
astChanTypeChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeChannels.setStatus('current')
astChanScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 5, 5))
astNumChanBridge = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChanBridge.setStatus('current')
mibBuilder.exportSymbols("ASTERISK-MIB", astChanMusicClass=astChanMusicClass, astChanCidTON=astChanCidTON, astNumIndications=astNumIndications, astChanTypeDesc=astChanTypeDesc, astChanBridge=astChanBridge, astChanWhenHangup=astChanWhenHangup, astChanCidName=astChanCidName, astIndicationsTable=astIndicationsTable, astChanCidPresentation=astChanCidPresentation, astChanAccountCode=astChanAccountCode, astChanTypeIndications=astChanTypeIndications, astNumChanBridge=astNumChanBridge, astChanTransferCap=astChanTransferCap, astChanTypeName=astChanTypeName, astChanTypeTransfer=astChanTypeTransfer, PYSNMP_MODULE_ID=asterisk, astChanMasq=astChanMasq, astChanLanguage=astChanLanguage, astNumChannels=astNumChannels, asteriskConfiguration=asteriskConfiguration, asterisk=asterisk, astChanExten=astChanExten, astChanTable=astChanTable, asteriskVersion=asteriskVersion, astChanPri=astChanPri, astChanTypeChannels=astChanTypeChannels, astConfigCallsActive=astConfigCallsActive, astChanName=astChanName, astCurrentIndication=astCurrentIndication, asteriskIndications=asteriskIndications, astChanPickupGroup=astChanPickupGroup, astChanToneZone=astChanToneZone, astChanCallGroup=astChanCallGroup, astChanState=astChanState, astConfigUpTime=astConfigUpTime, astIndIndex=astIndIndex, astChanHangupCause=astChanHangupCause, astChanTypeIndex=astChanTypeIndex, astChanContext=astChanContext, astChanData=astChanData, astIndAlias=astIndAlias, astNumModules=astNumModules, astChanScalars=astChanScalars, asteriskModules=asteriskModules, astChanMuted=astChanMuted, astChanCidRDNIS=astChanCidRDNIS, astChanMacroContext=astChanMacroContext, asteriskChannels=asteriskChannels, astChanCidTNS=astChanCidTNS, astChanApp=astChanApp, astChanTypeTable=astChanTypeTable, astChanCidANI2=astChanCidANI2, astChanFlags=astChanFlags, astChanType=astChanType, astChanIndex=astChanIndex, astIndCountry=astIndCountry, astConfigCallsProcessed=astConfigCallsProcessed, astChanRings=astChanRings, astChanTypeDeviceState=astChanTypeDeviceState, astChanEntry=astChanEntry, astChanAMAFlags=astChanAMAFlags, astVersionTag=astVersionTag, astChanCidDNID=astChanCidDNID, astVersionString=astVersionString, astChanUniqueId=astChanUniqueId, astChanCidNum=astChanCidNum, astChanMacroPri=astChanMacroPri, astNumChanTypes=astNumChanTypes, astChanForwardTo=astChanForwardTo, astConfigSocket=astConfigSocket, astConfigPid=astConfigPid, astChanCidANI=astChanCidANI, astChanVariables=astChanVariables, astChanADSI=astChanADSI, astChanMacroExten=astChanMacroExten, astChanMasqr=astChanMasqr, astIndDescription=astIndDescription, astIndicationsEntry=astIndicationsEntry, astConfigReloadTime=astConfigReloadTime, astChanTypeEntry=astChanTypeEntry)

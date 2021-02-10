#
# PySNMP MIB module MATIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MATIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:00:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, iso, ObjectIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, Counter64, TimeTicks, MibIdentifier, enterprises, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "iso", "ObjectIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "Counter64", "TimeTicks", "MibIdentifier", "enterprises", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ngcan = MibIdentifier((1, 3, 6, 1, 4, 1, 1978))
tiger = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2))
matipMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7))
matipUser = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2))
matipSession = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3))
matipTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4))
matipUserTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1))
matipSessionTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2))
matipNumUsers = MibScalar((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipNumUsers.setStatus('mandatory')
matipUserTable = MibTable((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2), )
if mibBuilder.loadTexts: matipUserTable.setStatus('mandatory')
matipUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1), ).setIndexNames((0, "MATIP-MIB", "matipUserIndex"))
if mibBuilder.loadTexts: matipUserEntry.setStatus('mandatory')
matipUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserIndex.setStatus('mandatory')
matipUserHLD = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserHLD.setStatus('mandatory')
matipUserA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserA1.setStatus('mandatory')
matipUserA2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserA2.setStatus('mandatory')
matipUserSessionRef = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserSessionRef.setStatus('mandatory')
matipUserCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("paddedbaudot", 1), ("ipars", 2), ("ascii", 3), ("ebcdic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserCoding.setStatus('mandatory')
matipUserPresentationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("p1024b", 1), ("p1024c", 2), ("sna3270", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserPresentationMode.setStatus('mandatory')
matipUserQueueThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserQueueThresholdHi.setStatus('mandatory')
matipUserQueueThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserQueueThresholdLow.setStatus('mandatory')
matipUserStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserStateTime.setStatus('mandatory')
matipUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("closed", 1), ("activated", 2), ("bound", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserStatus.setStatus('mandatory')
matipUserMsgsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserMsgsIn.setStatus('mandatory')
matipUserMsgsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserMsgsOut.setStatus('mandatory')
matipUserCharIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserCharIn.setStatus('mandatory')
matipUserCharOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserCharOut.setStatus('mandatory')
matipUserDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserDisconnects.setStatus('mandatory')
matipUserTrapReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserTrapReason.setStatus('mandatory')
matipUserStateChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("partial", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserStateChangeTrapEnable.setStatus('mandatory')
matipUserStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1) + (0,1)).setObjects(("MATIP-MIB", "matipUserIndex"), ("MATIP-MIB", "matipUserTrapReason"))
matipSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3), )
if mibBuilder.loadTexts: matipSessionTable.setStatus('mandatory')
matipSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1), ).setIndexNames((0, "MATIP-MIB", "matipSessionIndex"))
if mibBuilder.loadTexts: matipSessionEntry.setStatus('mandatory')
matipSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionIndex.setStatus('mandatory')
matipSessionClientServer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("client", 1), ("server", 2), ("both", 3))).clone('client')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionClientServer.setStatus('mandatory')
matipSessionMuxMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hlda1a2", 1), ("a1a2", 2), ("single", 3))).clone('hlda1a2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionMuxMode.setStatus('mandatory')
matipSessionPresentationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("p1024b", 1), ("p1024c", 2), ("sna3270", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionPresentationMode.setStatus('mandatory')
matipSessionCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("paddedbaudot", 1), ("ipars", 2), ("ascii", 3), ("ebcdic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionCoding.setStatus('mandatory')
matipSessionRestartTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionRestartTimer.setStatus('mandatory')
matipSessionDialOnDemand = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionDialOnDemand.setStatus('mandatory')
matipSessionActivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionActivityTimer.setStatus('mandatory')
matipSessionQueueThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionQueueThresholdHi.setStatus('mandatory')
matipSessionQueueThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionQueueThresholdLow.setStatus('mandatory')
matipSessionConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionConnectTime.setStatus('mandatory')
matipSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sessionDown", 1), ("sessionActivated", 2), ("sessionConnected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionStatus.setStatus('mandatory')
matipSessionDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDisconnects.setStatus('mandatory')
matipSessionSOSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSOSent.setStatus('mandatory')
matipSessionSOReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSOReceived.setStatus('mandatory')
matipSessionOCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionOCSent.setStatus('mandatory')
matipSessionOCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionOCReceived.setStatus('mandatory')
matipSessionSCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSCSent.setStatus('mandatory')
matipSessionSCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSCReceived.setStatus('mandatory')
matipSessionDataSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDataSent.setStatus('mandatory')
matipSessionDataReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDataReceived.setStatus('mandatory')
matipSessionStateChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("partial", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionStateChangeTrapEnable.setStatus('mandatory')
matipSessionTrapReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionTrapReason.setStatus('mandatory')
matipSessionStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2) + (0,1)).setObjects(("MATIP-MIB", "matipSessionIndex"), ("MATIP-MIB", "matipSessionTrapReason"))
mibBuilder.exportSymbols("MATIP-MIB", matipSessionDataReceived=matipSessionDataReceived, matipSessionIndex=matipSessionIndex, matipUserIndex=matipUserIndex, matipSessionCoding=matipSessionCoding, matipUserStateChange=matipUserStateChange, matipSessionDataSent=matipSessionDataSent, matipSessionRestartTimer=matipSessionRestartTimer, matipUserCharOut=matipUserCharOut, matipSessionStateChange=matipSessionStateChange, matipUserPresentationMode=matipUserPresentationMode, matipUserA1=matipUserA1, matipSessionTable=matipSessionTable, matipSessionTraps=matipSessionTraps, matipNumUsers=matipNumUsers, matipSessionStateChangeTrapEnable=matipSessionStateChangeTrapEnable, matipSession=matipSession, matipUserEntry=matipUserEntry, matipSessionMuxMode=matipSessionMuxMode, matipUserA2=matipUserA2, tiger=tiger, matipSessionSOReceived=matipSessionSOReceived, matipSessionActivityTimer=matipSessionActivityTimer, matipUserStateTime=matipUserStateTime, matipUserQueueThresholdLow=matipUserQueueThresholdLow, matipSessionClientServer=matipSessionClientServer, matipUserDisconnects=matipUserDisconnects, matipUserCharIn=matipUserCharIn, matipUserTraps=matipUserTraps, matipSessionStatus=matipSessionStatus, matipSessionDisconnects=matipSessionDisconnects, matipSessionEntry=matipSessionEntry, matipSessionConnectTime=matipSessionConnectTime, matipUser=matipUser, matipSessionSOSent=matipSessionSOSent, matipSessionSCSent=matipSessionSCSent, matipUserStatus=matipUserStatus, matipUserMsgsIn=matipUserMsgsIn, matipSessionOCSent=matipSessionOCSent, matipSessionTrapReason=matipSessionTrapReason, matipSessionQueueThresholdLow=matipSessionQueueThresholdLow, matipUserStateChangeTrapEnable=matipUserStateChangeTrapEnable, matipUserMsgsOut=matipUserMsgsOut, matipSessionPresentationMode=matipSessionPresentationMode, matipUserCoding=matipUserCoding, matipTraps=matipTraps, matipSessionQueueThresholdHi=matipSessionQueueThresholdHi, ngcan=ngcan, matipSessionOCReceived=matipSessionOCReceived, matipUserQueueThresholdHi=matipUserQueueThresholdHi, matipSessionSCReceived=matipSessionSCReceived, matipUserTable=matipUserTable, matipUserTrapReason=matipUserTrapReason, matipMIB=matipMIB, matipUserHLD=matipUserHLD, matipUserSessionRef=matipUserSessionRef, matipSessionDialOnDemand=matipSessionDialOnDemand)

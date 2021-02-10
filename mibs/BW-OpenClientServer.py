#
# PySNMP MIB module BW-OpenClientServer (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-OpenClientServer
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, TimeTicks, IpAddress, Unsigned32, ModuleIdentity, Bits, NotificationType, iso, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "TimeTicks", "IpAddress", "Unsigned32", "ModuleIdentity", "Bits", "NotificationType", "iso", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadsoft = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431))
broadsoft.setRevisions(('2005-08-16 10:00', '2000-09-19 14:31',))
if mibBuilder.loadTexts: broadsoft.setLastUpdated('200508161000Z')
if mibBuilder.loadTexts: broadsoft.setOrganization('Broadsoft, Inc')
broadworks = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1))
openClientServer = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8))
protocols = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1))
concurrent = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2))
ocsReserved = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 999))
bwOcsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000))
cap = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1))
oss = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2))
nsoss = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3))
commonComm = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4))
extAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5))
oci = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6))
tcp = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7))
bwOCSCAPRegisterAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPRegisterAuthentications.setStatus('current')
bwOCSCAPResponseAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPResponseAuthentications.setStatus('obsolete')
bwOCSCAPRegisterRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPRegisterRequests.setStatus('obsolete')
bwOCSCAPRegisterResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPRegisterResponses.setStatus('obsolete')
bwOCSCAPUnsuccessfulRegisterResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPUnsuccessfulRegisterResponses.setStatus('current')
bwOCSCAPAcknowledgements = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPAcknowledgements.setStatus('current')
bwOCSCAPUnregisterIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPUnregisterIns.setStatus('current')
bwOCSCAPUnregisterOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPUnregisterOuts.setStatus('current')
bwOCSCAPSessionUpdates = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPSessionUpdates.setStatus('current')
bwOCSCAPProfileUpdates = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPProfileUpdates.setStatus('current')
bwOCSCAPCallUpdates = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPCallUpdates.setStatus('current')
bwOCSCAPCallActions = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPCallActions.setStatus('current')
bwOCSCAPCallControlInfos = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPCallControlInfos.setStatus('current')
bwOCSCAPInfoRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPInfoRequests.setStatus('current')
bwOCSCAPInfoResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 15), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPInfoResponses.setStatus('current')
bwOCSCAPServerStatusRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 16), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPServerStatusRequests.setStatus('current')
bwOCSCAPExternalNotifies = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 17), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPExternalNotifies.setStatus('current')
bwOCSCAPMonitoringUsersRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 18), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPMonitoringUsersRequests.setStatus('current')
bwOCSCAPMonitoringUsersResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 19), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPMonitoringUsersResponses.setStatus('current')
bwOCSCAPStatsQueueUpdatesOut = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 20), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPStatsQueueUpdatesOut.setStatus('current')
bwOCSCAPStatsQueueActionsIn = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 21), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPStatsQueueActionsIn.setStatus('current')
bwOCSCAPStatsDatagramsIn = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 22), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPStatsDatagramsIn.setStatus('current')
bwOCSCAPStatsDatagramsOut = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 23), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPStatsDatagramsOut.setStatus('current')
bwOCSCAPRegisterRequestIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 24), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPRegisterRequestIns.setStatus('current')
bwOCSCAPRegisterRequestOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 25), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPRegisterRequestOuts.setStatus('current')
bwOCSCAPResponseAuthenticationIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 26), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPResponseAuthenticationIns.setStatus('current')
bwOCSCAPResponseAuthenticationOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 27), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCAPResponseAuthenticationOuts.setStatus('current')
bwOCSOSSRequestAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSRequestAuthentications.setStatus('obsolete')
bwOCSOSSResponseAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSResponseAuthentications.setStatus('obsolete')
bwOCSOSSRequestLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSRequestLogins.setStatus('obsolete')
bwOCSOSSResponseLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSResponseLogins.setStatus('obsolete')
bwOCSOSSUnsuccessfulResponseLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSUnsuccessfulResponseLogins.setStatus('obsolete')
bwOCSOSSRequestLogoutIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSRequestLogoutIns.setStatus('obsolete')
bwOCSOSSRequestLogoutOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSRequestLogoutOuts.setStatus('obsolete')
bwOCSOSSRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSRequests.setStatus('obsolete')
bwOCSOSSResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSResponses.setStatus('obsolete')
bwOCSOSSResponseAuthenticationOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSResponseAuthenticationOuts.setStatus('obsolete')
bwOCSOSSResponseAuthenticationIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOSSResponseAuthenticationIns.setStatus('obsolete')
bwOCSNSOSSRequestAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSRequestAuthentications.setStatus('current')
bwOCSNSOSSResponseAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSResponseAuthentications.setStatus('obsolete')
bwOCSNSOSSRequestLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSRequestLogins.setStatus('current')
bwOCSNSOSSResponseLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSResponseLogins.setStatus('current')
bwOCSNSOSSUnsuccessfulResponseLogins = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSUnsuccessfulResponseLogins.setStatus('current')
bwOCSNSOSSRequestLogoutIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSRequestLogoutIns.setStatus('current')
bwOCSNSOSSRequestLogoutOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSRequestLogoutOuts.setStatus('current')
bwOCSNSOSSRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSRequests.setStatus('current')
bwOCSNSOSSResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSResponses.setStatus('current')
bwOCSNSOSSResponseAuthenticationOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSResponseAuthenticationOuts.setStatus('current')
bwOCSNSOSSResponseAuthenticationIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSNSOSSResponseAuthenticationIns.setStatus('current')
bwOCSCommonCommStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1), )
if mibBuilder.loadTexts: bwOCSCommonCommStatsTable.setStatus('current')
bwOCSCommonCommStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1), ).setIndexNames((0, "BW-OpenClientServer", "bwOCSCommonCommStatsIndex"))
if mibBuilder.loadTexts: bwOCSCommonCommStatsEntry.setStatus('current')
bwOCSCommonCommStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSCommonCommStatsIndex.setStatus('current')
bwOCSCommonCommHost = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSCommonCommHost.setStatus('current')
bwOCSCommonCommInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSCommonCommInterface.setStatus('current')
bwOCSCommonCommProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSCommonCommProtocol.setStatus('current')
bwOCSCommonCommAcceptedOutboundConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommAcceptedOutboundConnections.setStatus('current')
bwOCSCommonCommAcceptedInboundConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommAcceptedInboundConnections.setStatus('current')
bwOCSCommonCommRejectedOutboundConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommRejectedOutboundConnections.setStatus('current')
bwOCSCommonCommRejectedInboundConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommRejectedInboundConnections.setStatus('current')
bwOCSCommonCommOutputMessagesProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommOutputMessagesProcessed.setStatus('current')
bwOCSCommonCommInputMessagesProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommInputMessagesProcessed.setStatus('current')
bwOCSCommonCommOutputCommunicationErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommOutputCommunicationErrors.setStatus('current')
bwOCSCommonCommInputCommunicationErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSCommonCommInputCommunicationErrors.setStatus('current')
bwOCSWASAuthenticationAttempts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSWASAuthenticationAttempts.setStatus('current')
bwOCSWASLoginAttempts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSWASLoginAttempts.setStatus('current')
bwOCSWASCommunicationErrors = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSWASCommunicationErrors.setStatus('current')
bwOCSWASProcessingErrors = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSWASProcessingErrors.setStatus('current')
bwOCSOCIAuthenticationRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIAuthenticationRequests.setStatus('current')
bwOCSOCILoginRequestIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCILoginRequestIns.setStatus('current')
bwOCSOCILoginRequestOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCILoginRequestOuts.setStatus('current')
bwOCSOCILoginResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCILoginResponses.setStatus('current')
bwOCSOCIUnsuccessfulLoginResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIUnsuccessfulLoginResponses.setStatus('current')
bwOCSOCILogoutRequestIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCILogoutRequestIns.setStatus('current')
bwOCSOCILogoutRequestOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCILogoutRequestOuts.setStatus('current')
bwOCSOCIRequests = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIRequests.setStatus('current')
bwOCSOCIResponses = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIResponses.setStatus('current')
bwOCSOCIAuthenticationResponseOuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIAuthenticationResponseOuts.setStatus('current')
bwOCSOCIAuthenticationResponseIns = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIAuthenticationResponseIns.setStatus('current')
bwOCSOCIUserIdLoginLevelNotAllowed = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIUserIdLoginLevelNotAllowed.setStatus('current')
bwOCSOCIErrorResponse = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSOCIErrorResponse.setStatus('current')
bwOCSMonitoringExecutorTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1), )
if mibBuilder.loadTexts: bwOCSMonitoringExecutorTable.setStatus('current')
bwOCSMonitoringExecutorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1), ).setIndexNames((0, "BW-OpenClientServer", "bwOCSMonitoringExecutorIndex"))
if mibBuilder.loadTexts: bwOCSMonitoringExecutorEntry.setStatus('current')
bwOCSMonitoringExecutorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorIndex.setStatus('current')
bwOCSMonitoringExecutorName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorName.setStatus('current')
bwOCSMonitoringExecutorCurrentPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorCurrentPoolSize.setStatus('current')
bwOCSMonitoringExecutorMaxPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorMaxPoolSize.setStatus('current')
bwOCSMonitoringExecutorAvgActiveThreads = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorAvgActiveThreads.setStatus('current')
bwOCSMonitoringExecutorTaskQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorTaskQueueSize.setStatus('current')
bwOCSMonitoringExecutorNbTasksRun = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorNbTasksRun.setStatus('current')
bwOCSMonitoringExecutorNbWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorNbWarnings.setStatus('current')
bwOCSMonitoringExecutorNbErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorNbErrors.setStatus('current')
bwOCSMonitoringExecutorLongestTaskMs = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorLongestTaskMs.setStatus('current')
bwOCSMonitoringExecutorLongestTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSMonitoringExecutorLongestTaskName.setStatus('current')
bwOCSTcpServersStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1), )
if mibBuilder.loadTexts: bwOCSTcpServersStatsTable.setStatus('current')
bwOCSTcpServersStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1), ).setIndexNames((0, "BW-OpenClientServer", "bwOCSTcpServersStatsIndex"))
if mibBuilder.loadTexts: bwOCSTcpServersStatsEntry.setStatus('current')
bwOCSTcpServersStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSTcpServersStatsIndex.setStatus('current')
bwOCSTcpServersName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSTcpServersName.setStatus('current')
bwOCSTcpServersNbConnectionsAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbConnectionsAccepted.setStatus('current')
bwOCSTcpServersNbConnectionsRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbConnectionsRefused.setStatus('current')
bwOCSTcpServersNbConnectionsInitiated = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbConnectionsInitiated.setStatus('current')
bwOCSTcpServersNbConnectionsClosed = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbConnectionsClosed.setStatus('current')
bwOCSTcpServersNbBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 7), Gauge32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbBytesSent.setStatus('current')
bwOCSTcpServersNbBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 8), Gauge32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbBytesReceived.setStatus('current')
bwOCSTcpServersOutgoingQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSTcpServersOutgoingQueueSize.setStatus('current')
bwOCSTcpServersIncomingQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSTcpServersIncomingQueueSize.setStatus('current')
bwOCSTcpServersNbBytesSentSecure = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 11), Gauge32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbBytesSentSecure.setStatus('current')
bwOCSTcpServersNbBytesReceivedSecure = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 12), Gauge32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwOCSTcpServersNbBytesReceivedSecure.setStatus('current')
bwOCSReserved = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 8, 999, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOCSReserved.setStatus('obsolete')
bwOcsMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1))
bwOcsMibCompliancy = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 2))
bwOcsCapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 1)).setObjects(("BW-OpenClientServer", "bwOCSCAPRegisterAuthentications"), ("BW-OpenClientServer", "bwOCSCAPResponseAuthentications"), ("BW-OpenClientServer", "bwOCSCAPRegisterRequests"), ("BW-OpenClientServer", "bwOCSCAPUnsuccessfulRegisterResponses"), ("BW-OpenClientServer", "bwOCSCAPAcknowledgements"), ("BW-OpenClientServer", "bwOCSCAPUnregisterIns"), ("BW-OpenClientServer", "bwOCSCAPUnregisterOuts"), ("BW-OpenClientServer", "bwOCSCAPSessionUpdates"), ("BW-OpenClientServer", "bwOCSCAPProfileUpdates"), ("BW-OpenClientServer", "bwOCSCAPCallUpdates"), ("BW-OpenClientServer", "bwOCSCAPCallActions"), ("BW-OpenClientServer", "bwOCSCAPCallControlInfos"), ("BW-OpenClientServer", "bwOCSCAPInfoRequests"), ("BW-OpenClientServer", "bwOCSCAPInfoResponses"), ("BW-OpenClientServer", "bwOCSCAPServerStatusRequests"), ("BW-OpenClientServer", "bwOCSCAPExternalNotifies"), ("BW-OpenClientServer", "bwOCSCAPMonitoringUsersRequests"), ("BW-OpenClientServer", "bwOCSCAPMonitoringUsersResponses"), ("BW-OpenClientServer", "bwOCSCAPStatsQueueUpdatesOut"), ("BW-OpenClientServer", "bwOCSCAPStatsQueueActionsIn"), ("BW-OpenClientServer", "bwOCSCAPStatsDatagramsIn"), ("BW-OpenClientServer", "bwOCSCAPStatsDatagramsOut"), ("BW-OpenClientServer", "bwOCSCAPRegisterRequestIns"), ("BW-OpenClientServer", "bwOCSCAPRegisterRequestOuts"), ("BW-OpenClientServer", "bwOCSCAPResponseAuthenticationIns"), ("BW-OpenClientServer", "bwOCSCAPResponseAuthenticationOuts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsCapGroup = bwOcsCapGroup.setStatus('current')
bwOcsAsOSSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 2)).setObjects(("BW-OpenClientServer", "bwOCSOSSRequestAuthentications"), ("BW-OpenClientServer", "bwOCSOSSResponseAuthentications"), ("BW-OpenClientServer", "bwOCSOSSRequestLogins"), ("BW-OpenClientServer", "bwOCSOSSResponseLogins"), ("BW-OpenClientServer", "bwOCSOSSUnsuccessfulResponseLogins"), ("BW-OpenClientServer", "bwOCSOSSRequestLogoutIns"), ("BW-OpenClientServer", "bwOCSOSSRequestLogoutOuts"), ("BW-OpenClientServer", "bwOCSOSSRequests"), ("BW-OpenClientServer", "bwOCSOSSResponses"), ("BW-OpenClientServer", "bwOCSOSSResponseAuthenticationOuts"), ("BW-OpenClientServer", "bwOCSOSSResponseAuthenticationIns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsAsOSSGroup = bwOcsAsOSSGroup.setStatus('obsolete')
bwOcsNsOSSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 3)).setObjects(("BW-OpenClientServer", "bwOCSNSOSSRequestAuthentications"), ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthentications"), ("BW-OpenClientServer", "bwOCSNSOSSRequestLogins"), ("BW-OpenClientServer", "bwOCSNSOSSResponseLogins"), ("BW-OpenClientServer", "bwOCSNSOSSUnsuccessfulResponseLogins"), ("BW-OpenClientServer", "bwOCSNSOSSRequestLogoutIns"), ("BW-OpenClientServer", "bwOCSNSOSSRequestLogoutOuts"), ("BW-OpenClientServer", "bwOCSNSOSSRequests"), ("BW-OpenClientServer", "bwOCSNSOSSResponses"), ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthenticationOuts"), ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthenticationIns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsNsOSSGroup = bwOcsNsOSSGroup.setStatus('current')
bwOcsBcctGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 4)).setObjects(("BW-OpenClientServer", "bwOCSCommonCommStatsTable"), ("BW-OpenClientServer", "bwOCSCommonCommStatsIndex"), ("BW-OpenClientServer", "bwOCSCommonCommHost"), ("BW-OpenClientServer", "bwOCSCommonCommInterface"), ("BW-OpenClientServer", "bwOCSCommonCommProtocol"), ("BW-OpenClientServer", "bwOCSCommonCommAcceptedOutboundConnections"), ("BW-OpenClientServer", "bwOCSCommonCommAcceptedInboundConnections"), ("BW-OpenClientServer", "bwOCSCommonCommRejectedOutboundConnections"), ("BW-OpenClientServer", "bwOCSCommonCommRejectedInboundConnections"), ("BW-OpenClientServer", "bwOCSCommonCommOutputMessagesProcessed"), ("BW-OpenClientServer", "bwOCSCommonCommInputMessagesProcessed"), ("BW-OpenClientServer", "bwOCSCommonCommOutputCommunicationErrors"), ("BW-OpenClientServer", "bwOCSCommonCommInputCommunicationErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsBcctGroup = bwOcsBcctGroup.setStatus('current')
bwOcsReserveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 5)).setObjects(("BW-OpenClientServer", "bwOCSReserved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsReserveGroup = bwOcsReserveGroup.setStatus('current')
bwOcsExtAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 6)).setObjects(("BW-OpenClientServer", "bwOCSWASAuthenticationAttempts"), ("BW-OpenClientServer", "bwOCSWASLoginAttempts"), ("BW-OpenClientServer", "bwOCSWASCommunicationErrors"), ("BW-OpenClientServer", "bwOCSWASProcessingErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsExtAuthGroup = bwOcsExtAuthGroup.setStatus('current')
bwOcsOciAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 7)).setObjects(("BW-OpenClientServer", "bwOCSOCIAuthenticationRequests"), ("BW-OpenClientServer", "bwOCSOCILoginRequestIns"), ("BW-OpenClientServer", "bwOCSOCILoginRequestOuts"), ("BW-OpenClientServer", "bwOCSOCILoginResponses"), ("BW-OpenClientServer", "bwOCSOCIUnsuccessfulLoginResponses"), ("BW-OpenClientServer", "bwOCSOCILogoutRequestIns"), ("BW-OpenClientServer", "bwOCSOCILogoutRequestOuts"), ("BW-OpenClientServer", "bwOCSOCIRequests"), ("BW-OpenClientServer", "bwOCSOCIResponses"), ("BW-OpenClientServer", "bwOCSOCIAuthenticationResponseOuts"), ("BW-OpenClientServer", "bwOCSOCIAuthenticationResponseIns"), ("BW-OpenClientServer", "bwOCSOCIUserIdLoginLevelNotAllowed"), ("BW-OpenClientServer", "bwOCSOCIErrorResponse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsOciAuthGroup = bwOcsOciAuthGroup.setStatus('current')
bwOcsTcpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 8)).setObjects(("BW-OpenClientServer", "bwOCSTcpServersStatsTable"), ("BW-OpenClientServer", "bwOCSTcpServersStatsIndex"), ("BW-OpenClientServer", "bwOCSTcpServersName"), ("BW-OpenClientServer", "bwOCSTcpServersNbConnectionsAccepted"), ("BW-OpenClientServer", "bwOCSTcpServersNbConnectionsClosed"), ("BW-OpenClientServer", "bwOCSTcpServersOutgoingQueueSize"), ("BW-OpenClientServer", "bwOCSTcpServersIncomingQueueSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsTcpStatsGroup = bwOcsTcpStatsGroup.setStatus('current')
bwOCSConcurrentFrameworkStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 9)).setObjects(("BW-OpenClientServer", "bwOCSMonitoringExecutorTable"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorIndex"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorName"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorCurrentPoolSize"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorMaxPoolSize"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorAvgActiveThreads"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorTaskQueueSize"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbTasksRun"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbWarnings"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbErrors"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorLongestTaskMs"), ("BW-OpenClientServer", "bwOCSMonitoringExecutorLongestTaskName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOCSConcurrentFrameworkStatsGroup = bwOCSConcurrentFrameworkStatsGroup.setStatus('current')
bwOcsBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 2, 1)).setObjects(("BW-OpenClientServer", "bwOcsCapGroup"), ("BW-OpenClientServer", "bwOcsAsOSSGroup"), ("BW-OpenClientServer", "bwOcsNsOSSGroup"), ("BW-OpenClientServer", "bwOcsBcctGroup"), ("BW-OpenClientServer", "bwOcsReserveGroup"), ("BW-OpenClientServer", "bwOcsExtAuthGroup"), ("BW-OpenClientServer", "bwOcsTcpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwOcsBasicCompliance = bwOcsBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("BW-OpenClientServer", bwOCSCommonCommProtocol=bwOCSCommonCommProtocol, bwOCSCAPMonitoringUsersResponses=bwOCSCAPMonitoringUsersResponses, bwOCSMonitoringExecutorName=bwOCSMonitoringExecutorName, bwOCSCAPInfoResponses=bwOCSCAPInfoResponses, bwOCSOSSResponses=bwOCSOSSResponses, bwOCSCAPInfoRequests=bwOCSCAPInfoRequests, bwOCSNSOSSUnsuccessfulResponseLogins=bwOCSNSOSSUnsuccessfulResponseLogins, bwOcsBasicCompliance=bwOcsBasicCompliance, bwOCSCommonCommAcceptedInboundConnections=bwOCSCommonCommAcceptedInboundConnections, bwOCSCommonCommInputCommunicationErrors=bwOCSCommonCommInputCommunicationErrors, bwOCSCommonCommRejectedInboundConnections=bwOCSCommonCommRejectedInboundConnections, bwOCSCAPSessionUpdates=bwOCSCAPSessionUpdates, bwOCSMonitoringExecutorCurrentPoolSize=bwOCSMonitoringExecutorCurrentPoolSize, bwOCSCAPServerStatusRequests=bwOCSCAPServerStatusRequests, bwOCSTcpServersStatsTable=bwOCSTcpServersStatsTable, bwOCSMonitoringExecutorLongestTaskName=bwOCSMonitoringExecutorLongestTaskName, bwOCSCAPRegisterResponses=bwOCSCAPRegisterResponses, commonComm=commonComm, bwOCSWASLoginAttempts=bwOCSWASLoginAttempts, bwOCSTcpServersOutgoingQueueSize=bwOCSTcpServersOutgoingQueueSize, bwOCSOSSResponseLogins=bwOCSOSSResponseLogins, bwOCSTcpServersNbConnectionsAccepted=bwOCSTcpServersNbConnectionsAccepted, bwOCSOCIErrorResponse=bwOCSOCIErrorResponse, bwOCSReserved=bwOCSReserved, bwOCSCAPStatsQueueActionsIn=bwOCSCAPStatsQueueActionsIn, bwOcsNsOSSGroup=bwOcsNsOSSGroup, bwOCSCommonCommStatsTable=bwOCSCommonCommStatsTable, cap=cap, bwOCSCAPAcknowledgements=bwOCSCAPAcknowledgements, bwOCSTcpServersNbBytesReceived=bwOCSTcpServersNbBytesReceived, bwOCSCommonCommOutputMessagesProcessed=bwOCSCommonCommOutputMessagesProcessed, bwOCSWASCommunicationErrors=bwOCSWASCommunicationErrors, bwOCSCAPResponseAuthentications=bwOCSCAPResponseAuthentications, oci=oci, bwOCSOSSRequests=bwOCSOSSRequests, bwOCSTcpServersNbConnectionsInitiated=bwOCSTcpServersNbConnectionsInitiated, bwOCSCAPResponseAuthenticationOuts=bwOCSCAPResponseAuthenticationOuts, bwOCSOCIAuthenticationResponseOuts=bwOCSOCIAuthenticationResponseOuts, tcp=tcp, broadsoft=broadsoft, bwOCSNSOSSResponses=bwOCSNSOSSResponses, bwOCSOCIUserIdLoginLevelNotAllowed=bwOCSOCIUserIdLoginLevelNotAllowed, bwOCSMonitoringExecutorIndex=bwOCSMonitoringExecutorIndex, bwOCSMonitoringExecutorTaskQueueSize=bwOCSMonitoringExecutorTaskQueueSize, bwOCSCAPUnsuccessfulRegisterResponses=bwOCSCAPUnsuccessfulRegisterResponses, bwOcsBcctGroup=bwOcsBcctGroup, bwOCSNSOSSRequests=bwOCSNSOSSRequests, bwOCSNSOSSRequestAuthentications=bwOCSNSOSSRequestAuthentications, bwOcsCapGroup=bwOcsCapGroup, bwOCSOSSUnsuccessfulResponseLogins=bwOCSOSSUnsuccessfulResponseLogins, bwOCSWASAuthenticationAttempts=bwOCSWASAuthenticationAttempts, bwOCSTcpServersNbBytesReceivedSecure=bwOCSTcpServersNbBytesReceivedSecure, bwOCSNSOSSResponseAuthenticationIns=bwOCSNSOSSResponseAuthenticationIns, bwOCSCAPStatsQueueUpdatesOut=bwOCSCAPStatsQueueUpdatesOut, bwOCSCommonCommHost=bwOCSCommonCommHost, bwOCSTcpServersName=bwOCSTcpServersName, bwOCSOCIResponses=bwOCSOCIResponses, bwOCSMonitoringExecutorLongestTaskMs=bwOCSMonitoringExecutorLongestTaskMs, bwOCSOCIAuthenticationRequests=bwOCSOCIAuthenticationRequests, bwOcsMibGroups=bwOcsMibGroups, nsoss=nsoss, bwOCSNSOSSRequestLogins=bwOCSNSOSSRequestLogins, bwOCSCAPUnregisterOuts=bwOCSCAPUnregisterOuts, bwOCSCAPStatsDatagramsOut=bwOCSCAPStatsDatagramsOut, bwOCSCommonCommStatsIndex=bwOCSCommonCommStatsIndex, bwOcsMibConformance=bwOcsMibConformance, bwOCSMonitoringExecutorEntry=bwOCSMonitoringExecutorEntry, bwOCSCommonCommInterface=bwOCSCommonCommInterface, bwOCSCAPStatsDatagramsIn=bwOCSCAPStatsDatagramsIn, bwOCSCommonCommOutputCommunicationErrors=bwOCSCommonCommOutputCommunicationErrors, bwOCSCAPResponseAuthenticationIns=bwOCSCAPResponseAuthenticationIns, bwOCSTcpServersNbBytesSentSecure=bwOCSTcpServersNbBytesSentSecure, extAuth=extAuth, bwOcsAsOSSGroup=bwOcsAsOSSGroup, bwOCSTcpServersIncomingQueueSize=bwOCSTcpServersIncomingQueueSize, bwOCSNSOSSResponseAuthenticationOuts=bwOCSNSOSSResponseAuthenticationOuts, bwOCSOCILoginRequestOuts=bwOCSOCILoginRequestOuts, bwOCSNSOSSRequestLogoutIns=bwOCSNSOSSRequestLogoutIns, bwOCSOCIRequests=bwOCSOCIRequests, bwOCSMonitoringExecutorMaxPoolSize=bwOCSMonitoringExecutorMaxPoolSize, concurrent=concurrent, bwOCSNSOSSResponseLogins=bwOCSNSOSSResponseLogins, bwOCSCommonCommAcceptedOutboundConnections=bwOCSCommonCommAcceptedOutboundConnections, bwOCSOSSResponseAuthentications=bwOCSOSSResponseAuthentications, openClientServer=openClientServer, bwOCSOCILoginRequestIns=bwOCSOCILoginRequestIns, bwOCSOSSRequestLogins=bwOCSOSSRequestLogins, bwOCSConcurrentFrameworkStatsGroup=bwOCSConcurrentFrameworkStatsGroup, bwOCSTcpServersNbConnectionsRefused=bwOCSTcpServersNbConnectionsRefused, bwOCSMonitoringExecutorNbTasksRun=bwOCSMonitoringExecutorNbTasksRun, bwOCSOSSResponseAuthenticationOuts=bwOCSOSSResponseAuthenticationOuts, bwOCSCommonCommRejectedOutboundConnections=bwOCSCommonCommRejectedOutboundConnections, bwOCSTcpServersStatsEntry=bwOCSTcpServersStatsEntry, bwOCSMonitoringExecutorNbErrors=bwOCSMonitoringExecutorNbErrors, bwOcsExtAuthGroup=bwOcsExtAuthGroup, ocsReserved=ocsReserved, PYSNMP_MODULE_ID=broadsoft, bwOCSOCILoginResponses=bwOCSOCILoginResponses, bwOCSMonitoringExecutorAvgActiveThreads=bwOCSMonitoringExecutorAvgActiveThreads, bwOcsTcpStatsGroup=bwOcsTcpStatsGroup, bwOCSOCIAuthenticationResponseIns=bwOCSOCIAuthenticationResponseIns, bwOCSCAPCallControlInfos=bwOCSCAPCallControlInfos, bwOCSCAPUnregisterIns=bwOCSCAPUnregisterIns, bwOCSNSOSSResponseAuthentications=bwOCSNSOSSResponseAuthentications, bwOCSCAPMonitoringUsersRequests=bwOCSCAPMonitoringUsersRequests, bwOcsReserveGroup=bwOcsReserveGroup, bwOCSOCILogoutRequestIns=bwOCSOCILogoutRequestIns, bwOCSOCILogoutRequestOuts=bwOCSOCILogoutRequestOuts, bwOcsMibCompliancy=bwOcsMibCompliancy, bwOCSOCIUnsuccessfulLoginResponses=bwOCSOCIUnsuccessfulLoginResponses, bwOCSCAPRegisterRequestIns=bwOCSCAPRegisterRequestIns, bwOCSMonitoringExecutorTable=bwOCSMonitoringExecutorTable, bwOCSNSOSSRequestLogoutOuts=bwOCSNSOSSRequestLogoutOuts, bwOCSWASProcessingErrors=bwOCSWASProcessingErrors, protocols=protocols, bwOCSCAPProfileUpdates=bwOCSCAPProfileUpdates, broadworks=broadworks, bwOCSCommonCommStatsEntry=bwOCSCommonCommStatsEntry, bwOCSOSSRequestLogoutIns=bwOCSOSSRequestLogoutIns, bwOCSCAPCallUpdates=bwOCSCAPCallUpdates, oss=oss, bwOCSCAPRegisterRequests=bwOCSCAPRegisterRequests, bwOCSCAPCallActions=bwOCSCAPCallActions, bwOCSCommonCommInputMessagesProcessed=bwOCSCommonCommInputMessagesProcessed, bwOcsOciAuthGroup=bwOcsOciAuthGroup, bwOCSCAPExternalNotifies=bwOCSCAPExternalNotifies, bwOCSOSSRequestAuthentications=bwOCSOSSRequestAuthentications, bwOCSTcpServersNbBytesSent=bwOCSTcpServersNbBytesSent, bwOCSCAPRegisterAuthentications=bwOCSCAPRegisterAuthentications, bwOCSCAPRegisterRequestOuts=bwOCSCAPRegisterRequestOuts, bwOCSOSSResponseAuthenticationIns=bwOCSOSSResponseAuthenticationIns, bwOCSTcpServersStatsIndex=bwOCSTcpServersStatsIndex, bwOCSMonitoringExecutorNbWarnings=bwOCSMonitoringExecutorNbWarnings, bwOCSTcpServersNbConnectionsClosed=bwOCSTcpServersNbConnectionsClosed, bwOCSOSSRequestLogoutOuts=bwOCSOSSRequestLogoutOuts)

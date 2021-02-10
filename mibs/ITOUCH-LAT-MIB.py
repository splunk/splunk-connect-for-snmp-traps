#
# PySNMP MIB module ITOUCH-LAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-LAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, ObjectIdentity, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, iso, Counter64, IpAddress, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "iso", "Counter64", "IpAddress", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xLat = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 3))
latAnnounceServices = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latAnnounceServices.setStatus('mandatory')
latCircuitTimer = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latCircuitTimer.setStatus('mandatory')
latIdentificationLengthLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latIdentificationLengthLimit.setStatus('mandatory')
latKeepaliveTimer = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 180))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latKeepaliveTimer.setStatus('mandatory')
latMulticastTimer = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 180))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latMulticastTimer.setStatus('mandatory')
latNodeLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latNodeLimit.setStatus('mandatory')
latNumber = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latNumber.setStatus('mandatory')
latRetransmitLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latRetransmitLimit.setStatus('mandatory')
latLocalServiceGroups = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latLocalServiceGroups.setStatus('mandatory')
latGroupPurge = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latGroupPurge.setStatus('mandatory')
latNodePurge = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latNodePurge.setStatus('mandatory')
latNodesRejected = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodesRejected.setStatus('mandatory')
latInMessages = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInMessages.setStatus('mandatory')
latOutMessages = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latOutMessages.setStatus('mandatory')
latInSessionsAccepted = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInSessionsAccepted.setStatus('mandatory')
latInSessionsRejected = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInSessionsRejected.setStatus('mandatory')
latAddressChange = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latAddressChange.setStatus('mandatory')
latInDuplicates = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInDuplicates.setStatus('mandatory')
latOutRetransmits = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latOutRetransmits.setStatus('mandatory')
latInBadMessages = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInBadMessages.setStatus('mandatory')
latInBadSlots = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInBadSlots.setStatus('mandatory')
latInBadMulticasts = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latInBadMulticasts.setStatus('mandatory')
latPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 3, 23), )
if mibBuilder.loadTexts: latPortTable.setStatus('mandatory')
latPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 3, 23, 1), ).setIndexNames((0, "ITOUCH-LAT-MIB", "latPortIndex"))
if mibBuilder.loadTexts: latPortEntry.setStatus('mandatory')
latPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latPortIndex.setStatus('mandatory')
latPortAuthorizedGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latPortAuthorizedGroups.setStatus('mandatory')
latPortAutoPrompt = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latPortAutoPrompt.setStatus('mandatory')
latPortCurrentGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latPortCurrentGroups.setStatus('mandatory')
latPortRemoteModification = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latPortRemoteModification.setStatus('mandatory')
latOfferedServiceTable = MibTable((1, 3, 6, 1, 4, 1, 33, 3, 24), )
if mibBuilder.loadTexts: latOfferedServiceTable.setStatus('mandatory')
latOfferedServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 3, 24, 1), ).setIndexNames((0, "ITOUCH-LAT-MIB", "latOfferedServiceName"))
if mibBuilder.loadTexts: latOfferedServiceEntry.setStatus('mandatory')
latOfferedServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latOfferedServiceName.setStatus('mandatory')
latOfferedServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServiceStatus.setStatus('mandatory')
latOfferedServiceAllowConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServiceAllowConnections.setStatus('mandatory')
latOfferedServiceIdentification = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServiceIdentification.setStatus('mandatory')
latOfferedServicePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServicePassword.setStatus('mandatory')
latOfferedServicePortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServicePortMap.setStatus('mandatory')
latOfferedServiceQueuing = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServiceQueuing.setStatus('mandatory')
latOfferedServiceEnvironmentalManager = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latOfferedServiceEnvironmentalManager.setStatus('mandatory')
latVisibleServiceTable = MibTable((1, 3, 6, 1, 4, 1, 33, 3, 25), )
if mibBuilder.loadTexts: latVisibleServiceTable.setStatus('mandatory')
latVisibleServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 3, 25, 1), ).setIndexNames((0, "ITOUCH-LAT-MIB", "latVisibleServiceName"))
if mibBuilder.loadTexts: latVisibleServiceEntry.setStatus('mandatory')
latVisibleServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceName.setStatus('mandatory')
latVisibleServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3), ("unreachable", 4), ("reachable", 5), ("connected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceStatus.setStatus('mandatory')
latVisibleServiceNode = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceNode.setStatus('mandatory')
latVisibleServiceConnectedSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceConnectedSessions.setStatus('mandatory')
latVisibleServiceIdentification = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceIdentification.setStatus('mandatory')
latVisibleServiceRating = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latVisibleServiceRating.setStatus('mandatory')
latNodeTable = MibTable((1, 3, 6, 1, 4, 1, 33, 3, 26), )
if mibBuilder.loadTexts: latNodeTable.setStatus('mandatory')
latNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 3, 26, 1), ).setIndexNames((0, "ITOUCH-LAT-MIB", "latNodeName"))
if mibBuilder.loadTexts: latNodeEntry.setStatus('mandatory')
latNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeName.setStatus('mandatory')
latNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3), ("unreachable", 4), ("reachable", 5), ("connected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeStatus.setStatus('mandatory')
latNodeConnectedSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeConnectedSessions.setStatus('mandatory')
latNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeAddress.setStatus('mandatory')
latNodeDataLinkFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeDataLinkFrame.setStatus('mandatory')
latNodeIdentification = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeIdentification.setStatus('mandatory')
latNodeGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeGroups.setStatus('mandatory')
latNodeServiceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeServiceNumber.setStatus('mandatory')
latNodeZero = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latNodeZero.setStatus('mandatory')
latNodeZeroTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeZeroTime.setStatus('mandatory')
latNodeInMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInMessages.setStatus('mandatory')
latNodeOutMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeOutMessages.setStatus('mandatory')
latNodeInSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInSlots.setStatus('mandatory')
latNodeOutSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeOutSlots.setStatus('mandatory')
latNodeInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInBytes.setStatus('mandatory')
latNodeOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeOutBytes.setStatus('mandatory')
latNodeAddressChange = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeAddressChange.setStatus('mandatory')
latNodeInDuplicates = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInDuplicates.setStatus('mandatory')
latNodeOutRetransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeOutRetransmits.setStatus('mandatory')
latNodeInBadMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInBadMessages.setStatus('mandatory')
latNodeInBadSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInBadSlots.setStatus('mandatory')
latNodeInSessionsAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInSessionsAccepted.setStatus('mandatory')
latNodeInSessionsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latNodeInSessionsRejected.setStatus('mandatory')
latSolicits = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latSolicits.setStatus('mandatory')
latImmediateAck = MibScalar((1, 3, 6, 1, 4, 1, 33, 3, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: latImmediateAck.setStatus('mandatory')
mibBuilder.exportSymbols("ITOUCH-LAT-MIB", latNodeZero=latNodeZero, latNodeServiceNumber=latNodeServiceNumber, latPortEntry=latPortEntry, latPortRemoteModification=latPortRemoteModification, latOfferedServiceEnvironmentalManager=latOfferedServiceEnvironmentalManager, latNodeInSessionsAccepted=latNodeInSessionsAccepted, latNodeInDuplicates=latNodeInDuplicates, latAnnounceServices=latAnnounceServices, latNodeInSessionsRejected=latNodeInSessionsRejected, latInDuplicates=latInDuplicates, latNodeInMessages=latNodeInMessages, latNodeInSlots=latNodeInSlots, latPortAutoPrompt=latPortAutoPrompt, latOfferedServicePassword=latOfferedServicePassword, latVisibleServiceStatus=latVisibleServiceStatus, latGroupPurge=latGroupPurge, latVisibleServiceName=latVisibleServiceName, latInBadSlots=latInBadSlots, latVisibleServiceNode=latVisibleServiceNode, latNodeAddressChange=latNodeAddressChange, latVisibleServiceRating=latVisibleServiceRating, latPortCurrentGroups=latPortCurrentGroups, latSolicits=latSolicits, latNodeOutBytes=latNodeOutBytes, latNodeInBadMessages=latNodeInBadMessages, latImmediateAck=latImmediateAck, latRetransmitLimit=latRetransmitLimit, latOutMessages=latOutMessages, latNodeZeroTime=latNodeZeroTime, latNodeOutSlots=latNodeOutSlots, latNodesRejected=latNodesRejected, latInMessages=latInMessages, latPortIndex=latPortIndex, latNodeDataLinkFrame=latNodeDataLinkFrame, latNumber=latNumber, latPortTable=latPortTable, latVisibleServiceEntry=latVisibleServiceEntry, latNodeOutRetransmits=latNodeOutRetransmits, latVisibleServiceConnectedSessions=latVisibleServiceConnectedSessions, latLocalServiceGroups=latLocalServiceGroups, latNodeTable=latNodeTable, latNodeGroups=latNodeGroups, latKeepaliveTimer=latKeepaliveTimer, latInSessionsAccepted=latInSessionsAccepted, latOutRetransmits=latOutRetransmits, latNodeInBytes=latNodeInBytes, latOfferedServiceQueuing=latOfferedServiceQueuing, xLat=xLat, latMulticastTimer=latMulticastTimer, latNodeIdentification=latNodeIdentification, latInBadMulticasts=latInBadMulticasts, latOfferedServiceAllowConnections=latOfferedServiceAllowConnections, latOfferedServiceName=latOfferedServiceName, latNodeStatus=latNodeStatus, latNodeOutMessages=latNodeOutMessages, latNodeLimit=latNodeLimit, latPortAuthorizedGroups=latPortAuthorizedGroups, latVisibleServiceIdentification=latVisibleServiceIdentification, latAddressChange=latAddressChange, latNodeInBadSlots=latNodeInBadSlots, latNodePurge=latNodePurge, latInBadMessages=latInBadMessages, latNodeEntry=latNodeEntry, latOfferedServiceTable=latOfferedServiceTable, latOfferedServiceEntry=latOfferedServiceEntry, latInSessionsRejected=latInSessionsRejected, latOfferedServiceIdentification=latOfferedServiceIdentification, latNodeName=latNodeName, latNodeAddress=latNodeAddress, latOfferedServicePortMap=latOfferedServicePortMap, latIdentificationLengthLimit=latIdentificationLengthLimit, latOfferedServiceStatus=latOfferedServiceStatus, latNodeConnectedSessions=latNodeConnectedSessions, latVisibleServiceTable=latVisibleServiceTable, latCircuitTimer=latCircuitTimer)

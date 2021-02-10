#
# PySNMP MIB module CISCO-TELNET-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELNET-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, iso, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter32, IpAddress, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "iso", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoTelnetServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 630))
ciscoTelnetServerMIB.setRevisions(('2007-05-08 00:00',))
if mibBuilder.loadTexts: ciscoTelnetServerMIB.setLastUpdated('200705080000Z')
if mibBuilder.loadTexts: ciscoTelnetServerMIB.setOrganization('Cisco Systems, Inc.')
ciscoTelnetServerMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 0))
ciscoTelnetServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 1))
ciscoTelnetServerMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 2))
ciscoTelnetServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 1))
ciscoTelnetServerConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1))
ciscoTelnetServerStatusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2))
ctsTelnetActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsTelnetActivation.setStatus('current')
ctsSessionEndedNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsSessionEndedNotifEnable.setStatus('current')
ctsSessionStartedNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsSessionStartedNotifEnable.setStatus('current')
ctsSessionDeniedNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsSessionDeniedNotifEnable.setStatus('current')
ctsSessionFailureNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionFailureNotifEnable.setStatus('current')
ctsSessionsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1), )
if mibBuilder.loadTexts: ctsSessionsTable.setStatus('current')
ctsSessionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-TELNET-SERVER-MIB", "ctsSessionID"))
if mibBuilder.loadTexts: ctsSessionsEntry.setStatus('current')
ctsSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ctsSessionID.setStatus('current')
ctsSessionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionDescription.setStatus('current')
ctsSessionClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionClientAddressType.setStatus('current')
ctsSessionsClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionsClientAddress.setStatus('current')
ctsSessionPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionPID.setStatus('current')
ctsSessionUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionUserID.setStatus('current')
ctsSessionTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 7), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsSessionTcpPort.setStatus('current')
ctsSessionEnded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 1)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
if mibBuilder.loadTexts: ctsSessionEnded.setStatus('current')
ctsSessionStarted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 2)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"))
if mibBuilder.loadTexts: ctsSessionStarted.setStatus('current')
ctsSessionDenied = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 3)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
if mibBuilder.loadTexts: ctsSessionDenied.setStatus('current')
ctsSessionLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 4)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
if mibBuilder.loadTexts: ctsSessionLoginFailure.setStatus('current')
ciscoTelnetServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2))
ciscoTelnetServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 1, 1)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsMIBSessionsObjectGroup"), ("CISCO-TELNET-SERVER-MIB", "ctsMIBNotificationGroup"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionNotifsControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelnetServerMIBCompliance = ciscoTelnetServerMIBCompliance.setStatus('current')
ctsMIBSessionsObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 1)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionDescription"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"), ("CISCO-TELNET-SERVER-MIB", "ctsTelnetActivation"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionPID"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctsMIBSessionsObjectGroup = ctsMIBSessionsObjectGroup.setStatus('current')
ctsMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 2)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionEnded"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionStarted"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionDenied"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionLoginFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctsMIBNotificationGroup = ctsMIBNotificationGroup.setStatus('current')
ctsSessionNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 3)).setObjects(("CISCO-TELNET-SERVER-MIB", "ctsSessionEndedNotifEnable"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionStartedNotifEnable"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionDeniedNotifEnable"), ("CISCO-TELNET-SERVER-MIB", "ctsSessionFailureNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctsSessionNotifsControlGroup = ctsSessionNotifsControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELNET-SERVER-MIB", ciscoTelnetServerMIBConform=ciscoTelnetServerMIBConform, ctsSessionClientAddressType=ctsSessionClientAddressType, PYSNMP_MODULE_ID=ciscoTelnetServerMIB, ctsSessionDescription=ctsSessionDescription, ciscoTelnetServerMIBCompliances=ciscoTelnetServerMIBCompliances, ctsMIBSessionsObjectGroup=ctsMIBSessionsObjectGroup, ctsSessionEnded=ctsSessionEnded, ciscoTelnetServerStatusObjects=ciscoTelnetServerStatusObjects, ciscoTelnetServerMIBCompliance=ciscoTelnetServerMIBCompliance, ciscoTelnetServerMIBNotifs=ciscoTelnetServerMIBNotifs, ctsSessionEndedNotifEnable=ctsSessionEndedNotifEnable, ctsSessionFailureNotifEnable=ctsSessionFailureNotifEnable, ctsSessionUserID=ctsSessionUserID, ciscoTelnetServerMIB=ciscoTelnetServerMIB, ctsMIBNotificationGroup=ctsMIBNotificationGroup, ciscoTelnetServerConfigObjects=ciscoTelnetServerConfigObjects, ctsSessionStartedNotifEnable=ctsSessionStartedNotifEnable, ctsSessionTcpPort=ctsSessionTcpPort, ctsTelnetActivation=ctsTelnetActivation, ciscoTelnetServerMIBObjects=ciscoTelnetServerMIBObjects, ctsSessionsEntry=ctsSessionsEntry, ciscoTelnetServerMIBGroups=ciscoTelnetServerMIBGroups, ctsSessionDenied=ctsSessionDenied, ctsSessionNotifsControlGroup=ctsSessionNotifsControlGroup, ctsSessionDeniedNotifEnable=ctsSessionDeniedNotifEnable, ctsSessionsTable=ctsSessionsTable, ctsSessionLoginFailure=ctsSessionLoginFailure, ctsSessionsClientAddress=ctsSessionsClientAddress, ctsSessionStarted=ctsSessionStarted, ctsSessionPID=ctsSessionPID, ctsSessionID=ctsSessionID)

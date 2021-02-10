#
# PySNMP MIB module CDR-DS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CDR-DS2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Gauge32, iso, IpAddress, NotificationType, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectName, Counter64, MibIdentifier, Unsigned32, snmpModules, Integer32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "iso", "IpAddress", "NotificationType", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectName", "Counter64", "MibIdentifier", "Unsigned32", "snmpModules", "Integer32", "ObjectIdentity", "Bits")
TestAndIncr, RowStatus, TimeStamp, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "RowStatus", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
cdrDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7))
cdrDS2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2))
if mibBuilder.loadTexts: cdrDS2.setLastUpdated('240701')
if mibBuilder.loadTexts: cdrDS2.setOrganization('Lucent Technologies')
cdrSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1))
cdrClient = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cdrClient.setStatus('current')
callState = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callState.setStatus('current')
fCAppID = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fCAppID.setStatus('current')
fCAppInstance = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fCAppInstance.setStatus('current')
severity = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: severity.setStatus('current')
originationNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: originationNumber.setStatus('current')
destinationNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: destinationNumber.setStatus('current')
callAnswerTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callAnswerTime.setStatus('current')
switchId = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: switchId.setStatus('current')
callId = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callId.setStatus('current')
fullPercent = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fullPercent.setStatus('current')
fileSystem = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fileSystem.setStatus('current')
mibBuilder.exportSymbols("CDR-DS2-MIB", cdrDeviceServer=cdrDeviceServer, cdrClient=cdrClient, softSwitch=softSwitch, destinationNumber=destinationNumber, severity=severity, lucent=lucent, fileSystem=fileSystem, products=products, PYSNMP_MODULE_ID=cdrDS2, fullPercent=fullPercent, originationNumber=originationNumber, callAnswerTime=callAnswerTime, cdrSystem=cdrSystem, switchId=switchId, callState=callState, cdrDS2=cdrDS2, fCAppID=fCAppID, fCAppInstance=fCAppInstance, callId=callId)

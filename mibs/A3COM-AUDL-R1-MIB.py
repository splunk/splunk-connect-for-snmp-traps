#
# PySNMP MIB module A3COM-AUDL-r1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-AUDL-R1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:48:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, iso, IpAddress, NotificationType, Unsigned32, Integer32, MibIdentifier, Gauge32, ObjectIdentity, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "iso", "IpAddress", "NotificationType", "Unsigned32", "Integer32", "MibIdentifier", "Gauge32", "ObjectIdentity", "TimeTicks", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComAuditLog = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 29))
a3ComAudlControl = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 29, 1))
a3ComAudlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 29, 2))
a3ComAudlControlAuditTrail = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auditTrail", 1), ("noAuditTrail", 2))).clone('noAuditTrail')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlControlAuditTrail.setStatus('mandatory')
a3ComAudlControlConfig = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("config", 1), ("noConfig", 2))).clone('noConfig')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlControlConfig.setStatus('mandatory')
a3ComAudlControlMessages = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("messages", 1), ("noMessages", 2))).clone('noMessages')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlControlMessages.setStatus('mandatory')
a3ComAudlControlSecurity = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("security", 1), ("noSecurity", 2))).clone('noSecurity')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlControlSecurity.setStatus('mandatory')
a3ComAudlLogServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlLogServerAddr.setStatus('mandatory')
a3ComAudlPriorityLevel = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("log-EMERG", 1), ("log-ALERT", 2), ("log-CRITICAL", 3), ("log-ERROR", 4), ("log-WARNING", 5), ("log-NOTICE", 6), ("log-INFO", 7), ("log-DEBUG", 8))).clone('log-INFO')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlPriorityLevel.setStatus('mandatory')
a3ComAudlMaxLog = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlMaxLog.setStatus('mandatory')
a3ComAudlIdleTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 480)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComAudlIdleTime.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-AUDL-r1-MIB", a3ComAudlIdleTime=a3ComAudlIdleTime, a3ComAudlConfig=a3ComAudlConfig, a3ComAudlLogServerAddr=a3ComAudlLogServerAddr, brouterMIB=brouterMIB, a3ComAudlControlMessages=a3ComAudlControlMessages, a3ComAuditLog=a3ComAuditLog, a3ComAudlControlConfig=a3ComAudlControlConfig, a3ComAudlMaxLog=a3ComAudlMaxLog, a3ComAudlPriorityLevel=a3ComAudlPriorityLevel, a3ComAudlControlSecurity=a3ComAudlControlSecurity, a3ComAudlControlAuditTrail=a3ComAudlControlAuditTrail, a3ComAudlControl=a3ComAudlControl, a3Com=a3Com)

#
# PySNMP MIB module HPN-ICF-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-PORT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfPortSecurity, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfPortSecurity")
dot1xAuthSessionTerminateCause, dot1xAuthSessionUserName, dot1xAuthSessionAuthenticMethod, dot1xPaePortNumber = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause", "dot1xAuthSessionUserName", "dot1xAuthSessionAuthenticMethod", "dot1xPaePortNumber")
ifAdminStatus, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifAdminStatus", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, ObjectIdentity, Unsigned32, TimeTicks, iso, Integer32, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "TimeTicks", "iso", "Integer32", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Counter64")
DisplayString, RowStatus, TextualConvention, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress", "TruthValue")
hpnicfPortSecurityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1))
hpnicfPortSecurityMIB.setRevisions(('2004-11-24 00:00',))
if mibBuilder.loadTexts: hpnicfPortSecurityMIB.setLastUpdated('200411240000Z')
if mibBuilder.loadTexts: hpnicfPortSecurityMIB.setOrganization('')
hpnicfPortSecurityLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1))
hpnicfSecurePortSecurityControl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecurePortSecurityControl.setStatus('current')
hpnicfSecurePortVlanMembershipList = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSecurePortVlanMembershipList.setStatus('current')
hpnicfSecureRalmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4))
hpnicfSecureRalmDefaultSessionTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmDefaultSessionTime.setStatus('current')
hpnicfSecureRalmHoldoffTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmHoldoffTime.setStatus('current')
hpnicfSecureRalmReauthenticate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmReauthenticate.setStatus('current')
hpnicfSecureRalmAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("papUsernameAsMacAddress", 1), ("papUsernameFixed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthMode.setStatus('current')
hpnicfSecureRalmAuthUsername = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthUsername.setStatus('current')
hpnicfSecureRalmAuthPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthPassword.setStatus('current')
hpnicfSecureRalmAuthDomain = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthDomain.setStatus('current')
hpnicfSecureRalmAuthOfflineTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 2147483647)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthOfflineTime.setStatus('current')
hpnicfSecureRalmAuthServerTimeoutTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureRalmAuthServerTimeoutTime.setStatus('current')
hpnicfSecureMacControl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureMacControl.setStatus('current')
hpnicfPortSecurityTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2))
hpnicfSecurePortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfSecurePortTable.setStatus('current')
hpnicfSecurePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfSecurePortEntry.setStatus('current')
hpnicfSecurePortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("noRestrictions", 1), ("continuousLearning", 2), ("autoLearn", 3), ("secure", 4), ("userLogin", 5), ("userLoginSecure", 6), ("userLoginWithOUI", 7), ("macAddressWithRadius", 8), ("macAddressOrUserLoginSecure", 9), ("macAddressElseUserLoginSecure", 10), ("userLoginSecureExt", 11), ("macAddressOrUserLoginSecureExt", 12), ("macAddressElseUserLoginSecureExt", 13), ("macAddressAndUserLoginSecure", 14), ("macAddressAndUserLoginSecureExt", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecurePortMode.setStatus('current')
hpnicfSecureNeedToKnowMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("notAvailable", 1), ("disabled", 2), ("needToKnowOnly", 3), ("needToKnowWithBroadcastsAllowed", 4), ("needToKnowWithMulticastsAllowed", 5), ("permanentNeedToKnowOnly", 6), ("permanentNeedToKnowWithBroadcastsAllowed", 7), ("permanentNeedToKnowWithMulticastsAllowed", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureNeedToKnowMode.setStatus('current')
hpnicfSecureIntrusionAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notAvailable", 1), ("noAction", 2), ("disablePort", 3), ("disablePortTemporarily", 4), ("allowDefaultAccess", 5), ("blockMacAddress", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureIntrusionAction.setStatus('current')
hpnicfSecureNumberAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureNumberAddresses.setStatus('current')
hpnicfSecureNumberAddressesStored = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSecureNumberAddressesStored.setStatus('current')
hpnicfSecureMaximumAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSecureMaximumAddresses.setStatus('current')
hpnicfSecureAddressTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2), )
if mibBuilder.loadTexts: hpnicfSecureAddressTable.setStatus('current')
hpnicfSecureAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrVlanID"))
if mibBuilder.loadTexts: hpnicfSecureAddressEntry.setStatus('current')
hpnicfSecureAddrMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSecureAddrMAC.setStatus('current')
hpnicfSecureAddrVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureAddrVlanID.setStatus('current')
hpnicfSecureAddrMACStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("addressBlackhole", 1), ("addressUserConfig", 2), ("addressDot1xAuth", 3), ("addressRALM", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureAddrMACStatus.setStatus('current')
hpnicfSecureAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureAddrRowStatus.setStatus('current')
hpnicfSecureOUITable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3), )
if mibBuilder.loadTexts: hpnicfSecureOUITable.setStatus('current')
hpnicfSecureOUIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureOUIIndex"))
if mibBuilder.loadTexts: hpnicfSecureOUIEntry.setStatus('current')
hpnicfSecureOUIIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: hpnicfSecureOUIIndex.setStatus('current')
hpnicfSecureOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureOUI.setStatus('current')
hpnicfSecureOUIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureOUIRowStatus.setStatus('current')
hpnicfSecureBindingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4), )
if mibBuilder.loadTexts: hpnicfSecureBindingTable.setStatus('current')
hpnicfSecureBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1), ).setIndexNames((0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureBindingIndex"))
if mibBuilder.loadTexts: hpnicfSecureBindingEntry.setStatus('current')
hpnicfSecureBindingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfSecureBindingIndex.setStatus('current')
hpnicfSecureBindingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureBindingPort.setStatus('current')
hpnicfSecureBindingAddrMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureBindingAddrMAC.setStatus('current')
hpnicfSecureBindingAddrIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureBindingAddrIp.setStatus('current')
hpnicfSecureBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSecureBindingRowStatus.setStatus('current')
hpnicfSecureAssignTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5), )
if mibBuilder.loadTexts: hpnicfSecureAssignTable.setStatus('current')
hpnicfSecureAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfSecureAssignEntry.setStatus('current')
hpnicfSecureAssignEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSecureAssignEnable.setStatus('current')
hpnicfSecureVlanAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSecureVlanAssignment.setStatus('current')
hpnicfPortSecurityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3))
hpnicfSecureAddressLearned = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 1)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"))
if mibBuilder.loadTexts: hpnicfSecureAddressLearned.setStatus('current')
hpnicfSecureViolation = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 2)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("IF-MIB", "ifAdminStatus"))
if mibBuilder.loadTexts: hpnicfSecureViolation.setStatus('current')
hpnicfSecureLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 3)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"))
if mibBuilder.loadTexts: hpnicfSecureLoginFailure.setStatus('current')
hpnicfSecureLogon = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 4)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
if mibBuilder.loadTexts: hpnicfSecureLogon.setStatus('current')
hpnicfSecureLogoff = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 5)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
if mibBuilder.loadTexts: hpnicfSecureLogoff.setStatus('current')
hpnicfSecureRalmLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 6)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"))
if mibBuilder.loadTexts: hpnicfSecureRalmLoginFailure.setStatus('current')
hpnicfSecureRalmLogon = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 7)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
if mibBuilder.loadTexts: hpnicfSecureRalmLogon.setStatus('current')
hpnicfSecureRalmLogoff = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 8)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"), ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
if mibBuilder.loadTexts: hpnicfSecureRalmLogoff.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-PORT-SECURITY-MIB", hpnicfSecurePortTable=hpnicfSecurePortTable, hpnicfSecureAddressLearned=hpnicfSecureAddressLearned, hpnicfSecureLogon=hpnicfSecureLogon, hpnicfPortSecurityLeaf=hpnicfPortSecurityLeaf, hpnicfSecureNeedToKnowMode=hpnicfSecureNeedToKnowMode, hpnicfSecureAddressTable=hpnicfSecureAddressTable, hpnicfSecurePortMode=hpnicfSecurePortMode, hpnicfSecureAssignTable=hpnicfSecureAssignTable, hpnicfSecureViolation=hpnicfSecureViolation, hpnicfSecureBindingAddrIp=hpnicfSecureBindingAddrIp, hpnicfSecureRalmAuthUsername=hpnicfSecureRalmAuthUsername, hpnicfPortSecurityTables=hpnicfPortSecurityTables, hpnicfSecureBindingEntry=hpnicfSecureBindingEntry, hpnicfSecureRalmReauthenticate=hpnicfSecureRalmReauthenticate, hpnicfSecureMaximumAddresses=hpnicfSecureMaximumAddresses, hpnicfSecureAssignEntry=hpnicfSecureAssignEntry, hpnicfSecureAssignEnable=hpnicfSecureAssignEnable, hpnicfSecurePortEntry=hpnicfSecurePortEntry, hpnicfSecureIntrusionAction=hpnicfSecureIntrusionAction, hpnicfSecureBindingIndex=hpnicfSecureBindingIndex, hpnicfSecureRalmHoldoffTime=hpnicfSecureRalmHoldoffTime, hpnicfSecureRalmAuthServerTimeoutTime=hpnicfSecureRalmAuthServerTimeoutTime, hpnicfSecureOUITable=hpnicfSecureOUITable, hpnicfPortSecurityMIB=hpnicfPortSecurityMIB, hpnicfSecureMacControl=hpnicfSecureMacControl, hpnicfSecureOUI=hpnicfSecureOUI, hpnicfSecureAddrRowStatus=hpnicfSecureAddrRowStatus, hpnicfSecureRalmLogoff=hpnicfSecureRalmLogoff, hpnicfSecureBindingPort=hpnicfSecureBindingPort, hpnicfSecureLoginFailure=hpnicfSecureLoginFailure, hpnicfSecureAddrVlanID=hpnicfSecureAddrVlanID, hpnicfSecureNumberAddresses=hpnicfSecureNumberAddresses, hpnicfSecureRalmLogon=hpnicfSecureRalmLogon, hpnicfSecureOUIEntry=hpnicfSecureOUIEntry, hpnicfSecureBindingTable=hpnicfSecureBindingTable, hpnicfSecureBindingRowStatus=hpnicfSecureBindingRowStatus, hpnicfSecureRalmAuthDomain=hpnicfSecureRalmAuthDomain, hpnicfSecureAddrMAC=hpnicfSecureAddrMAC, hpnicfSecureAddressEntry=hpnicfSecureAddressEntry, hpnicfSecurePortSecurityControl=hpnicfSecurePortSecurityControl, hpnicfSecureRalmLoginFailure=hpnicfSecureRalmLoginFailure, hpnicfSecureRalmAuthMode=hpnicfSecureRalmAuthMode, hpnicfSecureOUIRowStatus=hpnicfSecureOUIRowStatus, hpnicfSecureBindingAddrMAC=hpnicfSecureBindingAddrMAC, hpnicfSecureVlanAssignment=hpnicfSecureVlanAssignment, hpnicfSecurePortVlanMembershipList=hpnicfSecurePortVlanMembershipList, hpnicfSecureRalmAuthOfflineTime=hpnicfSecureRalmAuthOfflineTime, PYSNMP_MODULE_ID=hpnicfPortSecurityMIB, hpnicfSecureRalmObjects=hpnicfSecureRalmObjects, hpnicfSecureOUIIndex=hpnicfSecureOUIIndex, hpnicfSecureRalmDefaultSessionTime=hpnicfSecureRalmDefaultSessionTime, hpnicfSecureAddrMACStatus=hpnicfSecureAddrMACStatus, hpnicfPortSecurityNotifications=hpnicfPortSecurityNotifications, hpnicfSecureNumberAddressesStored=hpnicfSecureNumberAddressesStored, hpnicfSecureRalmAuthPassword=hpnicfSecureRalmAuthPassword, hpnicfSecureLogoff=hpnicfSecureLogoff)

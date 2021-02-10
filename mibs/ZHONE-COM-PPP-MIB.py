#
# PySNMP MIB module ZHONE-COM-PPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-PPP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, Bits, IpAddress, iso, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "IpAddress", "iso", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhonePpp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhonePpp", "zhoneModules")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
comPpp = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 69))
comPpp.setRevisions(('2001-06-06 16:00', '2001-04-19 15:00', '2001-03-20 09:30', '2001-03-12 11:00', '2001-03-01 11:00', '2001-02-08 10:02',))
if mibBuilder.loadTexts: comPpp.setLastUpdated('200106061600Z')
if mibBuilder.loadTexts: comPpp.setOrganization('Zhone Technologies, Inc.')
class ZhoneAuthenticationProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pap", 1), ("chap", 2))

class EnableFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

pppInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1), )
if mibBuilder.loadTexts: pppInterfaceTable.setStatus('current')
pppInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppInterfaceEntry.setStatus('current')
pppIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfLowerIfIndex.setStatus('current')
pppIfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 2), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfVpi.setStatus('current')
pppIfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 3), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfVci.setStatus('current')
pppIfCallMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noCall", 1), ("inCall", 2), ("outCall", 3))).clone('noCall')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfCallMode.setStatus('current')
pppIfFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("frameRelay", 2), ("atmLLC", 3), ("atmVc", 4))).clone('atmLLC')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfFrameType.setStatus('current')
pppIfNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfNumChannels.setStatus('current')
pppIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 7), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppIfRowStatus.setStatus('current')
pppLCPExtensionsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2), )
if mibBuilder.loadTexts: pppLCPExtensionsTable.setStatus('current')
pppLCPExtensionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1), )
pppInterfaceEntry.registerAugmentions(("ZHONE-COM-PPP-MIB", "pppLCPExtensionsEntry"))
pppLCPExtensionsEntry.setIndexNames(*pppInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: pppLCPExtensionsEntry.setStatus('current')
lcpExtReceiveAuthEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 1), EnableFlag().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtReceiveAuthEnable.setStatus('current')
lcpExtReceiveAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 2), ZhoneAuthenticationProtocol().clone('pap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtReceiveAuthProtocol.setStatus('current')
lcpExtSendAuthEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 3), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtSendAuthEnable.setStatus('current')
lcpExtSendAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 4), ZhoneAuthenticationProtocol().clone('pap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtSendAuthProtocol.setStatus('current')
lcpExtSendAuthIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtSendAuthIdentity.setStatus('current')
lcpExtQualityProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("lqr", 1))).clone('lqr')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtQualityProtocol.setStatus('current')
lcpExtMagicNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMagicNumber.setStatus('current')
lcpExtMaxPad = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMaxPad.setStatus('current')
lcpExtCallbackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 9), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtCallbackEnable.setStatus('current')
lcpExtCallbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("byAuth", 1), ("byDialStr", 2), ("byIdentifier", 3), ("byE164", 4), ("byName", 5))).clone('byAuth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtCallbackType.setStatus('current')
lcpExtCallbackDialString = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtCallbackDialString.setStatus('current')
lcpExtRestartTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtRestartTimer.setStatus('current')
lcpExtMaxConfigRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMaxConfigRetries.setStatus('current')
lcpExtMaxTerminateRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMaxTerminateRetries.setStatus('current')
lcpExtMaxFailureRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMaxFailureRetries.setStatus('current')
lcpExtMRUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 16), EnableFlag().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtMRUEnable.setStatus('current')
lcpExtACCMEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 17), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtACCMEnable.setStatus('current')
lcpExtPFCEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 18), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtPFCEnable.setStatus('current')
lcpExtACFCEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 19), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtACFCEnable.setStatus('current')
lcpExtFCSAltEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 20), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtFCSAltEnable.setStatus('current')
lcpExtSDPEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 21), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtSDPEnable.setStatus('current')
lcpExtNumModeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 22), EnableFlag().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lcpExtNumModeEnable.setStatus('current')
pppNCPExtensionsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3), )
if mibBuilder.loadTexts: pppNCPExtensionsTable.setStatus('current')
pppNCPExtensionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppNCPExtensionsEntry.setStatus('current')
ncpExtVJCompMaxSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 16)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtVJCompMaxSlotID.setStatus('current')
ncpExtVJCompSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 2), EnableFlag().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtVJCompSlotID.setStatus('current')
ncpExtIpAddrOptionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 3), EnableFlag().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtIpAddrOptionEnable.setStatus('current')
ncpExtRestartTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(3)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtRestartTimer.setStatus('current')
ncpExtMaxConfigRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtMaxConfigRetries.setStatus('current')
ncpExtMaxTerminateRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtMaxTerminateRetries.setStatus('current')
ncpExtFailureRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncpExtFailureRetries.setStatus('current')
pppNextAuthId = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppNextAuthId.setStatus('current')
pppAuthenticationTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5), )
if mibBuilder.loadTexts: pppAuthenticationTable.setStatus('current')
pppAuthenticationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1), ).setIndexNames((0, "ZHONE-COM-PPP-MIB", "pppAuthSubId"), (0, "ZHONE-COM-PPP-MIB", "pppAuthId"))
if mibBuilder.loadTexts: pppAuthenticationEntry.setStatus('current')
pppAuthSubId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: pppAuthSubId.setStatus('current')
pppAuthId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pppAuthId.setStatus('current')
pppAuthIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthIpIfIndex.setStatus('current')
pppAuthLgId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 4), InterfaceIndexOrZero().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthLgId.setStatus('current')
pppAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 5), Bits().clone(namedValues=NamedValues(("pap", 0), ("chap", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthProtocol.setStatus('current')
pppAuthPAPPeerID = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthPAPPeerID.setStatus('current')
pppAuthPAPPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthPAPPassword.setStatus('current')
pppAuthCHAPName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthCHAPName.setStatus('current')
pppAuthCHAPSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthCHAPSecret.setStatus('current')
pppAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2))).clone('valid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthStatus.setStatus('current')
pppAuthRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 12), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pppAuthRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-PPP-MIB", pppIfLowerIfIndex=pppIfLowerIfIndex, lcpExtReceiveAuthEnable=lcpExtReceiveAuthEnable, pppLCPExtensionsTable=pppLCPExtensionsTable, lcpExtCallbackEnable=lcpExtCallbackEnable, lcpExtCallbackDialString=lcpExtCallbackDialString, pppNextAuthId=pppNextAuthId, ncpExtVJCompMaxSlotID=ncpExtVJCompMaxSlotID, pppNCPExtensionsEntry=pppNCPExtensionsEntry, lcpExtMRUEnable=lcpExtMRUEnable, lcpExtSDPEnable=lcpExtSDPEnable, pppAuthId=pppAuthId, ncpExtIpAddrOptionEnable=ncpExtIpAddrOptionEnable, ncpExtMaxConfigRetries=ncpExtMaxConfigRetries, lcpExtMaxConfigRetries=lcpExtMaxConfigRetries, pppNCPExtensionsTable=pppNCPExtensionsTable, pppAuthenticationEntry=pppAuthenticationEntry, comPpp=comPpp, lcpExtReceiveAuthProtocol=lcpExtReceiveAuthProtocol, pppAuthStatus=pppAuthStatus, pppIfCallMode=pppIfCallMode, ncpExtFailureRetries=ncpExtFailureRetries, pppIfNumChannels=pppIfNumChannels, pppAuthSubId=pppAuthSubId, lcpExtCallbackType=lcpExtCallbackType, lcpExtFCSAltEnable=lcpExtFCSAltEnable, pppAuthCHAPName=pppAuthCHAPName, pppAuthPAPPassword=pppAuthPAPPassword, lcpExtACCMEnable=lcpExtACCMEnable, pppAuthenticationTable=pppAuthenticationTable, lcpExtMaxPad=lcpExtMaxPad, EnableFlag=EnableFlag, PYSNMP_MODULE_ID=comPpp, pppIfFrameType=pppIfFrameType, pppAuthCHAPSecret=pppAuthCHAPSecret, lcpExtQualityProtocol=lcpExtQualityProtocol, pppAuthIpIfIndex=pppAuthIpIfIndex, lcpExtSendAuthEnable=lcpExtSendAuthEnable, pppIfRowStatus=pppIfRowStatus, ncpExtMaxTerminateRetries=ncpExtMaxTerminateRetries, lcpExtACFCEnable=lcpExtACFCEnable, pppInterfaceTable=pppInterfaceTable, pppLCPExtensionsEntry=pppLCPExtensionsEntry, pppIfVpi=pppIfVpi, pppInterfaceEntry=pppInterfaceEntry, pppAuthLgId=pppAuthLgId, ZhoneAuthenticationProtocol=ZhoneAuthenticationProtocol, lcpExtSendAuthIdentity=lcpExtSendAuthIdentity, lcpExtNumModeEnable=lcpExtNumModeEnable, lcpExtPFCEnable=lcpExtPFCEnable, pppAuthPAPPeerID=pppAuthPAPPeerID, pppIfVci=pppIfVci, lcpExtMaxTerminateRetries=lcpExtMaxTerminateRetries, lcpExtSendAuthProtocol=lcpExtSendAuthProtocol, lcpExtMaxFailureRetries=lcpExtMaxFailureRetries, lcpExtRestartTimer=lcpExtRestartTimer, ncpExtRestartTimer=ncpExtRestartTimer, pppAuthProtocol=pppAuthProtocol, pppAuthRowStatus=pppAuthRowStatus, lcpExtMagicNumber=lcpExtMagicNumber, ncpExtVJCompSlotID=ncpExtVJCompSlotID)

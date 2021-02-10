#
# PySNMP MIB module WATCHGUARD-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-POLICY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Counter32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, enterprises, NotificationType, Gauge32, MibIdentifier, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "enterprises", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "ModuleIdentity")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
wgPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 4))
wgPolicyMIB.setRevisions(('2007-01-25 12:00',))
if mibBuilder.loadTexts: wgPolicyMIB.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgPolicyMIB.setOrganization('WatchGuard Technologies, Inc.')
wgPolicyToTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 4, 1))
if mibBuilder.loadTexts: wgPolicyToTunnel.setStatus('current')
wgPolicyStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 4, 2))
if mibBuilder.loadTexts: wgPolicyStatistics.setStatus('current')
wgPolicyToTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 3097, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyToTunnelNum.setStatus('current')
wgPolicyToTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 3097, 4, 1, 2), )
if mibBuilder.loadTexts: wgPolicyToTunnelTable.setStatus('current')
wgPolicyToTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1), ).setIndexNames((0, "WATCHGUARD-POLICY-MIB", "wgPolicyToTunnelPolicyID"), (0, "WATCHGUARD-POLICY-MIB", "wgPolicyToTunnelTunnelID"))
if mibBuilder.loadTexts: wgPolicyToTunnelEntry.setStatus('current')
wgPolicyToTunnelPolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyToTunnelPolicyID.setStatus('current')
wgPolicyToTunnelTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyToTunnelTunnelID.setStatus('current')
wgPolicyTableNum = MibScalar((1, 3, 6, 1, 4, 1, 3097, 4, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyTableNum.setStatus('current')
wgPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2), )
if mibBuilder.loadTexts: wgPolicyTable.setStatus('current')
wgPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1), ).setIndexNames((0, "WATCHGUARD-POLICY-MIB", "wgPolicyID"))
if mibBuilder.loadTexts: wgPolicyEntry.setStatus('current')
wgPolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyID.setStatus('current')
wgPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyName.setStatus('current')
wgPolicyBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyBytes.setStatus('current')
wgPolicyPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyPackets.setStatus('current')
wgPolicyIpsecDecryptErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecDecryptErr.setStatus('current')
wgPolicyIpsecAuthErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecAuthErr.setStatus('current')
wgPolicyIpsecReplayErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecReplayErr.setStatus('current')
wgPolicyIpsecPadErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecPadErr.setStatus('current')
wgPolicyIpsecPolicyErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecPolicyErr.setStatus('current')
wgPolicyFwDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyFwDisc.setStatus('current')
wgPolicyOtherDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyOtherDisc.setStatus('current')
wgPolicyActiveStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyActiveStreams.setStatus('current')
wgPolicyIpsecDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyIpsecDisc.setStatus('current')
wgPolicyDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyDisc.setStatus('current')
wgPolicyNumTunl = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyNumTunl.setStatus('current')
wgPolicySingleCntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicySingleCntrNum.setStatus('current')
wgPolicyLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyLogging.setStatus('current')
wgPolicyCurrActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgPolicyCurrActiveConns.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-POLICY-MIB", PYSNMP_MODULE_ID=wgPolicyMIB, wgPolicyPackets=wgPolicyPackets, wgPolicyIpsecDisc=wgPolicyIpsecDisc, wgPolicyToTunnelTable=wgPolicyToTunnelTable, wgPolicyOtherDisc=wgPolicyOtherDisc, wgPolicyIpsecDecryptErr=wgPolicyIpsecDecryptErr, wgPolicyID=wgPolicyID, wgPolicyStatistics=wgPolicyStatistics, wgPolicyLogging=wgPolicyLogging, wgPolicyToTunnelEntry=wgPolicyToTunnelEntry, wgPolicyToTunnelNum=wgPolicyToTunnelNum, wgPolicyName=wgPolicyName, wgPolicyToTunnelPolicyID=wgPolicyToTunnelPolicyID, wgPolicyNumTunl=wgPolicyNumTunl, wgPolicyActiveStreams=wgPolicyActiveStreams, wgPolicyIpsecPadErr=wgPolicyIpsecPadErr, wgPolicyTable=wgPolicyTable, wgPolicyIpsecReplayErr=wgPolicyIpsecReplayErr, wgPolicyToTunnel=wgPolicyToTunnel, wgPolicyTableNum=wgPolicyTableNum, wgPolicyToTunnelTunnelID=wgPolicyToTunnelTunnelID, wgPolicyMIB=wgPolicyMIB, wgPolicyDisc=wgPolicyDisc, wgPolicyFwDisc=wgPolicyFwDisc, wgPolicySingleCntrNum=wgPolicySingleCntrNum, wgPolicyIpsecAuthErr=wgPolicyIpsecAuthErr, wgPolicyIpsecPolicyErr=wgPolicyIpsecPolicyErr, wgPolicyCurrActiveConns=wgPolicyCurrActiveConns, wgPolicyEntry=wgPolicyEntry, wgPolicyBytes=wgPolicyBytes)

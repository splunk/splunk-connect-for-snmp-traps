#
# PySNMP MIB module RFC1269-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1269-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, IpAddress, Gauge32, ModuleIdentity, iso, ObjectIdentity, NotificationType, Unsigned32, mib_2, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "IpAddress", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "NotificationType", "Unsigned32", "mib-2", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bgp = MibIdentifier((1, 3, 6, 1, 2, 1, 15))
bgpVersion = MibScalar((1, 3, 6, 1, 2, 1, 15, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpVersion.setStatus('mandatory')
bgpLocalAs = MibScalar((1, 3, 6, 1, 2, 1, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpLocalAs.setStatus('mandatory')
bgpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 15, 3), )
if mibBuilder.loadTexts: bgpPeerTable.setStatus('mandatory')
bgpIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 15, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpIdentifier.setStatus('mandatory')
bgpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 3, 1), ).setIndexNames((0, "RFC1269-MIB", "bgpPeerRemoteAddr"))
if mibBuilder.loadTexts: bgpPeerEntry.setStatus('mandatory')
bgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerIdentifier.setStatus('mandatory')
bgpPeerState = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerState.setStatus('mandatory')
bgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerAdminStatus.setStatus('mandatory')
bgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerNegotiatedVersion.setStatus('mandatory')
bgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalAddr.setStatus('mandatory')
bgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalPort.setStatus('mandatory')
bgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAddr.setStatus('mandatory')
bgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemotePort.setStatus('mandatory')
bgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAs.setStatus('mandatory')
bgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdates.setStatus('mandatory')
bgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutUpdates.setStatus('mandatory')
bgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInTotalMessages.setStatus('mandatory')
bgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutTotalMessages.setStatus('mandatory')
bgpPeerLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLastError.setStatus('mandatory')
bgpRcvdPathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 5), )
if mibBuilder.loadTexts: bgpRcvdPathAttrTable.setStatus('mandatory')
bgpPathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 5, 1), ).setIndexNames((0, "RFC1269-MIB", "bgpPathAttrDestNetwork"), (0, "RFC1269-MIB", "bgpPathAttrPeer"))
if mibBuilder.loadTexts: bgpPathAttrEntry.setStatus('mandatory')
bgpPathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrPeer.setStatus('mandatory')
bgpPathAttrDestNetwork = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrDestNetwork.setStatus('mandatory')
bgpPathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrOrigin.setStatus('mandatory')
bgpPathAttrASPath = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrASPath.setStatus('mandatory')
bgpPathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrNextHop.setStatus('mandatory')
bgpPathAttrInterASMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrInterASMetric.setStatus('mandatory')
bgpEstablished = NotificationType((1, 3, 6, 1, 2, 1, 15) + (0,1)).setObjects(("RFC1269-MIB", "bgpPeerRemoteAddr"), ("RFC1269-MIB", "bgpPeerLastError"), ("RFC1269-MIB", "bgpPeerState"))
bgpBackwardTransition = NotificationType((1, 3, 6, 1, 2, 1, 15) + (0,2)).setObjects(("RFC1269-MIB", "bgpPeerRemoteAddr"), ("RFC1269-MIB", "bgpPeerLastError"), ("RFC1269-MIB", "bgpPeerState"))
mibBuilder.exportSymbols("RFC1269-MIB", bgpPathAttrDestNetwork=bgpPathAttrDestNetwork, bgpPathAttrEntry=bgpPathAttrEntry, bgpPeerLocalPort=bgpPeerLocalPort, bgpLocalAs=bgpLocalAs, bgpPathAttrASPath=bgpPathAttrASPath, bgpPeerTable=bgpPeerTable, bgpPathAttrNextHop=bgpPathAttrNextHop, bgpPathAttrOrigin=bgpPathAttrOrigin, bgpPeerOutTotalMessages=bgpPeerOutTotalMessages, bgpPeerInUpdates=bgpPeerInUpdates, bgpPeerIdentifier=bgpPeerIdentifier, bgpRcvdPathAttrTable=bgpRcvdPathAttrTable, bgpPeerNegotiatedVersion=bgpPeerNegotiatedVersion, bgpPathAttrInterASMetric=bgpPathAttrInterASMetric, bgpBackwardTransition=bgpBackwardTransition, bgpVersion=bgpVersion, bgpPeerOutUpdates=bgpPeerOutUpdates, bgpPeerState=bgpPeerState, bgpEstablished=bgpEstablished, bgpIdentifier=bgpIdentifier, bgpPeerLastError=bgpPeerLastError, bgpPeerEntry=bgpPeerEntry, bgpPeerRemoteAs=bgpPeerRemoteAs, bgpPeerInTotalMessages=bgpPeerInTotalMessages, bgpPeerLocalAddr=bgpPeerLocalAddr, bgp=bgp, bgpPeerRemoteAddr=bgpPeerRemoteAddr, bgpPathAttrPeer=bgpPathAttrPeer, bgpPeerRemotePort=bgpPeerRemotePort, bgpPeerAdminStatus=bgpPeerAdminStatus)

#
# PySNMP MIB module A3COM-HUAWEI-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huawei, hwLocal, hwInternetProtocol = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huawei", "hwLocal", "hwInternetProtocol")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Bits, MibIdentifier, ObjectIdentity, TimeTicks, Counter32, NotificationType, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rIp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1))
ipTooShorts = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTooShorts.setStatus('mandatory')
ipTooSmalls = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTooSmalls.setStatus('mandatory')
ipBadVersions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadVersions.setStatus('mandatory')
ipBadChecksums = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadChecksums.setStatus('mandatory')
ipBadLens = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadLens.setStatus('mandatory')
ipBadHeadLens = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadHeadLens.setStatus('mandatory')
ipBadOptions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadOptions.setStatus('mandatory')
ipFragDroppeds = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFragDroppeds.setStatus('mandatory')
ipRawOuts = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRawOuts.setStatus('mandatory')
ipRouteBadRedirects = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteBadRedirects.setStatus('mandatory')
ipRouteDynamics = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteDynamics.setStatus('mandatory')
ipRouteNewGateways = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteNewGateways.setStatus('mandatory')
ipRouteUnreachs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteUnreachs.setStatus('mandatory')
ipRouteWilds = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteWilds.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-HUAWEI-IP-MIB", ipBadHeadLens=ipBadHeadLens, ipBadLens=ipBadLens, ipRouteDynamics=ipRouteDynamics, ipTooShorts=ipTooShorts, ipFragDroppeds=ipFragDroppeds, ipTooSmalls=ipTooSmalls, ipBadVersions=ipBadVersions, ipBadChecksums=ipBadChecksums, rIp=rIp, ipRouteBadRedirects=ipRouteBadRedirects, ipRouteNewGateways=ipRouteNewGateways, ipBadOptions=ipBadOptions, ipRouteWilds=ipRouteWilds, ipRouteUnreachs=ipRouteUnreachs, ipRawOuts=ipRawOuts)

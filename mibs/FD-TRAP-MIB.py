#
# PySNMP MIB module FD-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FD-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
epon, = mibBuilder.importSymbols("EPON-EOC-MIB", "epon")
onuIdExhaust, linkIdExhaust, linkOnLineStatus = mibBuilder.importSymbols("FD-OLT-MIB", "onuIdExhaust", "linkIdExhaust", "linkOnLineStatus")
uniPortLink, onuOnLineStatus, uniPortRstpState = mibBuilder.importSymbols("FD-ONU-MIB", "uniPortLink", "onuOnLineStatus", "uniPortRstpState")
oltTrafficChangeVal, onuTrafficChangeVal, swSniPortTrafficChangeVal = mibBuilder.importSymbols("FD-PERFORMANCE-MIB", "oltTrafficChangeVal", "onuTrafficChangeVal", "swSniPortTrafficChangeVal")
sfpPlugStauts, swPortLinkState = mibBuilder.importSymbols("FD-SWITCH-MIB", "sfpPlugStauts", "swPortLinkState")
fanStatusBit, nonAuthOnuMac, ponCardRunningStatus, powerStatusBit = mibBuilder.importSymbols("FD-SYSTEM-MIB", "fanStatusBit", "nonAuthOnuMac", "ponCardRunningStatus", "powerStatusBit")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, IpAddress, Gauge32, iso, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, Integer32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "Gauge32", "iso", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eponTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6))
if mibBuilder.loadTexts: eponTraps.setLastUpdated('201005271056Z')
if mibBuilder.loadTexts: eponTraps.setOrganization('epon eoc factory.')
eponTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0))
sniSFPStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 1)).setObjects(("FD-SWITCH-MIB", "sfpPlugStauts"))
if mibBuilder.loadTexts: sniSFPStatusChange.setStatus('current')
sniPortLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 2)).setObjects(("FD-SWITCH-MIB", "swPortLinkState"))
if mibBuilder.loadTexts: sniPortLinkChange.setStatus('current')
powerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 3)).setObjects(("FD-SYSTEM-MIB", "powerStatusBit"))
if mibBuilder.loadTexts: powerStatusChange.setStatus('current')
fanStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 4)).setObjects(("FD-SYSTEM-MIB", "fanStatusBit"))
if mibBuilder.loadTexts: fanStatusChange.setStatus('current')
ponRunningStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 5)).setObjects(("FD-SYSTEM-MIB", "ponCardRunningStatus"))
if mibBuilder.loadTexts: ponRunningStatusChange.setStatus('current')
onuLinkStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 6)).setObjects(("FD-OLT-MIB", "linkOnLineStatus"))
if mibBuilder.loadTexts: onuLinkStatusChange.setStatus('current')
onuOnlineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 7)).setObjects(("FD-ONU-MIB", "onuOnLineStatus"))
if mibBuilder.loadTexts: onuOnlineStatusChange.setStatus('current')
onuPortStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 8)).setObjects(("FD-ONU-MIB", "uniPortLink"))
if mibBuilder.loadTexts: onuPortStatusChange.setStatus('current')
swSniPortTrafficChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 9)).setObjects(("FD-PERFORMANCE-MIB", "swSniPortTrafficChangeVal"))
if mibBuilder.loadTexts: swSniPortTrafficChange.setStatus('current')
oltTrafficChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 10)).setObjects(("FD-PERFORMANCE-MIB", "oltTrafficChangeVal"))
if mibBuilder.loadTexts: oltTrafficChange.setStatus('current')
onuTrafficChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 11)).setObjects(("FD-PERFORMANCE-MIB", "onuTrafficChangeVal"))
if mibBuilder.loadTexts: onuTrafficChange.setStatus('current')
linkIdResourceExhaust = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 12)).setObjects(("FD-OLT-MIB", "linkIdExhaust"))
if mibBuilder.loadTexts: linkIdResourceExhaust.setStatus('current')
onuIdResourceExhaust = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 13)).setObjects(("FD-OLT-MIB", "onuIdExhaust"))
if mibBuilder.loadTexts: onuIdResourceExhaust.setStatus('current')
illegalRegisterAlarm = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 14)).setObjects(("FD-SYSTEM-MIB", "nonAuthOnuMac"))
if mibBuilder.loadTexts: illegalRegisterAlarm.setStatus('current')
onuPortRstpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 15)).setObjects(("FD-ONU-MIB", "uniPortRstpState"))
if mibBuilder.loadTexts: onuPortRstpStateChange.setStatus('current')
fdTrapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1))
fdTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 1))
fdTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 1, 1)).setObjects(("FD-TRAP-MIB", "sniSFPStatusChange"), ("FD-TRAP-MIB", "sniPortLinkChange"), ("FD-TRAP-MIB", "powerStatusChange"), ("FD-TRAP-MIB", "fanStatusChange"), ("FD-TRAP-MIB", "ponRunningStatusChange"), ("FD-TRAP-MIB", "onuLinkStatusChange"), ("FD-TRAP-MIB", "onuOnlineStatusChange"), ("FD-TRAP-MIB", "onuPortStatusChange"), ("FD-TRAP-MIB", "swSniPortTrafficChange"), ("FD-TRAP-MIB", "oltTrafficChange"), ("FD-TRAP-MIB", "onuTrafficChange"), ("FD-TRAP-MIB", "onuPortRstpStateChange"), ("FD-TRAP-MIB", "illegalRegisterAlarm"), ("FD-TRAP-MIB", "linkIdResourceExhaust"), ("FD-TRAP-MIB", "onuIdResourceExhaust"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdTrapGroup = fdTrapGroup.setStatus('current')
fdTrapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 2))
fdTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 2, 1)).setObjects(("FD-TRAP-MIB", "fdTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdTrapCompliance = fdTrapCompliance.setStatus('current')
mibBuilder.exportSymbols("FD-TRAP-MIB", illegalRegisterAlarm=illegalRegisterAlarm, onuPortStatusChange=onuPortStatusChange, onuPortRstpStateChange=onuPortRstpStateChange, fdTrapGroups=fdTrapGroups, fdTrapCompliances=fdTrapCompliances, onuIdResourceExhaust=onuIdResourceExhaust, ponRunningStatusChange=ponRunningStatusChange, fdTrapConformance=fdTrapConformance, linkIdResourceExhaust=linkIdResourceExhaust, onuOnlineStatusChange=onuOnlineStatusChange, fdTrapCompliance=fdTrapCompliance, PYSNMP_MODULE_ID=eponTraps, eponTraps=eponTraps, powerStatusChange=powerStatusChange, eponTrapsPrefix=eponTrapsPrefix, oltTrafficChange=oltTrafficChange, fdTrapGroup=fdTrapGroup, sniPortLinkChange=sniPortLinkChange, sniSFPStatusChange=sniSFPStatusChange, onuLinkStatusChange=onuLinkStatusChange, onuTrafficChange=onuTrafficChange, swSniPortTrafficChange=swSniPortTrafficChange, fanStatusChange=fanStatusChange)

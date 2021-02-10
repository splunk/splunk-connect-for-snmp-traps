#
# PySNMP MIB module FORTINET-TRAP-MIB-280 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-TRAP-MIB-280
# Produced by pysmi-0.3.4 at Mon Apr 29 19:01:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
fnTraps, fnIpsSigSrcIp, fnSysSerial, fnIpsSigId = mibBuilder.importSymbols("FORTINET-MIB-280", "fnTraps", "fnIpsSigSrcIp", "fnSysSerial", "fnIpsSigId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ObjectIdentity, iso, ModuleIdentity, IpAddress, MibIdentifier, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fnTrapCpuHigh = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 101)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapCpuHigh.setStatus('current')
fnTrapMemLow = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 102)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapMemLow.setStatus('current')
fnTrapLogFull = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 103)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapLogFull.setStatus('current')
fnTrapIpChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 201)).setObjects(("FORTINET-MIB-280", "fnSysSerial"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fnTrapIpChange.setStatus('current')
fnTrapVpnTunUp = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 301)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapVpnTunUp.setStatus('current')
fnTrapVpnTunDown = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 302)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapVpnTunDown.setStatus('current')
fnTrapHaSwitch = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 401)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapHaSwitch.setStatus('current')
fnTrapHaStateChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 402)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapHaStateChange.setStatus('current')
fnTrapIdsSynFlood = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 501)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapIdsSynFlood.setStatus('current')
fnTrapIdsPortScan = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 502)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapIdsPortScan.setStatus('current')
fnTrapIpsSignature = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 503)).setObjects(("FORTINET-MIB-280", "fnSysSerial"), ("FORTINET-MIB-280", "fnIpsSigId"), ("FORTINET-MIB-280", "fnIpsSigSrcIp"))
if mibBuilder.loadTexts: fnTrapIpsSignature.setStatus('current')
fnTrapIpsAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 504)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapIpsAnomaly.setStatus('current')
fnTrapAvEvent = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 601)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapAvEvent.setStatus('current')
fnTrapBridge = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 701)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapBridge.setStatus('current')
fnTrapImTableFull = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 801)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapImTableFull.setStatus('current')
fnTrapFlgEventCount = NotificationType((1, 3, 6, 1, 4, 1, 12356, 0, 901)).setObjects(("FORTINET-MIB-280", "fnSysSerial"))
if mibBuilder.loadTexts: fnTrapFlgEventCount.setStatus('current')
mibBuilder.exportSymbols("FORTINET-TRAP-MIB-280", fnTrapVpnTunUp=fnTrapVpnTunUp, fnTrapIpsSignature=fnTrapIpsSignature, fnTrapHaStateChange=fnTrapHaStateChange, fnTrapIdsSynFlood=fnTrapIdsSynFlood, fnTrapImTableFull=fnTrapImTableFull, fnTrapCpuHigh=fnTrapCpuHigh, fnTrapLogFull=fnTrapLogFull, fnTrapIpsAnomaly=fnTrapIpsAnomaly, fnTrapHaSwitch=fnTrapHaSwitch, fnTrapBridge=fnTrapBridge, fnTrapAvEvent=fnTrapAvEvent, fnTrapMemLow=fnTrapMemLow, fnTrapIdsPortScan=fnTrapIdsPortScan, fnTrapIpChange=fnTrapIpChange, fnTrapFlgEventCount=fnTrapFlgEventCount, fnTrapVpnTunDown=fnTrapVpnTunDown)

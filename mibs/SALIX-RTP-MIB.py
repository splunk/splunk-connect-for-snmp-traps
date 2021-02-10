#
# PySNMP MIB module SALIX-RTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-RTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
platform1, = mibBuilder.importSymbols("SALIX-MIB", "platform1")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Gauge32, ObjectIdentity, MibIdentifier, Bits, IpAddress, ModuleIdentity, NotificationType, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
salixRtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1))
if mibBuilder.loadTexts: salixRtpMIB.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixRtpMIB.setOrganization('SALIX Technologies')
salixRtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1))
salixRtpMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 2))
salixRtpMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3))
salixRtpMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 2, 0))
salixRtpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1), )
if mibBuilder.loadTexts: salixRtpStatsTable.setStatus('current')
salixRtpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1), ).setIndexNames((0, "SALIX-RTP-MIB", "salixRtpStatsSrcIpAddress"), (0, "SALIX-RTP-MIB", "salixRtpStatsSrcPort"), (0, "SALIX-RTP-MIB", "salixRtpStatsDestIpAddress"), (0, "SALIX-RTP-MIB", "salixRtpStatsDestPort"))
if mibBuilder.loadTexts: salixRtpStatsEntry.setStatus('current')
salixRtpStatsSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: salixRtpStatsSrcIpAddress.setStatus('current')
salixRtpStatsSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: salixRtpStatsSrcPort.setStatus('current')
salixRtpStatsDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 3), IpAddress())
if mibBuilder.loadTexts: salixRtpStatsDestIpAddress.setStatus('current')
salixRtpStatsDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: salixRtpStatsDestPort.setStatus('current')
salixRtpStatsPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsPktsSent.setStatus('current')
salixRtpStatsPktsRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsPktsRecv.setStatus('current')
salixRtpStatsPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsPktsDropped.setStatus('current')
salixRtpStatsBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsBytesSent.setStatus('current')
salixRtpStatsBytesRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsBytesRecv.setStatus('current')
salixRtpStatsBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsBytesDropped.setStatus('current')
salixRtpStatsSignalPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsSignalPktsSent.setStatus('current')
salixRtpStatsSignalPktsRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsSignalPktsRecv.setStatus('current')
salixRtpStatsSignalPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsSignalPktsDropped.setStatus('current')
salixRtpStatsSignalBytesRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsSignalBytesRecv.setStatus('current')
salixRtpStatsAudioPktsRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsAudioPktsRecv.setStatus('current')
salixRtpStatsAudioBytesRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsAudioBytesRecv.setStatus('current')
salixRtpStatsEstimatedAvgLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixRtpStatsEstimatedAvgLatency.setStatus('current')
salixRtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 1))
salixRtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 2))
salixRtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 1, 3)).setObjects(("SALIX-RTP-MIB", "salixRtpStatsPktsSent"), ("SALIX-RTP-MIB", "salixRtpStatsPktsRecv"), ("SALIX-RTP-MIB", "salixRtpStatsPktsDropped"), ("SALIX-RTP-MIB", "salixRtpStatsBytesSent"), ("SALIX-RTP-MIB", "salixRtpStatsBytesRecv"), ("SALIX-RTP-MIB", "salixRtpStatsBytesDropped"), ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsSent"), ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsRecv"), ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsDropped"), ("SALIX-RTP-MIB", "salixRtpStatsSignalBytesRecv"), ("SALIX-RTP-MIB", "salixRtpStatsAudioPktsRecv"), ("SALIX-RTP-MIB", "salixRtpStatsAudioBytesRecv"), ("SALIX-RTP-MIB", "salixRtpStatsEstimatedAvgLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixRtpGroup = salixRtpGroup.setStatus('current')
salixRtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 2, 1)).setObjects(("SALIX-RTP-MIB", "salixRtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixRtpCompliance = salixRtpCompliance.setStatus('current')
mibBuilder.exportSymbols("SALIX-RTP-MIB", salixRtpStatsDestIpAddress=salixRtpStatsDestIpAddress, salixRtpStatsEntry=salixRtpStatsEntry, salixRtpStatsDestPort=salixRtpStatsDestPort, salixRtpStatsPktsSent=salixRtpStatsPktsSent, salixRtpStatsSrcPort=salixRtpStatsSrcPort, salixRtpCompliances=salixRtpCompliances, salixRtpStatsSignalPktsDropped=salixRtpStatsSignalPktsDropped, salixRtpStatsPktsDropped=salixRtpStatsPktsDropped, salixRtpMIBCompliance=salixRtpMIBCompliance, salixRtpStatsBytesSent=salixRtpStatsBytesSent, salixRtpMIBObjects=salixRtpMIBObjects, salixRtpStatsTable=salixRtpStatsTable, salixRtpMIB=salixRtpMIB, salixRtpGroup=salixRtpGroup, salixRtpStatsAudioBytesRecv=salixRtpStatsAudioBytesRecv, salixRtpCompliance=salixRtpCompliance, salixRtpStatsBytesDropped=salixRtpStatsBytesDropped, salixRtpGroups=salixRtpGroups, salixRtpMIBTraps=salixRtpMIBTraps, salixRtpMIBTrapPrefix=salixRtpMIBTrapPrefix, salixRtpStatsAudioPktsRecv=salixRtpStatsAudioPktsRecv, salixRtpStatsEstimatedAvgLatency=salixRtpStatsEstimatedAvgLatency, salixRtpStatsPktsRecv=salixRtpStatsPktsRecv, salixRtpStatsSignalPktsRecv=salixRtpStatsSignalPktsRecv, PYSNMP_MODULE_ID=salixRtpMIB, salixRtpStatsSignalBytesRecv=salixRtpStatsSignalBytesRecv, salixRtpStatsSignalPktsSent=salixRtpStatsSignalPktsSent, salixRtpStatsSrcIpAddress=salixRtpStatsSrcIpAddress, salixRtpStatsBytesRecv=salixRtpStatsBytesRecv)

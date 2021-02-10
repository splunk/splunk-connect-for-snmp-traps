#
# PySNMP MIB module TPLINK-DHCPSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-DHCPSERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, IpAddress, TimeTicks, Counter32, Gauge32, ObjectIdentity, Bits, Counter64, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkDhcpServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 38))
tplinkDhcpServerMIB.setRevisions(('2012-11-29 00:00',))
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setLastUpdated('201211290000Z')
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setOrganization('TP-LINK')
tplinkDhcpServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1))
tplinkDhcpServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 2))
tpDhcpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerEnable.setStatus('current')
tpDhcpServerVendorClassId = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerVendorClassId.setStatus('current')
tpDhcpServerCapwapAcIp = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerCapwapAcIp.setStatus('current')
tpDhcpServerUnusedIpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4), )
if mibBuilder.loadTexts: tpDhcpServerUnusedIpTable.setStatus('current')
tpDhcpServerUnusedIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerUnusedStartIp"))
if mibBuilder.loadTexts: tpDhcpServerUnusedIpEntry.setStatus('current')
tpDhcpServerUnusedStartIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerUnusedStartIp.setStatus('current')
tpDhcpServerUnusedEndIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerUnusedEndIp.setStatus('current')
tpDhcpServerUnusedIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerUnusedIpStatus.setStatus('current')
tpDhcpServerAddrPoolTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5), )
if mibBuilder.loadTexts: tpDhcpServerAddrPoolTable.setStatus('current')
tpDhcpServerAddrPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerAddrPoolNetwork"))
if mibBuilder.loadTexts: tpDhcpServerAddrPoolEntry.setStatus('current')
tpDhcpServerAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolName.setStatus('current')
tpDhcpServerAddrPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetwork.setStatus('current')
tpDhcpServerAddrPoolSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolSubnetMask.setStatus('current')
tpDhcpServerAddrPoolRentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolRentTime.setStatus('current')
tpDhcpServerAddrPoolGateWayA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayA.setStatus('current')
tpDhcpServerAddrPoolGateWayB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayB.setStatus('current')
tpDhcpServerAddrPoolGateWayC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayC.setStatus('current')
tpDhcpServerAddrPoolGateWayD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayD.setStatus('current')
tpDhcpServerAddrPoolGateWayE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayE.setStatus('current')
tpDhcpServerAddrPoolGateWayF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayF.setStatus('current')
tpDhcpServerAddrPoolGateWayG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayG.setStatus('current')
tpDhcpServerAddrPoolGateWayH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayH.setStatus('current')
tpDhcpServerAddrPoolDnsA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsA.setStatus('current')
tpDhcpServerAddrPoolDnsB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsB.setStatus('current')
tpDhcpServerAddrPoolDnsC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 15), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsC.setStatus('current')
tpDhcpServerAddrPoolDnsD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsD.setStatus('current')
tpDhcpServerAddrPoolDnsE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsE.setStatus('current')
tpDhcpServerAddrPoolDnsF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsF.setStatus('current')
tpDhcpServerAddrPoolDnsG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsG.setStatus('current')
tpDhcpServerAddrPoolDnsH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsH.setStatus('current')
tpDhcpServerAddrPoolNBNServerA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 21), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerA.setStatus('current')
tpDhcpServerAddrPoolNBNServerB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 22), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerB.setStatus('current')
tpDhcpServerAddrPoolNBNServerC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 23), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerC.setStatus('current')
tpDhcpServerAddrPoolNBNServerD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 24), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerD.setStatus('current')
tpDhcpServerAddrPoolNBNServerE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 25), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerE.setStatus('current')
tpDhcpServerAddrPoolNBNServerF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 26), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerF.setStatus('current')
tpDhcpServerAddrPoolNBNServerG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 27), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerG.setStatus('current')
tpDhcpServerAddrPoolNBNServerH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 28), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerH.setStatus('current')
tpDhcpServerAddrPoolNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("none", 0), ("broadcast", 1), ("peer-to-peer", 2), ("mixed", 4), ("hybrid", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetbiosNodeType.setStatus('current')
tpDhcpServerAddrPoolNextServer = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 30), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNextServer.setStatus('current')
tpDhcpServerAddrPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDomainName.setStatus('current')
tpDhcpServerAddrPoolBootfile = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 32), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolBootfile.setStatus('current')
tpDhcpServerAddrPoolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 33), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolStatus.setStatus('current')
tpDhcpServerStaticBindTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6), )
if mibBuilder.loadTexts: tpDhcpServerStaticBindTable.setStatus('current')
tpDhcpServerStaticBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindIpAddr"))
if mibBuilder.loadTexts: tpDhcpServerStaticBindEntry.setStatus('current')
tpDhcpServerStaticAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticAddrPoolName.setStatus('current')
tpDhcpServerBindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerBindIpAddr.setStatus('current')
tpDhcpServerStaticClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticClientId.setStatus('current')
tpDhcpServerMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerMacAddr.setStatus('current')
tpDhcpServerHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-2, -1, 1, 6))).clone(namedValues=NamedValues(("ascii", -2), ("hex", -1), ("ethernet", 1), ("ieee802", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerHardwareType.setStatus('current')
tpDhcpServerStaticBindStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticBindStatus.setStatus('current')
tpDhcpServerBindingTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7), )
if mibBuilder.loadTexts: tpDhcpServerBindingTable.setStatus('current')
tpDhcpServerBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindingIp"))
if mibBuilder.loadTexts: tpDhcpServerBindingEntry.setStatus('current')
tpDhcpServerBindingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingIp.setStatus('current')
tpDhcpServerBindingClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingClientId.setStatus('current')
tpDhcpServerBindingMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingMac.setStatus('current')
tpDhcpServerBindingType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("automatic", 0), ("manual", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingType.setStatus('current')
tpDhcpServerBindingRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingRemainTime.setStatus('current')
tpDhcpServerBindingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerBindingStatus.setStatus('current')
tpDhcpServerBindingClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("remain", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerBindingClear.setStatus('current')
tpDhcpServerStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9))
tpDhcpServerStatisticsBootRequest = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootRequest.setStatus('current')
tpDhcpServerStatisticsDiscover = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsDiscover.setStatus('current')
tpDhcpServerStatisticsRequest = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsRequest.setStatus('current')
tpDhcpServerStatisticsDecline = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsDecline.setStatus('current')
tpDhcpServerStatisticsRelease = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsRelease.setStatus('current')
tpDhcpServerStatisticsInform = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsInform.setStatus('current')
tpDhcpServerStatisticsBootReply = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootReply.setStatus('current')
tpDhcpServerStatisticsOffer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsOffer.setStatus('current')
tpDhcpServerStatisticsAck = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsAck.setStatus('current')
tpDhcpServerStatisticsNak = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsNak.setStatus('current')
tpDhcpServerStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("remain", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerStatisticsClear.setStatus('current')
tpDhcpServerPingPackets = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerPingPackets.setStatus('current')
tpDhcpServerPingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerPingTimeout.setStatus('current')
mibBuilder.exportSymbols("TPLINK-DHCPSERVER-MIB", tplinkDhcpServerMIB=tplinkDhcpServerMIB, tpDhcpServerMacAddr=tpDhcpServerMacAddr, tpDhcpServerAddrPoolNetbiosNodeType=tpDhcpServerAddrPoolNetbiosNodeType, tpDhcpServerAddrPoolBootfile=tpDhcpServerAddrPoolBootfile, tpDhcpServerBindingEntry=tpDhcpServerBindingEntry, tpDhcpServerUnusedIpEntry=tpDhcpServerUnusedIpEntry, tpDhcpServerAddrPoolNetwork=tpDhcpServerAddrPoolNetwork, tpDhcpServerStatisticsDecline=tpDhcpServerStatisticsDecline, tpDhcpServerAddrPoolGateWayF=tpDhcpServerAddrPoolGateWayF, tpDhcpServerAddrPoolNBNServerG=tpDhcpServerAddrPoolNBNServerG, tpDhcpServerAddrPoolDomainName=tpDhcpServerAddrPoolDomainName, tpDhcpServerStaticBindTable=tpDhcpServerStaticBindTable, tpDhcpServerAddrPoolGateWayA=tpDhcpServerAddrPoolGateWayA, tpDhcpServerAddrPoolGateWayB=tpDhcpServerAddrPoolGateWayB, tpDhcpServerAddrPoolStatus=tpDhcpServerAddrPoolStatus, tpDhcpServerAddrPoolEntry=tpDhcpServerAddrPoolEntry, tpDhcpServerUnusedStartIp=tpDhcpServerUnusedStartIp, tpDhcpServerAddrPoolDnsH=tpDhcpServerAddrPoolDnsH, tpDhcpServerAddrPoolSubnetMask=tpDhcpServerAddrPoolSubnetMask, tpDhcpServerAddrPoolNBNServerB=tpDhcpServerAddrPoolNBNServerB, tpDhcpServerAddrPoolGateWayD=tpDhcpServerAddrPoolGateWayD, tpDhcpServerUnusedIpStatus=tpDhcpServerUnusedIpStatus, tpDhcpServerStatisticsOffer=tpDhcpServerStatisticsOffer, tpDhcpServerStaticClientId=tpDhcpServerStaticClientId, tpDhcpServerAddrPoolNextServer=tpDhcpServerAddrPoolNextServer, tpDhcpServerStatisticsBootReply=tpDhcpServerStatisticsBootReply, tpDhcpServerStatisticsDiscover=tpDhcpServerStatisticsDiscover, tpDhcpServerUnusedEndIp=tpDhcpServerUnusedEndIp, tpDhcpServerStaticBindStatus=tpDhcpServerStaticBindStatus, tpDhcpServerAddrPoolDnsD=tpDhcpServerAddrPoolDnsD, tpDhcpServerStatisticsAck=tpDhcpServerStatisticsAck, tpDhcpServerStatisticsBootRequest=tpDhcpServerStatisticsBootRequest, tpDhcpServerBindingIp=tpDhcpServerBindingIp, tplinkDhcpServerMIBObjects=tplinkDhcpServerMIBObjects, tpDhcpServerAddrPoolGateWayH=tpDhcpServerAddrPoolGateWayH, PYSNMP_MODULE_ID=tplinkDhcpServerMIB, tpDhcpServerAddrPoolDnsC=tpDhcpServerAddrPoolDnsC, tpDhcpServerStatistics=tpDhcpServerStatistics, tpDhcpServerBindingMac=tpDhcpServerBindingMac, tplinkDhcpServerNotifications=tplinkDhcpServerNotifications, tpDhcpServerBindingStatus=tpDhcpServerBindingStatus, tpDhcpServerStatisticsNak=tpDhcpServerStatisticsNak, tpDhcpServerAddrPoolNBNServerE=tpDhcpServerAddrPoolNBNServerE, tpDhcpServerBindingType=tpDhcpServerBindingType, tpDhcpServerBindingTable=tpDhcpServerBindingTable, tpDhcpServerAddrPoolDnsA=tpDhcpServerAddrPoolDnsA, tpDhcpServerAddrPoolDnsB=tpDhcpServerAddrPoolDnsB, tpDhcpServerAddrPoolNBNServerC=tpDhcpServerAddrPoolNBNServerC, tpDhcpServerStaticAddrPoolName=tpDhcpServerStaticAddrPoolName, tpDhcpServerBindingClear=tpDhcpServerBindingClear, tpDhcpServerAddrPoolGateWayE=tpDhcpServerAddrPoolGateWayE, tpDhcpServerEnable=tpDhcpServerEnable, tpDhcpServerAddrPoolDnsE=tpDhcpServerAddrPoolDnsE, tpDhcpServerStatisticsInform=tpDhcpServerStatisticsInform, tpDhcpServerPingTimeout=tpDhcpServerPingTimeout, tpDhcpServerAddrPoolGateWayC=tpDhcpServerAddrPoolGateWayC, tpDhcpServerStaticBindEntry=tpDhcpServerStaticBindEntry, tpDhcpServerAddrPoolTable=tpDhcpServerAddrPoolTable, tpDhcpServerAddrPoolNBNServerA=tpDhcpServerAddrPoolNBNServerA, tpDhcpServerAddrPoolName=tpDhcpServerAddrPoolName, tpDhcpServerStatisticsClear=tpDhcpServerStatisticsClear, tpDhcpServerAddrPoolDnsG=tpDhcpServerAddrPoolDnsG, tpDhcpServerBindingClientId=tpDhcpServerBindingClientId, tpDhcpServerBindIpAddr=tpDhcpServerBindIpAddr, tpDhcpServerCapwapAcIp=tpDhcpServerCapwapAcIp, tpDhcpServerUnusedIpTable=tpDhcpServerUnusedIpTable, tpDhcpServerStatisticsRelease=tpDhcpServerStatisticsRelease, tpDhcpServerAddrPoolNBNServerH=tpDhcpServerAddrPoolNBNServerH, tpDhcpServerStatisticsRequest=tpDhcpServerStatisticsRequest, tpDhcpServerAddrPoolDnsF=tpDhcpServerAddrPoolDnsF, tpDhcpServerVendorClassId=tpDhcpServerVendorClassId, tpDhcpServerHardwareType=tpDhcpServerHardwareType, tpDhcpServerAddrPoolNBNServerF=tpDhcpServerAddrPoolNBNServerF, tpDhcpServerAddrPoolRentTime=tpDhcpServerAddrPoolRentTime, tpDhcpServerBindingRemainTime=tpDhcpServerBindingRemainTime, tpDhcpServerPingPackets=tpDhcpServerPingPackets, tpDhcpServerAddrPoolGateWayG=tpDhcpServerAddrPoolGateWayG, tpDhcpServerAddrPoolNBNServerD=tpDhcpServerAddrPoolNBNServerD)

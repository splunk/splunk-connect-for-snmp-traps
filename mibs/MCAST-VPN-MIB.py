#
# PySNMP MIB module MCAST-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MCAST-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:00:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ipMRouteEntry, = mibBuilder.importSymbols("IPMROUTE-STD-MIB", "ipMRouteEntry")
jnxMvpnExperiment, = mibBuilder.importSymbols("JUNIPER-EXPERIMENT-MIB", "jnxMvpnExperiment")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
JnxL2L3VpnMcastProviderTunnelType, = mibBuilder.importSymbols("L2L3-VPN-MCAST-MIB", "JnxL2L3VpnMcastProviderTunnelType")
MplsLabel, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel")
mplsVpnVrfName, MplsVpnRouteDistinguisher = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfName", "MplsVpnRouteDistinguisher")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Gauge32, Bits, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, NotificationType, ObjectIdentity, MibIdentifier, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "Counter64", "IpAddress")
DisplayString, TruthValue, TimeInterval, TimeStamp, RowStatus, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeInterval", "TimeStamp", "RowStatus", "RowPointer", "TextualConvention")
jnxMvpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1))
jnxMvpnMIB.setRevisions(('2013-01-07 12:00',))
if mibBuilder.loadTexts: jnxMvpnMIB.setLastUpdated('201307121200Z')
if mibBuilder.loadTexts: jnxMvpnMIB.setOrganization('IETF Layer-3 Virtual Private Networks Working Group.')
jnxMvpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 0))
jnxMvpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1))
jnxMvpnScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1))
jnxMvpnGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2))
jnxMvpnConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3))
jnxMvpnStates = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4))
jnxMvpnMvrfNumber = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumber.setStatus('current')
jnxMvpnMvrfNumberV4 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberV4.setStatus('current')
jnxMvpnMvrfNumberV6 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberV6.setStatus('current')
jnxMvpnMvrfNumberPimV4 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberPimV4.setStatus('current')
jnxMvpnMvrfNumberPimV6 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberPimV6.setStatus('current')
jnxMvpnMvrfNumberBgpV4 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberBgpV4.setStatus('current')
jnxMvpnMvrfNumberBgpV6 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberBgpV6.setStatus('current')
jnxMvpnMvrfNumberMldp = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMvrfNumberMldp.setStatus('current')
jnxMvpnNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnNotificationEnable.setStatus('current')
jnxMvpnGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1), )
if mibBuilder.loadTexts: jnxMvpnGeneralTable.setStatus('current')
jnxMvpnGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"))
if mibBuilder.loadTexts: jnxMvpnGeneralEntry.setStatus('current')
jnxMvpnGenOperStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("createdMvrf", 1), ("deletedMvrf", 2), ("modifiedMvrfIpmsiConfig", 3), ("modifiedMvrfSpmsiConfig", 4))).clone('createdMvrf')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenOperStatusChange.setStatus('current')
jnxMvpnGenOperChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenOperChangeTime.setStatus('current')
jnxMvpnGenCmcastRouteProtocolV4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pim", 1), ("bgp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenCmcastRouteProtocolV4.setStatus('current')
jnxMvpnGenCmcastRouteProtocolV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pim", 1), ("bgp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenCmcastRouteProtocolV6.setStatus('current')
jnxMvpnGenIpmsiConfigV4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenIpmsiConfigV4.setStatus('current')
jnxMvpnGenIpmsiConfigV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 6), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenIpmsiConfigV6.setStatus('current')
jnxMvpnGenInterAsPmsiConfigV4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenInterAsPmsiConfigV4.setStatus('current')
jnxMvpnGenInterAsPmsiConfigV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 8), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenInterAsPmsiConfigV6.setStatus('current')
jnxMvpnGenRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 9), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnGenRowStatus.setStatus('current')
jnxMvpnBgpGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2), )
if mibBuilder.loadTexts: jnxMvpnBgpGeneralTable.setStatus('current')
jnxMvpnBgpGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1), )
jnxMvpnGeneralEntry.registerAugmentions(("MCAST-VPN-MIB", "jnxMvpnBgpGeneralEntry"))
jnxMvpnBgpGeneralEntry.setIndexNames(*jnxMvpnGeneralEntry.getIndexNames())
if mibBuilder.loadTexts: jnxMvpnBgpGeneralEntry.setStatus('current')
jnxMvpnBgpGenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rpt-spt", 1), ("spt-only", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenMode.setStatus('current')
jnxMvpnBgpGenUmhSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("highest-pe-address", 1), ("c-root-group-hashing", 2), ("ucast-umh-route", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenUmhSelection.setStatus('current')
jnxMvpnBgpGenSiteType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sender-receiver", 1), ("receiver-only", 2), ("sender-only", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenSiteType.setStatus('current')
jnxMvpnBgpGenCmcastImportRt = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 4), MplsVpnRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenCmcastImportRt.setStatus('current')
jnxMvpnBgpGenSrcAs = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenSrcAs.setStatus('current')
jnxMvpnBgpGenSptnlLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnBgpGenSptnlLimit.setStatus('current')
jnxMvpnPmsiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1), )
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTable.setStatus('current')
jnxMvpnPmsiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1), ).setIndexNames((0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelType"), (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelAuxInfo"), (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelPimGroupAddressType"), (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelPimGroupAddress"), (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelOrTemplateName"))
if mibBuilder.loadTexts: jnxMvpnPmsiConfigEntry.setStatus('current')
jnxMvpnPmsiConfigTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 1), JnxL2L3VpnMcastProviderTunnelType())
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTunnelType.setStatus('current')
jnxMvpnPmsiConfigTunnelAuxInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTunnelAuxInfo.setStatus('current')
jnxMvpnPmsiConfigTunnelPimGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 3), InetAddressType())
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTunnelPimGroupAddressType.setStatus('current')
jnxMvpnPmsiConfigTunnelPimGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 4), InetAddress())
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTunnelPimGroupAddress.setStatus('current')
jnxMvpnPmsiConfigTunnelOrTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 5), SnmpAdminString())
if mibBuilder.loadTexts: jnxMvpnPmsiConfigTunnelOrTemplateName.setStatus('current')
jnxMvpnPmsiConfigEncapsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("greIp", 1), ("ipIp", 2), ("mpls", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnPmsiConfigEncapsType.setStatus('current')
jnxMvpnPmsiConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnPmsiConfigRowStatus.setStatus('current')
jnxMvpnSpmsiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2), )
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigTable.setStatus('current')
jnxMvpnSpmsiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastAddressType"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastGroupAddress"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastGroupPrefixLen"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastSourceAddress"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastSourcePrefixLen"))
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigEntry.setStatus('current')
jnxMvpnSpmsiConfigCmcastAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigCmcastAddressType.setStatus('current')
jnxMvpnSpmsiConfigCmcastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigCmcastGroupAddress.setStatus('current')
jnxMvpnSpmsiConfigCmcastGroupPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigCmcastGroupPrefixLen.setStatus('current')
jnxMvpnSpmsiConfigCmcastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 4), InetAddress())
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigCmcastSourceAddress.setStatus('current')
jnxMvpnSpmsiConfigCmcastSourcePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigCmcastSourcePrefixLen.setStatus('current')
jnxMvpnSpmsiConfigThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigThreshold.setStatus('current')
jnxMvpnSpmsiConfigPmsiPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigPmsiPointer.setStatus('current')
jnxMvpnSpmsiConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 8), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiConfigRowStatus.setStatus('current')
jnxMvpnIpmsiTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1), )
if mibBuilder.loadTexts: jnxMvpnIpmsiTable.setStatus('current')
jnxMvpnIpmsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiAfi"), (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiRD"), (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiOrigAddrType"), (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiOrigAddress"))
if mibBuilder.loadTexts: jnxMvpnIpmsiEntry.setStatus('current')
jnxMvpnIpmsiAfi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), )))
if mibBuilder.loadTexts: jnxMvpnIpmsiAfi.setStatus('current')
jnxMvpnIpmsiRD = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 2), MplsVpnRouteDistinguisher())
if mibBuilder.loadTexts: jnxMvpnIpmsiRD.setStatus('current')
jnxMvpnIpmsiOrigAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 3), InetAddressType())
if mibBuilder.loadTexts: jnxMvpnIpmsiOrigAddrType.setStatus('current')
jnxMvpnIpmsiOrigAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 4), InetAddress())
if mibBuilder.loadTexts: jnxMvpnIpmsiOrigAddress.setStatus('current')
jnxMvpnIpmsiUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnIpmsiUpTime.setStatus('current')
jnxMvpnIpmsiAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 6), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnIpmsiAttribute.setStatus('current')
jnxMvpnInterasIpmsiTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2), )
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiTable.setStatus('current')
jnxMvpnInterasIpmsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiAfi"), (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiRD"), (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiSrcAs"))
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiEntry.setStatus('current')
jnxMvpnInterasIpmsiAfi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), )))
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiAfi.setStatus('current')
jnxMvpnInterasIpmsiRD = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 2), MplsVpnRouteDistinguisher())
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiRD.setStatus('current')
jnxMvpnInterasIpmsiSrcAs = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiSrcAs.setStatus('current')
jnxMvpnInterasIpmsiAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 4), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnInterasIpmsiAttribute.setStatus('current')
jnxMvpnSpmsiTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3), )
if mibBuilder.loadTexts: jnxMvpnSpmsiTable.setStatus('current')
jnxMvpnSpmsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiOrigAddrType"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiOrigAddress"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastAddrType"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastGroup"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastGroupPrefixLen"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastSource"), (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastSourcePrefixLen"))
if mibBuilder.loadTexts: jnxMvpnSpmsiEntry.setStatus('current')
jnxMvpnSpmsiOrigAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: jnxMvpnSpmsiOrigAddrType.setStatus('current')
jnxMvpnSpmsiOrigAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: jnxMvpnSpmsiOrigAddress.setStatus('current')
jnxMvpnSpmsiCmcastAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 3), InetAddressType())
if mibBuilder.loadTexts: jnxMvpnSpmsiCmcastAddrType.setStatus('current')
jnxMvpnSpmsiCmcastGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 4), InetAddress())
if mibBuilder.loadTexts: jnxMvpnSpmsiCmcastGroup.setStatus('current')
jnxMvpnSpmsiCmcastGroupPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 5), Unsigned32())
if mibBuilder.loadTexts: jnxMvpnSpmsiCmcastGroupPrefixLen.setStatus('current')
jnxMvpnSpmsiCmcastSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 6), InetAddress())
if mibBuilder.loadTexts: jnxMvpnSpmsiCmcastSource.setStatus('current')
jnxMvpnSpmsiCmcastSourcePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 7), Unsigned32())
if mibBuilder.loadTexts: jnxMvpnSpmsiCmcastSourcePrefixLen.setStatus('current')
jnxMvpnSpmsiTunnelAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 8), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiTunnelAttribute.setStatus('current')
jnxMvpnSpmsiUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 9), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiUpTime.setStatus('current')
jnxMvpnSpmsiExpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 10), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiExpTime.setStatus('current')
jnxMvpnSpmsiRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnSpmsiRefCnt.setStatus('current')
jnxMvpnMrouteTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4), )
if mibBuilder.loadTexts: jnxMvpnMrouteTable.setStatus('current')
jnxMvpnMrouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1), )
ipMRouteEntry.registerAugmentions(("MCAST-VPN-MIB", "jnxMvpnMrouteEntry"))
jnxMvpnMrouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
if mibBuilder.loadTexts: jnxMvpnMrouteEntry.setStatus('current')
jnxMvpnMroutePmsiPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMroutePmsiPointer.setStatus('current')
jnxMvpnMrouteNumberOfLocalReplication = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMrouteNumberOfLocalReplication.setStatus('current')
jnxMvpnMrouteNumberOfRemoteReplication = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMrouteNumberOfRemoteReplication.setStatus('current')
jnxMvpnMrouteDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMvpnMrouteDataRate.setStatus('current')
jnxMvpnMvrfChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 0, 2)).setObjects(("MCAST-VPN-MIB", "jnxMvpnGenOperStatusChange"))
if mibBuilder.loadTexts: jnxMvpnMvrfChange.setStatus('current')
mibBuilder.exportSymbols("MCAST-VPN-MIB", jnxMvpnPmsiConfigTable=jnxMvpnPmsiConfigTable, jnxMvpnGenIpmsiConfigV6=jnxMvpnGenIpmsiConfigV6, jnxMvpnIpmsiEntry=jnxMvpnIpmsiEntry, jnxMvpnPmsiConfigTunnelAuxInfo=jnxMvpnPmsiConfigTunnelAuxInfo, jnxMvpnBgpGeneralEntry=jnxMvpnBgpGeneralEntry, jnxMvpnGenCmcastRouteProtocolV4=jnxMvpnGenCmcastRouteProtocolV4, jnxMvpnSpmsiConfigTable=jnxMvpnSpmsiConfigTable, jnxMvpnGenOperStatusChange=jnxMvpnGenOperStatusChange, jnxMvpnMrouteEntry=jnxMvpnMrouteEntry, jnxMvpnSpmsiConfigCmcastSourceAddress=jnxMvpnSpmsiConfigCmcastSourceAddress, jnxMvpnSpmsiEntry=jnxMvpnSpmsiEntry, jnxMvpnSpmsiOrigAddrType=jnxMvpnSpmsiOrigAddrType, jnxMvpnBgpGenMode=jnxMvpnBgpGenMode, jnxMvpnSpmsiConfigThreshold=jnxMvpnSpmsiConfigThreshold, jnxMvpnMvrfNumberBgpV4=jnxMvpnMvrfNumberBgpV4, jnxMvpnMvrfNumber=jnxMvpnMvrfNumber, jnxMvpnGeneralTable=jnxMvpnGeneralTable, jnxMvpnSpmsiConfigCmcastGroupPrefixLen=jnxMvpnSpmsiConfigCmcastGroupPrefixLen, jnxMvpnBgpGenCmcastImportRt=jnxMvpnBgpGenCmcastImportRt, jnxMvpnGenInterAsPmsiConfigV6=jnxMvpnGenInterAsPmsiConfigV6, jnxMvpnPmsiConfigTunnelPimGroupAddressType=jnxMvpnPmsiConfigTunnelPimGroupAddressType, jnxMvpnSpmsiCmcastSource=jnxMvpnSpmsiCmcastSource, jnxMvpnSpmsiConfigCmcastSourcePrefixLen=jnxMvpnSpmsiConfigCmcastSourcePrefixLen, jnxMvpnInterasIpmsiRD=jnxMvpnInterasIpmsiRD, jnxMvpnPmsiConfigRowStatus=jnxMvpnPmsiConfigRowStatus, jnxMvpnSpmsiCmcastGroupPrefixLen=jnxMvpnSpmsiCmcastGroupPrefixLen, jnxMvpnMvrfNumberV4=jnxMvpnMvrfNumberV4, jnxMvpnMvrfNumberV6=jnxMvpnMvrfNumberV6, jnxMvpnSpmsiConfigPmsiPointer=jnxMvpnSpmsiConfigPmsiPointer, jnxMvpnSpmsiConfigCmcastAddressType=jnxMvpnSpmsiConfigCmcastAddressType, jnxMvpnIpmsiRD=jnxMvpnIpmsiRD, jnxMvpnIpmsiAttribute=jnxMvpnIpmsiAttribute, jnxMvpnNotificationEnable=jnxMvpnNotificationEnable, jnxMvpnIpmsiUpTime=jnxMvpnIpmsiUpTime, jnxMvpnNotifications=jnxMvpnNotifications, jnxMvpnGenRowStatus=jnxMvpnGenRowStatus, jnxMvpnMroutePmsiPointer=jnxMvpnMroutePmsiPointer, jnxMvpnSpmsiCmcastSourcePrefixLen=jnxMvpnSpmsiCmcastSourcePrefixLen, jnxMvpnGenOperChangeTime=jnxMvpnGenOperChangeTime, jnxMvpnScalars=jnxMvpnScalars, jnxMvpnSpmsiConfigRowStatus=jnxMvpnSpmsiConfigRowStatus, jnxMvpnPmsiConfigEncapsType=jnxMvpnPmsiConfigEncapsType, jnxMvpnSpmsiTable=jnxMvpnSpmsiTable, jnxMvpnPmsiConfigTunnelPimGroupAddress=jnxMvpnPmsiConfigTunnelPimGroupAddress, jnxMvpnBgpGenSiteType=jnxMvpnBgpGenSiteType, jnxMvpnPmsiConfigTunnelOrTemplateName=jnxMvpnPmsiConfigTunnelOrTemplateName, jnxMvpnInterasIpmsiAfi=jnxMvpnInterasIpmsiAfi, jnxMvpnSpmsiRefCnt=jnxMvpnSpmsiRefCnt, jnxMvpnIpmsiAfi=jnxMvpnIpmsiAfi, jnxMvpnMvrfChange=jnxMvpnMvrfChange, jnxMvpnGenCmcastRouteProtocolV6=jnxMvpnGenCmcastRouteProtocolV6, jnxMvpnGeneral=jnxMvpnGeneral, jnxMvpnPmsiConfigTunnelType=jnxMvpnPmsiConfigTunnelType, jnxMvpnMvrfNumberMldp=jnxMvpnMvrfNumberMldp, jnxMvpnIpmsiTable=jnxMvpnIpmsiTable, jnxMvpnGenIpmsiConfigV4=jnxMvpnGenIpmsiConfigV4, jnxMvpnStates=jnxMvpnStates, jnxMvpnBgpGeneralTable=jnxMvpnBgpGeneralTable, jnxMvpnSpmsiConfigEntry=jnxMvpnSpmsiConfigEntry, jnxMvpnIpmsiOrigAddress=jnxMvpnIpmsiOrigAddress, jnxMvpnInterasIpmsiAttribute=jnxMvpnInterasIpmsiAttribute, jnxMvpnSpmsiOrigAddress=jnxMvpnSpmsiOrigAddress, jnxMvpnObjects=jnxMvpnObjects, jnxMvpnMvrfNumberBgpV6=jnxMvpnMvrfNumberBgpV6, jnxMvpnSpmsiUpTime=jnxMvpnSpmsiUpTime, jnxMvpnMrouteNumberOfRemoteReplication=jnxMvpnMrouteNumberOfRemoteReplication, jnxMvpnIpmsiOrigAddrType=jnxMvpnIpmsiOrigAddrType, jnxMvpnSpmsiCmcastGroup=jnxMvpnSpmsiCmcastGroup, jnxMvpnMvrfNumberPimV4=jnxMvpnMvrfNumberPimV4, jnxMvpnBgpGenUmhSelection=jnxMvpnBgpGenUmhSelection, jnxMvpnGeneralEntry=jnxMvpnGeneralEntry, jnxMvpnMIB=jnxMvpnMIB, jnxMvpnBgpGenSptnlLimit=jnxMvpnBgpGenSptnlLimit, jnxMvpnGenInterAsPmsiConfigV4=jnxMvpnGenInterAsPmsiConfigV4, jnxMvpnBgpGenSrcAs=jnxMvpnBgpGenSrcAs, jnxMvpnInterasIpmsiTable=jnxMvpnInterasIpmsiTable, jnxMvpnSpmsiTunnelAttribute=jnxMvpnSpmsiTunnelAttribute, jnxMvpnMvrfNumberPimV6=jnxMvpnMvrfNumberPimV6, jnxMvpnSpmsiCmcastAddrType=jnxMvpnSpmsiCmcastAddrType, jnxMvpnMrouteTable=jnxMvpnMrouteTable, jnxMvpnPmsiConfigEntry=jnxMvpnPmsiConfigEntry, jnxMvpnMrouteNumberOfLocalReplication=jnxMvpnMrouteNumberOfLocalReplication, jnxMvpnInterasIpmsiSrcAs=jnxMvpnInterasIpmsiSrcAs, PYSNMP_MODULE_ID=jnxMvpnMIB, jnxMvpnConfig=jnxMvpnConfig, jnxMvpnSpmsiConfigCmcastGroupAddress=jnxMvpnSpmsiConfigCmcastGroupAddress, jnxMvpnSpmsiExpTime=jnxMvpnSpmsiExpTime, jnxMvpnInterasIpmsiEntry=jnxMvpnInterasIpmsiEntry, jnxMvpnMrouteDataRate=jnxMvpnMrouteDataRate)
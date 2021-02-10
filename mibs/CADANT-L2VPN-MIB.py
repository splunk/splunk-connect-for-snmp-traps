#
# PySNMP MIB module CADANT-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-L2VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
cadL2vpn, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadL2vpn")
clabProjDocsis, DocsL2vpnIfList = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis", "DocsL2vpnIfList")
docsIfCmtsCmStatusIndex, = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusIndex")
DocsL2vpnIndex, docsL2vpnIdx, DocsNsiEncapSubtype, DocsL2vpnIdentifier = mibBuilder.importSymbols("DOCS-L2VPN-MIB", "DocsL2vpnIndex", "docsL2vpnIdx", "DocsNsiEncapSubtype", "DocsL2vpnIdentifier")
docsQosServiceFlowId, docsQosPktClassId = mibBuilder.importSymbols("DOCS-QOS3-MIB", "docsQosServiceFlowId", "docsQosPktClassId")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter32, MibIdentifier, iso, Bits, TimeTicks, IpAddress, Gauge32, ModuleIdentity, NotificationType, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "iso", "Bits", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "NotificationType", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
cadL2vpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1))
cadL2vpnMIB.setRevisions(('2015-10-01 00:00', '2015-07-07 00:00', '2015-06-24 00:00', '2015-06-22 00:00', '2015-03-09 00:00', '2014-12-02 00:00', '2013-09-23 00:00', '2013-09-10 00:00', '2009-08-03 00:00', '2009-06-25 00:00', '2009-06-23 00:00', '2009-06-18 00:00',))
if mibBuilder.loadTexts: cadL2vpnMIB.setLastUpdated('201510010000Z')
if mibBuilder.loadTexts: cadL2vpnMIB.setOrganization('Arris International, Inc.')
class CadNsiEncapValue(TextualConvention, OctetString):
    status = 'current'

cadL2vpnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1))
cadL2vpnParams = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1))
cadL2vpnPrimaryNetworkIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnPrimaryNetworkIfIndex.setStatus('current')
cadL2vpnSecondaryNetworkIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnSecondaryNetworkIfIndex.setStatus('current')
cadL2vpnActiveNetworkIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnActiveNetworkIfIndex.setStatus('current')
cadL2vpnForwardingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnForwardingEnabled.setStatus('current')
cadL2vpnCmCapEsafeIdentRequired = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnCmCapEsafeIdentRequired.setStatus('current')
cadL2vpnCmCapDutFilterRequired = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnCmCapDutFilterRequired.setStatus('current')
cadL2vpnGlobalTpid = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tpid8100", 1), ("tpid88a8", 2), ("tpid9100", 3))).clone('tpid8100')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadL2vpnGlobalTpid.setStatus('current')
cadL2vpnInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2), )
if mibBuilder.loadTexts: cadL2vpnInterfaceTable.setStatus('current')
cadL2vpnInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnInterfaceIfIndex"))
if mibBuilder.loadTexts: cadL2vpnInterfaceEntry.setStatus('current')
cadL2vpnInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadL2vpnInterfaceIfIndex.setStatus('current')
cadL2vpnInterfaceIpIgmpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnInterfaceIpIgmpSnooping.setStatus('current')
cadL2vpnInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnInterfaceRowStatus.setStatus('current')
cadL2vpnVlanIdRangeTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3), )
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeTable.setStatus('current')
cadL2vpnVlanIdRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnVlanIdRangeBegin"), (0, "CADANT-L2VPN-MIB", "cadL2vpnVlanIdRangeEnd"))
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeEntry.setStatus('current')
cadL2vpnVlanIdRangeBegin = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094)))
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeBegin.setStatus('current')
cadL2vpnVlanIdRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094)))
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeEnd.setStatus('current')
cadL2vpnVlanIdRangeNsiEncapSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("single-qtag", 1), ("dual-qtag", 2), ("l3-vrf", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeNsiEncapSubtype.setStatus('current')
cadL2vpnVlanIdRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnVlanIdRangeRowStatus.setStatus('current')
cadL2vpnInstanceIdToCmTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4), )
if mibBuilder.loadTexts: cadL2vpnInstanceIdToCmTable.setStatus('current')
cadL2vpnInstanceIdToCmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnInstanceId"))
if mibBuilder.loadTexts: cadL2vpnInstanceIdToCmEntry.setStatus('current')
cadL2vpnInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)))
if mibBuilder.loadTexts: cadL2vpnInstanceId.setStatus('current')
cadL2vpnInstanceIdVlanIdOuter = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnInstanceIdVlanIdOuter.setStatus('current')
cadL2vpnInstanceIdVlanIdInner = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnInstanceIdVlanIdInner.setStatus('current')
cadL2vpnInstanceIdCmMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnInstanceIdCmMac.setStatus('current')
cadL2vpnInstanceIdVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 5), DocsL2vpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnInstanceIdVpnId.setStatus('current')
cadL2vpnIdxToCmVpnInstTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6), )
if mibBuilder.loadTexts: cadL2vpnIdxToCmVpnInstTable.setStatus('current')
cadL2vpnIdxToCmVpnInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnVpnIdx"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"), (0, "CADANT-L2VPN-MIB", "cerL2vpnInstanceId"))
if mibBuilder.loadTexts: cadL2vpnIdxToCmVpnInstEntry.setStatus('current')
cadL2vpnVpnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6, 1, 1), DocsL2vpnIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnVpnIdx.setStatus('current')
cadL2vpnPktClassTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8), )
if mibBuilder.loadTexts: cadL2vpnPktClassTable.setStatus('current')
cadL2vpnPktClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"), (0, "DOCS-QOS3-MIB", "docsQosPktClassId"))
if mibBuilder.loadTexts: cadL2vpnPktClassEntry.setStatus('current')
cadL2vpnPktClassL2vpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 1), DocsL2vpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnPktClassL2vpnId.setStatus('current')
cadL2vpnPktClassUserPriRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnPktClassUserPriRangeLow.setStatus('current')
cadL2vpnPktClassUserPriRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnPktClassUserPriRangeHigh.setStatus('current')
cadL2vpnPktClassCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 4), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnPktClassCMIM.setStatus('current')
cadL2vpnPktClassVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadL2vpnPktClassVendorSpecific.setStatus('current')
cadL2vpnDenyForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9), )
if mibBuilder.loadTexts: cadL2vpnDenyForwardingTable.setStatus('current')
cadL2vpnDenyForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnDenyForwardingIndex"))
if mibBuilder.loadTexts: cadL2vpnDenyForwardingEntry.setStatus('current')
cadL2vpnDenyForwardingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cadL2vpnDenyForwardingIndex.setStatus('current')
cadL2vpnDenyForwardingVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnDenyForwardingVpnId.setStatus('current')
cadL2vpnDenyForwardingInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnDenyForwardingInstanceId.setStatus('current')
cadL2vpnDenyForwardingCmMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnDenyForwardingCmMac.setStatus('current')
cadL2vpnDenyForwardingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnDenyForwardingRowStatus.setStatus('current')
cadL2vpnDenyForwardingMplsPeerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnDenyForwardingMplsPeerIp.setStatus('current')
cerL2vpnCmVpnIdTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10), )
if mibBuilder.loadTexts: cerL2vpnCmVpnIdTable.setStatus('current')
cerL2vpnCmVpnIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"))
if mibBuilder.loadTexts: cerL2vpnCmVpnIdEntry.setStatus('current')
cerL2vpnCmMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 1), MacAddress())
if mibBuilder.loadTexts: cerL2vpnCmMac.setStatus('current')
cerL2vpnCmVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 2), DocsL2vpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmVpnId.setStatus('current')
cerL2vpnCmNsiEncapSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 3), DocsNsiEncapSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmNsiEncapSubtype.setStatus('current')
cerL2vpnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 4), DocsL2vpnIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnIdx.setStatus('current')
cerL2vpnCmForwardingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmForwardingEnabled.setStatus('current')
cerL2vpnInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215)))
if mibBuilder.loadTexts: cerL2vpnInstanceId.setStatus('current')
cerL2vpnInstanceOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 4094), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnInstanceOuterVlanId.setStatus('current')
cerL2vpnInstanceInnerVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnInstanceInnerVlanId.setStatus('current')
cerL2vpnInstanceNsiEncapSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("not-applicable", 0), ("single-qtag", 1), ("dual-qtag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnInstanceNsiEncapSubType.setStatus('current')
cerL2vpnCmCompliantCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmCompliantCapability.setStatus('current')
cerL2vpnCmDutFilteringCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmDutFilteringCapability.setStatus('current')
cerL2vpnCmDutCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 12), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmDutCMIM.setStatus('current')
cerL2vpnCmDhcpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 13), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmDhcpSnooping.setStatus('current')
cerL2vpnVpnCmCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 14), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnVpnCmCMIM.setStatus('current')
cerL2vpnVpnCmIndividualSAID = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnVpnCmIndividualSAID.setStatus('current')
cerL2vpnVpnCmVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnVpnCmVendorSpecific.setStatus('current')
cerL2vpnCmNsiEncapValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 17), CadNsiEncapValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmNsiEncapValue.setStatus('current')
cerL2vpnMplsAcId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnMplsAcId.setStatus('current')
cerL2vpnCmMplsPwId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmMplsPwId.setStatus('current')
cerL2vpnCmMplsPeerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 20), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmMplsPeerAddrType.setStatus('current')
cerL2vpnCmMplsPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 21), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmMplsPeerAddr.setStatus('current')
cerL2vpnCmBgpVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmBgpVpnId.setStatus('current')
cerL2vpnCmBgpRd = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmBgpRd.setStatus('current')
cerL2vpnCmBgpRtImport = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmBgpRtImport.setStatus('current')
cerL2vpnCmBgpRtExport = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmBgpRtExport.setStatus('current')
cerL2vpnCmBgpCeVeId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 26), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmBgpCeVeId.setStatus('current')
cerL2vpnCmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11), )
if mibBuilder.loadTexts: cerL2vpnCmStatsTable.setStatus('current')
cerL2vpnCmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"))
if mibBuilder.loadTexts: cerL2vpnCmStatsEntry.setStatus('current')
cerL2vpnCmStatsUpstreamPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsUpstreamPkts.setStatus('current')
cerL2vpnCmStatsUpstreamBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsUpstreamBytes.setStatus('current')
cerL2vpnCmStatsUpstreamDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsUpstreamDiscards.setStatus('current')
cerL2vpnCmStatsDownstreamPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsDownstreamPkts.setStatus('current')
cerL2vpnCmStatsDownstreamBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsDownstreamBytes.setStatus('current')
cerL2vpnCmStatsDownstreamDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmStatsDownstreamDiscards.setStatus('current')
cadL2vpnMplsPeerIpToCmTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12), )
if mibBuilder.loadTexts: cadL2vpnMplsPeerIpToCmTable.setStatus('current')
cadL2vpnMplsPeerIpToCmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cerL2vpnCmMplsPeerAddrType"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMplsPeerIpAddress"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"), (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"))
if mibBuilder.loadTexts: cadL2vpnMplsPeerIpToCmEntry.setStatus('current')
cerL2vpnCmMplsPeerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerL2vpnCmMplsPeerIpAddress.setStatus('current')
cadL2vpnProvisionedCmTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13), )
if mibBuilder.loadTexts: cadL2vpnProvisionedCmTable.setStatus('current')
cadL2vpnProvisionedCmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmMacAddress"))
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEntry.setStatus('current')
cadL2vpnProvisionedCmMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 1), MacAddress())
if mibBuilder.loadTexts: cadL2vpnProvisionedCmMacAddress.setStatus('current')
cadL2vpnProvisionedCmL2vpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 2), DocsL2vpnIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmL2vpnId.setStatus('current')
cadL2vpnProvisionedCmOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmOuterVlanId.setStatus('current')
cadL2vpnProvisionedCmInnerVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmInnerVlanId.setStatus('current')
cadL2vpnProvisionedCmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmRowStatus.setStatus('current')
cadL2vpnProvisionedCmEsafeTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14), )
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEsafeTable.setStatus('current')
cadL2vpnProvisionedCmEsafeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1), ).setIndexNames((0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmMacAddress"), (0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmEsafeMacAddress"))
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEsafeEntry.setStatus('current')
cadL2vpnProvisionedCmEsafeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 1), MacAddress())
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEsafeMacAddress.setStatus('current')
cadL2vpnProvisionedCmEsafeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 17, 19))).clone(namedValues=NamedValues(("mta", 16), ("stb", 17), ("tea", 19)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEsafeIfIndex.setStatus('current')
cadL2vpnProvisionedCmEsafeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadL2vpnProvisionedCmEsafeRowStatus.setStatus('current')
mibBuilder.exportSymbols("CADANT-L2VPN-MIB", cerL2vpnCmVpnId=cerL2vpnCmVpnId, cadL2vpnProvisionedCmL2vpnId=cadL2vpnProvisionedCmL2vpnId, cadL2vpnVpnIdx=cadL2vpnVpnIdx, cerL2vpnCmDutFilteringCapability=cerL2vpnCmDutFilteringCapability, cerL2vpnCmStatsDownstreamDiscards=cerL2vpnCmStatsDownstreamDiscards, cerL2vpnCmCompliantCapability=cerL2vpnCmCompliantCapability, cerL2vpnCmStatsDownstreamPkts=cerL2vpnCmStatsDownstreamPkts, cerL2vpnIdx=cerL2vpnIdx, cadL2vpnPktClassVendorSpecific=cadL2vpnPktClassVendorSpecific, cadL2vpnPktClassCMIM=cadL2vpnPktClassCMIM, cadL2vpnProvisionedCmOuterVlanId=cadL2vpnProvisionedCmOuterVlanId, cerL2vpnInstanceInnerVlanId=cerL2vpnInstanceInnerVlanId, cadL2vpnProvisionedCmEsafeMacAddress=cadL2vpnProvisionedCmEsafeMacAddress, cadL2vpnActiveNetworkIfIndex=cadL2vpnActiveNetworkIfIndex, cadL2vpnPktClassEntry=cadL2vpnPktClassEntry, cadL2vpnVlanIdRangeEntry=cadL2vpnVlanIdRangeEntry, cadL2vpnDenyForwardingEntry=cadL2vpnDenyForwardingEntry, cerL2vpnInstanceId=cerL2vpnInstanceId, cadL2vpnPktClassL2vpnId=cadL2vpnPktClassL2vpnId, cerL2vpnInstanceNsiEncapSubType=cerL2vpnInstanceNsiEncapSubType, cerL2vpnCmDhcpSnooping=cerL2vpnCmDhcpSnooping, cadL2vpnPktClassUserPriRangeHigh=cadL2vpnPktClassUserPriRangeHigh, cadL2vpnInterfaceTable=cadL2vpnInterfaceTable, cerL2vpnCmMplsPwId=cerL2vpnCmMplsPwId, cadL2vpnDenyForwardingCmMac=cadL2vpnDenyForwardingCmMac, cerL2vpnCmDutCMIM=cerL2vpnCmDutCMIM, cadL2vpnCmCapEsafeIdentRequired=cadL2vpnCmCapEsafeIdentRequired, CadNsiEncapValue=CadNsiEncapValue, cadL2vpnPrimaryNetworkIfIndex=cadL2vpnPrimaryNetworkIfIndex, cerL2vpnCmMplsPeerIpAddress=cerL2vpnCmMplsPeerIpAddress, cerL2vpnCmStatsUpstreamBytes=cerL2vpnCmStatsUpstreamBytes, cadL2vpnProvisionedCmRowStatus=cadL2vpnProvisionedCmRowStatus, cadL2vpnInstanceIdCmMac=cadL2vpnInstanceIdCmMac, cadL2vpnInterfaceIpIgmpSnooping=cadL2vpnInterfaceIpIgmpSnooping, cadL2vpnMplsPeerIpToCmTable=cadL2vpnMplsPeerIpToCmTable, cadL2vpnVlanIdRangeEnd=cadL2vpnVlanIdRangeEnd, cadL2vpnVlanIdRangeRowStatus=cadL2vpnVlanIdRangeRowStatus, cadL2vpnProvisionedCmEsafeEntry=cadL2vpnProvisionedCmEsafeEntry, cerL2vpnCmVpnIdTable=cerL2vpnCmVpnIdTable, cerL2vpnVpnCmVendorSpecific=cerL2vpnVpnCmVendorSpecific, cerL2vpnCmStatsDownstreamBytes=cerL2vpnCmStatsDownstreamBytes, cerL2vpnCmBgpRtExport=cerL2vpnCmBgpRtExport, cadL2vpnInterfaceIfIndex=cadL2vpnInterfaceIfIndex, cadL2vpnProvisionedCmEsafeRowStatus=cadL2vpnProvisionedCmEsafeRowStatus, cerL2vpnCmForwardingEnabled=cerL2vpnCmForwardingEnabled, cerL2vpnVpnCmCMIM=cerL2vpnVpnCmCMIM, cerL2vpnCmStatsTable=cerL2vpnCmStatsTable, cerL2vpnCmNsiEncapValue=cerL2vpnCmNsiEncapValue, cerL2vpnCmNsiEncapSubtype=cerL2vpnCmNsiEncapSubtype, cadL2vpnPktClassUserPriRangeLow=cadL2vpnPktClassUserPriRangeLow, cerL2vpnCmBgpRd=cerL2vpnCmBgpRd, cadL2vpnMIB=cadL2vpnMIB, cadL2vpnDenyForwardingTable=cadL2vpnDenyForwardingTable, cadL2vpnInstanceIdToCmTable=cadL2vpnInstanceIdToCmTable, cadL2vpnInstanceIdToCmEntry=cadL2vpnInstanceIdToCmEntry, cadL2vpnForwardingEnabled=cadL2vpnForwardingEnabled, cadL2vpnDenyForwardingRowStatus=cadL2vpnDenyForwardingRowStatus, cadL2vpnGlobalTpid=cadL2vpnGlobalTpid, cadL2vpnParams=cadL2vpnParams, cadL2vpnProvisionedCmInnerVlanId=cadL2vpnProvisionedCmInnerVlanId, cerL2vpnMplsAcId=cerL2vpnMplsAcId, cerL2vpnCmStatsUpstreamPkts=cerL2vpnCmStatsUpstreamPkts, cadL2vpnInstanceIdVpnId=cadL2vpnInstanceIdVpnId, cerL2vpnCmStatsEntry=cerL2vpnCmStatsEntry, cadL2vpnSecondaryNetworkIfIndex=cadL2vpnSecondaryNetworkIfIndex, cadL2vpnInterfaceEntry=cadL2vpnInterfaceEntry, cadL2vpnProvisionedCmMacAddress=cadL2vpnProvisionedCmMacAddress, cadL2vpnVlanIdRangeBegin=cadL2vpnVlanIdRangeBegin, cerL2vpnCmBgpRtImport=cerL2vpnCmBgpRtImport, cadL2vpnVlanIdRangeNsiEncapSubtype=cadL2vpnVlanIdRangeNsiEncapSubtype, cadL2vpnMIBObjects=cadL2vpnMIBObjects, PYSNMP_MODULE_ID=cadL2vpnMIB, cadL2vpnIdxToCmVpnInstTable=cadL2vpnIdxToCmVpnInstTable, cadL2vpnDenyForwardingIndex=cadL2vpnDenyForwardingIndex, cerL2vpnCmMplsPeerAddrType=cerL2vpnCmMplsPeerAddrType, cadL2vpnCmCapDutFilterRequired=cadL2vpnCmCapDutFilterRequired, cerL2vpnCmMplsPeerAddr=cerL2vpnCmMplsPeerAddr, cadL2vpnDenyForwardingVpnId=cadL2vpnDenyForwardingVpnId, cadL2vpnMplsPeerIpToCmEntry=cadL2vpnMplsPeerIpToCmEntry, cadL2vpnVlanIdRangeTable=cadL2vpnVlanIdRangeTable, cerL2vpnCmBgpCeVeId=cerL2vpnCmBgpCeVeId, cadL2vpnInterfaceRowStatus=cadL2vpnInterfaceRowStatus, cadL2vpnInstanceId=cadL2vpnInstanceId, cerL2vpnCmMac=cerL2vpnCmMac, cadL2vpnDenyForwardingInstanceId=cadL2vpnDenyForwardingInstanceId, cerL2vpnCmBgpVpnId=cerL2vpnCmBgpVpnId, cerL2vpnCmVpnIdEntry=cerL2vpnCmVpnIdEntry, cadL2vpnProvisionedCmEsafeTable=cadL2vpnProvisionedCmEsafeTable, cadL2vpnDenyForwardingMplsPeerIp=cadL2vpnDenyForwardingMplsPeerIp, cadL2vpnProvisionedCmEsafeIfIndex=cadL2vpnProvisionedCmEsafeIfIndex, cadL2vpnInstanceIdVlanIdOuter=cadL2vpnInstanceIdVlanIdOuter, cadL2vpnPktClassTable=cadL2vpnPktClassTable, cadL2vpnProvisionedCmTable=cadL2vpnProvisionedCmTable, cerL2vpnCmStatsUpstreamDiscards=cerL2vpnCmStatsUpstreamDiscards, cadL2vpnIdxToCmVpnInstEntry=cadL2vpnIdxToCmVpnInstEntry, cerL2vpnInstanceOuterVlanId=cerL2vpnInstanceOuterVlanId, cerL2vpnVpnCmIndividualSAID=cerL2vpnVpnCmIndividualSAID, cadL2vpnInstanceIdVlanIdInner=cadL2vpnInstanceIdVlanIdInner, cadL2vpnProvisionedCmEntry=cadL2vpnProvisionedCmEntry)
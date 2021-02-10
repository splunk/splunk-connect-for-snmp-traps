#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddressIPv4, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressPrefixLength")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Gauge32, Unsigned32, IpAddress, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
ciscoIetfDhcpSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102))
ciscoIetfDhcpSrvMIB.setRevisions(('2007-03-27 00:00', '2007-02-14 12:00', '2004-03-01 12:00',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvMIB.setLastUpdated('200703270000Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvMIB.setOrganization('Cisco Systems, Inc.')
ciscoIetfDhcpv4SrvMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 0))
ciscoIetfDhcpv4SrvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 1))
ciscoIetfDhcpv4SrvMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 2))
class CDhcpv4PhysicalAddress(TextualConvention, OctetString):
    reference = 'RFC 2131'
    status = 'current'
    displayHint = '1d,1d,1x:1x:1x:1x:1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(18, 18)
    fixedLength = 18

cDhcpv4SrvSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1))
if mibBuilder.loadTexts: cDhcpv4SrvSystem.setStatus('current')
cBootpCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2))
if mibBuilder.loadTexts: cBootpCounters.setStatus('current')
cDhcpv4Counters = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3))
if mibBuilder.loadTexts: cDhcpv4Counters.setStatus('current')
cDhcpv4SrvConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4))
if mibBuilder.loadTexts: cDhcpv4SrvConfiguration.setStatus('current')
cDhcpv4ServerNotifyObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7))
if mibBuilder.loadTexts: cDhcpv4ServerNotifyObjects.setStatus('current')
cBootpHCCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8))
if mibBuilder.loadTexts: cBootpHCCounters.setStatus('current')
cDhcpv4HCCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9))
if mibBuilder.loadTexts: cDhcpv4HCCounters.setStatus('current')
cDhcpv4SrvSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4SrvSystemDescr.setStatus('current')
cDhcpv4SrvSystemObjectID = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4SrvSystemObjectID.setStatus('current')
cBootpCountRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpCountRequests.setStatus('current')
cBootpCountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpCountInvalids.setStatus('current')
cBootpCountReplies = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpCountReplies.setStatus('current')
cBootpCountDropUnknownClients = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpCountDropUnknownClients.setStatus('current')
cBootpCountDropNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpCountDropNotServingSubnet.setStatus('current')
cDhcpv4CountDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountDiscovers.setStatus('current')
cDhcpv4CountOffers = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountOffers.setStatus('current')
cDhcpv4CountRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountRequests.setStatus('current')
cDhcpv4CountDeclines = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountDeclines.setStatus('current')
cDhcpv4CountAcks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountAcks.setStatus('current')
cDhcpv4CountNaks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountNaks.setStatus('current')
cDhcpv4CountReleases = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountReleases.setStatus('current')
cDhcpv4CountInforms = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountInforms.setStatus('current')
cDhcpv4CountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountInvalids.setStatus('current')
cDhcpv4CountDropUnknownClient = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountDropUnknownClient.setStatus('current')
cDhcpv4CountDropNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4CountDropNotServingSubnet.setStatus('current')
cBootpHCCountRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpHCCountRequests.setStatus('current')
cBootpHCCountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpHCCountInvalids.setStatus('current')
cBootpHCCountReplies = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpHCCountReplies.setStatus('current')
cBootpHCCountDropUnknownClients = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpHCCountDropUnknownClients.setStatus('current')
cBootpHCCountDropNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBootpHCCountDropNotServingSubnet.setStatus('current')
cDhcpv4HCCountDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountDiscovers.setStatus('current')
cDhcpv4HCCountOffers = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountOffers.setStatus('current')
cDhcpv4HCCountRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountRequests.setStatus('current')
cDhcpv4HCCountDeclines = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountDeclines.setStatus('current')
cDhcpv4HCCountAcks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountAcks.setStatus('current')
cDhcpv4HCCountNaks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountNaks.setStatus('current')
cDhcpv4HCCountReleases = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountReleases.setStatus('current')
cDhcpv4HCCountInforms = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountInforms.setStatus('current')
cDhcpv4HCCountForcedRenews = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountForcedRenews.setStatus('current')
cDhcpv4HCCountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountInvalids.setStatus('current')
cDhcpv4HCCountDropUnknownClient = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountDropUnknownClient.setStatus('current')
cDhcpv4HCCountDropNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4HCCountDropNotServingSubnet.setStatus('current')
cDhcpv4ServerSharedNetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1), )
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetTable.setStatus('current')
cDhcpv4ServerSharedNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetName"))
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetEntry.setStatus('current')
cDhcpv4ServerSharedNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100)))
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetName.setStatus('current')
cDhcpv4ServerSharedNetFreeAddrLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetFreeAddrLowThreshold.setStatus('current')
cDhcpv4ServerSharedNetFreeAddrHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetFreeAddrHighThreshold.setStatus('current')
cDhcpv4ServerSharedNetFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetFreeAddresses.setStatus('current')
cDhcpv4ServerSharedNetReservedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetReservedAddresses.setStatus('current')
cDhcpv4ServerSharedNetTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSharedNetTotalAddresses.setStatus('current')
cDhcpv4ServerSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2), )
if mibBuilder.loadTexts: cDhcpv4ServerSubnetTable.setStatus('current')
cDhcpv4ServerSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1), ).setIndexNames((0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetAddress"))
if mibBuilder.loadTexts: cDhcpv4ServerSubnetEntry.setStatus('current')
cDhcpv4ServerSubnetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 1), InetAddressIPv4())
if mibBuilder.loadTexts: cDhcpv4ServerSubnetAddress.setStatus('current')
cDhcpv4ServerSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 2), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSubnetMask.setStatus('current')
cDhcpv4ServerSubnetSharedNetworkName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSubnetSharedNetworkName.setStatus('current')
cDhcpv4ServerSubnetFreeAddrLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDhcpv4ServerSubnetFreeAddrLowThreshold.setStatus('current')
cDhcpv4ServerSubnetFreeAddrHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDhcpv4ServerSubnetFreeAddrHighThreshold.setStatus('current')
cDhcpv4ServerSubnetFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerSubnetFreeAddresses.setStatus('current')
cDhcpv4ServerRangeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3), )
if mibBuilder.loadTexts: cDhcpv4ServerRangeTable.setStatus('current')
cDhcpv4ServerRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1), ).setIndexNames((0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeStartAddress"), (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeEndAddress"))
if mibBuilder.loadTexts: cDhcpv4ServerRangeEntry.setStatus('current')
cDhcpv4ServerRangeStartAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 1), InetAddressIPv4())
if mibBuilder.loadTexts: cDhcpv4ServerRangeStartAddress.setStatus('current')
cDhcpv4ServerRangeEndAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 2), InetAddressIPv4())
if mibBuilder.loadTexts: cDhcpv4ServerRangeEndAddress.setStatus('current')
cDhcpv4ServerRangeSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 3), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerRangeSubnetMask.setStatus('current')
cDhcpv4ServerRangeInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerRangeInUse.setStatus('current')
cDhcpv4ServerRangeOutstandingOffers = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerRangeOutstandingOffers.setStatus('current')
cDhcpv4ServerClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4), )
if mibBuilder.loadTexts: cDhcpv4ServerClientTable.setStatus('current')
cDhcpv4ServerClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1), ).setIndexNames((0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClient"))
if mibBuilder.loadTexts: cDhcpv4ServerClientEntry.setStatus('current')
cDhcpv4ServerClient = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 1), InetAddressIPv4())
if mibBuilder.loadTexts: cDhcpv4ServerClient.setStatus('current')
cDhcpv4ServerClientSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 2), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientSubnetMask.setStatus('current')
cDhcpv4ServerClientRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 3), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientRange.setStatus('current')
cDhcpv4ServerClientLeaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("expired", 3), ("configurationReserved", 4), ("serverReserved", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientLeaseType.setStatus('current')
cDhcpv4ServerClientTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientTimeRemaining.setStatus('current')
cDhcpv4ServerClientAllowedProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("bootp", 2), ("dhcp", 3), ("bootpOrDhcp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientAllowedProtocol.setStatus('current')
cDhcpv4ServerClientServedProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("bootp", 2), ("dhcp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientServedProtocol.setStatus('current')
cDhcpv4ServerClientPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 8), CDhcpv4PhysicalAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientPhysicalAddress.setStatus('current')
cDhcpv4ServerClientClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientClientId.setStatus('current')
cDhcpv4ServerClientHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientHostName.setStatus('current')
cDhcpv4ServerClientDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDhcpv4ServerClientDomainName.setStatus('current')
cDhcpv4ServerNotifyDuplicateIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 1), InetAddressIPv4()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cDhcpv4ServerNotifyDuplicateIpAddr.setStatus('current')
cDhcpv4ServerNotifyDuplicateMac = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 2), CDhcpv4PhysicalAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cDhcpv4ServerNotifyDuplicateMac.setStatus('current')
cDhcpv4ServerNotifyClientOrServerDetected = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("client", 1), ("server", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cDhcpv4ServerNotifyClientOrServerDetected.setStatus('current')
cDhcpv4ServerNotifyServerStart = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 4), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cDhcpv4ServerNotifyServerStart.setStatus('current')
cDhcpv4ServerNotifyServerStop = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cDhcpv4ServerNotifyServerStop.setStatus('current')
cDhcpv4ServerNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2))
cDhcpv4ServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0))
cDhcpv4ServerFreeAddressLow = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 1)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrLowThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"))
if mibBuilder.loadTexts: cDhcpv4ServerFreeAddressLow.setStatus('current')
cDhcpv4ServerFreeAddressHigh = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 2)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrHighThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"))
if mibBuilder.loadTexts: cDhcpv4ServerFreeAddressHigh.setStatus('current')
cDhcpv4ServerStartTime = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 3)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStart"))
if mibBuilder.loadTexts: cDhcpv4ServerStartTime.setStatus('current')
cDhcpv4ServerStopTime = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 4)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStop"))
if mibBuilder.loadTexts: cDhcpv4ServerStopTime.setStatus('current')
cDhcpv4ServerDuplicateAddress = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 5)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateIpAddr"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateMac"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyClientOrServerDetected"))
if mibBuilder.loadTexts: cDhcpv4ServerDuplicateAddress.setStatus('current')
cDhcpv4SrvCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1))
cDhcpv4SrvGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2))
cDhcpv4SrvCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1, 1)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountersGroup"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CounterObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountersGroup"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCounterObjects"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4SrvCompliance = cDhcpv4SrvCompliance.setStatus('deprecated')
cDhcpv4SrvComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1, 2)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountersGroup"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CounterObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountersGroup"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCounterObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientObjects"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyObjectsGroup"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4SrvComplianceRev1 = cDhcpv4SrvComplianceRev1.setStatus('current')
cDhcpv4SrvSystemObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 1)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemDescr"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemObjectID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4SrvSystemObjects = cDhcpv4SrvSystemObjects.setStatus('current')
cBootpCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 2)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountRequests"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountInvalids"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountReplies"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountDropUnknownClients"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountDropNotServingSubnet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cBootpCountersGroup = cBootpCountersGroup.setStatus('current')
cDhcpv4CounterObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 3)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDiscovers"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountOffers"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountRequests"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDeclines"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountAcks"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountNaks"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountReleases"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountInforms"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountInvalids"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDropUnknownClient"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDropNotServingSubnet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4CounterObjects = cDhcpv4CounterObjects.setStatus('current')
cBootpHCCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 4)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountRequests"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountInvalids"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountReplies"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountDropUnknownClients"), ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountDropNotServingSubnet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cBootpHCCountersGroup = cBootpHCCountersGroup.setStatus('current')
cDhcpv4HCCounterObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 5)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDiscovers"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountOffers"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountRequests"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDeclines"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountAcks"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountNaks"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountReleases"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountInforms"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountForcedRenews"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountInvalids"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDropUnknownClient"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDropNotServingSubnet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4HCCounterObjects = cDhcpv4HCCounterObjects.setStatus('current')
cDhcpv4ServerSharedNetObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 6)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrLowThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrHighThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetReservedAddresses"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetTotalAddresses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerSharedNetObjects = cDhcpv4ServerSharedNetObjects.setStatus('current')
cDhcpv4ServerSubnetObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 7)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetMask"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetSharedNetworkName"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrLowThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrHighThreshold"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddresses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerSubnetObjects = cDhcpv4ServerSubnetObjects.setStatus('current')
cDhcpv4ServerRangeObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 8)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeSubnetMask"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeInUse"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeOutstandingOffers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerRangeObjects = cDhcpv4ServerRangeObjects.setStatus('current')
cDhcpv4ServerClientObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 9)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientSubnetMask"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientRange"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientLeaseType"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientTimeRemaining"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientAllowedProtocol"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientServedProtocol"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientPhysicalAddress"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientClientId"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientHostName"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientDomainName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerClientObjects = cDhcpv4ServerClientObjects.setStatus('current')
cDhcpv4ServerNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 10)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateIpAddr"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateMac"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyClientOrServerDetected"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStart"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerNotifyObjectsGroup = cDhcpv4ServerNotifyObjectsGroup.setStatus('current')
cDhcpv4ServerNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 11)).setObjects(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerFreeAddressLow"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerFreeAddressHigh"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerStartTime"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerStopTime"), ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerDuplicateAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDhcpv4ServerNotificationsGroup = cDhcpv4ServerNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-MIB", cBootpHCCountDropUnknownClients=cBootpHCCountDropUnknownClients, cDhcpv4ServerNotifyDuplicateMac=cDhcpv4ServerNotifyDuplicateMac, cDhcpv4CountAcks=cDhcpv4CountAcks, cDhcpv4CounterObjects=cDhcpv4CounterObjects, cDhcpv4Counters=cDhcpv4Counters, cDhcpv4HCCountDeclines=cDhcpv4HCCountDeclines, cDhcpv4HCCountDropNotServingSubnet=cDhcpv4HCCountDropNotServingSubnet, cBootpCountDropUnknownClients=cBootpCountDropUnknownClients, cDhcpv4ServerRangeInUse=cDhcpv4ServerRangeInUse, cDhcpv4HCCounters=cDhcpv4HCCounters, cBootpCountersGroup=cBootpCountersGroup, cDhcpv4SrvComplianceRev1=cDhcpv4SrvComplianceRev1, cDhcpv4ServerSharedNetTable=cDhcpv4ServerSharedNetTable, cBootpCountDropNotServingSubnet=cBootpCountDropNotServingSubnet, cBootpHCCountDropNotServingSubnet=cBootpHCCountDropNotServingSubnet, cDhcpv4ServerNotifyClientOrServerDetected=cDhcpv4ServerNotifyClientOrServerDetected, cDhcpv4ServerClient=cDhcpv4ServerClient, cDhcpv4ServerStopTime=cDhcpv4ServerStopTime, cDhcpv4ServerSubnetFreeAddrHighThreshold=cDhcpv4ServerSubnetFreeAddrHighThreshold, cDhcpv4HCCountOffers=cDhcpv4HCCountOffers, cBootpCounters=cBootpCounters, cDhcpv4CountInvalids=cDhcpv4CountInvalids, cDhcpv4ServerNotifyServerStart=cDhcpv4ServerNotifyServerStart, cDhcpv4ServerSubnetObjects=cDhcpv4ServerSubnetObjects, cDhcpv4HCCountDiscovers=cDhcpv4HCCountDiscovers, cDhcpv4ServerClientTable=cDhcpv4ServerClientTable, cDhcpv4ServerFreeAddressHigh=cDhcpv4ServerFreeAddressHigh, cDhcpv4SrvSystemObjectID=cDhcpv4SrvSystemObjectID, cBootpHCCountReplies=cBootpHCCountReplies, cDhcpv4ServerSubnetSharedNetworkName=cDhcpv4ServerSubnetSharedNetworkName, cDhcpv4ServerClientLeaseType=cDhcpv4ServerClientLeaseType, cDhcpv4ServerSubnetTable=cDhcpv4ServerSubnetTable, cDhcpv4ServerClientDomainName=cDhcpv4ServerClientDomainName, cDhcpv4ServerRangeEndAddress=cDhcpv4ServerRangeEndAddress, cDhcpv4CountInforms=cDhcpv4CountInforms, cDhcpv4HCCountInforms=cDhcpv4HCCountInforms, cDhcpv4ServerDuplicateAddress=cDhcpv4ServerDuplicateAddress, cDhcpv4ServerRangeEntry=cDhcpv4ServerRangeEntry, ciscoIetfDhcpSrvMIB=ciscoIetfDhcpSrvMIB, cDhcpv4ServerSharedNetEntry=cDhcpv4ServerSharedNetEntry, cDhcpv4HCCountReleases=cDhcpv4HCCountReleases, cBootpHCCountRequests=cBootpHCCountRequests, cDhcpv4ServerClientSubnetMask=cDhcpv4ServerClientSubnetMask, cDhcpv4SrvCompliances=cDhcpv4SrvCompliances, cDhcpv4ServerRangeStartAddress=cDhcpv4ServerRangeStartAddress, ciscoIetfDhcpv4SrvMIBNotifs=ciscoIetfDhcpv4SrvMIBNotifs, cDhcpv4HCCountInvalids=cDhcpv4HCCountInvalids, cDhcpv4CountDeclines=cDhcpv4CountDeclines, cDhcpv4SrvCompliance=cDhcpv4SrvCompliance, cDhcpv4ServerClientHostName=cDhcpv4ServerClientHostName, cDhcpv4SrvSystem=cDhcpv4SrvSystem, cDhcpv4HCCountAcks=cDhcpv4HCCountAcks, cDhcpv4ServerNotifyServerStop=cDhcpv4ServerNotifyServerStop, cDhcpv4ServerRangeTable=cDhcpv4ServerRangeTable, ciscoIetfDhcpv4SrvMIBObjects=ciscoIetfDhcpv4SrvMIBObjects, cDhcpv4HCCountRequests=cDhcpv4HCCountRequests, cDhcpv4ServerFreeAddressLow=cDhcpv4ServerFreeAddressLow, cDhcpv4ServerClientRange=cDhcpv4ServerClientRange, cBootpCountRequests=cBootpCountRequests, cDhcpv4ServerStartTime=cDhcpv4ServerStartTime, cDhcpv4ServerSharedNetReservedAddresses=cDhcpv4ServerSharedNetReservedAddresses, cDhcpv4CountDiscovers=cDhcpv4CountDiscovers, cDhcpv4ServerNotifyObjectsGroup=cDhcpv4ServerNotifyObjectsGroup, cDhcpv4ServerClientPhysicalAddress=cDhcpv4ServerClientPhysicalAddress, cDhcpv4ServerClientEntry=cDhcpv4ServerClientEntry, cBootpHCCounters=cBootpHCCounters, cBootpHCCountersGroup=cBootpHCCountersGroup, cDhcpv4CountDropNotServingSubnet=cDhcpv4CountDropNotServingSubnet, cDhcpv4ServerSharedNetFreeAddresses=cDhcpv4ServerSharedNetFreeAddresses, cDhcpv4ServerNotifyDuplicateIpAddr=cDhcpv4ServerNotifyDuplicateIpAddr, cDhcpv4SrvSystemObjects=cDhcpv4SrvSystemObjects, ciscoIetfDhcpv4SrvMIBConform=ciscoIetfDhcpv4SrvMIBConform, cDhcpv4CountNaks=cDhcpv4CountNaks, cDhcpv4ServerRangeOutstandingOffers=cDhcpv4ServerRangeOutstandingOffers, cDhcpv4HCCountForcedRenews=cDhcpv4HCCountForcedRenews, cBootpCountInvalids=cBootpCountInvalids, cDhcpv4ServerNotifications=cDhcpv4ServerNotifications, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvMIB, cDhcpv4ServerSharedNetFreeAddrHighThreshold=cDhcpv4ServerSharedNetFreeAddrHighThreshold, cDhcpv4ServerSubnetAddress=cDhcpv4ServerSubnetAddress, cDhcpv4ServerClientClientId=cDhcpv4ServerClientClientId, cDhcpv4ServerSubnetFreeAddresses=cDhcpv4ServerSubnetFreeAddresses, cBootpHCCountInvalids=cBootpHCCountInvalids, cDhcpv4ServerRangeSubnetMask=cDhcpv4ServerRangeSubnetMask, cDhcpv4ServerNotifyObjects=cDhcpv4ServerNotifyObjects, cDhcpv4HCCountNaks=cDhcpv4HCCountNaks, cDhcpv4ServerClientAllowedProtocol=cDhcpv4ServerClientAllowedProtocol, cDhcpv4ServerNotificationsGroup=cDhcpv4ServerNotificationsGroup, cDhcpv4CountDropUnknownClient=cDhcpv4CountDropUnknownClient, cDhcpv4SrvSystemDescr=cDhcpv4SrvSystemDescr, CDhcpv4PhysicalAddress=CDhcpv4PhysicalAddress, cDhcpv4HCCounterObjects=cDhcpv4HCCounterObjects, cDhcpv4ServerSharedNetFreeAddrLowThreshold=cDhcpv4ServerSharedNetFreeAddrLowThreshold, cDhcpv4ServerSubnetEntry=cDhcpv4ServerSubnetEntry, cDhcpv4ServerSubnetFreeAddrLowThreshold=cDhcpv4ServerSubnetFreeAddrLowThreshold, cDhcpv4ServerNotificationPrefix=cDhcpv4ServerNotificationPrefix, cDhcpv4ServerRangeObjects=cDhcpv4ServerRangeObjects, cDhcpv4CountOffers=cDhcpv4CountOffers, cDhcpv4ServerClientTimeRemaining=cDhcpv4ServerClientTimeRemaining, cDhcpv4ServerSubnetMask=cDhcpv4ServerSubnetMask, cBootpCountReplies=cBootpCountReplies, cDhcpv4ServerSharedNetObjects=cDhcpv4ServerSharedNetObjects, cDhcpv4SrvGroups=cDhcpv4SrvGroups, cDhcpv4ServerClientObjects=cDhcpv4ServerClientObjects, cDhcpv4CountRequests=cDhcpv4CountRequests, cDhcpv4CountReleases=cDhcpv4CountReleases, cDhcpv4HCCountDropUnknownClient=cDhcpv4HCCountDropUnknownClient, cDhcpv4ServerSharedNetTotalAddresses=cDhcpv4ServerSharedNetTotalAddresses, cDhcpv4SrvConfiguration=cDhcpv4SrvConfiguration, cDhcpv4ServerSharedNetName=cDhcpv4ServerSharedNetName, cDhcpv4ServerClientServedProtocol=cDhcpv4ServerClientServedProtocol)
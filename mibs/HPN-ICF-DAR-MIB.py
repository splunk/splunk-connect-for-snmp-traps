#
# PySNMP MIB module HPN-ICF-DAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Gauge32, Unsigned32, Bits, Counter64, TimeTicks, IpAddress, NotificationType, Counter32, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Gauge32", "Unsigned32", "Bits", "Counter64", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfDar = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112))
if mibBuilder.loadTexts: hpnicfDar.setLastUpdated('201011030000Z')
if mibBuilder.loadTexts: hpnicfDar.setOrganization('')
class HpnicfDarProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89))
    namedValues = NamedValues(("invalidProtocol", 1), ("bgp", 2), ("cifs", 3), ("citrix", 4), ("cuseeme", 5), ("dhcp", 6), ("dns", 7), ("egp", 8), ("eigrp", 9), ("exchange", 10), ("fasttrack", 11), ("finger", 12), ("ftp", 13), ("gnutella", 14), ("gopher", 15), ("gre", 16), ("http", 17), ("h323", 18), ("icmp", 19), ("igmp", 20), ("imap", 21), ("ip", 22), ("ipinip", 23), ("ipsec", 24), ("ipv6", 25), ("irc", 26), ("kerberos", 27), ("l2tp", 28), ("ldap", 29), ("mgcp", 30), ("napster", 31), ("netbios", 32), ("netshow", 33), ("nfs", 34), ("nntp", 35), ("notes", 36), ("novadign", 37), ("ntp", 38), ("pcanywhere", 39), ("pop3", 40), ("pptp", 41), ("printer", 42), ("rcmd", 43), ("rip", 44), ("rsvp", 45), ("rtcp", 46), ("rtp", 47), ("rtsp", 48), ("secureftp", 49), ("securehttp", 50), ("secureimap", 51), ("secureirc", 52), ("secureldap", 53), ("securenntp", 54), ("securepop3", 55), ("securetelnet", 56), ("sip", 57), ("skinny", 58), ("smtp", 59), ("snmp", 60), ("socks", 61), ("sqlnet", 62), ("sqlserver", 63), ("ssh", 64), ("streamwork", 65), ("sunrpc", 66), ("syslog", 67), ("tcp", 68), ("tcphandshake", 69), ("telnet", 70), ("tftp", 71), ("total", 72), ("udp", 73), ("unknownothers", 74), ("unknowntcp", 75), ("unknownudp", 76), ("userdefine001", 77), ("userdefine002", 78), ("userdefine003", 79), ("userdefine004", 80), ("userdefine005", 81), ("userdefine006", 82), ("userdefine007", 83), ("userdefine008", 84), ("userdefine009", 85), ("userdefine010", 86), ("vdolive", 87), ("winmx", 88), ("xwindows", 89))

hpnicfDarIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1))
hpnicfDarIfStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1))
hpnicfDarStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfDarStatisticsTable.setStatus('current')
hpnicfDarStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-DAR-MIB", "hpnicfDarStatisticsProtocolID"))
if mibBuilder.loadTexts: hpnicfDarStatisticsEntry.setStatus('current')
hpnicfDarStatisticsProtocolID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 1), HpnicfDarProtocol())
if mibBuilder.loadTexts: hpnicfDarStatisticsProtocolID.setStatus('current')
hpnicfDarStatisticsProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsProtocolName.setStatus('current')
hpnicfDarStatisticsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsInPkts.setStatus('current')
hpnicfDarStatisticsInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsInBytes.setStatus('current')
hpnicfDarStatisticsInBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsInBitRate.setStatus('current')
hpnicfDarStatisticsMaxInBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsMaxInBitRate.setStatus('current')
hpnicfDarStatisticsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsOutPkts.setStatus('current')
hpnicfDarStatisticsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsOutBytes.setStatus('current')
hpnicfDarStatisticsOutBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsOutBitRate.setStatus('current')
hpnicfDarStatisticsMaxOutBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDarStatisticsMaxOutBitRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-DAR-MIB", hpnicfDarStatisticsOutBytes=hpnicfDarStatisticsOutBytes, hpnicfDarStatisticsOutBitRate=hpnicfDarStatisticsOutBitRate, hpnicfDarStatisticsMaxOutBitRate=hpnicfDarStatisticsMaxOutBitRate, hpnicfDarIfStatisticsObjects=hpnicfDarIfStatisticsObjects, PYSNMP_MODULE_ID=hpnicfDar, hpnicfDarStatisticsInBytes=hpnicfDarStatisticsInBytes, hpnicfDarIfObjects=hpnicfDarIfObjects, hpnicfDar=hpnicfDar, HpnicfDarProtocol=HpnicfDarProtocol, hpnicfDarStatisticsTable=hpnicfDarStatisticsTable, hpnicfDarStatisticsProtocolID=hpnicfDarStatisticsProtocolID, hpnicfDarStatisticsProtocolName=hpnicfDarStatisticsProtocolName, hpnicfDarStatisticsInBitRate=hpnicfDarStatisticsInBitRate, hpnicfDarStatisticsMaxInBitRate=hpnicfDarStatisticsMaxInBitRate, hpnicfDarStatisticsOutPkts=hpnicfDarStatisticsOutPkts, hpnicfDarStatisticsEntry=hpnicfDarStatisticsEntry, hpnicfDarStatisticsInPkts=hpnicfDarStatisticsInPkts)

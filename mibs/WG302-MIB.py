#
# PySNMP MIB module WG302-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WG302-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Unsigned32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32, iso, ObjectIdentity, Integer32, ModuleIdentity, IpAddress, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "Integer32", "ModuleIdentity", "IpAddress", "enterprises", "NotificationType")
TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
accesspoint = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 4, 2))
if mibBuilder.loadTexts: accesspoint.setLastUpdated('200411030003Z')
if mibBuilder.loadTexts: accesspoint.setOrganization('NETGEAR Inc.')
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4))
lanSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1))
apName = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apName.setStatus('current')
adminName = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: adminName.setStatus('current')
adminPasswd = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: adminPasswd.setStatus('current')
dhcpStatus = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("static", 0), ("dhcpclient", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpStatus.setStatus('current')
ipAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddr.setStatus('current')
netmaskAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netmaskAddr.setStatus('current')
gatewayAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gatewayAddr.setStatus('current')
spantree = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spantree.setStatus('current')
pridnsipAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pridnsipAddr.setStatus('current')
snddnsipAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snddnsipAddr.setStatus('current')
wlanSettingTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2), )
if mibBuilder.loadTexts: wlanSettingTable.setStatus('current')
wlanSettingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: wlanSettingEntry.setStatus('current')
operatemode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("auto", 0), ("dot11b", 2), ("dot11g", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: operatemode.setStatus('current')
ssid = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssid.setStatus('current')
countrycode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(410, 36, 124, 208, 40, 246, 250, 276, 372, 380, 392, 484, 528, 554, 578, 630, 340, 724, 752, 756, 826, 840))).clone(namedValues=NamedValues(("asia", 410), ("australia", 36), ("canada", 124), ("denmark", 208), ("europe", 40), ("finland", 246), ("france", 250), ("germany", 276), ("ireland", 372), ("italy", 380), ("japan", 392), ("mexico", 484), ("netherlands", 528), ("newzealand", 554), ("norway", 578), ("puertorico", 630), ("southamerica", 340), ("spain", 724), ("sweden", 752), ("switzerland", 756), ("unitedkingdom", 826), ("unitedstates", 840)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: countrycode.setStatus('current')
channel = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: channel.setStatus('current')
datarate = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: datarate.setStatus('current')
beaconinterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: beaconinterval.setStatus('current')
rtsthreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2346))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtsthreshold.setStatus('current')
fraglength = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 2346))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fraglength.setStatus('current')
dtiminterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtiminterval.setStatus('current')
preambletype = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("long", 0), ("auto", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preambletype.setStatus('current')
hidenetworkname = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hidenetworkname.setStatus('current')
txpower = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("full", 0), ("half", 1), ("quarter", 2), ("eighth", 3), ("min", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: txpower.setStatus('current')
superG = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: superG.setStatus('current')
antenna = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: antenna.setStatus('current')
securityTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3), )
if mibBuilder.loadTexts: securityTable.setStatus('current')
securityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: securityEntry.setStatus('current')
authenticationtype = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 0), ("shared", 1), ("legacy802dot1x", 2), ("wpa", 3), ("wpapsk", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authenticationtype.setStatus('current')
encryption = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("wep", 1), ("tkip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: encryption.setStatus('current')
encryptionstrength = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 40, 104, 128))).clone(namedValues=NamedValues(("none", 0), ("wep64", 40), ("wep128", 104), ("wep152", 128)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: encryptionstrength.setStatus('current')
keyno = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: keyno.setStatus('current')
key1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: key1.setStatus('current')
key2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: key2.setStatus('current')
key3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: key3.setStatus('current')
key4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: key4.setStatus('current')
wlanseparator = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlanseparator.setStatus('current')
presharekey = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: presharekey.setStatus('current')
remoteSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4))
sshd = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshd.setStatus('current')
snmpenable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpenable.setStatus('current')
trapServerIP = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapServerIP.setStatus('current')
readOnlyCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: readOnlyCommunity.setStatus('current')
readWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: readWriteCommunity.setStatus('current')
statistic = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5))
wiredethernetstat = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1))
lanrecvpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanrecvpacket.setStatus('current')
lantranspacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lantranspacket.setStatus('current')
lanrecvbytes = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanrecvbytes.setStatus('current')
lantransbytes = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lantransbytes.setStatus('current')
wirelessstat = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2))
wlanrecvunicastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanrecvunicastpacket.setStatus('current')
wlantransunicastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlantransunicastpacket.setStatus('current')
wlanrecvbroadcastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanrecvbroadcastpacket.setStatus('current')
wlantransbroadcastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlantransbroadcastpacket.setStatus('current')
wlanrecvmulticastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanrecvmulticastpacket.setStatus('current')
wlantransmulticastpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlantransmulticastpacket.setStatus('current')
wlanrecvpacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanrecvpacket.setStatus('current')
wlantranspacket = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlantranspacket.setStatus('current')
wlanrecvbytes = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanrecvbytes.setStatus('current')
wlantransbytes = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlantransbytes.setStatus('current')
stationnumber = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stationnumber.setStatus('current')
stationListTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 4, 2, 6), )
if mibBuilder.loadTexts: stationListTable.setStatus('current')
stationListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: stationListEntry.setStatus('current')
macaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macaddress.setStatus('current')
ipaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddr.setStatus('current')
stationstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("authenticating", 1), ("authenticated", 2), ("associating", 3), ("associated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stationstatus.setStatus('current')
operationapmode = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7))
apmode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ap", 0), ("ptp", 2), ("ptp-ap", 3), ("pxp", 4), ("pxp-ap", 5), ("repeater", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apmode.setStatus('current')
ptpremotemacaddress = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpremotemacaddress.setStatus('current')
pxpremotemacaddress1 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxpremotemacaddress1.setStatus('current')
pxpremotemacaddress2 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxpremotemacaddress2.setStatus('current')
pxpremotemacaddress3 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxpremotemacaddress3.setStatus('current')
pxpremotemacaddress4 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxpremotemacaddress4.setStatus('current')
repremotemacaddress1 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 7), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repremotemacaddress1.setStatus('current')
repremotemacaddress2 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repremotemacaddress2.setStatus('current')
repremotemacaddress3 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 9), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repremotemacaddress3.setStatus('current')
repremotemacaddress4 = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 10), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repremotemacaddress4.setStatus('current')
info802dot1x = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8))
authinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1))
priradipaddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priradipaddr.setStatus('current')
priradport = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priradport.setStatus('current')
priradsharedsecret = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priradsharedsecret.setStatus('current')
sndradipaddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndradipaddr.setStatus('current')
sndradport = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndradport.setStatus('current')
sndradsharedsecret = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndradsharedsecret.setStatus('current')
reauthtime = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reauthtime.setStatus('current')
accntinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2))
priacntipaddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priacntipaddr.setStatus('current')
priacntport = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priacntport.setStatus('current')
priacntsharedsecret = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priacntsharedsecret.setStatus('current')
sndacntipaddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndacntipaddr.setStatus('current')
sndacntport = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndacntport.setStatus('current')
sndacntsharedsecret = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sndacntsharedsecret.setStatus('current')
userCommand = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 9))
resetAP = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 9, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetAP.setStatus('current')
setWirelessstatus = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 9, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setWirelessstatus.setStatus('current')
timeSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 10))
currenttime = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currenttime.setStatus('current')
timezone = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74))).clone(namedValues=NamedValues(("gmtwest12-international-date-line-west", 0), ("gmtwest11-midway-island-samoa", 1), ("gmtwest10-hawaii", 2), ("gmtwest09-alaska", 3), ("gmtwest08-pacific-time-us-canada-tijuana", 4), ("gmtwest07-arizona", 5), ("gmtwest07-chihuahua-la-paz-mazatlan", 6), ("gmtwest07-mountain-time-us-canada", 7), ("gmtwest06-central-america", 8), ("gmtwest06-central-time-us-canada", 9), ("gmtwest06-guadalajara-mexico-city-monterrey", 10), ("gmtwest06-saskatchewan", 11), ("gmtwest05-bogota-lima-quito", 12), ("gmtwest05-eastern-time-us-canada", 13), ("gmtwest05-indiana-east", 14), ("gmtwest04-atlantic-Time-canada", 15), ("gmtwest04-caracas-la-paz", 16), ("gmtwest04-santiago", 17), ("gmtwest03-30-newfoundland", 18), ("gmtwest03-brasilia", 19), ("gmtwest03-buenos-aires-georgetown", 20), ("gmtwest03-greenland", 21), ("gmtwest02-mid-atlantic", 22), ("gmtwest01-azores", 23), ("gmtwest01-cape-verde-is", 24), ("gmt00-casablanca-monrovia", 25), ("gmt00-greenwich-mean-time-dublin-edinburgh-lisbon-London", 26), ("gmteast01-amsterdam-berlin-bern-rome-stockholm-vienna", 27), ("gmteast01-belgrade-bratislava-budapest-ljubljana-prague", 28), ("gmteast01-brussels-copenhagen-madrid-paris", 29), ("gmteast01-sarajevo-skopje-warsaw-zagreb", 30), ("gmteast01-west-central-africa", 31), ("gmteast02-athens-istanbul-minsk", 32), ("gmteast02-bucharest", 33), ("gmteast02-cairo", 34), ("gmteast02-harare-pretoria", 35), ("gmteast02-helsinki-kyiv-riga-sofia-tallinn-vilnius", 36), ("gmteast02-jerusalem", 37), ("gmteast03-baghdad", 38), ("gmteast03-kuwait-riyadh", 39), ("gmteast03-moscow-st-petersburg-volgograd", 40), ("gmteast03-nairobi", 41), ("gmteast03-tehran", 42), ("gmteast04-abu-dhabi-muscat", 43), ("gmteast04-baku-tbilisi-yerevan", 44), ("gmteast04-kabul", 45), ("gmteast05-ekaterinburg", 46), ("gmteast05-islamabad-karachi-kashkent", 47), ("gmteast05-chennai-kolkata-mumbai-new-delhi", 48), ("gmteast05-kathmandu", 49), ("gmteast06-almaty-novosibirsk", 50), ("gmteast06-astana-dhaka", 51), ("gmteast06-sri-jayawardenepura", 52), ("gmteast06-rangoon", 53), ("gmteast07-bangkok-hanoi-jakarta", 54), ("gmteast07-krasnoyarsk", 55), ("gmteast08-beijing-chongqing-hong-kong-urumqi", 56), ("gmteast08-irkutsk-ulaan-bataar", 57), ("gmteast08-kuala-lumpur-singapore", 58), ("gmteast08-perth", 59), ("gmteast08-taipei", 60), ("gmteast09-osaka-sapporo-tokyo", 61), ("gmteast09-seoul", 62), ("gmteast09-yakutsk", 63), ("gmteast09-adelaide", 64), ("gmteast09-darwin", 65), ("gmteast10-brisbane", 66), ("gmteast10-canberra-melbourne-sydney", 67), ("gmteast10-guam-port-moresby", 68), ("gmteast10-hobart", 69), ("gmteast10-vladivostok", 70), ("gmteast11-magadan-solomon-is-new-caledonia", 71), ("gmteast12-auckland-wellington", 72), ("gmteast12-fiji-kamchatka-marshall-is", 73), ("gmteast13-nuku-alofa", 74)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timezone.setStatus('current')
daylightsaving = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daylightsaving.setStatus('current')
dhcpsSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11))
dhcpserver = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpserver.setStatus('current')
dhcpsipstart = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsipstart.setStatus('current')
dhcpsipend = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsipend.setStatus('current')
dhcpnetmask = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpnetmask.setStatus('current')
dhcpsgateway = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsgateway.setStatus('current')
dhcpspridns = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpspridns.setStatus('current')
dhcpspsnddns = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpspsnddns.setStatus('current')
dhcpspriwins = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpspriwins.setStatus('current')
dhcpspsndwins = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpspsndwins.setStatus('current')
dhcpsleasetime = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 44640))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsleasetime.setStatus('current')
anyip = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anyip.setStatus('current')
logSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 4, 2, 12))
syslog = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslog.setStatus('current')
syslogsrvip = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogsrvip.setStatus('current')
syslogsrvport = MibScalar((1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogsrvport.setStatus('current')
mibBuilder.exportSymbols("WG302-MIB", dhcpnetmask=dhcpnetmask, datarate=datarate, macaddress=macaddress, PYSNMP_MODULE_ID=accesspoint, lantranspacket=lantranspacket, channel=channel, sshd=sshd, dtiminterval=dtiminterval, wirelessstat=wirelessstat, stationnumber=stationnumber, key1=key1, sndradport=sndradport, operationapmode=operationapmode, snddnsipAddr=snddnsipAddr, pridnsipAddr=pridnsipAddr, securityEntry=securityEntry, wlanSettingEntry=wlanSettingEntry, hidenetworkname=hidenetworkname, reauthtime=reauthtime, dhcpsipend=dhcpsipend, readWriteCommunity=readWriteCommunity, priradipaddr=priradipaddr, keyno=keyno, wlanrecvpacket=wlanrecvpacket, repremotemacaddress3=repremotemacaddress3, beaconinterval=beaconinterval, timeSettings=timeSettings, lanrecvbytes=lanrecvbytes, gatewayAddr=gatewayAddr, encryption=encryption, adminName=adminName, lanrecvpacket=lanrecvpacket, priacntipaddr=priacntipaddr, wlanseparator=wlanseparator, repremotemacaddress1=repremotemacaddress1, ipAddr=ipAddr, priacntport=priacntport, stationListTable=stationListTable, key2=key2, wlanrecvbytes=wlanrecvbytes, apName=apName, key3=key3, netgear=netgear, wlantranspacket=wlantranspacket, logSettings=logSettings, syslogsrvip=syslogsrvip, readOnlyCommunity=readOnlyCommunity, accntinfo=accntinfo, priacntsharedsecret=priacntsharedsecret, syslog=syslog, countrycode=countrycode, authenticationtype=authenticationtype, wiredethernetstat=wiredethernetstat, dhcpspridns=dhcpspridns, sndacntport=sndacntport, ssid=ssid, repremotemacaddress4=repremotemacaddress4, daylightsaving=daylightsaving, encryptionstrength=encryptionstrength, antenna=antenna, sndacntipaddr=sndacntipaddr, trapServerIP=trapServerIP, pxpremotemacaddress4=pxpremotemacaddress4, priradport=priradport, operatemode=operatemode, snmpenable=snmpenable, spantree=spantree, lanSettings=lanSettings, anyip=anyip, netmaskAddr=netmaskAddr, dhcpsSettings=dhcpsSettings, txpower=txpower, adminPasswd=adminPasswd, dhcpserver=dhcpserver, dhcpsipstart=dhcpsipstart, rtsthreshold=rtsthreshold, statistic=statistic, dhcpspsndwins=dhcpspsndwins, accesspoint=accesspoint, key4=key4, presharekey=presharekey, remoteSettings=remoteSettings, authinfo=authinfo, resetAP=resetAP, dhcpStatus=dhcpStatus, ipaddr=ipaddr, info802dot1x=info802dot1x, fraglength=fraglength, wlanSettingTable=wlanSettingTable, currenttime=currenttime, pxpremotemacaddress2=pxpremotemacaddress2, wlanrecvunicastpacket=wlanrecvunicastpacket, dhcpspriwins=dhcpspriwins, dhcpsgateway=dhcpsgateway, superG=superG, wlanrecvmulticastpacket=wlanrecvmulticastpacket, wlanrecvbroadcastpacket=wlanrecvbroadcastpacket, pxpremotemacaddress1=pxpremotemacaddress1, userCommand=userCommand, wlantransunicastpacket=wlantransunicastpacket, dhcpsleasetime=dhcpsleasetime, lantransbytes=lantransbytes, wlantransbytes=wlantransbytes, sndacntsharedsecret=sndacntsharedsecret, setWirelessstatus=setWirelessstatus, wlantransmulticastpacket=wlantransmulticastpacket, sndradsharedsecret=sndradsharedsecret, securityTable=securityTable, pxpremotemacaddress3=pxpremotemacaddress3, sndradipaddr=sndradipaddr, dhcpspsnddns=dhcpspsnddns, priradsharedsecret=priradsharedsecret, preambletype=preambletype, ptpremotemacaddress=ptpremotemacaddress, wlantransbroadcastpacket=wlantransbroadcastpacket, stationListEntry=stationListEntry, apmode=apmode, syslogsrvport=syslogsrvport, repremotemacaddress2=repremotemacaddress2, wireless=wireless, stationstatus=stationstatus, timezone=timezone)

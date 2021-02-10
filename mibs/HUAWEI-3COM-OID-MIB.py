#
# PySNMP MIB module HUAWEI-3COM-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-3COM-OID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, enterprises, Counter64, Counter32, Unsigned32, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "enterprises", "Counter64", "Counter32", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
hwLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
huaweiMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6))
h3c = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10))
huaweiTCMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 20021210))
quidway = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 1))
hwInternetProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2))
lanSw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23))
mlsr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33))
dlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34))
hwDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7))
hwMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12))
hwpaeExtMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 22))
huaweiDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 1))
hwCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 7))
h3cProductId = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 1))
h3cCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2))
h3cEntityVendorTypeOID = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 3))
h3cNM = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 4))
hwSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 6))
h3cSNMPAgCpb = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 7))
h3cRhw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 8))
h3cSurveillanceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9))
h3cStorageRef = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10))
rIp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 1))
rIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2))
vrpProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 3))
rmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 4))
huawei_qos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 3, 2)).setLabel("huawei-qos")
huawei_vlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 3, 3)).setLabel("huawei-vlan")
lswCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1))
hwLswExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1))
hwLswVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2))
hwLswMacPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3))
hwLswArpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4))
hwLswL2InfMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5))
hwLswRstpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6))
hwLswIgmpsnoopingMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7))
hwLswDhcpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 8))
hwLswdevMMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9))
hwsLswTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12))
hwdot1sMstp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 14))
hwLswQosAclMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16))
hwLswMix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17))
hwLswDeviceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 18))
terminalServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 1))
huaweiNDEC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2))
redundancyPower = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 4))
redundancyFan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 5))
hwmSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 6))
hw8040If = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7))
pos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 8))
hwIsdnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 9))
aR46_E200 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20)).setLabel("aR46-E200")
hwDHCPRelayMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7, 1))
hwDHCPServerMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7, 2))
hwMplsLsr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 1))
hwMplsLdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 2))
hwMplsVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 3))
voice = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1))
hwIPX = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 2))
hwFWTP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 3))
hwHIIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 4))
hwHRP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 5))
hwASPF = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 6))
hwNAT = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 7))
hwBLS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8))
hwMACBIND = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 9))
hwATK = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 10))
hwSECSTAT = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 11))
hwPFLT = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 12))
hwTRNG = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 13))
hwSMAP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14))
hwSZONE = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15))
hwSLOG = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16))
hwSSHMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 17))
hwUserLogMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18))
hwSystemMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 19))
hwTACACS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 20))
hwNBPortalMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 21))
hwNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 22))
hwCmdOverSnmpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 23))
hwISIS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 24))
hwLAG = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 25))
hwSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26))
hwTask = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27))
hwDismanPing = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 28))
hwVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 29))
hwAddrMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 30))
hwEntityExtentMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 31))
hwQoS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 32))
hwMultilinkPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 33))
hwTCPMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34))
hwBGPMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 35))
hwVoiceGeneralMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1))
hwVoiceIfMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2))
hwVoiceAnalogInterfaceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3))
hwVoiceDigitalInterfaceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 4))
hwVoiceDialControlMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5))
hwVoiceCallActiveMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6))
hwVoiceCallHistoryMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7))
hwVoiceGKClientMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8))
hwVoiceAAAClientMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9))
hwVoiceH323CallStatMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11))
hwSIPMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12))
h3cFtm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 1))
h3cUIMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 2))
h3cSystemMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 3))
h3cConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 4))
h3cFlash = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5))
h3cEntityExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 6))
h3cIPSecMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 7))
h3cAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 8))
h3cVoiceVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9))
h3cL4Redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 10))
h3cIpPBX = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 11))
h3cUser = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12))
h3cRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 13))
h3cPowerEthernetExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 14))
h3cEntityRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15))
h3cProtocolVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 16))
h3cQosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17))
h3cNat = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 18))
h3cPos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 19))
h3cNS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 20))
h3cAAL5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21))
h3cSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 22))
h3cRSA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 23))
h3cVrrpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24))
h3cIpa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 25))
h3cPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 26))
h3cVpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 27))
h3cE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28))
h3cT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 29))
h3cIKEMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 30))
h3cWebSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 31))
h3cAutoDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 32))
h3cIpBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33))
h3cIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 34))
h3cIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 35))
h3cDhcpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36))
h3cProtocolPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37))
h3cTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 38))
h3cVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39))
h3cIfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40))
h3cCfCard = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 41))
h3cEpon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42))
h3cDldp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 43))
h3cUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 44))
h3cRrpp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45))
h3cDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 46))
h3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47))
h3cRcr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 48))
h3cAtmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 49))
h3cMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50))
h3cMpm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 51))
h3cOadp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 52))
h3cTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 53))
h3cGre = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 54))
h3cObjectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55))
h3cStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 56))
h3cDvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 57))
h3cDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58))
h3cIsis = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 59))
h3cRpr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 60))
h3cSubnetVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 61))
h3cDlswExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 62))
h3cSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63))
h3cFlowTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 64))
h3cQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 65))
h3cStormConstrain = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 66))
h3cIpAddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67))
h3cMirrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68))
h3cQINQ = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 69))
h3cTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70))
h3cIpv6AddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 71))
h3cBfdMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72))
h3cRCP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 73))
h3cAcfp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 74))
h3cDot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75))
h3cE1T1VI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 76))
h3cwapiMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77))
h3cL2VpnPwe3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78))
h3cMplsOam = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79))
h3cMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 80))
h3cSiemMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 81))
h3cUps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82))
h3cEOCCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 83))
h3cHPEOC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 84))
h3cAFC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 85))
h3cMultCDR = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 86))
h3cMACInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 87))
h3cFireWall = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88))
h3cDSP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 89))
h3cNetMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90))
h3cStack = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 91))
h3cPosa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 92))
h3cWebAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 93))
h3cCATVTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94))
h3cLpbkdt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 95))
h3cMultiMedia = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 96))
h3cDns = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 97))
h3c3GModem = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 98))
h3cPortal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 99))
h3clldp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 100))
h3cDHCPServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101))
h3cPPPoEServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 102))
h3cL2Isolate = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 103))
h3cSnmpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104))
h3cVsi = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 105))
h3cEvc = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 106))
h3cMinm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 107))
h3cBlg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108))
h3cRS485 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 109))
h3cARPRatelimit = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 110))
h3cLI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 111))
h3cDar = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112))
h3cPBR = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 113))
h3cAAANasId = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114))
h3cTeTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 115))
h3cLB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 116))
h3cDldp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 117))
h3cWIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 118))
h3cFCoE = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120))
h3cQosCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1))
h3cNqa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 8, 3))
h3cHgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 8, 7))
h3cNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 8, 19))
h3cVMMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 1))
h3cPUMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 2))
h3cMSMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 9, 3))
h3cStorageMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 1))
h3cStorageSnap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 2))
h3cDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3))
h3cRaid = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 4))
h3cLogicVolume = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5))
h3cIfQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 65, 1))
h3cCBQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 65, 2))
mibBuilder.exportSymbols("HUAWEI-3COM-OID-MIB", hwLswQosAclMib=hwLswQosAclMib, h3clldp=h3clldp, huaweiMgmt=huaweiMgmt, h3cCBQos2=h3cCBQos2, hwVoiceGKClientMIB=hwVoiceGKClientMIB, rIp=rIp, hwpaeExtMib=hwpaeExtMib, hwLswDhcpMib=hwLswDhcpMib, redundancyPower=redundancyPower, hwSZONE=hwSZONE, h3cNat=h3cNat, hwSystem=hwSystem, hwVoiceIfMIB=hwVoiceIfMIB, hwVoiceCallHistoryMIB=hwVoiceCallHistoryMIB, hwVoiceH323CallStatMIB=hwVoiceH323CallStatMIB, h3cIpBroadcast=h3cIpBroadcast, h3cPBR=h3cPBR, hwSystemMan=hwSystemMan, h3cStack=h3cStack, h3cIsis=h3cIsis, huaweiNDEC=huaweiNDEC, h3cLB=h3cLB, h3cBfdMIB=h3cBfdMIB, h3cConfig=h3cConfig, huawei_qos=huawei_qos, h3cLogicVolume=h3cLogicVolume, hwATK=hwATK, h3cL2Isolate=h3cL2Isolate, h3cIpv6AddrMIB=h3cIpv6AddrMIB, h3c=h3c, h3cMSMan=h3cMSMan, hwQoS=hwQoS, h3cDhcpSnoop=h3cDhcpSnoop, h3cRrpp=h3cRrpp, h3cMinm=h3cMinm, rIcmp=rIcmp, h3cPUMan=h3cPUMan, hwDHCPServerMib=hwDHCPServerMib, h3cPortal=h3cPortal, h3cFireWall=h3cFireWall, hwUserLogMIB=hwUserLogMIB, h3cPowerEthernetExt=h3cPowerEthernetExt, h3cProductId=h3cProductId, h3cEntityRelation=h3cEntityRelation, h3cDot11=h3cDot11, h3cQINQ=h3cQINQ, h3cAcl=h3cAcl, aR46_E200=aR46_E200, h3cRSA=h3cRSA, h3cIfQos2=h3cIfQos2, hwSmonExtend=hwSmonExtend, h3cBlg=h3cBlg, hwLocal=hwLocal, h3cAFC=h3cAFC, h3cPos=h3cPos, h3cMirrGroup=h3cMirrGroup, h3cCommon=h3cCommon, h3cIpAddrMIB=h3cIpAddrMIB, h3cAcfp=h3cAcfp, hwmSystem=hwmSystem, h3cSSH=h3cSSH, h3cRcr=h3cRcr, h3cAtmDxi=h3cAtmDxi, hwInternetProtocol=hwInternetProtocol, hwMplsVpn=hwMplsVpn, hwTask=hwTask, voice=voice, hwDismanPing=hwDismanPing, router=router, huawei_vlan=huawei_vlan, h3cFtm=h3cFtm, h3cIfExt=h3cIfExt, h3cPPPoEServer=h3cPPPoEServer, rmonExtend=rmonExtend, h3cWebSwitch=h3cWebSwitch, h3cLpbkdt=h3cLpbkdt, h3cRhw=h3cRhw, hwLswRstpMib=hwLswRstpMib, hwISIS=hwISIS, h3cMACInformation=h3cMACInformation, h3cMulticast=h3cMulticast, h3cWIPS=h3cWIPS, h3cVoice=h3cVoice, h3cDldp2=h3cDldp2, h3cMplsOamPs=h3cMplsOamPs, h3cIpa=h3cIpa, hwNTP=hwNTP, h3cT1=h3cT1, h3cE1T1VI=h3cE1T1VI, h3cStorageRef=h3cStorageRef, h3cAAANasId=h3cAAANasId, hwSECSTAT=hwSECSTAT, h3cTeTunnel=h3cTeTunnel, h3cIpx=h3cIpx, h3cFCoE=h3cFCoE, hwVoiceGeneralMIB=hwVoiceGeneralMIB, huawei=huawei, h3cIds=h3cIds, h3cIpPBX=h3cIpPBX, h3cUser=h3cUser, h3cPosa=h3cPosa, h3cFlowTemplate=h3cFlowTemplate, terminalServer=terminalServer, h3cL4Redirect=h3cL4Redirect, h3cRpr=h3cRpr, hwTACACS=hwTACACS, hwSIPMIB=hwSIPMIB, h3cSnmpExt=h3cSnmpExt, hw8040If=hw8040If, h3cMpm=h3cMpm, h3cFlash=h3cFlash, h3cNM=h3cNM, h3cAAL5=h3cAAL5, h3cDSP=h3cDSP, hwLswVlan=hwLswVlan, h3cPortSecurity=h3cPortSecurity, hwDHCPRelayMib=hwDHCPRelayMib, mlsr=mlsr, h3cDHCPServer=h3cDHCPServer, lswCommon=lswCommon, hwTCPMib=hwTCPMib, h3cDisk=h3cDisk, hwPFLT=hwPFLT, h3cNetMan=h3cNetMan, hwIsdnMib=hwIsdnMib, h3cQosCapability=h3cQosCapability, hwMplsLsr=hwMplsLsr, h3cProtocolVlan=h3cProtocolVlan, h3cQosProfile=h3cQosProfile, hwASPF=hwASPF, hwSSHMIB=hwSSHMIB, h3cMplsOam=h3cMplsOam, hwEntityExtentMIB=hwEntityExtentMIB, h3cRadius=h3cRadius, quidway=quidway, hwVoiceDigitalInterfaceMIB=hwVoiceDigitalInterfaceMIB, h3cTrap=h3cTrap, hwLswdevMMib=hwLswdevMMib, h3c3GModem=h3c3GModem, h3cStorageMIB=h3cStorageMIB, h3cVsi=h3cVsi, h3cMultiMedia=h3cMultiMedia, hwBGPMib=hwBGPMib, hwMplsLdp=hwMplsLdp, hwLswDeviceAdmin=hwLswDeviceAdmin, h3cEntityExtend=h3cEntityExtend, h3cIPSecMonitor=h3cIPSecMonitor, h3cVoiceVlan=h3cVoiceVlan, h3cIPS=h3cIPS, h3cDomain=h3cDomain, hwTRNG=hwTRNG, h3cStormConstrain=h3cStormConstrain, h3cUIMgt=h3cUIMgt, h3cEOCCommon=h3cEOCCommon, h3cDlswExt=h3cDlswExt, h3cProtocolPriority=h3cProtocolPriority, h3cCfCard=h3cCfCard, hwdot1sMstp=hwdot1sMstp, huaweiTCMIB=huaweiTCMIB, hwMpls=hwMpls, hwFWTP=hwFWTP, huaweiUtility=huaweiUtility, h3cARPRatelimit=h3cARPRatelimit, hwDhcp=hwDhcp, hwVoiceDialControlMIB=hwVoiceDialControlMIB, hwLswL2InfMib=hwLswL2InfMib, h3cDldp=h3cDldp, h3cwapiMIB=h3cwapiMIB, h3cDns=h3cDns, hwNBPortalMIB=hwNBPortalMIB, hwHRP=hwHRP, hwLswIgmpsnoopingMib=hwLswIgmpsnoopingMib, hwSLOG=hwSLOG, hwMACBIND=hwMACBIND, hwsLswTrapMib=hwsLswTrapMib, hwDevice=hwDevice, h3cVpls=h3cVpls, h3cDar=h3cDar, h3cEpon=h3cEpon, redundancyFan=redundancyFan, products=products, dlsw=dlsw, h3cQos2=h3cQos2, h3cL2VpnPwe3=h3cL2VpnPwe3, h3cNS=h3cNS, h3cUps=h3cUps, hwNAT=hwNAT, h3cCATVTransceiver=h3cCATVTransceiver, hwBLS=hwBLS, hwCluster=hwCluster, h3cSNMPAgCpb=h3cSNMPAgCpb, lanSw=lanSw, hwLswExtInterface=hwLswExtInterface, h3cMultCDR=h3cMultCDR, hwVoiceCallActiveMIB=hwVoiceCallActiveMIB, h3cNqa=h3cNqa, h3cLI=h3cLI, h3cDhcpRelay=h3cDhcpRelay, h3cRCP=h3cRCP, h3cSurveillanceMIB=h3cSurveillanceMIB, h3cHgmp=h3cHgmp, hwVlan=hwVlan, h3cVrrpExt=h3cVrrpExt, hwVoiceAnalogInterfaceMIB=hwVoiceAnalogInterfaceMIB, h3cRaid=h3cRaid, h3cDvpn=h3cDvpn, h3cTransceiver=h3cTransceiver, h3cEntityVendorTypeOID=h3cEntityVendorTypeOID, h3cGre=h3cGre, h3cObjectInfo=h3cObjectInfo, h3cStorage=h3cStorage, h3cHPEOC=h3cHPEOC, hwHIIP=hwHIIP, hwLswMix=hwLswMix, h3cUnicast=h3cUnicast, h3cNTP=h3cNTP, hwLAG=hwLAG, hwSMAP=hwSMAP, h3cVMMan=h3cVMMan, h3cE1=h3cE1, h3cSyslog=h3cSyslog, h3cStorageSnap=h3cStorageSnap, h3cRS485=h3cRS485, hwVoiceAAAClientMIB=hwVoiceAAAClientMIB, hwLswMacPort=hwLswMacPort, hwLswArpMib=hwLswArpMib, hwIPX=hwIPX, h3cWebAuthentication=h3cWebAuthentication, h3cEvc=h3cEvc, hwAddrMgmt=hwAddrMgmt, hwMultilinkPPP=hwMultilinkPPP, vrpProtocol=vrpProtocol, huaweiDatacomm=huaweiDatacomm, pos=pos, h3cIKEMonitor=h3cIKEMonitor, h3cTunnel=h3cTunnel, h3cSiemMib=h3cSiemMib, h3cOadp=h3cOadp, h3cSubnetVlan=h3cSubnetVlan, h3cAutoDetect=h3cAutoDetect, hwCmdOverSnmpMib=hwCmdOverSnmpMib, h3cSystemMan=h3cSystemMan)

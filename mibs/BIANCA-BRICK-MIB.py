#
# PySNMP MIB module BIANCA-BRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysName", "sysDescr")
NotificationType, Unsigned32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, ObjectIdentity, IpAddress, Bits, iso, ModuleIdentity, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "Bits", "iso", "ModuleIdentity", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
admin = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 1))
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

biboAdmTrapCommunity = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTrapCommunity.setStatus('mandatory')
biboAdmSnmpVersion = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("version1", 1), ("version1-compat", 2), ("version1p1", 3), ("version1p1-compat", 4), ("version1p1-auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSnmpVersion.setStatus('mandatory')
biboAdmSnmpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSnmpPort.setStatus('mandatory')
biboAdmSnmpTrapPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSnmpTrapPort.setStatus('mandatory')
biboAdmIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmIpAddr.setStatus('mandatory')
biboAdmTrapBrdCast = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTrapBrdCast.setStatus('mandatory')
biboAdmTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 10), )
if mibBuilder.loadTexts: biboAdmTrapHostTable.setStatus('mandatory')
biboAdmTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmTrapHostAddr"))
if mibBuilder.loadTexts: biboAdmTrapHostEntry.setStatus('mandatory')
biboAdmTrapHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTrapHostAddr.setStatus('mandatory')
biboAdmTrapHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTrapHostStatus.setStatus('mandatory')
biboAdmSyslogMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSyslogMaxEntries.setStatus('mandatory')
biboAdmSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 12), )
if mibBuilder.loadTexts: biboAdmSyslogTable.setStatus('mandatory')
biboAdmSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmSyslogTimeStamp"), (0, "BIANCA-BRICK-MIB", "biboAdmSyslogLevel"))
if mibBuilder.loadTexts: biboAdmSyslogEntry.setStatus('mandatory')
biboAdmSyslogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 1), Date()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSyslogTimeStamp.setStatus('mandatory')
biboAdmSyslogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSyslogLevel.setStatus('mandatory')
biboAdmSyslogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSyslogMessage.setStatus('mandatory')
biboAdmSyslogSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("acct", 1), ("isdn", 2), ("inet", 3), ("x25", 4), ("ipx", 5), ("capi", 6), ("ppp", 7), ("bridge", 8), ("config", 9), ("snmp", 10), ("x21", 11), ("token", 12), ("ether", 13), ("radius", 14), ("tapi", 15), ("ospf", 16), ("fr", 17), ("modem", 18), ("rip", 19), ("atm", 20), ("pabx", 21), ("ipsec", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSyslogSubject.setStatus('mandatory')
biboAdmLogHostTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 13), )
if mibBuilder.loadTexts: biboAdmLogHostTable.setStatus('mandatory')
biboAdmLogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmLogHostAddr"))
if mibBuilder.loadTexts: biboAdmLogHostEntry.setStatus('mandatory')
biboAdmLogHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLogHostAddr.setStatus('mandatory')
biboAdmLogHostLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8), ("delete", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLogHostLevel.setStatus('mandatory')
biboAdmLogHostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("local0", 1), ("local1", 2), ("local2", 3), ("local3", 4), ("local4", 5), ("local5", 6), ("local6", 7), ("local7", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLogHostFacility.setStatus('mandatory')
biboAdmLogHostType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("system", 1), ("acct", 2), ("all", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLogHostType.setStatus('mandatory')
biboAdmLogHostTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("time", 2), ("all", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLogHostTimestamp.setStatus('mandatory')
biboAdmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 14), )
if mibBuilder.loadTexts: biboAdmConfigTable.setStatus('mandatory')
biboAdmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmConfigCmd"))
if mibBuilder.loadTexts: biboAdmConfigEntry.setStatus('mandatory')
biboAdmConfigDirTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 15), )
if mibBuilder.loadTexts: biboAdmConfigDirTable.setStatus('mandatory')
biboAdmConfigDirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmConfigDirName"))
if mibBuilder.loadTexts: biboAdmConfigDirEntry.setStatus('mandatory')
biboAdmConfigCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("save", 1), ("load", 2), ("put", 3), ("get", 4), ("state", 5), ("delete", 6), ("move", 7), ("copy", 8), ("reboot", 9), ("reorg", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigCmd.setStatus('mandatory')
biboAdmConfigObject = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigObject.setStatus('mandatory')
biboAdmConfigPath = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigPath.setStatus('mandatory')
biboAdmConfigPathNew = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigPathNew.setStatus('mandatory')
biboAdmConfigHost = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigHost.setStatus('mandatory')
biboAdmConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("todo", 1), ("running", 2), ("done", 3), ("error", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmConfigState.setStatus('mandatory')
biboAdmConfigFile = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConfigFile.setStatus('mandatory')
biboAdmConfigDirName = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmConfigDirName.setStatus('mandatory')
biboAdmConfigDirCount = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmConfigDirCount.setStatus('mandatory')
biboAdmConfigDirContent = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmConfigDirContent.setStatus('mandatory')
biboAdmBoardTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 17), )
if mibBuilder.loadTexts: biboAdmBoardTable.setStatus('mandatory')
biboAdmBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboABrdSlot"), (0, "BIANCA-BRICK-MIB", "biboABrdUnit"))
if mibBuilder.loadTexts: biboAdmBoardEntry.setStatus('mandatory')
biboABrdSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdSlot.setStatus('mandatory')
biboABrdType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdType.setStatus('mandatory')
biboABrdHWRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdHWRelease.setStatus('mandatory')
biboABrdFWRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdFWRelease.setStatus('mandatory')
biboABrdPartNo = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdPartNo.setStatus('mandatory')
biboABrdConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 1), ("rj45", 2), ("bnc", 3), ("subd15", 4), ("rj45-10mbit-hdup", 5), ("rj45-10mbit-fdup", 6), ("rj45-100mbit-hdup", 7), ("rj45-100mbit-fdup", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboABrdConnector.setStatus('mandatory')
biboABrdUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdUnit.setStatus('mandatory')
biboABrdSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboABrdSerialNo.setStatus('mandatory')
biboAdmUsrTrapTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 18), )
if mibBuilder.loadTexts: biboAdmUsrTrapTable.setStatus('mandatory')
biboAdmUsrTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboATrpObj"))
if mibBuilder.loadTexts: biboAdmUsrTrapEntry.setStatus('mandatory')
biboATrpObj = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1, 1), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboATrpObj.setStatus('mandatory')
biboATrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboATrpStatus.setStatus('mandatory')
biboAdmDomainName = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmDomainName.setStatus('mandatory')
biboAdmNameServer = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmNameServer.setStatus('mandatory')
biboAdmNameServ2 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmNameServ2.setStatus('mandatory')
biboAdmBridgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmBridgeEnable.setStatus('mandatory')
biboAdmCapiTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmCapiTcpPort.setStatus('mandatory')
biboAdmTraceTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTraceTcpPort.setStatus('mandatory')
biboAdmRipUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmRipUdpPort.setStatus('mandatory')
biboAdmSWVersion = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSWVersion.setStatus('mandatory')
biboAdmTimeServer = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 27), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTimeServer.setStatus('mandatory')
biboAdmTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTimeOffset.setStatus('mandatory')
biboAdmConsoleSyslog = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmConsoleSyslog.setStatus('mandatory')
biboAdmSyslogTableLevel = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSyslogTableLevel.setStatus('mandatory')
biboAdmSystemId = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmSystemId.setStatus('mandatory')
biboAdmLicInfoTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 32), )
if mibBuilder.loadTexts: biboAdmLicInfoTable.setStatus('mandatory')
biboAdmLicInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboAdmLicInfoType"), (0, "BIANCA-BRICK-MIB", "biboAdmLicInfoStatus"))
if mibBuilder.loadTexts: biboAdmLicInfoEntry.setStatus('mandatory')
biboAdmLicInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 33, 128, 129, 130, 131, 132))).clone(namedValues=NamedValues(("ip", 1), ("capi", 2), ("bridge", 3), ("x25", 4), ("ipx", 5), ("stac", 6), ("frame-relay", 7), ("tapi", 8), ("ospf", 9), ("extended-lan", 10), ("tunneling", 11), ("taf", 12), ("extended-wan", 13), ("leased-line", 14), ("ipsec", 33), ("ethernet", 128), ("bri", 129), ("g703", 130), ("pri", 131), ("modem", 132)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoType.setStatus('mandatory')
biboAdmLicInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("builtin", 1), ("valid-license", 2), ("invalid-license", 3), ("no-license", 4), ("erase-internal", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoStatus.setStatus('mandatory')
biboAdmLicInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoId.setStatus('mandatory')
biboAdmLicInfoSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoSlot.setStatus('mandatory')
biboAdmLicInfoMaxLic = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoMaxLic.setStatus('mandatory')
biboAdmLicInfoInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoInUse.setStatus('mandatory')
biboAdmLicInfoHwSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoHwSerial.setStatus('mandatory')
biboAdmLicInfoUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicInfoUnit.setStatus('mandatory')
biboAdmBootpRelayServer = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 33), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmBootpRelayServer.setStatus('mandatory')
biboAdmRadiusServer = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 34), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmRadiusServer.setStatus('mandatory')
biboAdmLocalPPPIdent = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 35), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLocalPPPIdent.setStatus('mandatory')
biboAdmHttpTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 36), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmHttpTcpPort.setStatus('mandatory')
biboAdmTapiTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 37), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTapiTcpPort.setStatus('mandatory')
biboAdmTimeProtocol = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("time-udp", 2), ("time-tcp", 3), ("time-sntp", 4), ("isdn", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTimeProtocol.setStatus('mandatory')
biboAdmTimeUpdate = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 39), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmTimeUpdate.setStatus('mandatory')
biboAdmWINS1 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 40), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmWINS1.setStatus('mandatory')
biboAdmWINS2 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 41), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmWINS2.setStatus('mandatory')
admin_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 22)).setLabel("admin-2")
biboAdmCardTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 1, 42), )
if mibBuilder.loadTexts: biboAdmCardTable.setStatus('mandatory')
biboAdmCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1), ).setIndexNames((0, "BIANCA-BRICK-MIB", "biboACrdSlot"))
if mibBuilder.loadTexts: biboAdmCardEntry.setStatus('mandatory')
biboACrdSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdSlot.setStatus('mandatory')
biboACrdType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdType.setStatus('mandatory')
biboACrdState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("running", 2), ("fail", 3), ("stopped", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboACrdState.setStatus('mandatory')
biboACrdCpldVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdCpldVersion.setStatus('mandatory')
biboACrdFpgaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdFpgaVersion.setStatus('mandatory')
biboACrdTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdTemp.setStatus('mandatory')
biboACrdTempAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboACrdTempAlarmThreshold.setStatus('mandatory')
biboACrdTempAlarmTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboACrdTempAlarmTrap.setStatus('mandatory')
biboAdmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 1, 43))
biboAdmTrapACrdTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,1)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"), ("BIANCA-BRICK-MIB", "biboACrdTempAlarmThreshold"))
biboAdmTrapACrdTempOk = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,2)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"), ("BIANCA-BRICK-MIB", "biboACrdTempAlarmThreshold"))
biboAdmTrapACrdDown = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,3)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"))
biboAdmTrapACrdRunning = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,4)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"))
biboAdmTrapACrdFailed = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,5)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"))
biboAdmTrapACrdStopped = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 1, 43) + (0,6)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("BIANCA-BRICK-MIB", "biboACrdSlot"), ("BIANCA-BRICK-MIB", "biboACrdType"), ("BIANCA-BRICK-MIB", "biboACrdState"), ("BIANCA-BRICK-MIB", "biboACrdTemp"))
biboAdmSnmpLinkTrapEvent = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("any", 2), ("up", 3), ("down", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmSnmpLinkTrapEvent.setStatus('mandatory')
extadmin = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 22, 1))
biboExtAdmMonAddress = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboExtAdmMonAddress.setStatus('mandatory')
biboExtAdmMonPort = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboExtAdmMonPort.setStatus('mandatory')
biboExtAdmMonType = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("physical", 2), ("physical-virt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboExtAdmMonType.setStatus('mandatory')
biboExtAdmMonUpdate = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboExtAdmMonUpdate.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-MIB", biboAdmLogHostType=biboAdmLogHostType, biboAdmTapiTcpPort=biboAdmTapiTcpPort, org=org, biboAdmTrapHostTable=biboAdmTrapHostTable, biboAdmConfigFile=biboAdmConfigFile, biboAdmWINS1=biboAdmWINS1, Date=Date, PhysAddress=PhysAddress, biboAdmConfigDirCount=biboAdmConfigDirCount, biboAdmConfigState=biboAdmConfigState, biboAdmConsoleSyslog=biboAdmConsoleSyslog, biboAdmLicInfoStatus=biboAdmLicInfoStatus, biboAdmConfigPath=biboAdmConfigPath, biboAdmLogHostAddr=biboAdmLogHostAddr, biboAdmLicInfoSlot=biboAdmLicInfoSlot, biboAdmSyslogTable=biboAdmSyslogTable, biboAdmLogHostTimestamp=biboAdmLogHostTimestamp, biboExtAdmMonPort=biboExtAdmMonPort, biboAdmCardTable=biboAdmCardTable, biboAdmConfigHost=biboAdmConfigHost, biboAdmTrapACrdTempOk=biboAdmTrapACrdTempOk, biboACrdTempAlarmTrap=biboACrdTempAlarmTrap, biboAdmConfigCmd=biboAdmConfigCmd, biboAdmLogHostTable=biboAdmLogHostTable, biboAdmConfigEntry=biboAdmConfigEntry, biboABrdFWRelease=biboABrdFWRelease, extadmin=extadmin, admin=admin, biboAdmLicInfoEntry=biboAdmLicInfoEntry, biboAdmRipUdpPort=biboAdmRipUdpPort, biboACrdSlot=biboACrdSlot, biboAdmCardEntry=biboAdmCardEntry, biboExtAdmMonUpdate=biboExtAdmMonUpdate, biboAdmTimeUpdate=biboAdmTimeUpdate, biboAdmLogHostEntry=biboAdmLogHostEntry, biboAdmConfigTable=biboAdmConfigTable, biboAdmWINS2=biboAdmWINS2, biboAdmTraps=biboAdmTraps, biboACrdFpgaVersion=biboACrdFpgaVersion, biboExtAdmMonAddress=biboExtAdmMonAddress, biboAdmConfigObject=biboAdmConfigObject, biboAdmIpAddr=biboAdmIpAddr, biboAdmLicInfoHwSerial=biboAdmLicInfoHwSerial, biboAdmTrapACrdFailed=biboAdmTrapACrdFailed, biboAdmSnmpVersion=biboAdmSnmpVersion, biboExtAdmMonType=biboExtAdmMonType, HexValue=HexValue, biboAdmSWVersion=biboAdmSWVersion, biboAdmCapiTcpPort=biboAdmCapiTcpPort, biboAdmConfigDirTable=biboAdmConfigDirTable, biboAdmLicInfoType=biboAdmLicInfoType, biboAdmConfigDirContent=biboAdmConfigDirContent, biboAdmRadiusServer=biboAdmRadiusServer, biboAdmSnmpPort=biboAdmSnmpPort, biboAdmLogHostFacility=biboAdmLogHostFacility, biboAdmTimeProtocol=biboAdmTimeProtocol, internet=internet, biboAdmLicInfoInUse=biboAdmLicInfoInUse, enterprises=enterprises, DisplayString=DisplayString, biboAdmNameServ2=biboAdmNameServ2, biboAdmLicInfoMaxLic=biboAdmLicInfoMaxLic, biboAdmConfigDirEntry=biboAdmConfigDirEntry, biboAdmLogHostLevel=biboAdmLogHostLevel, biboAdmUsrTrapEntry=biboAdmUsrTrapEntry, biboAdmTrapHostStatus=biboAdmTrapHostStatus, biboAdmLocalPPPIdent=biboAdmLocalPPPIdent, biboABrdSlot=biboABrdSlot, private=private, biboACrdTemp=biboACrdTemp, biboATrpStatus=biboATrpStatus, biboAdmSyslogEntry=biboAdmSyslogEntry, biboAdmDomainName=biboAdmDomainName, biboAdmTraceTcpPort=biboAdmTraceTcpPort, biboABrdUnit=biboABrdUnit, biboACrdState=biboACrdState, bintec=bintec, biboAdmSystemId=biboAdmSystemId, biboAdmSyslogSubject=biboAdmSyslogSubject, biboAdmTrapHostAddr=biboAdmTrapHostAddr, biboAdmConfigDirName=biboAdmConfigDirName, bibo=bibo, biboAdmSyslogLevel=biboAdmSyslogLevel, admin_2=admin_2, biboAdmSyslogMessage=biboAdmSyslogMessage, biboAdmTrapBrdCast=biboAdmTrapBrdCast, biboABrdConnector=biboABrdConnector, biboABrdSerialNo=biboABrdSerialNo, biboAdmLicInfoId=biboAdmLicInfoId, biboAdmTrapHostEntry=biboAdmTrapHostEntry, biboAdmSnmpLinkTrapEvent=biboAdmSnmpLinkTrapEvent, biboAdmConfigPathNew=biboAdmConfigPathNew, biboAdmSyslogMaxEntries=biboAdmSyslogMaxEntries, biboAdmHttpTcpPort=biboAdmHttpTcpPort, biboABrdHWRelease=biboABrdHWRelease, biboAdmLicInfoUnit=biboAdmLicInfoUnit, biboAdmTrapACrdDown=biboAdmTrapACrdDown, biboABrdType=biboABrdType, biboACrdType=biboACrdType, biboAdmBridgeEnable=biboAdmBridgeEnable, biboABrdPartNo=biboABrdPartNo, biboAdmSnmpTrapPort=biboAdmSnmpTrapPort, biboAdmTimeOffset=biboAdmTimeOffset, biboAdmTrapACrdStopped=biboAdmTrapACrdStopped, biboAdmTrapACrdRunning=biboAdmTrapACrdRunning, biboAdmBoardEntry=biboAdmBoardEntry, biboAdmBootpRelayServer=biboAdmBootpRelayServer, biboATrpObj=biboATrpObj, biboACrdTempAlarmThreshold=biboACrdTempAlarmThreshold, biboAdmTrapCommunity=biboAdmTrapCommunity, biboAdmBoardTable=biboAdmBoardTable, biboAdmNameServer=biboAdmNameServer, biboAdmUsrTrapTable=biboAdmUsrTrapTable, biboAdmLicInfoTable=biboAdmLicInfoTable, biboAdmSyslogTableLevel=biboAdmSyslogTableLevel, dod=dod, biboAdmTimeServer=biboAdmTimeServer, biboACrdCpldVersion=biboACrdCpldVersion, biboAdmSyslogTimeStamp=biboAdmSyslogTimeStamp, biboAdmTrapACrdTempCritical=biboAdmTrapACrdTempCritical)

#
# PySNMP MIB module DLINK-3100-BANNER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-BANNER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, NotificationType, iso, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Unsigned32, Counter64, ModuleIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "NotificationType", "iso", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter64", "ModuleIdentity", "Integer32", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rlBanner = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133))
rlBanner.setRevisions(('2007-12-16 00:00',))
if mibBuilder.loadTexts: rlBanner.setLastUpdated('200803160000Z')
if mibBuilder.loadTexts: rlBanner.setOrganization('Dlink, Inc.')
class BannerMessageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlBannerMOTD", 1), ("rlBannerLogin", 2), ("rlBannerExec", 3))

rlBannerMessageTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1), )
if mibBuilder.loadTexts: rlBannerMessageTable.setStatus('current')
rlBannerMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1), ).setIndexNames((0, "DLINK-3100-BANNER-MIB", "rlBannerMessageType"), (0, "DLINK-3100-BANNER-MIB", "rlBannerMessageIndex"))
if mibBuilder.loadTexts: rlBannerMessageEntry.setStatus('current')
rlBannerMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 1), BannerMessageType())
if mibBuilder.loadTexts: rlBannerMessageType.setStatus('current')
rlBannerMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)))
if mibBuilder.loadTexts: rlBannerMessageIndex.setStatus('current')
rlBannerMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageText.setStatus('current')
rlBannerManageTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2), )
if mibBuilder.loadTexts: rlBannerManageTable.setStatus('current')
rlBannerManageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1), ).setIndexNames((0, "DLINK-3100-BANNER-MIB", "rlBannerMessageType"))
if mibBuilder.loadTexts: rlBannerManageEntry.setStatus('current')
rlBannerManageSSH = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageSSH.setStatus('current')
rlBannerManageTelnet = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageTelnet.setStatus('current')
rlBannerManageConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageConsole.setStatus('current')
rlBannerMessageClear = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 3), BannerMessageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageClear.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-BANNER-MIB", rlBannerManageEntry=rlBannerManageEntry, rlBannerManageTelnet=rlBannerManageTelnet, rlBannerMessageTable=rlBannerMessageTable, rlBanner=rlBanner, rlBannerManageTable=rlBannerManageTable, rlBannerMessageClear=rlBannerMessageClear, rlBannerMessageText=rlBannerMessageText, rlBannerMessageIndex=rlBannerMessageIndex, rlBannerManageSSH=rlBannerManageSSH, rlBannerMessageType=rlBannerMessageType, rlBannerManageConsole=rlBannerManageConsole, rlBannerMessageEntry=rlBannerMessageEntry, BannerMessageType=BannerMessageType, PYSNMP_MODULE_ID=rlBanner)
#
# PySNMP MIB module ELTEX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, NotificationType, TimeTicks, Counter64, enterprises, iso, Unsigned32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "enterprises", "iso", "Unsigned32", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
eltex = ModuleIdentity((1, 3, 6, 1, 4, 1, 34300))
if mibBuilder.loadTexts: eltex.setLastUpdated('200906031500Z')
if mibBuilder.loadTexts: eltex.setOrganization('Eltex Co')
elHardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 34300, 1))
if mibBuilder.loadTexts: elHardware.setStatus('current')
elSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 34300, 2))
if mibBuilder.loadTexts: elSoftware.setStatus('current')
eltrapGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 34300, 3))
if mibBuilder.loadTexts: eltrapGroup.setStatus('current')
mc240AlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 3))
mc240StreamAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 1)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240StreamAlarmTrap.setStatus('current')
mc240SyncAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 2)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240SyncAlarmTrap.setStatus('current')
mc240ss7LinkAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 3)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240ss7LinkAlarmTrap.setStatus('current')
mc240ss7LinksetAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 4)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240ss7LinksetAlarmTrap.setStatus('current')
mc240FileAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 5)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240FileAlarmTrap.setStatus('current')
mc240CardAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 6)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240CardAlarmTrap.setStatus('current')
mxlDPSAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 7)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: mxlDPSAlarmTrap.setStatus('current')
mxlTELEAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 8)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: mxlTELEAlarmTrap.setStatus('current')
mc240UPSAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 9)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240UPSAlarmTrap.setStatus('current')
mc240SensAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 10)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240SensAlarmTrap.setStatus('current')
dslamLinkDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 11)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamLinkDownTrap.setStatus('current')
dslamDSRateAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 12)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamDSRateAlarmTrap.setStatus('current')
dslamUSRateAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 13)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamUSRateAlarmTrap.setStatus('current')
ponONUAuthAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 14)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponONUAuthAlarmTrap.setStatus('current')
ponEthAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 15)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponEthAlarmTrap.setStatus('current')
ponOpticalAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 16)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponOpticalAlarmTrap.setStatus('current')
dslamOverheatAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 17)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamOverheatAlarmTrap.setStatus('current')
dslamVoltageAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 18)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamVoltageAlarmTrap.setStatus('current')
dslamSessionAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 19)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamSessionAlarmTrap.setStatus('current')
dslamEthLinkAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 3, 20)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamEthLinkAlarmTrap.setStatus('current')
mc240OkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 4))
mc240StreamOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 1)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240StreamOkTrap.setStatus('current')
mc240SyncOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 2)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240SyncOkTrap.setStatus('current')
mc240ss7LinkOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 3)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240ss7LinkOkTrap.setStatus('current')
mc240ss7LinksetOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 4)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240ss7LinksetOkTrap.setStatus('current')
mc240FileOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 5)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240FileOkTrap.setStatus('current')
mc240CardOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 6)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240CardOkTrap.setStatus('current')
mxlDPSOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 7)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: mxlDPSOkTrap.setStatus('current')
mxlTELEOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 8)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: mxlTELEOkTrap.setStatus('current')
mc240UPSOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 9)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240UPSOkTrap.setStatus('current')
mc240SensOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 10)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if mibBuilder.loadTexts: mc240SensOkTrap.setStatus('current')
dslamLinkUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 11)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamLinkUpTrap.setStatus('current')
dslamDSRateOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 12)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamDSRateOkTrap.setStatus('current')
dslamUSRateOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 13)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamUSRateOkTrap.setStatus('current')
ponONUAuthOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 14)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponONUAuthOkTrap.setStatus('current')
ponEthOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 15)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponEthOkTrap.setStatus('current')
ponOpticalOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 16)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: ponOpticalOkTrap.setStatus('current')
dslamOverheatOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 17)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamOverheatOkTrap.setStatus('current')
dslamVoltageOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 18)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamVoltageOkTrap.setStatus('current')
dslamSessionOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 19)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamSessionOkTrap.setStatus('current')
dslamEthLinkOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 4, 20)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: dslamEthLinkOkTrap.setStatus('current')
mc240TrapTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 5))
mcTrapExState = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapExState.setStatus('current')
mcTrapLParam1 = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapLParam1.setStatus('current')
mcTrapLParam2 = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapLParam2.setStatus('current')
mcTrapLParam3 = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapLParam3.setStatus('current')
mcTrapID = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapID.setStatus('current')
mcTrapDescr = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapDescr.setStatus('current')
mcTrapRestoredAlarmID = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapRestoredAlarmID.setStatus('current')
mcTrapSyncType = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcTrapSyncType.setStatus('current')
mcReservedFlag = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcReservedFlag.setStatus('current')
omsOperationAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 20))
omsOperationOkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 21))
omsOperationCommandAlarm = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 20, 1)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: omsOperationCommandAlarm.setStatus('current')
omsOperationCommandOk = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 21, 1)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: omsOperationCommandOk.setStatus('current')
mp800mkAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 8))
mp800mkMPStatusAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 1)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkMPStatusAlarmTrap.setStatus('current')
mp800mkInpParmAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 2)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkInpParmAlarmTrap.setStatus('current')
mp800mkUEPConfAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 3)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkUEPConfAlarmTrap.setStatus('current')
mp800mkTMAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 4)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkTMAlarmTrap.setStatus('current')
mp800mkACVMAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 5)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkACVMAlarmTrap.setStatus('current')
mp800mkIbatMAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 6)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIbatMAlarmTrap.setStatus('current')
mp800mkVbatMAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 7)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkVbatMAlarmTrap.setStatus('current')
mp800mkVbatChAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 8)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkVbatChAlarmTrap.setStatus('current')
mp800mkRlsDevAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 9)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkRlsDevAlarmTrap.setStatus('current')
mp800mkDVcellAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 10)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkDVcellAlarmTrap.setStatus('current')
mp800mkACVAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 11)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkACVAlarmTrap.setStatus('current')
mp800mkBatChargeAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 12)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkBatChargeAlarmTrap.setStatus('current')
mp800mkIloadAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 13)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIloadAlarmTrap.setStatus('current')
mp800mkIbatChAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 14)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIbatChAlarmTrap.setStatus('current')
mp800mkSuppAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 15)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkSuppAlarmTrap.setStatus('current')
mp800mkBatConnAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 8, 16)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkBatConnAlarmTrap.setStatus('current')
mp800mkOkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 9))
mp800mkMPStatusOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 1)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkMPStatusOkTrap.setStatus('current')
mp800mkInpParmOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 2)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkInpParmOkTrap.setStatus('current')
mp800mkUEPConfOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 3)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkUEPConfOkTrap.setStatus('current')
mp800mkTMOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 4)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkTMOkTrap.setStatus('current')
mp800mkACVMOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 5)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkACVMOkTrap.setStatus('current')
mp800mkIbatMOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 6)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIbatMOkTrap.setStatus('current')
mp800mkVbatMOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 7)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkVbatMOkTrap.setStatus('current')
mp800mkVbatChOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 8)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkVbatChOkTrap.setStatus('current')
mp800mkRlsDevOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 9)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkRlsDevOkTrap.setStatus('current')
mp800mkDVcellOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 10)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkDVcellOkTrap.setStatus('current')
mp800mkACVOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 11)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkACVOkTrap.setStatus('current')
mp800mkBatChargeOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 12)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkBatChargeOkTrap.setStatus('current')
mp800mkIloadOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 13)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIloadOkTrap.setStatus('current')
mp800mkIbatChOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 14)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkIbatChOkTrap.setStatus('current')
mp800mkSuppOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 15)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkSuppOkTrap.setStatus('current')
mp800mkBatConnOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 34300, 3, 9, 16)).setObjects(("ELTEX-SMI", "mp800mkTrapParameter"), ("ELTEX-SMI", "mp800mkTrapValue"), ("ELTEX-SMI", "mp800mkTrapComment"))
if mibBuilder.loadTexts: mp800mkBatConnOkTrap.setStatus('current')
mp800mkTrapTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 34300, 3, 10))
mp800mkTrapParameter = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mp800mkTrapParameter.setStatus('current')
mp800mkTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 10, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mp800mkTrapValue.setStatus('current')
mp800mkTrapComment = MibScalar((1, 3, 6, 1, 4, 1, 34300, 3, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mp800mkTrapComment.setStatus('current')
eltrapNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 34300, 3, 100)).setObjects(("ELTEX-SMI", "mc240StreamAlarmTrap"), ("ELTEX-SMI", "mc240SyncAlarmTrap"), ("ELTEX-SMI", "mc240ss7LinkAlarmTrap"), ("ELTEX-SMI", "mc240ss7LinksetAlarmTrap"), ("ELTEX-SMI", "mc240FileAlarmTrap"), ("ELTEX-SMI", "mc240CardAlarmTrap"), ("ELTEX-SMI", "mxlDPSAlarmTrap"), ("ELTEX-SMI", "mxlTELEAlarmTrap"), ("ELTEX-SMI", "mc240UPSAlarmTrap"), ("ELTEX-SMI", "mc240SensAlarmTrap"), ("ELTEX-SMI", "dslamLinkDownTrap"), ("ELTEX-SMI", "dslamDSRateAlarmTrap"), ("ELTEX-SMI", "dslamUSRateAlarmTrap"), ("ELTEX-SMI", "ponONUAuthAlarmTrap"), ("ELTEX-SMI", "ponEthAlarmTrap"), ("ELTEX-SMI", "ponOpticalAlarmTrap"), ("ELTEX-SMI", "mc240StreamOkTrap"), ("ELTEX-SMI", "mc240SyncOkTrap"), ("ELTEX-SMI", "mc240ss7LinkOkTrap"), ("ELTEX-SMI", "mc240ss7LinksetOkTrap"), ("ELTEX-SMI", "mc240FileOkTrap"), ("ELTEX-SMI", "mc240CardOkTrap"), ("ELTEX-SMI", "mxlDPSOkTrap"), ("ELTEX-SMI", "mxlTELEOkTrap"), ("ELTEX-SMI", "mc240UPSOkTrap"), ("ELTEX-SMI", "mc240SensOkTrap"), ("ELTEX-SMI", "dslamLinkUpTrap"), ("ELTEX-SMI", "dslamDSRateOkTrap"), ("ELTEX-SMI", "dslamUSRateOkTrap"), ("ELTEX-SMI", "ponONUAuthOkTrap"), ("ELTEX-SMI", "ponEthOkTrap"), ("ELTEX-SMI", "ponOpticalOkTrap"), ("ELTEX-SMI", "dslamOverheatAlarmTrap"), ("ELTEX-SMI", "dslamVoltageAlarmTrap"), ("ELTEX-SMI", "dslamSessionAlarmTrap"), ("ELTEX-SMI", "dslamEthLinkAlarmTrap"), ("ELTEX-SMI", "dslamOverheatOkTrap"), ("ELTEX-SMI", "dslamVoltageOkTrap"), ("ELTEX-SMI", "dslamSessionOkTrap"), ("ELTEX-SMI", "dslamEthLinkOkTrap"), ("ELTEX-SMI", "mp800mkMPStatusAlarmTrap"), ("ELTEX-SMI", "mp800mkInpParmAlarmTrap"), ("ELTEX-SMI", "mp800mkUEPConfAlarmTrap"), ("ELTEX-SMI", "mp800mkTMAlarmTrap"), ("ELTEX-SMI", "mp800mkACVMAlarmTrap"), ("ELTEX-SMI", "mp800mkIbatMAlarmTrap"), ("ELTEX-SMI", "mp800mkVbatMAlarmTrap"), ("ELTEX-SMI", "mp800mkVbatChAlarmTrap"), ("ELTEX-SMI", "mp800mkRlsDevAlarmTrap"), ("ELTEX-SMI", "mp800mkDVcellAlarmTrap"), ("ELTEX-SMI", "mp800mkACVAlarmTrap"), ("ELTEX-SMI", "mp800mkBatChargeAlarmTrap"), ("ELTEX-SMI", "mp800mkIloadAlarmTrap"), ("ELTEX-SMI", "mp800mkIbatChAlarmTrap"), ("ELTEX-SMI", "mp800mkSuppAlarmTrap"), ("ELTEX-SMI", "mp800mkBatConnAlarmTrap"), ("ELTEX-SMI", "mp800mkMPStatusOkTrap"), ("ELTEX-SMI", "mp800mkInpParmOkTrap"), ("ELTEX-SMI", "mp800mkUEPConfOkTrap"), ("ELTEX-SMI", "mp800mkTMOkTrap"), ("ELTEX-SMI", "mp800mkACVMOkTrap"), ("ELTEX-SMI", "mp800mkIbatMOkTrap"), ("ELTEX-SMI", "mp800mkVbatMOkTrap"), ("ELTEX-SMI", "mp800mkVbatChOkTrap"), ("ELTEX-SMI", "mp800mkRlsDevOkTrap"), ("ELTEX-SMI", "mp800mkDVcellOkTrap"), ("ELTEX-SMI", "mp800mkACVOkTrap"), ("ELTEX-SMI", "mp800mkBatChargeOkTrap"), ("ELTEX-SMI", "mp800mkIloadOkTrap"), ("ELTEX-SMI", "mp800mkIbatChOkTrap"), ("ELTEX-SMI", "mp800mkSuppOkTrap"), ("ELTEX-SMI", "mp800mkBatConnOkTrap"), ("ELTEX-SMI", "omsOperationCommandAlarm"), ("ELTEX-SMI", "omsOperationCommandOk"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eltrapNotificationGroup = eltrapNotificationGroup.setStatus('current')
eltrapObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 34300, 3, 101)).setObjects(("ELTEX-SMI", "mcTrapExState"), ("ELTEX-SMI", "mcTrapLParam1"), ("ELTEX-SMI", "mcTrapLParam2"), ("ELTEX-SMI", "mcTrapLParam3"), ("ELTEX-SMI", "mcTrapID"), ("ELTEX-SMI", "mcTrapDescr"), ("ELTEX-SMI", "mcTrapRestoredAlarmID"), ("ELTEX-SMI", "mcTrapSyncType"), ("ELTEX-SMI", "mcReservedFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eltrapObjectGroup = eltrapObjectGroup.setStatus('current')
mibBuilder.exportSymbols("ELTEX-SMI", elSoftware=elSoftware, dslamVoltageAlarmTrap=dslamVoltageAlarmTrap, mp800mkInpParmOkTrap=mp800mkInpParmOkTrap, eltrapGroup=eltrapGroup, mp800mkBatChargeAlarmTrap=mp800mkBatChargeAlarmTrap, mc240CardOkTrap=mc240CardOkTrap, omsOperationCommandOk=omsOperationCommandOk, mcTrapRestoredAlarmID=mcTrapRestoredAlarmID, mc240UPSOkTrap=mc240UPSOkTrap, dslamSessionOkTrap=dslamSessionOkTrap, dslamSessionAlarmTrap=dslamSessionAlarmTrap, mp800mkTrapParameter=mp800mkTrapParameter, dslamOverheatOkTrap=dslamOverheatOkTrap, mp800mkACVOkTrap=mp800mkACVOkTrap, ponONUAuthAlarmTrap=ponONUAuthAlarmTrap, mp800mkDVcellOkTrap=mp800mkDVcellOkTrap, mcTrapDescr=mcTrapDescr, mp800mkVbatChOkTrap=mp800mkVbatChOkTrap, mc240FileAlarmTrap=mc240FileAlarmTrap, mxlDPSOkTrap=mxlDPSOkTrap, mc240ss7LinksetAlarmTrap=mc240ss7LinksetAlarmTrap, mp800mkDVcellAlarmTrap=mp800mkDVcellAlarmTrap, mp800mkVbatChAlarmTrap=mp800mkVbatChAlarmTrap, mp800mkTMOkTrap=mp800mkTMOkTrap, PYSNMP_MODULE_ID=eltex, mcTrapSyncType=mcTrapSyncType, dslamEthLinkAlarmTrap=dslamEthLinkAlarmTrap, mc240ss7LinksetOkTrap=mc240ss7LinksetOkTrap, mp800mkMPStatusAlarmTrap=mp800mkMPStatusAlarmTrap, dslamUSRateAlarmTrap=dslamUSRateAlarmTrap, mc240ss7LinkAlarmTrap=mc240ss7LinkAlarmTrap, mp800mkUEPConfAlarmTrap=mp800mkUEPConfAlarmTrap, ponONUAuthOkTrap=ponONUAuthOkTrap, mp800mkBatConnAlarmTrap=mp800mkBatConnAlarmTrap, mp800mkTrapTypes=mp800mkTrapTypes, mcTrapExState=mcTrapExState, mp800mkIbatMAlarmTrap=mp800mkIbatMAlarmTrap, mp800mkOkTraps=mp800mkOkTraps, mp800mkInpParmAlarmTrap=mp800mkInpParmAlarmTrap, mp800mkIbatChAlarmTrap=mp800mkIbatChAlarmTrap, mp800mkRlsDevAlarmTrap=mp800mkRlsDevAlarmTrap, mc240CardAlarmTrap=mc240CardAlarmTrap, mc240StreamOkTrap=mc240StreamOkTrap, mc240UPSAlarmTrap=mc240UPSAlarmTrap, mc240SensOkTrap=mc240SensOkTrap, mxlTELEAlarmTrap=mxlTELEAlarmTrap, mxlDPSAlarmTrap=mxlDPSAlarmTrap, ponEthAlarmTrap=ponEthAlarmTrap, mp800mkAlarmTraps=mp800mkAlarmTraps, ponOpticalOkTrap=ponOpticalOkTrap, ponEthOkTrap=ponEthOkTrap, mp800mkTrapComment=mp800mkTrapComment, mc240SyncAlarmTrap=mc240SyncAlarmTrap, mc240SyncOkTrap=mc240SyncOkTrap, dslamLinkDownTrap=dslamLinkDownTrap, mp800mkIloadOkTrap=mp800mkIloadOkTrap, mp800mkVbatMAlarmTrap=mp800mkVbatMAlarmTrap, dslamDSRateAlarmTrap=dslamDSRateAlarmTrap, mc240TrapTypes=mc240TrapTypes, mc240AlarmTraps=mc240AlarmTraps, mp800mkACVMAlarmTrap=mp800mkACVMAlarmTrap, mp800mkSuppAlarmTrap=mp800mkSuppAlarmTrap, mc240SensAlarmTrap=mc240SensAlarmTrap, dslamUSRateOkTrap=dslamUSRateOkTrap, mc240ss7LinkOkTrap=mc240ss7LinkOkTrap, mp800mkSuppOkTrap=mp800mkSuppOkTrap, mp800mkMPStatusOkTrap=mp800mkMPStatusOkTrap, mc240StreamAlarmTrap=mc240StreamAlarmTrap, dslamLinkUpTrap=dslamLinkUpTrap, eltrapObjectGroup=eltrapObjectGroup, mcTrapLParam2=mcTrapLParam2, mp800mkBatChargeOkTrap=mp800mkBatChargeOkTrap, eltex=eltex, mp800mkTMAlarmTrap=mp800mkTMAlarmTrap, omsOperationOkTraps=omsOperationOkTraps, mc240FileOkTrap=mc240FileOkTrap, omsOperationCommandAlarm=omsOperationCommandAlarm, mcTrapLParam3=mcTrapLParam3, mp800mkUEPConfOkTrap=mp800mkUEPConfOkTrap, mp800mkIbatChOkTrap=mp800mkIbatChOkTrap, ponOpticalAlarmTrap=ponOpticalAlarmTrap, mcReservedFlag=mcReservedFlag, mxlTELEOkTrap=mxlTELEOkTrap, mp800mkIloadAlarmTrap=mp800mkIloadAlarmTrap, omsOperationAlarmTraps=omsOperationAlarmTraps, elHardware=elHardware, dslamVoltageOkTrap=dslamVoltageOkTrap, mp800mkBatConnOkTrap=mp800mkBatConnOkTrap, mp800mkTrapValue=mp800mkTrapValue, mcTrapLParam1=mcTrapLParam1, dslamDSRateOkTrap=dslamDSRateOkTrap, mcTrapID=mcTrapID, eltrapNotificationGroup=eltrapNotificationGroup, mp800mkACVMOkTrap=mp800mkACVMOkTrap, mc240OkTraps=mc240OkTraps, mp800mkVbatMOkTrap=mp800mkVbatMOkTrap, mp800mkACVAlarmTrap=mp800mkACVAlarmTrap, dslamOverheatAlarmTrap=dslamOverheatAlarmTrap, mp800mkIbatMOkTrap=mp800mkIbatMOkTrap, mp800mkRlsDevOkTrap=mp800mkRlsDevOkTrap, dslamEthLinkOkTrap=dslamEthLinkOkTrap)

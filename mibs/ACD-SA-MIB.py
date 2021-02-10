#
# PySNMP MIB module ACD-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACD-SA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Bits, ObjectIdentity, Counter32, iso, Integer32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Bits", "ObjectIdentity", "Counter32", "iso", "Integer32", "Counter64", "IpAddress")
TextualConvention, DisplayString, DateAndTime, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime", "RowStatus")
acdSa = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 12))
acdSa.setRevisions(('2011-12-21 01:00', '2011-03-15 01:00',))
if mibBuilder.loadTexts: acdSa.setLastUpdated('201112210100Z')
if mibBuilder.loadTexts: acdSa.setOrganization('Accedian Networks, Inc.')
acdSaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 0))
acdSaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1))
acdSaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2))
acdSaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1))
acdSaCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2))
acdSaStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3))
class AcdSaMetricType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("metricPaaPlr", 1), ("metricPaaOwDelay", 2), ("metricPaaOwDv", 3), ("metricPaaTwDelay", 4), ("metricPaaTwDv", 5), ("metricCfmPlr", 6), ("metricCfmOwDelay", 7), ("metricCfmOwDv", 8), ("metricCfmTwDelay", 9), ("metricCfmTwDv", 10), ("metricCfmSlmNearEndPlr", 11), ("metricCfmSlmFarEndPlr", 12))

class AcdSaValidFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valid", 1), ("adjusted", 2), ("pending", 3))

class AcdSaAdminStateFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class AcdSaOperStateFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("is", 1), ("oos", 2), ("oosAu", 3))

acdSaServiceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1), )
if mibBuilder.loadTexts: acdSaServiceConfigTable.setStatus('current')
acdSaServiceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"))
if mibBuilder.loadTexts: acdSaServiceConfigEntry.setStatus('current')
acdSaServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSaServiceIndex.setStatus('current')
acdSaServiceConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSaServiceConfigRowStatus.setStatus('current')
acdSaServiceConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSaServiceConfigName.setStatus('current')
acdSaServiceConfigAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 4), AcdSaAdminStateFlag().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaServiceConfigAdminState.setStatus('current')
acdSaServiceConfigReportingPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaServiceConfigReportingPeriod.setStatus('current')
acdSaServiceConfigUaWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaServiceConfigUaWindowSize.setStatus('current')
acdSaServiceConfigHliWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 999)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaServiceConfigHliWindowSize.setStatus('current')
acdSaServiceConfigTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaServiceConfigTimeInterval.setStatus('current')
acdSaMetricConfigTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2), )
if mibBuilder.loadTexts: acdSaMetricConfigTable.setStatus('current')
acdSaMetricConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"), (0, "ACD-SA-MIB", "acdSaMetricIndex"))
if mibBuilder.loadTexts: acdSaMetricConfigEntry.setStatus('current')
acdSaMetricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSaMetricIndex.setStatus('current')
acdSaMetricConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSaMetricConfigRowStatus.setStatus('current')
acdSaMetricConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSaMetricConfigName.setStatus('current')
acdSaMetricConfigSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSaMetricConfigSrcName.setStatus('current')
acdSaMetricConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 5), AcdSaMetricType().clone('metricCfmTwDelay')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaMetricConfigType.setStatus('current')
acdSaMetricConfigThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSaMetricConfigThreshold.setStatus('current')
acdSaServiceCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1), )
if mibBuilder.loadTexts: acdSaServiceCounterTable.setStatus('current')
acdSaServiceCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"))
if mibBuilder.loadTexts: acdSaServiceCounterEntry.setStatus('current')
acdSaServiceCounterPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterPeriodIndex.setStatus('current')
acdSaServiceCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 2), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterValidFlag.setStatus('current')
acdSaServiceCounterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterUpTime.setStatus('current')
acdSaServiceCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterUaTime.setStatus('current')
acdSaServiceCounterMaintTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterMaintTime.setStatus('current')
acdSaServiceCounterAvailRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterAvailRatio.setStatus('current')
acdSaServiceCounterGaps = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterGaps.setStatus('current')
acdSaServiceCounterLargestGap = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterLargestGap.setStatus('current')
acdSaServiceCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterChliTime.setStatus('current')
acdSaServiceCounterChliRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceCounterChliRatio.setStatus('current')
acdSaServiceHistCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2), )
if mibBuilder.loadTexts: acdSaServiceHistCounterTable.setStatus('current')
acdSaServiceHistCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"), (0, "ACD-SA-MIB", "acdSaServiceHistCounterPeriodIndex"))
if mibBuilder.loadTexts: acdSaServiceHistCounterEntry.setStatus('current')
acdSaServiceHistCounterPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSaServiceHistCounterPeriodIndex.setStatus('current')
acdSaServiceHistCounterIntervalEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterIntervalEnd.setStatus('current')
acdSaServiceHistCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 3), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterValidFlag.setStatus('current')
acdSaServiceHistCounterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterUpTime.setStatus('current')
acdSaServiceHistCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterUaTime.setStatus('current')
acdSaServiceHistCounterMaintTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterMaintTime.setStatus('current')
acdSaServiceHistCounterAvailRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterAvailRatio.setStatus('current')
acdSaServiceHistCounterGaps = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterGaps.setStatus('current')
acdSaServiceHistCounterLargestGap = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterLargestGap.setStatus('current')
acdSaServiceHistCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterChliTime.setStatus('current')
acdSaServiceHistCounterChliRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceHistCounterChliRatio.setStatus('current')
acdSaServiceMonoCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3), )
if mibBuilder.loadTexts: acdSaServiceMonoCounterTable.setStatus('current')
acdSaServiceMonoCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"))
if mibBuilder.loadTexts: acdSaServiceMonoCounterEntry.setStatus('current')
acdSaServiceMonoCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 1), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterValidFlag.setStatus('current')
acdSaServiceMonoCounterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterUpTime.setStatus('current')
acdSaServiceMonoCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterUaTime.setStatus('current')
acdSaServiceMonoCounterMaintTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterMaintTime.setStatus('current')
acdSaServiceMonoCounterAvailRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterAvailRatio.setStatus('current')
acdSaServiceMonoCounterGaps = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterGaps.setStatus('current')
acdSaServiceMonoCounterLargestGap = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterLargestGap.setStatus('current')
acdSaServiceMonoCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterChliTime.setStatus('current')
acdSaServiceMonoCounterChliRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceMonoCounterChliRatio.setStatus('current')
acdSaMetricCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4), )
if mibBuilder.loadTexts: acdSaMetricCounterTable.setStatus('current')
acdSaMetricCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"), (0, "ACD-SA-MIB", "acdSaMetricIndex"))
if mibBuilder.loadTexts: acdSaMetricCounterEntry.setStatus('current')
acdSaMetricCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 1), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricCounterValidFlag.setStatus('current')
acdSaMetricCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricCounterUaTime.setStatus('current')
acdSaMetricCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricCounterChliTime.setStatus('current')
acdSaMetricHistCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5), )
if mibBuilder.loadTexts: acdSaMetricHistCounterTable.setStatus('current')
acdSaMetricHistCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaMetricHistCounterID"), (0, "ACD-SA-MIB", "acdSaMetricHistCounterPeriodIndex"))
if mibBuilder.loadTexts: acdSaMetricHistCounterEntry.setStatus('current')
acdSaMetricHistCounterID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSaMetricHistCounterID.setStatus('current')
acdSaMetricHistCounterPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 2), Unsigned32())
if mibBuilder.loadTexts: acdSaMetricHistCounterPeriodIndex.setStatus('current')
acdSaMetricHistCounterIntervalEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricHistCounterIntervalEnd.setStatus('current')
acdSaMetricHistCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 4), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricHistCounterValidFlag.setStatus('current')
acdSaMetricHistCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricHistCounterUaTime.setStatus('current')
acdSaMetricHistCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricHistCounterChliTime.setStatus('current')
acdSaMetricMonoCounterTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6), )
if mibBuilder.loadTexts: acdSaMetricMonoCounterTable.setStatus('current')
acdSaMetricMonoCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceIndex"), (0, "ACD-SA-MIB", "acdSaMetricIndex"))
if mibBuilder.loadTexts: acdSaMetricMonoCounterEntry.setStatus('current')
acdSaMetricMonoCounterValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 1), AcdSaValidFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricMonoCounterValidFlag.setStatus('current')
acdSaMetricMonoCounterUaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricMonoCounterUaTime.setStatus('current')
acdSaMetricMonoCounterChliTime = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaMetricMonoCounterChliTime.setStatus('current')
acdSaServiceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1), )
if mibBuilder.loadTexts: acdSaServiceStatusTable.setStatus('current')
acdSaServiceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1), ).setIndexNames((0, "ACD-SA-MIB", "acdSaServiceStatusID"))
if mibBuilder.loadTexts: acdSaServiceStatusEntry.setStatus('current')
acdSaServiceStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSaServiceStatusID.setStatus('current')
acdSaServiceStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceStatusName.setStatus('current')
acdSaServiceStatusAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 3), AcdSaAdminStateFlag().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceStatusAdminState.setStatus('current')
acdSaServiceStatusOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 4), AcdSaOperStateFlag().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceStatusOperState.setStatus('current')
acdSaServiceStatusNbrMetrics = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSaServiceStatusNbrMetrics.setStatus('current')
acdSaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 1))
acdSaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2))
acdSaServiceConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 1)).setObjects(("ACD-SA-MIB", "acdSaServiceConfigRowStatus"), ("ACD-SA-MIB", "acdSaServiceConfigName"), ("ACD-SA-MIB", "acdSaServiceConfigAdminState"), ("ACD-SA-MIB", "acdSaServiceConfigReportingPeriod"), ("ACD-SA-MIB", "acdSaServiceConfigUaWindowSize"), ("ACD-SA-MIB", "acdSaServiceConfigHliWindowSize"), ("ACD-SA-MIB", "acdSaServiceConfigTimeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaServiceConfigGroup = acdSaServiceConfigGroup.setStatus('current')
acdSaMetricConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 2)).setObjects(("ACD-SA-MIB", "acdSaMetricConfigRowStatus"), ("ACD-SA-MIB", "acdSaMetricConfigName"), ("ACD-SA-MIB", "acdSaMetricConfigSrcName"), ("ACD-SA-MIB", "acdSaMetricConfigType"), ("ACD-SA-MIB", "acdSaMetricConfigThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaMetricConfigGroup = acdSaMetricConfigGroup.setStatus('current')
acdSaServiceCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 3)).setObjects(("ACD-SA-MIB", "acdSaServiceCounterPeriodIndex"), ("ACD-SA-MIB", "acdSaServiceCounterValidFlag"), ("ACD-SA-MIB", "acdSaServiceCounterUpTime"), ("ACD-SA-MIB", "acdSaServiceCounterUaTime"), ("ACD-SA-MIB", "acdSaServiceCounterMaintTime"), ("ACD-SA-MIB", "acdSaServiceCounterAvailRatio"), ("ACD-SA-MIB", "acdSaServiceCounterGaps"), ("ACD-SA-MIB", "acdSaServiceCounterLargestGap"), ("ACD-SA-MIB", "acdSaServiceCounterChliTime"), ("ACD-SA-MIB", "acdSaServiceCounterChliRatio"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaServiceCounterGroup = acdSaServiceCounterGroup.setStatus('current')
acdSaServiceHistCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 4)).setObjects(("ACD-SA-MIB", "acdSaServiceHistCounterIntervalEnd"), ("ACD-SA-MIB", "acdSaServiceHistCounterValidFlag"), ("ACD-SA-MIB", "acdSaServiceHistCounterUpTime"), ("ACD-SA-MIB", "acdSaServiceHistCounterUaTime"), ("ACD-SA-MIB", "acdSaServiceHistCounterMaintTime"), ("ACD-SA-MIB", "acdSaServiceHistCounterAvailRatio"), ("ACD-SA-MIB", "acdSaServiceHistCounterGaps"), ("ACD-SA-MIB", "acdSaServiceHistCounterLargestGap"), ("ACD-SA-MIB", "acdSaServiceHistCounterChliTime"), ("ACD-SA-MIB", "acdSaServiceHistCounterChliRatio"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaServiceHistCounterGroup = acdSaServiceHistCounterGroup.setStatus('current')
acdSaServiceMonoCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 5)).setObjects(("ACD-SA-MIB", "acdSaServiceMonoCounterValidFlag"), ("ACD-SA-MIB", "acdSaServiceMonoCounterUpTime"), ("ACD-SA-MIB", "acdSaServiceMonoCounterUaTime"), ("ACD-SA-MIB", "acdSaServiceMonoCounterMaintTime"), ("ACD-SA-MIB", "acdSaServiceMonoCounterAvailRatio"), ("ACD-SA-MIB", "acdSaServiceMonoCounterGaps"), ("ACD-SA-MIB", "acdSaServiceMonoCounterLargestGap"), ("ACD-SA-MIB", "acdSaServiceMonoCounterChliTime"), ("ACD-SA-MIB", "acdSaServiceMonoCounterChliRatio"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaServiceMonoCounterGroup = acdSaServiceMonoCounterGroup.setStatus('current')
acdSaMetricCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 6)).setObjects(("ACD-SA-MIB", "acdSaMetricCounterValidFlag"), ("ACD-SA-MIB", "acdSaMetricCounterUaTime"), ("ACD-SA-MIB", "acdSaMetricCounterChliTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaMetricCounterGroup = acdSaMetricCounterGroup.setStatus('current')
acdSaMetricHistCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 7)).setObjects(("ACD-SA-MIB", "acdSaMetricHistCounterIntervalEnd"), ("ACD-SA-MIB", "acdSaMetricHistCounterValidFlag"), ("ACD-SA-MIB", "acdSaMetricHistCounterUaTime"), ("ACD-SA-MIB", "acdSaMetricHistCounterChliTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaMetricHistCounterGroup = acdSaMetricHistCounterGroup.setStatus('current')
acdSaMetricMonoCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 8)).setObjects(("ACD-SA-MIB", "acdSaMetricMonoCounterValidFlag"), ("ACD-SA-MIB", "acdSaMetricMonoCounterUaTime"), ("ACD-SA-MIB", "acdSaMetricMonoCounterChliTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaMetricMonoCounterGroup = acdSaMetricMonoCounterGroup.setStatus('current')
acdSaServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 9)).setObjects(("ACD-SA-MIB", "acdSaServiceStatusName"), ("ACD-SA-MIB", "acdSaServiceStatusAdminState"), ("ACD-SA-MIB", "acdSaServiceStatusOperState"), ("ACD-SA-MIB", "acdSaServiceStatusNbrMetrics"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaServiceStatusGroup = acdSaServiceStatusGroup.setStatus('current')
acdSaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 1, 1)).setObjects(("ACD-SA-MIB", "acdSaServiceConfigGroup"), ("ACD-SA-MIB", "acdSaMetricConfigGroup"), ("ACD-SA-MIB", "acdSaServiceCounterGroup"), ("ACD-SA-MIB", "acdSaServiceHistCounterGroup"), ("ACD-SA-MIB", "acdSaServiceMonoCounterGroup"), ("ACD-SA-MIB", "acdSaMetricCounterGroup"), ("ACD-SA-MIB", "acdSaMetricHistCounterGroup"), ("ACD-SA-MIB", "acdSaMetricMonoCounterGroup"), ("ACD-SA-MIB", "acdSaServiceStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSaCompliance = acdSaCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-SA-MIB", acdSaMetricHistCounterChliTime=acdSaMetricHistCounterChliTime, acdSaServiceHistCounterMaintTime=acdSaServiceHistCounterMaintTime, acdSaMetricConfigRowStatus=acdSaMetricConfigRowStatus, acdSaMetricMonoCounterChliTime=acdSaMetricMonoCounterChliTime, acdSaMetricHistCounterPeriodIndex=acdSaMetricHistCounterPeriodIndex, acdSaServiceCounterEntry=acdSaServiceCounterEntry, acdSaCounter=acdSaCounter, acdSaServiceConfigUaWindowSize=acdSaServiceConfigUaWindowSize, acdSaServiceMonoCounterTable=acdSaServiceMonoCounterTable, acdSaServiceCounterTable=acdSaServiceCounterTable, acdSaServiceHistCounterUpTime=acdSaServiceHistCounterUpTime, acdSaMetricCounterUaTime=acdSaMetricCounterUaTime, acdSaMetricHistCounterUaTime=acdSaMetricHistCounterUaTime, acdSaMetricHistCounterGroup=acdSaMetricHistCounterGroup, acdSaServiceConfigTable=acdSaServiceConfigTable, acdSaServiceConfigReportingPeriod=acdSaServiceConfigReportingPeriod, acdSaServiceMonoCounterAvailRatio=acdSaServiceMonoCounterAvailRatio, acdSaMetricCounterValidFlag=acdSaMetricCounterValidFlag, acdSaMetricCounterGroup=acdSaMetricCounterGroup, acdSaCompliances=acdSaCompliances, acdSaServiceHistCounterTable=acdSaServiceHistCounterTable, acdSaServiceStatusTable=acdSaServiceStatusTable, acdSaMetricHistCounterEntry=acdSaMetricHistCounterEntry, acdSaServiceConfigTimeInterval=acdSaServiceConfigTimeInterval, acdSaServiceCounterUaTime=acdSaServiceCounterUaTime, acdSaServiceMonoCounterChliRatio=acdSaServiceMonoCounterChliRatio, acdSaMetricConfigType=acdSaMetricConfigType, acdSaServiceHistCounterChliRatio=acdSaServiceHistCounterChliRatio, acdSaMetricCounterTable=acdSaMetricCounterTable, acdSaMetricMonoCounterUaTime=acdSaMetricMonoCounterUaTime, acdSaServiceMonoCounterValidFlag=acdSaServiceMonoCounterValidFlag, acdSaServiceMonoCounterMaintTime=acdSaServiceMonoCounterMaintTime, acdSaMetricMonoCounterGroup=acdSaMetricMonoCounterGroup, acdSaMetricHistCounterID=acdSaMetricHistCounterID, AcdSaAdminStateFlag=AcdSaAdminStateFlag, acdSaMetricConfigTable=acdSaMetricConfigTable, acdSaServiceMonoCounterUpTime=acdSaServiceMonoCounterUpTime, acdSaServiceStatusAdminState=acdSaServiceStatusAdminState, acdSa=acdSa, acdSaServiceStatusOperState=acdSaServiceStatusOperState, AcdSaMetricType=AcdSaMetricType, acdSaServiceCounterAvailRatio=acdSaServiceCounterAvailRatio, AcdSaValidFlag=AcdSaValidFlag, acdSaStatus=acdSaStatus, acdSaServiceHistCounterGroup=acdSaServiceHistCounterGroup, acdSaServiceCounterMaintTime=acdSaServiceCounterMaintTime, acdSaMetricMonoCounterEntry=acdSaMetricMonoCounterEntry, acdSaMetricConfigSrcName=acdSaMetricConfigSrcName, acdSaServiceHistCounterIntervalEnd=acdSaServiceHistCounterIntervalEnd, acdSaServiceConfigEntry=acdSaServiceConfigEntry, acdSaServiceConfigName=acdSaServiceConfigName, acdSaMetricHistCounterIntervalEnd=acdSaMetricHistCounterIntervalEnd, acdSaServiceMonoCounterUaTime=acdSaServiceMonoCounterUaTime, acdSaMetricConfigThreshold=acdSaMetricConfigThreshold, acdSaServiceMonoCounterLargestGap=acdSaServiceMonoCounterLargestGap, acdSaServiceStatusEntry=acdSaServiceStatusEntry, acdSaServiceConfigRowStatus=acdSaServiceConfigRowStatus, acdSaServiceHistCounterChliTime=acdSaServiceHistCounterChliTime, acdSaServiceCounterUpTime=acdSaServiceCounterUpTime, acdSaServiceMonoCounterGroup=acdSaServiceMonoCounterGroup, acdSaMetricConfigGroup=acdSaMetricConfigGroup, acdSaMetricCounterEntry=acdSaMetricCounterEntry, AcdSaOperStateFlag=AcdSaOperStateFlag, acdSaServiceStatusNbrMetrics=acdSaServiceStatusNbrMetrics, acdSaServiceHistCounterLargestGap=acdSaServiceHistCounterLargestGap, acdSaGroups=acdSaGroups, acdSaServiceStatusID=acdSaServiceStatusID, acdSaNotifications=acdSaNotifications, acdSaMetricHistCounterValidFlag=acdSaMetricHistCounterValidFlag, acdSaMetricMonoCounterValidFlag=acdSaMetricMonoCounterValidFlag, acdSaServiceCounterChliTime=acdSaServiceCounterChliTime, acdSaServiceMonoCounterEntry=acdSaServiceMonoCounterEntry, acdSaServiceHistCounterGaps=acdSaServiceHistCounterGaps, acdSaServiceCounterValidFlag=acdSaServiceCounterValidFlag, acdSaServiceCounterGroup=acdSaServiceCounterGroup, acdSaServiceCounterGaps=acdSaServiceCounterGaps, acdSaServiceMonoCounterGaps=acdSaServiceMonoCounterGaps, acdSaServiceHistCounterUaTime=acdSaServiceHistCounterUaTime, acdSaMIBObjects=acdSaMIBObjects, acdSaMetricIndex=acdSaMetricIndex, acdSaServiceIndex=acdSaServiceIndex, acdSaServiceConfigHliWindowSize=acdSaServiceConfigHliWindowSize, acdSaServiceHistCounterAvailRatio=acdSaServiceHistCounterAvailRatio, acdSaMetricConfigName=acdSaMetricConfigName, acdSaServiceCounterChliRatio=acdSaServiceCounterChliRatio, acdSaConfig=acdSaConfig, acdSaServiceStatusGroup=acdSaServiceStatusGroup, acdSaMetricConfigEntry=acdSaMetricConfigEntry, acdSaCompliance=acdSaCompliance, acdSaMetricCounterChliTime=acdSaMetricCounterChliTime, acdSaServiceCounterPeriodIndex=acdSaServiceCounterPeriodIndex, PYSNMP_MODULE_ID=acdSa, acdSaServiceConfigAdminState=acdSaServiceConfigAdminState, acdSaServiceHistCounterEntry=acdSaServiceHistCounterEntry, acdSaServiceHistCounterPeriodIndex=acdSaServiceHistCounterPeriodIndex, acdSaServiceStatusName=acdSaServiceStatusName, acdSaMetricMonoCounterTable=acdSaMetricMonoCounterTable, acdSaServiceCounterLargestGap=acdSaServiceCounterLargestGap, acdSaServiceMonoCounterChliTime=acdSaServiceMonoCounterChliTime, acdSaMetricHistCounterTable=acdSaMetricHistCounterTable, acdSaConformance=acdSaConformance, acdSaServiceHistCounterValidFlag=acdSaServiceHistCounterValidFlag, acdSaServiceConfigGroup=acdSaServiceConfigGroup)

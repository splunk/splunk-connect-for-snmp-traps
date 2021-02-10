#
# PySNMP MIB module TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, IpAddress, Counter32, MibIdentifier, Counter64, Integer32, NotificationType, ObjectIdentity, iso, Bits, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "Counter64", "Integer32", "NotificationType", "ObjectIdentity", "iso", "Bits", "Gauge32", "ModuleIdentity")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
TrpzApNum, TrpzApRadioIndex, TrpzRssi, TrpzRadioRateEx, TrpzChannelNum = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApNum", "TrpzApRadioIndex", "TrpzRssi", "TrpzRadioRateEx", "TrpzChannelNum")
TrpzRFDetectClassificationReason, TrpzRFDetectDot11ModulationStandard, TrpzRFDetectClassification, TrpzRFDetectNetworkingMode = mibBuilder.importSymbols("TRAPEZE-NETWORKS-RF-DETECT-TC", "TrpzRFDetectClassificationReason", "TrpzRFDetectDot11ModulationStandard", "TrpzRFDetectClassification", "TrpzRFDetectNetworkingMode")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzInfoRFDetectMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 9))
trpzInfoRFDetectMib.setRevisions(('2011-07-27 00:22', '2009-08-18 00:21', '2007-06-27 00:11', '2007-04-18 00:10', '2006-10-11 00:03',))
if mibBuilder.loadTexts: trpzInfoRFDetectMib.setLastUpdated('201107270022Z')
if mibBuilder.loadTexts: trpzInfoRFDetectMib.setOrganization('Trapeze Networks')
trpzInfoRFDetectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1))
trpzInfoRFDetectDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1))
trpzInfoRFDetectXmtrTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1), )
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrTable.setStatus('current')
trpzInfoRFDetectXmtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrTransmitterMacAddress"), (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrListenerMacAddress"), (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrChannelNum"))
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrEntry.setStatus('current')
trpzInfoRFDetectXmtrTransmitterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrTransmitterMacAddress.setStatus('current')
trpzInfoRFDetectXmtrListenerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrListenerMacAddress.setStatus('current')
trpzInfoRFDetectXmtrChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 3), TrpzChannelNum())
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrChannelNum.setStatus('current')
trpzInfoRFDetectXmtrRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 4), TrpzRssi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrRssi.setStatus('current')
trpzInfoRFDetectXmtrSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrSsid.setStatus('current')
trpzInfoRFDetectXmtrNetworkingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 6), TrpzRFDetectNetworkingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrNetworkingMode.setStatus('current')
trpzInfoRFDetectXmtrClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 7), TrpzRFDetectClassification()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrClassification.setStatus('current')
trpzInfoRFDetectXmtrClassificationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 8), TrpzRFDetectClassificationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectXmtrClassificationReason.setStatus('current')
trpzInfoRFDetectClientTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3), )
if mibBuilder.loadTexts: trpzInfoRFDetectClientTable.setStatus('current')
trpzInfoRFDetectClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientMacAddress"), (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientListenerMacAddress"))
if mibBuilder.loadTexts: trpzInfoRFDetectClientEntry.setStatus('current')
trpzInfoRFDetectClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzInfoRFDetectClientMacAddress.setStatus('current')
trpzInfoRFDetectClientListenerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: trpzInfoRFDetectClientListenerMacAddress.setStatus('current')
trpzInfoRFDetectClientConnectedBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientConnectedBssid.setStatus('current')
trpzInfoRFDetectClientApNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 4), TrpzApNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientApNum.setStatus('current')
trpzInfoRFDetectClientApRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 5), TrpzApRadioIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientApRadioIndex.setStatus('current')
trpzInfoRFDetectClientModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 6), TrpzRFDetectDot11ModulationStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientModulation.setStatus('current')
trpzInfoRFDetectClientChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 7), TrpzChannelNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientChannelNum.setStatus('current')
trpzInfoRFDetectClientRate = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 8), TrpzRadioRateEx()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientRate.setStatus('current')
trpzInfoRFDetectClientRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 9), TrpzRssi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientRssi.setStatus('current')
trpzInfoRFDetectClientClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 10), TrpzRFDetectClassification()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectClientClassification.setStatus('current')
trpzInfoRFDetectCurrentXmtrTableSize = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzInfoRFDetectCurrentXmtrTableSize.setStatus('current')
trpzInfoRFDetectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2))
trpzInfoRFDetectCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1))
trpzInfoRFDetectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2))
trpzInfoRFDetectCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrGroup"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassificationGroup"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectCurrentXmtrTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectCompliance = trpzInfoRFDetectCompliance.setStatus('obsolete')
trpzInfoRFDetectComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1, 2)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrGroup"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassificationGroup"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectCurrentXmtrTableSizeGroup"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectComplianceRev2 = trpzInfoRFDetectComplianceRev2.setStatus('current')
trpzInfoRFDetectXmtrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrRssi"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrSsid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectXmtrGroup = trpzInfoRFDetectXmtrGroup.setStatus('current')
trpzInfoRFDetectXmtrClassificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 2)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrNetworkingMode"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassification"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassificationReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectXmtrClassificationGroup = trpzInfoRFDetectXmtrClassificationGroup.setStatus('current')
trpzInfoRFDetectCurrentXmtrTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 3)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectCurrentXmtrTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectCurrentXmtrTableSizeGroup = trpzInfoRFDetectCurrentXmtrTableSizeGroup.setStatus('current')
trpzInfoRFDetectClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 4)).setObjects(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientConnectedBssid"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientApNum"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientApRadioIndex"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientModulation"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientChannelNum"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientRate"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientRssi"), ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientClassification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzInfoRFDetectClientGroup = trpzInfoRFDetectClientGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", trpzInfoRFDetectClientEntry=trpzInfoRFDetectClientEntry, trpzInfoRFDetectClientModulation=trpzInfoRFDetectClientModulation, trpzInfoRFDetectXmtrClassificationGroup=trpzInfoRFDetectXmtrClassificationGroup, trpzInfoRFDetectClientRssi=trpzInfoRFDetectClientRssi, trpzInfoRFDetectXmtrTransmitterMacAddress=trpzInfoRFDetectXmtrTransmitterMacAddress, trpzInfoRFDetectCurrentXmtrTableSize=trpzInfoRFDetectCurrentXmtrTableSize, trpzInfoRFDetectConformance=trpzInfoRFDetectConformance, trpzInfoRFDetectCompliances=trpzInfoRFDetectCompliances, trpzInfoRFDetectCurrentXmtrTableSizeGroup=trpzInfoRFDetectCurrentXmtrTableSizeGroup, trpzInfoRFDetectMib=trpzInfoRFDetectMib, trpzInfoRFDetectComplianceRev2=trpzInfoRFDetectComplianceRev2, trpzInfoRFDetectClientChannelNum=trpzInfoRFDetectClientChannelNum, trpzInfoRFDetectClientConnectedBssid=trpzInfoRFDetectClientConnectedBssid, trpzInfoRFDetectObjects=trpzInfoRFDetectObjects, trpzInfoRFDetectXmtrChannelNum=trpzInfoRFDetectXmtrChannelNum, trpzInfoRFDetectXmtrListenerMacAddress=trpzInfoRFDetectXmtrListenerMacAddress, trpzInfoRFDetectClientTable=trpzInfoRFDetectClientTable, trpzInfoRFDetectClientListenerMacAddress=trpzInfoRFDetectClientListenerMacAddress, trpzInfoRFDetectClientGroup=trpzInfoRFDetectClientGroup, trpzInfoRFDetectXmtrClassificationReason=trpzInfoRFDetectXmtrClassificationReason, trpzInfoRFDetectCompliance=trpzInfoRFDetectCompliance, trpzInfoRFDetectXmtrNetworkingMode=trpzInfoRFDetectXmtrNetworkingMode, trpzInfoRFDetectClientApNum=trpzInfoRFDetectClientApNum, trpzInfoRFDetectXmtrGroup=trpzInfoRFDetectXmtrGroup, trpzInfoRFDetectDataObjects=trpzInfoRFDetectDataObjects, trpzInfoRFDetectClientApRadioIndex=trpzInfoRFDetectClientApRadioIndex, trpzInfoRFDetectClientClassification=trpzInfoRFDetectClientClassification, trpzInfoRFDetectXmtrTable=trpzInfoRFDetectXmtrTable, trpzInfoRFDetectXmtrRssi=trpzInfoRFDetectXmtrRssi, trpzInfoRFDetectXmtrSsid=trpzInfoRFDetectXmtrSsid, trpzInfoRFDetectClientRate=trpzInfoRFDetectClientRate, trpzInfoRFDetectGroups=trpzInfoRFDetectGroups, PYSNMP_MODULE_ID=trpzInfoRFDetectMib, trpzInfoRFDetectClientMacAddress=trpzInfoRFDetectClientMacAddress, trpzInfoRFDetectXmtrClassification=trpzInfoRFDetectXmtrClassification, trpzInfoRFDetectXmtrEntry=trpzInfoRFDetectXmtrEntry)

#
# PySNMP MIB module ATT-CNM-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATT-CNM-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Bits, enterprises, ObjectIdentity, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, NotificationType, Counter32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Bits", "enterprises", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "NotificationType", "Counter32", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_products = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1)).setLabel("att-products")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
att_cnmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1, 9)).setLabel("att-cnmAgent")
att_cnm = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15)).setLabel("att-cnm")
att_cnm_ds1 = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15, 3)).setLabel("att-cnm-ds1")
attCNMds1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1), )
if mibBuilder.loadTexts: attCNMds1ConfigTable.setStatus('mandatory')
attCNMds1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1), ).setIndexNames((0, "ATT-CNM-DS1-MIB", "attCNMds1ConfigIndex"))
if mibBuilder.loadTexts: attCNMds1ConfigEntry.setStatus('mandatory')
attCNMds1ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ConfigIndex.setStatus('mandatory')
attCNMds1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ds1ESF", 2), ("ds1D4", 3), ("ds1ANSI-ESF", 4), ("ds1G704", 5), ("ds1G704-CRC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1LineType.setStatus('mandatory')
attCNMds1ZeroCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds1JammedBit", 1), ("ds1B8ZS", 2), ("ds1InvertedHDLC", 3), ("ds1HDB3", 4), ("ds1ZBTSI", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ZeroCoding.setStatus('mandatory')
attCNMds1ErrorsMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsMaxIntervals.setStatus('mandatory')
attCNMds1ErrorsIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsIntervalLen.setStatus('mandatory')
attCNMds1StatusTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2), )
if mibBuilder.loadTexts: attCNMds1StatusTable.setStatus('mandatory')
attCNMds1StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1), ).setIndexNames((0, "ATT-CNM-DS1-MIB", "attCNMds1StatusIndex"))
if mibBuilder.loadTexts: attCNMds1StatusEntry.setStatus('mandatory')
attCNMds1StatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1StatusIndex.setStatus('mandatory')
attCNMds1LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1LineStatus.setStatus('mandatory')
attCNMds1ErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3), )
if mibBuilder.loadTexts: attCNMds1ErrorsTable.setStatus('mandatory')
attCNMds1ErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1), ).setIndexNames((0, "ATT-CNM-DS1-MIB", "attCNMds1ErrorsIndex"), (0, "ATT-CNM-DS1-MIB", "attCNMds1ErrorsInterval"))
if mibBuilder.loadTexts: attCNMds1ErrorsEntry.setStatus('mandatory')
attCNMds1ErrorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsIndex.setStatus('mandatory')
attCNMds1ErrorsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsInterval.setStatus('mandatory')
attCNMds1ErrorsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsTimeStamp.setStatus('mandatory')
attCNMds1ErrorsLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ErrorsLocalTime.setStatus('mandatory')
attCNMds1LCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1LCVs.setStatus('mandatory')
attCNMds1LESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1LESs.setStatus('mandatory')
attCNMds1LSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1LSESs.setStatus('mandatory')
attCNMds1CVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1CVs.setStatus('mandatory')
attCNMds1ESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1ESs.setStatus('mandatory')
attCNMds1SESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1SESs.setStatus('mandatory')
attCNMds1SEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1SEFSs.setStatus('mandatory')
attCNMds1UASs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds1UASs.setStatus('mandatory')
mibBuilder.exportSymbols("ATT-CNM-DS1-MIB", att_products=att_products, attCNMds1ErrorsEntry=attCNMds1ErrorsEntry, attCNMds1SESs=attCNMds1SESs, attCNMds1ConfigIndex=attCNMds1ConfigIndex, attCNMds1ErrorsMaxIntervals=attCNMds1ErrorsMaxIntervals, att_cnm_ds1=att_cnm_ds1, attCNMds1ErrorsIntervalLen=attCNMds1ErrorsIntervalLen, att_cnm=att_cnm, attCNMds1LESs=attCNMds1LESs, attCNMds1StatusTable=attCNMds1StatusTable, attCNMds1StatusIndex=attCNMds1StatusIndex, attCNMds1ConfigEntry=attCNMds1ConfigEntry, attCNMds1SEFSs=attCNMds1SEFSs, attCNMds1StatusEntry=attCNMds1StatusEntry, att_2=att_2, attCNMds1UASs=attCNMds1UASs, attCNMds1ErrorsLocalTime=attCNMds1ErrorsLocalTime, attCNMds1ErrorsTable=attCNMds1ErrorsTable, attCNMds1ErrorsIndex=attCNMds1ErrorsIndex, attCNMds1LSESs=attCNMds1LSESs, att_mgmt=att_mgmt, att_cnmAgent=att_cnmAgent, attCNMds1ErrorsInterval=attCNMds1ErrorsInterval, attCNMds1ErrorsTimeStamp=attCNMds1ErrorsTimeStamp, attCNMds1CVs=attCNMds1CVs, attCNMds1ConfigTable=attCNMds1ConfigTable, attCNMds1ZeroCoding=attCNMds1ZeroCoding, attCNMds1LineType=attCNMds1LineType, attCNMds1LineStatus=attCNMds1LineStatus, attCNMds1LCVs=attCNMds1LCVs, attCNMds1ESs=attCNMds1ESs)

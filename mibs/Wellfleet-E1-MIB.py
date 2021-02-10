#
# PySNMP MIB module Wellfleet-E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-E1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, NotificationType, IpAddress, mgmt, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, Unsigned32, mib_2, ObjectIdentity, Opaque, iso, Counter64, NotificationType, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "NotificationType", "IpAddress", "mgmt", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "Unsigned32", "mib-2", "ObjectIdentity", "Opaque", "iso", "Counter64", "NotificationType", "enterprises", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfLine, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfLine")
wfE1Table = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 11), )
if mibBuilder.loadTexts: wfE1Table.setStatus('mandatory')
wfE1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1), ).setIndexNames((0, "Wellfleet-E1-MIB", "wfE1Slot"), (0, "Wellfleet-E1-MIB", "wfE1Connector"))
if mibBuilder.loadTexts: wfE1Entry.setStatus('mandatory')
wfE1Delete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1Delete.setStatus('mandatory')
wfE1Disable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1Disable.setStatus('mandatory')
wfE1State = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1State.setStatus('mandatory')
wfE1Slot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1Slot.setStatus('mandatory')
wfE1Connector = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one", 1), ("two", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1Connector.setStatus('mandatory')
wfE1Madr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1Madr.setStatus('mandatory')
wfE1HDB3Support = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1HDB3Support.setStatus('mandatory')
wfE1ClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("internal", 1), ("slave", 2), ("manual", 4))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1ClockMode.setStatus('mandatory')
wfE1MiniDacs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1MiniDacs.setStatus('mandatory')
wfE1BipolarVios = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1BipolarVios.setStatus('mandatory')
wfE1FrameErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1FrameErrs.setStatus('mandatory')
wfE1RcvRemAlms = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1RcvRemAlms.setStatus('mandatory')
wfE1RcvMfmAlms = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1RcvMfmAlms.setStatus('mandatory')
wfE1MfsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1MfsErrs.setStatus('mandatory')
wfE1SyncLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1SyncLoss.setStatus('mandatory')
wfE1RcvSig1s = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1RcvSig1s.setStatus('mandatory')
wfE1RcvUnfrm1s = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1RcvUnfrm1s.setStatus('mandatory')
wfE1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e1", 1), ("e1crc4", 2))).clone('e1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1LineType.setStatus('mandatory')
wfE1CRC4Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfE1CRC4Errors.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-E1-MIB", wfE1State=wfE1State, wfE1Slot=wfE1Slot, wfE1Madr=wfE1Madr, wfE1SyncLoss=wfE1SyncLoss, wfE1RcvSig1s=wfE1RcvSig1s, wfE1Disable=wfE1Disable, wfE1LineType=wfE1LineType, wfE1Entry=wfE1Entry, wfE1HDB3Support=wfE1HDB3Support, wfE1Table=wfE1Table, wfE1RcvUnfrm1s=wfE1RcvUnfrm1s, wfE1FrameErrs=wfE1FrameErrs, wfE1RcvMfmAlms=wfE1RcvMfmAlms, wfE1MiniDacs=wfE1MiniDacs, wfE1CRC4Errors=wfE1CRC4Errors, wfE1Delete=wfE1Delete, wfE1BipolarVios=wfE1BipolarVios, wfE1Connector=wfE1Connector, wfE1ClockMode=wfE1ClockMode, wfE1RcvRemAlms=wfE1RcvRemAlms, wfE1MfsErrs=wfE1MfsErrs)

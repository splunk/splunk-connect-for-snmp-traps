#
# PySNMP MIB module Nortel-Magellan-Passport-FrameRelayIsdnMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-FrameRelayIsdnMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:17:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
frUniIndex, frUni = mibBuilder.importSymbols("Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex", "frUni")
Counter32, Unsigned32, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Counter32", "Unsigned32", "StorageType", "RowStatus", "DisplayString")
DigitString, NonReplicated = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "DigitString", "NonReplicated")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, Gauge32, IpAddress, ModuleIdentity, Integer32, Counter32, Unsigned32, ObjectIdentity, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Gauge32", "IpAddress", "ModuleIdentity", "Integer32", "Counter32", "Unsigned32", "ObjectIdentity", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
frameRelayIsdnMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122))
frUniIsdn = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100))
frUniIsdnRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1), )
if mibBuilder.loadTexts: frUniIsdnRowStatusTable.setStatus('mandatory')
frUniIsdnRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"))
if mibBuilder.loadTexts: frUniIsdnRowStatusEntry.setStatus('mandatory')
frUniIsdnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frUniIsdnRowStatus.setStatus('mandatory')
frUniIsdnComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnComponentName.setStatus('mandatory')
frUniIsdnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnStorageType.setStatus('mandatory')
frUniIsdnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: frUniIsdnIndex.setStatus('mandatory')
frUniIsdnProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11), )
if mibBuilder.loadTexts: frUniIsdnProvTable.setStatus('mandatory')
frUniIsdnProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"))
if mibBuilder.loadTexts: frUniIsdnProvEntry.setStatus('mandatory')
frUniIsdnT320 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frUniIsdnT320.setStatus('mandatory')
frUniIsdnAddressSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("isdnDna", 0), ("normalBehavior", 1))).clone('normalBehavior')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frUniIsdnAddressSignalling.setStatus('mandatory')
frUniIsdnOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12), )
if mibBuilder.loadTexts: frUniIsdnOperTable.setStatus('mandatory')
frUniIsdnOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayIsdnMIB", "frUniIsdnIndex"))
if mibBuilder.loadTexts: frUniIsdnOperEntry.setStatus('mandatory')
frUniIsdnDataSigChan = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnDataSigChan.setStatus('mandatory')
frUniIsdnBChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("busy", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnBChannelState.setStatus('mandatory')
frUniIsdnLastUsedCgpn = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 3), DigitString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnLastUsedCgpn.setStatus('mandatory')
frUniIsdnBChanIntState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("isdnInit", 0), ("waitAccEnable", 1), ("waitLnsResponse", 2), ("waitFramerData", 3), ("enabling", 4), ("waitAccRegAck", 5), ("up", 6), ("down", 7), ("releasing", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnBChanIntState.setStatus('mandatory')
frUniIsdnActiveVirtualCircuitsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 100, 12, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frUniIsdnActiveVirtualCircuitsCount.setStatus('mandatory')
frameRelayIsdnGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1))
frameRelayIsdnGroupBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4))
frameRelayIsdnGroupBD02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4, 3))
frameRelayIsdnGroupBD02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 1, 4, 3, 2))
frameRelayIsdnCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3))
frameRelayIsdnCapabilitiesBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4))
frameRelayIsdnCapabilitiesBD02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4, 3))
frameRelayIsdnCapabilitiesBD02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 122, 3, 4, 3, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-FrameRelayIsdnMIB", frUniIsdnDataSigChan=frUniIsdnDataSigChan, frUniIsdnOperEntry=frUniIsdnOperEntry, frUniIsdnComponentName=frUniIsdnComponentName, frUniIsdnActiveVirtualCircuitsCount=frUniIsdnActiveVirtualCircuitsCount, frameRelayIsdnMIB=frameRelayIsdnMIB, frUniIsdnRowStatus=frUniIsdnRowStatus, frUniIsdn=frUniIsdn, frUniIsdnStorageType=frUniIsdnStorageType, frameRelayIsdnCapabilities=frameRelayIsdnCapabilities, frUniIsdnAddressSignalling=frUniIsdnAddressSignalling, frameRelayIsdnGroupBD=frameRelayIsdnGroupBD, frUniIsdnT320=frUniIsdnT320, frUniIsdnBChanIntState=frUniIsdnBChanIntState, frameRelayIsdnCapabilitiesBD02=frameRelayIsdnCapabilitiesBD02, frameRelayIsdnGroup=frameRelayIsdnGroup, frUniIsdnProvEntry=frUniIsdnProvEntry, frUniIsdnIndex=frUniIsdnIndex, frUniIsdnLastUsedCgpn=frUniIsdnLastUsedCgpn, frameRelayIsdnGroupBD02A=frameRelayIsdnGroupBD02A, frameRelayIsdnCapabilitiesBD02A=frameRelayIsdnCapabilitiesBD02A, frameRelayIsdnGroupBD02=frameRelayIsdnGroupBD02, frUniIsdnRowStatusEntry=frUniIsdnRowStatusEntry, frUniIsdnOperTable=frUniIsdnOperTable, frUniIsdnProvTable=frUniIsdnProvTable, frUniIsdnBChannelState=frUniIsdnBChannelState, frameRelayIsdnCapabilitiesBD=frameRelayIsdnCapabilitiesBD, frUniIsdnRowStatusTable=frUniIsdnRowStatusTable)

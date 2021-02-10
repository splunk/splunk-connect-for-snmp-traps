#
# PySNMP MIB module SHIVA-AT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-AT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:54:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
tATalk, = mibBuilder.importSymbols("SHIVA-MIB", "tATalk")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, NotificationType, Unsigned32, iso, Bits, ModuleIdentity, Integer32, Gauge32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "Unsigned32", "iso", "Bits", "ModuleIdentity", "Integer32", "Gauge32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tRTMPEntryTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryTimeouts.setStatus('mandatory')
tRTMPEntryDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryDeletes.setStatus('mandatory')
tRTMPEntryEqualReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryEqualReplaces.setStatus('mandatory')
tRTMPEntryBetterReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryBetterReplaces.setStatus('mandatory')
tRTMPEntryAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryAdds.setStatus('mandatory')
tRTMPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tRTMPZeroCounters.setStatus('mandatory')
tZIPDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPDeletes.setStatus('mandatory')
tZIPAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPAdds.setStatus('mandatory')
tZIPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tZIPZeroCounters.setStatus('mandatory')
tAARPClearCache = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tAARPClearCache.setStatus('mandatory')
tKIPRoutesValid = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tKIPRoutesValid.setStatus('mandatory')
tNBPDeviceObject = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tNBPDeviceObject.setStatus('mandatory')
tNBPDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tNBPDeviceType.setStatus('mandatory')
tNBPDeviceZone = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tNBPDeviceZone.setStatus('mandatory')
tNBPDeviceSocket = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tNBPDeviceSocket.setStatus('mandatory')
tATDialinNetwork = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: tATDialinNetwork.setStatus('mandatory')
tATDialinZone = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: tATDialinZone.setStatus('mandatory')
tATRoutingMode = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("conformingRouter", 1), ("seedRouter", 2), ("endNode", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tATRoutingMode.setStatus('mandatory')
tATDialinPacketDeliveryMode = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("routing", 1), ("endNodeForwarding", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tATDialinPacketDeliveryMode.setStatus('mandatory')
tRTMPEntryTotal = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryTotal.setStatus('mandatory')
tZoneTotal = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZoneTotal.setStatus('mandatory')
mibBuilder.exportSymbols("SHIVA-AT-MIB", tZIPAdds=tZIPAdds, tRTMPZeroCounters=tRTMPZeroCounters, tRTMPEntryBetterReplaces=tRTMPEntryBetterReplaces, tRTMPEntryEqualReplaces=tRTMPEntryEqualReplaces, tRTMPEntryAdds=tRTMPEntryAdds, tRTMPEntryTotal=tRTMPEntryTotal, tZoneTotal=tZoneTotal, tATDialinZone=tATDialinZone, tZIPDeletes=tZIPDeletes, tATDialinPacketDeliveryMode=tATDialinPacketDeliveryMode, tKIPRoutesValid=tKIPRoutesValid, tNBPDeviceType=tNBPDeviceType, tNBPDeviceZone=tNBPDeviceZone, tRTMPEntryTimeouts=tRTMPEntryTimeouts, tAARPClearCache=tAARPClearCache, tNBPDeviceSocket=tNBPDeviceSocket, tATRoutingMode=tATRoutingMode, tRTMPEntryDeletes=tRTMPEntryDeletes, tZIPZeroCounters=tZIPZeroCounters, tATDialinNetwork=tATDialinNetwork, tNBPDeviceObject=tNBPDeviceObject)

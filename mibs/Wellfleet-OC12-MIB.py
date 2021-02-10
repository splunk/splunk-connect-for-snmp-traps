#
# PySNMP MIB module Wellfleet-OC12-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-OC12-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Gauge32, ObjectIdentity, Counter32, Counter64, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "IpAddress", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfSonetGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSonetGroup")
wfOc12ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20), )
if mibBuilder.loadTexts: wfOc12ConfigTable.setStatus('mandatory')
wfOc12ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1), ).setIndexNames((0, "Wellfleet-OC12-MIB", "wfOc12ConfigIndex"))
if mibBuilder.loadTexts: wfOc12ConfigEntry.setStatus('mandatory')
wfOc12ConfigDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigDelete.setStatus('mandatory')
wfOc12ConfigDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigDisable.setStatus('mandatory')
wfOc12ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigIndex.setStatus('mandatory')
wfOc12ConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigIfIndex.setStatus('mandatory')
wfOc12ConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 20))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("los", 3), ("lof", 4), ("ais", 5), ("rdi", 6), ("loopback", 7), ("notpresent", 20))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigState.setStatus('mandatory')
wfOc12ConfigLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 128, 512))).clone(namedValues=NamedValues(("noalarm", 1), ("los", 2), ("lof", 4), ("ais", 8), ("rdi", 16), ("loopback", 128), ("otherfailure", 512))).clone('noalarm')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigLineStatus.setStatus('mandatory')
wfOc12ConfigLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigLastChange.setStatus('mandatory')
wfOc12ConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfOc12ConfigType.setStatus('mandatory')
wfOc12ConfigLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("b3zs", 2), ("cmi", 3), ("nrz", 4), ("rz", 5))).clone('nrz')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigLineCoding.setStatus('mandatory')
wfOc12ConfigLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("shortsinglemode", 2), ("longsinglemode", 3), ("multimode", 4), ("coax", 5), ("utp", 6))).clone('shortsinglemode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigLineType.setStatus('mandatory')
wfOc12ConfigLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noloop", 1), ("payloadloop", 2), ("lineloop", 3))).clone('noloop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigLoopbackConfig.setStatus('mandatory')
wfOc12ConfigManagerMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("frac", 1), ("clear", 2))).clone('frac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOc12ConfigManagerMethod.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-OC12-MIB", wfOc12ConfigLineType=wfOc12ConfigLineType, wfOc12ConfigState=wfOc12ConfigState, wfOc12ConfigLineCoding=wfOc12ConfigLineCoding, wfOc12ConfigLastChange=wfOc12ConfigLastChange, wfOc12ConfigIndex=wfOc12ConfigIndex, wfOc12ConfigDelete=wfOc12ConfigDelete, wfOc12ConfigIfIndex=wfOc12ConfigIfIndex, wfOc12ConfigLineStatus=wfOc12ConfigLineStatus, wfOc12ConfigEntry=wfOc12ConfigEntry, wfOc12ConfigManagerMethod=wfOc12ConfigManagerMethod, wfOc12ConfigDisable=wfOc12ConfigDisable, wfOc12ConfigTable=wfOc12ConfigTable, wfOc12ConfigType=wfOc12ConfigType, wfOc12ConfigLoopbackConfig=wfOc12ConfigLoopbackConfig)

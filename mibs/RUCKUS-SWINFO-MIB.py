#
# PySNMP MIB module RUCKUS-SWINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-SWINFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ruckusCommonSwInfoModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonSwInfoModule")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Gauge32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Gauge32", "Unsigned32", "Counter32")
DateAndTime, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString", "TruthValue")
ruckusSwInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1))
if mibBuilder.loadTexts: ruckusSwInfoMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusSwInfoMIB.setOrganization('Ruckus Wireless Inc.')
ruckusSwInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1))
ruckusSwInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1))
ruckusSwInfoEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 2))
ruckusSwRevTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusSwRevTable.setStatus('current')
ruckusSwRevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1), ).setIndexNames((0, "RUCKUS-SWINFO-MIB", "ruckusSwRevIndex"))
if mibBuilder.loadTexts: ruckusSwRevEntry.setStatus('current')
ruckusSwRevIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: ruckusSwRevIndex.setStatus('current')
ruckusSwRevName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSwRevName.setStatus('current')
ruckusSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSwRevision.setStatus('current')
ruckusSwRevSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSwRevSize.setStatus('current')
ruckusSwRevStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSwRevStatus.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-SWINFO-MIB", ruckusSwRevTable=ruckusSwRevTable, ruckusSwInfoObjects=ruckusSwInfoObjects, ruckusSwRevEntry=ruckusSwRevEntry, ruckusSwRevStatus=ruckusSwRevStatus, ruckusSwInfoEvents=ruckusSwInfoEvents, ruckusSwInfoMIB=ruckusSwInfoMIB, ruckusSwRevision=ruckusSwRevision, PYSNMP_MODULE_ID=ruckusSwInfoMIB, ruckusSwRevIndex=ruckusSwRevIndex, ruckusSwRevSize=ruckusSwRevSize, ruckusSwRevName=ruckusSwRevName, ruckusSwInfo=ruckusSwInfo)

#
# PySNMP MIB module Juniper-Products-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Products-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
juniperUni, = mibBuilder.importSymbols("Juniper-UNI-SMI", "juniperUni")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, NotificationType, Gauge32, Unsigned32, TimeTicks, Counter32, ObjectIdentity, Counter64, Integer32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "TimeTicks", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 1))
juniProducts.setRevisions(('2006-11-24 09:13', '2005-05-25 06:04', '2003-12-16 18:54', '2002-11-13 20:18', '2001-12-07 15:36', '2001-03-01 15:27', '2000-05-24 00:00', '1999-12-13 19:36', '1999-11-16 00:00', '1999-09-28 00:00',))
if mibBuilder.loadTexts: juniProducts.setLastUpdated('200611240913Z')
if mibBuilder.loadTexts: juniProducts.setOrganization('Juniper Networks, Inc.')
juniperUniProductFamilies = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1))
juniProductFamilies = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1))
juniErx = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1))
juniErx1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 1))
juniErx700 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 2))
juniErx1440 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 3))
juniErx705 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 4))
juniErx310 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 5))
juniEseries2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6))
juniE320 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6, 1))
juniE120 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6, 2))
juniUmc = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5))
juniUmcSystemManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5, 1))
juniOemProductFamilies = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2))
juniMarconiProductFamilies = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1))
juniSsx = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1))
juniSsx1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 1))
juniSsx700 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 2))
juniSsx1440 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 3))
usSmx = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 3))
usServiceMediationSwitch2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 3, 1))
usSrx = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 4))
usServiceReadySwitch3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 4, 1))
mibBuilder.exportSymbols("Juniper-Products-MIB", juniSsx1440=juniSsx1440, juniSsx700=juniSsx700, juniEseries2=juniEseries2, juniProducts=juniProducts, usServiceMediationSwitch2100=usServiceMediationSwitch2100, usServiceReadySwitch3000=usServiceReadySwitch3000, PYSNMP_MODULE_ID=juniProducts, juniSsx1400=juniSsx1400, juniMarconiProductFamilies=juniMarconiProductFamilies, juniErx705=juniErx705, juniProductFamilies=juniProductFamilies, juniErx1400=juniErx1400, juniOemProductFamilies=juniOemProductFamilies, juniperUniProductFamilies=juniperUniProductFamilies, usSmx=usSmx, juniUmcSystemManagement=juniUmcSystemManagement, juniErx1440=juniErx1440, juniE120=juniE120, juniSsx=juniSsx, juniErx=juniErx, juniErx700=juniErx700, juniErx310=juniErx310, usSrx=usSrx, juniUmc=juniUmc, juniE320=juniE320)

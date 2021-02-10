#
# PySNMP MIB module NETAL-PRODUCTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETAL-PRODUCTS
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
netalProducts, netalModules, networkAlchemy = mibBuilder.importSymbols("NETAL-SMI", "netalProducts", "netalModules", "networkAlchemy")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, ObjectIdentity, Integer32, iso, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, ModuleIdentity, Gauge32, TimeTicks, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "ObjectIdentity", "Integer32", "iso", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netalProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972, 5, 1))
if mibBuilder.loadTexts: netalProductsMIB.setLastUpdated('200101160000Z')
if mibBuilder.loadTexts: netalProductsMIB.setOrganization('Network Alchemy, Inc.')
netalHardwareUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 1))
if mibBuilder.loadTexts: netalHardwareUnknown.setStatus('current')
netalKiltlifterUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 2))
if mibBuilder.loadTexts: netalKiltlifterUnknown.setStatus('current')
netalStingrayUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 3))
if mibBuilder.loadTexts: netalStingrayUnknown.setStatus('current')
netalCryptoCluster500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 4))
if mibBuilder.loadTexts: netalCryptoCluster500.setStatus('current')
netalCryptoCluster5010 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 5))
if mibBuilder.loadTexts: netalCryptoCluster5010.setStatus('current')
netalCryptoCluster501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 8))
if mibBuilder.loadTexts: netalCryptoCluster501.setStatus('current')
netalCryptoCluster5000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 10))
if mibBuilder.loadTexts: netalCryptoCluster5000.setStatus('current')
netalCryptoCluster2500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 11))
if mibBuilder.loadTexts: netalCryptoCluster2500.setStatus('current')
netalCryptoCluster2501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 12))
if mibBuilder.loadTexts: netalCryptoCluster2501.setStatus('current')
netalFreeBSDApplication = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 13))
if mibBuilder.loadTexts: netalFreeBSDApplication.setStatus('current')
netalCryptoCluster5200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 15))
if mibBuilder.loadTexts: netalCryptoCluster5200.setStatus('current')
netalCryptoCluster5205 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 16))
if mibBuilder.loadTexts: netalCryptoCluster5205.setStatus('current')
netalCA200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 18))
if mibBuilder.loadTexts: netalCA200.setStatus('current')
netalCA600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 19))
if mibBuilder.loadTexts: netalCA600.setStatus('current')
netalChameleon100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1, 20))
if mibBuilder.loadTexts: netalChameleon100.setStatus('current')
mibBuilder.exportSymbols("NETAL-PRODUCTS", netalProductsMIB=netalProductsMIB, netalHardwareUnknown=netalHardwareUnknown, netalKiltlifterUnknown=netalKiltlifterUnknown, netalCryptoCluster501=netalCryptoCluster501, netalStingrayUnknown=netalStingrayUnknown, netalCA200=netalCA200, netalCA600=netalCA600, netalCryptoCluster2500=netalCryptoCluster2500, PYSNMP_MODULE_ID=netalProductsMIB, netalCryptoCluster5200=netalCryptoCluster5200, netalCryptoCluster5205=netalCryptoCluster5205, netalCryptoCluster5000=netalCryptoCluster5000, netalChameleon100=netalChameleon100, netalFreeBSDApplication=netalFreeBSDApplication, netalCryptoCluster2501=netalCryptoCluster2501, netalCryptoCluster500=netalCryptoCluster500, netalCryptoCluster5010=netalCryptoCluster5010)

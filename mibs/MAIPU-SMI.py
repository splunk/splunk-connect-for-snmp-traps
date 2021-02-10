#
# PySNMP MIB module MAIPU-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MAIPU-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, Integer32, iso, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "Integer32", "iso", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
maipu = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651))
maipu.setRevisions(('1901-01-01 00:00',))
if mibBuilder.loadTexts: maipu.setLastUpdated('0101010000Z')
if mibBuilder.loadTexts: maipu.setOrganization('Maipu Data Communication, Inc.')
mpProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 1))
if mibBuilder.loadTexts: mpProducts.setStatus('current')
mpTrapObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 2))
if mibBuilder.loadTexts: mpTrapObject.setStatus('current')
mpMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 3))
if mibBuilder.loadTexts: mpMgmt.setStatus('current')
mpExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 4))
if mibBuilder.loadTexts: mpExperiment.setStatus('current')
mpSecurity = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 5))
if mibBuilder.loadTexts: mpSecurity.setStatus('current')
mpMgmt2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6))
if mibBuilder.loadTexts: mpMgmt2.setStatus('current')
mpSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 1))
if mibBuilder.loadTexts: mpSystem.setStatus('current')
mpRouterTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 2))
if mibBuilder.loadTexts: mpRouterTech.setStatus('current')
mpSwitchTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 3))
if mibBuilder.loadTexts: mpSwitchTech.setStatus('current')
mpVoipTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 4))
if mibBuilder.loadTexts: mpVoipTech.setStatus('current')
mpSecurityTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 5))
if mibBuilder.loadTexts: mpSecurityTech.setStatus('current')
mpApp = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 6))
if mibBuilder.loadTexts: mpApp.setStatus('current')
mpOtherSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 7))
if mibBuilder.loadTexts: mpOtherSys.setStatus('current')
mibBuilder.exportSymbols("MAIPU-SMI", mpMgmt2=mpMgmt2, PYSNMP_MODULE_ID=maipu, mpSwitchTech=mpSwitchTech, mpProducts=mpProducts, mpVoipTech=mpVoipTech, mpExperiment=mpExperiment, mpSecurityTech=mpSecurityTech, mpApp=mpApp, mpSecurity=mpSecurity, mpMgmt=mpMgmt, mpSystem=mpSystem, mpRouterTech=mpRouterTech, mpTrapObject=mpTrapObject, mpOtherSys=mpOtherSys, maipu=maipu)

#
# PySNMP MIB module ALCATEL-IND1-PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-PIM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:03:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Pim, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Pim")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InetAddressType, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressPrefixLength", "InetAddress")
pimInterfaceEntry, = mibBuilder.importSymbols("PIM-STD-MIB", "pimInterfaceEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Gauge32, TimeTicks, iso, MibIdentifier, Bits, Counter64, Counter32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "MibIdentifier", "Bits", "Counter64", "Counter32", "ObjectIdentity", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
alcatelIND1PIMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1))
alcatelIND1PIMMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1PIMMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1PIMMIB.setOrganization('Alcatel-Lucent')
alcatelIND1PIMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1))
alaPimsmGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1))
alaPimdmGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2))
alaPimGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3))
alaPimsmAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmAdminStatus.setStatus('current')
alaPimsmMaxRPs = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmMaxRPs.setStatus('current')
alaPimsmProbeTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmProbeTime.setStatus('current')
alaPimsmOldRegisterMessageSupport = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("header", 1), ("full", 2))).clone('header')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmOldRegisterMessageSupport.setStatus('current')
alaPimsmAdminSPTConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmAdminSPTConfig.setStatus('current')
alaPimsmRPThreshold = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmRPThreshold.setStatus('current')
alaPimsmV6AdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmV6AdminStatus.setStatus('current')
alaPimsmV6SPTConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmV6SPTConfig.setStatus('current')
alaPimsmV6RPSwitchover = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmV6RPSwitchover.setStatus('current')
alaPimsmBidirStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimsmBidirStatus.setStatus('current')
alaPimsmBidirPeriodicInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmBidirPeriodicInterval.setStatus('current')
alaPimsmBidirDFAbort = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmBidirDFAbort.setStatus('current')
alaPimsmNonBidirHelloPeriod = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(65535)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimsmNonBidirHelloPeriod.setStatus('current')
alaPimsmNonBidirHelloMsgsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimsmNonBidirHelloMsgsRcvd.setStatus('current')
alaPimsmNonBidirHelloAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 15), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimsmNonBidirHelloAddressType.setStatus('current')
alaPimsmNonBidirHelloOrigin = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 16), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimsmNonBidirHelloOrigin.setStatus('current')
alaPimsmV6BidirStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimsmV6BidirStatus.setStatus('current')
alaPimdmAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimdmAdminStatus.setStatus('current')
alaPimdmStateRefreshTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 2), Integer32().clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimdmStateRefreshTimeToLive.setStatus('current')
alaPimdmStateRefreshLimitInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimdmStateRefreshLimitInterval.setStatus('current')
alaPimdmV6AdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimdmV6AdminStatus.setStatus('current')
alaPimdmDenseGroupTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5), )
if mibBuilder.loadTexts: alaPimdmDenseGroupTable.setStatus('current')
alaPimdmDenseGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1), ).setIndexNames((0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupAddressType"), (0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupGrpAddress"), (0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupGrpPrefixLength"))
if mibBuilder.loadTexts: alaPimdmDenseGroupEntry.setStatus('current')
alaPimdmDenseGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaPimdmDenseGroupAddressType.setStatus('current')
alaPimdmDenseGroupGrpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: alaPimdmDenseGroupGrpAddress.setStatus('current')
alaPimdmDenseGroupGrpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 3), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: alaPimdmDenseGroupGrpPrefixLength.setStatus('current')
alaPimdmDenseGroupOverrideDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimdmDenseGroupOverrideDynamic.setStatus('current')
alaPimdmDenseGroupPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimdmDenseGroupPrecedence.setStatus('current')
alaPimdmDenseGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimdmDenseGroupRowStatus.setStatus('current')
alaPimBfdStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBfdStatus.setStatus('current')
alaPimBfdAllInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBfdAllInterfaceStatus.setStatus('current')
alaPimMoFRRStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimMoFRRStatus.setStatus('current')
alaPimMoFRRAllRouteStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimMoFRRAllRouteStatus.setStatus('current')
alaPimInterfaceAugTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5), )
if mibBuilder.loadTexts: alaPimInterfaceAugTable.setStatus('current')
alaPimInterfaceAugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5, 1), )
pimInterfaceEntry.registerAugmentions(("ALCATEL-IND1-PIM-MIB", "alaPimInterfaceAugEntry"))
alaPimInterfaceAugEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: alaPimInterfaceAugEntry.setStatus('current')
alaPimInterfaceBfdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimInterfaceBfdStatus.setStatus('current')
alaPimMbrAllSourcesStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaPimMbrAllSourcesStatus.setStatus('current')
alaPimMbrOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimMbrOperStatus.setStatus('current')
alaPimNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 0))
alaPimNonBidirHello = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 0, 1)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloAddressType"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloOrigin"))
if mibBuilder.loadTexts: alaPimNonBidirHello.setStatus('current')
alcatelIND1PIMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2))
alcatelIND1PIMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1))
alcatelIND1PIMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2))
alaPimsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimsmConfigMIBGroup"), ("ALCATEL-IND1-PIM-MIB", "alaPimConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimsmCompliance = alaPimsmCompliance.setStatus('current')
alaPimdmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimdmConfigMIBGroup"), ("ALCATEL-IND1-PIM-MIB", "alaPimConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimdmCompliance = alaPimdmCompliance.setStatus('current')
alaPimsmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmMaxRPs"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmProbeTime"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmOldRegisterMessageSupport"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminSPTConfig"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmRPThreshold"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6AdminStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6SPTConfig"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6RPSwitchover"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirPeriodicInterval"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirDFAbort"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloPeriod"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloMsgsRcvd"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6BidirStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimsmConfigMIBGroup = alaPimsmConfigMIBGroup.setStatus('current')
alaPimdmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 2)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimdmAdminStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshTimeToLive"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshLimitInterval"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmV6AdminStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupOverrideDynamic"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupPrecedence"), ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimdmConfigMIBGroup = alaPimdmConfigMIBGroup.setStatus('current')
alaPimConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 3)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimBfdStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimBfdAllInterfaceStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimMoFRRStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimMoFRRAllRouteStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimInterfaceBfdStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimMbrAllSourcesStatus"), ("ALCATEL-IND1-PIM-MIB", "alaPimMbrOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimConfigMIBGroup = alaPimConfigMIBGroup.setStatus('current')
alaPimOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 4)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloAddressType"), ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloOrigin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimOptionalGroup = alaPimOptionalGroup.setStatus('current')
alaPimNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 5)).setObjects(("ALCATEL-IND1-PIM-MIB", "alaPimNonBidirHello"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimNotificationGroup = alaPimNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-PIM-MIB", alaPimsmRPThreshold=alaPimsmRPThreshold, alaPimsmConfigMIBGroup=alaPimsmConfigMIBGroup, alaPimsmNonBidirHelloPeriod=alaPimsmNonBidirHelloPeriod, alaPimsmAdminStatus=alaPimsmAdminStatus, alaPimdmGlobalConfig=alaPimdmGlobalConfig, alcatelIND1PIMMIBCompliances=alcatelIND1PIMMIBCompliances, alcatelIND1PIMMIBGroups=alcatelIND1PIMMIBGroups, alaPimsmV6SPTConfig=alaPimsmV6SPTConfig, alaPimdmAdminStatus=alaPimdmAdminStatus, alaPimdmV6AdminStatus=alaPimdmV6AdminStatus, alaPimsmCompliance=alaPimsmCompliance, alaPimConfigMIBGroup=alaPimConfigMIBGroup, alaPimOptionalGroup=alaPimOptionalGroup, alaPimsmNonBidirHelloMsgsRcvd=alaPimsmNonBidirHelloMsgsRcvd, alaPimsmGlobalConfig=alaPimsmGlobalConfig, alcatelIND1PIMMIB=alcatelIND1PIMMIB, alaPimsmV6BidirStatus=alaPimsmV6BidirStatus, alaPimBfdStatus=alaPimBfdStatus, alaPimdmStateRefreshTimeToLive=alaPimdmStateRefreshTimeToLive, alaPimdmDenseGroupOverrideDynamic=alaPimdmDenseGroupOverrideDynamic, alcatelIND1PIMMIBObjects=alcatelIND1PIMMIBObjects, alaPimInterfaceAugTable=alaPimInterfaceAugTable, alaPimdmDenseGroupGrpPrefixLength=alaPimdmDenseGroupGrpPrefixLength, alaPimBfdAllInterfaceStatus=alaPimBfdAllInterfaceStatus, alaPimsmBidirStatus=alaPimsmBidirStatus, alaPimdmDenseGroupTable=alaPimdmDenseGroupTable, alaPimMbrOperStatus=alaPimMbrOperStatus, alaPimMoFRRAllRouteStatus=alaPimMoFRRAllRouteStatus, alcatelIND1PIMMIBConformance=alcatelIND1PIMMIBConformance, alaPimdmDenseGroupEntry=alaPimdmDenseGroupEntry, alaPimdmDenseGroupPrecedence=alaPimdmDenseGroupPrecedence, alaPimdmCompliance=alaPimdmCompliance, alaPimMbrAllSourcesStatus=alaPimMbrAllSourcesStatus, PYSNMP_MODULE_ID=alcatelIND1PIMMIB, alaPimNonBidirHello=alaPimNonBidirHello, alaPimdmStateRefreshLimitInterval=alaPimdmStateRefreshLimitInterval, alaPimsmMaxRPs=alaPimsmMaxRPs, alaPimNotificationGroup=alaPimNotificationGroup, alaPimGlobalConfig=alaPimGlobalConfig, alaPimNotifications=alaPimNotifications, alaPimdmDenseGroupGrpAddress=alaPimdmDenseGroupGrpAddress, alaPimsmOldRegisterMessageSupport=alaPimsmOldRegisterMessageSupport, alaPimdmDenseGroupAddressType=alaPimdmDenseGroupAddressType, alaPimMoFRRStatus=alaPimMoFRRStatus, alaPimInterfaceAugEntry=alaPimInterfaceAugEntry, alaPimsmV6AdminStatus=alaPimsmV6AdminStatus, alaPimsmNonBidirHelloOrigin=alaPimsmNonBidirHelloOrigin, alaPimsmProbeTime=alaPimsmProbeTime, alaPimsmNonBidirHelloAddressType=alaPimsmNonBidirHelloAddressType, alaPimdmConfigMIBGroup=alaPimdmConfigMIBGroup, alaPimsmBidirPeriodicInterval=alaPimsmBidirPeriodicInterval, alaPimsmAdminSPTConfig=alaPimsmAdminSPTConfig, alaPimsmV6RPSwitchover=alaPimsmV6RPSwitchover, alaPimsmBidirDFAbort=alaPimsmBidirDFAbort, alaPimInterfaceBfdStatus=alaPimInterfaceBfdStatus, alaPimdmDenseGroupRowStatus=alaPimdmDenseGroupRowStatus)

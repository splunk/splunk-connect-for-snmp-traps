#
# PySNMP MIB module OWNEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OWNEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ownExt, = mibBuilder.importSymbols("APENT-MIB", "ownExt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, iso, ObjectIdentity, Bits, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "iso", "ObjectIdentity", "Bits", "Counter64", "TimeTicks", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
apOwnExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 25, 1))
if mibBuilder.loadTexts: apOwnExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apOwnExtMib.setOrganization('ArrowPoint Communications Inc.')
apOwnTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2), )
if mibBuilder.loadTexts: apOwnTable.setStatus('current')
apOwnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1), ).setIndexNames((0, "OWNEXT-MIB", "apOwnName"))
if mibBuilder.loadTexts: apOwnEntry.setStatus('current')
apOwnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnName.setStatus('current')
apOwnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnIndex.setStatus('current')
apOwnMaxFlowPipeBwdth = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnMaxFlowPipeBwdth.setStatus('current')
apOwnFlowPipeBurstTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnFlowPipeBurstTolerance.setStatus('current')
apOwnMaxPrioritizedFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnMaxPrioritizedFlows.setStatus('current')
apOwnBillingInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnBillingInfo.setStatus('current')
apOwnAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnAddress.setStatus('current')
apOwnEmailAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnEmailAddress.setStatus('current')
apOwnFlowPipeBwdthAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnFlowPipeBwdthAlloc.setStatus('current')
apOwnFlowPipeActiveFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnFlowPipeActiveFlows.setStatus('current')
apOwnFlowPipeTotalFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnFlowPipeTotalFlows.setStatus('current')
apOwnFlowPipeTotalMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnFlowPipeTotalMisses.setStatus('current')
apOwnQosBwdthAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnQosBwdthAlloc.setStatus('current')
apOwnBEBwdthAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnBEBwdthAlloc.setStatus('current')
apOwnHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnHits.setStatus('current')
apOwnRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnRedirects.setStatus('current')
apOwnDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnDrops.setStatus('current')
apOwnRejNoServices = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnRejNoServices.setStatus('current')
apOwnRejServOverload = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnRejServOverload.setStatus('current')
apOwnSpoofs = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnSpoofs.setStatus('current')
apOwnNats = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnNats.setStatus('current')
apOwnByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnByteCount.setStatus('current')
apOwnFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apOwnFrameCount.setStatus('current')
apOwnDNSPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("accept", 1), ("push", 2), ("both", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnDNSPolicy.setStatus('current')
apOwnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnStatus.setStatus('current')
apOwnCaseSensitive = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("insensitive", 0), ("sensitive", 1))).clone('insensitive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnCaseSensitive.setStatus('current')
apOwnDNSBalance = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("preferlocal", 1), ("roundrobin", 2), ("leastloaded", 3))).clone('roundrobin')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apOwnDNSBalance.setStatus('current')
mibBuilder.exportSymbols("OWNEXT-MIB", apOwnDrops=apOwnDrops, apOwnIndex=apOwnIndex, apOwnFlowPipeActiveFlows=apOwnFlowPipeActiveFlows, apOwnByteCount=apOwnByteCount, apOwnFlowPipeTotalMisses=apOwnFlowPipeTotalMisses, apOwnRejNoServices=apOwnRejNoServices, apOwnFrameCount=apOwnFrameCount, PYSNMP_MODULE_ID=apOwnExtMib, apOwnNats=apOwnNats, apOwnSpoofs=apOwnSpoofs, apOwnQosBwdthAlloc=apOwnQosBwdthAlloc, apOwnName=apOwnName, apOwnHits=apOwnHits, apOwnEntry=apOwnEntry, apOwnBillingInfo=apOwnBillingInfo, apOwnExtMib=apOwnExtMib, apOwnFlowPipeBwdthAlloc=apOwnFlowPipeBwdthAlloc, apOwnRejServOverload=apOwnRejServOverload, apOwnRedirects=apOwnRedirects, apOwnAddress=apOwnAddress, apOwnCaseSensitive=apOwnCaseSensitive, apOwnMaxPrioritizedFlows=apOwnMaxPrioritizedFlows, apOwnFlowPipeTotalFlows=apOwnFlowPipeTotalFlows, apOwnTable=apOwnTable, apOwnMaxFlowPipeBwdth=apOwnMaxFlowPipeBwdth, apOwnStatus=apOwnStatus, apOwnBEBwdthAlloc=apOwnBEBwdthAlloc, apOwnEmailAddress=apOwnEmailAddress, apOwnDNSBalance=apOwnDNSBalance, apOwnFlowPipeBurstTolerance=apOwnFlowPipeBurstTolerance, apOwnDNSPolicy=apOwnDNSPolicy)

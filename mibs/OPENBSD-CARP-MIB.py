#
# PySNMP MIB module OPENBSD-CARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPENBSD-CARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter64, ObjectIdentity, TimeTicks, Integer32, MibIdentifier, Counter32, iso, Bits, NotificationType, IpAddress, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter64", "ObjectIdentity", "TimeTicks", "Integer32", "MibIdentifier", "Counter32", "iso", "Bits", "NotificationType", "IpAddress", "Unsigned32", "enterprises")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
carpMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 6))
carpMIBObjects.setRevisions(('2012-01-31 00:00',))
if mibBuilder.loadTexts: carpMIBObjects.setLastUpdated('201201310000Z')
if mibBuilder.loadTexts: carpMIBObjects.setOrganization('OpenBSD')
carpSysctl = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 1))
carpIf = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 2))
carpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 3))
carpAllow = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpAllow.setStatus('current')
carpPreempt = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPreempt.setStatus('current')
carpLog = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpLog.setStatus('current')
carpIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfNumber.setStatus('current')
carpIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2), )
if mibBuilder.loadTexts: carpIfTable.setStatus('current')
carpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1), ).setIndexNames((0, "OPENBSD-CARP-MIB", "carpIfIndex"))
if mibBuilder.loadTexts: carpIfEntry.setStatus('current')
carpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfIndex.setStatus('current')
carpIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfDescr.setStatus('current')
carpIfVhid = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfVhid.setStatus('current')
carpIfDev = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfDev.setStatus('current')
carpIfAdvbase = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfAdvbase.setStatus('current')
carpIfAdvskew = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfAdvskew.setStatus('current')
carpIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("init", 0), ("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfState.setStatus('current')
carpIpPktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIpPktsRecv.setStatus('current')
carpIp6PktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIp6PktsRecv.setStatus('current')
carpPktDiscardsForBadInterface = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadInterface.setStatus('current')
carpPktDiscardsForWrongTtl = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForWrongTtl.setStatus('current')
carpPktShorterThanHeader = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktShorterThanHeader.setStatus('current')
carpPktDiscardsForBadChecksum = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadChecksum.setStatus('current')
carpPktDiscardsForBadVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadVersion.setStatus('current')
carpPktDiscardsForTooShort = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForTooShort.setStatus('current')
carpPktDiscardsForBadAuth = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadAuth.setStatus('current')
carpPktDiscardsForBadVhid = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadVhid.setStatus('current')
carpPktDiscardsForBadAddressList = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadAddressList.setStatus('current')
carpIpPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIpPktsSent.setStatus('current')
carpIp6PktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIp6PktsSent.setStatus('current')
carpNoMemory = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpNoMemory.setStatus('current')
carpTransitionsToMaster = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpTransitionsToMaster.setStatus('current')
mibBuilder.exportSymbols("OPENBSD-CARP-MIB", carpTransitionsToMaster=carpTransitionsToMaster, carpIfNumber=carpIfNumber, carpIfAdvbase=carpIfAdvbase, carpIfDescr=carpIfDescr, carpStats=carpStats, carpPktDiscardsForBadChecksum=carpPktDiscardsForBadChecksum, carpPktDiscardsForTooShort=carpPktDiscardsForTooShort, carpPktDiscardsForBadAuth=carpPktDiscardsForBadAuth, carpPreempt=carpPreempt, carpIfVhid=carpIfVhid, carpNoMemory=carpNoMemory, carpIfAdvskew=carpIfAdvskew, carpPktDiscardsForBadVersion=carpPktDiscardsForBadVersion, carpPktDiscardsForWrongTtl=carpPktDiscardsForWrongTtl, carpPktDiscardsForBadAddressList=carpPktDiscardsForBadAddressList, PYSNMP_MODULE_ID=carpMIBObjects, carpIp6PktsRecv=carpIp6PktsRecv, carpLog=carpLog, carpSysctl=carpSysctl, carpPktDiscardsForBadInterface=carpPktDiscardsForBadInterface, carpIfDev=carpIfDev, carpIfState=carpIfState, carpIfEntry=carpIfEntry, carpIfIndex=carpIfIndex, carpIpPktsSent=carpIpPktsSent, carpIp6PktsSent=carpIp6PktsSent, carpIfTable=carpIfTable, carpIf=carpIf, carpMIBObjects=carpMIBObjects, carpIpPktsRecv=carpIpPktsRecv, carpAllow=carpAllow, carpPktShorterThanHeader=carpPktShorterThanHeader, carpPktDiscardsForBadVhid=carpPktDiscardsForBadVhid)

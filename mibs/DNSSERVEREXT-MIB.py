#
# PySNMP MIB module DNSSERVEREXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNSSERVEREXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
dnsServerExt, = mibBuilder.importSymbols("APENT-MIB", "dnsServerExt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Gauge32, TimeTicks, MibIdentifier, NotificationType, Bits, Unsigned32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Gauge32", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "Unsigned32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
apDnsServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 40, 1))
if mibBuilder.loadTexts: apDnsServerMib.setLastUpdated('9806122000Z')
if mibBuilder.loadTexts: apDnsServerMib.setOrganization('ArrowPoint Communications Inc.')
apDnsServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsServerEnable.setStatus('current')
apDnsServerBufferCount = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsServerBufferCount.setStatus('current')
apDnsServerResponderTasks = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 250)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsServerResponderTasks.setStatus('current')
apDnsPeerRcvEntries = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 1024)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsPeerRcvEntries.setStatus('current')
apDnsPeerSndEntries = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 1024)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsPeerSndEntries.setStatus('current')
apDnsPeerReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 120)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsPeerReportInterval.setStatus('current')
apDnsAclIndex = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDnsAclIndex.setStatus('current')
apProximityType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("pdns", 2), ("pdb", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProximityType.setStatus('current')
apProximityEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProximityEnable.setStatus('current')
apProximityZone = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProximityZone.setStatus('current')
apProximityDescription = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20)).clone(hexValue="0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityDescription.setStatus('current')
apProximityZoneMax = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 16))).clone(namedValues=NamedValues(("tier1", 6), ("tier2", 16))).clone('tier1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProximityZoneMax.setStatus('current')
apProximityPDBIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 40, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityPDBIpAddr.setStatus('current')
apProximityRecordTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15), )
if mibBuilder.loadTexts: apProximityRecordTable.setStatus('current')
apProximityRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1), ).setIndexNames((0, "DNSSERVEREXT-MIB", "apProximityRecordName"))
if mibBuilder.loadTexts: apProximityRecordEntry.setStatus('current')
apProximityRecordName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordName.setStatus('current')
apProximityRecordType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("typeA", 1), ("typeNS", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordType.setStatus('current')
apProximityRecordAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordAddr.setStatus('current')
apProximityRecordTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordTtl.setStatus('current')
apProximityRecordKalType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("kal-none", 0), ("kal-icmp", 1), ("kal-ap", 2))).clone('kal-icmp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordKalType.setStatus('current')
apProximityRecordKalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordKalAddr.setStatus('current')
apProximityRecordKalThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 254)).clone(254)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordKalThreshold.setStatus('current')
apProximityRecordRtnSingleArec = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("multiple", 0), ("single", 1))).clone('single')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordRtnSingleArec.setStatus('current')
apProximityRecordStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apProximityRecordStatus.setStatus('current')
mibBuilder.exportSymbols("DNSSERVEREXT-MIB", apProximityRecordKalThreshold=apProximityRecordKalThreshold, apProximityDescription=apProximityDescription, apProximityPDBIpAddr=apProximityPDBIpAddr, apDnsPeerRcvEntries=apDnsPeerRcvEntries, apProximityEnable=apProximityEnable, apProximityRecordEntry=apProximityRecordEntry, apProximityRecordName=apProximityRecordName, apProximityRecordAddr=apProximityRecordAddr, apProximityRecordKalType=apProximityRecordKalType, apProximityZone=apProximityZone, apDnsServerMib=apDnsServerMib, apProximityRecordRtnSingleArec=apProximityRecordRtnSingleArec, apProximityType=apProximityType, apDnsAclIndex=apDnsAclIndex, apDnsServerBufferCount=apDnsServerBufferCount, apProximityRecordType=apProximityRecordType, apProximityZoneMax=apProximityZoneMax, apDnsServerEnable=apDnsServerEnable, PYSNMP_MODULE_ID=apDnsServerMib, apProximityRecordTtl=apProximityRecordTtl, apProximityRecordTable=apProximityRecordTable, apDnsServerResponderTasks=apDnsServerResponderTasks, apDnsPeerSndEntries=apDnsPeerSndEntries, apProximityRecordKalAddr=apProximityRecordKalAddr, apDnsPeerReportInterval=apDnsPeerReportInterval, apProximityRecordStatus=apProximityRecordStatus)

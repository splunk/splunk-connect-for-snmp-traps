#
# PySNMP MIB module A3COM-HUAWEI-MPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MPM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter64, Gauge32, mib_2, IpAddress, Integer32, NotificationType, Unsigned32, TimeTicks, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "mib-2", "IpAddress", "Integer32", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
h3cMpm = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51))
h3cMpm.setRevisions(('2005-03-22 00:00',))
if mibBuilder.loadTexts: h3cMpm.setLastUpdated('200503220000Z')
if mibBuilder.loadTexts: h3cMpm.setOrganization('Huawei 3Com Technologies Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cMPMObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1))
h3cMPortGroupLimitMinNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMPortGroupLimitMinNumber.setStatus('current')
h3cMPortGroupLimitMaxNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMPortGroupLimitMaxNumber.setStatus('current')
h3cMPMTable = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2))
h3cMPortGroupJoinTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1), )
if mibBuilder.loadTexts: h3cMPortGroupJoinTable.setStatus('current')
h3cMPortGroupJoinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinVlanID"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinAddressType"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinAddress"))
if mibBuilder.loadTexts: h3cMPortGroupJoinEntry.setStatus('current')
h3cMPortGroupJoinVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMPortGroupJoinVlanID.setStatus('current')
h3cMPortGroupJoinAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cMPortGroupJoinAddressType.setStatus('current')
h3cMPortGroupJoinAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 3), InetAddress())
if mibBuilder.loadTexts: h3cMPortGroupJoinAddress.setStatus('current')
h3cMPortGroupJoinStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortGroupJoinStatus.setStatus('current')
h3cMPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2), )
if mibBuilder.loadTexts: h3cMPortGroupTable.setStatus('current')
h3cMPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupVlanID"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupAddressType"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupAddress"))
if mibBuilder.loadTexts: h3cMPortGroupEntry.setStatus('current')
h3cMPortGroupVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMPortGroupVlanID.setStatus('current')
h3cMPortGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMPortGroupAddressType.setStatus('current')
h3cMPortGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMPortGroupAddress.setStatus('current')
h3cMPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3), )
if mibBuilder.loadTexts: h3cMPortConfigTable.setStatus('current')
h3cMPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortConfigVlanID"))
if mibBuilder.loadTexts: h3cMPortConfigEntry.setStatus('current')
h3cMPortConfigVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMPortConfigVlanID.setStatus('current')
h3cMPortGroupLimitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortGroupLimitNumber.setStatus('current')
h3cMPortFastLeaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 3), EnabledStatus().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortFastLeaveStatus.setStatus('current')
h3cMPortGroupPolicyParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortGroupPolicyParameter.setStatus('current')
h3cMPortConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortConfigRowStatus.setStatus('current')
h3cMPortGroupLimitReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 6), EnabledStatus().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMPortGroupLimitReplace.setStatus('current')
h3cHostStaticJoinTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4), )
if mibBuilder.loadTexts: h3cHostStaticJoinTable.setStatus('current')
h3cHostStaticJoinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinVlanID"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinAddressType"), (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinAddress"))
if mibBuilder.loadTexts: h3cHostStaticJoinEntry.setStatus('current')
h3cHostStaticJoinVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cHostStaticJoinVlanID.setStatus('current')
h3cHostStaticJoinAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cHostStaticJoinAddressType.setStatus('current')
h3cHostStaticJoinAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 3), InetAddress())
if mibBuilder.loadTexts: h3cHostStaticJoinAddress.setStatus('current')
h3cHostStaticJoinStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cHostStaticJoinStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-MPM-MIB", h3cMPortGroupJoinStatus=h3cMPortGroupJoinStatus, h3cMPortGroupJoinVlanID=h3cMPortGroupJoinVlanID, h3cMPortGroupLimitMaxNumber=h3cMPortGroupLimitMaxNumber, h3cHostStaticJoinStatus=h3cHostStaticJoinStatus, h3cMPortGroupTable=h3cMPortGroupTable, h3cMPortGroupLimitReplace=h3cMPortGroupLimitReplace, h3cMPortGroupJoinTable=h3cMPortGroupJoinTable, h3cMPortGroupAddressType=h3cMPortGroupAddressType, h3cMPortGroupAddress=h3cMPortGroupAddress, h3cMPMObject=h3cMPMObject, h3cMPortConfigEntry=h3cMPortConfigEntry, h3cMPortGroupLimitNumber=h3cMPortGroupLimitNumber, h3cHostStaticJoinAddressType=h3cHostStaticJoinAddressType, PYSNMP_MODULE_ID=h3cMpm, h3cMPortGroupJoinAddress=h3cMPortGroupJoinAddress, h3cHostStaticJoinTable=h3cHostStaticJoinTable, h3cMPortGroupEntry=h3cMPortGroupEntry, h3cMPortGroupLimitMinNumber=h3cMPortGroupLimitMinNumber, h3cHostStaticJoinVlanID=h3cHostStaticJoinVlanID, h3cMPortGroupJoinEntry=h3cMPortGroupJoinEntry, h3cMPortGroupVlanID=h3cMPortGroupVlanID, h3cHostStaticJoinAddress=h3cHostStaticJoinAddress, h3cMPortConfigVlanID=h3cMPortConfigVlanID, h3cMpm=h3cMpm, h3cMPortGroupPolicyParameter=h3cMPortGroupPolicyParameter, h3cHostStaticJoinEntry=h3cHostStaticJoinEntry, h3cMPMTable=h3cMPMTable, EnabledStatus=EnabledStatus, h3cMPortConfigRowStatus=h3cMPortConfigRowStatus, h3cMPortGroupJoinAddressType=h3cMPortGroupJoinAddressType, h3cMPortFastLeaveStatus=h3cMPortFastLeaveStatus, h3cMPortConfigTable=h3cMPortConfigTable)

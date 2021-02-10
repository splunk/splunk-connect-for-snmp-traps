#
# PySNMP MIB module NMS-IPAcl (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-IPAcl
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Unsigned32, iso, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Bits, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "iso", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Bits", "ModuleIdentity", "Counter32", "IpAddress")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
nmsIPAclMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5))
if mibBuilder.loadTexts: nmsIPAclMIB.setLastUpdated('200811180000Z')
if mibBuilder.loadTexts: nmsIPAclMIB.setOrganization('')
nmsAclTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsAclTotal.setStatus('mandatory')
nmsIPAclTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2), )
if mibBuilder.loadTexts: nmsIPAclTable.setStatus('mandatory')
nmsIPAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1), ).setIndexNames((0, "NMS-IPAcl", "nmsIPAclname"))
if mibBuilder.loadTexts: nmsIPAclEntry.setStatus('mandatory')
nmsIPAclname = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIPAclname.setStatus('mandatory')
nmsIPAclEntrytotal = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIPAclEntrytotal.setStatus('mandatory')
nmsIPAclType = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("standard", 1), ("extended", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclType.setStatus('mandatory')
nmsIPAclMergeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclMergeEnable.setStatus('mandatory')
nmsIPAclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclRowStatus.setStatus('mandatory')
nmsIPAclsRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3), )
if mibBuilder.loadTexts: nmsIPAclsRuleTable.setStatus('mandatory')
nmsIPAclsRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1), ).setIndexNames((0, "NMS-IPAcl", "nmsIPAclsname"), (0, "NMS-IPAcl", "nmsIPAclsentryId"))
if mibBuilder.loadTexts: nmsIPAclsRuleEntry.setStatus('mandatory')
nmsIPAclsname = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIPAclsname.setStatus('current')
nmsIPAclsentryId = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclsentryId.setStatus('current')
nmsIPAclsrule = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("permit", 1), ("deny", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclsrule.setStatus('mandatory')
nmsIPAclssrcip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclssrcip.setStatus('current')
nmsIPAclssrcmask = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclssrcmask.setStatus('current')
nmsIPAclssrcbeginip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclssrcbeginip.setStatus('current')
nmsIPAclssrcendip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclssrcendip.setStatus('current')
nmsIPAclscompare = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usemask", 1), ("userange", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclscompare.setStatus('current')
nmsIPAclsany = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("usezero", 1), ("useany", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclsany.setStatus('current')
nmsIPAclslog = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclslog.setStatus('current')
nmsIPAclsrowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclsrowstatus.setStatus('current')
nmsIPAcleRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4), )
if mibBuilder.loadTexts: nmsIPAcleRuleTable.setStatus('mandatory')
nmsIPAcleRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1), ).setIndexNames((0, "NMS-IPAcl", "nmsIPAclename"), (0, "NMS-IPAcl", "nmsIPAcleentryId"))
if mibBuilder.loadTexts: nmsIPAcleRuleEntry.setStatus('mandatory')
nmsIPAclename = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsIPAclename.setStatus('current')
nmsIPAcleentryId = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleentryId.setStatus('current')
nmsIPAclerule = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("permit", 1), ("deny", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclerule.setStatus('mandatory')
nmsIPAcleprotocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleprotocol.setStatus('current')
nmsIPAclesrceid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrceid.setStatus('current')
nmsIPAclesrcip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcip.setStatus('current')
nmsIPAclesrcmask = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcmask.setStatus('current')
nmsIPAclesrcport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcport.setStatus('current')
nmsIPAclesrcpflag = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("gt", 1), ("lt", 2), ("eq", 3), ("neq", 4), ("range", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcpflag.setStatus('current')
nmsIPAclesrcbeginip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcbeginip.setStatus('current')
nmsIPAclesrcendip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcendip.setStatus('current')
nmsIPAclesrcbeginport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcbeginport.setStatus('current')
nmsIPAclesrcendport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcendport.setStatus('current')
nmsIPAclesrccompare = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usemask", 1), ("userange", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrccompare.setStatus('current')
nmsIPAclesrcany = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("usezero", 1), ("useany", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclesrcany.setStatus('current')
nmsIPAcledeseid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledeseid.setStatus('current')
nmsIPAcledesip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesip.setStatus('current')
nmsIPAcledesmask = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesmask.setStatus('current')
nmsIPAcledesport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesport.setStatus('current')
nmsIPAcledespflag = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("gt", 1), ("lt", 2), ("eq", 3), ("neq", 4), ("range", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledespflag.setStatus('current')
nmsIPAcledesbeginip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesbeginip.setStatus('current')
nmsIPAcledesendip = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 22), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesendip.setStatus('current')
nmsIPAcledesbeginport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesbeginport.setStatus('current')
nmsIPAcledesendport = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesendport.setStatus('current')
nmsIPAcledescompare = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usemask", 1), ("userange", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledescompare.setStatus('current')
nmsIPAcledesany = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("usezero", 1), ("useany", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledesany.setStatus('current')
nmsIPAcleicmptype = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleicmptype.setStatus('mandatory')
nmsIPAcleigmptype = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleigmptype.setStatus('current')
nmsIPAcletimerange = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 29), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcletimerange.setStatus('current')
nmsIPAcletos = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 30), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcletos.setStatus('current')
nmsIPAcleprecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleprecedence.setStatus('current')
nmsIPAcleestablished = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("yes", 1), ("no", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleestablished.setStatus('current')
nmsIPAclelog = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclelog.setStatus('current')
nmsIPAcledonotfragment = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1, 0))).clone(namedValues=NamedValues(("notset", 2), ("set", 1), ("donotcheck", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcledonotfragment.setStatus('current')
nmsIPAcleisfragment = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1, 0))).clone(namedValues=NamedValues(("notset", 2), ("set", 1), ("donotcheck", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcleisfragment.setStatus('current')
nmsIPAcletotallen = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcletotallen.setStatus('current')
nmsIPAcletotallenflag = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("donotcheck", 0), ("gt", 1), ("lt", 2), ("eq", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAcletotallenflag.setStatus('current')
nmsIPAclettl = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclettl.setStatus('current')
nmsIPAclettlflag = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("donotcheck", 0), ("gt", 1), ("lt", 2), ("eq", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclettlflag.setStatus('current')
nmsIPAclerowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 40), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsIPAclerowstatus.setStatus('current')
mibBuilder.exportSymbols("NMS-IPAcl", nmsIPAclssrcip=nmsIPAclssrcip, nmsIPAclesrcpflag=nmsIPAclesrcpflag, nmsIPAcleestablished=nmsIPAcleestablished, nmsIPAclesrcport=nmsIPAclesrcport, nmsIPAclerowstatus=nmsIPAclerowstatus, nmsIPAcleisfragment=nmsIPAcleisfragment, nmsIPAclname=nmsIPAclname, nmsIPAclename=nmsIPAclename, nmsIPAclTable=nmsIPAclTable, nmsIPAclssrcmask=nmsIPAclssrcmask, nmsIPAclslog=nmsIPAclslog, nmsIPAclMergeEnable=nmsIPAclMergeEnable, nmsIPAclEntry=nmsIPAclEntry, nmsIPAclsentryId=nmsIPAclsentryId, nmsIPAclsrule=nmsIPAclsrule, nmsIPAclsrowstatus=nmsIPAclsrowstatus, nmsIPAcleRuleTable=nmsIPAcleRuleTable, nmsIPAcleRuleEntry=nmsIPAcleRuleEntry, nmsIPAclesrcmask=nmsIPAclesrcmask, nmsIPAcledesmask=nmsIPAcledesmask, nmsIPAclType=nmsIPAclType, nmsIPAclEntrytotal=nmsIPAclEntrytotal, nmsIPAcleigmptype=nmsIPAcleigmptype, nmsIPAclMIB=nmsIPAclMIB, nmsIPAcletos=nmsIPAcletos, nmsIPAclelog=nmsIPAclelog, nmsIPAcleentryId=nmsIPAcleentryId, nmsIPAclRowStatus=nmsIPAclRowStatus, nmsIPAcledesport=nmsIPAcledesport, nmsIPAcleicmptype=nmsIPAcleicmptype, nmsIPAclscompare=nmsIPAclscompare, nmsIPAclsRuleEntry=nmsIPAclsRuleEntry, nmsIPAcledescompare=nmsIPAcledescompare, nmsIPAcledesbeginip=nmsIPAcledesbeginip, nmsIPAcledesendip=nmsIPAcledesendip, nmsIPAcletotallenflag=nmsIPAcletotallenflag, nmsIPAcletimerange=nmsIPAcletimerange, nmsIPAclsRuleTable=nmsIPAclsRuleTable, nmsIPAclettl=nmsIPAclettl, nmsIPAclsany=nmsIPAclsany, nmsIPAclesrccompare=nmsIPAclesrccompare, nmsIPAclesrcendip=nmsIPAclesrcendip, nmsIPAclssrcendip=nmsIPAclssrcendip, nmsIPAcledonotfragment=nmsIPAcledonotfragment, nmsIPAcleprotocol=nmsIPAcleprotocol, nmsIPAcleprecedence=nmsIPAcleprecedence, nmsIPAclesrcbeginip=nmsIPAclesrcbeginip, nmsIPAclsname=nmsIPAclsname, nmsIPAcletotallen=nmsIPAcletotallen, nmsIPAclesrcip=nmsIPAclesrcip, nmsIPAclesrcbeginport=nmsIPAclesrcbeginport, nmsIPAcledesbeginport=nmsIPAcledesbeginport, nmsAclTotal=nmsAclTotal, nmsIPAcledesany=nmsIPAcledesany, nmsIPAclssrcbeginip=nmsIPAclssrcbeginip, PYSNMP_MODULE_ID=nmsIPAclMIB, nmsIPAclesrcany=nmsIPAclesrcany, nmsIPAcledesip=nmsIPAcledesip, nmsIPAcledesendport=nmsIPAcledesendport, nmsIPAcledeseid=nmsIPAcledeseid, nmsIPAclerule=nmsIPAclerule, nmsIPAclettlflag=nmsIPAclettlflag, nmsIPAcledespflag=nmsIPAcledespflag, nmsIPAclesrcendport=nmsIPAclesrcendport, nmsIPAclesrceid=nmsIPAclesrceid)

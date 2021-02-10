#
# PySNMP MIB module DEPNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEPNODE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:23:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Bits, ObjectIdentity, Gauge32, TimeTicks, Integer32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, iso, IpAddress, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Bits", "ObjectIdentity", "Gauge32", "TimeTicks", "Integer32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "iso", "IpAddress", "enterprises", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibmSP = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 117))
ibmSPDepNode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 117, 4))
ibmSPDepNodeTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1), )
if mibBuilder.loadTexts: ibmSPDepNodeTable.setStatus('mandatory')
ibmSPDepNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1), ).setIndexNames((0, "DEPNODE-MIB", "ibmSPDepNodeName"))
if mibBuilder.loadTexts: ibmSPDepNodeEntry.setStatus('mandatory')
ibmSPDepNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmSPDepNodeName.setStatus('mandatory')
ibmSPDepNodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepNodeNumber.setStatus('mandatory')
ibmSPDepSwToken = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepSwToken.setStatus('mandatory')
ibmSPDepSwARP = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepSwARP.setStatus('mandatory')
ibmSPDepSwNodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepSwNodeNumber.setStatus('mandatory')
ibmSPDepIPaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepIPaddr.setStatus('mandatory')
ibmSPDepNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepNetMask.setStatus('mandatory')
ibmSPDepIPMaxLinkPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepIPMaxLinkPkt.setStatus('mandatory')
ibmSPDepIPHostOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepIPHostOffset.setStatus('mandatory')
ibmSPDepConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notConfigured", 1), ("firmwareLoadFailed", 2), ("driverLoadFailed", 3), ("diagnosticFailed", 4), ("microcodeLoadFailed", 5), ("fullyConfigured", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmSPDepConfigState.setStatus('mandatory')
ibmSPDepSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepSysName.setStatus('mandatory')
ibmSPDepNodeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nodeUp", 1), ("nodeDown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmSPDepNodeState.setStatus('mandatory')
ibmSPDepSwChipLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepSwChipLink.setStatus('mandatory')
ibmSPDepNodeDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepNodeDelay.setStatus('mandatory')
ibmSPDepAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("reconfigure", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmSPDepAdminStatus.setStatus('mandatory')
switchInfoNeeded = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 117, 4) + (0,1)).setObjects(("DEPNODE-MIB", "ibmSPDepNodeName"))
switchConfigState = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 117, 4) + (0,2)).setObjects(("DEPNODE-MIB", "ibmSPDepConfigState"))
switchNodeUp = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 117, 4) + (0,3)).setObjects(("DEPNODE-MIB", "ibmSPDepNodeName"))
switchNodeDown = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 117, 4) + (0,4)).setObjects(("DEPNODE-MIB", "ibmSPDepNodeName"))
mibBuilder.exportSymbols("DEPNODE-MIB", ibmSPDepNodeNumber=ibmSPDepNodeNumber, ibmSPDepAdminStatus=ibmSPDepAdminStatus, ibm=ibm, ibmSPDepNetMask=ibmSPDepNetMask, ibmProd=ibmProd, switchNodeDown=switchNodeDown, switchNodeUp=switchNodeUp, ibmSPDepNode=ibmSPDepNode, switchConfigState=switchConfigState, ibmSPDepConfigState=ibmSPDepConfigState, ibmSPDepSysName=ibmSPDepSysName, ibmSPDepNodeDelay=ibmSPDepNodeDelay, ibmSPDepSwToken=ibmSPDepSwToken, ibmSPDepSwNodeNumber=ibmSPDepSwNodeNumber, ibmSPDepSwChipLink=ibmSPDepSwChipLink, ibmSPDepNodeState=ibmSPDepNodeState, ibmSPDepIPaddr=ibmSPDepIPaddr, ibmSP=ibmSP, switchInfoNeeded=switchInfoNeeded, ibmSPDepNodeName=ibmSPDepNodeName, ibmSPDepSwARP=ibmSPDepSwARP, ibmSPDepNodeTable=ibmSPDepNodeTable, ibmSPDepIPHostOffset=ibmSPDepIPHostOffset, ibmSPDepIPMaxLinkPkt=ibmSPDepIPMaxLinkPkt, ibmSPDepNodeEntry=ibmSPDepNodeEntry)

#
# PySNMP MIB module ADTRAN-ATLAS-550-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-550-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, iso, Counter32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, IpAddress, Integer32, Gauge32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "IpAddress", "Integer32", "Gauge32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLAS550mg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219))
adATLAS550Fpnl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1))
adATLAS550FpnlSysLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1))
adATLAS550FpnlPow = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("syson", 1), ("sysoff", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlPow.setStatus('mandatory')
adATLAS550FpnlSys = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sysok", 1), ("syserr", 2), ("syswarn", 3), ("sysflashupdate", 4), ("sysflasherror", 5), ("sysoff", 6), ("greenslow", 7), ("yellowslow", 8), ("yellowfast", 9), ("redslow", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlSys.setStatus('mandatory')
adATLAS550FpnlEth = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("etheron", 1), ("etheroff", 2), ("etherflashslow", 3), ("etherflashfast", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlEth.setStatus('mandatory')
adATLAS550FpnlRem = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("remon", 1), ("remoff", 2), ("remflashslow", 3), ("remflashfast", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlRem.setStatus('mandatory')
adATLAS550FpnlNtwkLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2))
adATLAS550FpnlNwTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1), )
if mibBuilder.loadTexts: adATLAS550FpnlNwTable.setStatus('mandatory')
adATLAS550FpnlNwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlNwIndex"))
if mibBuilder.loadTexts: adATLAS550FpnlNwEntry.setStatus('mandatory')
adATLAS550FpnlNwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwIndex.setStatus('mandatory')
adATLAS550FpnlNwOK = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nwokon", 1), ("nwokflashslow", 2), ("nwokflashfast", 3), ("nwokoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwOK.setStatus('mandatory')
adATLAS550FpnlNwTest = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("teston", 1), ("testflashslow", 2), ("testflashfast", 3), ("testoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwTest.setStatus('mandatory')
adATLAS550FpnlNwError = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("erroron", 1), ("errorflashslow", 2), ("errorflashfast", 3), ("erroroff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwError.setStatus('mandatory')
adATLAS550FpnlNwAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("alarmon", 1), ("alarmflashslow", 2), ("alarmflashfast", 3), ("alarmoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwAlarm.setStatus('mandatory')
adATLAS550FpnlModLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3))
adATLAS550FpnlModNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlModNumber.setStatus('mandatory')
adATLAS550FpnlMLTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2), )
if mibBuilder.loadTexts: adATLAS550FpnlMLTable.setStatus('mandatory')
adATLAS550FpnlMLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlMLIndex"))
if mibBuilder.loadTexts: adATLAS550FpnlMLEntry.setStatus('mandatory')
adATLAS550FpnlMLIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLIndex.setStatus('mandatory')
adATLAS550FpnlMLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("mlstatusok", 1), ("mlstatuswarn", 2), ("mlstatuserr", 3), ("mlstatusflashslowgreen", 4), ("mlstatusflashfastgreen", 5), ("mlstatusflashslowyellow", 6), ("mlstatusflashfastyellow", 7), ("mlstatusflashslowred", 8), ("mlstatusflashfastred", 9), ("mlstatusoff", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLStatus.setStatus('mandatory')
adATLAS550FpnlMLOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("mlonlineon", 1), ("mlonlineflashslow", 2), ("mlonlineflashfast", 3), ("mlonlineoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLOnline.setStatus('mandatory')
adATLAS550FpnlMLTest = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mlteston", 1), ("mltestflash", 2), ("mltestoff", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLTest.setStatus('mandatory')
adATLAS550ExtAlarmActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 219) + (0,21900))
adATLAS550ExtAlarmInactive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 219) + (0,21901))
mibBuilder.exportSymbols("ADTRAN-ATLAS-550-MIB", adATLAS550FpnlNtwkLeds=adATLAS550FpnlNtwkLeds, adATLAS550FpnlMLTest=adATLAS550FpnlMLTest, adATLAS550FpnlNwIndex=adATLAS550FpnlNwIndex, adATLAS550FpnlMLEntry=adATLAS550FpnlMLEntry, adATLAS550FpnlMLIndex=adATLAS550FpnlMLIndex, adATLAS550FpnlMLOnline=adATLAS550FpnlMLOnline, adATLAS550FpnlNwEntry=adATLAS550FpnlNwEntry, adATLAS550FpnlNwError=adATLAS550FpnlNwError, adATLAS550FpnlMLStatus=adATLAS550FpnlMLStatus, adATLAS550FpnlNwTest=adATLAS550FpnlNwTest, adATLAS550ExtAlarmActive=adATLAS550ExtAlarmActive, adATLAS550ExtAlarmInactive=adATLAS550ExtAlarmInactive, adATLAS550FpnlModLeds=adATLAS550FpnlModLeds, adATLAS550mg=adATLAS550mg, adtran=adtran, adMgmt=adMgmt, adATLAS550FpnlSys=adATLAS550FpnlSys, adATLAS550FpnlModNumber=adATLAS550FpnlModNumber, adATLAS550FpnlMLTable=adATLAS550FpnlMLTable, adATLAS550FpnlEth=adATLAS550FpnlEth, adATLAS550FpnlSysLeds=adATLAS550FpnlSysLeds, adATLAS550Fpnl=adATLAS550Fpnl, adATLAS550FpnlPow=adATLAS550FpnlPow, adATLAS550FpnlNwTable=adATLAS550FpnlNwTable, adATLAS550FpnlNwAlarm=adATLAS550FpnlNwAlarm, adATLAS550FpnlNwOK=adATLAS550FpnlNwOK, adATLAS550FpnlRem=adATLAS550FpnlRem)

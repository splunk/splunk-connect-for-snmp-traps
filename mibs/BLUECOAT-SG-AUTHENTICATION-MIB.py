#
# PySNMP MIB module BLUECOAT-SG-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-SG-AUTHENTICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, NotificationType, ModuleIdentity, Integer32, IpAddress, TimeTicks, Unsigned32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "Unsigned32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecoatSGAuthentication = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 15))
bluecoatSGAuthentication.setRevisions(('2014-08-06 03:00',))
if mibBuilder.loadTexts: bluecoatSGAuthentication.setLastUpdated('201408060300Z')
if mibBuilder.loadTexts: bluecoatSGAuthentication.setOrganization('Blue Coat Systems, Inc.')
class ToggleState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

schannelStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2))
lsaDomainControllerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3))
schannelServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4))
authNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5))
authNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0))
schannelStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1), )
if mibBuilder.loadTexts: schannelStatsTable.setStatus('current')
schannelStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelStatsIndex"))
if mibBuilder.loadTexts: schannelStatsEntry.setStatus('current')
schannelStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: schannelStatsIndex.setStatus('current')
domainName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainName.setStatus('current')
domainStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainStatus.setStatus('current')
timeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 4), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: timeouts.setStatus('current')
transactions = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 5), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: transactions.setStatus('current')
currentWaiters = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 6), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: currentWaiters.setStatus('current')
maxWaiters = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 7), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxWaiters.setStatus('current')
resets = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: resets.setStatus('current')
lsaDomainControllerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1), )
if mibBuilder.loadTexts: lsaDomainControllerStatsTable.setStatus('current')
lsaDomainControllerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "lsaDomainControllerStatsIndex"))
if mibBuilder.loadTexts: lsaDomainControllerStatsEntry.setStatus('current')
lsaDomainControllerStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lsaDomainControllerStatsIndex.setStatus('current')
domainControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domainControllerName.setStatus('current')
address = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: address.setStatus('current')
siteName = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: siteName.setStatus('current')
avgLDAPPingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLDAPPingTime.setStatus('current')
lastLDAPPingTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLDAPPingTime.setStatus('current')
flags = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flags.setStatus('current')
schannelServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1), )
if mibBuilder.loadTexts: schannelServerStatsTable.setStatus('current')
schannelServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelServerStatsIndex"))
if mibBuilder.loadTexts: schannelServerStatsEntry.setStatus('current')
schannelServerStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: schannelServerStatsIndex.setStatus('current')
serverName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverName.setStatus('current')
connectionsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsInUse.setStatus('current')
availableConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availableConnections.setStatus('current')
averageTransactions = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: averageTransactions.setStatus('current')
authsByDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 6), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast1Minute.setStatus('current')
authsByDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 7), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast3Minutes.setStatus('current')
authsByDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast5Minutes.setStatus('current')
authsByDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 9), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast15Minutes.setStatus('current')
authsByDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 10), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: authsByDomainLast60Minutes.setStatus('current')
failedAuthsByDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 11), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast1Minute.setStatus('current')
failedAuthsByDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 12), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast3Minutes.setStatus('current')
failedAuthsByDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 13), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast5Minutes.setStatus('current')
failedAuthsByDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 14), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast15Minutes.setStatus('current')
failedAuthsByDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 15), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: failedAuthsByDomainLast60Minutes.setStatus('current')
avgLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 16), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast1Minute.setStatus('current')
avgLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 17), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast3Minutes.setStatus('current')
avgLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 18), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast5Minutes.setStatus('current')
avgLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 19), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast15Minutes.setStatus('current')
avgLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 20), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: avgLatencyPerDomainLast60Minutes.setStatus('current')
maxLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 21), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast1Minute.setStatus('current')
maxLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 22), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast3Minutes.setStatus('current')
maxLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 23), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast5Minutes.setStatus('current')
maxLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 24), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast15Minutes.setStatus('current')
maxLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 25), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLatencyPerDomainLast60Minutes.setStatus('current')
minLatencyPerDomainLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 26), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast1Minute.setStatus('current')
minLatencyPerDomainLast3Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 27), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast3Minutes.setStatus('current')
minLatencyPerDomainLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 28), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast5Minutes.setStatus('current')
minLatencyPerDomainLast15Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 29), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast15Minutes.setStatus('current')
minLatencyPerDomainLast60Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 30), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: minLatencyPerDomainLast60Minutes.setStatus('current')
schannelLatencyTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0, 1)).setObjects(("BLUECOAT-SG-AUTHENTICATION-MIB", "domainName"), ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyType"), ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyValue"))
if mibBuilder.loadTexts: schannelLatencyTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-AUTHENTICATION-MIB", authsByDomainLast3Minutes=authsByDomainLast3Minutes, transactions=transactions, siteName=siteName, avgLatencyPerDomainLast15Minutes=avgLatencyPerDomainLast15Minutes, lsaDomainControllerStatsIndex=lsaDomainControllerStatsIndex, resets=resets, address=address, schannelStatsIndex=schannelStatsIndex, maxWaiters=maxWaiters, authsByDomainLast15Minutes=authsByDomainLast15Minutes, maxLatencyPerDomainLast1Minute=maxLatencyPerDomainLast1Minute, schannelStats=schannelStats, availableConnections=availableConnections, currentWaiters=currentWaiters, schannelLatencyTrap=schannelLatencyTrap, domainName=domainName, bluecoatSGAuthentication=bluecoatSGAuthentication, domainStatus=domainStatus, serverName=serverName, PYSNMP_MODULE_ID=bluecoatSGAuthentication, connectionsInUse=connectionsInUse, schannelStatsEntry=schannelStatsEntry, authsByDomainLast5Minutes=authsByDomainLast5Minutes, lsaDomainControllerStatsTable=lsaDomainControllerStatsTable, minLatencyPerDomainLast1Minute=minLatencyPerDomainLast1Minute, minLatencyPerDomainLast5Minutes=minLatencyPerDomainLast5Minutes, authNotificationsPrefix=authNotificationsPrefix, lsaDomainControllerStatsEntry=lsaDomainControllerStatsEntry, authsByDomainLast60Minutes=authsByDomainLast60Minutes, flags=flags, avgLatencyPerDomainLast5Minutes=avgLatencyPerDomainLast5Minutes, domainControllerName=domainControllerName, schannelServerStatsTable=schannelServerStatsTable, minLatencyPerDomainLast3Minutes=minLatencyPerDomainLast3Minutes, failedAuthsByDomainLast5Minutes=failedAuthsByDomainLast5Minutes, maxLatencyPerDomainLast3Minutes=maxLatencyPerDomainLast3Minutes, schannelStatsTable=schannelStatsTable, maxLatencyPerDomainLast15Minutes=maxLatencyPerDomainLast15Minutes, minLatencyPerDomainLast15Minutes=minLatencyPerDomainLast15Minutes, lsaDomainControllerStats=lsaDomainControllerStats, averageTransactions=averageTransactions, minLatencyPerDomainLast60Minutes=minLatencyPerDomainLast60Minutes, avgLatencyPerDomainLast60Minutes=avgLatencyPerDomainLast60Minutes, avgLatencyPerDomainLast1Minute=avgLatencyPerDomainLast1Minute, failedAuthsByDomainLast15Minutes=failedAuthsByDomainLast15Minutes, failedAuthsByDomainLast1Minute=failedAuthsByDomainLast1Minute, failedAuthsByDomainLast60Minutes=failedAuthsByDomainLast60Minutes, authNotifications=authNotifications, failedAuthsByDomainLast3Minutes=failedAuthsByDomainLast3Minutes, ToggleState=ToggleState, timeouts=timeouts, schannelServerStatsIndex=schannelServerStatsIndex, avgLatencyPerDomainLast3Minutes=avgLatencyPerDomainLast3Minutes, maxLatencyPerDomainLast5Minutes=maxLatencyPerDomainLast5Minutes, avgLDAPPingTime=avgLDAPPingTime, authsByDomainLast1Minute=authsByDomainLast1Minute, maxLatencyPerDomainLast60Minutes=maxLatencyPerDomainLast60Minutes, lastLDAPPingTime=lastLDAPPingTime, schannelServerStats=schannelServerStats, schannelServerStatsEntry=schannelServerStatsEntry)

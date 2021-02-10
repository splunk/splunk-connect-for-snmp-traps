#
# PySNMP MIB module HP-SN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
snChasFanDescription, snChasFanIndex, snChasPwrSupplyIndex, snAgentBrdIndex, snChasPwrSupplyDescription, snAgGblTrapMessage, snChasPwrSupplyStatus = mibBuilder.importSymbols("HP-SN-AGENT-MIB", "snChasFanDescription", "snChasFanIndex", "snChasPwrSupplyIndex", "snAgentBrdIndex", "snChasPwrSupplyDescription", "snAgGblTrapMessage", "snChasPwrSupplyStatus")
hp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "hp")
snL4TcpSynLimit, snL4TrapRealServerCurConnections, snL4TrapRealServerIP, snL4MaxSessionLimit, snL4TrapRealServerPort, snL4TrapRealServerName = mibBuilder.importSymbols("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit", "snL4TrapRealServerCurConnections", "snL4TrapRealServerIP", "snL4MaxSessionLimit", "snL4TrapRealServerPort", "snL4TrapRealServerName")
snSwViolatorPortNumber, snSwViolatorMacAddress = mibBuilder.importSymbols("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber", "snSwViolatorMacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Integer32, Counter32, Counter64, iso, Bits, NotificationType, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Counter32", "Counter64", "iso", "Bits", "NotificationType", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snTrapChasPwrSupply = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,1)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyStatus"))
snTrapLockedAddressViolation = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,2)).setObjects(("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber"), ("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress"))
snTrapL4MaxSessionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,19)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit"))
snTrapL4TcpSynLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,20)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit"))
snTrapL4RealServerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,21)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
snTrapL4RealServerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,22)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
snTrapL4RealServerPortUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,23)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
snTrapL4RealServerPortDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,24)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
snTrapL4RealServerMaxConnectionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,25)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
snTrapL4BecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,26))
snTrapL4BecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,27))
snTrapModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,28)).setObjects(("HP-SN-AGENT-MIB", "snAgentBrdIndex"))
snTrapModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,29)).setObjects(("HP-SN-AGENT-MIB", "snAgentBrdIndex"))
snTrapChasPwrSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,30)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"), ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
snTrapChasFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,31)).setObjects(("HP-SN-AGENT-MIB", "snChasFanIndex"), ("HP-SN-AGENT-MIB", "snChasFanDescription"))
snTrapLockedAddressViolation2 = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,32)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapFsrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,33)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapVrrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,34)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMgmtModuleRedunStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,35)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,36)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapAccessListDeny = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,37)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMacFilterDeny = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,38)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,39)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,40)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteControllerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,41)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteControllerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,42)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,43)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,44)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpPortUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,45)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpPortDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,46)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4FirewallBecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,47))
snTrapL4FirewallBecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,48))
snTrapL4FirewallPathUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,49))
snTrapL4FirewallPathDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,50))
snTrapIcmpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,51)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapIcmpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,52)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTcpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,53)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTcpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,54)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ContentVerification = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,55))
snTrapDuplicateIp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,56))
snTrapMplsProblem = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,57))
snTrapMplsException = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,58))
snTrapMplsAudit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,59))
snTrapMplsDeveloper = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,60))
snTrapNoBmFreeQueue = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,61)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapSmcDmaDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,62)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapSmcBpDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,63)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBmWriteSeqDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,64)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBgpPeerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,65)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBgpPeerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,66)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4RealServerResponseTimeLowerLimit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,67)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4RealServerResponseTimeUpperLimit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,68)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4TcpAttackRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,69)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4TcpAttackRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,70)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ConnectionRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,71)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ConnectionRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,72)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,73)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapStartupConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,74)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,75)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapUserLogout = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,76)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,77)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapPortSecurityShutdown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,78)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMrpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,79)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMrpCamError = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,80)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapChasPwrSupplyOK = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,81)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"), ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
snTrapVrrpeIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,82)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapVsrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,83)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
mibBuilder.exportSymbols("HP-SN-TRAP-MIB", snTrapL4FirewallPathDown=snTrapL4FirewallPathDown, snTrapL4FirewallBecomeStandby=snTrapL4FirewallBecomeStandby, snTrapNoBmFreeQueue=snTrapNoBmFreeQueue, snTrapPortSecurityShutdown=snTrapPortSecurityShutdown, snTrapL4GslbHealthCheckIpPortDown=snTrapL4GslbHealthCheckIpPortDown, snTrapL4GslbHealthCheckIpPortUp=snTrapL4GslbHealthCheckIpPortUp, snTrapAccessListDeny=snTrapAccessListDeny, snTrapLockedAddressViolation=snTrapLockedAddressViolation, snTrapL4RealServerUp=snTrapL4RealServerUp, snTrapL4RealServerResponseTimeUpperLimit=snTrapL4RealServerResponseTimeUpperLimit, snTrapMplsAudit=snTrapMplsAudit, snTrapL4GslbHealthCheckIpDown=snTrapL4GslbHealthCheckIpDown, snTrapL4GslbRemoteUp=snTrapL4GslbRemoteUp, snTrapL4RealServerPortDown=snTrapL4RealServerPortDown, snTrapIcmpLocalExceedBurst=snTrapIcmpLocalExceedBurst, snTrapTemperatureWarning=snTrapTemperatureWarning, snTrapMrpCamError=snTrapMrpCamError, snTrapTcpTransitExceedBurst=snTrapTcpTransitExceedBurst, snTrapUserLogin=snTrapUserLogin, snTrapSmcBpDrop=snTrapSmcBpDrop, snTrapMplsProblem=snTrapMplsProblem, snTrapL4RealServerDown=snTrapL4RealServerDown, snTrapL4BecomeActive=snTrapL4BecomeActive, snTrapL4RealServerPortUp=snTrapL4RealServerPortUp, snTrapLockedAddressViolation2=snTrapLockedAddressViolation2, snTrapL4TcpAttackRateExceedMax=snTrapL4TcpAttackRateExceedMax, snTrapL4ConnectionRateExceedMax=snTrapL4ConnectionRateExceedMax, snTrapFsrpIfStateChange=snTrapFsrpIfStateChange, snTrapL4GslbRemoteDown=snTrapL4GslbRemoteDown, snTrapL4ConnectionRateExceedThreshold=snTrapL4ConnectionRateExceedThreshold, snTrapPortSecurityViolation=snTrapPortSecurityViolation, snTrapDuplicateIp=snTrapDuplicateIp, snTrapIcmpTransitExceedBurst=snTrapIcmpTransitExceedBurst, snTrapL4ContentVerification=snTrapL4ContentVerification, snTrapStartupConfigChanged=snTrapStartupConfigChanged, snTrapL4TcpAttackRateExceedThreshold=snTrapL4TcpAttackRateExceedThreshold, snTrapTcpLocalExceedBurst=snTrapTcpLocalExceedBurst, snTrapRunningConfigChanged=snTrapRunningConfigChanged, snTrapMplsDeveloper=snTrapMplsDeveloper, snTrapChasPwrSupplyFailed=snTrapChasPwrSupplyFailed, snTrapMplsException=snTrapMplsException, snTrapMrpStateChange=snTrapMrpStateChange, snTrapModuleRemoved=snTrapModuleRemoved, snTrapL4GslbHealthCheckIpUp=snTrapL4GslbHealthCheckIpUp, snTrapModuleInserted=snTrapModuleInserted, snTrapL4GslbRemoteControllerDown=snTrapL4GslbRemoteControllerDown, snTrapChasFanFailed=snTrapChasFanFailed, snTrapL4MaxSessionLimitReached=snTrapL4MaxSessionLimitReached, snTrapVrrpeIfStateChange=snTrapVrrpeIfStateChange, snTrapL4RealServerMaxConnectionLimitReached=snTrapL4RealServerMaxConnectionLimitReached, snTrapChasPwrSupply=snTrapChasPwrSupply, snTrapL4FirewallBecomeActive=snTrapL4FirewallBecomeActive, snTrapBgpPeerUp=snTrapBgpPeerUp, snTrapChasPwrSupplyOK=snTrapChasPwrSupplyOK, snTrapL4FirewallPathUp=snTrapL4FirewallPathUp, snTrapVsrpIfStateChange=snTrapVsrpIfStateChange, snTrapL4BecomeStandby=snTrapL4BecomeStandby, snTrapL4GslbRemoteControllerUp=snTrapL4GslbRemoteControllerUp, snTrapBmWriteSeqDrop=snTrapBmWriteSeqDrop, snTrapSmcDmaDrop=snTrapSmcDmaDrop, snTrapMacFilterDeny=snTrapMacFilterDeny, snTrapMgmtModuleRedunStateChange=snTrapMgmtModuleRedunStateChange, snTrapL4TcpSynLimitReached=snTrapL4TcpSynLimitReached, snTrapL4RealServerResponseTimeLowerLimit=snTrapL4RealServerResponseTimeLowerLimit, snTrapBgpPeerDown=snTrapBgpPeerDown, snTrapUserLogout=snTrapUserLogout, snTrapVrrpIfStateChange=snTrapVrrpIfStateChange)
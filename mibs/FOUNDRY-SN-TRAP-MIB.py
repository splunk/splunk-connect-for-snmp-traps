#
# PySNMP MIB module FOUNDRY-SN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
snAgentBrdIndex, snAgGblTrapMessage, snChasPwrSupplyDescription, snChasPwrSupplyIndex, snChasFanDescription, snChasPwrSupplyStatus, snChasFanIndex = mibBuilder.importSymbols("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex", "snAgGblTrapMessage", "snChasPwrSupplyDescription", "snChasPwrSupplyIndex", "snChasFanDescription", "snChasPwrSupplyStatus", "snChasFanIndex")
snOspfRouterId, snOspfNbrIpAddr, snOspfLsdbType, snOspfVirtIfStatusAreaID, snOspfPacketSrc, snOspfVirtNbrArea, snOspfVirtNbrRtrId, snOspfConfigErrorType, snOspfNbrRtrId, snOspfLsdbRouterId, snOspfIfStatusState, snOspfLsdbAreaId, snOspfIfStatusIpAddress, snOspfNbrState, snOspfLsdbLsId, snOspfVirtIfStatusNeighbor, snOspfVirtNbrState, snOspfExtLsdbLimit, snOspfVirtIfStatusState, snOspfPacketType = mibBuilder.importSymbols("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId", "snOspfNbrIpAddr", "snOspfLsdbType", "snOspfVirtIfStatusAreaID", "snOspfPacketSrc", "snOspfVirtNbrArea", "snOspfVirtNbrRtrId", "snOspfConfigErrorType", "snOspfNbrRtrId", "snOspfLsdbRouterId", "snOspfIfStatusState", "snOspfLsdbAreaId", "snOspfIfStatusIpAddress", "snOspfNbrState", "snOspfLsdbLsId", "snOspfVirtIfStatusNeighbor", "snOspfVirtNbrState", "snOspfExtLsdbLimit", "snOspfVirtIfStatusState", "snOspfPacketType")
foundry, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "foundry")
snL4TrapRealServerCurConnections, snL4TrapRealServerIP, snL4TcpSynLimit, snL4TrapRealServerPort, snL4MaxSessionLimit, snL4TrapRealServerName = mibBuilder.importSymbols("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections", "snL4TrapRealServerIP", "snL4TcpSynLimit", "snL4TrapRealServerPort", "snL4MaxSessionLimit", "snL4TrapRealServerName")
snSwViolatorPortNumber, snSwViolatorMacAddress = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber", "snSwViolatorMacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, MibIdentifier, Bits, ModuleIdentity, iso, TimeTicks, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "iso", "TimeTicks", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snTrapChasPwrSupply = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,1)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyStatus"))
snTrapLockedAddressViolation = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,2)).setObjects(("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber"), ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress"))
snTrapOspfIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,3)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusState"))
snTrapOspfVirtIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,4)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusState"))
snOspfNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,5)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrIpAddr"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrState"))
snOspfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,6)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrArea"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrRtrId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrState"))
snOspfIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,7)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,8)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,9)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,10)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,11)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,12)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,13)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
ospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,14)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfOriginateLsa = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,15)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfMaxAgeLsa = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,16)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfLsdbOverflow = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,17)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
snOspfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,18)).setObjects(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
snTrapL4MaxSessionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,19)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit"))
snTrapL4TcpSynLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,20)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit"))
snTrapL4RealServerUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,21)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
snTrapL4RealServerDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,22)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
snTrapL4RealServerPortUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,23)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
snTrapL4RealServerPortDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,24)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
snTrapL4RealServerMaxConnectionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,25)).setObjects(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
snTrapL4BecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,26))
snTrapL4BecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,27))
snTrapModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,28)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"))
snTrapModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,29)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"))
snTrapChasPwrSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,30)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"), ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
snTrapChasFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,31)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"), ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
snTrapLockedAddressViolation2 = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,32)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapFsrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,33)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapVrrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,34)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMgmtModuleRedunStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,35)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,36)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapAccessListDeny = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,37)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapMacFilterDeny = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,38)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,39)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,40)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteControllerUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,41)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbRemoteControllerDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,42)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,43)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,44)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpPortUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,45)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4GslbHealthCheckIpPortDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,46)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4FirewallBecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,47))
snTrapL4FirewallBecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,48))
snTrapL4FirewallPathUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,49))
snTrapL4FirewallPathDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,50))
snTrapIcmpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,51)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapIcmpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,52)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTcpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,53)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapTcpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,54)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ContentVerification = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,55))
snTrapDuplicateIp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,56))
snTrapMplsProblem = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,57))
snTrapMplsException = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,58))
snTrapMplsAudit = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,59))
snTrapMplsDeveloper = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,60))
snTrapNoBmFreeQueue = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,61)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapSmcDmaDrop = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,62)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapSmcBpDrop = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,63)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBmWriteSeqDrop = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,64)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBgpPeerUp = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,65)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapBgpPeerDown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,66)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4RealServerResponseTimeLowerLimit = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,67)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4RealServerResponseTimeUpperLimit = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,68)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4TcpAttackRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,69)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4TcpAttackRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,70)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ConnectionRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,71)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapL4ConnectionRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,72)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,73)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapStartupConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,74)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,75)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapUserLogout = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,76)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,77)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
snTrapPortSecurityShutdown = NotificationType((1, 3, 6, 1, 4, 1, 1991) + (0,78)).setObjects(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
mibBuilder.exportSymbols("FOUNDRY-SN-TRAP-MIB", snOspfOriginateLsa=snOspfOriginateLsa, snOspfIfRxBadPacket=snOspfIfRxBadPacket, snTrapL4TcpAttackRateExceedMax=snTrapL4TcpAttackRateExceedMax, snTrapL4GslbHealthCheckIpPortDown=snTrapL4GslbHealthCheckIpPortDown, snTrapL4TcpAttackRateExceedThreshold=snTrapL4TcpAttackRateExceedThreshold, snTrapL4BecomeStandby=snTrapL4BecomeStandby, snOspfLsdbApproachingOverflow=snOspfLsdbApproachingOverflow, snTrapMacFilterDeny=snTrapMacFilterDeny, snTrapL4RealServerPortDown=snTrapL4RealServerPortDown, snTrapL4GslbRemoteControllerDown=snTrapL4GslbRemoteControllerDown, snTrapTcpTransitExceedBurst=snTrapTcpTransitExceedBurst, snTrapUserLogout=snTrapUserLogout, snTrapBgpPeerUp=snTrapBgpPeerUp, snOspfIfConfigError=snOspfIfConfigError, snTrapL4GslbHealthCheckIpDown=snTrapL4GslbHealthCheckIpDown, snTrapL4GslbHealthCheckIpUp=snTrapL4GslbHealthCheckIpUp, snOspfVirtIfAuthFailure=snOspfVirtIfAuthFailure, snTrapL4FirewallPathUp=snTrapL4FirewallPathUp, snTrapLockedAddressViolation2=snTrapLockedAddressViolation2, snTrapChasFanFailed=snTrapChasFanFailed, snTrapL4MaxSessionLimitReached=snTrapL4MaxSessionLimitReached, snOspfVirtIfRxBadPacket=snOspfVirtIfRxBadPacket, snOspfVirtIfConfigError=snOspfVirtIfConfigError, snOspfNbrStateChange=snOspfNbrStateChange, snTrapChasPwrSupplyFailed=snTrapChasPwrSupplyFailed, snTrapOspfVirtIfStateChange=snTrapOspfVirtIfStateChange, snTrapLockedAddressViolation=snTrapLockedAddressViolation, snTrapL4FirewallPathDown=snTrapL4FirewallPathDown, snTrapL4RealServerResponseTimeUpperLimit=snTrapL4RealServerResponseTimeUpperLimit, snTrapIcmpTransitExceedBurst=snTrapIcmpTransitExceedBurst, snTrapL4BecomeActive=snTrapL4BecomeActive, snOspfLsdbOverflow=snOspfLsdbOverflow, snTrapTcpLocalExceedBurst=snTrapTcpLocalExceedBurst, snTrapL4RealServerResponseTimeLowerLimit=snTrapL4RealServerResponseTimeLowerLimit, snTrapL4FirewallBecomeActive=snTrapL4FirewallBecomeActive, snTrapL4ConnectionRateExceedThreshold=snTrapL4ConnectionRateExceedThreshold, snTrapDuplicateIp=snTrapDuplicateIp, snTrapL4RealServerMaxConnectionLimitReached=snTrapL4RealServerMaxConnectionLimitReached, snTrapL4GslbRemoteUp=snTrapL4GslbRemoteUp, snOspfMaxAgeLsa=snOspfMaxAgeLsa, snTrapBgpPeerDown=snTrapBgpPeerDown, snTrapPortSecurityShutdown=snTrapPortSecurityShutdown, snTrapTemperatureWarning=snTrapTemperatureWarning, snTrapFsrpIfStateChange=snTrapFsrpIfStateChange, snTrapL4TcpSynLimitReached=snTrapL4TcpSynLimitReached, ospfVirtIfTxRetransmit=ospfVirtIfTxRetransmit, snTrapL4RealServerUp=snTrapL4RealServerUp, snTrapSmcDmaDrop=snTrapSmcDmaDrop, snTrapOspfIfStateChange=snTrapOspfIfStateChange, snTrapVrrpIfStateChange=snTrapVrrpIfStateChange, snOspfIfAuthFailure=snOspfIfAuthFailure, snTrapL4ConnectionRateExceedMax=snTrapL4ConnectionRateExceedMax, snTrapL4GslbRemoteControllerUp=snTrapL4GslbRemoteControllerUp, snTrapL4ContentVerification=snTrapL4ContentVerification, snTrapL4GslbHealthCheckIpPortUp=snTrapL4GslbHealthCheckIpPortUp, snTrapStartupConfigChanged=snTrapStartupConfigChanged, snTrapChasPwrSupply=snTrapChasPwrSupply, snTrapMplsProblem=snTrapMplsProblem, snTrapSmcBpDrop=snTrapSmcBpDrop, snTrapMplsDeveloper=snTrapMplsDeveloper, snOspfTxRetransmit=snOspfTxRetransmit, snTrapMplsAudit=snTrapMplsAudit, snTrapMplsException=snTrapMplsException, snTrapIcmpLocalExceedBurst=snTrapIcmpLocalExceedBurst, snOspfVirtNbrStateChange=snOspfVirtNbrStateChange, snTrapL4GslbRemoteDown=snTrapL4GslbRemoteDown, snTrapAccessListDeny=snTrapAccessListDeny, snTrapPortSecurityViolation=snTrapPortSecurityViolation, snTrapL4RealServerDown=snTrapL4RealServerDown, snTrapUserLogin=snTrapUserLogin, snTrapMgmtModuleRedunStateChange=snTrapMgmtModuleRedunStateChange, snTrapL4RealServerPortUp=snTrapL4RealServerPortUp, snTrapModuleRemoved=snTrapModuleRemoved, snTrapBmWriteSeqDrop=snTrapBmWriteSeqDrop, snTrapNoBmFreeQueue=snTrapNoBmFreeQueue, snTrapModuleInserted=snTrapModuleInserted, snTrapRunningConfigChanged=snTrapRunningConfigChanged, snTrapL4FirewallBecomeStandby=snTrapL4FirewallBecomeStandby)

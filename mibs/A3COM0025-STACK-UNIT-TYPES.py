#
# PySNMP MIB module A3COM0025-STACK-UNIT-TYPES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0025-STACK-UNIT-TYPES
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
stackUnitTypes, stackSysObjIdentities = mibBuilder.importSymbols("A3COM0017-STACK-CONFIG", "stackUnitTypes", "stackSysObjIdentities")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, TimeTicks, NotificationType, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Bits, Counter64, Counter32, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter64", "Counter32", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stackDistributedAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1))
stackHub = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 1))
stackSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2))
stackAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 3))
stackDualSpeedHub500 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 1, 1))
stackSwitch1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 1))
stackSwitch3300 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 2))
stackSwitch3400 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 3))
stackSwitch4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 4))
stackSwitch4900 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 5))
stackSwitchBeefy = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 6))
stackSwitchBluetooth = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 7))
stackSwitchVCN2010 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 8))
stackSwitchVCN2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 2, 9))
stackWebCache1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 3, 1))
stackWebCache3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 4, 1, 3, 2))
stack12Port10BaseTRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 1))
stack24Port10BaseTRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 2))
stack24Port10BaseTRepeaterSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 3))
stack12Port100BaseTxRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 4))
stack24Port100BaseTxRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 5))
stack12Port10100BaseTxRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 6))
stack24Port10100BaseTxRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 7))
stack12Port10BaseTSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 8))
stack24Port10BaseTSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 9))
stack12Port10100BaseTxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 10))
stack24Port10100BaseTxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 11))
stack24Port10BaseTFixedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 12))
stack24Port10100BaseTxFixedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 13))
stack8Port100BaseFXSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 14))
stack12Port10100BaseTxSwitch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 15))
stack24Port10100BaseTxSwitch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 16))
stack12Port10100BaseTxSwitch3 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 17))
stack24Port10100BaseTxSwitch3 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 18))
stack12Port1001000BaseTxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 19))
stack12Port10100BaseTxSwitch4 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 20))
stack24Port10100BaseTxSwitch4 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 21))
stack10BaseT1Radio = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 22))
stack10BaseT4Radio = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 23))
stack24Port10100BaseTxSwitchXM = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 24))
stack24Port101001000BaseTxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 25))
stack24Port10100BaseTxSwitchMM = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 26))
stack24Port10100BaseTxSwitchSM = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 27))
stack24Port10100BaseTxSwitchTM = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 28))
stack24Port10100BaseTxSwitchXMA = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 29))
stack12Port1000BaseSxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 30))
stack24Port1000BaseSxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 31))
stack24Port10100BaseTxSwitchMM2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 32))
stack24Port10100BaseTxSwitchSM2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 33))
stack24Port10100BaseTxSwitchTM2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 34))
stack24Port10100BaseTxSwitchXM2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 35))
stack12Port10100BaseTxSwitch5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 36))
stack24Port10100BaseTxSwitch5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 37))
stack8Port100BaseFXSwitch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 38))
stack24Port10BaseTSwitchVCN = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 39))
stack24Port100BaseTxSwitchVCN = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 40))
stack48Port10100BaseTxSwitch3 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 41))
stack12Port101001000BaseTxSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 42))
stackWebCache1000UnitType = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 43))
stackWebCache3000UnitType = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 44))
stack24Port101001000BaseTSXGBICSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 45))
stack24Port101001000BaseTSXGBICRswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27, 5, 46))
mibBuilder.exportSymbols("A3COM0025-STACK-UNIT-TYPES", stackHub=stackHub, stack24Port10100BaseTxSwitchMM=stack24Port10100BaseTxSwitchMM, stackSwitch4400=stackSwitch4400, stack12Port10100BaseTxSwitch2=stack12Port10100BaseTxSwitch2, stack12Port10100BaseTxSwitch3=stack12Port10100BaseTxSwitch3, stack24Port10100BaseTxSwitch2=stack24Port10100BaseTxSwitch2, stack24Port10100BaseTxSwitch5=stack24Port10100BaseTxSwitch5, stackWebCache3000=stackWebCache3000, stackSwitch=stackSwitch, stack12Port1000BaseSxSwitch=stack12Port1000BaseSxSwitch, stackSwitch3300=stackSwitch3300, stack24Port101001000BaseTxSwitch=stack24Port101001000BaseTxSwitch, stack24Port10100BaseTxSwitchMM2=stack24Port10100BaseTxSwitchMM2, stack24Port101001000BaseTSXGBICRswitch=stack24Port101001000BaseTSXGBICRswitch, stack24Port10100BaseTxSwitchTM=stack24Port10100BaseTxSwitchTM, stackSwitchBeefy=stackSwitchBeefy, stack24Port10100BaseTxSwitchSM2=stack24Port10100BaseTxSwitchSM2, stack12Port101001000BaseTxSwitch=stack12Port101001000BaseTxSwitch, stackSwitchVCN2010=stackSwitchVCN2010, stack8Port100BaseFXSwitch=stack8Port100BaseFXSwitch, stack48Port10100BaseTxSwitch3=stack48Port10100BaseTxSwitch3, stack12Port10100BaseTxRepeater=stack12Port10100BaseTxRepeater, stack24Port100BaseTxRepeater=stack24Port100BaseTxRepeater, stack12Port10100BaseTxSwitch=stack12Port10100BaseTxSwitch, stack12Port1001000BaseTxSwitch=stack12Port1001000BaseTxSwitch, stack24Port10100BaseTxSwitchTM2=stack24Port10100BaseTxSwitchTM2, stack24Port10100BaseTxSwitch=stack24Port10100BaseTxSwitch, stack10BaseT1Radio=stack10BaseT1Radio, stack24Port101001000BaseTSXGBICSwitch=stack24Port101001000BaseTSXGBICSwitch, stackWebCache1000=stackWebCache1000, stackSwitch3400=stackSwitch3400, stack24Port10BaseTSwitchVCN=stack24Port10BaseTSwitchVCN, stackSwitchBluetooth=stackSwitchBluetooth, stack24Port1000BaseSxSwitch=stack24Port1000BaseSxSwitch, stackDualSpeedHub500=stackDualSpeedHub500, stack24Port10BaseTSwitch=stack24Port10BaseTSwitch, stack24Port10100BaseTxSwitchXM2=stack24Port10100BaseTxSwitchXM2, stack24Port10100BaseTxSwitchXM=stack24Port10100BaseTxSwitchXM, stack24Port100BaseTxSwitchVCN=stack24Port100BaseTxSwitchVCN, stack24Port10100BaseTxSwitchXMA=stack24Port10100BaseTxSwitchXMA, stack12Port100BaseTxRepeater=stack12Port100BaseTxRepeater, stack24Port10BaseTRepeaterSwitch=stack24Port10BaseTRepeaterSwitch, stack12Port10100BaseTxSwitch5=stack12Port10100BaseTxSwitch5, stack24Port10100BaseTxSwitch4=stack24Port10100BaseTxSwitch4, stackWebCache3000UnitType=stackWebCache3000UnitType, stackSwitchVCN2100=stackSwitchVCN2100, stack24Port10BaseTRepeater=stack24Port10BaseTRepeater, stack24Port10BaseTFixedSwitch=stack24Port10BaseTFixedSwitch, stack24Port10100BaseTxFixedSwitch=stack24Port10100BaseTxFixedSwitch, stack8Port100BaseFXSwitch2=stack8Port100BaseFXSwitch2, stackAppliance=stackAppliance, stackWebCache1000UnitType=stackWebCache1000UnitType, stack12Port10BaseTRepeater=stack12Port10BaseTRepeater, stack12Port10BaseTSwitch=stack12Port10BaseTSwitch, stackSwitch4900=stackSwitch4900, stack12Port10100BaseTxSwitch4=stack12Port10100BaseTxSwitch4, stack24Port10100BaseTxSwitch3=stack24Port10100BaseTxSwitch3, stack10BaseT4Radio=stack10BaseT4Radio, stack24Port10100BaseTxSwitchSM=stack24Port10100BaseTxSwitchSM, stackDistributedAgent=stackDistributedAgent, stackSwitch1100=stackSwitch1100, stack24Port10100BaseTxRepeater=stack24Port10100BaseTxRepeater)

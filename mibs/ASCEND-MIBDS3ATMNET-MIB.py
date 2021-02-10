#
# PySNMP MIB module ASCEND-MIBDS3ATMNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBDS3ATMNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Integer32, NotificationType, iso, Bits, Counter32, TimeTicks, Gauge32, Counter64, ObjectIdentity, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "iso", "Bits", "Counter32", "TimeTicks", "Gauge32", "Counter64", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibds3AtmNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 13))
mibds3AtmNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 13, 1), )
if mibBuilder.loadTexts: mibds3AtmNetworkProfileTable.setStatus('mandatory')
mibds3AtmNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1), ).setIndexNames((0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Shelf-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Slot-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibds3AtmNetworkProfileEntry.setStatus('mandatory')
ds3AtmNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 1), Integer32()).setLabel("ds3AtmNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Shelf_o.setStatus('mandatory')
ds3AtmNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 2), Integer32()).setLabel("ds3AtmNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Slot_o.setStatus('mandatory')
ds3AtmNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 3), Integer32()).setLabel("ds3AtmNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Item_o.setStatus('mandatory')
ds3AtmNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 4), DisplayString()).setLabel("ds3AtmNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Name.setStatus('mandatory')
ds3AtmNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("ds3AtmNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
ds3AtmNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ds3AtmNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
ds3AtmNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 7), Integer32()).setLabel("ds3AtmNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
ds3AtmNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Enabled.setStatus('mandatory')
ds3AtmNetworkProfile_SparePhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("ds3AtmNetworkProfile-SparePhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_SparePhysicalAddress_Shelf.setStatus('mandatory')
ds3AtmNetworkProfile_SparePhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ds3AtmNetworkProfile-SparePhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_SparePhysicalAddress_Slot.setStatus('mandatory')
ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 11), Integer32()).setLabel("ds3AtmNetworkProfile-SparePhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setStatus('mandatory')
ds3AtmNetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("ds3AtmNetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_SparingMode.setStatus('mandatory')
ds3AtmNetworkProfile_ProfileNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 13), Integer32()).setLabel("ds3AtmNetworkProfile-ProfileNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_ProfileNumber.setStatus('mandatory')
ds3AtmNetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("ds3AtmNetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_IgnoreLineup.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrunkGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 14), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrunkGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrunkGroup.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 15), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 16), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 17), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 18), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_Activation = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dsrActive", 2), ("dcdDsrActive", 3)))).setLabel("ds3AtmNetworkProfile-LineConfig-Activation").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_Activation.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_Loopback = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noLoopback", 1), ("facilityLoopback", 2), ("localLoopback", 3)))).setLabel("ds3AtmNetworkProfile-LineConfig-Loopback").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_Loopback.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_HighTxOutput = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-HighTxOutput").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_HighTxOutput.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_ReceiveEqualization = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-ReceiveEqualization").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_ReceiveEqualization.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_FramerMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cBitADM", 1), ("cBITPLCP", 2), ("cBitAdmLoopTimed", 3), ("cBitPlcpLoopTimed", 4), ("cBitAdmFrameLocked", 5), ("cBitPlcpFrameLocked", 6)))).setLabel("ds3AtmNetworkProfile-LineConfig-FramerMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_FramerMode.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VpiVciRange = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("n-01-3232767", 1), ("n-03-3216383", 2), ("n-07-328191", 3), ("n-015-324095", 4), ("n-031-322047", 5), ("n-063-321023", 6), ("n-0127-32511", 7), ("n-0255-32255", 8), ("vpi0255Vci32255", 9), ("vpi0255Vci32511", 10), ("vpi0255Vci321023", 11), ("vpi0255Vci322047", 12), ("vpi0255Vci324095", 13), ("vpi0255Vci328191", 14), ("vpi0255Vci3216383", 15)))).setLabel("ds3AtmNetworkProfile-LineConfig-VpiVciRange").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VpiVciRange.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_ClockSource = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eligible", 1), ("notEligible", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-ClockSource").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_ClockSource.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_ClockPriority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("highPriority", 2), ("middlePriority", 3), ("lowPriority", 4)))).setLabel("ds3AtmNetworkProfile-LineConfig-ClockPriority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_ClockPriority.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_CellPayloadScramble = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-CellPayloadScramble").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_CellPayloadScramble.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-StatusChangeTrapEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setStatus('mandatory')
ds3AtmNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ds3AtmNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_Action_o.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 13, 2), ).setLabel("mibds3AtmNetworkProfile-LineConfig-TrafficShapersTable")
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1), ).setLabel("mibds3AtmNetworkProfile-LineConfig-TrafficShapersEntry").setIndexNames((0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o"))
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 1), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 2), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 3), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 4), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 6), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-BitRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 7), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-PeakRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 8), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-MaxBurstSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Aggregate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 10), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-TrafficShapers-Priority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 13, 3), ).setLabel("mibds3AtmNetworkProfile-LineConfig-IncomingVCCsTable")
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1), ).setLabel("mibds3AtmNetworkProfile-LineConfig-IncomingVCCsEntry").setIndexNames((0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o"))
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 1), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 2), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 3), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 4), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 6), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Vpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 7), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-StartVci").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 8), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-IncomingVCCs-EndVci").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 13, 4), ).setLabel("mibds3AtmNetworkProfile-LineConfig-VcSwitchingVpiTable")
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable.setStatus('mandatory')
mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1), ).setLabel("mibds3AtmNetworkProfile-LineConfig-VcSwitchingVpiEntry").setIndexNames((0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o"), (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o"))
if mibBuilder.loadTexts: mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 1), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 2), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 3), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 4), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setStatus('mandatory')
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 5), Integer32()).setLabel("ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBDS3ATMNET-MIB", ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber=ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber, ds3AtmNetworkProfile_LineConfig_TrunkGroup=ds3AtmNetworkProfile_LineConfig_TrunkGroup, ds3AtmNetworkProfile_Shelf_o=ds3AtmNetworkProfile_Shelf_o, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi, ds3AtmNetworkProfile_SparePhysicalAddress_Slot=ds3AtmNetworkProfile_SparePhysicalAddress_Slot, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci, ds3AtmNetworkProfile_ProfileNumber=ds3AtmNetworkProfile_ProfileNumber, ds3AtmNetworkProfile_LineConfig_CellPayloadScramble=ds3AtmNetworkProfile_LineConfig_CellPayloadScramble, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority, mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable=mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable, ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate=ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate, ds3AtmNetworkProfile_LineConfig_ClockPriority=ds3AtmNetworkProfile_LineConfig_ClockPriority, ds3AtmNetworkProfile_PhysicalAddress_Slot=ds3AtmNetworkProfile_PhysicalAddress_Slot, ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber=ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber, mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable=mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable, ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize=ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize, ds3AtmNetworkProfile_IgnoreLineup=ds3AtmNetworkProfile_IgnoreLineup, ds3AtmNetworkProfile_SparingMode=ds3AtmNetworkProfile_SparingMode, ds3AtmNetworkProfile_Slot_o=ds3AtmNetworkProfile_Slot_o, ds3AtmNetworkProfile_LineConfig_FramerMode=ds3AtmNetworkProfile_LineConfig_FramerMode, ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi=ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o, ds3AtmNetworkProfile_SparePhysicalAddress_Shelf=ds3AtmNetworkProfile_SparePhysicalAddress_Shelf, ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber=ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o, mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry=mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry, ds3AtmNetworkProfile_LineConfig_VpiVciRange=ds3AtmNetworkProfile_LineConfig_VpiVciRange, ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o=ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o, mibds3AtmNetworkProfileEntry=mibds3AtmNetworkProfileEntry, ds3AtmNetworkProfile_LineConfig_NailedGroup=ds3AtmNetworkProfile_LineConfig_NailedGroup, ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate=ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate, ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o=ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o, ds3AtmNetworkProfile_PhysicalAddress_ItemNumber=ds3AtmNetworkProfile_PhysicalAddress_ItemNumber, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o, ds3AtmNetworkProfile_PhysicalAddress_Shelf=ds3AtmNetworkProfile_PhysicalAddress_Shelf, DisplayString=DisplayString, mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable=mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable, mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry=mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry, ds3AtmNetworkProfile_Item_o=ds3AtmNetworkProfile_Item_o, mibds3AtmNetworkProfileTable=mibds3AtmNetworkProfileTable, ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o=ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o, ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o=ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o, ds3AtmNetworkProfile_LineConfig_ClockSource=ds3AtmNetworkProfile_LineConfig_ClockSource, mibds3AtmNetworkProfile=mibds3AtmNetworkProfile, ds3AtmNetworkProfile_LineConfig_HighTxOutput=ds3AtmNetworkProfile_LineConfig_HighTxOutput, ds3AtmNetworkProfile_LineConfig_ReceiveEqualization=ds3AtmNetworkProfile_LineConfig_ReceiveEqualization, mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry=mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry, ds3AtmNetworkProfile_Name=ds3AtmNetworkProfile_Name, ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable=ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable, ds3AtmNetworkProfile_LineConfig_Loopback=ds3AtmNetworkProfile_LineConfig_Loopback, ds3AtmNetworkProfile_Action_o=ds3AtmNetworkProfile_Action_o, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci, ds3AtmNetworkProfile_Enabled=ds3AtmNetworkProfile_Enabled, ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber=ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber, ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o=ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o, ds3AtmNetworkProfile_LineConfig_Activation=ds3AtmNetworkProfile_LineConfig_Activation, ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o=ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o)

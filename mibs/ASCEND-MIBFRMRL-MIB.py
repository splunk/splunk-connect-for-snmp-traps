#
# PySNMP MIB module ASCEND-MIBFRMRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBFRMRL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Gauge32, Integer32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Bits, Counter64, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Bits", "Counter64", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmfrProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 78))
mibframeRelayProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 2))
mibmfrProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 78, 1), )
if mibBuilder.loadTexts: mibmfrProfileTable.setStatus('mandatory')
mibmfrProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1), ).setIndexNames((0, "ASCEND-MIBFRMRL-MIB", "mfrProfile-MfrBundleName"))
if mibBuilder.loadTexts: mibmfrProfileEntry.setStatus('mandatory')
mfrProfile_MfrBundleName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 1), DisplayString()).setLabel("mfrProfile-MfrBundleName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrProfile_MfrBundleName.setStatus('mandatory')
mfrProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mfrProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrProfile_Active.setStatus('mandatory')
mfrProfile_MfrBundleType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("mfrDte", 1)))).setLabel("mfrProfile-MfrBundleType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrProfile_MfrBundleType.setStatus('mandatory')
mfrProfile_MaxBundleMembers = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 4), Integer32()).setLabel("mfrProfile-MaxBundleMembers").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrProfile_MaxBundleMembers.setStatus('mandatory')
mfrProfile_MinBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 5), Integer32()).setLabel("mfrProfile-MinBandwidth").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrProfile_MinBandwidth.setStatus('mandatory')
mfrProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mfrProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrProfile_Action_o.setStatus('mandatory')
mibframeRelayProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 2, 1), )
if mibBuilder.loadTexts: mibframeRelayProfileTable.setStatus('mandatory')
mibframeRelayProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1), ).setIndexNames((0, "ASCEND-MIBFRMRL-MIB", "frameRelayProfile-FrName"))
if mibBuilder.loadTexts: mibframeRelayProfileEntry.setStatus('mandatory')
frameRelayProfile_FrName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 1), DisplayString()).setLabel("frameRelayProfile-FrName").setMaxAccess("readonly")
if mibBuilder.loadTexts: frameRelayProfile_FrName.setStatus('mandatory')
frameRelayProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("frameRelayProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Active.setStatus('mandatory')
frameRelayProfile_NailedUpGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 3), Integer32()).setLabel("frameRelayProfile-NailedUpGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_NailedUpGroup.setStatus('mandatory')
frameRelayProfile_NailedMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("off", 1), ("ft1", 2), ("ft1Mpp", 3), ("bri", 4), ("ft1Bo", 5), ("dChan", 6), ("aodi", 7), ("megamax", 8)))).setLabel("frameRelayProfile-NailedMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_NailedMode.setStatus('mandatory')
frameRelayProfile_CalledNumberType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 5), Integer32()).setLabel("frameRelayProfile-CalledNumberType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_CalledNumberType.setStatus('mandatory')
frameRelayProfile_SwitchedCallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 255, 263))).clone(namedValues=NamedValues(("voice", 1), ("n-56kRestricted", 2), ("n-64kClear", 3), ("n-64kRestricted", 4), ("n-56kClear", 5), ("n-384kRestricted", 6), ("n-384kClear", 7), ("n-1536kClear", 8), ("n-1536kRestricted", 9), ("n-128kClear", 10), ("n-192kClear", 11), ("n-256kClear", 12), ("n-320kClear", 13), ("dws384Clear", 14), ("n-448Clear", 15), ("n-512Clear", 16), ("n-576Clear", 17), ("n-640Clear", 18), ("n-704Clear", 19), ("n-768Clear", 20), ("n-832Clear", 21), ("n-896Clear", 22), ("n-960Clear", 23), ("n-1024Clear", 24), ("n-1088Clear", 25), ("n-1152Clear", 26), ("n-1216Clear", 27), ("n-1280Clear", 28), ("n-1344Clear", 29), ("n-1408Clear", 30), ("n-1472Clear", 31), ("n-1600Clear", 32), ("n-1664Clear", 33), ("n-1728Clear", 34), ("n-1792Clear", 35), ("n-1856Clear", 36), ("n-1920Clear", 37), ("x30RestrictedBearer", 39), ("v110ClearBearer", 40), ("n-64kX30Restricted", 41), ("n-56kV110Clear", 42), ("modem", 43), ("atmodem", 44), ("n-2456kV110", 46), ("n-4856kV110", 47), ("n-9656kV110", 48), ("n-19256kV110", 49), ("n-38456kV110", 50), ("n-2456krV110", 51), ("n-4856krV110", 52), ("n-9656krV110", 53), ("n-19256krV110", 54), ("n-38456krV110", 55), ("n-2464kV110", 56), ("n-4864kV110", 57), ("n-9664kV110", 58), ("n-19264kV110", 59), ("n-38464kV110", 60), ("n-2464krV110", 61), ("n-4864krV110", 62), ("n-9664krV110", 63), ("n-19264krV110", 64), ("n-38464krV110", 65), ("v32", 66), ("phs64k", 67), ("voiceOverIp", 68), ("atmSvc", 70), ("frameRelaySvc", 71), ("vpnTunnel", 72), ("wormarq", 73), ("n-14456kV110", 74), ("n-28856kV110", 75), ("n-14456krV110", 76), ("n-28856krV110", 77), ("n-14464kV110", 78), ("n-28864kV110", 79), ("n-14464krV110", 80), ("n-28864krV110", 81), ("modem31khzAudio", 82), ("x25Svc", 83), ("n-144kClear", 255), ("iptoip", 263)))).setLabel("frameRelayProfile-SwitchedCallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_SwitchedCallType.setStatus('mandatory')
frameRelayProfile_PhoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 7), DisplayString()).setLabel("frameRelayProfile-PhoneNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_PhoneNumber.setStatus('mandatory')
frameRelayProfile_BillingNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 8), DisplayString()).setLabel("frameRelayProfile-BillingNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_BillingNumber.setStatus('mandatory')
frameRelayProfile_TransitNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 9), DisplayString()).setLabel("frameRelayProfile-TransitNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_TransitNumber.setStatus('mandatory')
frameRelayProfile_CallByCallId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 11), Integer32()).setLabel("frameRelayProfile-CallByCallId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_CallByCallId.setStatus('mandatory')
frameRelayProfile_LinkMgmt = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ansiT1617d", 2), ("ccittQ933a", 3)))).setLabel("frameRelayProfile-LinkMgmt").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_LinkMgmt.setStatus('mandatory')
frameRelayProfile_LinkType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("nni", 3)))).setLabel("frameRelayProfile-LinkType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_LinkType.setStatus('mandatory')
frameRelayProfile_N391Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 13), Integer32()).setLabel("frameRelayProfile-N391Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_N391Val.setStatus('mandatory')
frameRelayProfile_N392Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 14), Integer32()).setLabel("frameRelayProfile-N392Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_N392Val.setStatus('mandatory')
frameRelayProfile_N393Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 15), Integer32()).setLabel("frameRelayProfile-N393Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_N393Val.setStatus('mandatory')
frameRelayProfile_T391Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 16), Integer32()).setLabel("frameRelayProfile-T391Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_T391Val.setStatus('mandatory')
frameRelayProfile_T392Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 17), Integer32()).setLabel("frameRelayProfile-T392Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_T392Val.setStatus('mandatory')
frameRelayProfile_oMRU = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 18), Integer32()).setLabel("frameRelayProfile-oMRU").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_oMRU.setStatus('mandatory')
frameRelayProfile_DceN392Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 19), Integer32()).setLabel("frameRelayProfile-DceN392Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_DceN392Val.setStatus('mandatory')
frameRelayProfile_DceN393Val = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 20), Integer32()).setLabel("frameRelayProfile-DceN393Val").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_DceN393Val.setStatus('mandatory')
frameRelayProfile_LinkMgmtDlci = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 1024))).clone(namedValues=NamedValues(("dlci0", 1), ("dlci1023", 1024)))).setLabel("frameRelayProfile-LinkMgmtDlci").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_LinkMgmtDlci.setStatus('mandatory')
frameRelayProfile_MfrBundleName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 24), DisplayString()).setLabel("frameRelayProfile-MfrBundleName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_MfrBundleName.setStatus('mandatory')
frameRelayProfile_Frf5Options_Enable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("frameRelayProfile-Frf5Options-Enable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Frf5Options_Enable.setStatus('mandatory')
frameRelayProfile_Frf5Options_Vpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 28), Integer32()).setLabel("frameRelayProfile-Frf5Options-Vpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Frf5Options_Vpi.setStatus('mandatory')
frameRelayProfile_Frf5Options_Vci = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 29), Integer32()).setLabel("frameRelayProfile-Frf5Options-Vci").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Frf5Options_Vci.setStatus('mandatory')
frameRelayProfile_Frf5Options_Shaper = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 30), Integer32()).setLabel("frameRelayProfile-Frf5Options-Shaper").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Frf5Options_Shaper.setStatus('mandatory')
frameRelayProfile_SvcOptions_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("frameRelayProfile-SvcOptions-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_SvcOptions_Enabled.setStatus('mandatory')
frameRelayProfile_SvcOptions_FrAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 26), DisplayString()).setLabel("frameRelayProfile-SvcOptions-FrAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_SvcOptions_FrAddress.setStatus('mandatory')
frameRelayProfile_FastPathEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("frameRelayProfile-FastPathEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_FastPathEnabled.setStatus('mandatory')
frameRelayProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("frameRelayProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: frameRelayProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBFRMRL-MIB", frameRelayProfile_Frf5Options_Shaper=frameRelayProfile_Frf5Options_Shaper, frameRelayProfile_Frf5Options_Vci=frameRelayProfile_Frf5Options_Vci, frameRelayProfile_Action_o=frameRelayProfile_Action_o, frameRelayProfile_FastPathEnabled=frameRelayProfile_FastPathEnabled, mibmfrProfileTable=mibmfrProfileTable, mfrProfile_Active=mfrProfile_Active, frameRelayProfile_PhoneNumber=frameRelayProfile_PhoneNumber, mfrProfile_MfrBundleName=mfrProfile_MfrBundleName, DisplayString=DisplayString, frameRelayProfile_oMRU=frameRelayProfile_oMRU, frameRelayProfile_DceN393Val=frameRelayProfile_DceN393Val, frameRelayProfile_NailedUpGroup=frameRelayProfile_NailedUpGroup, frameRelayProfile_CalledNumberType=frameRelayProfile_CalledNumberType, frameRelayProfile_DceN392Val=frameRelayProfile_DceN392Val, mibframeRelayProfileTable=mibframeRelayProfileTable, frameRelayProfile_SvcOptions_FrAddress=frameRelayProfile_SvcOptions_FrAddress, frameRelayProfile_SwitchedCallType=frameRelayProfile_SwitchedCallType, frameRelayProfile_MfrBundleName=frameRelayProfile_MfrBundleName, frameRelayProfile_TransitNumber=frameRelayProfile_TransitNumber, frameRelayProfile_N392Val=frameRelayProfile_N392Val, frameRelayProfile_CallByCallId=frameRelayProfile_CallByCallId, frameRelayProfile_T391Val=frameRelayProfile_T391Val, frameRelayProfile_SvcOptions_Enabled=frameRelayProfile_SvcOptions_Enabled, frameRelayProfile_LinkType=frameRelayProfile_LinkType, mfrProfile_MfrBundleType=mfrProfile_MfrBundleType, mibmfrProfileEntry=mibmfrProfileEntry, frameRelayProfile_LinkMgmtDlci=frameRelayProfile_LinkMgmtDlci, mibmfrProfile=mibmfrProfile, frameRelayProfile_T392Val=frameRelayProfile_T392Val, mfrProfile_Action_o=mfrProfile_Action_o, frameRelayProfile_N391Val=frameRelayProfile_N391Val, mfrProfile_MaxBundleMembers=mfrProfile_MaxBundleMembers, mibframeRelayProfile=mibframeRelayProfile, frameRelayProfile_Active=frameRelayProfile_Active, frameRelayProfile_LinkMgmt=frameRelayProfile_LinkMgmt, frameRelayProfile_Frf5Options_Vpi=frameRelayProfile_Frf5Options_Vpi, frameRelayProfile_Frf5Options_Enable=frameRelayProfile_Frf5Options_Enable, mibframeRelayProfileEntry=mibframeRelayProfileEntry, frameRelayProfile_BillingNumber=frameRelayProfile_BillingNumber, mfrProfile_MinBandwidth=mfrProfile_MinBandwidth, frameRelayProfile_N393Val=frameRelayProfile_N393Val, frameRelayProfile_FrName=frameRelayProfile_FrName, frameRelayProfile_NailedMode=frameRelayProfile_NailedMode)

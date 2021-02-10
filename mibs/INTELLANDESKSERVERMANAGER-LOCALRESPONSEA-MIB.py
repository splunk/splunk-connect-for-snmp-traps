#
# PySNMP MIB module INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Integer32, TimeTicks, IpAddress, Bits, MibIdentifier, enterprises, Gauge32, Counter64, NotificationType, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Integer32", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "enterprises", "Gauge32", "Counter64", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiInteger(Integer32):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiDateX(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2))
server_management = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10)).setLabel("server-management")
software = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10, 3))
lra = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1))
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1))
tComponentid = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1), )
if mibBuilder.loadTexts: tComponentid.setStatus('mandatory')
eComponentid = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1), ).setIndexNames((0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eComponentid.setStatus('mandatory')
a1Manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Manufacturer.setStatus('mandatory')
a1Product = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Product.setStatus('mandatory')
a1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Version.setStatus('mandatory')
a1SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1SerialNumber.setStatus('mandatory')
a1Installation = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 5), DmiDateX()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Installation.setStatus('mandatory')
a1Verify = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vAnErrorOccurredCheckStatusCode", 0), ("vThisComponentDoesNotExist", 1), ("vVerificationIsNotSupported", 2), ("vReserved", 3), ("vThisComponentExistsButTheFunctionalityI", 4), ("vThisComponentExistsButTheFunctionality1", 5), ("vThisComponentExistsAndIsNotFunctioningC", 6), ("vThisComponentExistsAndIsFunctioningCorr", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Verify.setStatus('mandatory')
tNameTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2), )
if mibBuilder.loadTexts: tNameTable.setStatus('mandatory')
eNameTable = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1), ).setIndexNames((0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a2MifId"))
if mibBuilder.loadTexts: eNameTable.setStatus('mandatory')
a2MifId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 99))).clone(namedValues=NamedValues(("vUnknown", 0), ("vBaseboard", 1), ("vAdaptecScsi", 2), ("vMylexRaid", 3), ("vNic", 4), ("vUps", 5), ("vSymbiosSdms", 6), ("vAmiRaid", 7), ("vMylexGamRaid", 8), ("vAdaptecCioScsi", 9), ("vSymbiosScsi", 10), ("vIntelNic", 11), ("vLsiScsi211", 12), ("vTestmif", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2MifId.setStatus('mandatory')
a2ComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2ComponentName.setStatus('mandatory')
tActionsTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4), )
if mibBuilder.loadTexts: tActionsTable.setStatus('mandatory')
eActionsTable = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1), ).setIndexNames((0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4RelatedMif"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Group"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Instance"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Attribute"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Value"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Severity"))
if mibBuilder.loadTexts: eActionsTable.setStatus('mandatory')
a4RelatedMif = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 99))).clone(namedValues=NamedValues(("vUnknown", 0), ("vBaseboard", 1), ("vAdaptecScsi", 2), ("vMylexRaid", 3), ("vNic", 4), ("vUps", 5), ("vSymbiosSdms", 6), ("vAmiRaid", 7), ("vMylexGamRaid", 8), ("vAdaptecCioScsi", 9), ("vSymbiosScsi", 10), ("vIntelNic", 11), ("vLsiScsi211", 12), ("vTestmif", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4RelatedMif.setStatus('mandatory')
a4Group = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Group.setStatus('mandatory')
a4Instance = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Instance.setStatus('mandatory')
a4Attribute = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Attribute.setStatus('mandatory')
a4Value = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Value.setStatus('mandatory')
a4Severity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Severity.setStatus('mandatory')
a4BeepSpeaker = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 7), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4BeepSpeaker.setStatus('mandatory')
a4DisplayAlertMessageOnConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 8), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4DisplayAlertMessageOnConsole.setStatus('mandatory')
a4LogToDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 9), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4LogToDisk.setStatus('mandatory')
a4WriteToLcd = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 10), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4WriteToLcd.setStatus('mandatory')
a4ShutdownTheOs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 11), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4ShutdownTheOs.setStatus('mandatory')
a4ShutdownAndPowerOffTheSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 12), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4ShutdownAndPowerOffTheSystem.setStatus('mandatory')
a4ShutdownAndResetTheSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 13), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4ShutdownAndResetTheSystem.setStatus('mandatory')
a4ImmediatePowerOff = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 14), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4ImmediatePowerOff.setStatus('mandatory')
a4ImmediateReset = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 15), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4ImmediateReset.setStatus('mandatory')
a4BroadcastMessageOnNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 16), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4BroadcastMessageOnNetwork.setStatus('mandatory')
a4AmsAlertName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 17), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4AmsAlertName.setStatus('mandatory')
a4Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 30), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4Enabled.setStatus('mandatory')
tActionsTableForStandardIndications = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10), )
if mibBuilder.loadTexts: tActionsTableForStandardIndications.setStatus('mandatory')
eActionsTableForStandardIndications = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1), ).setIndexNames((0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10RelatedMif"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventGenerationGroup"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventType"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Instance"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Reserved"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Severity"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventSystem"), (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventSub-system"))
if mibBuilder.loadTexts: eActionsTableForStandardIndications.setStatus('mandatory')
a10RelatedMif = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 99))).clone(namedValues=NamedValues(("vUnknown", 0), ("vBaseboard", 1), ("vAdaptecScsi", 2), ("vMylexRaid", 3), ("vNic", 4), ("vUps", 5), ("vSymbiosSdms", 6), ("vAmiRaid", 7), ("vMylexGamRaid", 8), ("vAdaptecCioScsi", 9), ("vSymbiosScsi", 10), ("vIntelNic", 11), ("vLsiScsi211", 12), ("vTestmif", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10RelatedMif.setStatus('mandatory')
a10EventGenerationGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10EventGenerationGroup.setStatus('mandatory')
a10EventType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10EventType.setStatus('mandatory')
a10Instance = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10Instance.setStatus('mandatory')
a10Reserved = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10Reserved.setStatus('mandatory')
a10Severity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10Severity.setStatus('mandatory')
a10BeepSpeaker = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 7), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10BeepSpeaker.setStatus('mandatory')
a10DisplayAlertMessageOnConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 8), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10DisplayAlertMessageOnConsole.setStatus('mandatory')
a10LogToDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 9), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10LogToDisk.setStatus('mandatory')
a10WriteToLcd = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 10), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10WriteToLcd.setStatus('mandatory')
a10ShutdownTheOs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 11), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ShutdownTheOs.setStatus('mandatory')
a10ShutdownAndPowerOffTheSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 12), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ShutdownAndPowerOffTheSystem.setStatus('mandatory')
a10ShutdownAndResetTheSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 13), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ShutdownAndResetTheSystem.setStatus('mandatory')
a10ImmediatePowerOff = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 14), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ImmediatePowerOff.setStatus('mandatory')
a10ImmediateReset = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 15), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ImmediateReset.setStatus('mandatory')
a10BroadcastMessageOnNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 16), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10BroadcastMessageOnNetwork.setStatus('mandatory')
a10AmsAlertName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 17), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10AmsAlertName.setStatus('mandatory')
a10ImmediateNmi = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 18), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10ImmediateNmi.setStatus('mandatory')
a10Page = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 19), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10Page.setStatus('mandatory')
a10Email = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 20), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10Email.setStatus('mandatory')
a10Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 30), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a10Enabled.setStatus('mandatory')
a10EventSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 31), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a10EventSystem.setStatus('mandatory')
a10EventSub_system = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 32), DmiInteger()).setLabel("a10EventSub-system").setMaxAccess("readonly")
if mibBuilder.loadTexts: a10EventSub_system.setStatus('mandatory')
tMiftomib = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99), )
if mibBuilder.loadTexts: tMiftomib.setStatus('mandatory')
eMiftomib = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1), ).setIndexNames((0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eMiftomib.setStatus('mandatory')
a99MibName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99MibName.setStatus('mandatory')
a99MibOid = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99MibOid.setStatus('mandatory')
a99DisableTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 3), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a99DisableTrap.setStatus('mandatory')
mibBuilder.exportSymbols("INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", a10ShutdownTheOs=a10ShutdownTheOs, a4BroadcastMessageOnNetwork=a4BroadcastMessageOnNetwork, a2MifId=a2MifId, a10RelatedMif=a10RelatedMif, a10EventType=a10EventType, a10Email=a10Email, a1Version=a1Version, tActionsTable=tActionsTable, a10Reserved=a10Reserved, a10BroadcastMessageOnNetwork=a10BroadcastMessageOnNetwork, a10EventGenerationGroup=a10EventGenerationGroup, a4ShutdownTheOs=a4ShutdownTheOs, tComponentid=tComponentid, eActionsTableForStandardIndications=eActionsTableForStandardIndications, a10EventSystem=a10EventSystem, a99MibName=a99MibName, a10Instance=a10Instance, a10LogToDisk=a10LogToDisk, a4ShutdownAndResetTheSystem=a4ShutdownAndResetTheSystem, eComponentid=eComponentid, a10AmsAlertName=a10AmsAlertName, lra=lra, a4LogToDisk=a4LogToDisk, a2ComponentName=a2ComponentName, a4Severity=a4Severity, intel=intel, a10ShutdownAndPowerOffTheSystem=a10ShutdownAndPowerOffTheSystem, DmiInteger=DmiInteger, tMiftomib=tMiftomib, a4ImmediateReset=a4ImmediateReset, tActionsTableForStandardIndications=tActionsTableForStandardIndications, a10Page=a10Page, tNameTable=tNameTable, a10ShutdownAndResetTheSystem=a10ShutdownAndResetTheSystem, DmiComponentIndex=DmiComponentIndex, software=software, server_management=server_management, a4RelatedMif=a4RelatedMif, a4BeepSpeaker=a4BeepSpeaker, a4WriteToLcd=a4WriteToLcd, a4Value=a4Value, DmiDateX=DmiDateX, a4Attribute=a4Attribute, a1Verify=a1Verify, a4ShutdownAndPowerOffTheSystem=a4ShutdownAndPowerOffTheSystem, eMiftomib=eMiftomib, a10Severity=a10Severity, a4DisplayAlertMessageOnConsole=a4DisplayAlertMessageOnConsole, a99DisableTrap=a99DisableTrap, a10BeepSpeaker=a10BeepSpeaker, DmiDisplaystring=DmiDisplaystring, a1Installation=a1Installation, a4Instance=a4Instance, eNameTable=eNameTable, a1SerialNumber=a1SerialNumber, a10WriteToLcd=a10WriteToLcd, a99MibOid=a99MibOid, a4ImmediatePowerOff=a4ImmediatePowerOff, products=products, a4AmsAlertName=a4AmsAlertName, a4Enabled=a4Enabled, a1Manufacturer=a1Manufacturer, a10DisplayAlertMessageOnConsole=a10DisplayAlertMessageOnConsole, a10ImmediateReset=a10ImmediateReset, a10EventSub_system=a10EventSub_system, a10Enabled=a10Enabled, a10ImmediatePowerOff=a10ImmediatePowerOff, a10ImmediateNmi=a10ImmediateNmi, a1Product=a1Product, eActionsTable=eActionsTable, dmtfGroups=dmtfGroups, a4Group=a4Group)

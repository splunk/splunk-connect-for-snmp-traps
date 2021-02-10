#
# PySNMP MIB module IPSEC-IPSECACTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPSEC-IPSECACTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
IfDirection, = mibBuilder.importSymbols("DIFFSERV-MIB", "IfDirection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SpdIPPacketLogging, spdActions, SpdAdminStatus = mibBuilder.importSymbols("IPSEC-SPD-MIB", "SpdIPPacketLogging", "spdActions", "SpdAdminStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Unsigned32, Counter32, ObjectIdentity, Bits, NotificationType, MibIdentifier, Gauge32, ModuleIdentity, Counter64, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "ModuleIdentity", "Counter64", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TimeStamp, RowStatus, TruthValue, StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "TruthValue", "StorageType", "TextualConvention", "DisplayString")
ipsaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 153, 4, 1))
ipsaMIB.setRevisions(('2006-10-17 00:00',))
if mibBuilder.loadTexts: ipsaMIB.setLastUpdated('200610170000Z')
if mibBuilder.loadTexts: ipsaMIB.setOrganization('IETF IP Security Policy Working Group')
ipsaConfigObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 1))
ipsaNotificationObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 2))
ipsaConformanceObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 3))
class IpsecDoiEncapsulationMode(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IpsecDoiIpcompTransform(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.4.5 and 6.6, RFC 3051'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class IpsecDoiAuthAlgorithm(TextualConvention, Unsigned32):
    reference = 'RFC 2407 section 4.5, RFC 2407 section 4.4.3.1, RFC 1826, IANA, RFC 2857'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IpsecDoiEspTransform(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.4.4 and 6.5, IANA'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class IpsecDoiIdentType(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.4.5, 4.6.2.1, and 6.9'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class IpsaCredentialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("unknown", 1), ("sharedSecret", 2), ("x509", 3), ("kerberos", 4))

class IpsaIdentityFilter(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

ipsaSaPreconfiguredActionTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1), )
if mibBuilder.loadTexts: ipsaSaPreconfiguredActionTable.setStatus('current')
ipsaSaPreconfiguredActionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionName"), (0, "IPSEC-IPSECACTION-MIB", "ipsaSaPreActSADirection"))
if mibBuilder.loadTexts: ipsaSaPreconfiguredActionEntry.setStatus('current')
ipsaSaPreActActionName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaSaPreActActionName.setStatus('current')
ipsaSaPreActSADirection = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 2), IfDirection())
if mibBuilder.loadTexts: ipsaSaPreActSADirection.setStatus('current')
ipsaSaPreActActionDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActActionDescription.setStatus('current')
ipsaSaPreActActionLifetimeSec = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 4), Unsigned32().clone(28800)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActActionLifetimeSec.setStatus('current')
ipsaSaPreActActionLifetimeKB = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActActionLifetimeKB.setStatus('current')
ipsaSaPreActDoActionLogging = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActDoActionLogging.setStatus('current')
ipsaSaPreActDoPacketLogging = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 7), SpdIPPacketLogging().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActDoPacketLogging.setStatus('current')
ipsaSaPreActDFHandling = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("copy", 1), ("set", 2), ("clear", 3))).clone('copy')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActDFHandling.setStatus('current')
ipsaSaPreActActionType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 9), IpsecDoiEncapsulationMode().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActActionType.setStatus('current')
ipsaSaPreActAHSPI = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActAHSPI.setStatus('current')
ipsaSaPreActAHTransformName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActAHTransformName.setStatus('current')
ipsaSaPreActAHSharedSecretName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActAHSharedSecretName.setStatus('current')
ipsaSaPreActESPSPI = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActESPSPI.setStatus('current')
ipsaSaPreActESPTransformName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 14), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActESPTransformName.setStatus('current')
ipsaSaPreActESPEncSecretName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActESPEncSecretName.setStatus('current')
ipsaSaPreActESPAuthSecretName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 16), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActESPAuthSecretName.setStatus('current')
ipsaSaPreActIPCompSPI = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActIPCompSPI.setStatus('current')
ipsaSaPreActIPCompTransformName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 18), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActIPCompTransformName.setStatus('current')
ipsaSaPreActPeerGatewayIdName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 19), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActPeerGatewayIdName.setStatus('current')
ipsaSaPreActLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaSaPreActLastChanged.setStatus('current')
ipsaSaPreActStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 21), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActStorageType.setStatus('current')
ipsaSaPreActRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaSaPreActRowStatus.setStatus('current')
ipsaAhTransformTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2), )
if mibBuilder.loadTexts: ipsaAhTransformTable.setStatus('current')
ipsaAhTransformEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaAhTranName"))
if mibBuilder.loadTexts: ipsaAhTransformEntry.setStatus('current')
ipsaAhTranName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaAhTranName.setStatus('current')
ipsaAhTranMaxLifetimeSec = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranMaxLifetimeSec.setStatus('current')
ipsaAhTranMaxLifetimeKB = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranMaxLifetimeKB.setStatus('current')
ipsaAhTranAlgorithm = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 4), IpsecDoiAuthAlgorithm()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranAlgorithm.setStatus('current')
ipsaAhTranReplayProtection = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranReplayProtection.setStatus('current')
ipsaAhTranReplayWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranReplayWindowSize.setStatus('current')
ipsaAhTranLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaAhTranLastChanged.setStatus('current')
ipsaAhTranStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranStorageType.setStatus('current')
ipsaAhTranRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaAhTranRowStatus.setStatus('current')
ipsaEspTransformTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3), )
if mibBuilder.loadTexts: ipsaEspTransformTable.setStatus('current')
ipsaEspTransformEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaEspTranName"))
if mibBuilder.loadTexts: ipsaEspTransformEntry.setStatus('current')
ipsaEspTranName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaEspTranName.setStatus('current')
ipsaEspTranMaxLifetimeSec = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranMaxLifetimeSec.setStatus('current')
ipsaEspTranMaxLifetimeKB = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranMaxLifetimeKB.setStatus('current')
ipsaEspTranCipherTransformId = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 4), IpsecDoiEspTransform()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranCipherTransformId.setStatus('current')
ipsaEspTranCipherKeyLength = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranCipherKeyLength.setStatus('current')
ipsaEspTranCipherKeyRounds = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranCipherKeyRounds.setStatus('current')
ipsaEspTranIntegrityAlgorithmId = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 7), IpsecDoiAuthAlgorithm()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranIntegrityAlgorithmId.setStatus('current')
ipsaEspTranReplayPrevention = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranReplayPrevention.setStatus('current')
ipsaEspTranReplayWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranReplayWindowSize.setStatus('current')
ipsaEspTranLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaEspTranLastChanged.setStatus('current')
ipsaEspTranStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranStorageType.setStatus('current')
ipsaEspTranRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaEspTranRowStatus.setStatus('current')
ipsaIpcompTransformTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4), )
if mibBuilder.loadTexts: ipsaIpcompTransformTable.setStatus('current')
ipsaIpcompTransformEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaIpcompTranName"))
if mibBuilder.loadTexts: ipsaIpcompTransformEntry.setStatus('current')
ipsaIpcompTranName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaIpcompTranName.setStatus('current')
ipsaIpcompTranMaxLifetimeSec = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranMaxLifetimeSec.setStatus('current')
ipsaIpcompTranMaxLifetimeKB = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranMaxLifetimeKB.setStatus('current')
ipsaIpcompTranAlgorithm = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 4), IpsecDoiIpcompTransform()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranAlgorithm.setStatus('current')
ipsaIpcompTranDictionarySize = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranDictionarySize.setStatus('current')
ipsaIpcompTranPrivateAlgorithm = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranPrivateAlgorithm.setStatus('current')
ipsaIpcompTranLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaIpcompTranLastChanged.setStatus('current')
ipsaIpcompTranStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranStorageType.setStatus('current')
ipsaIpcompTranRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaIpcompTranRowStatus.setStatus('current')
ipsaCredentialTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5), )
if mibBuilder.loadTexts: ipsaCredentialTable.setStatus('current')
ipsaCredentialEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaCredName"))
if mibBuilder.loadTexts: ipsaCredentialEntry.setStatus('current')
ipsaCredName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaCredName.setStatus('current')
ipsaCredType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 2), IpsaCredentialType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredType.setStatus('current')
ipsaCredCredential = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredCredential.setStatus('current')
ipsaCredSize = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaCredSize.setStatus('current')
ipsaCredMngName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredMngName.setStatus('current')
ipsaCredRemoteID = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredRemoteID.setStatus('current')
ipsaCredAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 7), SpdAdminStatus().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredAdminStatus.setStatus('current')
ipsaCredLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaCredLastChanged.setStatus('current')
ipsaCredStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredStorageType.setStatus('current')
ipsaCredRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredRowStatus.setStatus('current')
ipsaCredentialSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6), )
if mibBuilder.loadTexts: ipsaCredentialSegmentTable.setStatus('current')
ipsaCredentialSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaCredName"), (0, "IPSEC-IPSECACTION-MIB", "ipsaCredSegIndex"))
if mibBuilder.loadTexts: ipsaCredentialSegmentEntry.setStatus('current')
ipsaCredSegIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ipsaCredSegIndex.setStatus('current')
ipsaCredSegValue = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredSegValue.setStatus('current')
ipsaCredSegLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaCredSegLastChanged.setStatus('current')
ipsaCredSegStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaCredSegStorageType.setStatus('current')
ipsaCredSegRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaCredSegRowStatus.setStatus('current')
ipsaPeerIdentityTable = MibTable((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7), )
if mibBuilder.loadTexts: ipsaPeerIdentityTable.setStatus('current')
ipsaPeerIdentityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1), ).setIndexNames((0, "IPSEC-IPSECACTION-MIB", "ipsaPeerIdName"), (0, "IPSEC-IPSECACTION-MIB", "ipsaPeerIdPriority"))
if mibBuilder.loadTexts: ipsaPeerIdentityEntry.setStatus('current')
ipsaPeerIdName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ipsaPeerIdName.setStatus('current')
ipsaPeerIdPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ipsaPeerIdPriority.setStatus('current')
ipsaPeerIdType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 3), IpsecDoiIdentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdType.setStatus('current')
ipsaPeerIdValue = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 4), IpsaIdentityFilter()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdValue.setStatus('current')
ipsaPeerIdAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdAddressType.setStatus('current')
ipsaPeerIdAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdAddress.setStatus('current')
ipsaPeerIdCredentialName = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdCredentialName.setStatus('current')
ipsaPeerIdLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsaPeerIdLastChanged.setStatus('current')
ipsaPeerIdStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdStorageType.setStatus('current')
ipsaPeerIdRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsaPeerIdRowStatus.setStatus('current')
ipsaNotificationVariables = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 2, 1))
ipsaNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 2, 0))
ipsaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 1))
ipsaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2))
ipsaIPsecCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 1, 1)).setObjects(("IPSEC-IPSECACTION-MIB", "ipsaPreconfiguredGroup"), ("IPSEC-IPSECACTION-MIB", "ipsaSharedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsaIPsecCompliance = ipsaIPsecCompliance.setStatus('current')
ipsaPreconfiguredGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2, 1)).setObjects(("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionDescription"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionLifetimeSec"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionLifetimeKB"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDoActionLogging"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDoPacketLogging"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDFHandling"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionType"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHSPI"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHTransformName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHSharedSecretName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPSPI"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPTransformName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPEncSecretName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPAuthSecretName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActIPCompSPI"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActIPCompTransformName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActPeerGatewayIdName"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsaPreconfiguredGroup = ipsaPreconfiguredGroup.setStatus('current')
ipsaSharedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2, 2)).setObjects(("IPSEC-IPSECACTION-MIB", "ipsaAhTranMaxLifetimeSec"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranMaxLifetimeKB"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranAlgorithm"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranReplayProtection"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranReplayWindowSize"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaAhTranRowStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranMaxLifetimeSec"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranMaxLifetimeKB"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherTransformId"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherKeyLength"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherKeyRounds"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranIntegrityAlgorithmId"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranReplayPrevention"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranReplayWindowSize"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaEspTranRowStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranDictionarySize"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranAlgorithm"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranMaxLifetimeSec"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranMaxLifetimeKB"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranPrivateAlgorithm"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranRowStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaCredType"), ("IPSEC-IPSECACTION-MIB", "ipsaCredCredential"), ("IPSEC-IPSECACTION-MIB", "ipsaCredMngName"), ("IPSEC-IPSECACTION-MIB", "ipsaCredSize"), ("IPSEC-IPSECACTION-MIB", "ipsaCredRemoteID"), ("IPSEC-IPSECACTION-MIB", "ipsaCredAdminStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaCredLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaCredStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaCredRowStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaCredSegValue"), ("IPSEC-IPSECACTION-MIB", "ipsaCredSegLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaCredSegStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaCredSegRowStatus"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdValue"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdType"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdAddress"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdAddressType"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdCredentialName"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdLastChanged"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdStorageType"), ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsaSharedGroup = ipsaSharedGroup.setStatus('current')
mibBuilder.exportSymbols("IPSEC-IPSECACTION-MIB", IpsecDoiEncapsulationMode=IpsecDoiEncapsulationMode, IpsecDoiIdentType=IpsecDoiIdentType, IpsecDoiEspTransform=IpsecDoiEspTransform, ipsaAhTranReplayWindowSize=ipsaAhTranReplayWindowSize, ipsaSaPreActIPCompTransformName=ipsaSaPreActIPCompTransformName, ipsaIpcompTranPrivateAlgorithm=ipsaIpcompTranPrivateAlgorithm, ipsaPeerIdAddressType=ipsaPeerIdAddressType, ipsaAhTranStorageType=ipsaAhTranStorageType, ipsaEspTranName=ipsaEspTranName, ipsaSaPreActSADirection=ipsaSaPreActSADirection, ipsaEspTranReplayWindowSize=ipsaEspTranReplayWindowSize, ipsaPeerIdName=ipsaPeerIdName, ipsaSharedGroup=ipsaSharedGroup, ipsaEspTranStorageType=ipsaEspTranStorageType, ipsaIpcompTranRowStatus=ipsaIpcompTranRowStatus, ipsaSaPreActActionType=ipsaSaPreActActionType, ipsaPeerIdRowStatus=ipsaPeerIdRowStatus, ipsaAhTranMaxLifetimeSec=ipsaAhTranMaxLifetimeSec, ipsaEspTranCipherKeyLength=ipsaEspTranCipherKeyLength, ipsaCredentialSegmentTable=ipsaCredentialSegmentTable, ipsaNotificationVariables=ipsaNotificationVariables, ipsaIpcompTransformTable=ipsaIpcompTransformTable, ipsaCredLastChanged=ipsaCredLastChanged, ipsaCredStorageType=ipsaCredStorageType, IpsecDoiAuthAlgorithm=IpsecDoiAuthAlgorithm, ipsaSaPreconfiguredActionTable=ipsaSaPreconfiguredActionTable, ipsaSaPreActPeerGatewayIdName=ipsaSaPreActPeerGatewayIdName, ipsaCredRemoteID=ipsaCredRemoteID, PYSNMP_MODULE_ID=ipsaMIB, ipsaIpcompTranDictionarySize=ipsaIpcompTranDictionarySize, ipsaPreconfiguredGroup=ipsaPreconfiguredGroup, ipsaIpcompTransformEntry=ipsaIpcompTransformEntry, ipsaIPsecCompliance=ipsaIPsecCompliance, ipsaPeerIdType=ipsaPeerIdType, ipsaAhTranRowStatus=ipsaAhTranRowStatus, ipsaGroups=ipsaGroups, ipsaAhTranMaxLifetimeKB=ipsaAhTranMaxLifetimeKB, ipsaAhTransformTable=ipsaAhTransformTable, ipsaCredentialEntry=ipsaCredentialEntry, ipsaCredCredential=ipsaCredCredential, ipsaIpcompTranMaxLifetimeKB=ipsaIpcompTranMaxLifetimeKB, ipsaNotificationObjects=ipsaNotificationObjects, IpsaIdentityFilter=IpsaIdentityFilter, ipsaCredRowStatus=ipsaCredRowStatus, ipsaIpcompTranMaxLifetimeSec=ipsaIpcompTranMaxLifetimeSec, ipsaCredentialSegmentEntry=ipsaCredentialSegmentEntry, ipsaNotifications=ipsaNotifications, ipsaMIB=ipsaMIB, IpsecDoiIpcompTransform=IpsecDoiIpcompTransform, ipsaEspTransformEntry=ipsaEspTransformEntry, ipsaEspTranMaxLifetimeKB=ipsaEspTranMaxLifetimeKB, ipsaIpcompTranAlgorithm=ipsaIpcompTranAlgorithm, ipsaCredName=ipsaCredName, ipsaPeerIdLastChanged=ipsaPeerIdLastChanged, ipsaConfigObjects=ipsaConfigObjects, ipsaConformanceObjects=ipsaConformanceObjects, ipsaSaPreActActionLifetimeKB=ipsaSaPreActActionLifetimeKB, ipsaSaPreActAHSPI=ipsaSaPreActAHSPI, ipsaEspTranCipherKeyRounds=ipsaEspTranCipherKeyRounds, ipsaPeerIdStorageType=ipsaPeerIdStorageType, ipsaSaPreActActionName=ipsaSaPreActActionName, ipsaCredentialTable=ipsaCredentialTable, ipsaSaPreActESPTransformName=ipsaSaPreActESPTransformName, ipsaCredSegRowStatus=ipsaCredSegRowStatus, ipsaSaPreActESPSPI=ipsaSaPreActESPSPI, ipsaEspTranCipherTransformId=ipsaEspTranCipherTransformId, ipsaIpcompTranLastChanged=ipsaIpcompTranLastChanged, ipsaEspTranRowStatus=ipsaEspTranRowStatus, ipsaSaPreActActionDescription=ipsaSaPreActActionDescription, ipsaIpcompTranStorageType=ipsaIpcompTranStorageType, ipsaPeerIdCredentialName=ipsaPeerIdCredentialName, ipsaEspTranMaxLifetimeSec=ipsaEspTranMaxLifetimeSec, ipsaPeerIdAddress=ipsaPeerIdAddress, IpsaCredentialType=IpsaCredentialType, ipsaPeerIdentityEntry=ipsaPeerIdentityEntry, ipsaAhTranReplayProtection=ipsaAhTranReplayProtection, ipsaSaPreActAHTransformName=ipsaSaPreActAHTransformName, ipsaCompliances=ipsaCompliances, ipsaAhTranName=ipsaAhTranName, ipsaCredType=ipsaCredType, ipsaSaPreActDoPacketLogging=ipsaSaPreActDoPacketLogging, ipsaEspTransformTable=ipsaEspTransformTable, ipsaSaPreActESPAuthSecretName=ipsaSaPreActESPAuthSecretName, ipsaEspTranLastChanged=ipsaEspTranLastChanged, ipsaCredSegValue=ipsaCredSegValue, ipsaSaPreActRowStatus=ipsaSaPreActRowStatus, ipsaCredSegIndex=ipsaCredSegIndex, ipsaCredSegStorageType=ipsaCredSegStorageType, ipsaEspTranIntegrityAlgorithmId=ipsaEspTranIntegrityAlgorithmId, ipsaSaPreActAHSharedSecretName=ipsaSaPreActAHSharedSecretName, ipsaSaPreActDFHandling=ipsaSaPreActDFHandling, ipsaPeerIdValue=ipsaPeerIdValue, ipsaPeerIdPriority=ipsaPeerIdPriority, ipsaPeerIdentityTable=ipsaPeerIdentityTable, ipsaCredSize=ipsaCredSize, ipsaAhTranLastChanged=ipsaAhTranLastChanged, ipsaSaPreActDoActionLogging=ipsaSaPreActDoActionLogging, ipsaSaPreconfiguredActionEntry=ipsaSaPreconfiguredActionEntry, ipsaEspTranReplayPrevention=ipsaEspTranReplayPrevention, ipsaSaPreActIPCompSPI=ipsaSaPreActIPCompSPI, ipsaSaPreActStorageType=ipsaSaPreActStorageType, ipsaAhTransformEntry=ipsaAhTransformEntry, ipsaCredAdminStatus=ipsaCredAdminStatus, ipsaSaPreActActionLifetimeSec=ipsaSaPreActActionLifetimeSec, ipsaAhTranAlgorithm=ipsaAhTranAlgorithm, ipsaIpcompTranName=ipsaIpcompTranName, ipsaCredSegLastChanged=ipsaCredSegLastChanged, ipsaSaPreActESPEncSecretName=ipsaSaPreActESPEncSecretName, ipsaSaPreActLastChanged=ipsaSaPreActLastChanged, ipsaCredMngName=ipsaCredMngName)

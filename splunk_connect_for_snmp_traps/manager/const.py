from pysnmp.entity import config

AuthProtocolMap = {
    "MD5": config.usmHMACMD5AuthProtocol,
    "SHA": config.usmHMACSHAAuthProtocol,
    "SHA224": config.usmHMAC128SHA224AuthProtocol,
    "SHA256": config.usmHMAC192SHA256AuthProtocol,
    "SHA384": config.usmHMAC256SHA384AuthProtocol,
    "SHA512": config.usmHMAC384SHA512AuthProtocol,
    "NONE": config.usmNoAuthProtocol,
}

PrivProtocolMap = {
    "DES": config.usmDESPrivProtocol,
    "3DES": config.usm3DESEDEPrivProtocol,
    "AES": config.usmAesCfb128Protocol,
    "AES128": config.usmAesCfb128Protocol,
    "AES192": config.usmAesCfb192Protocol,
    "AES192BLMT": config.usmAesBlumenthalCfb192Protocol,
    "AES256": config.usmAesCfb256Protocol,
    "AES256BLMT": config.usmAesBlumenthalCfb256Protocol,
    "NONE": config.usmNoPrivProtocol,
}

from pysnmp.entity import config

AuthProtocolMap = {
    "NOAUTH": config.usmNoAuthProtocol,
    "MD5": config.usmHMACMD5AuthProtocol,
    "SHA": config.usmHMACSHAAuthProtocol,
}

PrivProtocolMap = {
    "NOPRIV": config.usmNoPrivProtocol,
    "DES": config.usmDESPrivProtocol,
    "3DES": config.usm3DESEDEPrivProtocol,
    "AES": config.usmAesCfb128Protocol,
    "AES256": config.usmAesCfb256Protocol,
    "AES192": config.usmAesCfb192Protocol,
}
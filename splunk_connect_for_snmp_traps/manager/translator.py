from pysnmp.smi import builder, view, compiler, rfc1902
import os
import json
import csv
import logging

logger = logging.getLogger(__name__)

class Translator:
    def __init__(self, server_config):
        self._server_config = server_config
        self._custom_translation_table = self.get_custom_translation_table()


    # Translate SNMP PDU varBinds into MIB objects using MIB
    def mib_translator(self, name, val):
        # Assemble MIB browser
        snmp_config = self._server_config['snmp']
        mibBuilder = builder.MibBuilder()
        mibViewController = view.MibViewController(mibBuilder)
        compiler.addMibCompiler(mibBuilder, sources=snmp_config['mibs']['url'])

        # Pre-load MIB modules we expect to work with
        mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-COMMUNITY-MIB')

        # Run var-binds through MIB resolver
        try:
            varBind = rfc1902.ObjectType(rfc1902.ObjectIdentity(name), val).resolveWithMib(mibViewController)
            logger.debug(f'* Translated PDU: {varBind.prettyPrint()}')
            return varBind.prettyPrint()
        except Exception as e:
            logger.error(f'Error happended in translateion: {e}')
        finally:
            pass


    # Translate SNMP PDU varBinds into MIB objects using custom translation table
    def custom_translator(self, oid):
        return self._custom_translation_table.get(oid, None)
        

    # Read the custom mib translation table into memory
    def get_custom_translation_table(self):
        translation_table = {}
        file_path = os.path.join(os.getcwd(), 'lookups/custom_mib_string_table.csv')
        logger.debug(f'file_path {file_path}')
        with open(file_path) as files:
            reader = csv.reader(files)
            next(reader) # skip header
            for row in reader:
                translation_table[row[0]] = row[1]
        return translation_table
    
    # Format and translate the trap events
    def format_trap_event(self, var_binds):
        trap_event_string = ''
        offset = 0

        for name, val in var_binds:
            logger.debug(f'{name.prettyPrint()} = {val.prettyPrint()}')

            # extract oid and value
            oid = name.prettyPrint()
            value = val.prettyPrint()

            # Extrat the types
            cursor = '->'
            nameType = name.prettyPrintType()
            if cursor in nameType:
                nameType = nameType.split(cursor)[1].strip()
                
            valType = val.prettyPrintType()
            if cursor in valType:
                valType = valType.split(cursor)[1].strip()

            # custom translation 
            custom_translated_oid = self.custom_translator(oid)
            custom_translated_value = value
            # tranlate value ONLY when it is oid
            if valType == 'ObjectIdentifier':         
                custom_translated_value = self.custom_translator(value)

            # Construct trap string
            offset += 1
            original_oid = 'oid{offset} = {oid}'.format(offset=offset, oid=oid)
            oid_type_string = 'oid_type{offset} = {oid_type}'.format(offset=offset, oid_type=nameType)
            original_value = 'value{offset} = {value}'.format(offset=offset, value=value)
            val_type_string = 'val_type{offset} = {val_type}'.format(offset=offset, val_type=valType)
            translated_mib_string = 'mib{offset} = {mib}'.format(offset=offset, mib=self.mib_translator(name, val))
            custom_translated_mib_string = 'custom_mib{offset} = {custom_translated_oid} = {custom_translated_value}'.format(offset=offset, custom_translated_oid=custom_translated_oid, custom_translated_value=custom_translated_value) 
            trap_event_string += '\n'.join([original_oid, oid_type_string, original_value, val_type_string, translated_mib_string, custom_translated_mib_string])
            trap_event_string += '\n\n'

        trap_event_string = trap_event_string.rstrip("\n") # remove trailing newline      
        logger.debug(f'--- Trap Event String ---')
        logger.debug(trap_event_string)
        return trap_event_string
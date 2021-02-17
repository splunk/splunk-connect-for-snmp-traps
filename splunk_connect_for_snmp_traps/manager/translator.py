from pysnmp.smi import builder, view, compiler, rfc1902
import os
import json
import csv
import logging
import sys
import subprocess

from pysmi import debug as pysmi_debug
pysmi_debug.setLogger(pysmi_debug.Debug('compiler'))

logger = logging.getLogger(__name__)


class Translator:
    def __init__(self, server_config):
        self._server_config = server_config
        self._custom_translation_table = self.get_custom_translation_table()
        self._load_list = server_config["snmp"]["mibs"]["load_list"]
        self._mib_builder, self._mib_view_controller = self.build_mib_compiler(self._load_list)
        # Execute the 1st translation to force mibs to be ready to use
        self.first_mib_translation_trigger()

    def build_mib_compiler(self, load_list):
        # Assemble MIB browser
        snmp_config = self._server_config["snmp"]
        mibBuilder = builder.MibBuilder()
        mibViewController = view.MibViewController(mibBuilder)
        compiler.addMibCompiler(mibBuilder, sources=snmp_config["mibs"]["url"])

        # Optionally set an alternative path to compiled MIBs
        logger.debug('Setting MIB sources...')
        mibBuilder.addMibSources(builder.DirMibSource(snmp_config["mibs"]["dir"]))
        logger.debug(mibBuilder.getMibSources())
        logger.debug('done')

        mib_file_path = os.path.join(os.getcwd(), self._load_list)
        logger.debug(f"mib_file_path {mib_file_path}")
        with open(mib_file_path) as mib_files:
            reader = csv.reader(mib_files)
            cnt = 0
            for row in reader:
                module = row[0]
                try:
                    mibBuilder.loadModules(module)
                    cnt += 1
                    logger.debug(f"[-] {cnt} Loaded module: {module}")
                except Exception as e:
                    logger.error(f"Error happened during load module: {e}")
                    pass
       
        logger.debug("compiler is loaded")

        return mibBuilder, mibViewController
    
    def first_mib_translation_trigger(self):
        # This is a test TRAP PDU
        var_binds = [
            ('1.3.6.1.2.1.1.3.0', 12345),
            ('1.3.6.1.6.3.1.1.4.1.0', '1.3.6.1.6.3.1.1.5.2')
        ]

        for name, val in var_binds:
            self.mib_translator(name, val)
        logger.debug("mib_translator is ready to use!")

    
    # Check if the oid was translated properly
    def is_not_translated(self, org_val, trans_val):
        # if translated value equals to original value, it was not translated at all
        if org_val == trans_val:
            return True
        temp = trans_val.split(".")
        logger.debug(f"temp: {temp}")
        # if the second last number of the oid is numeric, it was not translated properly
        return len(temp) >= 2 and temp[-2].isnumeric()

    # Find mib module based on the oid
    def find_mib_file(self, oid):
        snmp_config = self._server_config["snmp"]
        value_tuple='"'+str(oid).replace(".",", ")+'"'
        try:
            val_direct_output = subprocess.check_output("grep -rl {value} {path}".format(value=value_tuple, path=snmp_config["mibs"]["dir"]), shell=True)
        except Exception as e:
            logger.debug(f"Cannot find the oid: {e}")
            # TODO : write the oid to mongo
            return

        logger.debug(f"val_direct_output: {val_direct_output}")
        mib_name =str(val_direct_output, 'utf-8').split("/")[-1].strip()[:-3]
        logger.debug(f"mib_name: {mib_name}")
        self.load_extra_mib(mib_name)


    # Load additional mib module
    def load_extra_mib(self, mib_module):
        try:
            self._mib_builder.loadModules(mib_module)
            logger.debug(f"[-] Loaded module: {mib_module}")
        except Exception as e:
            logger.error(f"Error happened during load module: {e}")
            pass


    # Translate SNMP PDU varBinds into MIB objects using MIB
    def mib_translator(self, name, val):
        
        # Run var-binds through MIB resolver
        try:
            varBind = rfc1902.ObjectType(
                rfc1902.ObjectIdentity(name), val
            ).resolveWithMib(self._mib_view_controller)
            logger.debug(f"* Translated PDU: {varBind.prettyPrint()}")
            trans_string = varBind.prettyPrint().replace(" = ", "=")
            trans_oid = trans_string.split("=")[0]
            trans_val = trans_string.split("=")[1]
            valType = val.__class__.__name__

            # TODO check if the OIDs inside mongo, if it is, skip the following steps
            
            try:
                # Check if oid was translated properly
                if self.is_not_translated(name, trans_oid):
                    self.find_mib_file(name)
              
                # Check if value was translated properly if value is OID type
                if valType == "ObjectIdentifier":
                    if self.is_not_translated(val, trans_val):
                        self.find_mib_file(val)

                # Re-translated with the extra mibs   
                varBind = rfc1902.ObjectType(
                        rfc1902.ObjectIdentity(name), val
                    ).resolveWithMib(self._mib_view_controller)
                logger.debug(f"* Re-Translated PDU: {varBind.prettyPrint()}")
            except Exception as e:
                logger.debug(f"Error happended during translation checking: {e}")
                pass               
          
            return varBind.prettyPrint().replace(" = ", "=")
        except Exception as e:
            logger.error(f"Error happended in translation: {e}")
        finally:
            pass


    # Translate SNMP PDU varBinds into MIB objects using custom translation table
    def custom_translator(self, oid):
        return self._custom_translation_table.get(oid, None)


    # Read the custom mib translation table into memory
    def get_custom_translation_table(self):
        translation_table = {}
        logger.debug(f"cwd {os.getcwd()}")
        file_path = os.path.join(os.getcwd(), "lookups/custom_mib_string_table.csv")
        logger.debug(f"file_path {file_path}")
        with open(file_path) as files:
            reader = csv.reader(files)
            next(reader)  # skip header
            for row in reader:
                translation_table[row[0]] = row[1]
        return translation_table

    # Format and translate the trap events
    def format_trap_event(self, var_binds):
        trap_event_string = ""
        offset = 0

        for name, val in var_binds:
            logger.debug(f"{name.prettyPrint()} = {val.prettyPrint()}")

            # extract oid and value
            oid = name.prettyPrint()
            value = val.prettyPrint()
            # Extrat the types
            nameType = name.__class__.__name__
            valType = val.__class__.__name__

            # custom translation
            custom_translated_oid = self.custom_translator(oid)
            custom_translated_value = value
            # tranlate value ONLY when it is oid
            if valType == "ObjectIdentifier":
                custom_translated_value = self.custom_translator(value)

            # Construct trap string
            offset += 1
            original_oid = "{oid}={value}".format(offset=offset, oid=oid, value=value)
            oid_type_string = "oid-type{offset}={oid_type}".format(
                offset=offset, oid_type=nameType
            )
            translated_mib_string = self.mib_translator(name, val)

            if custom_translated_oid:
                custom_translated_mib_string = (
                    "{custom_translated_oid}={custom_translated_value}".format(
                        offset=offset,
                        custom_translated_oid=custom_translated_oid,
                        custom_translated_value=custom_translated_value,
                    )
                )
            else:
                custom_translated_oid = ""

            original_value = "value{offset}={value}".format(offset=offset, value=value)
            val_type_string = "value{offset}-type={val_type}".format(
                offset=offset, val_type=valType
            )
            trap_event_string += " ".join(
                [
                    oid_type_string,
                    val_type_string,
                    original_oid,
                    original_value,
                    translated_mib_string,
                    custom_translated_mib_string,
                    #
                ]
            )
            trap_event_string += "\n"

        trap_event_string = trap_event_string.rstrip("\n")  # remove trailing newline
        logger.debug(f"--- Trap Event String ---")
        logger.debug(trap_event_string)
        return trap_event_string
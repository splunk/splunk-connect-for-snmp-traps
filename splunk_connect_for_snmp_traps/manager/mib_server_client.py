#   ########################################################################
#   Copyright 2021 Splunk Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#   ########################################################################
import json
import logging
import os

from aiohttp import ClientSession
from splunk_connect_for_snmp_traps.utilities import format_value_for_mib_server

logger = logging.getLogger(__name__)


async def get_translation(var_binds, mib_server_url):
    """
    @param var_binds: var_binds object getting from SNMP agents
    @param mib_server_url: URL of SNMP MIB server
    @return: translated string
    """

    payload = {}
    var_binds_list = []
    trap_event_string = ""
    for name, val in var_binds:
        var_bind = {
            "oid": str(name),
            "oid_type": name.__class__.__name__,
            "val": format_value_for_mib_server(val, val.__class__.__name__),
            "val_type": val.__class__.__name__,
        }
        var_binds_list.append(var_bind)
        org_var_bind = '{oid}="{value}"'.format(oid=str(name), value=str(val))
        trap_event_string += " " + org_var_bind

    payload["var_binds"] = var_binds_list
    payload = json.dumps(payload)

    headers = {"Content-type": "application/json"}
    endpoint = "translation"
    TRANSLATION_URL = os.path.join(mib_server_url.strip("/"), endpoint)
    logger.debug(f"[-] TRANSLATION_URL: {TRANSLATION_URL}")

    try:
        session = ClientSession()
        resp = await session.post(TRANSLATION_URL, headers=headers, data=payload)
        if resp.status == 200:
            trap_event_string = await resp.text()
        if resp.status != 200:
            logger.error(f"[-] Mib Server API Error with code: {resp.status}")
    except Exception as e:
        logger.error(
            f"MIB server is unreachable! Error happened while communicating to MIB server to perform "
            f"the Translation: {e}"
        )

    return trap_event_string

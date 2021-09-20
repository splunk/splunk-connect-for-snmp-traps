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

import aiohttp
import backoff
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
    translation_url = os.path.join(mib_server_url.strip("/"), endpoint)
    logger.debug(f"[-] translation_url: {translation_url}")

    try:
        trap_event_string = await get_url(translation_url, headers, payload)
    except Exception as e:
        logger.error(
            f"Error getting translation from MIB Server: {e} "
        )

    return trap_event_string


@backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=3)
async def get_url(url, headers, payload):
    async with ClientSession(raise_for_status=True) as session:
        resp = await session.post(url, headers=headers, data=payload)
        return await resp.text()

import logging
import json
import requests
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


def get_translation(var_binds, mib_server_url):
    """
    @param var_binds: var_binds object getting from SNMP agents
    @param mib_server_url: URL of SNMP MIB server
    @return: translated string
    """
    # Construct the payload
    payload = {}
    var_binds_list = []
    trap_event_string = ""
    for name, val in var_binds:
        var_bind = {
            "oid": str(name),
            "oid_type": name.__class__.__name__,
            "val": str(val),
            "val_type": val.__class__.__name__
        }
        var_binds_list.append(var_bind)
        org_var_bind = '{oid}="{value}"'.format(oid=str(name), value=str(val))
        trap_event_string += " " + org_var_bind
    payload["var_binds"] = var_binds_list
    payload = json.dumps(payload)
    
    # trap_event_string = payload

    # Send the POST request to mib server
    headers = {'Content-type': 'application/json'}
    endpoint = "translation"
    TRANSLATION_URL = os.path.join(mib_server_url.strip('/'), endpoint)
    logger.debug(f"[-] TRANSLATION_URL: {TRANSLATION_URL}")

    try:
        # resp = requests.request("POST", TRANSLATION_URL, headers=headers, data=payload)
        # use Session with Retry
        retry_strategy = Retry(
            total=3,
            backoff_factor = 1,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        resp = session.post(TRANSLATION_URL, headers=headers, data=payload)
        # If varBinds gets translated, overide it with the translated one
        if resp.status_code == 200: 
            trap_event_string = resp.text
        if resp.status_code != 200:
            logger.error(f"[-] Mib Server API Error with code: {resp.status_code}")
    except Exception as e:
        logger.error(f"MIB server is unreachable! Error happened while communicating to MIB server to perform the Translation: {e}")
        
    return trap_event_string

from mpayg_iot.sim_management import base
from mpayg_iot import globals
from mpayg_domain.hub import base as hub_base
import requests
import json


class SIMInfoService(base.SIMInfoService):

    #
    # Aeris implementation of SIM information service
    #

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def get_sim_info(cls, hub: hub_base.Hub):
        return cls.__get_device_network_status_api(cls.__prepare_get_device_network_status_url(hub))

    @classmethod
    def __get_device_network_status_api(self, url: str) -> dict:

        print("url: {}".format(url))

        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)

        return response

    @classmethod
    def __prepare_get_device_network_status_url(self, hub: hub_base.Hub) -> str:

        base_url = "{}?accountID={}&{}={}&email={}&apiKey={}".format(
            globals.AERIS_AERADMIN_DEVICE_NETWORK_DETAILS_URL_ENDPOINT,
            globals.AERIS_ACCOUNT_ID,
            "IMSI",
            hub.imsi,
            globals.AERIS_ACCOUNT_EMAIL,
            globals.AERIS_ACCOUNT_API_KEY,
        )

        return base_url


class SIMInfoHelper(base.SIMInfoHelper):

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def prepare_info(cls, aeris_response) -> hub_base.Hub:

        hub = hub_base.Hub
        resp_object = json.loads(aeris_response.text)

        hub.imsi = resp_object['activeProfile']['IMSI']
        hub.iccid = resp_object['activeProfile']['ICCID']
        hub.ip = resp_object['activeProfile']['ipAddress']

        return hub

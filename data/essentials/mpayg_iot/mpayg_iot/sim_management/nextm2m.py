from mpayg_iot.sim_management import base
from mpayg_domain.hub import base as hub_base
from mpayg_iot import globals
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport


class SIMInfoService(base.SIMInfoService):

    #
    # NextM2M implementation of SIM information service
    #

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def get_sim_info(cls, hub: hub_base.Hub):

        m2muser = globals.NEXTM2M_API_USER
        m2mpassword = globals.NEXTM2M_API_PASSWORD

        return cls.__get_sim_api(cls.__prepare_get_sim_url(), m2muser, m2mpassword, hub)

    @classmethod
    def __get_sim_api(self, url: str, m2muser: str, m2mpassword: str, hub: hub_base.Hub) -> dict:

        session = Session()
        session.auth = HTTPBasicAuth(m2muser, m2mpassword)
        client = Client(url, transport=Transport(session=session))
        result_sim_info = None
        hub_id = hub.id
        imsi = hub.imsi

        if imsi:
            result_sim_info = client.service.getSim(imsi=imsi)
            print("NextM2M getSim() result: ", result_sim_info)
        else:
            raise Exception("IMSI for hub id {} is invalid: {}".format(hub_id, imsi))

        return result_sim_info

    @classmethod
    def __prepare_get_sim_url(self) -> str:

        base_url = "{}".format(globals.NEXTM2M_API_WSDL_URL)

        return base_url


class SIMInfoHelper(base.SIMInfoHelper):

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def prepare_info(cls, nextm2m_response) -> hub_base.Hub:
        hub = hub_base.Hub
        hub.imsi = nextm2m_response["imsi"]
        hub.iccid = nextm2m_response["iccId"]
        hub.ip = nextm2m_response["ip"]

        return hub

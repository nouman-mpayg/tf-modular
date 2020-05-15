from mpayg_iot import globals
from mpayg_iot.m2m_sms.mo import nextm2m
from mpayg_iot.m2m_sms.mo import aeris
from mpayg_iot.m2m_sms.mo import base


class MOSMSAPIFactory:

    @classmethod
    def get_instance(cls, provider, mock=False) -> base.MOSMSAPIService:

        if provider == globals.M2M_PROVIDER_NEXTM2M_ID:

            if not mock:
                return nextm2m.MOSMSAPIService()
            else:
                return nextm2m.MOSMSMockedAPIService()

        elif provider == globals.M2M_PROVIDER_AERIS_ID:

            if not mock:
                return aeris.MOSMSAPIService()
            else:
                return aeris.MOSMSMockedAPIService()

        else:
            raise NotImplementedError

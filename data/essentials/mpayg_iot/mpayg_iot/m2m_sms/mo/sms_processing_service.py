from mpayg_iot.m2m_sms.mo import nextm2m
from mpayg_iot.m2m_sms.mo import aeris
from mpayg_iot import globals


class MOSMSProcessingServiceFactory:

    @classmethod
    def get_instance(cls, provider, connection: dict, mock=False):

        if provider == globals.M2M_PROVIDER_NEXTM2M_ID:

            if not mock:

                if connection is not None and connection.get('conn', None) is not None and connection.get('cur', None) is not None:
                    return nextm2m.MOSMSProcessingService(connection)
                else:
                    raise Exception("With this non-mocked provider connection not provided")
            else:
                return nextm2m.MOSMSMockedProcessingService(connection)

        elif provider == globals.M2M_PROVIDER_AERIS_ID:

            if not mock:
                if connection is not None and connection.get('conn', None) is not None and connection.get('cur', None) is not None:
                    return aeris.MOSMSProcessingService(connection)
                else:
                    raise Exception("With this non-mocked provider connection not provided")
            else:
                return aeris.MOSMSMockedProcessingService(connection)

        else:
            raise NotImplementedError

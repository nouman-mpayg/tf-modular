from mpayg_iot import globals
from mpayg_iot.sim_management import nextm2m
from mpayg_iot.sim_management import aeris
from mpayg_iot.sim_management import mock


class SIMInfoServiceFactory:

    @classmethod
    def get_instance(cls, provider, mock=False):

        print("provider: {}".format(provider))

        if mock is False:

            if provider == globals.M2M_PROVIDER_NEXTM2M_ID:

                return nextm2m.SIMInfoService()

            elif provider == globals.M2M_PROVIDER_AERIS_ID:

                return aeris.SIMInfoService()

            else:

                raise NotImplementedError
        else:

            return mock.SIMInfoService()


class SIMInfoHelperFactory:

    #
    # Factory class which provides provider specific service
    #

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls, provider, mock=False):

        if mock is False:

            if provider == globals.M2M_PROVIDER_AERIS_ID:

                return aeris.SIMInfoHelper()

            elif provider == globals.M2M_PROVIDER_NEXTM2M_ID:

                return nextm2m.SIMInfoHelper()

            else:

                raise NotImplementedError
        else:

            raise NotImplementedError

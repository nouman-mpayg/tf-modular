from abc import ABCMeta, abstractmethod
from mpayg_domain.request import service as request_service
from mpayg_domain.hub import service as hub_service
from mpayg_domain import globals


class MOSMSAPIService(metaclass=ABCMeta):

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def retrieve_sms(cls) -> dict:
        pass


class MOSMSProcessingService(metaclass=ABCMeta):

    @classmethod
    def __init__(self, connection: dict):
        self.conn = connection['conn'] if connection.get('conn', None) else None
        self.cur = connection['cur'] if connection.get('cur', None) else None
        self.req_service_factory = request_service.RequestServiceFactory()
        self.req_service = self.req_service_factory.get_instance(provider=globals.DOMAIN_PROVIDER_POSTGRES, connection=connection)
        self.hub_service_factory = hub_service.HubServiceFactory()
        self.hub_service = self.hub_service_factory.get_instance(provider=globals.DOMAIN_PROVIDER_POSTGRES, connection=connection)

    @classmethod
    def process_sms(cls, mo_sms: list):

        print("process_mo_sms() invoked")

        status = False

        if cls.conn is not None and cls.cur is not None:

            if len(mo_sms) > 0:
                for mo_sms in mo_sms:
                    cls.process_each_sms(mo_sms)

                status = True

            else:
                print("mo_sms is empty. Doing nothing.")

        else:
            print("DB connection is not available. So not saving the SMSes in DB")

        print("process_mo_sms() returning")

        return status

    @abstractmethod
    def process_each_sms(cls, mo_sms):
        pass

    @classmethod
    def validate_sms_format(cls, message: str) -> bool:

        if len(message.split(message[3])) > 1:
            return True
        else:
            return False

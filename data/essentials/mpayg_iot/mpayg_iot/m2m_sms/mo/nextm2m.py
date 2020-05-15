import string
import requests
from mpayg_iot import globals as iot_globals
from mpayg_iot.m2m_sms.mo import base
from mpayg_iot.m2m_sms.mo import request_record_helper
from mpayg_domain.hub import base as hub_base
from requests import Session
from datetime import datetime
from dateutil import tz


class MOSMSAPIService(base.MOSMSAPIService):

    @classmethod
    def __init__(cls):
        return

    @classmethod
    def retrieve_sms(cls) -> dict:

        print("retrieve_sms() invoked")

        print("Retrieving SMSs from {} network...".format(iot_globals.M2M_PROVIDER_NEXTM2M_ID))

        wsdl_url = iot_globals.NEXTM2M_API_WSDL_URL
        user = iot_globals.NEXTM2M_API_USER
        password = iot_globals.NEXTM2M_API_PASSWORD

        print("wsdl_url: {}".format(wsdl_url))
        print("user: {}***".format(user[:2]))
        print("password: {}***".format(password[:2]))

        try:
            session = Session()
            session.auth = (user, password)
            url = iot_globals.NEXTM2M_API_SOAP_URL
            msg = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://neoconsult.dk/nextm2m/chayn/webservices/services/server">
                   <soapenv:Header />
                   <soapenv:Body>
                      <ser:retrieveNewSms />
                   </soapenv:Body>
                </soapenv:Envelope>
            """
            headers = {'Content-Type': 'text/xml'}

            print("url: ", url)
            print("body: ", msg)

            response = session.post(url, data=msg, headers=headers)

            # If the HTTP GET request was served
            if response.status_code == 200:

                print("response.text: ", response.text)

                # remove non-printable characters from response string
                filtered_string = "".join(s for s in response.text if s in string.printable)

                response._content = filtered_string

            else:
                print("response is not 200: ", response.text)

        except Exception as e:

            print("Error occurred. Details: {}".format(e))

            raise Exception()

        finally:
            print("retrieve_sms() returning")

        return response


class MOSMSMockedAPIService(MOSMSAPIService):

    @classmethod
    def __init__(cls):
        return

    @classmethod
    def retrieve_sms(cls) -> dict:
        response = requests.models.Response()
        response.status_code = 200
        response.encoding = "utf-8"
        response._content = """<?xml version="1.0" encoding="UTF-8"?>
            <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
               <S:Body>
                  <ns2:retrieveNewSmsResponse xmlns:ns2="http://neoconsult.dk/nextm2m/chayn/webservices/services/server">
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>904047102858019</imsi>
                        <insertedDate>2019-04-26T08:24:58+01:00</insertedDate>
                        <message>R06|42efd0121f|1|00|00|80|00|0c|0000|0000|0000|0000</message>
                        <status>Delivered</status>
                     </return>
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>204047102858019</imsi>
                        <insertedDate>2019-04-26T08:24:58+01:00</insertedDate>
                        <message>R06|92efd0121f|1|00|00|80|00|0c|0000|0000|0000|0000</message>
                        <status>Delivered</status>
                     </return>
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>204047102858019</imsi>
                        <insertedDate>2019-04-29T02:43:01+01:00</insertedDate>
                        <message>C51|2c|1|001|007|001|03|000b|3498|0|2019-04-28 23:02:00</message>
                        <status>Delivered</status>
                     </return>
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>204047102858019</imsi>
                        <insertedDate>2019-04-28T15:20:03+01:00</insertedDate>
                        <message>R00|uwk00ljv0zl1ju|1|SH1|3|1.11.1</message>
                        <status>Delivered</status>
                     </return>
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>204043396402311</imsi>
                        <insertedDate>2019-04-29T23:46:02+01:00</insertedDate>
                        <message>C51|23|0|00|02|+0e|7d|00b2|00|02|+0f|7c|00bc|00|02|+13|7b|00e5|00|02|+12|7a|00d7|00|02|+0a|7b|0071|00|00|+05|7b|003b|201</message>
                        <status>Delivered</status>
                     </return>
                     <return>
                        <direction>Inbound</direction>
                        <from>Vodafone SMS MO</from>
                        <imsi>204047102858019</imsi>
                        <insertedDate>2019-04-29T23:46:05+01:00</insertedDate>
                        <message>9-04-29 22:06:00</message>
                        <status>Delivered</status>
                     </return>
                  </ns2:retrieveNewSmsResponse>
               </S:Body>
            </S:Envelope>
        """

        # remove non-printable characters from response string
        filtered_string = "".join(s for s in response._content if s in string.printable)

        response._content = filtered_string

        return response


class MOSMSProcessingService(base.MOSMSProcessingService):

    @classmethod
    def process_each_sms(cls, mo_sms):

        print("mo_sms: {}".format(mo_sms))

        message = mo_sms['message']

        if cls.validate_sms_format(message):

            date_time = mo_sms['insertedDate']
            hub = hub_base.Hub()
            hub.imsi = mo_sms['imsi']
            hub_info = cls.hub_service.get_info_by_imsi(hub)

            print("hub_info.id: {}".format(hub_info.id))

            if hub_info.id is None:
                print("Sender doesn't match any hub id in DB. So skipping this SMS")
                return None

            print("SMS MO message: {}".format(message))

            print("======date_time: {}".format(date_time))
            print("type date_time: {}".format(type(date_time)))

            # 2018-09-08T13:49:03+01:00
            date_time = date_time.replace("T", " ")
            date_time = date_time.replace("+01:00", "+0100")
            d = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S%z')

            print("------d: ", d)
            print("d.tzinfo: ", d.tzinfo)

            # Convert to UTC
            utc_z = tz.gettz('UTC')
            date_time = d.astimezone(utc_z)

            print("......date_time: {}".format(date_time))
            print("date_time.tzinfo: ", date_time.tzinfo)

            req_rec_helper_factory = request_record_helper.MOSMSRequestRecordHelperFactory()
            req_rec_helper = req_rec_helper_factory.get_instance()
            request_record = req_rec_helper.prepare_request_record_dict(hub_info, message, date_time, date_time)

            response = None

            if message[:1].lower() == "c":
                if request_record.command_id == 0:
                    print("Couldn't find a valid command id for this message. Skipping it.")
                    return response
                else:
                    response = cls.req_service.add_request_record(request_record)
            elif message[:1].lower() == "r":
                response = cls.req_service.update_request_record(request_record)
            else:
                print("Couldn't parse message: {}".format(message))
        else:
            print("SMS content has invalid format. Skipping it. Content: {}".format(message))

        return response


class MOSMSMockedProcessingService(base.MOSMSProcessingService):

    @classmethod
    def process_sms(cls, mo_sms: list):
        pass

    @classmethod
    def process_each_sms(cls, mo_sms):
        pass

    @classmethod
    def validate_sms_format(cls, message: str) -> bool:
        pass

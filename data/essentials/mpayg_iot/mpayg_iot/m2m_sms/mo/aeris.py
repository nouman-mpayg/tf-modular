from mpayg_iot.m2m_sms.mo import base
from mpayg_domain.hub import base as hub_base
from mpayg_iot.m2m_sms.mo import request_record_helper
from mpayg_iot import globals
import requests
import base64
import json


class MOSMSAPIService(base.MOSMSAPIService):

    @classmethod
    def __init__(cls):
        return

    @classmethod
    def retrieve_sms(cls) -> dict:
        headers = {'Content-Type': 'application/json'}
        response = requests.get(cls.prepare_retrieve_sms_url(), headers=headers)
        return response

    @classmethod
    def prepare_retrieve_sms_url(cls) -> str:

        base_url = "{}/{}/longpoll/{}?apiKey={}".format(
            globals.AERIS_AERFRAME_SMS_NOTIFICATION_LONGPOLL_URL_ENDPOINT,
            globals.AERIS_ACCOUNT_ID,
            globals.AERIS_AERFRAME_SMS_NOTIFICATION_LONGPOLL_CHANNEL_ID,
            globals.AERIS_API_KEY,
        )

        return base_url


class MOSMSMockedAPIService(base.MOSMSAPIService):

    @classmethod
    def __init__(cls):
        return

    @classmethod
    def retrieve_sms(cls) -> dict:

        response = requests.models.Response()
        response.status_code = 200
        response.encoding = "utf-8"
        response._content = json.dumps({
                  "deliveryInfoNotification": [
                    {
                      "callbackData": "testapp1-mtsub1",
                      "deliveryInfo":   [
                        {
                          "address": "204043396402311",
                          "deliveryStatus": "DeliveredToTerminal",
                          "link": [
                            {
                              "rel": "MTMessageRequest ResourceUrl",
                              "href": "https://api.aerframe..com/smsmessaging/v2/1234/outbound/testapp1/requests/000d3e0a-6012-237a-4254-994bbff08833"
                            },
                            {
                              "rel": "MTDeliverySubscription ResourceUrl",
                              "href": "https://api.aerframe..com/smsmessaging/v2/1234/outbound/testapp1/subscriptions/00029952-f2c7-55b2-2d9a-ba2975334182"
                            }
                          ]
                        }
                      ]
                    }
                  ],
                  "inboundSMSMessageNotification": [
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",

                        # non existent sender
                        "senderAddress": "904043396402311",

                        # R06
                        "message": "UjA2O2FiY2RlZjk7MTswMDswMDs3OTswMDsxYzswMDAwOzAwMDA7MDAwMDswMDAw",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",
                        "senderAddress": "204043396402311",

                        # R06
                        "message": "UjA2O2FiY2RlZjk7MTswMDswMDs3OTswMDsxYzswMDAwOzAwMDA7MDAwMDswMDAw",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",
                        "senderAddress": "204043396402311",

                        # R04
                        "message": "UjA3Ozk4OGViMGY1OGU7MTtvaw==",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",
                        "senderAddress": "204043396402311",

                        # R44 - invalid command
                        "message": "UjQ0fDU2",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",
                        "senderAddress": "204043396402311",

                        # C51
                        "message": "QzUxOzllMzswOzAwOzAwOyswMDs3YTswMDAwOzAwOzAwOyswMDs3YTswMDAwOzAwOzAwOyswMDs3YTswMDAwOzAwOzAwOyswMDs3YTswMDAwOzAwOzAwOyswMDs3YTswMDAwOzAwOzAwOyswMDs3YTswMDAwOzIwMTktMDQtMDUgMDY6MjU6MDA=",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                    {
                      "callbackData": "testapp1-mosub1",
                      "inboundSMSMessage": {
                        "destinationAddress": "316540940550",
                        "senderAddress": "204043396402311",

                        # C57
                        "message": "QzU3fDU2",

                        "dateTime": "2019-04-04T06:31:16.987Z",
                        "link": [
                          {
                            "rel": "MOSubscription ResourceUrl",
                            "href": "https://api.aerframe..com/smsmessaging/v2/1234/inbound/subscriptions/00059949-78f7-9321-179e-1d6bd931f3c9"
                          }
                        ],
                        "messageId": "21840af1-0000-0000-007f-c8d6c137c113",
                        "encodingScheme": "7-Bit",
                        "serviceCode": "16142"
                      }
                    },
                  ]
                }).encode("utf-8")

        return response


class MOSMSProcessingService(base.MOSMSProcessingService):

    @classmethod
    def process_each_sms(cls, mo_sms):

        print("mo_sms: {}".format(mo_sms))

        message = mo_sms['inboundSMSMessage']['message']
        message = base64.b64decode(message).decode('utf-8')

        if cls.validate_sms_format(message):
            sender_address = mo_sms['inboundSMSMessage']['senderAddress']
            date_time = mo_sms['inboundSMSMessage']['dateTime']

            # 2019-04-04T06:31:16.987Z'
            date_time = date_time.replace("T", " ")
            date_time = date_time.replace("Z", " ")

            print("SMS MO message: {}".format(message))

            hub = hub_base.Hub()
            hub.imsi = sender_address

            hub = cls.hub_service.get_info_by_imsi(hub)

            print("hub_info.id: {}".format(hub.id))

            if hub.id is None:
                print("Sender doesn't match any hub id in DB. So skipping this SMS")
                return None

            req_rec_helper_factory = request_record_helper.MOSMSRequestRecordHelperFactory()
            req_rec_helper = req_rec_helper_factory.get_instance()
            request_record = req_rec_helper.prepare_request_record_dict(hub, message, date_time, date_time)

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

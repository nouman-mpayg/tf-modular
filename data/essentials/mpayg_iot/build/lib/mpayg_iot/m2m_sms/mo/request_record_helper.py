from mpayg_domain.request import base as request_base
from mpayg_domain.hub import base as hub_base
from mpayg_iot import globals as iot_globals
import json
from datetime import datetime


class MOSMSRequestRecordHelperFactory:

    @classmethod
    def get_instance(cls):
        return MOSMSRequestRecordHelper()


class MOSMSRequestRecordHelper:

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def prepare_request_record_dict(cls, hub: hub_base.Hub, message: str, creation_date=None, updation_date=None):

        request = request_base.Request()

        if len(message) > 0:
            msg_s_arr = message.split(message[3])
            reference_id = msg_s_arr[1]

            print("hub: {}".format(hub))

            request.reference_id = reference_id
            request.command_id = cls.get_command_id(message)
            request.hub_id = hub.id
            request.user_id = iot_globals.SERVICE_USER_SMS
            request.creation_date = creation_date if creation_date is not None else None
            request.updation_date = updation_date if updation_date is not None else None
            request.current_status = "Processed"
            request.progress = "Accepted,Processed"
            request.request_payload = message if cls.is_request(message) else None
            request.response_payload = cls.get_command_response(message) if cls.is_request(message) else message

            print("request: {}".format(request))

        else:
            print("Message is empty. Doing nothing for it")

        return request

    @classmethod
    def is_request(cls, message):

        if len(message) > 0:

            if message[:1].lower() == "c":
                return True
            elif message[:1].lower() == "r":
                return False
            else:
                print("message parsing error.")
        else:
            print("message is empty. Doing nothing.")

        return False

    @classmethod
    def is_response(cls, message):

        if len(message) > 0:

            if message[:1].lower() == "c":
                return False
            elif message[:1].lower() == "r":
                return True
            else:
                print("message parsing error.")
        else:
            print("message is empty. Doing nothing.")

        return False

    @classmethod
    def get_command_id(cls, message: str) -> str:

        command_id = 0
        command_ids_arr = json.loads(iot_globals.SHS_COMMAND_IDS)

        if len(message) > 0:

            if message[:1].lower() == "c":
                if message[:3].lower() == "c51":
                    command_id = command_ids_arr["record_status"]
                elif message[:3].lower() == "c57":
                    command_id = command_ids_arr["tamper_alarm"]
                elif message[:3].lower() == "c59":
                    command_id = command_ids_arr["firmware_update"]
            elif message[:1].lower() == "r":
                if message[:3].lower() == "r06":
                    command_id = command_ids_arr["adhoc_status"]
                else:
                    print("command id calculation is not needed in case of responses RXX")
            else:
                print("message parsing error.")
        else:
            print("message is empty. Doing nothing.")

        return command_id

    @classmethod
    def get_command_response(cls, cmd_data: str) -> str:

        print("Processing the input received: ", cmd_data)

        SEPARATOR = cls.get_separator(cmd_data)

        response = ""
        NOW_DT = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        ##cmd_data = cmd_data.decode("utf-8").replace("\n", "")
        cmd_data = cmd_data.replace("\n", "")
        print(cmd_data.split(SEPARATOR)[0])
        if (cmd_data.split(SEPARATOR))[0] == "C57":
            response = "R57" + SEPARATOR + \
                       (cmd_data.split(SEPARATOR))[1] + SEPARATOR + "1\n\n"
        elif cmd_data.split(SEPARATOR)[0] == "C51":
            response = "R51" + SEPARATOR + cmd_data.split(SEPARATOR)[1] + SEPARATOR + cmd_data.split(
                SEPARATOR)[2] + SEPARATOR + "1" + SEPARATOR + NOW_DT + "\n\n"
        elif cmd_data.split(SEPARATOR)[0] == "C59":
            response = "R59" + SEPARATOR + \
                       cmd_data.split(SEPARATOR)[1] + SEPARATOR + "1\n\n"
        elif cmd_data == "heart beat":
            response = "OK:: " + NOW_DT

        print("Calculated response: ", response)
        return response

    @classmethod
    def get_separator(cls, cmd_data):
        separator = ""

        separators = json.loads(iot_globals.SEPARATOR_LIST)

        for item in separators:
            if len(cmd_data.split(item)) > 1:
                separator = item

        return separator


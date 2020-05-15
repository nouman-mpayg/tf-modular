import json
import os

from mpayg_iot.device_messaging.base import DeviceMessageRequest, DeviceMessageResponse
from mpayg_iot.device_messaging.socket_client import SocketClient

DEFAULT_CMD_SEPARATOR = os.getenv('DEFAULT_CMD_SEPARATOR', "")


class SendMessage:

    def send(self,
             event: dict, lambda_name: str,
             cxx_obj_list: DeviceMessageRequest, cxx_payload_list: list, rxx_obj: DeviceMessageResponse,
             custom_request_msg: str = "", custom_response_msg: str = ""):

        print("event: ", event)

        request_id, separator, host, port = self.process_input(event)
        cxx_list = self.prepare_cxx(cxx_obj_list, request_id, separator, cxx_payload_list)

        cmd_str = cxx_list[0]  # just as a starting point
        rxx = ""  # later assigned with actual object reference
        # In case an exception is thrown
        exc_message = {
            "error": "Exception occurred",
            "reason": "",
            "cmd_request": str(cxx_obj_list[0])
        }

        try:
            sock = SocketClient()
            sock.connect(host, port)

            # Send each command in the list to the device
            for cxx in cxx_list:

                cmd_str = cxx

                # Send the command to device and receive response
                resp = sock.send(cxx)

                # Command response processing
                rxx = rxx_obj
                rxx.parse_str(resp)

                # Break the commands sending sequence, if an error occurs
                if rxx.is_error:
                    raise Exception(rxx.error_msg)

                print("Response str(rxx):", str(rxx))

            # Close connection after sending all commands to the device
            sock.close()

        except Exception as e:
            exc_message['cmd_request'] = custom_request_msg if len(custom_request_msg) > 0 else cmd_str
            exc_message['reason'] = str(rxx) if len(str(rxx)) > 0 else str(e)
            raise Exception(json.dumps(exc_message))

        return {
            "code": 200,
            "message": "Returned from Lambda {}".format(lambda_name),
            "cmd_request": custom_request_msg if len(custom_request_msg) > 0 else cmd_str,  # last command's in the list
            "cmd_response": custom_response_msg if len(custom_response_msg) > 0 else str(rxx)  # last command's response
        }

    def process_input(self, event):
        # Input processing
        request_id = event.get('request_record_info', {}).get('request_id', "")
        separator = event.get('hub_info', {}).get('hub_cmd_separator', DEFAULT_CMD_SEPARATOR)
        host = event['hub_ip'] if event.get('hub_ip') else event['hub_info']['hub_ip']
        port = 6969

        return request_id, separator, host, port

    def prepare_cxx(self, cxx_obj_list, request_id, separator, cxx_payload_list):

        payload_index = 0
        cxx_list = []

        # Prepare each command in the list
        for cxx_obj in cxx_obj_list:

            # Command message preparation
            cxx_obj.request_id = request_id if len(request_id) > 0 else cxx_obj.request_id
            cxx_obj.separator = separator
            cxx_obj.payload.separator = separator

            # Set payload attributes for each command
            if cxx_payload_list is not None and cxx_payload_list[payload_index] is not None:

                for i in cxx_payload_list[payload_index]:
                    setattr(cxx_obj.payload, i, cxx_payload_list[payload_index][i])

                payload_index = payload_index + 1

            cxx_list.append(str(cxx_obj))

        return cxx_list

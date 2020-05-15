# """
# Tests for C06 lambda
# """
# import json
#
# import pytest
# from pytest_mock import mocker
# from mpayg_iot.device_messaging.socket_client import SocketClient
# from index import handler
# from mpayg_iot.device_messaging.C06DeviceMessage import C06_DeviceMessage, R06_DeviceMessage
#
#
# @pytest.mark.parametrize("request_id, separator, hub_ip, expected", [
#     ("abcdef123", ";", "10.241.97.119", "R06;abcdef123;1;c2;03;88;00;06;aaaaaaa;0001;0014;0000"),
#     ("uvwxyz123", "|", "10.241.97.119", "R06|uvwxyz123|1|c2|03|88|00|06|aaaaaaa|0001|0014|0000")
# ])
# def test_when_input_provided_to_c06_should_return_valid_response(mocker, request_id, separator, hub_ip, expected):
#
#     event = {
#         "request_record_info": {
#             "request_id": request_id
#         },
#         "hub_info": {
#             "hub_cmd_separator": separator,
#             "hub_ip": hub_ip
#         }
#     }
#
#     mocker.patch.object(SocketClient, "send")
#     SocketClient.send.return_value = expected
#
#     response = handler(event, None)
#
#     # Response Null checks
#     assert response is not None
#     assert response['code'] is not None
#     assert response['message'] is not None
#     assert response['cmd_request'] is not None
#     assert response['cmd_response'] is not None
#
#     # Response values checks
#     assert response['code'] == 200
#     assert response['message'] == "Returned from Lambda C06"
#
#     # Response format checks
#     c06 = C06_DeviceMessage()
#     c06.parse_str(response['cmd_request'])
#
#     r06 = R06_DeviceMessage()
#     r06.parse_str(response['cmd_response'])
#
#     assert response['cmd_request'] == str(c06)
#     assert response['cmd_response'] == str(r06)
#     assert response['cmd_response'] == expected
#
#     # Response values checks
#     assert response['cmd_request'] == "{}{}{}".format("C06", separator, event['request_record_info']['request_id'])
#
#
# @pytest.mark.parametrize("request_id, separator, response", [
#     ("abcdef123", ";", "R06;abcdef123;0;error message from R06")
# ])
# def test_when_error_status_in_c06_should_throw_exception(mocker, request_id, separator, response):
#
#     event = {
#         "request_record_info": {
#             "request_id": request_id
#         },
#         "hub_info": {
#             "hub_cmd_separator": separator,
#             "hub_ip": ""
#         }
#     }
#
#     mocker.patch.object(SocketClient, "send")
#     SocketClient.send.return_value = response
#
#     try:
#         handler(event, None)
#     except Exception as e:
#         exception_msg = str(e)
#         msg = json.loads(exception_msg)
#         assert msg['reason'] == "error message from R06"

"""
Tests for all Cxx lambdas using SendMessage
"""
import json

import pytest
from mpayg_iot.device_messaging.C00DeviceMessage import C00_DeviceMessage, R00_DeviceMessage
from mpayg_iot.device_messaging.C04DeviceMessage import C04_DeviceMessage, R04_DeviceMessage
from mpayg_iot.device_messaging.C05DeviceMessage import C05_DeviceMessage, R05_DeviceMessage
from mpayg_iot.device_messaging.C06DeviceMessage import C06_DeviceMessage, R06_DeviceMessage
from mpayg_iot.device_messaging.C07DeviceMessage import C07_DeviceMessage, R07_DeviceMessage
from mpayg_iot.device_messaging.C11DeviceMessage import C11_DeviceMessage, R11_DeviceMessage
from mpayg_iot.device_messaging.C19DeviceMessage import C19_DeviceMessage, R19_DeviceMessage
from mpayg_iot.device_messaging.C90DeviceMessage import C90_DeviceMessage, R90_DeviceMessage
from mpayg_iot.device_messaging.C91DeviceMessage import C91_DeviceMessage, R91_DeviceMessage
from mpayg_iot.device_messaging.base import DeviceMessageRequest, DeviceMessageResponse
from mpayg_iot.device_messaging.send_message import SendMessage
from mpayg_iot.device_messaging.socket_client import SocketClient
from pytest_mock import mocker


########################################################################################################################
# tests fixtures

request_id = "abcdef123"
separator1 = ";"
separator2 = "|"
hub_ip = "10.241.97.119"


def get_tests_input_data(separator: str = ";"):
    return [
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C00",
            [C00_DeviceMessage()],
            None,
            R00_DeviceMessage(),
            "",
            "",
            "R00{}aaa1234{}1{}SH2{}0{}2.0.1".format(separator, separator, separator, separator, separator)
        ),

        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C00",
            [C00_DeviceMessage()],
            [{   # C00|4mlpjlmbxpni|6|192.168.254.161|6969|5|30|310000202|2018-09-03 13:37:31|30|50|25
                "status_sending_frequency_in_hours": "6",
                "host_ip": "192.168.254.161",
                "host_port": "6969",
                "socket_connection_retry_interval_in_seconds": "5",
                "socket_connection_retry_count": "30",
                "host_sms_number": "310000202",
                "now_dt": "2018-09-03 13:37:31",
                "unlock_period": "30",
                "panel_wattage": "50",
                "remaining_unlock_period": "25"
            }],
            R00_DeviceMessage(),
            "",
            "",
            "R00{}aaa1234{}1{}SH2{}0{}2.0.1".format(separator, separator, separator, separator, separator)
        ),
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C04",
            [C04_DeviceMessage()],
            [{"suspend_duration":  "10"}],
            R04_DeviceMessage(),
            "",
            "",
            "R04{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C05",
            [C05_DeviceMessage()],
            [{"action":  "1"}],
            R05_DeviceMessage(),
            "",
            "",
            "R05{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C06",
            [C06_DeviceMessage()],
            None,
            R06_DeviceMessage(),
            "",
            "",
            "R06{}{}{}1{}b4{}00{}9d{}01{}14{}0000{}0000{}0000{}0000".format(separator, request_id, separator,
                                                                            separator, separator, separator,
                                                                            separator, separator, separator,
                                                                            separator, separator, separator)
        ),
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C07",
            [C07_DeviceMessage()],
            [{"key":  "cabddef123"}],
            R07_DeviceMessage(),
            "",
            "",
            "R07{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
            {
                "request_record_info": {
                    "request_id": request_id
                },
                "hub_info": {
                    "hub_cmd_separator": separator,
                    "hub_ip": hub_ip
                }
            },
            "C11",
            [C11_DeviceMessage()],
            [{
                "shared_key_1":  "1770ca8b13", "shared_key_2":  "82419b3d97", "shared_key_3":  "18ba96e2c9",
                "shared_key_4":  "92328d2210", "shared_key_5":  "bb9ed9424d", "shared_key_6":  "2eac61e458",
                "shared_key_7":  "aa26e7aba3", "shared_key_8":  "378706bd94", "shared_key_9":  "e2029f4736",
                "shared_key_10":  "a4f24cac19"
            }],
            R11_DeviceMessage(),
            "",
            "",
            "R11{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
                {
                    "request_record_info": {
                        "request_id": request_id
                    },
                    "hub_info": {
                        "hub_cmd_separator": separator,
                        "hub_ip": hub_ip
                    }
                },
                "C19",
                [C19_DeviceMessage()],
                None,
                R19_DeviceMessage(),
                "",
                "",
                "R19{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
                {
                    "request_record_info": {
                        "request_id": request_id
                    },
                    "hub_info": {
                        "hub_cmd_separator": separator,
                        "hub_ip": hub_ip
                    }
                },
                "C90",
                [C90_DeviceMessage()],
                None,
                R90_DeviceMessage(),
                "",
                "",
                "R91{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
        (
                {
                    "request_record_info": {
                        "request_id": request_id
                    },
                    "hub_info": {
                        "hub_cmd_separator": separator,
                        "hub_ip": hub_ip
                    }
                },
                "C91",
                [C91_DeviceMessage()],
                None,
                R91_DeviceMessage(),
                "",
                "",
                "R19{}{}{}1{}ok".format(separator, request_id, separator, separator)
        ),
    ]

# ----------------------------------------------------------------------------------------------------------------------
# replace the response string in tests_input_data_exception with error_msgs


def get_error_msgs(separator: str = ";"):
    return {
        "C00": "R00{}abcdef123{}0{}error message from R00".format(separator, separator, separator),
        "C04": "R04{}abcdef123{}0{}error message from R04".format(separator, separator, separator),
        "C05": "R05{}abcdef123{}0{}error message from R05".format(separator, separator, separator),
        "C06": "R06{}abcdef123{}0{}error message from R06".format(separator, separator, separator),
        "C07": "R07{}abcdef123{}0{}error message from R07".format(separator, separator, separator),
        "C11": "R11{}abcdef123{}0{}error message from R11".format(separator, separator, separator),
        "C19": "R19{}abcdef123{}0{}error message from R19".format(separator, separator, separator),
        "C90": "R90{}abcdef123{}0{}error message from R90".format(separator, separator, separator),
        "C91": "R91{}abcdef123{}0{}error message from R91".format(separator, separator, separator)
    }


def replace_response_with_error(separator: str = ";"):
    tests_input_data_exception = []

    for d in get_tests_input_data(separator1):

        d = list(d)  # since tuple is immutable
        d[7] = get_error_msgs(separator)[[r for r in get_error_msgs(separator) if d[1] in r][0]]
        d = tuple(d)  # revert back to tuple type
        tests_input_data_exception.append(d)

    return tests_input_data_exception

########################################################################################################################


@pytest.mark.parametrize("event, lambda_name, cxx_obj_list, cxx_payload_list, rxx_obj,"
                         " custom_request_msg, custom_response_msg, expected",
                         get_tests_input_data(separator1) + get_tests_input_data(separator2))
def test_when_input_provided_to_send_message_should_return_valid_response(
        mocker: mocker,
        event: dict,
        lambda_name: str,
        cxx_obj_list: DeviceMessageRequest,
        cxx_payload_list: list,
        rxx_obj: DeviceMessageResponse,
        custom_request_msg: str,
        custom_response_msg: str,
        expected):

    mocker.patch.object(SocketClient, "connect")
    mocker.patch.object(SocketClient, "send")
    SocketClient.send.return_value = expected
    mocker.patch.object(SocketClient, "close")

    send_message = SendMessage()

    response = send_message.send(
        event, lambda_name, cxx_obj_list, cxx_payload_list, rxx_obj, custom_request_msg, custom_response_msg
    )

    # Response Null checks
    assert response is not None
    assert response['code'] is not None
    assert response['message'] is not None
    assert response['cmd_request'] is not None
    assert response['cmd_response'] is not None

    # Response values checks
    assert response['code'] == 200
    assert response['message'] == "Returned from Lambda {}".format(lambda_name)

    # Response format checks
    cxx = cxx_obj_list[0]
    cxx.parse_str(response['cmd_request'])

    print("response['cmd_response']:", response['cmd_response'])

    rxx = rxx_obj
    rxx.parse_str(response['cmd_response'])

    assert response['cmd_request'] == str(cxx)
    assert response['cmd_response'] == str(rxx)
    assert response['cmd_response'] == expected

    # Response values checks
    assert response['cmd_request'] == "{}{}{}{}{}".format(
        lambda_name, event['hub_info']['hub_cmd_separator'],
        event['request_record_info']['request_id'],
        event['hub_info']['hub_cmd_separator'] if len(str(cxx.payload)) > 0 else "",
        str(cxx.payload)
    )


@pytest.mark.parametrize("event, lambda_name, cxx_obj_list, cxx_payload_list, rxx_obj,"
                         " custom_request_msg, custom_response_msg, expected",
                         replace_response_with_error(separator1) + replace_response_with_error(separator2))
def test_when_error_status_in_cxx_should_throw_exception(
        mocker: mocker,
        event: dict,
        lambda_name: str,
        cxx_obj_list: DeviceMessageRequest,
        cxx_payload_list: list,
        rxx_obj: DeviceMessageResponse,
        custom_request_msg: str,
        custom_response_msg: str,
        expected):

    mocker.patch.object(SocketClient, "connect")
    mocker.patch.object(SocketClient, "send")
    SocketClient.send.return_value = expected
    mocker.patch.object(SocketClient, "close")

    send_message = SendMessage()

    try:
        response = send_message.send(
            event, lambda_name, cxx_obj_list, cxx_payload_list, rxx_obj, custom_request_msg, custom_response_msg
        )
    except Exception as e:
        msg = json.loads(str(e))
        assert msg['reason'] == expected

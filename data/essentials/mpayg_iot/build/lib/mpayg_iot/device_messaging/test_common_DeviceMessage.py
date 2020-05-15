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

"""
Tests for classes C**_DeviceMessage
"""

REQUEST_ID_DEFUALT_LENGTH = 10


@pytest.mark.parametrize("class_obj, name, separator", [
    (C91_DeviceMessage(), "C91", ";"),
    (C90_DeviceMessage(), "C90", ";"),
    (C19_DeviceMessage(), "C19", ";"),
    (C11_DeviceMessage(), "C11", ";"),
    (C07_DeviceMessage(), "C07", ";"),
    (C06_DeviceMessage(), "C06", ";"),
    (C05_DeviceMessage(), "C05", ";"),
    (C04_DeviceMessage(), "C04", ";"),
    (C00_DeviceMessage(), "C00", ";")
])
def test_when_object_is_created_then_it_should_have_default_values_Cmd_DeviceMessage(
        class_obj, name, separator):

    cmd = class_obj

    assert cmd.name == name
    assert cmd.separator == separator
    assert cmd.request_id is not None
    assert len(cmd.request_id) == REQUEST_ID_DEFUALT_LENGTH


@pytest.mark.parametrize("class_obj, name, separator, request_id", [
    (C91_DeviceMessage(), "C91", "|", "abc1234"),
    (C90_DeviceMessage(), "C90", "|", "ijk1234"),
    (C19_DeviceMessage(), "C19", "|", "lmn1234"),
    (C11_DeviceMessage(), "C11", "|", "pqr1234"),
    (C07_DeviceMessage(), "C07", "|", "pqr1234"),
    (C06_DeviceMessage(), "C06", "|", "tuv1234"),
    (C05_DeviceMessage(), "C05", "|", "wxy1234"),
    (C04_DeviceMessage(), "C04", "|", "zzz1234"),
    (C00_DeviceMessage(), "C00", "|", "aaa1234"),

    (C91_DeviceMessage(), "C91", ";", "abc1234"),
    (C90_DeviceMessage(), "C90", ";", "ijk1234"),
    (C19_DeviceMessage(), "C19", ";", "lmn1234"),
    (C11_DeviceMessage(), "C11", ";", "pqr1234"),
    (C07_DeviceMessage(), "C07", ";", "pqr1234"),
    (C06_DeviceMessage(), "C06", ";", "tuv1234"),
    (C05_DeviceMessage(), "C05", ";", "wxy1234"),
    (C04_DeviceMessage(), "C04", ";", "zzz1234"),
    (C00_DeviceMessage(), "C00", ";", "aaa1234")
])
def test_when_cmd_properties_are_set_then_it_should_be_valid_cmd_Cmd_DeviceMessage(
        class_obj, name, separator, request_id):

    cmd = class_obj
    cmd.separator = separator
    cmd.request_id = request_id

    assert cmd.name == name
    assert cmd.separator == separator
    assert cmd.request_id == request_id


@pytest.mark.parametrize("class_obj, name, separator, request_id, payload", [
    (C11_DeviceMessage(), "C11", "|", "tuv1234", {"shared_key_1": "abcdef",
                                                  "shared_key_2": "abcdef",
                                                  "shared_key_3": "abcdef",
                                                  "shared_key_4": "abcdef",
                                                  "shared_key_5": "abcdef",
                                                  "shared_key_6": "abcdef",
                                                  "shared_key_7": "abcdef",
                                                  "shared_key_8": "abcdef",
                                                  "shared_key_9": "abcdef",
                                                  "shared_key_10": "abcdef"
                                                }),
    (C07_DeviceMessage(), "C07", "|", "tuv1234", {"key": "ceabcdef"}),
    (C05_DeviceMessage(), "C05", "|", "tuv1234", {"action": 2}),
    (C04_DeviceMessage(), "C04", "|", "tuv1234", {"suspend_duration": 10}),
    (C00_DeviceMessage(), "C00", "|", "tuv1234", {"status_sending_frequency_in_hours": 6,
                                                  "host_ip": "192.168.71.10",
                                                  "host_port": 6969,
                                                  "socket_connection_retry_interval_in_seconds": 5,
                                                  "socket_connection_retry_count": 30,
                                                  "host_sms_number": "316540940550",
                                                  "now_dt": "2019-12-04 07:16:26",
                                                  "unlock_period": 30,
                                                  "panel_wattage": 80,
                                                  "remaining_unlock_period": 10}),

    (C11_DeviceMessage(), "C11", ";", "tuv1234", {"shared_key_1": "abcdef",
                                                  "shared_key_2": "abcdef",
                                                  "shared_key_3": "abcdef",
                                                  "shared_key_4": "abcdef",
                                                  "shared_key_5": "abcdef",
                                                  "shared_key_6": "abcdef",
                                                  "shared_key_7": "abcdef",
                                                  "shared_key_8": "abcdef",
                                                  "shared_key_9": "abcdef",
                                                  "shared_key_10": "abcdef"
                                                }),
    (C07_DeviceMessage(), "C07", ";", "tuv1234", {"key": "ceabcdef"}),
    (C05_DeviceMessage(), "C05", ";", "tuv1234", {"action": 2}),
    (C04_DeviceMessage(), "C04", ";", "tuv1234", {"suspend_duration": 10}),
    (C00_DeviceMessage(), "C00", ";", "tuv1234", {"status_sending_frequency_in_hours": 6,
                                                  "host_ip": "192.168.71.10",
                                                  "host_port": 6969,
                                                  "socket_connection_retry_interval_in_seconds": 5,
                                                  "socket_connection_retry_count": 30,
                                                  "host_sms_number": "316540940550",
                                                  "now_dt": "2019-12-04 07:16:26",
                                                  "unlock_period": 30,
                                                  "panel_wattage": 80,
                                                  "remaining_unlock_period": 10}),
])
def test_when_cmd_payload_properties_are_set_then_it_should_be_valid_cmd_Cmd_DeviceMessage(
        class_obj, name, separator, request_id, payload):

    cmd = class_obj
    cmd.separator = separator
    cmd.request_id = request_id

    for i in payload:
        setattr(cmd.payload, i, payload[i])

    assert cmd.name == name
    assert cmd.separator == separator
    assert cmd.request_id == request_id
    for i in payload:
        assert getattr(cmd.payload, i) == payload[i]


@pytest.mark.parametrize("class_obj, name, separator, request_id, expected", [
    (C91_DeviceMessage(), "C91", ";", "abc1234", "C91;abc1234"),
    (C90_DeviceMessage(), "C90", ";", "ijk1234", "C90;ijk1234"),
    (C19_DeviceMessage(), "C19", ";", "lmn1234", "C19;lmn1234"),
    (C11_DeviceMessage(), "C11", ";", "pqr1234", "C11;pqr1234;abc;abc;abc;abc;abc;abc;abc;abc;abc;abc"),
    (C07_DeviceMessage(), "C07", ";", "pqr1234", "C07;pqr1234;ceabcdef"),
    (C06_DeviceMessage(), "C06", ";", "tuv1234", "C06;tuv1234"),
    (C05_DeviceMessage(), "C05", ";", "wxy1234", "C05;wxy1234;2"),
    (C04_DeviceMessage(), "C04", ";", "zzz1234", "C04;zzz1234;10"),
    (C00_DeviceMessage(), "C00", ";", "aaa1234", "C00;aaa1234;6;192.168.71.10;6969;5;30;316540940550;2019-12-04 07:16:26;30;50;179"),
])
def test_when_cmd_str_passed_to_parse_str_it_should_set_to_self_Cmd_DeviceMessage(
        class_obj, name, separator, request_id, expected):

    cmd = class_obj
    cmd.parse_str(expected)

    assert cmd.name == name
    assert cmd.separator == separator
    assert cmd.request_id == request_id


@pytest.mark.parametrize("class_obj, string_cmd", [
    (C91_DeviceMessage(), "C91;abc1234"),
    (C90_DeviceMessage(), "C90;ijk1234"),
    (C19_DeviceMessage(), "C19;lmn1234"),
    (C11_DeviceMessage(), "C11;pqr1234;abc;abc;abc;abc;abc;abc;abc;abc;abc;abc"),
    (C07_DeviceMessage(), "C07;pqr1234;ceabcdef"),
    (C06_DeviceMessage(), "C06;tuv1234"),
    (C05_DeviceMessage(), "C05;wxy1234;2"),
    (C04_DeviceMessage(), "C04;zzz1234;10"),
    (C00_DeviceMessage(), "C00;aaa1234;6;192.168.71.10;6969;5;30;316540940550;2019-12-04 07:16:26;30;50;179"),
])
def test_when_str_compared_to_string_it_should_be_valid_cmd_Cmd_DeviceMessage(
        class_obj, string_cmd):

    cmd = class_obj
    cmd.parse_str(string_cmd)

    assert str(cmd) == string_cmd


"""
Tests for classes R**_DeviceMessage
"""


@pytest.mark.parametrize("class_obj, name, separator, status", [
    (R91_DeviceMessage(), "R91", ";", -1),
    (R90_DeviceMessage(), "R90", ";", -1),
    (R19_DeviceMessage(), "R19", ";", -1),
    (R11_DeviceMessage(), "R11", ";", -1),
    (R07_DeviceMessage(), "R07", ";", -1),
    (R06_DeviceMessage(), "R06", ";", -1),
    (R05_DeviceMessage(), "R05", ";", -1),
    (R04_DeviceMessage(), "R04", ";", -1),
    (R00_DeviceMessage(), "R00", ";", -1),
])
def test_when_object_is_created_then_it_should_have_default_values_Res_DeviceMessage(
        class_obj, name, separator, status):

    resp = class_obj

    assert resp.name == name
    assert resp.separator == separator
    assert resp.request_id is not None
    assert len(resp.request_id) == REQUEST_ID_DEFUALT_LENGTH
    assert resp.status == status


@pytest.mark.parametrize("class_obj, name, separator, request_id, status, payload", [

    (R91_DeviceMessage(), "R91", "|", "abc1234", 1, "ok"),
    (R90_DeviceMessage(), "R90", "|", "ijk1234", 1, "ok"),
    (R19_DeviceMessage(), "R19", "|", "lmn1234", 1, "ok"),
    (R11_DeviceMessage(), "R11", "|", "tuv1234", 1, "ok"),
    (R07_DeviceMessage(), "R07", "|", "tuv1234", 1, "ok"),
    (R06_DeviceMessage(), "R06", "|", "pqr1234", 1, "c2|03|88|00|06|aaaaaaa|0001|0014|0000"),
    (R05_DeviceMessage(), "R05", "|", "wxy1234", 1, "ok"),
    (R04_DeviceMessage(), "R04", "|", "zzz1234", 1, "ok"),
    (R00_DeviceMessage(), "R00", "|", "aaa1234", 1, "SH2|0|2.0.1"),

    (R91_DeviceMessage(), "R91", ";", "abc1234", 1, "ok"),
    (R90_DeviceMessage(), "R90", ";", "ijk1234", 1, "ok"),
    (R19_DeviceMessage(), "R19", ";", "lmn1234", 1, "ok"),
    (R11_DeviceMessage(), "R11", ";", "pqr1234", 1, "ok"),
    (R07_DeviceMessage(), "R07", ";", "pqr1234", 1, "ok"),
    (R06_DeviceMessage(), "R06", ";", "tuv1234", 1, "c2;03;88;00;06;aaaaaaa;0001;0014;0000"),
    (R05_DeviceMessage(), "R05", ";", "wxy1234", 1, "ok"),
    (R04_DeviceMessage(), "R04", ";", "zzz1234", 1, "ok"),
    (R00_DeviceMessage(), "R00", ";", "aaa1234", 1, "SH2;0;2.0.1"),
])
def test_when_resp_properties_are_set_then_it_should_be_valid_resp__Res_DeviceMessage(
        class_obj, name, separator, request_id, status, payload):

    resp = class_obj
    resp.separator = separator
    resp.request_id = request_id
    resp.status = status

    resp.payload.separator = separator
    resp.payload.parse_str(payload)

    assert resp.name == name
    assert resp.separator == separator
    assert resp.request_id == request_id
    assert resp.status == status
    assert str(resp.payload) == payload


@pytest.mark.parametrize("class_obj, name, separator, request_id, status, payload, string_cmd", [
    (R91_DeviceMessage(), "R91", ";", "abc1234", 1, "ok", "R91;abc1234;1;ok"),
    (R90_DeviceMessage(), "R90", ";", "ijk1234", 1, "ok", "R90;ijk1234;1;ok"),
    (R19_DeviceMessage(), "R19", ";", "lmn1234", 1, "ok", "R19;lmn1234;1;ok"),
    (R11_DeviceMessage(), "R11", ";", "pqr1234", 1, "ok", "R11;pqr1234;1;ok"),
    (R07_DeviceMessage(), "R07", ";", "pqr1234", 1, "ok", "R07;pqr1234;1;ok"),
    (R06_DeviceMessage(), "R06", ";", "tuv1234", 1, "c2;03;88;00;06;aaaaaaa;0001;0014;0000", "R06;tuv1234;1;c2;03;88;00;06;aaaaaaa;0001;0014;0000"),
    (R05_DeviceMessage(), "R05", ";", "wxy1234", 1, "ok", "R05;wxy1234;1;ok"),
    (R04_DeviceMessage(), "R04", ";", "zzz1234", 1, "ok", "R04;zzz1234;1;ok"),
    (R00_DeviceMessage(), "R00", ";", "aaa1234", 1, "SH2;0;2.0.1", "R00;aaa1234;1;SH2;0;2.0.1"),
])
def test_when_string_passed_to_parse_str_is_called_it_should_set_to_self_and_match_object_properties_Res_DeviceMessage(
        class_obj, name, separator, request_id, status, payload, string_cmd):

    resp = class_obj
    resp.parse_str(string_cmd)

    assert resp.name == name
    assert resp.separator == separator
    assert resp.request_id == request_id
    assert resp.status == status
    assert str(resp.payload) == payload


@pytest.mark.parametrize("class_obj, string_cmd", [
    (R91_DeviceMessage(), "R91;abc1234;1;ok"),
    (R90_DeviceMessage(), "R90;ijk1234;1;ok"),
    (R19_DeviceMessage(), "R19;lmn1234;1;ok"),
    (R11_DeviceMessage(), "R11;pqr1234;1;ok"),
    (R07_DeviceMessage(), "R07;pqr1234;1;ok"),
    (R06_DeviceMessage(), "R06;tuv1234;1;c2;03;88;00;06;aaaaaaa;0001;0014;0000"),
    (R05_DeviceMessage(), "R05;wxy1234;1;ok"),
    (R04_DeviceMessage(), "R04;zzz1234;1;ok"),
    (R00_DeviceMessage(), "R00;aaa1234;1;SH2;0;2.0.1"),
])
def test_when_str_is_called_it_should_match_object_properties__Res_DeviceMessage(
        class_obj, string_cmd):

    resp = class_obj
    resp.parse_str(string_cmd)

    assert str(resp) == string_cmd

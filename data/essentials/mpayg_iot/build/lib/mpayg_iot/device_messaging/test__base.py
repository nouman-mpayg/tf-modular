from mpayg_iot.device_messaging.base import generate_request_id, DeviceMessagePayload, DeviceMessage, DeviceMessageResponse


REQUEST_ID_DEFUALT_LENGTH = 10


def test_generate_request_id():
    r = generate_request_id()

    assert r is not None
    assert len(r) == REQUEST_ID_DEFUALT_LENGTH
    assert isinstance(r, str)


"""
Tests for class DeviceMessagePayload
"""


def test_when_setting_invalid_attrib_then_should_throw_AttributeError_DeviceMessagePayload():

    payload = DeviceMessagePayload()

    try:
        payload.attrib3 = "value3"
    except AttributeError as e:
        assert str(e) == "The attribute attrib3 is not a valid attribute of the class. And cannot be set"


def test_when_setting_invalid_separator_then_should_throw_ValueError_DeviceMessagePayload():

    payload = DeviceMessagePayload()

    try:
        payload.separator = ""
    except ValueError as e:
        assert str(e) == "Command message separator must be of type str and cannot be empty/null"


def test_when_getting_non_existent_attrib_then_should_throw_AttributeError_DeviceMessagePayload():

    payload = DeviceMessagePayload()

    try:
        payload.attrib3
    except AttributeError as e:
        assert str(e) == "'DeviceMessagePayload' object has no attribute 'attrib3'"


"""
Tests for class DeviceMessage
"""


def test_when_using_init_then_should_create_instance_DeviceMessage():
    dm = DeviceMessage("CCC")

    assert dm.name == "CCC"
    assert dm.request_id is not None
    assert dm.payload is not None


def test_when_attribs_are_set_then_should_allow_get_set_attribs_DeviceMessage():
    dm = DeviceMessage("CCC")
    dm.name = "CAA"
    dm.request_id = "abcdef123"
    p = DeviceMessagePayload()
    dm.payload = p

    assert dm.name is not None
    assert isinstance(dm.name, str)
    assert dm.name == "CAA"

    assert dm.request_id is not None
    assert isinstance(dm.request_id, str)
    assert dm.request_id == "abcdef123"

    assert dm.payload is not None
    assert isinstance(dm.payload, DeviceMessagePayload)
    assert dm.payload == p


def test_when_attribs_are_set_invalid_types_then_should_throw_ValueError_DeviceMessage():
    try:
        DeviceMessage(123)
    except ValueError as v:
        assert str(v) == "Command message name must be of type str and cannot be empty/null"

    dm = DeviceMessage("CCC")

    try:
        dm.name = 123
    except ValueError as v:
        assert str(v) == "Command message name must be of type str and cannot be empty/null"

    try:
        dm.separator = ""
    except ValueError as v:
        assert str(v) == "Command message separator must be of type str and cannot be empty/null"

    try:
        dm.request_id = 123
    except ValueError as v:
        assert str(v) == "Command message request id must be of type str and cannot be empty/null"

    try:
        dm.payload = 123
    except ValueError as v:
        assert str(v) == "Command message payload must be of type DeviceMessagePayload and cannot be empty/null"


def test_when_str_then_provides_commmand_string_DeviceMessage():

    ccc = DeviceMessage("CCC")
    ccc.request_id = "abc1233"

    assert str(ccc) == "{}{}{}".format(ccc.name, ccc.separator, ccc.request_id)
    assert "{}".format(ccc) == "{}{}{}".format(ccc.name, ccc.separator, ccc.request_id)


def test_when_str_passed_to_parse_str_it_should_parse_it_and_set_to_self_DeviceMessage():

    response = DeviceMessage("CCC")

    response.parse_str("CCC;wxyz456")

    assert str(response) == "{}{}{}".format("CCC", ";", "wxyz456")


def test_when_str_passed_to_parse_str_is_invalid_it_should_throw_ValueError_exception_DeviceMessage():

    response = DeviceMessage("CCC")

    try:
        response.parse_str("abadsfsadfsaf")
    except ValueError as v:
        assert str(v) == "The provided string must of correct format to parse and convert to object"


def test_when_custom_separator_is_used_with_parse_str_it_should_parse_it_and_set_to_self_DeviceMessage():

    response = DeviceMessage("CCC")

    response.request_id = "wxyz456"

    assert str(response) == "{}{}{}".format("CCC", ";", "wxyz456")

    response.separator = "|"

    assert str(response) == "{}{}{}".format("CCC", "|", "wxyz456")


"""
Tests for class DeviceMessageResponse
"""

def test_when_initialzed_should_set_default_values_DeviceMessageResponse():

    response = DeviceMessageResponse("RRR")

    assert response.name is not None
    assert response.name == "RRR"

    assert response.separator is not None
    assert response.separator == ";"

    assert response.request_id is not None

    assert response.status is not None
    assert response.status == -1


def test_when_attribs_are_set_invalid_types_then_should_throw_ValueError_DeviceMessageResponse():

    dm = DeviceMessageResponse("RRR")

    try:
        dm.status = ""
    except ValueError as v:
        assert str(v) == "Command message status must be of type int and cannot be empty/null"

    try:
        dm.is_error = ""
    except ValueError as v:
        assert str(v) == "Command message is error must be of type bool and cannot be empty/null"

    try:
        dm.error_msg = 1
    except ValueError as v:
        assert str(v) == "Command error message must be of type str and cannot be empty/null"


def test_when_converted_to_str_should_provide_valid_response_packet_DeviceMessageResponse():

    response = DeviceMessageResponse("RRR")

    assert str(response) == "{}{}{}{}{}".format(response.name,
        response.separator, response.request_id, response.separator, response.status)


def test_when_properties_are_set_should_set_them_DeviceMessageResponse():

    response = DeviceMessageResponse("RRR")

    response.name = "ROR"

    assert response.name == "ROR"

    response.request_id = "abddef123"

    assert response.request_id == "abddef123"

    response.status = 1

    assert response.status == 1

    response.is_error = True
    response.error_msg = "This is an error message"

    assert response.is_error == True
    assert response.error_msg == "This is an error message"


def test_when_str_passed_to_parse_str_it_should_parse_it_and_set_to_self_DeviceMessageResponse():

    response = DeviceMessageResponse("RIR")

    response.parse_str("RAR;wxyz456;1")

    assert str(response) == "{}{}{}{}{}".format("RAR", ";", "wxyz456", ";", "1")


def test_when_str_passed_to_parse_str_is_invalid_it_should_throw_ValueError_exception_DeviceMessageResponse():

    response = DeviceMessageResponse("RIR")

    try:
        response.parse_str("abadsfsadfsaf")
    except ValueError as v:
        assert str(v) == "invalid literal for int() with base 10: 'fsaf'"

    try:
        response.parse_str(1111)
    except ValueError as v:
        assert str(v) == "The provided string must of correct format to parse and convert to object"


def test_when_custom_separator_is_used_with_parse_str_it_should_parse_it_and_set_to_self_DeviceMessageResponse():

    response = DeviceMessageResponse("RIR")

    response.request_id = "wxyz456"

    assert str(response) == "{}{}{}{}{}".format("RIR", ";", "wxyz456", ";", "-1")

    response.separator = "|"

    assert str(response) == "{}{}{}{}{}".format("RIR", "|", "wxyz456", "|", "-1")

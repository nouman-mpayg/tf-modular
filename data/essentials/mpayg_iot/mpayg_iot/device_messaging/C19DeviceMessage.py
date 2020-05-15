from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_DeviceMessage


# Request

class C19_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C19", None)


# Response


class R19_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R19_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R19", R19_Payload())

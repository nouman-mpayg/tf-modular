from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_DeviceMessage


# Request

class C90_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C90", None)


# Response


class R90_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R90_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R90", R90_Payload())

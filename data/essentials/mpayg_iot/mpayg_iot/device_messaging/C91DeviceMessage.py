from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_DeviceMessage


# Request

class C91_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C91", None)


# Response


class R91_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R91_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R91", R91_Payload())

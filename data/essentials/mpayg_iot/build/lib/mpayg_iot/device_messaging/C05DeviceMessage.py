from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_Payload, Cxx_DeviceMessage


# Request


class C05_Payload(Cxx_Payload):

    def __init__(self):

        super().__init__([
            "action"
        ])


class C05_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C05", C05_Payload())


# Response


class R05_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R05_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R05", R05_Payload())

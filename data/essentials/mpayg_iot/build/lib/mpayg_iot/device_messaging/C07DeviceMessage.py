from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_Payload, Cxx_DeviceMessage


# Request


class C07_Payload(Cxx_Payload):

    def __init__(self):

        super().__init__([
            "key"
        ])


class C07_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C07", C07_Payload())


# Response


class R07_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R07_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R07", R07_Payload())

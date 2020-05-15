from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_Payload, Cxx_DeviceMessage


# Request


class C11_Payload(Cxx_Payload):

    def __init__(self):

        super().__init__([
            "shared_key_1",
            "shared_key_2",
            "shared_key_3",
            "shared_key_4",
            "shared_key_5",
            "shared_key_6",
            "shared_key_7",
            "shared_key_8",
            "shared_key_9",
            "shared_key_10",
        ])


class C11_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C11", C11_Payload())


# Response


class R11_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R11_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R11", R11_Payload())

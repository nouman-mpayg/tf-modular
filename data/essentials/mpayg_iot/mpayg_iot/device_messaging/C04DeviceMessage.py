from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_Payload, Cxx_DeviceMessage


# Request


class C04_Payload(Cxx_Payload):

    def __init__(self):

        super().__init__([
            "suspend_duration"
        ])


class C04_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C04", C04_Payload())


# Response


class R04_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "response_message"
        ])


class R04_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R04", R04_Payload())

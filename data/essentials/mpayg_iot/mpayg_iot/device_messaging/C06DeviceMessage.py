from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_DeviceMessage


# Request

class C06_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C06", None)


# Response


class R06_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "current_PanelVoltage",
            "current_PanelCurrent",
            "current_BatteryVoltage",
            "current_BatteryCurrent",
            "current_RSSI",
            "current_UnlockPeriod",
            "unlockFailureCount",
            "portOverloadCount",
            "powerOverloadCount",
        ])


class R06_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R06", R06_Payload())

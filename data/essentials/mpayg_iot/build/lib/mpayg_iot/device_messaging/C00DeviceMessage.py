from mpayg_iot.device_messaging.base import Rxx_Payload, Rxx_DeviceMessageResponse, Cxx_Payload, Cxx_DeviceMessage


# Request


class C00_Payload(Cxx_Payload):

    def __init__(self):

        super().__init__([
            "status_sending_frequency_in_hours",
            "host_ip",
            "host_port",
            "socket_connection_retry_interval_in_seconds",
            "socket_connection_retry_count",
            "host_sms_number",
            "now_dt",
            "unlock_period",
            "panel_wattage",
            "remaining_unlock_period"
        ])


class C00_DeviceMessage(Cxx_DeviceMessage):

    def __init__(self):
        super().__init__("C00", C00_Payload())


# Response


class R00_Payload(Rxx_Payload):

    def __init__(self):

        super().__init__([
            "product_name",
            "hardware_revision",
            "firmware_version"
        ])


class R00_DeviceMessage(Rxx_DeviceMessageResponse):
    def __init__(self):
        super().__init__("R00", R00_Payload())

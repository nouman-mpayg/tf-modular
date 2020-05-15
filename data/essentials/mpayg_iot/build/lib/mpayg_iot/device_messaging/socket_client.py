import socket
import os
from mpayg_iot import globals
from mpayg_iot.device_messaging.base import DeviceMessageRequest, DeviceMessageResponse, DeviceMessage

globals.DEVICE_SOCKET_TIMEOUT_SEC = os.getenv("DEVICE_SOCKET_TIMEOUT_SEC", 30)
socket_timeout_sec = globals.DEVICE_SOCKET_TIMEOUT_SEC


class SocketClient:

    socket_client = None

    def connect(self, host: str, port: int):

        try:
            print("Connecting to device IP: {}:{}...".format(host, port))

            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.socket_client.settimeout(socket_timeout_sec)
            self.socket_client.connect((host, port))

            print("Connected")

        except Exception as e:
            print("Connection error occurred. Details: {}".format(e))
            raise e
        finally:
            print("Returning from SocketClient.connect()")

    def close(self):
        if self.socket_client:
            self.socket_client.close()
        else:
            raise Exception("Tried close a non-existent connection")

    def send(self, data: DeviceMessageRequest) -> str:

        print("SocketClient.send() invoked")

        cmd_str = str(data)

        try:
            if self.socket_client:
                c2d_cmd = "{}\n".format(cmd_str).encode()

                print("Sending the command to device: {}...".format(cmd_str))
                self.socket_client.settimeout(socket_timeout_sec)
                self.socket_client.send(c2d_cmd)

                data = self.socket_client.recv(1024)
                data_str = data.decode().strip('\n')

                print("Received from device: {}\n".format(repr(data)))

                return data_str
            else:
                raise Exception("Tried to send data without a connection")

        except Exception as e:
            print("Error occurred when trying to transfer data. Details: {}".format(e))
            raise e
        finally:
            print("Returning from SocketClient.send()")

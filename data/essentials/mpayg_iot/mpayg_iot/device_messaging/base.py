import hashlib
import time


# TODO: duplicate. Refactored to mpayg_domani.request.base.Request
def generate_request_id():
    m = hashlib.sha256()
    m.update(b"" + bytes(str(time.time()), 'utf-8'))
    req_id_hex = m.hexdigest()[:10]

    return req_id_hex

########################################################################################################################


class DeviceMessagePayload(object):
    """
    Payload class for device messaging. Top level class to represent a device command message payload. Child classes
    will specialize the allowed attributes to get and set
    """

    def __init__(self):
        self.valid_attr = {}
        self.__separator = ";"

    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, s: str):
        if s is not None and isinstance(s, str) and len(s) > 0:
            self.__separator = s
        else:
            raise ValueError("Command message separator must be of type str and cannot be empty/null")

    def __setattr__(self, name, value):

        if name == "valid_attr" or name == "separator" or name == "_DeviceMessagePayload__separator":
            object.__setattr__(self, name, value)
        elif name in self.valid_attr:
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("The attribute {} is not a valid attribute of the class. And cannot be set".format(name))

    def __str__(self):
        return self.separator.join(
                    [str(getattr(self, a) for a in self.valid_attr)]
                ) if (len(self.valid_attr) > 0) else ""


class DeviceMessage:

    """
    Top level class to represent a request/response message sent to/from device (SmartHub)

    Attributes
    ----------

    name : str
        The name of the command. Either can be request of the command or its response

    separator : str
        The separator of the command. It can be ; or |

    request_id : str
        The request id of the command. It's a random string of alpha-numeric values

    payload: DeviceMessagePayload
        The payload of the command. The base class is composed of a payload. Child classes will specialize it

    """

    def __init__(self, command_name: str = "000"):

        if command_name is not None and isinstance(command_name, str) and len(command_name) > 0:
            self.__name = command_name
        else:
            raise ValueError("Command message name must be of type str and cannot be empty/null")

        self.__separator = ";"
        self.__request_id = generate_request_id()
        self.__payload = DeviceMessagePayload()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n: str):
        if n is not None and isinstance(n, str) and len(n) > 0:
            self.__name = n
        else:
            raise ValueError("Command message name must be of type str and cannot be empty/null")

    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, s: str):
        if s is not None and isinstance(s, str) and len(s) > 0:
            self.__separator = s
        else:
            raise ValueError("Command message separator must be of type str and cannot be empty/null")

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, r: str):
        if r is not None and isinstance(r, str) and len(r) > 0:
            self.__request_id = r
        else:
            raise ValueError("Command message request id must be of type str and cannot be empty/null")

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, p: DeviceMessagePayload):
        if p is not None and isinstance(p, DeviceMessagePayload):
            self.__payload = p
        else:
            raise ValueError("Command message payload must be of type DeviceMessagePayload and cannot be empty/null")

    def parse_str(self, value):

        if isinstance(value, str) and len(value.split(value[3])) >= 2:

            v = value.split(value[3])
            self.name = v[0]
            self.separator = value[3]
            self.request_id = v[1]

            return self
        else:
            raise ValueError("The provided string must of correct format to parse and convert to object")

    def __str__(self):
        return "{}{}{}{}{}".format(self.name,
                                   self.separator,
                                   self.request_id,
                                   self.separator if len(self.payload.valid_attr) > 0 else "",
                                   str(self.payload) if self.payload is not None else ""
                                   )

########################################################################################################################


class DeviceMessageRequest(DeviceMessage):
    """
    Top level class to represent a request message sent to/from device (SmartHub)
    """
    def __init__(self, command_name: str):
        super().__init__(command_name)


class DeviceMessageResponse(DeviceMessage):

    """
    Top level class to represent a response message sent to/from device (SmartHub)


    Additional Attributes
    ---------------------

    status : int
        The numeric status of the command. It is single digit
    """

    def __init__(self, command_name: str):

        self.__status = -1
        self.__is_error = False
        self.__error_msg = ""
        super().__init__(command_name)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, n: int):
        if n is not None and isinstance(n, int):
            self.__status = n
        else:
            raise ValueError("Command message status must be of type int and cannot be empty/null")

    @property
    def is_error(self):
        return self.__is_error

    @is_error.setter
    def is_error(self, if_error: bool):
        if if_error is not None and isinstance(if_error, bool):
            self.__is_error = if_error
        else:
            raise ValueError("Command message is error must be of type bool and cannot be empty/null")

    @property
    def error_msg(self):
        return self.__error_msg

    @error_msg.setter
    def error_msg(self, msg: str):
        if msg is not None and isinstance(msg, str):
            self.__error_msg = msg
        else:
            raise ValueError("Command error message must be of type str and cannot be empty/null")

    def __str__(self):
        return "{}{}{}{}{}{}{}".format(self.name,
                                       self.separator,
                                       self.request_id,
                                       self.separator if (self.is_error or self.status is not None) else "",
                                       0 if self.is_error else self.status,
                                       self.separator if (self.is_error or len(str(self.payload)) > 0) else "",
                                       self.error_msg if self.is_error else self.payload)

    def parse_str(self, value):

        if isinstance(value, str) and len(value.split(value[3])) >= 3:

            v = value.split(value[3])
            self.name = v[0]
            self.separator = value[3]
            self.request_id = v[1]
            self.status = int(v[2])

            self.is_error = True if self.status == 0 else False
            self.error_msg = v[3] if self.is_error else ""

            return self
        else:
            raise ValueError("The provided string must of correct format to parse and convert to object")

########################################################################################################################


class Cxx_Payload(DeviceMessagePayload):

    def __init__(self, attribs: dict):
        super().__init__()

        self.valid_attr = attribs

        for a in self.valid_attr:
            setattr(self, a, -1)  # set default values

    def parse_str(self, payload: str):

        print("Cxx_Payload.parse_str() invoked with payload:", payload)

        v = payload.split("{}".format(self.separator))
        i = 0

        print("Cxx_Payload.parse_str() payload split:", v)

        for a in self.valid_attr:
            setattr(self, a, str(v[i]))
            i += 1

    def __str__(self):
        return self.separator.join([str(getattr(self, a)) for a in self.valid_attr])


class Cxx_DeviceMessage(DeviceMessageRequest):

    """
    Parent class containing common code to process a command message
    """
    def __init__(self, name: str, cxx_obj: Cxx_Payload):
        super().__init__(name)
        self.payload = cxx_obj if cxx_obj is not None else Cxx_Payload([])

    def parse_str(self, value: str):

        super().parse_str(value)

        if len(self.payload.valid_attr) > 0:
            c = "{}{}{}{}".format(self.name, self.separator, self.request_id, self.separator)
            pl = value.replace(c, "")
            self.payload.separator = self.separator
            self.payload.parse_str(pl)

        return self


class Rxx_Payload(DeviceMessagePayload):

    def __init__(self, attribs: list):

        super().__init__()

        self.valid_attr = attribs

        for a in self.valid_attr:
            setattr(self, a, "0")  # set default values

    def parse_str(self, payload: str):

        print("Rxx_Payload.parse_str() invoked with payload:", payload)

        v = payload.split("{}".format(self.separator))
        i = 0

        print("Rxx_Payload.parse_str() payload split:", v)

        for a in self.valid_attr:
            setattr(self, a, str(v[i]))
            i += 1

    def __str__(self):
        return self.separator.join([getattr(self, a) for a in self.valid_attr])


class Rxx_DeviceMessageResponse(DeviceMessageResponse):

    """
    Parent class containing common code to process a response message
    """
    def __init__(self, name: str, rxx_obj: Rxx_Payload):
        super().__init__(name)
        self.payload = rxx_obj

    def parse_str(self, value: str):

        super().parse_str(value)

        if not self.is_error:
            r = "{}{}{}{}{}{}".format(self.name, self.separator, self.request_id, self.separator, self.status, self.separator)
            pl = value.replace(r, "")
            self.payload.separator = self.separator
            self.payload.parse_str(pl)

        return self

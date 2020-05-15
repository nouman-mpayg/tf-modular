import json


class FailedExecution:

    def __init__(self):
        pass

    def get_cmd_request(self, event):

        errorMessage = self.get_error_message(event)
        cmd_request = event.get('cmd_request', None)

        if errorMessage is not None:
            cmd_request = json.loads(errorMessage)["cmd_request"]

        print("cmd_request is: ", cmd_request)

        return cmd_request

    def get_error_message(self, event):

        errorMessage = None

        if event.get('error_info', {}).get('Cause', {}):
            try:
                errorMessage = json.loads(event.get('error_info', {}).get('Cause', "{}")).get('errorMessage', None)
            except Exception as e:
                return None

        print("errorMessage is: ", errorMessage)

        return errorMessage

    def get_error(self, event):

        error = event.get('error_info', {}).get('Error', None)

        if error:
            if error == "Exception":
                failed_execution = FailedExecution()
                error = json.loads(failed_execution.get_error_message(event))["reason"]
            else:
                error = str(error) + ". See Server logs"

        print("error is: ", error)

        return error

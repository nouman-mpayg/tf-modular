# C07 cloud to device command sending client program

from mpayg_iot.device_messaging.send_message import SendMessage

def handler(event, context):
    return {
        "statusCode": "200",
        "body": "tf_lambda_function_01 been executed.."
    }

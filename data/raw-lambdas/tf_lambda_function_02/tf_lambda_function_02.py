# C07 cloud to device command sending client program
import requests


def handler(event, context):
    return {
        "statusCode": "200",
        "body": "tf_lambda_function_02 been executed.."
    }

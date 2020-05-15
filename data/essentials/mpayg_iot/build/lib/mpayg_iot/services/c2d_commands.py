import json
from random import random

import boto3


class CommandInfo:

    def __init__(self, action_name: str, command_id, command_params):
        self.action_name = action_name
        self.command_id = command_id
        self.command_params = command_params


class C2DCommands:

    def __init__(self):
        self.client = boto3.client('stepfunctions')

    def launch_command_sending(self, hub_ids: list, state_machine_arn: str, command_info: CommandInfo, user_id, event):

        # Currently we are not handling all hubs use-case. But may be in future
        # if len(hub_ids) == 1 and str(hub_ids[0]).lower() == "all":
        #     print("all means going to update all hubs")
        #     return {
        #         "statusCode": 200,
        #         "body": json.dumps({
        #             "status": {
        #                 "code": 200,
        #                 "message": "Success from Lambda provisionAdhocStatusHub",
        #             }
        #         })
        #     }

        for hub_id in hub_ids:

            # consider breaking it up more
            response = {
                "statusCode": 400,
                "body": json.dumps({
                    "status": {
                        "code": 400,
                        "message": "a cloud-to-device command for hub id {} already in progress".format(hub_id),
                    }
                })
            }

            # check if already running
            if self.is_c2d_command_running(hub_id, state_machine_arn):
                if len(hub_ids) == 1:  # means API request is not multi hub update
                    print(response)
                    return response
            else:
                continue

        # Reaching here means we are good to go with starting C2D operation for this hub
        print('Starting execution of C2D operation for this hub: ', hub_id)

        response = self.client.start_execution(
            stateMachineArn=state_machine_arn,
            name="SH_{}_{}_{}".format(command_info.action_name.upper(), hub_id, hex(int(random() * 10000000000))[2:]),
            input=json.dumps({
                "hub_id": hub_id,
                "action": command_info.action_name,
                "createRequestRecordInput": {
                    "command_id": command_info.command_id,
                    "command_params": command_info.command_params,
                    "user_id": user_id
                },
                "provisioner_event": event
            })
        )

        print("self.client.start_execution(): ", response)

        execution_arn_sf = response['executionArn']
        response_desc = self.client.describe_execution(executionArn=execution_arn_sf)

        print("self.client.describe_execution(): ", response_desc)
        print("SF execution status: ", response_desc['status'])

        # responseTerm = self.client.stop_execution(
        #     executionArn = execution_arn_sf,
        #     error = "100",
        #     cause = "User stopped the execution on purpose to test provisioner lambda"
        # )

        # print("self.client.stop_execution(): ", responseTerm)

        return True

    # Check if any Cloud-to-Device command for this hub already running
    def is_c2d_command_running(self, hub_id: str, state_machine_arn: str):

        resposne_list_exec = self.client.list_executions(
            stateMachineArn=state_machine_arn,
            statusFilter='RUNNING',
            maxResults=100
        )

        print("client.list_executions(): ", resposne_list_exec)

        if any(hub_id in i['name'] for i in resposne_list_exec.get('executions')):
            return True
        else:
            return False

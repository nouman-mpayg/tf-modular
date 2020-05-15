resource "random_string" "name" {
  length  = 5
  special = false
  upper   = false
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "${var.func_name}-iam-for-lambda-${random_string.name.result}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}


resource "aws_iam_role_policy" "lambda_invoke_sfn_policy" {
  name = "${var.func_name}-lambda-policy"
  role = "${aws_iam_role.iam_for_lambda.id}"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExecuteLambda",
            "Effect": "Allow",
            "Action": [
                "states:ListExecutions",
                "states:StartExecution",
                "states:DescribeExecution",
                "batch:SubmitJob",
                "cloudwatch:*",
                "logs:*",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "batch:DescribeJobs",
                "codepipeline:GetPipelineState",
                "codepipeline:PutJobSuccessResult",
                "codepipeline:PutJobFailureResult",
                "codebuild:BatchGetBuilds",
                "codebuild:StopBuild",
                "codebuild:UpdateProject",
                "dynamodb:GetItem",
                "dynamodb:UpdateItem",
                "apigateway:*",
                "s3:*",
                "codecommit:*",
                "codepipeline:StartPipelineExecution",
                "codebuild:ListBuildsForProject",
                "events:*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
EOF
}
resource "null_resource" "pip_install" {
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]

    working_dir = "${var.source_dir == "" ? "${path.root}/data/raw-lambdas/${var.func_name}" : var.source_dir}"

    command = <<EOF
      pip3 install \
      -t ${var.absolute_path}/data/raw-lambdas/${var.func_name}/vendors \
      -r ${var.absolute_path}/data/raw-lambdas/${var.func_name}/requirements.txt --upgrade \
      $(pip3 install --system 2> /dev/null; if [ $? == 0 ] ; then echo --system; fi) \
    EOF
  }

  triggers = {
    string = "${timestamp()}"
  }
}

data "archive_file" "make_zip" {
  type        = "zip"
  source_dir  = "${var.source_dir == "" ? "${path.root}/data/raw-lambdas/${var.func_name}" : var.source_dir}"
  output_path = "${path.root}/data/lambda-zips/${var.func_name}.zip"

  depends_on = [
    "null_resource.pip_install",
  ]
}
resource "aws_lambda_function" "lambda_function" {
  filename      = "${path.root}/data/lambda-zips/${var.func_name}.zip"
  function_name = "${var.func_name}"
  role          = "${aws_iam_role.iam_for_lambda.arn}"
  handler       = "${var.func_name}.handler"
  runtime       = "${var.runtime}"
  timeout       = "${var.timeout}"

  environment = {
    variables = "${var.env}"
  }
}

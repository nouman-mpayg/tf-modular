
resource "aws_iam_role" "stf_role" {
  name = "${var.sfn_name}-iam-for-sfn"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "sfn_policy" {
  role = "${aws_iam_role.stf_role.name}"
  name = "${var.sfn_name}-sfn-policy"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExecuteLambda",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
EOF
}

resource "aws_sfn_state_machine" "sfn" {
  name       = "${var.sfn_name}"
  role_arn = "${aws_iam_role.stf_role.arn}"
  definition = "${data.template_file.sfn_file.rendered}"
  depends_on = [
    "aws_lambda_function.lambda_function",
  ]
}

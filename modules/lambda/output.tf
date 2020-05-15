output "arn" {
    value = "${aws_lambda_function.lambda_function.arn}"
}

output "iam_role_arn" {
    value = "${aws_iam_role.iam_for_lambda.arn}"
}

output "lambda_name" {
    value = "${aws_lambda_function.lambda_function.function_name}"
}

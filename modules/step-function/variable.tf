data "template_file" "sfn_file" {
  template = "${file("*/services/data/step-function-jsons/${var.sfn_name}.json")}"

  vars = {
    region                  = "${var.region}"
    aws_account_id          = "${var.aws_account_id}"
  }
}

variable "sfn_name" {
  type = "string"
}

variable "prefix" {
  type = "string"
}

variable "aws_account_id" {
  type = "string"
  default = "219767559618"
}

variable "region" {
  type = "string"
  default = "eu-west-1"
}

module "tf_step_function_01" {
  source         = "./modules/step-function"
  sfn_name       = "tf_step_function_01"
  prefix         = "stf-"
  region         = "eu-west-1"
  aws_account_id = "219767559618"
}
module "tf_step_function_02" {
  source         = "./modules/step-function"
  sfn_name       = "tf_step_function_02"
  prefix         = "stf-"
  region         = "eu-west-1"
  aws_account_id = "219767559618"
}

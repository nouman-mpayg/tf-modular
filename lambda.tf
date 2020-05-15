module "lambda_function_invoke_01" {
  source     = "./modules/lambda"
  func_name  = "tf_lambda_function_01"
  source_dir = "${path.root}/data/raw-lambdas/tf_lambda_function_01"
  region     = "u-west-1"
  env = {
    PYTHONPATH = "/var/task/vendors:/var/runtime"
  }
}
module "lambda_function_invoke_02" {
  source     = "./modules/lambda"
  func_name  = "tf_lambda_function_02"
  source_dir = "${path.root}/data/raw-lambdas/tf_lambda_function_02"
  region     = "eu-west-1"
  env = {
    PYTHONPATH = "/var/task/vendors:/var/runtime"
  }
}

data "external" "read_secrets" {
  program = [
    "python3",
    "${path.module}/../../setup.py",
    "convert",
    "secrets",
    "--workspace=${terraform.workspace}",
    "--create_logs=false",
  ]

  query = {}
}

data "terraform_remote_state" "rds" {
  backend   = "s3"
  workspace = "${data.external.read_secrets.result["workspace"]}"

  config = {
    bucket         = "mp-tf-states"
    key            = "mp-tf-states/rds"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-state"
  }
}

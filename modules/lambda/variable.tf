variable "func_name" {
  type = "string"
}
variable "env" {
  type = "map"
}
variable "timeout" {
  type    = "string"
  default = "20"
}
variable "runtime" {
  type    = "string"
  default = "python3.6"
}
variable "root" {
  type    = "string"
  default = "/Users/adeel/Desktop/mpayg-learning/terraform-modular/services"
}
variable "region" {
  type    = "string"
}
variable "source_dir" {
  type    = "string"
  default = ""
}
variable "absolute_path" {
  type    = "string"
  default = "/Users/adeel/Desktop/mpayg-learning/terraform-modular/services"
}
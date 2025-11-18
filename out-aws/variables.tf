variable "project_name" {
  type = string
}

variable "aws_region" {
  type = string
}

variable "tags" {
  type    = map(string)
  default = {}
}

# Feature flags per le risorse opzionali
variable "enable_vpc" {
  type    = bool
  default = false
}

variable "enable_ec2" {
  type    = bool
  default = false
}

variable "enable_s3" {
  type    = bool
  default = false
}

# VPC
variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  type    = string
  default = "10.0.1.0/24"
}

# EC2
variable "ec2_instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ec2_ami_id" {
  type    = string
  default = "ami-1234567890abcdef0"
}

# S3
variable "s3_bucket_name" {
  type = string
}

variable "s3_versioning" {
  type    = bool
  default = false
}

terraform {
    required_version = ">= 1.0.0"

    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
}

provider "aws" {
    region = "us-west-2"
}

resource "aws_instance" "app" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"

  tags = {
    Name        = "sample-app"

    Environment = "Development"

    Project = "SampleApp"

  }
}
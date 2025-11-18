project_name = "iac-factory-aws-demo"
aws_region   = "eu-central-1"

tags = {

  environment = "dev"

  owner = "joule"

  project = "iac-factory-lite"

}

# Feature flags
enable_vpc = true
enable_ec2 = true
enable_s3  = true

# VPC
vpc_cidr           = "10.20.0.0/16"
public_subnet_cidr = "10.20.1.0/24"

# EC2
ec2_instance_type = "t3.micro"
ec2_ami_id        = "ami-1234567890abcdef0"

# S3
s3_bucket_name = "iac-factory-demo-bucket"
s3_versioning  = true

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# =========================
# VPC (opzionale)
# =========================
resource "aws_vpc" "this" {
  count = var.enable_vpc ? 1 : 0

  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(
    {
      Name = "${var.project_name}-vpc"
    },
    var.tags,
  )
}

resource "aws_subnet" "public" {
  count = var.enable_vpc ? 1 : 0

  vpc_id                  = aws_vpc.this[0].id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true

  tags = merge(
    {
      Name = "${var.project_name}-public-subnet"
    },
    var.tags,
  )
}

# =========================
# EC2 (opzionale)
# =========================
resource "aws_instance" "app" {
  count = var.enable_ec2 ? 1 : 0

  ami           = var.ec2_ami_id
  instance_type = var.ec2_instance_type

  # Se esiste una subnet VPC usiamola, altrimenti lasciamo scegliere ad AWS
  subnet_id = var.enable_vpc ? aws_subnet.public[0].id : null

  tags = merge(
    {
      Name = "${var.project_name}-ec2"
    },
    var.tags,
  )
}

# =========================
# S3 (opzionale)
# =========================
resource "aws_s3_bucket" "this" {
  count = var.enable_s3 ? 1 : 0

  bucket = var.s3_bucket_name

  tags = merge(
    {
      Name = "${var.project_name}-bucket"
    },
    var.tags,
  )
}

resource "aws_s3_bucket_versioning" "this" {
  count = var.enable_s3 && var.s3_versioning ? 1 : 0

  bucket = aws_s3_bucket.this[0].id

  versioning_configuration {
    status = "Enabled"
  }
}

terraform {
  required_version = ">= 1.6"

  backend "s3" {
    bucket = "terraform-state-file-devops-capstone-2"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
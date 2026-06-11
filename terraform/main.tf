module "vpc" {
  source = "./modules/vpc"
}

module "ecr" {
  source = "./modules/ecr"

  frontend_repo_name = "devops-frontend"
  backend_repo_name  = "devops-backend"
}
module "eks" {
  source = "./modules/eks"

  cluster_name    = "devops-eks"
  cluster_version = "1.33"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
}
module "rds" {
  source = "./modules/rds"

  vpc_id             = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  db_password        = var.db_password
}
module "lambda_s3" {
  source = "./modules/lambda-s3"

  project_name = "devops-master"
}
module "loki_s3" {
  source = "./modules/loki-s3"
}
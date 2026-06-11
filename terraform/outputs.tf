output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_ids" {
  value = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  value = module.vpc.private_subnet_ids
}
output "frontend_repository_url" {
  value = module.ecr.frontend_repository_url
}

output "backend_repository_url" {
  value = module.ecr.backend_repository_url
}
output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "eks_cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "eks_cluster_arn" {
  value = module.eks.cluster_arn
}
output "oidc_provider_arn" {
  value = module.eks.oidc_provider_arn
}

output "oidc_issuer_url" {
  value = module.eks.oidc_issuer_url
}
output "rds_endpoint" {
  value = module.rds.rds_endpoint
}

output "rds_db_name" {
  value = module.rds.rds_db_name
}
output "lambda_function_name" {
  value = module.lambda_s3.lambda_function_name
}

output "s3_bucket_name" {
  value = module.lambda_s3.s3_bucket_name
}
output "loki_bucket_name" {
  value = module.loki_s3.loki_bucket_name
}
variable "frontend_repo_name" {
  description = "Frontend ECR repository name"
  type        = string
  default     = "devops-frontend"
}

variable "backend_repo_name" {
  description = "Backend ECR repository name"
  type        = string
  default     = "devops-backend"
}
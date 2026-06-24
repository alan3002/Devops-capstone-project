# 🚀 DevOps Capstone Project
-----------------------------

A complete Production-Style DevOps implementation on AWS demonstrating Infrastructure as Code, CI/CD, GitOps, Kubernetes Deployments, Observability, Logging, Alerting, Serverless Automation, and Progressive Delivery.

---

## 📌 Project Overview

This project simulates a real-world DevOps workflow used in modern cloud environments.

The application consists of:

- Frontend Application
- Backend API Service
- Amazon RDS MySQL Database
- Amazon EKS Kubernetes Cluster
- Amazon ECR Container Registry
- GitHub Actions CI Pipeline
- ArgoCD GitOps Deployment
- Argo Rollouts Canary Deployment
- Prometheus Monitoring
- Grafana Dashboards & Alerting
- Loki Centralized Logging
- AWS Lambda + SNS Automation
- Terraform Infrastructure Provisioning

---

# 🏗️ Architecture

Users
│
▼
Route53
│
▼
Application Load Balancer(ingress)
│
▼
Amazon EKS Cluster
├── Staging Namespace
├── Production Namespace
├── Prometheus
├── Grafana
├── Loki
│
▼
Amazon RDS

Developer
│
▼
GitHub
│
▼
GitHub Actions
│
▼
Amazon ECR
│
▼
ArgoCD
│
▼
Amazon EKS

Application Events
│
▼
Amazon S3
│
▼
AWS Lambda
│
▼
Amazon SNS
│
▼
Email Notification

---

# ⚙️ Technology Stack

## Cloud
- AWS

## Infrastructure as Code
- Terraform

## Containerization
- Docker

## Container Registry
- Amazon ECR

## Kubernetes
- Amazon EKS

## GitOps
- ArgoCD

## Progressive Delivery
- Argo Rollouts

## Monitoring
- Prometheus

## Visualization
- Grafana

## Logging
- Loki
- Promtail

## Database
- Amazon RDS MySQL

## CI/CD
- GitHub Actions

## Serverless
- AWS Lambda
- Amazon SNS

---

# 📂 Repository Structure

```bash
.
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       └── backend.yml
│
├── app/
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── index.html
│   │   └── nginx.conf
│   │
│   └── backend/
│       ├── app.py
│       ├── requirements.txt
│       ├── test_app.py
│       └── Dockerfile
│
├── terraform/
│   ├── modules/
│   │   ├── vpc/
│   │   ├── eks/
│   │   ├── ecr/
│   │   └── rds/
│   │
│   ├── provider.tf
│   └── main.tf
│
├── k8s/
│   ├── staging/
│   └── production/
│
├── loki-s3-values.yaml
├── grafana-smtp-values.yaml
├── backend-s3-policy.json
└── trust-policy.json
```

---

# 🌐 Infrastructure Provisioning using Terraform

Terraform provisions:

- Custom VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- EKS Cluster
- ECR Repositories
- RDS MySQL

## Initialize Terraform

```bash
terraform init
```

## Validate Configuration

```bash
terraform validate
```

## Plan Infrastructure

```bash
terraform plan
```

## Deploy Infrastructure

```bash
terraform apply
```

---

# 🐳 Docker Containerization

## Frontend

Build Image

```bash
docker build -t devops-frontend ./app/frontend
```

## Backend

Build Image

```bash
docker build -t devops-backend ./app/backend
```

---

# 📦 Amazon ECR

Login to ECR

```bash
aws ecr get-login-password \
| docker login \
--username AWS \
--password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

Push Image

```bash
docker push IMAGE_NAME
```

---

# 🔄 CI Pipeline using GitHub Actions

The CI Pipeline automatically performs:

1. Source Checkout
2. Application Validation
3. Dependency Installation
4. Unit Testing
5. Docker Build
6. Trivy Security Scan
7. Push Image to ECR

### Trigger

Pipeline runs automatically on:

```yaml
push:
```

---

# ☸️ Kubernetes Deployment

Namespaces:

```bash
staging
production
```

Deployments:

- Frontend Deployment
- Backend Deployment
- Services
- Ingress
- HPA

---

# 🚀 GitOps using ArgoCD

ArgoCD continuously watches GitHub repository.

Whenever manifests are updated:

```text
Git Push
     ↓
ArgoCD Detects Change
     ↓
Sync Application
     ↓
Deploy to EKS
```

Benefits:

- Git as Single Source of Truth
- Automated Deployments
- Easy Rollbacks
- Environment Consistency

---

# 🎯 Canary Deployments using Argo Rollouts

Progressive delivery strategy:

```text
Version v1
     ↓
Deploy v2
     ↓
50% Traffic
     ↓
Pause
     ↓
100% Traffic
     ↓
Promote Stable
```

### Rollout Status

```bash
kubectl argo rollouts get rollout backend-rollout-demo -n staging
```

### Rollback

```bash
kubectl argo rollouts undo rollout backend-rollout-demo -n staging
```

---

# 📊 Monitoring with Prometheus

Install Monitoring Stack

```bash
kubectl create namespace monitoring

helm repo add prometheus-community \
https://prometheus-community.github.io/helm-charts

helm repo update

helm install monitoring \
prometheus-community/kube-prometheus-stack \
-n monitoring
```

Metrics Collected:

- CPU Usage
- Memory Usage
- Pod Health
- Restart Count
- Request Latency

---

# 📈 Grafana Dashboards

Configured Dashboards:

## Kubernetes Dashboard

Displays:

- Cluster Health
- Node Usage
- Pod Usage
- Namespace Metrics

## Application Dashboard

Displays:

- Frontend Requests
- Backend Requests
- Response Times

---

# 📝 Centralized Logging using Loki

Components:

```text
Application Pods
        ↓
Promtail
        ↓
Loki
        ↓
Grafana Explore
```

Features:

- Centralized Logs
- Log Search
- LogQL Queries
- Historical Analysis

---

# ☁️ Store Loki Logs in Amazon S3

Create IAM Policy

```bash
aws iam create-policy \
--policy-name LokiS3Policy \
--policy-document file://loki-s3-policy.json
```

Attach Policy

```bash
aws iam attach-role-policy \
--role-name AmazonEKSLokiS3Role \
--policy-arn POLICY_ARN
```

Annotate Service Account

```bash
kubectl annotate serviceaccount loki \
-n monitoring \
eks.amazonaws.com/role-arn=ROLE_ARN \
--overwrite
```

---

# 🔔 Grafana Alerting

Alerting Flow

```text
Prometheus
      ↓
Grafana Alert Rule
      ↓
Contact Point
      ↓
Email Notification
```

Configured:

- SMTP Integration
- Contact Points
- Notification Policies
- Alert Rules

Example Alert:

```text
Backend Pod Down
Available Replicas < 1
```

---

# ⚡ Serverless Automation

Workflow:

```text
User Registration
        ↓
Store Data in RDS
        ↓
Create JSON File
        ↓
Upload to S3
        ↓
Lambda Trigger
        ↓
SNS Notification
        ↓
Email Sent
```

Components:

- S3 Bucket
- Lambda Function
- SNS Topic
- Email Subscription

---

# 🗄️ Database Layer

Database:

```text
Amazon RDS MySQL
```

Stores:

- User Information
- Registration Records

Backend connects securely using environment variables and Kubernetes Secrets.

---

# 🔐 Security Best Practices

Implemented:

- IAM Roles
- IRSA (IAM Roles for Service Accounts)
- Kubernetes Secrets
- Private Subnets
- Security Groups
- Trivy Image Scanning
- GitOps Controlled Deployments

---

# 🎯 Key DevOps Concepts Demonstrated

✅ Infrastructure as Code

✅ Containerization

✅ CI/CD

✅ GitOps

✅ Progressive Delivery

✅ Kubernetes

✅ Monitoring

✅ Logging

✅ Alerting

✅ Serverless

✅ AWS Cloud Services

---

# 👨‍💻 Author

**Alan Biju**

DevOps Engineer | AWS | Kubernetes | Terraform | GitOps | CI/CD

LinkedIn: <your-linkedin>

GitHub: https://github.com/alan3002

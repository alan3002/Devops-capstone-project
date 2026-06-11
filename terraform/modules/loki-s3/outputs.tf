output "loki_bucket_name" {
  value = aws_s3_bucket.loki_logs.bucket
}
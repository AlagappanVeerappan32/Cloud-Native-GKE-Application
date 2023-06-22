variable "gcp_credentials" {
  type        = string
  description = "location of GCP credentials"
}

variable "project_id" {
  type        = string
  description = "project id"
}

variable "cluster_name" {
  type        = string
  description = "cluster name "
}

variable "region" {
  type        = string
  description = "region name id"
}

variable "region_zones" {
  type        = list(string)
  description = "list of zones"
}

variable "node_pool_name" {
  type        = string
  description = "name of node pool"
}

variable "machine_type" {
  type        = string
  description = "name of node pool"
}

variable "disk_type" {
  type        = string
  description = "name of node pool"
}

variable "service_account" {
  type        = string
  description = "name of node pool"
}


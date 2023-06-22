terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.66.0"
    }
  }
}

module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.project_id
  name                       = var.cluster_name
  region                     = var.region
  regional                   = false
  zones                      = var.region_zones
  network                    = "default"
  subnetwork                 = "default"
  ip_range_pods              = ""
  ip_range_services          = ""
  http_load_balancing        = false
  network_policy             = false
  horizontal_pod_autoscaling = true

  node_pools = [
    {
      name               = "my-first-name-pool"
      machine_type       = var.machine_type
      node_locations     = "us-central1-c"
      min_count          = 3 // Minimum number of nodes
      max_count          = 3 // Maximum number of nodes 
      local_ssd_count    = 0
      preemptible        = false
      disk_size_gb       = 10
      disk_type          = var.disk_type
      image_type         = "COS_CONTAINERD"
      enable_gcfs        = false
      enable_gvnic       = false
      auto_repair        = true
      auto_upgrade       = true
      initial_node_count = 3 // Desired number of nodes
    },
  ]

  node_pools_oauth_scopes = {
    all = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }

  node_pools_labels = {
    all = {}

    default-node-pool = {
      default-node-pool = true
    }
  }

  node_pools_metadata = {
    all = {}

    default-node-pool = {
      node-pool-metadata-custom-value = "my-node-pool"
    }
  }

  node_pools_taints = {
    all = []

    default-node-pool = [
      {
        key    = "default-node-pool"
        value  = true
        effect = "PREFER_NO_SCHEDULE"
      },
    ]
  }

  node_pools_tags = {
    all = []

    default-node-pool = [
      "default-node-pool",
    ]
  }
}

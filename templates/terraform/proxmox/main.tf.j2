terraform {
  required_version = ">= 1.0.0"

  required_providers {
    proxmox = {
      source  = "Telmate/proxmox"
      version = "~> 3.0"
    }
  }
}

provider "proxmox" {
  pm_api_url          = var.proxmox_endpoint
  pm_api_token_id     = var.proxmox_token_id
  pm_api_token_secret = var.proxmox_token_secret
  pm_tls_insecure     = true
}

resource "proxmox_vm_qemu" "this" {
  name        = var.vm_name
  target_node = var.node
  cores       = var.cores
  memory      = var.memory_mb

  disk {
    size    = "${var.disk_gb}G"
    storage = var.storage
  }

  iso = var.iso_image
}

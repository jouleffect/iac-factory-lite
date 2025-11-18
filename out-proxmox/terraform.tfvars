project_name          = "iac-factory-proxmox-demo"
proxmox_endpoint      = "https://proxmox.example.local:8006/api2/json"
proxmox_token_id      = "root@pam!iac-factory"
proxmox_token_secret  = "super-secret-token"

vm_name   = "iac-factory-demo-vm"
node      = "pve1"
memory_mb = 4096
cores     = 2
disk_gb   = 40
storage   = "local-lvm"
iso_image = "local:iso/debian-12.iso"

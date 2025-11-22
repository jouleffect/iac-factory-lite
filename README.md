# 🏗️ IaC Factory LITE  
**YAML → Terraform Generator (Free Version)**

IaC Factory LITE is a command-line tool that takes a YAML file
and automatically generates a Terraform or Ansible project structure based on the provided parameters.

This version is intended as a simple **open-source base**

The **PRO** version (coming soon) will include:
- complete **Terraform + Ansible** generation
- auto-generated folder structure
- advanced Jinja2 templates
- bundle mode (ZIP)
- additional validations
- multiple generators (EC2, VPC, S3, ECS, etc.)

---

## Features (LITE)

✔ Reads a YAML file   
✔ Automatically generates a terraform project structure consisting of   
- `main.tf`
- `variables.tf`
- `outputs.tf`
- `terraform.tfvars`

✔ Simple Jinja2 Template (Extensible)  
✔ Intuitive CLI command  
✔ Simple YAML input

AWS example
```yaml
cloud: aws

project_name: iac-factory-aws-demo
aws_region: eu-central-1

tags:
  environment: dev
  owner: joule

ec2:
  enabled: true
  instance_type: t3.micro
  ami_id: ami-1234567890abcdef0

s3:
  enabled: true
  bucket_name: iac-factory-demo-bucket
  versioning: true

vpc:
  enabled: true
  vpc_cidr: 10.20.0.0/16
  public_subnet_cidr: 10.20.1.0/24

```
Proxmox example
```yaml
cloud: proxmox

project_name: iac-factory-proxmox-demo

proxmox:
  endpoint: https://proxmox.example.local:8006/api2/json
  token_id: root@pam!iac-factory
  token_secret: super-secret-token

vm:
  name: demo-vm
  node: pve1
  memory_mb: 4096
  cores: 2
  disk_gb: 40
  storage: local-lvm
  iso_image: local:iso/debian-12.iso
```

Output
```bash
out/
├── main.tf
├── variables.tf
├── outputs.tf
└── terraform.tfvars
```
All .tf files use only var.*.   
All dynamic values ​​are generated in .tfvars.

---

## 📦 Requirements

- Python 3.9+
- `pip install -r requirements.txt`
- (optional) Terraform installed to validate the generated files

---

## 📁 Project Structure (LITE)

```bash
iac-factory-lite/
├── iac_factory/
│   ├── cli.py
│   └── generator_terraform.py
├── templates/
│   └── terraform/
│       ├── aws/
│       └── proxmox/
├── examples/
│   └── terraform/
│       ├── aws/
│       └── proxmox/
├── README.md
└── LICENSE
```

---

### ▶️ How to use

1. Clone the repo
```bash
git clone https://github.com/<tuo-utente>/iac-factory-lite.git
cd iac-factory-lite
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Generate all Terraform files:
```bash
python -m iac_factory.cli examples/aws-sample.yaml -o out-aws
```
4. Generate only some files:
```bash
python -m iac_factory.cli examples/aws-sample.yaml -o out --main --tfvars
```
5. Flags available:
```css
--main
--variables
--outputs
--tfvars
```

Expected output:
```bash
[OK] Generated out-aws/main.tf
[OK] Generated out-aws/variables.tf
[OK] Generated out-aws/outputs.tf
[OK] Generated out-aws/terraform.tfvars
```
6. Validation with Terraform
```bash
cd out-aws
terraform init
terraform validate
```
---

| Feature                | LITE              | PRO                 |
| ---------------------- | ----------------- | ------------------- |
| YAML → main.tf         | ✔                 | ✔                   |
| YAML → variables.tf    | ✔ (minimal)       | ✔ (advanced)        |
| YAML → outputs.tf      | ✔ (minimal)       | ✔ (complete)        |
| terraform.tfvars       | ✔  auto           | ✔ with multienv     |
| Multi-template AWS     | ❌                | ✔ (many modules)    |
| Proxmox support        | ✔ (simple)        | ✔ (advanced) |
| Ansible output         | ❌                 | ✔                   |
| Bundle ZIP             | ❌                 | ✔                   |
| Multi-file per risorsa | ❌                 | ✔                   |
| Validazioni YAML       | ❌                 | ✔                   |
| Multi-environment      | ❌                 | ✔                   |
| Moduli Terraform       | ❌                 | ✔                   |
| backend remoto         | ❌                 | ✔                   |
| Documentazione         | minimal            | complete            |
| Struttura enterprise   | ❌                 | ✔                   |


--- 

📜 License

MIT License (see the LICENSE file).

---

🧑‍💻 Author

IaC Factory LITE — by Joule (2025)
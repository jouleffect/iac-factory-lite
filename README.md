# 🏗️ IaC Factory LITE  
**YAML → Terraform Generator (Versione Gratuita)**

IaC Factory LITE è un piccolo tool da linea di comando che prende un file YAML
e genera automaticamente un file `main.tf` Terraform basato sui parametri forniti.

Questa versione è pensata come **base open-source**, semplice e didattica.

La versione **PRO** (in arrivo) includerà:
- generazione completa **Terraform + Ansible**
- struttura cartelle auto-generata
- template Jinja2 avanzati
- modalità `bundle` (ZIP)
- validazioni aggiuntive
- generatori multipli (EC2, VPC, S3, ECS, ecc.)

---

## Funzionalità (LITE)

✔ Legge un file YAML  
✔ Genera automaticamente una struttura di progetto terraform composta da
 - `main.tf`
 - `variables.tf`
 - `outputs.tf`
 - `terraform.tfvars` 

✔ Template Jinja2 semplice (estendibile)  
✔ Comando CLI intuitivo  
✔ Input YAML semplice

Esempio AWS
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
Esempio Proxmox
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

Output generato
```bash
out/
├── main.tf
├── variables.tf
├── outputs.tf
└── terraform.tfvars
```
Tutti i file .tf usano solo var.*.
Tutti i valori dinamici vengono generati nel .tfvars.

---

## 📦 Requisiti

- Python 3.9+
- `pip install -r requirements.txt`
- (opzionale) Terraform installato per validare il file generato

---

## 📁 Struttura progetto (LITE)

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

### ▶️ Come usarlo

1. Clona il repo
```bash
git clone https://github.com/<tuo-utente>/iac-factory-lite.git
cd iac-factory-lite
```
2. Installa le dipendenze
```bash
pip install -r requirements.txt
```
3. Generare tutti i file Terraform:
```bash
python -m iac_factory.cli examples/aws-sample.yaml -o out-aws
```
4. Generare solo alcuni file:
```bash
python -m iac_factory.cli examples/aws-sample.yaml -o out --main --tfvars
```
5. Flag disponibili:
```css
--main
--variables
--outputs
--tfvars
```

Output atteso:
```bash
[OK] Generato out-aws/main.tf
[OK] Generato out-aws/variables.tf
[OK] Generato out-aws/outputs.tf
[OK] Generato out-aws/terraform.tfvars
```
6. Validazione con Terraform
```bash
cd out-aws
terraform init
terraform validate
```
---

| Feature                | LITE              | PRO                 |
| ---------------------- | ----------------- | ------------------- |
| YAML → main.tf         | ✔                 | ✔                   |
| YAML → variables.tf    | ✔ (minimale)      | ✔ (avanzato)        |
| YAML → outputs.tf      | ✔ (minimale)      | ✔ (completo)        |
| terraform.tfvars       | ✔  auto           | ✔ con multienv      |
| Multi-template AWS     | ❌                | ✔ (molti moduli)    |
| Proxmox support        | ✔ (semplice)      | ✔ (modulo avanzato) |
| Ansible output         | ❌                 | ✔                   |
| Bundle ZIP             | ❌                 | ✔                   |
| Multi-file per risorsa | ❌                 | ✔                   |
| Validazioni YAML       | ❌                 | ✔                   |
| Multi-environment      | ❌                 | ✔                   |
| Moduli Terraform       | ❌                 | ✔                   |
| backend remoto         | ❌                 | ✔                   |
| Documentazione         | minima            | completa            |
| Struttura enterprise   | ❌                 | ✔                   |


--- 

📜 Licenza

MIT License (consulta il file LICENSE).

---

🧑‍💻 Autore

IaC Factory LITE — by Joule (2025)
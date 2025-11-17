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

## 🚀 Funzionalità (LITE)

✔ Legge un file YAML  
✔ Genera un file `main.tf` con valori sostituiti  
✔ Template Jinja2 semplice (estendibile)  
✔ Comando CLI intuitivo  
✔ Zero dipendenze strane (solo `PyYAML` + `Jinja2`)

---

## 📦 Requisiti

- Python 3.9+
- `pip install -r requirements.txt`
- (opzionale) Terraform installato per validare il file generato

---

## 📁 Struttura progetto (LITE)

iac-factory-lite/
├─ iac_factory/
│ ├─ init.py
│ ├─ cli.py
│ └─ generator_terraform.py
├─ templates/
│ └─ terraform/
│ └─ main.tf.j2
├─ examples/
│ └─ sample-app.yaml
├─ requirements.txt
└─ README.md


---

## 🧪 Esempio YAML

`examples/sample-app.yaml`

```yaml
project_name: demo-app
aws_region: eu-central-1
instance_type: t3.micro
ami_id: ami-12345678
tags:
  environment: dev
  owner: demo
```

---

▶️ Come usarlo

1. Clona il repo
```bash
git clone https://github.com/<tuo-utente>/iac-factory-lite.git
cd iac-factory-lite
```
2. Installa le dipendenze
```bash
pip install -r requirements.txt
```
3. Genera il file Terraform
```bash
python -m iac_factory.cli examples/sample-app.yaml -o out
```
Output atteso:
```bash
[OK] Generato out/main.tf a partire da examples/sample-app.yaml
```

📌 Obiettivi della versione LITE

Mostrare il funzionamento del generatore
Offrire un esempio didattico utilizzabile subito
Permettere di estendere il template con facilità
La versione PRO aggiungerà molte funzionalità per DevOps / Cloud Engineer, mantenendo però un workflow semplice e lineare.

🚧 Versione PRO (coming soon)

La versione PRO includerà:

🔧 Output multipli

Terraform
Ansible
Struttura di progetto pronta all’uso

📂 Generazione completa

main.tf, variables.tf, outputs.tf
playbook Ansible + tasks

README generato automaticamente

🧰 Funzionalità aggiuntive

Validazione YAML avanzata
Modalità bundling (--bundle)
Template estesi AWS (EC2, VPC, ECS, S3, Lambda)
Supporto estendibile via plugin
Se vuoi essere avvisato quando sarà disponibile la versione PRO, potrai trovare info nel repo quando sarà pronta.

📄 Licenza

Rilasciato sotto licenza MIT.
Puoi usarlo liberamente per progetti personali e professionali.

🤝 Contribuire

Ogni contributo è benvenuto:
nuovi template
fix
miglioramenti CLI
documentazione
Apri una pull request o una issue!
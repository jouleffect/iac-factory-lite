import pathlib
from typing import Dict, Iterable, Optional

from jinja2 import Environment, FileSystemLoader


SUPPORTED_CLOUDS = {"aws", "proxmox"}

ALL_FILES = {
    "main": "main.tf",
    "variables": "variables.tf",
    "outputs": "outputs.tf",
    "tfvars": "terraform.tfvars",
}


def _get_env(cloud: str) -> Environment:
    base_dir = pathlib.Path(__file__).resolve().parent.parent
    templates_dir = base_dir / "templates" / "terraform" / cloud
    return Environment(loader=FileSystemLoader(str(templates_dir)), keep_trailing_newline=True)


def _build_context(cloud: str, config: Dict) -> Dict:
    """
    Costruisce il context da passare ai template Jinja2.
    """
    ctx: Dict = {}

    ctx["project_name"] = config.get("project_name", "demo-project")

    # tags generici (per AWS)
    ctx["tags"] = config.get("tags", {})

    if cloud == "aws":
        ctx["aws_region"] = config.get("aws_region", "eu-central-1")

        # blocchi risorse
        ec2_cfg = config.get("ec2", {}) or {}
        s3_cfg = config.get("s3", {}) or {}
        vpc_cfg = config.get("vpc", {}) or {}

        ctx["ec2"] = {
            "enabled": bool(ec2_cfg.get("enabled", False)),
            "instance_type": ec2_cfg.get("instance_type", "t3.micro"),
            "ami_id": ec2_cfg.get("ami_id", "ami-1234567890abcdef0"),
        }

        ctx["s3"] = {
            "enabled": bool(s3_cfg.get("enabled", False)),
            "bucket_name": s3_cfg.get("bucket_name", "iac-factory-demo-bucket"),
            "versioning": bool(s3_cfg.get("versioning", False)),
        }

        ctx["vpc"] = {
            "enabled": bool(vpc_cfg.get("enabled", False)),
            "vpc_cidr": vpc_cfg.get("vpc_cidr", "10.0.0.0/16"),
            "public_subnet_cidr": vpc_cfg.get("public_subnet_cidr", "10.0.1.0/24"),
        }

    elif cloud == "proxmox":
        prox_cfg = config.get("proxmox", {}) or {}
        vm_cfg = config.get("vm", {}) or {}

        ctx["proxmox"] = {
            "endpoint": prox_cfg.get("endpoint", ""),
            "token_id": prox_cfg.get("token_id", ""),
            "token_secret": prox_cfg.get("token_secret", ""),
        }

        ctx["vm"] = {
            "name": vm_cfg.get("name", "demo-vm"),
            "node": vm_cfg.get("node", "pve1"),
            "memory_mb": int(vm_cfg.get("memory_mb", 2048)),
            "cores": int(vm_cfg.get("cores", 2)),
            "disk_gb": int(vm_cfg.get("disk_gb", 20)),
            "storage": vm_cfg.get("storage", "local-lvm"),
            "iso_image": vm_cfg.get("iso_image", "local:iso/debian-12.iso"),
        }

    return ctx


def render_files(config: Dict, only: Optional[Iterable[str]] = None) -> Dict[str, str]:
    """
    Ritorna un dict:
      {
        "main.tf": "...",
        "variables.tf": "...",
        "outputs.tf": "...",
        "terraform.tfvars": "...",
      }

    Se `only` è impostato (insieme di chiavi logiche: {"main", "variables", ...}),
    genera solo quei file.
    """
    cloud = config.get("cloud")
    if cloud not in SUPPORTED_CLOUDS:
        raise ValueError(
            f"Cloud non supportato: {cloud!r}. "
            f"Valori validi: {', '.join(sorted(SUPPORTED_CLOUDS))}"
        )

    env = _get_env(cloud)
    ctx = _build_context(cloud, config)

    if only:
        keys = [k for k in ALL_FILES if k in set(only)]
    else:
        keys = list(ALL_FILES.keys())

    rendered: Dict[str, str] = {}
    for logical_name in keys:
        out_name = ALL_FILES[logical_name]
        template_name = out_name + ".j2"
        template = env.get_template(template_name)
        rendered[out_name] = template.render(**ctx)

    return rendered

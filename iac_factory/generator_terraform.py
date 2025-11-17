import pathlib
from typing import Dict 

from jinja2 import Environment, FileSystemLoader

def render_main_tf(config: Dict) -> str:
    """
    Genera il contenuto del file main.tf utilizzando un template Jinja2
    e i dati di configurazione forniti.
    """
    base_dir = pathlib.Path(__file__).resolve().parent.parent
    templates_dir = base_dir / "templates" / "terraform"

    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("main.tf.j2")

    context = {
        "project_name": config.get("project-name", "default-project"),
        "aws_region": config.get("aws-region", "us-east-1"),
        "instance_type": config.get("instance-type", "t2.micro"),
        "ami_id": config.get("ami-id", "ami-12345678"),
        "tags": config.get("tags", {}),
    }

    return template.render(**context)
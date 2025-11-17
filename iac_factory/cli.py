import argparse
import pathlib

import yaml

from .generator_terraform import render_main_tf

def main() -> None: 
    parser = argparse.ArgumentParser( 
        prog="iac-factory-lite",
        description="Generatore di infrastruttura come codice semplificato per Terraform",
    )
    parser.add_argument(
        "config",
        help="Percorso al file di configurazione YAML",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="out",
        help="Directory di output per i file Terraform generati",
    )

    args = parser.parse_args()

    config_path = pathlib.Path(args.config)
    if not config_path.is_file():
        print(f"Errore: il file di configurazione '{args.config}' non esiste.")
        return  
    with config_path.open("r") as f:
        config = yaml.safe_load(f)
    
    output_dir = pathlib.Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    main_tf_content = render_main_tf(config)

    output_file = output_dir / "main.tf"
    output_file.write_text(main_tf_content)

    print(f"File Terraform generato in: {output_file}")

if __name__ == "__main__":
    main()
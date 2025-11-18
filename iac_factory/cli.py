import argparse
import pathlib

import yaml

from .generator_terraform import render_files


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="iac-factory-lite",
        description="Legge un file YAML e genera un piccolo progetto Terraform (LITE).",
    )
    parser.add_argument(
        "config",
        help="Percorso al file di configurazione YAML (es: examples/sample-s3.yaml)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="out",
        help="Directory di output per i file Terraform (default: out)",
    )

    args = parser.parse_args()

    config_path = pathlib.Path(args.config)
    if not config_path.exists():
        raise SystemExit(f"[ERRORE] File YAML non trovato: {config_path}")

    with config_path.open() as f:
        config = yaml.safe_load(f)

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = render_files(config)

    for filename, content in files.items():
        target = output_dir / filename
        target.write_text(content)
        print(f"[OK] Generato {target}")

    print(f"\n[OK] Progetto Terraform LITE generato in: {output_dir}")


if __name__ == "__main__":
    main()

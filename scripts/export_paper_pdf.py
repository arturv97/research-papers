#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path
import tempfile


ENGINES = ["tectonic", "wkhtmltopdf", "pdflatex"]


def extract_title_and_body(input_file: Path):
    lines = input_file.read_text(encoding="utf-8").splitlines()

    title = None
    body_lines = []

    for i, line in enumerate(lines):
        if title is None and line.startswith("# "):
            title = line[2:].strip()
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()

    return title, body


def run_pandoc(input_file: Path, output_file: Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    title, body = extract_title_and_body(input_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
        tmp.write(body.encode("utf-8"))
        tmp_path = tmp.name

    for engine in ENGINES:
        try:
            cmd = [
                "pandoc",
                tmp_path,
                "-o",
                str(output_file),
                f"--pdf-engine={engine}",
                "--toc",
                "--number-sections",
                "-V", "geometry:margin=1in"
            ]

            if title:
                cmd.extend(["--metadata", f"title={title}"])

            subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            print(f"[OK] {input_file} -> {output_file} (engine: {engine})")
            return

        except subprocess.CalledProcessError:
            continue

    print(f"[ERROR] Failed to convert {input_file} with all engines")


def collect_files_from_pattern(pattern: str):
    return [Path(p) for p in Path().glob(pattern) if p.is_file() and p.suffix == ".md"]


def collect_files_from_directory(directory: Path):
    return list(directory.rglob("*.md"))


def compute_output_path(input_file: Path):
    parts = input_file.parts

    if "papers" not in parts:
        raise ValueError(f"'papers' not found in path: {input_file}")

    idx = parts.index("papers")
    relative_parts = parts[idx + 1:]

    output_path = Path("output").joinpath(*relative_parts)
    return output_path.with_suffix(".pdf")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  export_pdf.py <file.md>")
        print("  export_pdf.py <folder>")
        print("  export_pdf.py <pattern*>")
        sys.exit(1)

    arg = sys.argv[1]
    input_path = Path(arg)

    files = []

    if input_path.is_file():
        files = [input_path]
    elif input_path.is_dir():
        files = collect_files_from_directory(input_path)
    else:
        files = collect_files_from_pattern(arg)

    if not files:
        print("No markdown files found.")
        sys.exit(1)

    for file in files:
        try:
            output_file = compute_output_path(file)
            run_pandoc(file, output_file)
        except Exception as e:
            print(f"[ERROR] {file}: {e}")


if __name__ == "__main__":
    main()
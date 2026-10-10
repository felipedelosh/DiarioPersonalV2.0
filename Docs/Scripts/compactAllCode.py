"""
FelipedelosH
2026

Recorre todo el proyecto y concatena el contenido de todos los .py
en un único archivo all_code.txt.
"""
from pathlib import Path

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "all_code.txt"
EXTENSIONS = {".py"}

SKIP_DIRS = {
    "__pycache__", ".git", ".idea", ".vscode",
    "venv", ".venv", "env", "node_modules",
    "build", "dist", ".pytest_cache", ".mypy_cache",
}
SKIP_FILES = {"all_code.txt"}


# ------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------
def _is_inside_skipped_dir(path: Path, root: Path) -> bool:
    try:
        relatives = path.relative_to(root).parts[:-1]  # dirs, sin el nombre del archivo
    except ValueError:
        return True
    return any(part in SKIP_DIRS for part in relatives)


def collect_py_files(root: Path) -> list[Path]:
    files: list[Path] = []
    self_path = Path(__file__).resolve()

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if path.name in SKIP_FILES:
            continue
        if path.resolve() == self_path:
            continue
        if _is_inside_skipped_dir(path, root):
            continue
        files.append(path)

    # Orden determinista y legible
    files.sort(key=lambda p: str(p.relative_to(root)).lower())
    return files


def build_output(root: Path, files: list[Path]) -> str:
    separator = "=" * 78
    chunks: list[str] = []

    for path in files:
        relative = path.relative_to(root)
        chunks.append(separator)
        chunks.append(f"# {relative}")
        chunks.append(separator)
        chunks.append("")  # línea en blanco antes del código

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = path.read_text(encoding="latin-1")

        chunks.append(content.rstrip("\n"))
        chunks.append("")
        chunks.append("")

    return "\n".join(chunks)


# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
def main():
    files = collect_py_files(ROOT)

    if not files:
        print("No se encontraron archivos .py")
        return

    text = build_output(ROOT, files)
    OUTPUT.write_text(text, encoding="utf-8")

    total_bytes = sum(p.stat().st_size for p in files)
    print(f"OK: {len(files)} archivos, {total_bytes:,} bytes -> {OUTPUT}")
    for path in files:
        print(f"  - {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

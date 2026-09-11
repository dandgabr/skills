#!/usr/bin/env python3
"""Validates the harness/ directory, mirroring scripts/validate_skills.py.

Checks:
1. harness/README.md exists.
2. Each harness subfolder (excluding _template and shared) has a HARNESS.md with valid frontmatter (name, description, harness) and at least one *.example file.
3. No absolute machine-specific paths (/home/, /Users/, ~) in tracked harness files.
4. No inline secrets in harness/**/*.example tracked files.
5. .agents/harness.json lists only existing paths.
"""
import json
import os
import re
import sys

SECRET_PATTERNS = [
    re.compile(r"\b(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35})\b"),
    re.compile(r"(\beyJhbGciOi\b)"),  # JWT
    re.compile(r"(-----BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY-----)"),
]

PATH_PATTERNS = [
    re.compile(r"/home/"),
    re.compile(r"/Users/"),
    re.compile(r"(?<![\w])~(?!/|[\w])"),
]


def validate():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    harness_dir = os.path.join(base_dir, "harness")
    errors = []
    warnings = []

    # 1. harness/README.md
    readme = os.path.join(harness_dir, "README.md")
    if not os.path.exists(readme):
        errors.append("harness/README.md não encontrado.")

    if not os.path.exists(harness_dir):
        errors.append("Diretório 'harness' não encontrado.")
        return _report(errors, warnings)

    # 2. Per-harness subfolders
    for entry in sorted(os.listdir(harness_dir)):
        sub = os.path.join(harness_dir, entry)
        if not os.path.isdir(sub) or entry.startswith("_") or entry == "shared":
            continue

        harness_md = os.path.join(sub, "HARNESS.md")
        if not os.path.exists(harness_md):
            errors.append(f"harness/{entry}/HARNESS.md ausente.")
            continue

        content = open(harness_md, encoding="utf-8").read()
        fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not fm:
            errors.append(f"harness/{entry}/HARNESS.md sem frontmatter YAML.")
        else:
            for field in ("name", "description", "harness"):
                if not re.search(rf"^{field}:", fm.group(1), re.MULTILINE):
                    errors.append(
                        f"harness/{entry}/HARNESS.md campo '{field}' obrigatório no frontmatter.")

        # at least one .example file
        examples = [f for f in os.listdir(sub) if f.endswith(".example")]
        if not examples:
            warnings.append(f"harness/{entry}/ sem nenhum arquivo .example.")

    # 3 & 4: scan tracked files for absolute paths and secrets
    if os.path.exists(os.path.join(base_dir, ".git")):
        pass

    for root, _dirs, files in os.walk(harness_dir):
        for fname in files:
            fpath = os.path.join(root, fname)
            if not (fname.endswith(".example") or fname.endswith(".template.json")
                    or fname.endswith(".schema.json") or fname in ("HARNESS.md", "README.md")):
                continue
            text = open(fpath, encoding="utf-8").read()
            for pat in PATH_PATTERNS:
                if pat.search(text):
                    errors.append(
                        f"harness/{os.path.relpath(fpath, harness_dir)}: caminho absoluto detectado ({pat.pattern}).")
            for pat in SECRET_PATTERNS:
                if pat.search(text):
                    errors.append(
                        f"harness/{os.path.relpath(fpath, harness_dir)}: possível segredo inline ({pat.pattern}).")

    # 5. .agents/harness.json
    discovery = os.path.join(base_dir, ".agents", "harness.json")
    if os.path.exists(discovery):
        try:
            data = json.load(open(discovery, encoding="utf-8"))
            for ent in data.get("entries", []):
                p = ent.get("path", "")
                resolved = os.path.normpath(os.path.join(base_dir, p))
                if not os.path.exists(resolved):
                    errors.append(f".agents/harness.json: caminho não existe: '{p}'.")
        except Exception as e:
            errors.append(f"Erro ao analisar .agents/harness.json: {e}")
    else:
        warnings.append(".agents/harness.json não encontrado.")

    return _report(errors, warnings)


def _report(errors, warnings):
    print("--- RELATÓRIO DE VALIDAÇÃO (harness) ---")
    print(f"Total de Erros: {len(errors)}")
    print(f"Total de Avisos: {len(warnings)}")
    for e in errors:
        print(f"[ERRO] {e}")
    for w in warnings:
        print(f"[AVISO] {w}")
    if errors:
        print("FALHA: corrija os erros acima.")
    else:
        print("OK: estrutura 'harness' validada.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(validate())

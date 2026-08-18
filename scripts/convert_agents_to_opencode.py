#!/usr/bin/env python3
"""
Conversor de Agentes ADK 2.0 para Agentes do opencode
------------------------------------------------------
Gera, a partir dos arquivos `agents/<nome>/agent.yaml` (especificação ADK 2.0),
arquivos de agente do opencode (`<nome>.md` com frontmatter) no diretório global
de agentes `~/.config/opencode/agent/`.

O opencode não lê o formato YAML do ADK nem pastas de agentes arbitrárias, então
este script traduz cada agente para o formato `.md` que o opencode carrega em
qualquer instância nova.

Uso:
    python scripts/convert_agents_to_opencode.py                 # converte para o diretório global
    python scripts/convert_agents_to_opencode.py --target <dir>  # converte para outro diretório
    python scripts/convert_agents_to_opencode.py --dry-run       # apenas mostra o que seria gerado
"""

import sys
import re
import argparse
import pathlib

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
AGENTS_SRC = BASE_DIR / "agents"
DEFAULT_TARGET = pathlib.Path.home() / ".config" / "opencode" / "agent"

MODE = "subagent"

# Regex que extrai o nome da skill a partir de caminhos relativos do ADK,
# ex.: ../../skills/security/appsec/sast-code-review/SKILL.md -> sast-code-review
SKILL_PATH_RE = re.compile(r"(?:\.\./)+skills/[^\s]+/SKILL\.md")


def parse_agent_yaml(text: str) -> dict:
    """Extrai name, description e instruction de um agent.yaml simples."""
    name_match = re.search(r"^name:\s*(.+?)$", text, re.M)
    if not name_match:
        raise ValueError("campo 'name' não encontrado")
    description_match = re.search(r"^description:\s*(.+?)$", text, re.M)
    if not description_match:
        raise ValueError("campo 'description' não encontrado")
    instruction_match = re.search(r"^instruction:\s*>\s*\n((?:.*\n)+?)(?=^tools:)", text, re.M)
    if not instruction_match:
        raise ValueError("campo 'instruction' (block scalar) não encontrado")

    raw_lines = instruction_match.group(1).rstrip("\n").split("\n")
    instruction = "\n".join(re.sub(r"^\s{2}", "", line) for line in raw_lines).strip()

    return {
        "name": name_match.group(1).strip(),
        "description": description_match.group(1).strip(),
        "instruction": instruction,
    }


def skill_name_from_path(path: str) -> str:
    """Extrai o nome da skill de um caminho ADK (ex.: sast-code-review)."""
    return path.strip().rstrip("/").rsplit("/", 2)[-2]


def normalize_skill_paths(instruction: str) -> str:
    """Substitui caminhos relativos do ADK pelo nome da skill referenciada."""
    return SKILL_PATH_RE.sub(lambda m: skill_name_from_path(m.group(0)), instruction)


def polish_instruction(name: str, instruction: str) -> str:
    """Ajustes pontuais de redação após a normalização de caminhos."""
    if name == "documenter":
        instruction = instruction.replace(
            'da skill "documentation-designer" localizada em documentation-designer',
            "da skill documentation-designer",
        )
    if name == "software-architect":
        instruction = instruction.replace(
            "contidas em software-architect",
            "contidas na skill software-architect",
        )
    return instruction


def build_agent_markdown(agent: dict) -> str:
    """Monta o conteúdo do arquivo .md no formato de agente do opencode."""
    instruction = polish_instruction(
        agent["name"], normalize_skill_paths(agent["instruction"])
    )
    body = (
        "---\n"
        f"description: {agent['description']}\n"
        f"mode: {MODE}\n"
        "---\n\n"
        f"<!-- Generated from agents/{agent['name']}/agent.yaml (ADK 2.0) -->\n\n"
        f"{instruction}\n"
    )
    return body


def convert_agents(target: pathlib.Path, dry_run: bool) -> None:
    """Converte todos os agentes ADK do repositório para .md do opencode."""
    if not AGENTS_SRC.is_dir():
        sys.exit(f"ERRO: pasta de agentes não encontrada em {AGENTS_SRC}")

    yaml_files = sorted(AGENTS_SRC.glob("*/agent.yaml"))
    if not yaml_files:
        sys.exit(f"ERRO: nenhum agent.yaml encontrado em {AGENTS_SRC}")

    if dry_run:
        print(f"[dry-run] destino: {target}")
    else:
        target.mkdir(parents=True, exist_ok=True)

    generated = 0
    unchanged = 0
    to_generate = 0
    for yaml_path in yaml_files:
        agent = parse_agent_yaml(yaml_path.read_text(encoding="utf-8"))
        out_path = target / f"{agent['name']}.md"
        content = build_agent_markdown(agent)

        if out_path.exists() and out_path.read_text(encoding="utf-8") == content:
            unchanged += 1
            print(f"[ok] {out_path.name} (inalterado)")
            continue

        to_generate += 1
        if dry_run:
            print(f"[gerar] {out_path.name}")
        else:
            out_path.write_text(content, encoding="utf-8")
            generated += 1
            print(f"[ok] {out_path.name} (gerado)")

    if dry_run:
        print(f"\nResumo: {to_generate} a gerar, {unchanged} inalterados, "
              f"total {len(yaml_files)} agentes.")
    else:
        print(f"\nResumo: {generated} gerados, {unchanged} inalterados, "
              f"total {len(yaml_files)} agentes.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Converte agentes ADK 2.0 (agent.yaml) para agentes do opencode (.md)."
    )
    parser.add_argument(
        "--target",
        type=pathlib.Path,
        default=DEFAULT_TARGET,
        help=f"Diretório de saída (padrão: {DEFAULT_TARGET})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra o que seria gerado sem escrever arquivos",
    )
    args = parser.parse_args()
    convert_agents(args.target, args.dry_run)


if __name__ == "__main__":
    main()

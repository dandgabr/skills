import os
import re
import shutil
import json
import zipfile
from pathlib import Path

def export_all_skills():
    base_dir = Path("B:/Code/Skills")
    skills_dir = base_dir / "skills"
    export_dir = base_dir / "all_skills_export"
    export_skills_dir = export_dir / "skills"
    
    # 1. Limpar diretório de exportação existente
    if export_dir.exists():
        shutil.rmtree(export_dir)
    export_dir.mkdir(parents=True, exist_ok=True)
    export_skills_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Listar todas as skills reais
    all_skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    skill_names = [d.name for d in all_skill_dirs if (d / "SKILL.md").exists()]
    print(f"Encontradas {len(skill_names)} skills com SKILL.md")
    
    skills_metadata = {}
    yaml_regex = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    
    # 3. Ler metadados e conteúdo original
    for name in skill_names:
        src_folder = skills_dir / name
        skill_md_path = src_folder / "SKILL.md"
        
        content = skill_md_path.read_text(encoding="utf-8")
        
        # Parse frontmatter
        match = yaml_regex.match(content)
        metadata = {}
        if match:
            frontmatter_text = match.group(1)
            for line in frontmatter_text.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    metadata[k.strip()] = v.strip().strip('"').strip("'")
        
        skills_metadata[name] = {
            "id": name,
            "name": metadata.get("name", name),
            "description": metadata.get("description", ""),
            "original_content": content,
            "references": set()
        }

    # 4. Encontrar dependências/referências entre as skills
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for name, data in skills_metadata.items():
        content = data["original_content"]
        links = link_pattern.findall(content)
        for text, url in links:
            # Ignorar links externos
            if url.startswith(("http://", "https://", "mailto:", "git+")):
                continue
            
            # Verificar se aponta para alguma de nossas skills
            for possible_skill in skill_names:
                # Se o nome da skill está na URL do link
                if f"../{possible_skill}/" in url or f"/{possible_skill}/" in url or (possible_skill in url and "SKILL.md" in url):
                    if possible_skill != name: # Evitar auto-referência
                        data["references"].add(possible_skill)
                        break

    # Converter referências em lista ordenada
    for data in skills_metadata.values():
        data["references"] = sorted(list(data["references"]))

    # 5. Copiar pastas de skills e processar conteúdo
    for name, data in skills_metadata.items():
        dest_folder = export_skills_dir / name
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        # Garantir e copiar subpastas úteis
        for subfolder in ["examples", "references", "resources", "scripts"]:
            src_sub = skills_dir / name / subfolder
            dest_sub = dest_folder / subfolder
            dest_sub.mkdir(exist_ok=True)
            
            # Se a subpasta original existe e tem arquivos, copia eles
            if src_sub.exists():
                for item in src_sub.iterdir():
                    if item.is_file():
                        shutil.copy2(item, dest_sub)
            
            # Se a subpasta de destino ficou vazia, garante o .gitkeep para integridade
            if not list(dest_sub.glob("*")):
                (dest_sub / ".gitkeep").write_text("", encoding="utf-8")
                
        # Escrever o SKILL.md processado
        src_md = data["original_content"]
        
        # Se por acaso houver algum link absoluto do workspace, convertê-lo em relativo
        processed_md = re.sub(
            r"file:///[^)]*?/skills?/([^/)]+)/SKILL.md",
            r"../\1/SKILL.md",
            src_md
        )
        
        (dest_folder / "SKILL.md").write_text(processed_md, encoding="utf-8")
        print(f"Exportada skill: skills/{name}/SKILL.md")

    # 6. Copiar AGENTS.md e skills.json originais do workspace
    agents_src = base_dir / "AGENTS.md"
    if agents_src.exists():
        shutil.copy2(agents_src, export_dir / "AGENTS.md")
        print("Copiado AGENTS.md")
    else:
        # Fallback se não existir por algum motivo
        (export_dir / "AGENTS.md").write_text("# Regras e Diretrizes Gerais", encoding="utf-8")
        
    skills_json_src = base_dir / "skills.json"
    if skills_json_src.exists():
        shutil.copy2(skills_json_src, export_dir / "skills.json")
        print("Copiado skills.json")
    else:
        # Fallback
        default_skills_json = {
            "entries": [{"path": "skills/"}],
            "inherits": [],
            "exclude": []
        }
        with open(export_dir / "skills.json", "w", encoding="utf-8") as f:
            json.dump(default_skills_json, f, indent=2)

    # 7. Gerar manifest.json na raiz do export
    manifest = {
        "moduleName": "Antigravity Global Skills Bundle",
        "description": f"Pacote completo com todas as {len(skill_names)} skills de desenvolvimento, arquitetura e segurança com caminhos relativos.",
        "version": "1.0.0",
        "exportedAt": "2026-07-01T07:56:00-04:00",
        "skills": [
            {
                "id": s["id"],
                "name": s["name"],
                "description": s["description"],
                "path": f"skills/{s['id']}/SKILL.md",
                "references": s["references"]
            }
            for s in skills_metadata.values()
        ]
    }
    with open(export_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print("Gerado manifest.json")

    # 8. Gerar README.md com visualização do grafo
    # Vamos gerar o grafo Mermaid de forma limpa
    mermaid_lines = ["graph TD"]
    for name, data in skills_metadata.items():
        clean_name = data["name"].split(" (")[0]
        # Adicionar nó
        mermaid_lines.append(f'  {name}["{clean_name}"]')
        
    for name, data in skills_metadata.items():
        for ref in data["references"]:
            mermaid_lines.append(f"  {name} --> {ref}")
            
    mermaid_code = "\n".join(mermaid_lines)

    readme_content = f"""# Antigravity Global Skills Bundle

Este repositório contém uma estrutura exportável de **{len(skill_names)} habilidades (skills)**, abrangendo Engenharia de Software, Padrões de Projeto (Design Patterns do GoF), Metodologias Ágeis, Garantia de Qualidade (QA) e Cibersegurança.

A estrutura é 100% modular, compatível com a CLI do Antigravity (AGY), IDEs de desenvolvimento e ferramentas de documentação (Obsidian, Logseq, GitBook, etc.).

## 📊 Grafo de Relações entre as Skills (Mermaid)

```mermaid
{mermaid_code}
```

## 📂 Estrutura de Arquivos do Pacote

```text
skills_bundle/
├── AGENTS.md            # Regras gerais de estilo e comportamento do projeto
├── skills.json          # Manifesto de registro de caminhos de customização
├── manifest.json        # Metadados estruturados das skills e suas dependências
├── README.md            # Esta documentação de referência
└── skills/              # Pasta principal contendo todas as skills
    └── [nome-da-skill]/ # Diretório de cada skill individual
        ├── SKILL.md     # Instruções em Markdown (com frontmatter YAML)
        ├── examples/    # Pasta de exemplos
        ├── references/  # Documentação de referência
        ├── resources/   # Recursos de suporte
        └── scripts/     # Scripts de automação associados
```

## 🛠️ Habilidades Incluídas no Pacote

A tabela abaixo lista todas as habilidades presentes neste pacote:

| ID da Skill | Nome da Skill | Descrição |
|-------------|---------------|-----------|
"""
    for s in skills_metadata.values():
        readme_content += f"| `{s['id']}` | **{s['name']}** | {s['description']} |\n"

    readme_content += """
## 🚀 Como Importar e Usar

### 1. Na CLI do Antigravity ou Assistentes Compatíveis
Basta extrair o arquivo ZIP no diretório desejado.
Se você deseja que o assistente carregue estas habilidades globalmente ou no seu projeto atual:
- Adicione o caminho da pasta extraída ou da subpasta `skills/` no seu arquivo `skills.json` (seja global ou local do projeto).
- O arquivo `skills.json` incluído na raiz deste pacote já está configurado para ler todas as skills presentes na pasta `skills/`.

### 2. No Obsidian ou Logseq
- Extraia o ZIP e abra a pasta extraída como um novo **Vault**.
- Graças aos links relativos padronizados no formato `../[outra-skill]/SKILL.md`, todos os links funcionarão perfeitamente para navegação visual e análise do grafo de notas.
"""

    (export_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print("Gerado README.md")

    # 9. Criar arquivo ZIP
    zip_path = base_dir / "all_skills_export.zip"
    print(f"Iniciando compressão em {zip_path}...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(export_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(export_dir)
                zip_file.write(file_path, arcname)
                
    # 10. Limpar pasta temporária
    shutil.rmtree(export_dir)
    
    print(f"Sucesso! Todas as {len(skill_names)} skills foram exportadas para: {zip_path}")

if __name__ == "__main__":
    export_all_skills()

import os
import re
import json

def validate():
    base_dir = r"B:\Code\Skills"
    errors = []
    warnings = []
    
    # 1. Validar skills.json
    skills_json_path = os.path.join(base_dir, "skills.json")
    if not os.path.exists(skills_json_path):
        errors.append("skills.json não encontrado no root.")
    else:
        try:
            with open(skills_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "entries" not in data:
                errors.append("skills.json está sem o campo obrigatório 'entries'.")
        except Exception as e:
            errors.append(f"Erro ao analisar o JSON do skills.json: {e}")
            
    # 2. Validar existências das pastas de skills
    skills_dir = os.path.join(base_dir, "skills")
    validated_skills_count = 0
    checked_links_count = 0
    broken_links_count = 0
    
    if not os.path.exists(skills_dir):
        errors.append("Diretório 'skills' não encontrado.")
    else:
        skill_folders = [f for f in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, f))]
        
        # Regex para extrair frontmatter
        yaml_regex = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
        # Regex para capturar links no formato markdown [texto](url)
        link_regex = re.compile(r"\[[^\]]+\]\(([^)#\s]+)(?:#[^\s\)]*)?\)")

        for folder in skill_folders:
            folder_path = os.path.join(skills_dir, folder)
            skill_file = os.path.join(folder_path, "SKILL.md")
            
            # Validar arquivo principal
            if not os.path.exists(skill_file):
                errors.append(f"Skill '{folder}' não possui o arquivo obrigatório SKILL.md.")
                continue
                
            validated_skills_count += 1
            
            # Ler e validar frontmatter
            try:
                with open(skill_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                match = yaml_regex.match(content)
                if not match:
                    errors.append(f"Arquivo '{skill_file}' não contém frontmatter YAML válido cercado por '---'.")
                    continue
                    
                yaml_text = match.group(1)
                # Análise manual simples do YAML (name e description)
                yaml_data = {}
                for line in yaml_text.splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        yaml_data[k.strip()] = v.strip().strip('"').strip("'")
                        
                if "name" not in yaml_data:
                    errors.append(f"O frontmatter em '{skill_file}' está sem a chave obrigatória 'name'.")
                if "description" not in yaml_data:
                    errors.append(f"O frontmatter em '{skill_file}' está sem a chave obrigatória 'description'.")
                    
                # Validar estrutura de subdiretórios padrão
                for sub in ["scripts", "examples", "resources", "references"]:
                    sub_path = os.path.join(folder_path, sub)
                    if not os.path.exists(sub_path):
                        warnings.append(f"Subdiretório '{sub}' ausente na skill '{folder}'.")
                    elif not os.path.exists(os.path.join(sub_path, ".gitkeep")):
                        warnings.append(f"Arquivo .gitkeep ausente em '{sub_path}'.")
                        
                # Validar links locais contidos no SKILL.md
                links = link_regex.findall(content)
                for link in links:
                    if link.startswith(("http://", "https://", "mailto:", "git+")):
                        continue
                    checked_links_count += 1
                    if link.startswith("file:///"):
                        local_path = link.replace("file:///", "").replace("/", os.sep)
                    else:
                        local_path = os.path.normpath(os.path.join(os.path.dirname(skill_file), link.replace("/", os.sep)))
                    if not os.path.exists(local_path):
                        broken_links_count += 1
                        errors.append(f"Link quebrado em '{skill_file}': {link} (Caminho local correspondente: {local_path} não existe)")
                        
            except Exception as e:
                errors.append(f"Erro ao ler/validar '{skill_file}': {e}")
                
    # 3. Validar agentes (ADK 2.0 YAML Config)
    agents_dir = os.path.join(base_dir, "agents")
    validated_agents_count = 0
    
    if not os.path.exists(agents_dir):
        errors.append("Diretório 'agents' não encontrado.")
    else:
        agent_folders = [f for f in os.listdir(agents_dir) if os.path.isdir(os.path.join(agents_dir, f))]
        
        for folder in agent_folders:
            folder_path = os.path.join(agents_dir, folder)
            agent_file = os.path.join(folder_path, "agent.yaml")
            
            # Validar arquivo principal do agente
            if not os.path.exists(agent_file):
                errors.append(f"Agente '{folder}' não possui o arquivo obrigatório agent.yaml.")
                continue
                
            validated_agents_count += 1
            
            # Ler e analisar agent.yaml
            try:
                with open(agent_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                agent_data = {}
                current_key = None
                
                # Parsing manual simples de YAML multinível
                for line in lines:
                    stripped = line.strip()
                    if not stripped or stripped.startswith("#"):
                        continue
                    
                    if ":" in line and not stripped.startswith("-"):
                        k, v = line.split(":", 1)
                        k = k.strip()
                        v = v.strip()
                        agent_data[k] = v
                        current_key = k
                    elif stripped.startswith("-") and current_key == "tools":
                        # Identificar caminhos de skills registradas
                        if "path:" in stripped:
                            path_part = stripped.split("path:", 1)[1].strip().strip('"').strip("'")
                            # Validar se o arquivo de skill referenciado no agent.yaml existe
                            normalized_path = path_part.replace("/", os.sep)
                            if not os.path.isabs(normalized_path):
                                normalized_path = os.path.normpath(os.path.join(folder_path, normalized_path))
                            if not os.path.exists(normalized_path):
                                errors.append(f"Caminho de skill inválido no agent.yaml de '{folder}': {path_part}")
                
                # Checar campos obrigatórios do ADK 2.0
                for req in ["name", "model", "description", "instruction"]:
                    if req not in agent_data or not agent_data[req]:
                        errors.append(f"O arquivo '{agent_file}' está sem o campo obrigatório '{req}'.")
                        
            except Exception as e:
                errors.append(f"Erro ao ler/validar '{agent_file}': {e}")

    # 4. Validar links locais no README.md e AGENTS.md
    # Regex para capturar links no formato markdown [texto](url)
    link_regex = re.compile(r"\[[^\]]+\]\(([^)#\s]+)(?:#[^\s\)]*)?\)")
    for other_file in ["README.md", "AGENTS.md", "agents\\README.md"]:
        other_file_path = os.path.join(base_dir, other_file)
        if os.path.exists(other_file_path):
            try:
                with open(other_file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                links = link_regex.findall(content)
                for link in links:
                    if link.startswith(("http://", "https://", "mailto:", "git+")):
                        continue
                    checked_links_count += 1
                    if link.startswith("file:///"):
                        local_path = link.replace("file:///", "").replace("/", os.sep)
                    else:
                        local_path = os.path.normpath(os.path.join(os.path.dirname(other_file_path), link.replace("/", os.sep)))
                    if not os.path.exists(local_path):
                        broken_links_count += 1
                        errors.append(f"Link quebrado em '{other_file}': {link} (Caminho local correspondente: {local_path} não existe)")
            except Exception as e:
                errors.append(f"Erro ao ler '{other_file}': {e}")

    # Output final do Relatório
    print("--- RELATÓRIO DE VALIDAÇÃO ---")
    print(f"Total de Skills Validadas: {validated_skills_count}")
    print(f"Total de Agentes Validados: {validated_agents_count}")
    print(f"Total de Links Locais Checados: {checked_links_count}")
    print(f"Total de Links Quebrados: {broken_links_count}")
    print(f"Total de Erros Encontrados: {len(errors)}")
    print(f"Total de Avisos (Warnings) Encontrados: {len(warnings)}")
    print("------------------------------")
    
    if errors:
        print("\n[ERROS ENCONTRADOS]:")
        for err in errors:
            print(f"- {err}")
    else:
        print("\n[OK] Nenhum erro de estrutura, link quebrado ou configuração de agente foi detectado!")
        
    if warnings:
        print("\n[AVISOS / WARNINGS]:")
        for warn in warnings:
            print(f"- {warn}")
            
    return errors, warnings

if __name__ == "__main__":
    validate()

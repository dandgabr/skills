import os
import re

base_dir = r"B:\Code\skills"
skills_dir = os.path.join(base_dir, "skills")
folders = sorted(os.listdir(skills_dir))

yaml_regex = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

skills_info = []

for folder in folders:
    folder_path = os.path.join(skills_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    skill_file = os.path.join(folder_path, "SKILL.md")
    if not os.path.exists(skill_file):
        continue
        
    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        match = yaml_regex.match(content)
        if match:
            yaml_text = match.group(1)
            yaml_data = {}
            for line in yaml_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    yaml_data[k.strip()] = v.strip().strip('"').strip("'")
            
            skills_info.append({
                "folder": folder,
                "name": yaml_data.get("name", folder),
                "description": yaml_data.get("description", "")
            })
    except Exception as e:
        print(f"Error reading {folder}: {e}")

dp_skills = []
dev_skills = []
sec_skills = []
tech_skills = []
other_skills = []

for s in skills_info:
    folder = s["folder"]
    if folder.startswith("dp-"):
        dp_skills.append(s)
    elif folder.startswith("tech-"):
        tech_skills.append(s)
    elif folder in ["appsec-owasp-asvs", "pentester-owasp-wstg", "secops-incident-responder", "security-architect-sabsa", "security-grc-compliance", "security-manager-samm", "threat-modeler", "devsecops-engineer"]:
        sec_skills.append(s)
    elif folder in ["backend-developer", "frontend-developer", "qa-engineer", "scrum-master", "product-owner", "ui-ux-designer", "software-architect"]:
        dev_skills.append(s)
    else:
        other_skills.append(s)

output_file = os.path.join(base_dir, "scripts", "skills_list.md")
with open(output_file, "w", encoding="utf-8") as out:
    out.write("### 🛠️ Engenharia, Papéis e Desenvolvimento de Software\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in dev_skills:
        out.write(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🛡️ Segurança, DevSecOps e Conformidade\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in sec_skills:
        out.write(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 💻 Tecnologias e Linguagens\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in tech_skills:
        out.write(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🧩 Padrões de Projeto (Design Patterns - GoF)\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in dp_skills:
        out.write(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### ⚙️ Auxiliares e Templates\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in other_skills:
        out.write(f"| [`{s['folder']}`](skills/{s['folder']}/SKILL.md) | **{s['name']}** | {s['description']} |\n")

print("File written successfully!")

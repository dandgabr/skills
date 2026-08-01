import os
import re

base_dir = r"B:\Code\skills"
skills_dir = os.path.join(base_dir, "skills")

yaml_regex = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

skills_info = []

for root, dirs, files in os.walk(skills_dir):
    if "SKILL.md" in files:
        skill_file = os.path.join(root, "SKILL.md")
        folder = os.path.basename(root)
        rel_path = os.path.relpath(skill_file, base_dir).replace("\\", "/")
        
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
                    "rel_path": rel_path,
                    "name": yaml_data.get("name", folder),
                    "description": yaml_data.get("description", "")
                })
        except Exception as e:
            print(f"Error reading {skill_file}: {e}")

dp_skills = []
dev_skills = []
sec_skills = []
lang_skills = []
framework_skills = []
program_skills = []
other_skills = []

for s in sorted(skills_info, key=lambda x: x["name"]):
    name = s["name"]
    folder = s["folder"]
    if name.startswith("dp-") or folder.startswith("dp-"):
        dp_skills.append(s)
    elif name.startswith("lang-") or "languages" in s["rel_path"]:
        lang_skills.append(s)
    elif name.startswith("framework-") or "framework" in s["rel_path"]:
        framework_skills.append(s)
    elif name.startswith("program-") or "programs" in s["rel_path"]:
        program_skills.append(s)
    elif folder in ["appsec-owasp-asvs", "pentester-owasp-wstg", "pentester-owasp-api-security-2023", "secops-incident-responder", "security-architect-sabsa", "security-grc-compliance", "security-manager-samm", "threat-modeler", "devsecops-engineer", "security-champions", "security-privacy"]:
        sec_skills.append(s)
    elif folder in ["backend-developer", "frontend-developer", "qa-engineer", "scrum-master", "product-owner", "ui-ux-designer", "software-architect", "devops-engineer", "clean-code-reusability", "documentation-designer"]:
        dev_skills.append(s)
    else:
        other_skills.append(s)

output_file = os.path.join(base_dir, "scripts", "skills_list.md")
with open(output_file, "w", encoding="utf-8") as out:
    out.write("### 🛠️ Engenharia, Papéis e Desenvolvimento de Software\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in dev_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🛡️ Segurança, DevSecOps e Conformidade\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in sec_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🔤 Linguagens de Programação e Marcação (Languages)\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in lang_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🧱 Frameworks e Ferramentas (Framework)\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in framework_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🖥️ Programas e Softwares (Programs)\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in program_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### 🧩 Padrões de Projeto (Design Patterns - GoF)\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in dp_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

    out.write("\n### ⚙️ Auxiliares e Templates\n\n")
    out.write("| Skill / Caminho | Nome da Habilidade | Descrição / Caso de Uso |\n")
    out.write("| :--- | :--- | :--- |\n")
    for s in other_skills:
        out.write(f"| [`{s['name']}`]({s['rel_path']}) | **{s['name']}** | {s['description']} |\n")

print("File written successfully!")

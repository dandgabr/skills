import glob
import yaml
import os

def get_skill_info(path):
    with open(path) as f:
        content = f.read()
    parts = content.split('---')
    if len(parts) >= 3:
        try:
            frontmatter = yaml.safe_load(parts[1])
            name = frontmatter.get('name', os.path.basename(os.path.dirname(path)))
            desc = str(frontmatter.get('description', '')).strip().replace('\n', ' ')
            return name, desc
        except Exception:
            pass
    name = os.path.basename(os.path.dirname(path))
    return name, 'Descrição da skill.'

def make_table(skill_paths):
    lines = ['| Skill | Caminho | Descrição |', '| :--- | :--- | :--- |']
    for p in sorted(skill_paths):
        name, desc = get_skill_info(p)
        lines.append(f'| **{name}** | [`{p}`]({p}) | {desc} |')
    return '\n'.join(lines)

def make_agents_table():
    agents = sorted([d for d in os.listdir('agents') if os.path.isdir(os.path.join('agents', d))])
    lines = ['| # | Agente | Markdown (Universal) | YAML (ADK 2.0) | JSON (APIs) | Descrição e Especialidade |',
             '| :-: | :--- | :--- | :--- | :--- | :--- |']
    for i, a in enumerate(agents, 1):
        yaml_p = f'agents/{a}/agent.yaml'
        desc = ''
        if os.path.exists(yaml_p):
            with open(yaml_p) as f:
                y = yaml.safe_load(f)
                desc = str(y.get('description', '')).strip().replace('\n', ' ')
        lines.append(f'| {i} | **{a}** | [`AGENT.md`](agents/{a}/AGENT.md) | [`agent.yaml`](agents/{a}/agent.yaml) | [`agent.json`](agents/{a}/agent.json) | {desc} |')
    return '\n'.join(lines)

skills_roles = glob.glob('skills/roles/**/SKILL.md')
skills_eng = glob.glob('skills/engineering-practices/**/SKILL.md')
skills_patterns = glob.glob('skills/patterns/**/SKILL.md', recursive=True)
skills_framework = glob.glob('skills/framework/**/SKILL.md')
skills_lang = glob.glob('skills/languages/**/SKILL.md')
skills_db = glob.glob('skills/databases/**/SKILL.md')
skills_cloud = glob.glob('skills/cloud-infra/**/SKILL.md')
skills_map = glob.glob('skills/mapping/**/SKILL.md')

skills_sec_ai = glob.glob('skills/security/ai-security/**/SKILL.md')
skills_sec_app = glob.glob('skills/security/appsec/**/SKILL.md')
skills_sec_iam = glob.glob('skills/security/cloud-iam/**/SKILL.md')
skills_sec_crypto = glob.glob('skills/security/crypto-pki/**/SKILL.md')
skills_sec_grc = glob.glob('skills/security/grc-compliance/**/SKILL.md')
skills_sec_ops = glob.glob('skills/security/ops-architecture/**/SKILL.md')
total_sec = len(skills_sec_ai) + len(skills_sec_app) + len(skills_sec_iam) + len(skills_sec_crypto) + len(skills_sec_grc) + len(skills_sec_ops)

skills_prog = glob.glob('skills/programs/**/SKILL.md')
skills_dom = glob.glob('skills/domains/**/SKILL.md')

all_skills = sorted(glob.glob('skills/**/SKILL.md', recursive=True))
total_skills = len(all_skills)
total_agents = len([d for d in os.listdir('agents') if os.path.isdir(os.path.join('agents', d))])

content = f"""# 📚 Catálogo Central de Habilidades e Agentes Especializados

Este documento consolida o inventário canônico de todas as **{total_skills} Habilidades Especializadas (Skills)** e **{total_agents} Agentes Especializados Universais (Multi-Harness)** disponíveis neste repositório.

---

## 📊 Dashboard do Repositório

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ESTATÍSTICAS GERAIS DO ECOSSISTEMA                              │
├────────────────────────────────────────┬───────────────────────────────────────────────┤
│ 🤖 Agentes Especializados Universais   │ {total_agents:<45} │
│ 📚 Total de Skills de Produção         │ {total_skills:<45} │
│ 🎓 Domínios Acadêmicos & Engenharia    │ {len(skills_dom):<45} │
│ 🔒 Segurança da Informação & AppSec    │ {total_sec:<45} │
│ 💻 Linguagens & Frameworks             │ {len(skills_lang) + len(skills_framework):<45} │
│ 🗺️ Mapeamento, Cloud & Bancos de Dados │ {len(skills_map) + len(skills_cloud) + len(skills_db):<45} │
└────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 🤖 Agentes Especializados Universais ({total_agents})

{make_agents_table()}

---

## 🛠️ Papéis e Funções — Roles ({len(skills_roles)})

{make_table(skills_roles)}

---

## 📐 Práticas de Engenharia e Arquitetura ({len(skills_eng)})

{make_table(skills_eng)}

---

## 🧱 Padrões de Projeto — Design Patterns GoF ({len(skills_patterns)})

{make_table(skills_patterns)}

---

## 🌐 Frameworks, APIs e Bibliotecas ({len(skills_framework)})

{make_table(skills_framework)}

---

## 💻 Linguagens de Programação e Marcação ({len(skills_lang)})

{make_table(skills_lang)}

---

## 💾 Bancos de Dados e Streaming ({len(skills_db)})

{make_table(skills_db)}

---

## ☁️ Infraestrutura Cloud & Sistemas Operacionais ({len(skills_cloud)})

{make_table(skills_cloud)}

---

## 🗺️ Mapeamento, Descoberta e Observabilidade ({len(skills_map)})

{make_table(skills_map)}

---

## 🔒 Segurança da Informação e Cibersegurança ({total_sec})

### 🤖 Segurança de Inteligência Artificial ({len(skills_sec_ai)})
{make_table(skills_sec_ai)}

### 🛡️ Application Security & Offensive Red Teaming ({len(skills_sec_app)})
{make_table(skills_sec_app)}

### ☁️ Gestão de Acessos & Identidades Cloud IAM ({len(skills_sec_iam)})
{make_table(skills_sec_iam)}

### 🔑 Criptografia, PKI & PQC ({len(skills_sec_crypto)})
{make_table(skills_sec_crypto)}

### 📋 Governança, Riscos e Conformidade — GRC & Privacidade ({len(skills_sec_grc)})
{make_table(skills_sec_grc)}

### 🏗️ Arquitetura Operacional de Segurança & Resposta a Incidentes ({len(skills_sec_ops)})
{make_table(skills_sec_ops)}

---

## ⚙️ Programas, Ferramentas e Ecossistemas ({len(skills_prog)})

{make_table(skills_prog)}

---

## 🎓 Domínios Especializados & Ciências Exatas ({len(skills_dom)})

{make_table(skills_dom)}
"""

with open('CATALOGO.md', 'w') as f:
    f.write(content)

print('CATALOGO.md generated successfully!')

---
name: ai-llm-slm-security
description: "Atua como Especialista em Segurança, Governança, Red Teaming e Pentest de Modelos de Linguagem (LLMs e SLMs), cobrindo mitigação e exploração de Prompt Injection, Jailbreaking, envenenamento de dados (Data Poisoning), vazamento de modelo (Model Inversion), segurança de RAG e conformidade total com o OWASP Top 10 for LLM e OWASP AI Exchange."
---

# Segurança, Red Teaming e Governança de LLMs & SLMs

Esta skill fornece os princípios, heurísticas e metodologias tanto para a defesa (Blue Team / Governança) quanto para a auditoria ofensiva (Red Team / Pentest) de sistemas baseados em Inteligência Artificial Generativa e Large Language Models (LLMs).

---

## 🛡️ 1. Matriz de Ameaças: OWASP Top 10 for LLM

| ID | Vulnerabilidade | Descrição Técnica | Vetor de Teste & Mitigação |
| :--- | :--- | :--- | :--- |
| **LLM01** | **Prompt Injection** | Manipulação direta ou indireta de instruções contextuais. | Sanitização de inputs, delimitadores estritos (`### Instructions`) e LLM Guardrails (NeMo, Guardrails AI). |
| **LLM02** | **Insecure Output Handling** | Execução cega da saída do modelo pelo sistema host (XSS, SQLi, RCE). | Sanitização rigorosa e validação de schema antes da execução de tool calls. |
| **LLM03** | **Training Data Poisoning** | Inserção de dados maliciosos durante o pré-treinamento ou fine-tuning. | Validação criptográfica de procedência de dados e filtragem estatística de anomalias. |
| **LLM04** | **Model Denial of Service** | Sobrecarga de contexto ou recursão infinita de queries de alta latência. | Rate limiting, capping de tokens e timeouts em cadeias RAG. |
| **LLM05** | **Supply Chain Vulnerabilities** | Modelos pré-treinados adulterados, pacotes maliciosos ou dependências vulneráveis. | Varredura de checkpoints (`safetensors` em vez de `pickle`), SBOM e SCA. |
| **LLM06** | **Sensitive Information Disclosure** | Vazamento de PII, chaves de API ou segredos incorporados no treinamento ou RAG. | Anonimização diferencial, scrubbing de logs e controle de acesso baseado em roles (RBAC). |
| **LLM07** | **Insecure Plugin Design** | Plugins/Tools com privilégios excessivos sem validação humana (HITL). | Princípio do menor privilégio para ferramentas e confirmação explícita para ações de escrita. |
| **LLM08** | **Excessive Agency** | Concessão de autonomia desproporcional ao modelo para tomar decisões críticas. | Limitação de escopo e aprovação humana em transações financeiras/administrativas. |

---

## 🎯 2. Metodologia de Red Teaming e Testes Ofensivos

- **Prompt Injection Direto**: Técnicas de prefix injection, framing cognitivo e simulação de modos alternativos ("DAN", "Developer Mode").
- **Prompt Injection Indireto**: Injeção de instruções maliciosas em documentos indexados no banco vetorial de RAG ou páginas web raspadas pelo agente.
- **Model Inversion / Extraction**: Extração de dados de treinamento através de repetições estocásticas de tokens ou queries de predição de alta confiança.

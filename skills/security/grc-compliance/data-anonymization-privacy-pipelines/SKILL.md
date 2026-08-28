---
name: data-anonymization-privacy-pipelines
description: Especialista em Anonimização de Dados, Engenharia de Desidentificação e Modelos Formais de Privacidade baseado nas obras Building an Anonymization Pipeline e Anonymizing Health Data (Khaled El Emam). Cobre k-anonymity, l-diversity, t-closeness, Differential Privacy (Privacidade Diferencial), identificadores diretos vs quase-identificadores (QIDs) e conformidade técnica rigorosa com HIPAA, LGPD e GDPR.
---

# Anonimização de Dados e Pipelines de Desidentificação

Esta skill estabelece métodos estatísticos e algoritmos formais para transformar conjuntos de dados sensíveis (dados de saúde, financeiros, pessoais) em dados anonimizados irreversíveis, garantindo privacidade com utilidade analítica.

---

## 🔐 1. Modelos Formais de Anonimização

### A. $k$-Anonymity
- **Definição**: Um dataset atinge $k$-anonymity se cada tupla de quase-identificadores (ex: `Idade`, `CEP`, `Gênero`) for indistinguível de pelo menos $k - 1$ outros registros na mesma base.
- **Técnicas**: Generalização (ex: idade `28` -> faixa `20-30`) e Supressão de linhas que violam o limiar $k$.

### B. $l$-Diversity
- **Definição**: Além de $k$-anonymity, cada grupo de equivalência deve conter pelo menos $l$ valores bem representados para cada atributo sensível (ex: diagnóstico médico), prevenindo *Homogeneity Attacks*.

### C. $\epsilon$-Differential Privacy (Privacidade Diferencial)
- Adição controlada de ruído matemático (Laplace ou Gaussiano) ao resultado de consultas analíticas para garantir que a inclusão ou remoção de um único indivíduo não altere a probabilidade do resultado da query além de um fator $e^\epsilon$.

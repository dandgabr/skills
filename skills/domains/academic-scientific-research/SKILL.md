---
name: academic-scientific-research
description: "Especialista em Metodologia de Pesquisa Científica, Revisão Sistemática de Literatura (PRISMA 2020), Estruturação PICO/PECO, Avaliação PRESS, Busca em Bases Indexadas (PubMed/MeSH, arXiv, IEEE Xplore, Semantic Scholar, Scopus, SciELO) e Redes de Citação."
---

# Academic & Scientific Research Methodology

Esta skill estabelece o padrão metodológico e operacional para conduzir investigações científicas rigorosas, formulação de perguntas estruturadas, buscas sistemáticas em bases acadêmicas indexadas e síntese de evidências sem viés.

---

## 🔬 1. Metodologia de Formulação de Perguntas

Antes de disparar consultas a bases de dados, a questão de pesquisa deve ser decomposta em um framework conceitual validado:

### A. Framework PICO / PECO
- **P (Population / Problem)**: População, amostra, domínio, contexto clínico ou problema de engenharia em estudo.
- **I / E (Intervention / Exposure)**: Intervenção proposta, técnica algorítmica, tratamento, fármaco ou tecnologia investigada.
- **C (Comparison)**: Controle, baseline existente, estado da arte atual ou placebo (se aplicável).
- **O (Outcome)**: Desfechos medidos (ex.: acurácia, latência, redução de mortalidade, throughput, eficácia).
- **S (Study Design - PICOS)**: Tipos de estudos elegíveis (ensaios clínicos randomizados, revisões por pares, preprints, estudos empíricos).

---

## 📜 2. Protocolo de Revisão Sistemática (PRISMA 2020 & Cochrane)

### A. Fluxograma de 4 Fases (PRISMA Flow Diagram)
1. **Identificação (Identification)**:
   - Registro de todos os registros recuperados por base acadêmica e buscas complementares (grey literature).
   - Remoção de duplicatas automatizada ou assistida por DOI / PMID / arXiv ID.
2. **Triagem (Screening)**:
   - Leitura cega ou paralela de Títulos e Resumos (*Titles & Abstracts*) com critérios explícitos de inclusão/exclusão.
3. **Elegibilidade (Eligibility)**:
   - Obtenção do texto completo (*Full-Text*) e verificação detalhada das variáveis metodológicas.
4. **Inclusão (Inclusion)**:
   - Conjunto final de artigos submetidos à síntese qualitativa ou metanálise quantitativa.

### B. Diretrizes PRESS (Peer Review of Electronic Search Strategies)
- **Tradução Conceitual**: Assegurar que cada componente PICO tenha sinônimos completos (termos livres e termos controlados).
- **Vocabulários Controlados**: Uso obrigatório de **MeSH** (Medical Subject Headings) no PubMed, **DeCS** na BVS/SciELO e **ACM/IEEE Taxonomy** em computação.
- **Operadores Booleanos Rígidos**:
  - `OR` intra-conceito (sinônimos e variantes ortográficas).
  - `AND` inter-conceito (combinação das dimensões do PICO).
  - Uso parcimonioso de `NOT` para evitar exclusão inadvertida de estudos relevantes.

---

## 📚 3. Estratégias por Base Científica e Indexadores

| Base de Dados | Domínio Primário | Sintaxe e Recursos Chave |
| :--- | :--- | :--- |
| **PubMed / MEDLINE** | Medicina, Biologia, Saúde | `("termo"[MeSH Terms] OR "termo"[Title/Abstract]) AND ...` |
| **arXiv.org** | Computação, Física, Matemática | Filtros por categoria (`cat:cs.AI`, `cat:stat.ML`), busca de preprints imediatos. |
| **Semantic Scholar** | Multidisciplinar / IA | Grafos de citações influentes (*Highly Influential Citations*), TLDRs e extração semântica. |
| **IEEE Xplore** | Engenharia Elétrica, Computação | `("Document Title":termo AND "Abstract":termo)`, foco em padrões e conferências IEEE. |
| **Google Scholar** | Descoberta ampla (secundária) | Rastreamento de citações reversas (*cited by*), autores canônicos e métricas h5. |
| **SciELO & BVS** | América Latina, Lusofonia | Artigos em Português/Espanhol, descritores DeCS bilíngues. |

---

## 🔗 4. Análise de Redes de Citação e Snowballing

1. **Forward Snowballing (Citações Posteriores)**:
   - Identificar quais artigos recentes citaram o paper seminal/fundacional para acompanhar a evolução do estado da arte.
2. **Backward Snowballing (Referências Anteriores)**:
   - Inspecionar a bibliografia dos artigos chave selecionados para resgatar estudos primários pioneiros.
3. **Identificação de Co-citação e Acoplamento Bibliográfico**:
   - Detectar clusters temáticos e consensos consolidados vs. controvérsias na literatura científica.

---

## 📝 5. Diretrizes de Síntese de Evidências

Ao estruturar relatórios acadêmicos e revisões:
- Apresentar Tabela de Características dos Estudos (Autor, Ano, Amostra/Dataset, Metodologia, Principais Métricas e Limitações).
- Relatar explicitamente os vieses potenciais (Risk of Bias) e nível de evidência (ex.: GRADE).
- Fornecer citações formais completas (DOI, periódico, volume/número e autores).

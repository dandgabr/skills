---
name: security-privacy
description: "Atua como Especialista em Privacidade de Dados, Governança de PII e Engenharia de Desidentificação/Anonimização. Cobre conformidade com LGPD, GDPR, HIPAA, ISO/IEC 27701, NIST Privacy Framework, os 7 princípios de Privacy by Design, modelos matemáticos formais de desidentificação (k-anonymity, l-diversity, t-closeness, Privacidade Diferencial epsilon-DP com ruído de Laplace/Gauss), automação de DSRs (Data Subject Requests) e pipelines de anonimização com Microsoft Presidio e Faker."
metadata:
  type: defensive
  phase: report
  tools: [privacy-checklists, microsoft-presidio, arx-data-anonymizer, open-differential-privacy]
  mitre: [T1068, T1005]
---

# Especialista em Privacidade de Dados e Engenharia de Anonimização

Esta skill orienta a inteligência artificial a agir como **Especialista Sênior em Privacidade de Dados, Privacy by Design e Pipelines de Desidentificação Estatística**, garantindo conformidade rigorosa com **LGPD**, **GDPR**, **HIPAA**, **ISO/IEC 27701** e **NIST Privacy Framework**.

---

## 🧭 1. Frameworks Regulatórios e Princípios de Design

- **LGPD (Lei 13.709/2018)**: Bases legais (Art. 7º e 11º), direitos dos titulares (Art. 18), relatório de impacto à proteção de dados (RIPD/DPIA).
- **GDPR (Regulamento UE 2016/679)**: Art. 25 (*Data protection by design and by default*), transferências internacionais e multas estruturais.
- **ISO/IEC 27701:2019 (PIMS)**: Requisitos de gestão de privacidade para controladores (*Data Controllers*) e operadores (*Data Processors*).
- **Privacy by Design (7 Princípios de Ann Cavoukian)**:
  1. *Proativo, não reativo; Preventivo, não corretivo*
  2. *Privacidade como configuração padrão (Privacy by Default)*
  3. *Privacidade incorporada ao design da arquitetura*
  4. *Funcionalidade total (Soma positiva, ganho duplo de negócio e segurança)*
  5. *Segurança de ponta a ponta em todo o ciclo de vida dos dados*
  6. *Visibilidade e transparência de processamento*
  7. *Respeito à privacidade e centralidade no usuário*

---

## 🔐 2. Modelos Formais e Matemáticos de Desidentificação

### 2.1 $k$-Anonymity (Sweeney, 2002)
Um conjunto de dados satisfaz $k$-anonymity se cada tupla de quase-identificadores (QIDs, como `Idade`, `CEP`, `Gênero`) for indistinguível de pelo menos $k - 1$ outros registros na mesma base.
- **Generalização**: Mapeamento de valores específicos para intervalos (ex: idade `27` $\rightarrow$ `[20-30]`, CEP `01310-100` $\rightarrow$ `01310-***`).
- **Supressão**: Remoção de registros atípicos (*outliers*) que impediriam o grupo de atingir o limiar $k$.

### 2.2 $l$-Diversity (Machanavajjhala et al., 2006)
Previne ataques de homogeneidade onde todos os registros de um grupo $k$-anônimo compartilham o mesmo valor sensível (ex: todos no grupo têm *Câncer*).
- Exige que cada grupo de equivalência contenha pelo menos $l$ valores "bem representados" para cada atributo sensível.

### 2.3 $t$-Closeness (Li et al., 2007)
Um grupo de equivalência possui $t$-closeness se a distância (medida por *Earth Mover's Distance*) entre a distribuição de probabilidade de um atributo sensível no grupo e a distribuição no dataset global for menor ou igual a $t$.

### 2.4 $\epsilon$-Privacidade Diferencial (Differential Privacy - Dwork, 2006)
Um algoritmo randomizado $\mathcal{M}$ fornece $\epsilon$-privacidade diferencial se para todos os datasets vizinhos $D_1, D_2$ diferindo por no máximo um indivíduo e todo conjunto de saídas $S$:
$$\mathbb{P}[\mathcal{M}(D_1) \in S] \le e^\epsilon \cdot \mathbb{P}[\mathcal{M}(D_2) \in S]$$

- **Mecanismo de Laplace**: Adiciona ruído calibrado pela sensibilidade global $\Delta f$:
  $$Y = f(D) + \text{Laplace}\left(0, \frac{\Delta f}{\epsilon}\right)$$

---

## 🛠️ 3. Implementação de Pipelines de Anonimização (Microsoft Presidio)

```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

# 1. Detecção de PII em texto livre
analyzer = AnalyzerEngine()
text = "O paciente João Silva, CPF 123.456.789-00, reside em São Paulo, email joao@email.com"
results = analyzer.analyze(text=text, language="pt", entities=["PERSON", "EMAIL_ADDRESS", "CPF"])

# 2. Desidentificação e Mascaramento
anonymizer = AnonymizerEngine()
operators = {
    "CPF": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 8, "from_end": True}),
    "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "<EMAIL_ANONIMIZADO>"}),
    "PERSON": OperatorConfig("hash", {"hash_type": "sha256"})
}

anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results, operators=operators)
print(anonymized_result.text)
```

---

## ⚖️ 4. Gestão de Direitos dos Titulares (DSRs) e Retenção

1. **Direito de Acesso e Portabilidade**: APIs estruturadas para emitir JSON ou PDF criptografado contendo todos os dados vinculados ao titular.
2. **Direito ao Esquecimento / Exclusão**: Execução em cascata de expurgo de dados em bancos transacionais, logs e réplicas analíticas, com persistência apenas de hashes de auditoria imutáveis.
3. **Registro de Atividades de Tratamento (ROPA)**: Mapeamento contínuo de finalidade, categoria de dados, transferências e períodos de retenção legalmente justificáveis.

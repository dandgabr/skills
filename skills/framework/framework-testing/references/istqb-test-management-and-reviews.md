# 📋 Guia de Gestão de Testes, Revisões Estáticas e ISTQB

Este guia sintetiza as práticas de gestão, revisões estáticas, testes baseados em risco e métricas de qualidade consolidadas no corpo de conhecimento ISTQB/ISEB, baseadas em **Brian Hambling et al.** (*Software Testing: An ISEB/ISTQB Foundation Guide*).

---

## 1. Os 7 Princípios Fundamentais de Testes de Software (ISTQB)

1. **Testes demonstram a presença de defeitos, não a sua ausência**: Testar reduz a probabilidade de defeitos remanescentes, mas não prova a correção matemática absoluta do software.
2. **Testes exaustivos são impossíveis**: Testar todas as combinações de entradas e pré-condições é inviável; deve-se aplicar análise de risco, valores limites e partições de equivalência.
3. **Teste antecipado (Early Testing / Shift-Left)**: Atividades de teste devem iniciar nas fases iniciais do ciclo de vida (requisitos, arquitetura) para evitar a propagação exponencial do custo de correção.
4. **Agrupamento de defeitos (Defect Clustering)**: Uma pequena fração de módulos contém a maioria dos defeitos descobertos (Princípio de Pareto: ~80% dos defeitos concentrados em ~20% do código).
5. **Paradoxo do Pesticida (Pesticide Paradox)**: Executar repetidamente a mesma suíte de testes sem alterações faz com que ela perca a capacidade de encontrar novos defeitos; os casos de teste devem ser continuamente revisados e evoluídos.
6. **Teste depende do contexto**: Testar um sistema financeiro ou de controle de tráfego aéreo requer abordagens substancialmente mais rigorosas que um blog ou e-commerce estático.
7. **A falácia da ausência de erros (Absence-of-Errors Fallacy)**: Encontrar e corrigir defeitos não garante o sucesso se o sistema construído não atender às reais necessidades e expectativas dos usuários finais.

---

## 2. Técnicas Estáticas de Teste (Static Testing)

O teste estático examina artefatos de software (requisitos, diagramas, código-fonte) **sem executar o código**.

### 2.1. Níveis de Formalidade nas Revisões Humanas

```
[ Informal ] ────► [ Walkthrough ] ────► [ Revisão Técnica ] ────► [ Inspeção Formal ]
  (Sem atas)      (Conduzido pelo autor)    (Especialistas/Pares)     (Fagan - Papéis e métricas)
```

| Tipo de Revisão | Formalidade | Conduzido Por | Foco Principal | Métricas Coletadas |
| :--- | :--- | :--- | :--- | :--- |
| **Revisão Informal** | Baixa | Qualquer par | Verificação rápida em duas vias (pair review) | Não |
| **Walkthrough** | Média | Autor do artefato | Treinamento, alinhamento de entendimento e coleta de ideias | Opcional |
| **Revisão Técnica** | Alta | Revisor Líder / Moderador | Conformidade com padrões técnicos e arquitetura | Sim |
| **Inspeção (Fagan)** | Muito Alta | Moderador treinado independente | Detecção sistemática de defeitos usando checklists estritos | Sim (taxa de leitura, densidade de defeitos/página) |

### 2.2. Papéis em uma Inspeção Formal
- **Autor**: Criador do artefato sob revisão.
- **Moderador (Facilitador)**: Conduz a inspeção, gerencia o tempo e garante que o processo seja seguido.
- **Escriba (Relator)**: Registra cada defeito identificado e ações acordadas.
- **Revisores (Inspetores)**: Especialistas que examinam detalhadamente o documento antes da reunião.
- **Gerente**: Garante alocação de tempo e recursos, mas não interfere tecnicamente nas decisões.

---

## 3. Teste Baseado em Risco (Risk-Based Testing - RBT)

O RBT direciona o esforço, tempo e orçamento de teste para as áreas do sistema com maior probabilidade de falha e maior impacto ao negócio.

### 3.1. Matriz de Avaliação de Risco

$$Nível\ de\ Risco = Probabilidade\ (Likelihood) \times Impacto\ no\ Negócio\ (Impact)$$

```
Alto     │   MÉDIO    │    ALTO    │  CRÍTICO   │
         │  (Testar)  │ (Prioridade)│(Extensivo) │
Impacto  ├────────────┼────────────┼────────────┤
Médio    │   BAIXO    │   MÉDIO    │    ALTO    │
         │(Amostragem)│  (Testar)  │ (Prioridade)│
         ├────────────┼────────────┼────────────┤
Baixo    │   MÍNIMO   │   BAIXO    │   MÉDIO    │
         │(Se houver  │(Amostragem)│  (Testar)  │
         │  tempo)    │            │            │
         └────────────┴────────────┴────────────┘
             Baixa        Média        Alta
                     Probabilidade
```

### 3.2. Aplicação Prática do RBT
1. **Priorização de Execução**: Casos de teste de risco Crítico e Alto são executados primeiro e com múltiplos métodos (BVA Worst-case, MC/DC).
2. **Critérios de Parada (Exit Criteria)**: O release só é autorizado quando $100\%$ dos testes de risco Alto/Crítico passarem e o risco residual for aceitável.

---

## 4. Métricas de Qualidade e Eficácia de Testes

### 4.1. Eficácia de Remoção de Defeitos (Defect Removal Efficiency - DRE)
Mede a porcentagem de defeitos eliminados antes do release para produção:

$$DRE = \frac{D_{interno}}{D_{interno} + D_{producao}} \times 100\%$$

Onde:
- $D_{interno}$: Defeitos descobertos e corrigidos durante as fases de desenvolvimento e testes.
- $D_{producao}$: Defeitos reportados por usuários após o release.
- *Meta de Excelência*: $DRE \ge 95\%$.

### 4.2. Densidade de Defeitos (Defect Density)
$$Densidade = \frac{\text{Total de Defeitos}}{\text{Tamanho do Software (KLOC ou Pontos de Função)}}$$

Permite identificar componentes anormalmente propensos a falhas no repositório.

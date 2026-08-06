# Guia Completo da Matriz SABSA 6x6 e Perfil de Atributos de Negócio (BAP)

Este guia serve como documento de referência técnica para a aplicação rigorosa do framework **SABSA (Sherwood Applied Business Security Architecture)** no repositório.

---

## 📐 Matriz SABSA 6x6 (Visualização Completa)

A matriz SABSA cruza as 6 camadas de abstração arquitetural com os 6 aspectos fundamentais de qualquer sistema de informação:

| Camada \ Pergunta | **Assets (O quê)** | **Motivation (Por quê)** | **Process (Como)** | **People (Quem)** | **Location (Onde)** | **Time (Quando)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Contextual** *(Business)* | Objetivos do Negócio & Valor | Drivers do Negócio & Riscos | Processos de Negócio Principais | Atores do Negócio & Organização | Geografia & Mercados do Negócio | Calendário de Negócio & Janelas de Oportunidade |
| **2. Conceitual** *(Architect)* | Perfil de Atributos de Negócio (BAP) | Objetivos de Segurança do Negócio | Conceito de Engenharia de Segurança | Conceito de Confiança e Acessos | Conceito de Limites e Domínios | Conceito de Oportunidade de Tempo & Durabilidade |
| **3. Lógica** *(Designer)* | Modelos de Informação & Dados | Políticas de Segurança Lógicas | Serviços de Segurança & Fluxos Lógicos | Entidades e Atores Lógicos | Zonas de Confiança Lógicas & Redes | Cronograma Lógico & Sequenciamento |
| **4. Física** *(Builder)* | Servidores, Databases & Hardware | Mecanismos de Segurança Físicos | Aplicações, Middleware & Protocolos | Usuários Físicos & IDs em IdPs | Nós de Rede, Nuvem & IPs Físicos | Escalabilidade em Tempo Real & Performance |
| **5. Componente** *(Tradesman)* | Estruturas de Dados, Arquivos & Keys | Regras de Configuração de Segurança | Funções de Código, APIs & Scripts | Certificados, Chaves & Credenciais | Endereços de Memória & URIs | Temporizadores, Timeouts & Latências |
| **6. Operacional** *(Service Mgr)* | Ativos Operacionais & SIEM Logs | Métricas de Risco (KRI/KPI) | SOPs, Playbooks & Runbooks | Operadores, DevOps & SOC | Ambientes Produtivos & Disaster Recovery | Agendamentos, Janelas de Manutenção & SLAs |

---

## 📊 Taxonomia de Atributos de Negócio (BAP)

O **Perfil de Atributos de Negócio (BAP - Business Attribute Profile)** é o coração do SABSA. Ele traduz expectativas subjetivas de negócios em requisitos quantificáveis de segurança.

### Categorias Principais de Atributos:

1. **Atributos Financeiros**:
   - *Auditabilidade Transacional*: Rastreabilidade ponta a ponta sem desvio de saldos.
   - *Custo-Efetividade*: Retorno sobre investimento de segurança (ROSI) positivo.

2. **Atributos Operacionais**:
   - *Disponibilidade Ininterrupta*: Tolerância a falhas e alta resiliência (Ex: SLAs 99.99%).
   - *Escalabilidade Segura*: Suporte a picos de tráfego sem degradação do perfil de segurança.

3. **Atributos de Proteção e Privacidade**:
   - *Confidencialidade Estrita*: Proteção contra acesso não autorizado a dados pessoais/PHI.
   - *Integridade Inviolável*: Garantia de inexistência de modificação não autorizada.

4. **Atributos Regulatórios e de Conformidade**:
   - *Conformidade Legal*: Aderência total a LGPD, GDPR, PCI DSS e regulamentos do BCB/BACEN.
   - *Incontestabilidade (Non-Repudiation)*: Assinaturas digitais juridicamente válidas.

---

## 🔁 O Ciclo de Vida SABSA (SABSA Lifecycle)

1. **Strategy & Planning**:
   - Mapeamento dos objetivos de negócios e limites do sistema.
   - Construção inicial da camada Contextual.
2. **Design**:
   - Definição da Matriz Conceitual, Lógica, Física e de Componentes.
   - Criação dos Domínios de Segurança e Perfil de Atributos (BAP).
3. **Implement**:
   - Provisionamento de infraestrutura segura (IaC), código defensivo e testes AppSec/Pentesting.
4. **Manage & Measure**:
   - Operação contínua de segurança (SecOps), monitoramento de logs, resposta a incidentes e medição de KPIs/KRIs.

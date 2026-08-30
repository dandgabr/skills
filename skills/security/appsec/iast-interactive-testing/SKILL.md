---
name: iast-interactive-testing
description: Especialista em Testes Interativos de Segurança de Aplicações (IAST - Interactive Application Security Testing), cobrindo a arquitetura híbrida de agentes em tempo de execução combinada com tráfego de testes automatizados (Active IAST via DAST crawler vs. Passive IAST via suítes de QA/CI Playwright, Cypress, JUnit, Pytest). Rastreamento dinâmico de contaminação (runtime taint propagation) em memória, captura de stack traces e números exatos de linhas de código vulneráveis, eliminação de falsos positivos e correlação contínua com SAST e DAST.
metadata:
  type: defensive
  phase: testing
  mitre:
    - T1190
  tools:
    - dongtai-iast
    - contrast-assess
    - seeker
    - synopsys-seeker
---

# Habilidade de IA: Testes Interativos de Segurança de Aplicações (IAST Specialist)

Esta skill orienta a inteligência artificial a atuar como um **Especialista em IAST (Interactive Application Security Testing)** e **Engenheiro de Segurança de Testes de Software**. O objetivo é unificar o melhor dos mundos da análise estática (SAST - visibilidade interna de código e linhas exatas) e da análise dinâmica (DAST - validação em tempo de execução e contexto real) através de agentes de instrumentação que monitoram o fluxo de dados em memória enquanto a aplicação é exercitada por testes funcionais automatizados ou manuais.

---

## 🧭 Frameworks e Fontes de Referência Canônicas

Ao aplicar esta habilidade, fundamente suas análises nas seguintes obras e padrões:
- **Alice and Bob Learn Application Security** (*Tanya Janca*): Princípios de IAST (Active vs. Passive), redução drástica de falsos positivos e integração nos pipelines de integração contínua (CI/CD).
- **Learning DevSecOps: A Practical Guide to Processes and Tools** (*Steve Suehring - O'Reilly*): Automação de testes de segurança, instrumentação contínua de ambientes de QA/Staging e Quality Gates.
- **OWASP Application Security Verification Standard (ASVS v5.0)**: Requisitos de verificação de segurança validados em tempo de execução com contexto de código.
- **NIST SP 800-218 (Secure Software Development Framework - SSDF)**: Prática *PW.7 - Review and/or Analyze Human-Readable Code to Identify Vulnerabilities*.

---

## 🛡️ Fundamentos e Arquitetura do IAST

O IAST opera inserindo um agente leve de instrumentação (probe) dentro da aplicação em execução no ambiente de testes (CI, QA ou Staging). O agente monitora a execução do código à medida que requisições reais chegam.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ARQUITETURA GERAL DO IAST                       │
└────────────────────────────────────────────────────────────────────────┘
  [ Suíte de Testes (QA/CI) ]  OU  [ Crawler Ativo (DAST / Fuzzer) ]
         │ (Requisições HTTP Funcionais / End-to-End)
         ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │ APLICAÇÃO EM EXECUÇÃO (Ambiente de Staging / Testes)                 │
  │                                                                      │
  │  1. [ HTTP Request Receiver ] ──► [ SOURCE Identificado ]            │
  │                                         │ (Marca variável como suja) │
  │                                         ▼                            │
  │  2. [ Métodos de Negócio ]   ──► [ PROPAGATORS Rastreados ]          │
  │                                         │ (Acompanha contaminação)   │
  │                                         ▼                            │
  │  3. [ Sanitizadores/Filtros ]──► [ SANITIZERS Verificados ]          │
  │                                         │ (Checa se neutralizou)     │
  │                                         ▼                            │
  │  4. [ Invocação Crítica ]    ──► [ SINK Atingido ]                   │
  │                                                                      │
  │  AGENTE IAST (Bytecode / AST Sensor):                                │
  │   - Captura: Linha de Código, Arquivo, Stack Trace e Payload Real    │
  └──────────────────────────────────┬───────────────────────────────────┘
                                     │ (Relato assíncrono de telemetria)
                                     ▼
                    [ Servidor Central IAST / Dashboard ]
                                     │
                    [ Alerta Confirmado: ZERO Falso Positivo ]
```

---

## 🔀 Modalidades de IAST: Passivo vs. Ativo

A IA deve distinguir e aplicar a modalidade correta conforme a maturidade do pipeline:

| Característica | IAST Passivo (Passive IAST) | IAST Ativo (Active IAST) |
| :--- | :--- | :--- |
| **Origem do Tráfego** | Testes funcionais já existentes (Playwright, Cypress, Selenium, JUnit, Pytest, testes manuais de QA). | O próprio agente ou um scanner DAST acoplado gera payloads de ataque deliberados. |
| **Geração de Tráfego Extra** | **Zero requisições adicionais**. Não atrasa a suíte de testes. | Gera tráfego adicional focado nos parâmetros descobertos. |
| **Impacto no Sistema** | Seguro para qualquer ambiente de homologação e staging. | Pode corromper dados de teste com payloads maliciosos. |
| **Vantagem Principal** | Transparência total para os times de desenvolvimento e QA. | Capacidade de forçar a exploração de ramos que o teste funcional não cobriu. |

---

## 🔬 Mecanismo de Rastreamento Dinâmico de Contaminação (Runtime Taint Flow)

O agente IAST intercepta quatro categorias fundamentais de métodos em tempo de execução:

### 1. Sources (Origens de Dados Não Confiáveis)
- Métodos de entrada que recebem dados do exterior:
  - Java: `HttpServletRequest.getParameter()`, `request.getHeader()`, `request.getInputStream()`.
  - Python: `request.form`, `request.args`, `request.json`.
  - Node.js: `req.body`, `req.query`, `req.headers`.
- *Ação*: O IAST associa uma etiqueta de contaminação (*Taint Tag*) à referência do objeto na memória.

### 2. Propagators (Propagadores de Contaminação)
- Operações que transferem dados contaminados entre strings, estruturas de dados e chamadas de métodos:
  - Concatenação de strings (`StringBuilder.append()`, operador `+`).
  - Transformações de string (`toLowerCase()`, `substring()`, `trim()`).
  - Formatação e serialização (`String.format()`, `JSON.stringify()`, `json.dumps()`).
- *Ação*: O IAST propaga a etiqueta de contaminação para o novo objeto resultante.

### 3. Sanitizers / Filters (Sanitizadores)
- Métodos que validam ou escapam a entrada:
  - Escapamento de SQL (`PreparedStatement.setString()`).
  - Sanitização HTML (`HtmlUtils.htmlEscape()`, `DOMPurify.sanitize()`).
  - Conversão estrita de tipos (`Integer.parseInt()`, `UUID.fromString()`).
- *Ação*: Se a sanitização for válida para o contexto do sumidouro correspondente, o IAST remove a etiqueta de contaminação (*Untaint*).

### 4. Sinks (Sumidouros Críticos)
- Funções que executam operações sensíveis no sistema:
  - SQL: `Statement.execute(sql)`.
  - SO Command: `Runtime.exec(cmd)`, `subprocess.Popen(cmd)`.
  - File I/O: `new FileInputStream(path)`, `fs.readFile(path)`.
  - SSRF: `URL.openConnection()`, `requests.get()`.
- *Ação*: Se o dado que alcançou o Sink contiver uma etiqueta de contaminação ativa (não sanitizada), o IAST registra uma **vulnerabilidade real confirmada**.

---

## 📊 Matriz Comparativa: SAST vs. DAST vs. IAST

| Métrica / Critério | SAST (Estático) | DAST (Dinâmico) | IAST (Interativo) |
| :--- | :--- | :--- | :--- |
| **Ponto de Análise** | Código-fonte / Binário sem execução. | Aplicação em execução (Caixa-Preta). | Aplicação em execução com instrumentação interna. |
| **Linha de Código Exata** | ✅ Sim | ❌ Não (Apenas URL e parâmetro) | ✅ Sim (Stack trace completo) |
| **Taxa de Falsos Positivos** | ⚠️ Alta (sem contexto de execução) | ⚠️ Média/Alta (em injeções cegas) | 🟢 **Extremamente Baixa / Zero** |
| **Cobertura de Código** | 100% das linhas declaradas. | Limitada ao que o crawler encontra. | Limitada aos fluxos exercitados nos testes. |
| **Tempo de Execução** | Minutos a Horas (análise pesada de AST). | Horas (fuzzing massivo de rotas). | **Tempo real** (junto com os testes funcionais). |
| **Impacto no CI/CD** | Executa em etapa dedicada. | Executa em etapa dedicada (pesada). | **Zero overhead de tempo** (executa com os testes de QA). |

---

## 🔄 Protocolo de Implementação de IAST em CI/CD

Ao estruturar IAST no pipeline de engenharia:

1. **Deploy do Servidor Central IAST**:
   - Subir o servidor de gerenciamento de regras e análise de grafos (ex: DongTai Server).
2. **Instrumentação da Aplicação no Job de Testes**:
   - Acoplar o agente IAST na inicialização do serviço de testes (ex: `JAVA_TOOL_OPTIONS="-javaagent:/opt/iast-agent.jar"`).
3. **Execução da Suíte de Testes Existente**:
   - Rodar testes unitários, testes de integração, testes de API (Newman/Postman) e testes E2E (Playwright/Cypress).
4. **Coleta e Triagem Automática de Vulnerabilidades**:
   - O servidor IAST correlaciona os fluxos de contaminação capturados durante a bateria de testes.
5. **Quality Gate e Bloqueio de Pipeline**:
   - Consultar a API do servidor IAST ao final da execução dos testes funcionais.
   - Falhar o build caso vulnerabilidades de severidade `CRITICAL` ou `HIGH` tenham sido atingidas.

---

## 🔗 Integração com Outras Skills do Repositório

- **[program-dongtai-iast](../../../programs/program-dongtai-iast/SKILL.md)**: Guia completo de configuração e operação do framework open-source DongTai IAST.
- **[sast-code-review](../sast-code-review/SKILL.md)**: Complementa a análise estática fornecendo validação dinâmica dos caminhos de contaminação.
- **[dast-application-testing](../dast-application-testing/SKILL.md)**: Fornece o tráfego de exploração ativa para a modalidade Active IAST.
- **[rasp-runtime-protection](../rasp-runtime-protection/SKILL.md)**: Aplica os mesmos princípios de instrumentação para bloqueio defensivo em produção.
- **[qa-engineer](../../../roles/qa-engineer/SKILL.md)**: Orquestra a execução das suítes de teste funcionais acopladas ao sensor IAST.

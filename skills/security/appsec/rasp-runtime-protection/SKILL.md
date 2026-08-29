---
name: rasp-runtime-protection
description: Especialista em Proteção de Aplicações em Tempo de Execução (RASP - Runtime Application Self-Protection), cobrindo instrumentação de bytecode (Java Virtual Machine Tool Interface / Java Agent, .NET CLR Profiler API, extensões PHP Zend Engine, monkey-patching em Python e Node.js, e sondas eBPF em Go), monitoramento contextual de chamadas a sinks críticos (SQL drivers, execução de subprocessos, I/O de arquivos, deserialização de objetos, conexões de rede/SSRF), políticas de bloqueio (block mode) vs. monitoramento (log mode), fail-safe e minimização de overhead de performance.
metadata:
  type: defensive
  phase: operations
  mitre:
    - T1190
    - T1059
  tools:
    - openrasp
    - contrast-rasp
    - imperva-rasp
    - jvmti
    - ebpf
---

# Habilidade de IA: Proteção de Aplicações em Tempo de Execução (RASP Specialist)

Esta skill orienta a inteligência artificial a atuar como um **Especialista em RASP (Runtime Application Self-Protection)** e **Arquiteto de Segurança de Runtime**. O objetivo é projetar, implementar e gerenciar defesas ativas incorporadas diretamente dentro do ambiente de execução das aplicações (JVM, CLR, interpretadores PHP/Python/Node.js ou binários compilados), monitorando e interceptando chamadas internas a recursos sensíveis do sistema em tempo real para neutralizar ataques antes de sua execução no sistema operacional ou banco de dados.

---

## 🧭 Frameworks e Fontes de Referência Canônicas

Ao aplicar esta habilidade, fundamente suas análises e diretrizes nas seguintes obras e padrões:
- **Alice and Bob Learn Application Security** (*Tanya Janca*): Princípios de defesa em profundidade, segurança integrada ao runtime e comparação entre RASP, WAF e IAST.
- **Building Secure and Reliable Systems** (*Heather Adkins, Betsy Beyer, Paul Blankinship et al. - Google / O'Reilly*): Arquiteturas resilientes a falhas, isolamento de processos e contenção de privilégios em runtime.
- **NIST SP 800-53 Rev. 5**: Controles de integridade de software e proteção de execução (em especial *SI-7: Software, Firmware, and Information Integrity* e *SI-16: Memory Protection*).
- **OWASP Runtime Application Self-Protection Guidance**: Requisitos de instrumentação, cobertura de vetores de ataque e conformidade de telemetria.

---

## 🛡️ Fundamentos e Diferenciação Arquitetural do RASP

Diferente de um WAF (Web Application Firewall) que atua na borda da rede inspecionando pacotes HTTP puramente por casamento de assinaturas (sem conhecer a estrutura interna do código), o **RASP reside no mesmo espaço de memória do processo da aplicação**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ARQUITETURA DE UM AGENTE RASP                   │
└────────────────────────────────────────────────────────────────────────┘
  [ Requisição HTTP de Entrada ] ──► [ Servidor Web (Tomcat, Gunicorn, Express) ]
                                                │
                                                ▼
                                   [ Código da Aplicação (Lógica) ]
                                                │
  ┌─────────────────────────────────────────────┼─────────────────────────────────────────────┐
  │ AGENTE RASP (Instrumentação de Bytecode)     │                                             │
  │                                             ▼                                             │
  │   [ Hook Interceptor no Sink ] ──► (Ex: java.sql.Statement.executeQuery)                  │
  │          │                                                                                │
  │          ▼                                                                                │
  │   [ Análise Contextual & AST Taint Check ]                                                │
  │          │                                                                                │
  │          ├──► [ Ameaça Detectada? ]                                                       │
  │          │          ├── SIM (Block Mode) ──► Bloqueia execução + Lança SecurityException  │
  │          │          │                        + Emite Alarme Estruturado (JSON/SIEM)       │
  │          │          │                                                                     │
  │          │          └── NÃO (ou Log Mode) ─► Permite a invocação do Driver Real           │
  │          │                                                                                │
  └──────────┼────────────────────────────────────────────────────────────────────────────────┘
             ▼
     [ Recurso Real: Banco de Dados / Sistema de Arquivos / Shell do SO ]
```

### Vantagens do RASP em Relação a WAFs Perimetrais:
1. **Consciência de Contexto (Context-Awareness)**: O RASP sabe se uma string recebida na requisição HTTP chegou intacta até o driver de banco de dados ou se passou por sanitização/parametrização.
2. **Zero Falso Positivo em Tráfego Inócuo**: Se um invasor envia um payload `' OR '1'='1` para um campo de busca que é consultado via *Prepared Statement*, o RASP sabe que o comando não foi alterado estruturalmente e não bloqueia a requisição legítima.
3. **Visibilidade da Pilha de Execução (Call Stack)**: O RASP captura o stack trace completo no momento exato do ataque, apontando a classe, o método e a linha de código vulnerável.
4. **Proteção contra Vulnerabilidades de Dia Zero (0-Day)**: Bloqueia a ação danosa no sink final (ex: execução de `/bin/sh` ou leitura de `/etc/passwd`), independentemente de quão novo ou ofuscado seja o payload no HTTP.

---

## ⚙️ Mecanismos de Instrumentação por Ambiente de Runtime

A IA deve dominar as técnicas nativas de injeção de sondas (hooks) conforme a tecnologia do projeto:

### 1. Java / JVM
- **Java Agent (`-javaagent`)**: Utilização de `java.lang.instrument.Instrumentation` e `ClassFileTransformer`.
- **Manipulação de Bytecode**: Utilização de bibliotecas como ASM, ByteBuddy ou Javassist para injetar código nos métodos carregados pelo ClassLoader.
- **Sinks Críticos Interceptados**:
  - SQL: `java.sql.Statement`, `java.sql.PreparedStatement`.
  - Processos: `java.lang.ProcessBuilder.start()`, `java.lang.Runtime.exec()`.
  - Deserialização: `java.io.ObjectInputStream.resolveClass()`.
  - Arquivos: `java.io.FileInputStream.<init>`, `java.io.FileOutputStream.<init>`.
  - SSRF: `java.net.Socket.connect()`, `sun.net.www.protocol.http.HttpURLConnection.connect()`.

### 2. .NET / CLR (C#, VB.NET, F#)
- **CLR Profiling API**: Implementação de `ICorProfilerCallback` em C++ para interceptar compilações JIT (`JITCompilationStarted`) e reescrever instruções IL (Intermediate Language).
- **Sinks Críticos**: `System.Data.SqlClient.SqlCommand`, `System.Diagnostics.Process.Start`, `System.IO.FileStream`, `System.Runtime.Serialization.Formatters.Binary.BinaryFormatter`.

### 3. PHP / Zend Engine
- **Zend Extension (`zend_extension`)**: Compilação de módulo em C integrado ao Zend Engine (ex: `openrasp.so`).
- **Hooking de Funções Internas**: Sobrescrita dos ponteiros `zend_execute_ex` e `zend_compile_file`.
- **Sinks Críticos**: `mysqli_query`, `PDO::query`, `system()`, `exec()`, `passthru()`, `file_get_contents()`, `unserialize()`.

### 4. Python
- **Monkey Patching Dinâmico & `sys.settrace`**: Envolvimento de funções sensíveis da biblioteca padrão na inicialização do interpretador (`sitecustomize.py`).
- **Sinks Críticos**: `subprocess.Popen`, `os.system`, `eval()`, `exec()`, `sqlite3.Cursor.execute`, `pickle.loads`, `requests.api.request`.

### 5. Node.js / V8
- **Module Wrapping**: Interceptação de carregamento de módulos via monkey patching nos protótipos de `child_process`, `fs`, `http`, `net` e `vm`.
- **Sinks Críticos**: `child_process.exec()`, `child_process.spawn()`, `fs.readFile()`, `http.request()`, `vm.runInNewContext()`.

### 6. Linguagens Compiladas Nativas (Go, Rust, C/C++)
- **eBPF (Extended Berkeley Packet Filter) & Uprobes**: Injeção de sondas a nível de kernel nos símbolos de usuários (`uprobes` / `uretprobes`) sem recompilar a aplicação, monitorando syscalls (`sys_enter_execve`, `sys_enter_connect`, `sys_enter_openat`).

---

## 🎯 Modos de Operação e Resiliência (Fail-Safe)

A IA deve estruturar a governança de RASP em duas fases operacionais:

### 1. Modo de Auditoria / Monitoramento (Log/Alert Mode)
- Quando uma chamada a um sink sensível viola a política de segurança:
  1. A operação **não é abortada** (continua executando normalmente).
  2. Um log estruturado é emitido imediatamente com severidade `CRITICAL`/`ALERT`.
  3. Utilizado em ambientes de produção durante o período de calibração para garantir zero impacto na operação.

### 2. Modo de Bloqueio Ativo (Block Mode)
- Quando uma violação é detectada:
  1. A execução do método no sink é interrompida imediatamente.
  2. O agente lança uma exceção de segurança (`SecurityException` ou equivalente) ou força o retorno de um código de erro HTTP (ex: `403 Forbidden` / `400 Bad Request`).
  3. O payload não chega ao banco de dados ou ao kernel do sistema operacional.

### 3. Diretrizes de Resiliência e Desempenho (Non-Negotiable)
- **Overhead Máximo Permitido**: Menor que 3% em CPU e menor que 5% em latência HTTP.
- **Fail-Open por Padrão**: Caso ocorra uma exceção interna no próprio motor de análise do RASP, a requisição da aplicação deve continuar normalmente (fail-open), evitando que uma falha no agente cause Denial of Service (DoS) no serviço.
- **Logging Assíncrono**: O envio de alertas e telemetria para o SIEM deve ocorrer em thread assíncrona desacoplada da thread de requisição do usuário.

---

## 📋 Checklist de Implantação e Operação de RASP

1. **Seleção e Compatibilidade do Runtime**:
   - Mapear a versão exata do JDK/CLR/Python/PHP e garantir suporte do agente.
2. **Configuração de Políticas de Detecção**:
   - Habilitar regras contra SQLi, Command Injection, SSRF, Deserialização Insegura e Path Traversal.
   - Definir listas brancas (*allow-lists*) de comandos executáveis conhecidos e domínios de saída autorizados.
3. **Fase de Calibração (Staging & Canary em Log Mode)**:
   - Ativar o agente inicialmente em `log mode` em ambiente de testes ou canary deployment.
   - Analisar falsos alarmes causados por scripts de manutenção legítimos ou frameworks legados.
4. **Virada para Modo de Bloqueio (Block Mode)**:
   - Transicionar módulos críticos (ex: Command Injection e Deserialização) para `block mode`.
5. **Integração com SOC / SIEM**:
   - Exportar logs em JSON via syslog, Fluentd, Filebeat ou OpenTelemetry para centralização no Splunk, Elastic ou Graylog.

---

## 🔗 Integração com Outras Skills do Repositório

- **[program-openrasp](../../programs/program-openrasp/SKILL.md)**: Guia operacional completo da ferramenta open-source Baidu OpenRASP para Java e PHP.
- **[sast-code-review](../sast-code-review/SKILL.md)**: Correlação entre as regras estáticas de taint analysis e os pontos de hook do RASP.
- **[iast-interactive-testing](../iast-interactive-testing/SKILL.md)**: Aplicação dos mesmos princípios de instrumentação em ambiente de testes de QA.
- **[secops-incident-responder](../../ops-architecture/secops-incident-responder/SKILL.md)**: Consumo e automação de resposta a incidentes gerados por alertas do RASP em produção.

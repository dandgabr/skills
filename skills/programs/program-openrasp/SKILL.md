---
name: program-openrasp
description: Guia Definitivo e Padrões de Engenharia para Baidu OpenRASP (github.com/baidu/openrasp), cobrindo o framework open-source de Runtime Application Self-Protection (RASP), instalação de agentes Java e PHP, painel OpenRASP Cloud, desenvolvimento de plugins de detecção em JavaScript (motor V8), interceptação de SQLi, RCE, SSRF, Deserialização, e integração com SOC/SIEM.
metadata:
  type: defensive
  phase: operations
  mitre:
    - T1190
    - T1059
  tools:
    - openrasp
    - javaagent
    - zend-extension
---

# Habilidade de IA: Guia e Engenharia com Baidu OpenRASP

Esta skill fornece orientação técnica aprofundada, comandos operacionais e padrões de implementação para o **OpenRASP** ([github.com/baidu/openrasp](https://github.com/baidu/openrasp)), a solução de código aberto líder em **Runtime Application Self-Protection (RASP)** desenvolvida pela Baidu, projetada para proteger servidores web Java e PHP diretamente no ambiente de execução.

---

## 🧭 Visão Geral e Arquitetura do OpenRASP

O OpenRASP opera injetando sondas de instrumentação diretamente nos runtimes das linguagens suportadas, inspecionando parâmetros de execução antes que métodos críticos do sistema operacional ou do banco de dados sejam invocados.

```
┌────────────────────────────────────────────────────────────────────────┐
│                      ARQUITETURA GERAL DO OPENRASP                     │
└────────────────────────────────────────────────────────────────────────┘
  [ NÓ DE APLICAÇÃO (Java / PHP) ]
  ┌────────────────────────────────────────────────────────────────────┐
  │  1. Invocação de Método Sensível (Ex: Statement.executeQuery)      │
  │     │                                                              │
  │     ▼                                                              │
  │  2. Sonda OpenRASP Hook Intercepta a Chamada                       │
  │     │                                                              │
  │     ▼                                                              │
  │  3. Motor Google V8 Embutido Executa o Plugin JavaScript           │
  │     │ (Analisa AST da query SQL, tokenização, regex e stack trace) │
  │     │                                                              │
  │     ├──► Ação: BLOCK  ──► Aborta execução + Lança Erro HTTP 403    │
  │     ├──► Ação: LOG    ──► Registra alerta e permite a chamada      │
  │     └──► Ação: IGNORE ──► Permite a operação normalmente           │
  └─────────────────────────────────┬──────────────────────────────────┘
                                    │ (Heartbeat + Logs de Alerta JSON)
                                    ▼
  [ OPENRASP CLOUD MANAGEMENT CONSOLE ] (Painel Web + API)
  ┌────────────────────────────────────────────────────────────────────┐
  │  - Backend: Go / Python                                            │
  │  - Banco de Dados: MongoDB / MySQL                                 │
  │  - Logs & Analytics: Elasticsearch + Kibana                        │
  │  - Gestão de Políticas e Atualização Automática de Plugins em JS   │
  └────────────────────────────────────────────────────────────────────┘
```

---

## 💻 Instalação e Configuração dos Agentes

### 1. Agente Java (Spring Boot, Tomcat, JBoss, WebLogic)

#### Instalação do Pacote:
Baixe a versão mais recente do OpenRASP Java Agent e descompacte no diretório `/opt/rasp`.

#### Estrutura do Diretório:
```
/opt/rasp/
├── conf/
│   └── openrasp.yml      # Configurações do agente e conexão com o Cloud
├── plugins/
│   └── official.js       # Plugin JavaScript padrão de detecção
├── logs/                 # Logs de alarmes e auditoria em JSON
└── rasp.jar              # Binário principal do Java Agent
```

#### Configuração do Arquivo `conf/openrasp.yml`:
```yaml
# Conexão com o OpenRASP Cloud Management
cloud:
  enable: true
  backend_url: "http://openrasp-cloud.empresa.local:8086"
  app_id: "a1b2c3d4e5f6g7h8i9j0"
  app_secret: "secret-token-gerado-no-painel"
  heartbeat_interval: 180

# Modos de proteção (true = Bloqueio Ativo, false = Apenas Log)
block:
  status: true

# Configurações de logging
logger:
  max_size: 500MB
  max_backup: 10
```

#### Inicialização da Aplicação com o Agente:
```bash
# Executando aplicação Spring Boot (.jar)
java -javaagent:/opt/rasp/rasp.jar -Dfile.encoding=UTF-8 -jar app.jar

# Configuração para Apache Tomcat (no arquivo catalina.sh ou setenv.sh)
export JAVA_OPTS="$JAVA_OPTS -javaagent:/opt/rasp/rasp.jar"
```

---

### 2. Agente PHP (Zend Engine Extension)

#### Instalação do Módulo:
```bash
# Compilação ou instalação via script oficial
cd /tmp && git clone https://github.com/baidu/openrasp.git
cd openrasp/agent/php && phpize
./configure --with-php-config=/usr/bin/php-config
make && sudo make install
```

#### Configuração no `php.ini`:
```ini
; Carregamento da extensão OpenRASP
extension=openrasp.so

; Diretório raiz de configurações e plugins
openrasp.root_dir=/opt/rasp

; Habilitar proteção ativa
openrasp.inject_urlprefix=/
openrasp.block_status=1
```

---

## 📜 Desenvolvimento de Plugins de Detecção em JavaScript (V8 Engine)

O grande diferencial do OpenRASP é a capacidade de estender suas políticas através de scripts em JavaScript executados em uma sandbox V8 nativa de alta velocidade dentro do processo.

### 1. Estrutura de um Plugin OpenRASP (`custom-security.js`)
```javascript
'use strict';

var plugin = new RASP('custom-security-rules');

// =========================================================================
// 1. Interceptação de Injeção de Comandos do Sistema Operacional (RCE)
// =========================================================================
plugin.register('command', function (params, context) {
    var command = params.command;
    
    // Bloquear invocações de shells reversas ou comandos destrutivos
    var dangerousPatterns = [
        /nc\s+-e/i,
        /bash\s+-i/i,
        /rm\s+-rf\s+\//i,
        /curl.*\|\s*sh/i,
        /wget.*\|\s*sh/i
    ];

    for (var i = 0; i < dangerousPatterns.length; i++) {
        if (dangerousPatterns[i].test(command)) {
            return {
                action: 'block',
                message: 'Injeção de Comando Crítica bloqueada pelo OpenRASP: ' + command,
                confidence: 100
            };
        }
    }

    return { action: 'ignore' };
});

// =========================================================================
// 2. Interceptação de SQL Injection com Análise Sintática
// =========================================================================
plugin.register('sql', function (params, context) {
    var query = params.query;
    
    // Detectar injeções booleanas ou de união clássicas
    if (/union(\s+all)?\s+select/i.test(query) || /or\s+1\s*=\s*1/i.test(query)) {
        return {
            action: 'block',
            message: 'SQL Injection detectada em tempo de execução: ' + query,
            confidence: 95
        };
    }

    return { action: 'ignore' };
});

// =========================================================================
// 3. Interceptação de SSRF (Server-Side Request Forgery)
// =========================================================================
plugin.register('ssrf', function (params, context) {
    var url = params.url;

    // Bloquear acesso aos metadados de nuvem (AWS/GCP/Azure) e interfaces de loopback
    if (/169\.254\.169\.254/i.test(url) || /127\.0\.0\.1/i.test(url) || /localhost/i.test(url)) {
        return {
            action: 'block',
            message: 'Requisição SSRF para endereço interno/metadados bloqueada: ' + url,
            confidence: 100
        };
    }

    return { action: 'ignore' };
});
```

---

## 📊 Lista de Hooks Suportados pelo OpenRASP

| Hook ID | Recurso Interceptado | Exemplos de Ameaças Mitigadas |
| :--- | :--- | :--- |
| `sql` | Drivers JDBC / MySQL / PostgreSQL / Oracle | SQL Injection (CWE-89), Stacked Queries |
| `command` | `ProcessBuilder`, `Runtime.exec()`, `system()`, `exec()` | OS Command Injection (CWE-78), Web Shells |
| `readFile` / `writeFile` | `FileInputStream`, `fopen()`, `file_get_contents()` | Path Traversal (CWE-22), Arbitrary File Overwrite |
| `fileUpload` | `MultipartResolver`, `$_FILES` | Upload de Web Shells (`.jsp`, `.php`, `.phtml`) |
| `deserialization` | `ObjectInputStream.readObject()`, `unserialize()` | Insecure Deserialization / Java Gadgets (CWE-502) |
| `ssrf` | `HttpURLConnection`, `HttpClient`, `curl_exec()` | SSRF para redes internas ou metadados de nuvem (CWE-918) |
| `xss_userinput` | Manipulação de saída HTML no buffer de resposta | Stored & Reflected XSS (CWE-79) |
| `ognl` | Evaluators OGNL (Apache Struts) | Struts RCE (CVE-2017-5638, CVE-2018-11776) |

---

## 📈 Formato dos Logs de Alerta e Integração SIEM

Quando um ataque é interceptado, o OpenRASP grava no arquivo `/opt/rasp/logs/alarm/alarm.log` uma entrada JSON completa contendo todo o contexto:

```json
{
  "event_type": "attack",
  "app_id": "a1b2c3d4e5f6g7h8i9j0",
  "server_hostname": "app-prod-01",
  "server_ip": "10.0.1.50",
  "attack_type": "sql",
  "plugin_name": "custom-security-rules",
  "action": "block",
  "confidence": 95,
  "client_ip": "198.51.100.42",
  "request_method": "POST",
  "request_url": "https://app.empresa.com/api/v1/search",
  "attack_params": {
    "query": "SELECT * FROM users WHERE id = 1 UNION SELECT null, username, password FROM admin"
  },
  "stack_trace": [
    "com.mysql.cj.jdbc.StatementImpl.executeQuery(StatementImpl.java:115)",
    "com.empresa.app.dao.UserDAO.findUser(UserDAO.java:45)",
    "com.empresa.app.controller.UserController.search(UserController.java:28)"
  ],
  "timestamp": "2026-08-29T17:30:00.123Z"
}
```

---

## 🔗 Integração com Outras Skills do Repositório

- **[rasp-runtime-protection](../../security/appsec/rasp-runtime-protection/SKILL.md)**: Teoria e diretrizes de governança arquitetural de proteção em tempo de execução.
- **[sast-code-review](../../security/appsec/sast-code-review/SKILL.md)**: Validação estática prévia dos mesmos sinks protegidos pelo OpenRASP.
- **[secops-incident-responder](../../security/ops-architecture/secops-incident-responder/SKILL.md)**: Ingestão de alertas do OpenRASP e criação de playbooks de resposta a incidentes.

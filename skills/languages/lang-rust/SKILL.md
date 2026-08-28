---
name: "lang-rust"
description: "Fornece padrões de engenharia de software em Rust baseados na documentação oficial (doc.rust-lang.org), cobrindo Ownership, Borrowing, Lifetimes, Traits, Concorrência, Async (Tokio), tratamento de erros (Result/Option), Unsafe Rust e ecossistema Cargo."
---

# Habilidade de IA: Engenharia de Rust (Rust Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista na linguagem **Rust**, seguindo rigorosamente as diretrizes da documentação oficial ([doc.rust-lang.org](https://doc.rust-lang.org/stable/)), o livro oficial *The Rust Programming Language*, *Rust by Example*, *The Cargo Book* e *The Rustonomicon*. O objetivo é criar código seguro contra corridas de dados (*data races*), livre de vazamentos de memória (sem Garbage Collector), concorrente e de extrema performance.

---

## 🧭 Diretrizes Gerais de Desenvolvimento em Rust

Ao atuar nesta skill, aplique rigorosamente os fundamentos de segurança de memória e concorrência destemida (*fearless concurrency*):

### 1. Sistema de Posse (Ownership), Empréstimo (Borrowing) e Lifetimes
- **Posse Única (Ownership)**: Cada valor em Rust tem um único proprietário por vez. Quando o proprietário sai de escopo, o valor é desalocado automaticamente via trait `Drop`.
- **Regras de Empréstimo (Borrowing)**:
  - Pode-se ter qualquer número de referências imutáveis (`&T`) **OU** exatamente uma referência mutável (`&mut T`) em um determinado escopo, mas nunca ambas simultaneamente.
  - Referências devem ser sempre válidas (prevenção de ponteiros pendentes / *dangling pointers*).
- **Tempo de Vida (Lifetimes)**:
  - Utilize anotações explícitas de tempo de vida (`'a`) em estruturas e funções apenas quando o compilador não puder elidir as regras de tempo de vida ( Lifetime Elision Rules).

### 2. Tratamento Idiomático de Erros (`Result` e `Option`)
- **Sem Exceções em Tempo de Execução**: Rust não utiliza exceções. Erros recuperáveis devem ser representados pelo tipo enum `Result<T, E>` e valores opcionais por `Option<T>`.
- **Operador de Propagação `?`**: Prefira propagar erros usando o operador `?` em vez de chamadas repetitivas de `match` ou `.unwrap()`.
- **Proibição de `.unwrap()` em Produção**: Evite `.unwrap()` e `.expect()` em código de produção, exceto em testes unitários ou invariantes matematicamente comprovadas.
- **Tratamento Encadeado de Erros**: Utilize crates consolidadas como `thiserror` (para definir erros de bibliotecas) e `anyhow` (para tratamento flexível de erros em aplicações binárias).

### 3. Abstração Zero-Cost, Traits e Genéricos
- **Polimorfismo Baseado em Traits**: Defina comportamentos compartilhados utilizando `trait`. Prefira dispatch estático (*monomorphization*) usando `impl Trait` ou genéricos `<T: Trait>`.
- **Dynamic Dispatch (`dyn Trait`)**: Use `Box<dyn Trait>` apenas quando for estritamente necessário alocar tipos heterogêneos em tempo de execução.
- **Derivações Automáticas**: Utilize atributos decoradores como `#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]` em structs e enums sempre que apropriado.

### 4. Concorrência e Programação Assíncrona (`Async/Await`)
- **Segurança Concorrente Estática**: Tipos que podem ser transferidos entre threads com segurança implementam o marker trait `Send`. Tipos que podem ser acessados concorrentemente via referências imutáveis implementam `Sync`.
- **Sincronização Primitiva**: Use `Arc<T>` (Atomic Reference Counting) para compartilhamento de posse entre threads e `Mutex<T>` ou `RwLock<T>` para mutabilidade interior concorrente.
- **Ecossistema Assíncrono (`Future`)**:
  - Utilize o padrão `async/await` com um runtime assíncrono consolidado como **Tokio** ou `async-std`.
  - Evite bloqueios síncronos de I/O em tarefas assíncronas (use `tokio::task::spawn_blocking` quando necessário).

### 5. Unsafe Rust e FFI
- **Encapsulamento Estrito de `unsafe`**: Isole blocos `unsafe` dentro de abstrações e funções públicas totalmente seguras (*safe wrappers*).
- **Invariantes de Segurança**: Documente detalhadamente as precondições e invariantes de segurança (`// SAFETY: ...`) em cada bloco `unsafe`.
- **FFI (Foreign Function Interface)**: Utilize `extern "C"` e C-compatible tipos (`c_char`, `c_int`) para interoperabilidade segura com C/C++.

---

## 🛠️ Ferramentas e Gerenciamento de Projetos (Cargo & Toolchain)

- **Configuração de Dependências (`Cargo.toml`)**:
  - Defina dependências, recursos opcionais (*features*) e perfis de compilação.
  - Utilize `cargo check` durante o desenvolvimento para compilações rápidas sem geração de código de máquina.
- **Qualidade de Código e Formatação**:
  - **`rustfmt`**: Formatação estrita oficial do código (`cargo fmt`).
  - **`clippy`**: Linter oficial para capturar antipadrões e otimizações (`cargo clippy -- -D warnings`).
- **Segurança de Dependências**: Execute `cargo audit` periodicamente para verificar vulnerabilidades conhecidas em crates de terceiros.

---

## 🧰 Padrões de Código Recomendados

### 1. Manipulação Idiomática de Erros com `Result` e `thiserror`
```rust
use std::fs::File;
use std::io::{self, Read};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ConfigError {
    #[error("falha de E/S ao ler o arquivo de configuração")]
    Io(#[from] io::Error),
    #[error("formato de configuração inválido: {0}")]
    InvalidFormat(String),
}

pub fn read_config(path: &str) -> Result<String, ConfigError> {
    let mut file = File::open(path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    
    if content.is_empty() {
        return Err(ConfigError::InvalidFormat("arquivo vazio".into()));
    }
    
    Ok(content)
}
```

### 2. Concorrência Assíncrona com Tokio e Canais
```rust
use tokio::sync::mpsc;
use tokio::task;

#[derive(Debug)]
pub struct WorkItem {
    pub id: u64,
    pub payload: String,
}

pub async fn run_pipeline(items: Vec<WorkItem>) {
    let (tx, mut rx) = mpsc::channel::<String>(32);

    for item in items {
        let tx_clone = tx.clone();
        task::spawn(async move {
            let result = format!("Processado item {}: {}", item.id, item.payload);
            let _ = tx_clone.send(result).await;
        });
    }

    drop(tx); // Fecha o transmissor original para permitir que o receptor termine quando as tasks concluírem

    while let Some(message) = rx.recv().await {
        println!("[+] Recebido: {}", message);
    }
}
```

### 3. Padrão Builder com Validação Estática
```rust
#[derive(Debug)]
pub struct ServerConfig {
    pub host: String,
    pub port: u16,
}

pub struct ServerConfigBuilder {
    host: Option<String>,
    port: Option<u16>,
}

impl ServerConfigBuilder {
    pub fn new() -> Self {
        Self { host: None, port: None }
    }

    pub fn host(mut self, host: impl Into<String>) -> Self {
        self.host = Some(host.into());
        self
    }

    pub fn port(mut self, port: u16) -> Self {
        self.port = Some(port);
        self
    }

    pub fn build(self) -> Result<ServerConfig, &'static str> {
        let host = self.host.ok_or("host é obrigatório")?;
        let port = self.port.unwrap_or(8080);
        Ok(ServerConfig { host, port })
    }
}
```

---

## 🔒 Questões de Segurança e Práticas Seguras

- **Blocos Unsafe e Comportamento Indefinido**: Isole blocos `unsafe` ao estrito necessário. Certifique-se de que as premissas de segurança de memória exigidas pelo Rust sejam respeitadas, evitando desalinhamentos de dados ou referências nulas.
- **Data Races em Unsafe**: Embora o compilador do Rust garanta a thread-safety do código seguro, o uso incorreto de `Send`/`Sync` e ponteiros crus em blocos `unsafe` pode introduzir condições de corrida complexas.
- **Panics como Vetor de DoS**: Operações aritméticas estritas ou acessos a índices de vetores podem causar `panic!` em runtime se falharem. Use métodos seguros como `.get()` ou `.checked_add()` para evitar interrupções de serviço repentinas.

## 🔗 Integração com Outras Skills

- Para aplicação de análise estática e revisão de segurança em código Rust, consulte [sast-code-review](../../security/appsec/sast-code-review/SKILL.md) e [appsec-owasp-asvs](../../security/appsec/appsec-owasp-asvs/SKILL.md).
- Para integrar acesso a banco de dados com tipos verificados em tempo de compilação em Rust (`sqlx`, `diesel`, `tokio-postgres`, `mongodb`), consulte [dba-database-administrator](../../roles/dba-database-administrator/SKILL.md), [db-postgresql](../../databases/db-postgresql/SKILL.md), [db-sqlite](../../databases/db-sqlite/SKILL.md), [db-mariadb](../../databases/db-mariadb/SKILL.md) e [db-mongodb](../../databases/db-mongodb/SKILL.md).
- Para desenvolvimento de ferramentas ofensivas, agentes de segurança ou parsers de alta performance em Rust, consulte [pentest-scripter-python-bash-go](../../security/appsec/pentest-scripter-python-bash-go/SKILL.md).
- Para modelar a arquitetura e comunicação entre componentes de software usando Rust, consulte [software-architect](../../roles/software-architect/SKILL.md).

# Rust — Guia de Referência (Livro Oficial / rust-lang.org)

Consolidado de "A Linguagem de Programação Rust" (The Rust Programming Language — rust-br.github.io/rust-book-pt-br) e da documentação oficial rust-lang.org/pt-BR/learn (O Livro, Rust by Example, Rustlings, Cargo Book, Rustonomicon, Referência).

---

## 1. Começando (Cap. 1–2)

- **Toolchain via rustup**: `rustup` gerencia versões de `rustc`, `cargo`, docs locais (`rustup doc`). Componentes: `rustfmt`, `clippy`.
- **Cargo (essencial)**:
  - `cargo new <projeto>` → estrutura `src/main.rs` + `Cargo.toml`.
  - `cargo build` / `cargo run` / `cargo check` (rápido, sem gerar binário) / `cargo build --release` (otimizado).
  - `Cargo.toml`: `[package]` (name, version, edition), `[dependencies]`. **Edition** define compatibilidade de idioma (2015/2018/2021) — retrocompatível.
- Estrutura default de projeto: `src/main.rs` (binário) + `src/lib.rs` (biblioteca) + `tests/` (integração).

## 2. Conceitos Comuns (Cap. 3)

- **Variáveis**: `let` = imutável por padrão; `let mut` para mutabilidade; `const` (tipo + valor constante computável, `SCREAMING_SNAKE_CASE`).
- **Shadowing**: redeclarar `let` no mesmo escopo substitui (permite mudar tipo).
- **Tipos escalares**: `i8/u8 … i128/u128`, `isize/usize`, `f32/f64` (default `f64`), `bool`, `char` (4 bytes, Unicode).
- **Inteiros**: literal `_` separador, hexadecimal `0x`, octal `0o`, binário `0b`, byte `b'A'`. Overflow em release **wraps** (`wrapping_add`, `checked_add`, `saturating_add`, `overflowing_add`).
- **Tuplas**: `(i32, f64)` com destructuring e acesso `.0/.1`; unit type `()`.

```rust
fn main() {
    let tup: (i32, f64, char) = (500, 6.4, 'x');
    let (x, y, z) = tup;                    // pattern matching
    let five_hundred = tup.0;
}
```

- **Arrays**: tamanho fixo `[i32; 5]`, alocado na stack; acesso `a[0]`; out-of-bounds → **panic** (bounds check).
- **Funções**: nomes `snake_case`; tipos obrigatórios nos parâmetros; **última expressão é o retorno** (sem `;`):
  ```rust
  fn plus_one(x: i32) -> i32 { x + 1 }
  ```
- **Comentários de documento** `///` viram docs no `cargo doc`.
- **Controle de fluxo**: `if/else` (condição deve ser `bool`, sem truthiness); `if` é expressão; **loops com rótulos** `'outer: loop` e `break 'outer value`/`continue`; `loop` retorna valor; `while`; `for x in` sobre ranges/iteradores:
  ```rust
  let r = loop { break 5 * 2; };     // loop como expressão → 10
  for num in (1..4).rev() { ... }
  ```

## 3. Ownership, Borrowing e Slices (Cap. 4) — fundamento único de Rust

- **Regras de ownership**:
  1. Cada valor tem **um único dono**.
  2. Quando o dono sai de escopo, o valor é **drop** (RAII).
  3. Atribuição/move de valores não-Copy **move** a posse (shallow copy + invalida a origem).
- **Stack vs Heap**: tipos conhecidos em compile time vão para stack; `String` (dados no heap) move, `i32` copia (Copy/Clone).
- **Move semantics**: atribuir uma `String` a outra transfere posse (`use of moved value` se usar a origem).
- **Copy trait**: inteiros, floats, bool, char, tuplas de tipos Copy. `Clone` para cópia deep explícita (`s.clone()`).

```rust
let s1 = String::from("olá");
let len = calcular(&s1);            // borrowing — não transfere posse
fn calcular(s: &String) -> usize { s.len() }
let mut s2 = String::from("a");
s2.push_str("b");
let r1 = &s2; let r2 = &s2;         // N referências imutáveis OK
// let r3 = &mut s2;                // ERRO: &mut enquanto há & vivas
let r4 = &mut s2;                   // OK após r1/r2 usarem e morrerem (NLL)
```
- **Borrowing**: `&T` (compartilhada, múltiplas) OU `&mut T` (exclusiva, única). Nunca ambas ao mesmo tempo.
- **Dangling references** impossíveis em safe Rust: borrow checker garante que o dado vive além da referência.
- **Slices**: view sem posse sobre coleção — `&str` (string slice), `&[i32]` (array slice):
  ```rust
  fn first_word(s: &str) -> &str { s.split_whitespace().next().unwrap_or("") }
  // &String é coerível para &str (deref coercion); prefira &str em APIs
  ```

## 4. Structs (Cap. 5)

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,     // tuple structs: struct Point(i32, i32);
}                           // unit structs: struct AlwaysEqual;

impl User {
    fn new(email: String) -> Self {
        User { active: true, username: String::from("anônimo"), email, sign_in_count: 1 } // field init shorthand
    }
    fn email(&self) -> &str { &self.email }              // método (associated function com receiver)
    fn to_upper_email(mut self) -> Self {                 // consumer builder-style
        self.email = self.email.to_uppercase(); self
    }
}
let u = User::new(String::from("a@b.c"));
```
- **Struct update syntax**: `..outro` copia campos restantes (**move** os não-Copy).
- **Métodos** (`&self` = borrow, `&mut self` = mut borrow, `self` = consume) e **associated functions** sem receiver (construtores `::new`).
- Acessos a campos podem ser "out of borrow" (separação de campos pelo borrow checker).

## 5. Enums e Pattern Matching (Cap. 6, 18)

```rust
enum IpAddr { V4(u8, u8, u8, u8), V6(String) }        // enums carregam dados
enum Shape { Circle(f64), Square(f64), Triangle(f64) }

fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r) => std::f64::consts::PI * r * r,
        Shape::Square(s) => s * s,
        Shape::Triangle { base, height } => (base * height) / 2.0,
    }
}

enum Option<T> { Some(T), None }           // do core, elimina null
fn dividir(x: f64, y: f64) -> Option<f64> {
    if y == 0.0 { None } else { Some(x / y) }
}

if let Some(val) = talvez_valor() { ... }  // um caso só
let x = 5;                                  // let pode desestruturar
let (a, b) = (1, 2);
```
- **`match` é exaustivo** (obrigatório cobrir todos os casos; `_` como catch-all).
- Guards `x if x > 5`, bindings `@` (`n @ 1..=5`), `|` or-patterns, `..` ranges, destructuring de structs/tuplas, matches em `Result`/`Option`.
- **`Option<T>`**: nunca `None` implícito; métodos úteis `.unwrap_or(default)`, `.map`, `.and_then`, `.ok_or(err)`, `.expect("msg")` (só em testes/invariantes).

## 6. Módulos e Packages (Cap. 7)

- **Package** = 1+ crates; **crate** = unidade de compilação (lib ou binário); **module** = organiza código dentro do crate.
- Módulos formam árvore; `mod` declara; `pub` torna público; caminhos absolutos (`crate::`) ou relativos (`super::`, `self::`).
- `use` importa (renomear `use foo::bar as baz`), re-exportar `pub use`, módulos em arquivos separados `mod nome;` → `src/nome.rs` ou `src/nome/mod.rs`.
- **Idiom: binary crate fino, library crate com a lógica + testes** (`lib.rs` + `main.rs` pequeno).

## 7. Coleções Comuns (Cap. 8)

| Coleção | Descrição / idiom |
| :--- | :--- |
| `Vec<T>` | array dinâmico no heap (`vec![1,2,3]`, `push/pop`, indexa com `[]` (panico) ou `.get(i) -> Option<&T>`); iterar `for x in &v`. |
| `String` | UTF-8, `String::from`, `+`/`format!`; acesso por índice **não funciona** (UTF-8 variável) — usar `chars()`, `bytes()`, slices que respeitem fronteiras de caracteres. |
| `HashMap<K, V>` | `insert`, `get(&k) -> Option<&V>`, entry API (`map.entry(k).or_insert(0)` += 1), `remove`, iteração `for (k, v) in &map` (ordem arbitrária). |
- Ownership: `insert(s.clone())` ou mover; `String` keys comuns; iteradores possuem os valores (a menos que `&map`/`&vec`).

## 8. Tratamento de Erros (Cap. 9) — sem exceções

- **`panic!`** = irrecuperável (bug de invariante, array OOB, unhandled unwrap). **`Result<T, E>`** = recuperável:
  ```rust
  enum Result<T, E> { Ok(T), Err(E) }
```
- **`?`** propaga `Err` e unwraps `Ok` (também em `Option<T>`); funciona em funções que retornam `Result`/`Option`.
- `.unwrap()`/`.expect()` **nunca em produção** (código de protótipo/testes/invariantes).
- Estratégia: "Não entre em panic" — use `Result` para falhas esperadas (arquivo, rede, parse) e `panic!`/unreachable para bugs de programador.
- Erros de biblioteca: enumerar com `#[error(...)]` (`thiserror`); apps: `anyhow::Result` + `?` + contexto `.context("...")`.

## 9. Genéricos, Traits e Lifetimes (Cap. 10)

- **Genéricos**: `<T>` em funções/structs/impls — zerocost via **monomorphization** (código especializado por tipo em compile-time).
  ```rust
  fn maior<T: PartialOrd>(list: &[T]) -> &T { ... }
  struct Point<T> { x: T, y: T }

  impl<T: std::fmt::Display> Point<T> {
      fn print(&self) { println!("{}", self.x); }
  }
  ```
- **Traits = contratos de comportamento** (interfaces com default methods):
  ```rust
  trait Resumir {
      fn resumir(&self) -> String;
      fn preview(&self) -> String { format!("Lendo: {}", self.resumir()) } // default
  }
  impl Resumir for Artigo { fn resumir(&self) -> String { ... } }
```
- **Trait bounds**: `<T: Resumir>`; múltiplos `where` ou `impl Resumir + Clone`.
- **Retorno de traits** (aparele types): `fn cria() -> impl Resumir { ... }` (um tipo só); objetos trait `Box<dyn Resumir>` para **dynamic dispatch** (heterogênio/vtable).
- **Trait objects `dyn Trait`**: `&dyn Trait` ou `Box<dyn Trait>` para polimorfismo em runtime.

### Lifetimes

- Garantem que referências permaneçam válidas (**não mudam a vida — apenas descrevem**):

```rust
// Elision rule: 1 ref-input → 1 lifetime de saída implícita
fn maior<'a>(a: &'a str, b: &'a str) -> &'a str { if a.len() > b.len() { a } else { b } }

struct Livro<'a> {
    titulo: &'a str,   // struct não pode sobreviver às suas referências
}
impl<'a> Livro<'a> { fn first(&self) -> &'a str { self.titulo } }
```
- `'static` = viva pelo programa inteiro (literals, `Box::leak`).

## 10. Testes (Cap. 11) — integração com cargo test

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn um_mais_um() { assert_eq!(1 + 1, 2); }

    #[test]
    #[should_panic(expected = "index out of bounds")]
    fn falha() { let v: Vec<i32> = vec![]; v[0]; }

    #[test]
    fn io_erro() -> Result<(), Box<dyn std::error::Error>> {
        let f = File::open("inexistente")?;
        Ok(())
    }

    #[test]
    #[ignore]
    fn caro() { ... }
}
```
- `cargo test` roda unit tests + integration tests (em `tests/`) + doc-tests.
- Unit tests colados no módulo (`#[cfg(test)] mod tests { use super::*; ... }`); integração em `tests/*.rs`; docs em `///` com ``` examples.

## 11. Projeto I/O idiomático (Cap. 12) — minigrep

- CLI `std::env::args()` / `std::env::var`; leitura de arquivo `fs::read_to_string`; separar config/pesquisa em `src/lib.rs`, I/O em `main.rs`.
- Erros na **stderr**: `eprintln!` (para pipes); `Result<(), Box<dyn Error>>` como retorno de main.

## 12. Features Funcionais — Closures e Iterators (Cap. 13)

```rust
let nums = vec![1, 2, 3, 4, 5];
let soma = nums.iter().filter(|&&x| x % 2 == 0).map(|x| x * 2).sum::<i32>();
// soma com closures capturando por referência/move
let clonado = nums.clone();
let pares = nums.iter().filter(|x| x % 2 == 0).collect::<Vec<_>>();
```
- **Closures**: inferem tipos; capturam por empréstimo (`Fn`), mut (`FnMut`) ou posse (`FnOnce`); `move` transfere posse (necessário para threads/tasks).
- **Iterators são lazy** — `.collect()` consome; **sem custo**: compilado para loop nativo igual.
- Closures/iterators são zero-cost: preferir `.iter().map/filter/sum` a loops manuais quando clássicas.

## 13. Cargo, Crates.io e Workspaces (Cap. 14)

- **Release Profile** (`Cargo.toml`):
  ```toml
  [profile.dev]
  opt-level = 0
  [profile.release]
  opt-level = 3
  ```
- `cargo publish` (crates.io) — requer versionamento semântico e README.
- **Cargo Workspaces**: monorepo com múltiplos crates compartilhando lockfile/target.

## 14. Smart Pointers (Cap. 15) — Box, Rc, RefCell, Arc, Mutex

| Smart Pointer | Uso idiomático |
| :--- | :--- |
| `Box<T>` | heap allocation, tamanho conhecido (recursividade, `dyn Trait`). |
| `Rc<T>` | contagem refs **single-thread** (não `Send`); ciclos exigem `Weak<T>`. |
| `Arc<T>` | contagem refs **thread-safe** (atomic) para compartilhar entre threads. |
| `RefCell<T>` | mutabilidade interior com check em **runtime** (single-thread); `borrow()/borrow_mut()`. |
| `Mutex<T>` / `RwLock<T>` | mutabilidade interior **thread-safe** (lock/guard). |
- **Drop** (`impl Drop for X`) → RAII; **Deref** (auto-coerção `&SmartPtr` → `&T`).

### Ciclos de referência = vazamento (mesmo em Rust)
`Rc<RefCell<T>>` com ciclo → vaza. Solução: usar `Weak<T>` (upgrade() -> Option<Rc<T>>) no lado "não-don".

## 15. Concorrência (Cap. 16) — fearless concurrency

- **Threads OS**: `std::thread::spawn(move || ...)`; `join()` espera; dados movidos via `move`.
- **Canais**: `std::sync::mpsc::channel()` (`mpsc::Sender/receiver`); transferência de posse por mensagem.
- **Arc + Mutex**: compartilhar mutabilidade entre threads:
  ```rust
  let counter = Arc::new(Mutex::new(0));
  let mut handles = vec![];
  for _ in 0..10 {
      let c = Arc::clone(&counter);
      handles.push(std::thread::spawn(move || { *c.lock().unwrap() += 1; }));
  }
  for h in handles { h.join().unwrap(); }
  ```
- **Send/Sync** marker traits — garantias seguras pelo compilador: `Send` = transferível entre threads; `Sync` = compartilhado (&T é Send).
- Alternativa moderna: **Tokio** (`tokio::spawn`, async/await) para I/O concurrency; `rayon` para paralelismo de dados (par_iter).

## 16. Rust OOP e padrões de projeto (Cap. 17)

- Rust **não é classe**; usa **traits + structs + impl** (composição>herança); trait objects `Box<dyn Trait>` para polimorfismo runtime; state pattern via enums trocando estados (mais idiomático que OO).

## 17. Advanced Types / Macros / Unsafe (nomicon)

- **Newtype**: `struct Meters(f64);` para type-safety.
- **Type aliases**: `type Kilometers = f64;`
- **Never type `!`**: para funções que nunca retornam (`panic!`, `continue`, `process::exit`).
- **DST**: `str`, `[T]`, `dyn Trait` (tamanho não conhecido) — por trás de `&`/`Box`.
- **Macros**: `macro_rules!` (declarativas) e proc macros (`derive`, attribute, fun-like) — código que gera código.
- **unsafe**: `unsafe { ... }` habilita deref de raw pointer, chamar FFI, mutar estáticos, acessar union fields. Encapsular em abstrações seguras com comentário `// SAFETY:`.

## 18. Keywords resumidas

`as`, `break`, `const`, `continue`, `crate`, `dyn`, `else`, `enum`, `extern`, `false`, `fn`, `for`, `if`, `impl`, `in`, `let`, `loop`, `match`, `mod`, `move`, `mut`, `pub`, `ref`, `return`, `self`, `Self`, `static`, `struct`, `super`, `trait`, `true`, `type`, `unsafe`, `use`, `where`, `while`, `async`, `await`.
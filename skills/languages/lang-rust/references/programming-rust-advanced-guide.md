# Rust — Guia Avançado (Programming Rust 2ª ed. + TRPL 3ª ed.)

Consolidado de **Programming Rust, 2nd Edition** (Jim Blandy, Jason Orendorff, Leonora Tindall — O'Reilly) e **The Rust Programming Language, 3rd Edition** (Steve Klabnik, Carol Nichols, Chris Krycho — Rust 1.85+, edition 2024). Este guia cobre temas profundos que complementam o [guia do Livro](rust-book-guide.md): layout de memória, traits/generics avançados, unsafe, atomics e memory orderings, macros `macro_rules!`, Pin/Futures e FFI.

---

## 1. Layout de Memória: Sizes, Alignment e `repr` (Programming Rust, Cap. 8/10)

- **`std::mem::size_of::<T>()`** retorna o tamanho em bytes de um valor do tipo `T`; **`std::mem::align_of::<T>()`** retorna seu alinhamento:

```rust
use std::mem::{size_of, align_of};

assert_eq!(size_of::<i64>(), 8);
assert_eq!(align_of::<(i32, i32)>(), 4);
```

- Para valores atrás de referências (slices, DSTs), use `size_of_val` e `align_of_val`, que consultam o tipo dinâmico do valor:
  - `size_of_val(slice)` de uma `&[u8]` de 5 elementos = 5 bytes;
  - `size_of_val(text)` de uma `&str` de 9 caracteres = 9 bytes.
- **Reordenação de campos**: Rust reorganiza os campos de structs para minimizar o tamanho total (reduzir padding). Zero-sized types (ZSTs) não ocupam espaço. Isso difere de C, que preserva a ordem de declaração.
- **`#[repr(Rust)]`** (padrão): layout livre, otimizado pelo compilador — não use para FFI.
- **`#[repr(C)]`**: campos na ordem declarada, como um compilador C faria — obrigatório para interoperabilidade e para unions cujo layout importa:

```rust
#[repr(C)]
union SignExtractor {
    value: i64,
    bytes: [u8; 8],
}

fn sign(int: i64) -> bool {
    let se = SignExtractor { value: int };
    unsafe { se.bytes[7] >= 0b10000000 } // sign bit no byte mais significativo
}
```

- **`#[repr(transparent)]`**: garante que um wrapper de um único campo tenha exatamente o layout do campo interno.
- **`#[repr(u8)` / `#[repr(i16)` / etc.]**: fixa a representação de enums ao tamanho do inteiro indicado (útil para enums C/C++ com inteiros explícitos ou para fazer casting seguro via `transmute` controlado).
- **Fat pointers**: referências a slices (`&[T]`, `&str`) e trait objects (`&dyn Trait`) ocupam **duas palavras** — ponteiro + metadado (length ou vtable):
  - Slice: ponto de início + número de elementos.
  - Trait object: ponteiro para o dado + ponteiro para a **vtable** (gerada uma vez em tempo de compilação, compartilhada por todos os objetos do mesmo tipo).
- **`Sized`**: marker trait implementado automaticamente para todos os tipos de tamanho conhecido em compilação; `T: Sized` é o bound padrão de genéricos. Tipos unsized (`str`, `[T]`, `dyn Trait`) só podem aparecer atrás de `&`, `Box`, `Rc`, etc. O bound `?Sized` relaxa essa exigência.
- **Union**: todos os campos compartilham a mesma memória; o tamanho é o do maior campo e apenas um campo está ativo. Ler um campo de uma union é `unsafe` (cabo de reinterpretar bits). Com `#[repr(C)]`, todos os campos começam no offset 0, permitindo extração manipulada de bits (como no exemplo `SignExtractor`).

## 2. Traits e Generics Avançados (Programming Rust, Cap. 11; TRPL, Cap. 20)

- **Objetos trait (dynamic dispatch)**: `Box<dyn Trait>`, `&dyn Trait`, `Rc<dyn Trait>`. Em memória, um trait object é um fat pointer (dado + vtable). A vtable é única por tipo concreto e gerada em compile time.

```rust
let shapes: Vec<Box<dyn Draw>> = vec![Box::new(Button), Box::new(Select)];
for s in &shapes { s.draw(); } // dispatch via vtable
```

- **Object safety**: um trait só pode ser convertido em `dyn Trait` se for "dyn-compatible": métodos sem generics e sem `Self` por valor, sem associated functions não recebedoras etc. Traits com associated types só viram objetos se todos os tipos associados forem especificados (`Box<dyn Iterator<Item = i32>>`).
- **Associated types**: vinculam um tipo de saída ao trait, evitando anotações repetidas no call-site:

```rust
use std::ops::Add;

impl Add for Point {          // trait Add<Rhs=Self> { type Output; fn add(...) ... }
    type Output = Point;
    fn add(self, other: Point) -> Point { /* ... */ }
}
```

  - Use associated types quando houver **um único tipo de saída lógico por implementação** (ex.: `Iterator::Item`). Use genéricos `<T>` quando a mesma implementação precisa funcionar com múltiplos tipos (`Add<i64> for Point`).
- **Default generic parameters e operator overloading**: `Add<Rhs = Self>` com type parameter default; sobrecarga de operadores é feita implementando os traits de `std::ops` (`Add`, `Mul`, `Index`, `Fn`, ...).
- **Fully qualified syntax**: resolve ambiguidade entre métodos de mesmo nome (trait próprio vs. trait importado vs. `Self`):

```rust
<Pilot as Flyable>::fly(&person);   // chama Pilot::fly
<<Wizard as Flyable>::fly>(&person);
```

- **Supertraits**: `trait Player: fmt::Display { ... }` exige que implementadores também implementem `Display`.
- **Newtype pattern para implementar traits externos**: `struct Wrapper(Vec<String>);` contorna a orphan rule (trait externo + tipo externo), muito usado com `Display` sobre `Vec`.
- **`impl Trait`** (static dispatch por type erasure em assinaturas):
  - `fn make_adder(x: i32) -> impl Fn(i32) -> i32` — retorna uma closure sem nomear o tipo concreto (único tipo por função).
  - Diferente de `dyn Trait` na frente de `&`/`Box`: `impl Trait` é estático (monomorfizado) e não permite retorno de tipos heterogêneos.

## 3. Unsafe Avançado (Programming Rust, Cap. 22; TRPL, Cap. 20)

- **Raw pointers (`*const T`, `*mut T`)**:
  - Podem ser nulos, desalinhados e apontar para memória livre — **dereferenciar é sempre `unsafe`**.
  - Safe Rust pode criar raw pointers de referências (`let p = &mut v[0] as *mut i32;`), números arbitrários não podem ser dereferenciados.
  - Diferem de referências: sem garantia de validade, sem aliasing exclusivo (o que ativa menos otimizações; use `&T`/`&mut T` sempre que possível).
- **`unsafe fn`**: declara que toda a função impõe contratos ao chamador; o corpo pode operar como bloco `unsafe`. Chamar é `unsafe`. Idiomática: prefixar com `unsafe_` (`Vec::from_raw_parts`-style) e documentar a precondição.
- **Unsafe traits**: um trait cujo contrato o compilador não verifica — implementadores devem manualmente garantir a invariante:

```rust
pub unsafe trait Zeroable {}

unsafe impl Zeroable for u8 {}   // zeroizar um i8 é seguro
// unsafe impl Zeroable for &T {} // ERRADO: &T zeroizada é null reference
```

  - **`Send` e `Sync` são unsafe traits** canônicos: `Send` exige segurança ao mover entre threads; `Sync` exige segurança de acesso compartilhado (`&T: Send`). Implementá-los para tipos inapropriados destrói a segurança de todo o ecossistema (p.ex., tornaria `Mutex` insegura).
- **Unions**: declarar como no C; construir/atribuir campos é safe, mas **ler é `unsafe`**. Sempre use `#[repr(C)]` quando um union cruza fronteira com C.
- **Miri** (TRPL 3ª ed., Cap. 20): verificador dinâmico oficial (`rustup +nightly component add miri` + `cargo +nightly miri test`) para detectar undefined behavior em código unsafe — use como parte da suíte de testes de abstrações unsafe.

## 4. Concorrência Detalhada: Atomics, Memory Orderings, Scoped Threads (Programming Rust, Cap. 19)

- **Atomics (`std::sync::atomic`)**: `AtomicBool`, `AtomicIsize/Usize`, `AtomicI8..I64/AtomicU8..U64`, `AtomicPtr<T>`. Múltiplas threads podem ler/escrever sem data races. Métodos em vez de operadores:

```rust
use std::sync::atomic::{AtomicIsize, Ordering};

let atom = AtomicIsize::new(0);
atom.fetch_add(1, Ordering::SeqCst);  // x86-64: lock incq (lock-free)
```

- **Memory orderings (`Ordering`)** — análogo a níveis de isolamento de transação em banco de dados: definem quão fortes são as garantias de causalidade/tempo vs. performance:
  - `SeqCst` (sequentially consistent): a mais rigorosa — todas as operações aparecem em uma única ordem global. **Quando em dúvida, use `Ordering::SeqCst`** (a penalidade de performance é geralmente baixa).
  - `Acquire`/`Release`: pares producer-consumer de consistência de memória (release store → acquire load publica/observa escritas anteriores).
  - `Relaxed`: garante apenas atomicidade da operação individual, sem ordenação entre threads (para contadores independentes).
  - Rust herda os orderings do modelo Standard C++ atomics; errar orderings causa data races não detectadas pelo compilador.
- **Uso idiomático de AtomicBool: flag de cancelamento** entre threads (compartilhada em `Arc<AtomicBool>`), verificada em pontos de checagem do loop de trabalho.
- **`std::thread::JoinHandle`**: `thread::spawn` retorna `JoinHandle<T>`; `.join()` aguarda e retorna `Result<T, Box<dyn Error>>` (a thread pode ter entrado em panic).
- **Scoped threads (`std::thread::scope`)**: fork-join com borrowing — as threads do escopo podem referenciar dados locais do frame que as criou, sem `Arc`, pois o escopo garante que todas terminam antes do retorno:

```rust
let mut results = vec![];
std::thread::scope(|s| {
    for chunk in data.chunks_mut(1000) {
        s.spawn(|| results.push(process(chunk))); // &mut borrowing direto
    }
}); // todas as threads morrem antes de `results` ser usado
```

- **Canais e locks**: lembre-se que `mpsc::Receiver` é single-consumer; para work-stealing entre workers use `Arc<Mutex<Receiver<T>>>` ou `crossbeam-channel` (que também oferece scoped threads e MPMC). `Mutex::lock()` retorna `LockResult<Guard>` — o guard `MutexGuard` implementa `Deref/DerefMut` e libera ao sair de escopo (RAII); deadlocks evitáveis com ordem fixa de locks.
- **`catch_unwind` e panics entre threads**: `std::panic::catch_unwind()` captura unwinding do panic (usado pelo test harness); útil para isolar worker threads. Panics em `Drop` aninhados ou `-C panic=abort` abortam o processo inteiro.

## 5. Macros Declarativas com `macro_rules!` (Programming Rust, Cap. 21; TRPL, Cap. 20)

- `macro_rules!` opera por **pattern matching de tokens** (não de caracteres): padrões consomem fragmentos tipados e o template substitui `$name` pelo fragmento capturado.

```rust
macro_rules! log {
    ($left:expr, $right:expr) => {
        eprintln!("{} / {}", stringify!($left), stringify!($right));
    };
}
```

- **Erros comuns**: escrever `$left:expr` no **template** (só no padrão!) faz o macro injetar tokens espúrios `: expr` — o erro aparece apenas no call-site (`cannot find type 'expr' in this scope`). Use apenas `$left`.
- **Fragment specifiers (Table 21-2 — Programming Rust)**:

| Fragment | Matches | Pode ser seguido de |
| :--- | :--- | :--- |
| `expr` | expressão: `2 + 2`, `"udon"`, `x.len()` | `=>`, `,`, `;` |
| `stmt` | expressão ou declaração | `=>`, `,`, `;` |
| `ty` | tipo: `String`, `Vec<u8>` | `=>`, `,`, `;`, `=`, `\|`, `{`, `[`, `:`, `>`, `as`, `where` |
| `path` | path: `fern`, `::std::sync::mpsc` | idem `ty` |
| `pat` | pattern: `_`, `Some(ref x)` | `=>`, `,`, `=`, `\|`, `if`, `in` |
| `item` | item: `struct Point {...}`, `mod ferns` | qualquer |
| `block` | bloco: `{ s += "ok\n"; true }` | qualquer |
| `meta` | corpo de attribute: `inline`, `derive(Copy, Clone)` | qualquer |
| `ident` | identificador: `std`, `Json` | qualquer |
| `literal` | literal: `1024`, `"Hello"`, `1_000_000f64` | qualquer |
| `lifetime` | `'a`, `'static` | qualquer |
| `vis` | visibilidade: `pub`, `pub(crate)` | qualquer |
| `tt` | token tree | qualquer |

- **Repetições**: `$( $x:expr ),+` (uma ou mais, separadas por vírgula), `$( ... ),*` (zero ou mais); suporte a trailing comma opcional para permitir ambas as formas.

```rust
macro_rules! vec_shortcut {
    ( $( $x:expr ),+ , ) => { {
        let mut v = Vec::new();
        $( v.push($x); )+
        v
    } };
    ( $( $x:expr ),+ ) => { vec_shortcut![ $( $x ),+ , ] };
}
```

- **Macros built-in úteis**: `file!()`, `line!()`, `column!()`, `stringify!`, `concat!`, `cfg!`, `env!`. Para metaprogramação complexa (derive customizado, attribute macro, function-like macro), use **proc macros** (crate `syn` + `quote`).
- **Higiene**: identifiers criados no template não vazam para o call-site; fragmentos capturados preservam a visibilidade original do código-fonte.

## 6. Pin/Unpin e Internals de Futures/Async (TRPL 3ª ed., Cap. 17; Programming Rust, Cap. 20)

- **`async fn` desugars**: `async fn f() -> T` é aproximadamente `fn f() -> impl Future<Output = T>`. O corpo compila para uma **state machine** que gera uma `Future`. `async` blocks (`async move { ... }` move capturas por posse) criam futures anônimas.

```rust
use std::future::Future;

async fn page_title(url: &str) -> Option<String> {
    // equivalente a: fn page_title<'a>(url: &'a str) -> impl Future<Output = Option<String>> + 'a
    // o futuro retém os parâmetros emprestados, tornando o Future 'a
    /* ... */
}
```

- **Trait `Future`** (std::future):

```rust
trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}

enum Poll<T> { Ready(T), Pending }
```

  - O runtime faz polling; a Future sinaliza prontidão via `Waker` (dentro de `Context`) para ser re-pollada quando o dado chegar — o executor não faz busy-wait.
- **Pin/Unpin**: futures são frequentemente **self-referential** (guardam ponteiros para os próprios campos). Se uma future se move na memória entre polls, esses ponteiros internos invalidam-se. Logo:
  - `Pin<&mut T>` garante que o valor **não se moverá** da memória enquanto estiver pinned.
  - A maioria dos tipos comuns (`i32`, `String`, closures async comuns) é **`Unpin`**: não há necessidade de pinning real, `Pin<&mut T>` se comporta como `&mut T`.
  - Uma Future que captura referências (ex.: gerada de `async fn` com parâmetros `&str`) **não é Unpin**; para `.poll()` manualmente use `Box::pin(my_future).as_mut().poll(&mut cx)`.

```rust
use std::pin::Pin;
use std::task::{Context, Poll};

fn do_poll<F: Future>(fut: Pin<&mut F>, cx: &mut Context) -> Poll<F::Output> {
    fut.poll(cx) // método poll exige Pin<&mut Self>
}
```

  - `Unpin` é um marker trait auto-implementado para todos os tipos cujo movimento é seguro. Combinar com generics async usa `F: Future + Unpin` como bound prático para loops manuais de polling.
- **`Stream` trait**: análogo assíncrono de `Iterator` — `poll_next` retorna `Poll<Option<Item>>` (`Some` = item disponível; `None` = fim). Combinadores como `map`, `filter`, `timeouts` funcionam via traits extension do ecossistema (`futures::StreamExt`).
- **Concorrência assíncrona em prática**: `.await` sequencial executa em série; `tokio::join!`/`try_join!` ou `FuturesUnordered` executam concorrentemente. Use `select!` para compor races de múltiplos caminhos de efeito.

## 7. FFI Detalhado: `repr(C)`, Strings, Panic Safety (Programming Rust, Cap. 23)

- **Tipos C-compatíveis**: `std::os::raw::{c_char, c_int, c_uchar, ...}` mapeiam 1:1 aos tipos C usuais em todas as plataformas suportadas. `usize` ↔ `size_t` são idênticos.
- **Structs compatíveis com C**: use `#[repr(C)]` — campos em ordem declarada, sem reordenação. Cada campo individual deve também ser de tipo C-like. Sem `#[repr(C)]`, Rust reordena campos e ZSTs ocupam zero bytes:

```rust
use std::os::raw::{c_char, c_int};

#[repr(C)]
pub struct git_error {
    pub message: *const c_char,
    pub klass: c_int,
}
```

- **Enums**: por padrão, Rust usa 1 byte para variantes sem dados; `#[repr(C)]` força tamanho de `c_int`. Para representação exata de uma enum C de 16 bits, use `#[repr(i16)]`. Enums com payload (tagged unions à la Rust) **não são** FFI-safe — no lugar, modele tag + union:

```rust
#[repr(C)] #[derive(Clone, Copy)] pub enum Tag { Float = 0, Int = 1 }

#[repr(C)] pub union FloatOrInt { f: f64, i: i64 }

#[repr(C)] pub struct Value { pub tag: Tag, pub union: FloatOrInt }
```

- **Opaque types**: para tipos C handle (que o Rust só passa ao redor), declare structs vazias ZST (`#[repr(C)] pub struct git_repository { _private: [u8; 0] }`) e use `*const`/`*mut` opacos.
- **Extern block**: declara funções definidas em outra biblioteca (link na fase final). Funções declaradas em `extern "C" {}` são `unsafe` por padrão (chamadas exigem bloco `unsafe`):

```rust
use std::os::raw::c_char;

extern {
    fn strlen(s: *const c_char) -> usize;
}

#[link(name = "git2")]   // linka libgit2
extern {
    pub fn git_libgit2_init() -> c_int;
    pub fn git_repository_open(out: *mut *mut git_repository, path: *const c_char) -> c_int;
}
```

- **Strings — CString/CStr**: `String`/`&str` não são null-terminated, e podem conter bytes nulos internos. Nunca passe `&str` diretamente para C. Use:
  - `CString::new(rust_str)` → string owned null-terminated (falha com `NulError` se o corpo tiver `\0` interno);
  - `c_string.as_ptr()` → `*const c_char` para funções C;
  - `CStr::from_ptr(ptr)` (para bytes emprestados de C) → `to_str() -> Result<&str, Utf8Error>` para converter a `&str` (checa UTF-8).
- **Callbacks — expondo Rust para C**: use `#[no_mangle] extern "C" fn` para exportar funções Rust; a chamada por ponteiro de função usa apenas callbacks com conversões C-style. Em Rust moderno, assinaturas para FFI devem usar `unsafe extern "C"` se os corpos envolvem `unsafe`.
- **Panic safety através da fronteira**:
  - Unwinding **através de código C/C++ é undefined behavior** — um panic em uma função Rust chamada por C pode atravessar frames C e corromper o estado do processo.
  - Use `std::panic::catch_unwind` na fronteira para capturar panics e convertê-los em códigos de retorno/códigos de erro C, ou configure o runtime com `panic = "abort"` para abortar imediatamente em vez de unwinding.
  - `panic=abort` reduz o tamanho do binário (não precisa de tabela de unwinding), mas remove a capacidade de `catch_unwind`.
  - Lembre que `catch_unwind` só intercepta panics que unwind — com `abort`, o programa morre no primeiro panic.
- **bindgen/cbindgen**: para headers C extensos, o crate `bindgen` gera declarações `#[repr(C)]` e `extern` blocks a partir de headers `.h`; para gerar headers C de APIs Rust, use `cbindgen`.
- **Boas práticas**: trate a API externa como **unsafe por definição** em um módulo `raw` interno; construa **safe wrappers** que traduzem contratos C (null-terminated, lifetimes implícitos, códigos de erro) para os tipos idiomáticos Rust (`Result<T, E>`, `&str`, RAII `Drop` para `*_free`).

---

## Referências dos capítulos

- Programming Rust 2ª ed.: Cap. 8 (Structs/Layout), Cap. 10–11 (Generics/Traits/fat pointers), Cap. 13 (Utility Traits/Sized), Cap. 19 (Concorrência/Atomics), Cap. 21 (Macros), Cap. 22 (Unsafe), Cap. 23 (FFI/libgit2).
- TRPL 3ª ed. (edition 2024, Rust 1.85+): Cap. 17 (Async Fundamentals, Future/Stream/Pin), Cap. 19 (Patterns e `let else`), Cap. 20 (Advanced Features, Advanced Traits, Macros, unsafe + introdução ao Miri), Apêndice E (Editions).
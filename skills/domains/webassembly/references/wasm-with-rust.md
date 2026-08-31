# Programming WebAssembly with Rust (Kevin Hoffman) — Notas Consolidadas

> Fonte: *Programming WebAssembly with Rust* (Kevin Hoffman, The Pragmatic Bookshelf, 2019).
> Cobre wasm-bindgen, integração com JavaScript, hosts fora do browser e padrões host/guest. Complementa [wasm-mdn-guide.md](wasm-mdn-guide.md) e [wasm-definitive-guide.md](wasm-definitive-guide.md).

---

## 1. wasm-bindgen — bindings Rust ↔ JavaScript (cap. 4)

- `wasm-bindgen` é um conjunto de **crates + CLI**. Em essência: o `#[wasm_bindgen]` (macro procedural) **injeta metadados** no módulo compilado; a CLI (`cargo install wasm-bindgen-cli`) lê esses metadados, remove-os e gera o "**JavaScript wrapper bridge**" com as funções/classes que você quer expor.
- Projeto mínimo (`Cargo.toml` + `src/lib.rs`):

```toml
[package]
name = "bindgenhello"
version = "0.1.0"

[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2"
```

```rust
use wasm_bindgen::prelude::*;

// Import 'window.alert'
#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

// Export a 'hello' function
#[wasm_bindgen]
pub fn hello(name: &str) {
    alert(&format!("Hello, {}!", name));
}
```

```bash
cargo build --target wasm32-unknown-unknown
wasm-bindgen target/wasm32-unknown-unknown/debug/bindgenhello.wasm --out-dir .
```

- Importar funções de **namespaces JavaScript** específicos e classes de bibliotecas JS (ex.: ROT.js):

```rust
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);

    #[wasm_bindgen(module = "./index")]
    fn stats_updated(stats: JsValue);

    pub type Display;
    #[wasm_bindgen(method, structural, js_namespace = ROT)]
    fn draw(this: &Display, x: i32, y: i32, ch: &str);
    #[wasm_bindgen(method, structural, js_name = draw, js_namespace = ROT)]
    fn draw_color(this: &Display, x: i32, y: i32, ch: &str, color: &str);
}
```

  - `js_namespace` importa de um módulo JS específico; `method` + `structural` ligam métodos de classes JS a funções Rust com `this` explícito; `js_name = draw` mapeia overloads; `pub type Display` dentro do `extern` torna a classe JS utilizável como struct Rust.
  - Do lado JS, structs Rust decorados com `#[wasm_bindgen]` aparecem como **classes JS** exportáveis no arquivo gerado: `import { Engine, PlayerCore } from './roguewasm';` — e `new Engine(this.display)` passa uma instância de classe JS para dentro do Rust como se fosse nativa.

## 2. `JsValue`, `Option`/`Result` e passagem de dados

- **`JsValue`** é o tipo "qualquer valor JS". Para callbacks que passam objetos dinâmicos, em vez de espelhar structs em ambos os lados, envie JSON cru via `JsValue` — mais rápido e sem boilerplate de classe gerada.
- Com a feature **`serde-serialize`** e `serde`/`serde_derive`, serialize structs Rust para `JsValue`:

```toml
[dependencies]
serde = "^1.0"
serde_derive = "^1.0"

[dependencies.wasm-bindgen]
version = "^0.2"
features = ["serde-serialize"]
```

```rust
#[derive(Serialize)]
pub struct Stats {
    pub hitpoints: i32,
    pub max_hitpoints: i32,
    pub moves: i32,
}

// no callback do jogo:
stats_updated(JsValue::from_serde(&stats).unwrap());
```

- Memória: wasm-bindgen gera `__wbindgen_free()` e utilitários equivalentes para liberar memória linear alocada por valores atravessando a fronteira — o glue JS chama isso automaticamente ao descartar objetos.
- Módulos que precisam rodar **dentro e fora do browser** (cap. 10, "Designing Code for In and Out of the Browser"): isole código browser-only atrás de `#[cfg(target_arch = "wasm32")]` e mantenha a lógica central (engine, regras) agnóstica de host — padrão usado no jogo Rogue do livro.

## 3. Framework Yew (cap. 5)

- **Yew** é o framework de UI em Rust (estilo componentizado, com Virtual DOM) que também compila para wasm via wasm-bindgen; o livro constrói um **chat ao vivo multiusuário** com WebSocket.
- O padrão de integração importa hooks/serviços JS, usa `JsValue`/`serde` para payloads e trata eventos do browser via callbacks registrados pelo framework — sem escrever glue JavaScript manual.
- Referências de API global do browser (`js_sys`, `web_sys`) e utilitários (`document()`, `window()`) vêm do ecossistema wasm-bindgen (`wasm-bindgen` + `js_sys` + `web_sys`).

## 4. wasm-pack e distribuição

- O `wasm-pack` empacota módulos Rust+wasm-bindgen em pacotes **npm** e é a via recomendada para distribuir e consumir módulos em bundlers web. O livro o cita no contexto de **serverless** (deploy de módulos a Cloudflare Workers via `wasm-pack`).
- Fluxo padrão (moderno, complementando o livro): `wasm-pack build --target web|bundler|nodejs|no-modules` — escolha o target conforme consumidor (navegador direto, webpack/npm, Node.js, ou glue próprio gerando `*.d.ts` TypeScript).
- Note que o livro (2019, Rust 2018) usa CLI `wasm-bindgen` + npm/webpack manualmente; hoje prefira `wasm-pack` para o mesmo resultado, mantendo os mesmos atributos `#[wasm_bindgen]`.

## 5. Hosts fora do browser (cap. 6–7)

- **Contrato de um bom host** (load/validate, expor exports, satisfazer imports, executar, isolar módulos) — detalhado em [wasm-definitive-guide.md](wasm-definitive-guide.md) §3.
- O livro cria hosts em Rust com o crate **wasmi** (interpretador extraído do cliente Ethereum da Parity):

```toml
[dependencies]
wasmi = "0.4"
```

```rust
use wasmi::{ImportsBuilder, ModuleInstance, NopExternals, RuntimeValue};

let module = wasmi::Module::from_buffer(buffer)?;
// injeta host functions via ImportsBuilder; invoca exports e lê RuntimeValue
```

- **Host functions**: o host registra funções Rust que o módulo chama via imports — é assim que módulos fazem I/O (satisfazendo o contrato do host). Um host "mock" que satisfaz os mesmos imports torna módulos testáveis fora do ambiente real.
- **IoT**: capítulo 7 roda o mesmo interpretador em **Raspberry Pi** (ARM) controlando LEDs via GPIO com módulos wasm como "indicator modules" — prova do conceito "wasm como plugin portátil em qualquer host".

## 6. Segurança (Apêndice A2)

- Vetores no browser: módulos wasm são dados — valide procedência (assinatura/autenticação), evite instanciar `.wasm` de fontes não confiáveis sem validação, e lembre que o módulo pode abusar dos **imports** que o glue JS concede (mínima superfície de imports).
- O livro recomenda **assinatura e criptografia de módulos** no pipeline de distribuição ( Signing/Encrypting WebAssembly Modules ) e destaca que o módulo não consegue auto-instanciar sua execução — o host é o ponto de controle.

---

### Ligações

- Toolchain WABT/WASI/Emscripten/threads → [wasm-definitive-guide.md](wasm-definitive-guide.md)
- Conceitos base/API JS → [wasm-mdn-guide.md](wasm-mdn-guide.md)
- Para *game projects* em C++ (setup Emscripten, memória, modularização, build) consulte *Learn WebAssembly* (Mike Rourke).
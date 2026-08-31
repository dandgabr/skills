# WebAssembly: The Definitive Guide (Brian Sletten) — Notas Consolidadas

> Fonte: *WebAssembly: The Definitive Guide — Safe, Fast, and Portable Code* (Brian Sletten, O'Reilly, 2022).
> Complementa [wasm-mdn-guide.md](wasm-mdn-guide.md) (guia MDN) com a perspectiva de toolchain, WASI, Emscripten e execução fora do browser.

---

## 1. Modelo de execução e módulos (cap. 1–3)

- WebAssembly foi concebido para software **safe, fast, portable e compact** — não como substituto do JavaScript, mas como complemento na mesma VM.
- Um **module** é a forma compilada (binária) de um programa; a execução requer: carregar/validar bytes → satisfazer imports (funções, memórias, globals) → instanciar (`Instance`) → invocar exports ou executar `start`.
- O formato binário é seccionado (types, imports, functions, tables, memory, globals, exports, start, elem, code, data, custom). Use `wasm-objdump -x` para inspecionar cada seção.
- O **linear memory** é o único canal de dados por valor entre host e guest; `Memory` é um `ArrayBuffer` (ou `SharedArrayBuffer`) em páginas de 64 KB. Strings/estruturas precisam ser serializadas na memória + passadas (ponteiro, comprimento).
- **Tables** dissociam ponteiros de função do `code` e habilitam **dynamic linking** (side modules com `-s SIDE_MODULE=1`; main module com `MAIN_MODULE=1`).
- A MVP deliberadamente deixou de fora threads, GC e exceções (não existiam em todas as linguagens) — todos retornam como *propostas* independentes, adotadas por runtimes de forma incremental (cap. 12).

## 2. Toolchain WABT (cap. 2–3, Apêndice)

Instalação via **wabt** (brew/apt/npm) ou pela [WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt). Ferramentas citadas no livro:

| Ferramenta | Uso |
|---|---|
| `wat2wasm` | Converte texto `.wat` → binário `.wasm` |
| `wasm2wat` | Converte binário de volta para texto (leitura/debug) |
| `wasm-objdump` | Inspeciona seções/símbolos (`-x` para detalhado; `-d` para disassembly) |
| `wasm-interp` | Executa módulos direto no terminal (REPL wasm) |
| `wasm-validate` | Valida conformidade do binário |
| `wasm2c` | Gera código C a partir de um binário wasm (embedding nativo) |

Padrões do livro ao construir módulos "à mão":

```bash
wat2wasm hello.wat -o hello.wasm
wasm-objdump -x hello.wasm
# preserve function/local names for debugging (Custom section):
wat2wasm hello.wat -o hellodebug.wasm --debug-names
wasm-objdump -x hellodebug.wasm
```

- Sem `--debug-names`, o objdump mostra apenas índices numéricos; os *names* de funções/locais vivem em uma **Custom section** não observável pela semântica.
- Módulos podem viver em arquivos ou inline no JS via `WebAssembly.Module` a partir de bytes; o livro demonstra REPL com `wasm-interp` e no browser com o glue mínimo de `instantiateStreaming`.

## 3. WASI — WebAssembly System Interface (cap. 11–12)

- **Problema**: o wasm MVP não tem I/O; cada host reinventaria acesso a arquivos, console, tempo, RNG e sockets. WASI padroniza um *contract* portátil e seguro.
- O módulo importa funções do namespace `wasi_snapshot_preview1` (historicamente `wasi_unstable`), ex.: `fd_write` (stdout), `fd_read`, `proc_exit`, `environ_get`, `random_get`, `clock_time_get`.
- Um módulo WASI exporta `memory` e `_start` (o `main` do programa). Exemplo mínimo de `fd_write` em Wat (do tutorial do Wasmtime reproduzido no livro):

```wat
(module
  (import "wasi_unstable" "fd_write"
    (func $fd_write (param i32 i32 i32 i32) (result i32)))
  (memory 1)
  (export "memory" (memory 0))
  (data (i32.const 8) "hello world\n")
  (func $main (export "_start")
    ;; iov.iov_base = 8, iov.iov_len = 12, io = fd 1 (stdout)
    (i32.store (i32.const 0) (i32.const 8))
    (i32.store (i32.const 4) (i32.const 12))
    (call $fd_write (i32.const 1) (i32.const 0) (i32.const 1) (i32.const 20))
    drop))
```

```bash
wasmtime hello.wat   # WASI hosts executam .wat diretamente
wasmer  hello.wat
```

- **Security baseada em capabilities**: o módulo não recebe acesso direto a file handles/sockets — recebe *handles opacos e inforgeáveis* ("preopened file descriptors"). Sem a capability, a chamada à libc falha:

```bash
# falha: sem capability de escrita no diretório atual
wasmtime target/wasm32-wasi/release/hello-fs.wasm
# funciona: concede o diretório como preopen
wasmtime --dir=. target/wasm32-wasi/release/hello-fs.wasm
wasmer  --dir=. target/wasm32-wasi/release/hello-fs.wasm
```

- **Toolchains**: `clang` + **wasi-sdk** (sysroot WASI para C/C++), Rust com `cargo build --target wasm32-wasi`, ou `cargo install cargo-wasi` + `cargo wasi run`.
- **Runtimes WASI** citados: **Wasmtime** (Bytecode Alliance, ex-Mozilla), **Wasmer**, **wasm3**, **WasmEdge** (blockchains/veículos); plataformas: Istio/Envoy plugins, Fastly Compute@Edge, Cloudflare Workers, wasmCloud (atores), Krustlet (Kubernetes).

### Runtimes embutidos via Wasmtime (Rust host)

Tipos centrais do Wasmtime: `Engine` (configuração compartilhável entre threads) → `Store` (unidade de isolamento; objetos não vazam entre Stores) → `Module` (forma compilada) → `Instance` (módulo + estado).

```rust
use wasmtime::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let engine = Engine::default();
    let mut store = Store::new(&engine, ());
    let module = Module::from_file(&engine, "hello.wat")?;
    let instance = Instance::new(&mut store, &module, &[])?;
    let how_old =
        instance.get_typed_func::<(i32, i32), (i32), _>(&mut store, "how_old")?;
    let age: i32 = how_old.call(&mut store, (2021i32, 2000i32))?;
    println!("You are {age}");
    Ok(())
}
```

Também há API equivalente em **bash** (`wasmtime hello.wat --invoke how_old 2021 2000`) e binding para C/Python/.NET. Casos de uso de hosts: plug-ins seguros, serverless, filtros de proxy, hot-swap, motores de regras/blockchain.

### Padrões host ↔ guest (Hoffman, cap. 6 + Sletten)

Um "bom host" deve: (1) **carregar e validar** o binário wasm; (2) **expor exports** com glue de invocação; (3) **satisfazer imports** ou falhar com erro claro; (4) **executar o módulo** (inclusive `start`); (5) **isolar módulos** — um módulo não pode chamar funções privadas ou corromper dados de outro; falha em um módulo nunca deve derrubar o host ou outro módulo.

## 4. Emscripten (cap. 5–6)

- Baseado em **LLVM**; gera `.wasm` + glue JS (e HTML opcional). É a via prática para portar código C/C++ legado: provê `emcc`, versões wasm de `cc`, `make`, `configure`, libc parcial, SDL e OpenGL sobre Web APIs.
- O objeto `Module` no JS gerado é a interface entre os mundos. Flags citadas no livro:

```bash
emcc hello.c -o hello.js                            # roda main() ao carregar
emcc hello.c -o hello.js -s INVOKE_RUN=0            # não executa main() automaticamente
emcc hello.c -o hello.js -s INVOKE_RUN=0 \
  -s EXTRA_EXPORTED_RUNTIME_METHODS="['callMain']"  # expõe Module.callMain()
emcc with-glue.c -O3 -s WASM=1 -s USE_SDL=2 -s MODULARIZE=1 -o custom-loading.js
```

- `-s INVOKE_RUN=0` + `Module.callMain()` permite chamar o `main` em resposta a eventos (ex.: clique de botão); `-s MODULARIZE=1` transforma o carregamento numa API Promise-like (útil p/ carregamento customizado, cf. Rourke cap. 5).
- **File System virtual (MEMFS)**: código C/C++ que escreve em disco roda sem modificação — Emscripten emula um FS em memória sobre o sandbox do browser. Permite portar bibliotecas de terceiro (ex.: bitmap, libsodium) quase "drop-in".
- **embind**: `-s MODULARIZE=1` com `emcc --bind -o example.js example.cpp` para expor classes/funções C++ a JS com conversão de tipos.
- Para módulos puros (sem glue pesado) use `-s SIDE_MODULE=1` na compilação de bibliotecas a serem linkadas dinamicamente.

## 5. Web APIs e bindings (cap. 8–10)

- **Node.js/Deno**: wasm funciona nativamente (sem DOM); bom para extensões nativas seguras de Node (alternativa a addons C++), mitigando **supply-chain attacks** por sandboxing de módulos de terceiros.
- **Rust+wasm-bindgen** (detalhes em [wasm-with-rust.md](wasm-with-rust.md)): o livro usa wasm-bindgen também para **threads** e gera *TypeScript Declaration files* (`*.d.ts`) prontos para consumo npm.
- **TensorFlow.js**: backend WebAssembly acelera inferência quando WebGL é insuficiente; SIMD/threads (`/s` SIMD 128-bit, `v128`) elevam ainda mais a performance de ML no browser.
- **Testing/proposals**: Multi-Value Return (funções retornam múltiplos valores — resolve o padrão `(ptr,len)` de strings), Reference Types (`externref`/`funcref` em tabelas), Module Linking, Feature Testing (`WebAssembly.validate` por proposital feature), Threads, GC, Exceptions.

## 6. Threading e memória (conceitos transversais)

- **Memory API**: `grow(delta)` expande em páginas de 64 KB; views TypedArray ficam **destacadas** após o crescimento — recree as views sempre após `grow()`.
- **Threading**: a proposta de threads adiciona memórias *shared* (`SharedArrayBuffer`) + instruções atômicas. No browser: cada thread roda um `Web Worker` com a **mesma** memória compartilhada (transferida via `postMessage`); bloqueio/sincronização com `Atomics.wait`/`notify` (no worker; não na main thread). Requer COOP/COEP headers para ativar `SharedArrayBuffer`. Emscripten expõe via `-pthread`/`PTHREAD_POOL_SIZE` (cap. 12 "threads, garbage collection, e exceptions" como propostas em evolução).
- **Stack/Heap**: dentro do linear memory há uma região de *data/stack* fixa (endereços em `__data_end`/`__heap_base` nos exports — visíveis no `wasm-objdump -x` de módulos Rust); alocações dinâmicas vão para o heap (dlmalloc/emmalloc no Emscripten; runtime do AssemblyScript faz GC próprio desde v0.18). `memory.grow()` é o únicos mecanismo de expansão.
- **Feature testing**: consulte proposta-a-proposta em tempo de execução antes de depender de threads/SIMD/multi-value.

## 7. Onde não usar wasm

- Substituir JavaScript na camada de aplicação/DOM;
- Apps pequenas onde o custo do glue e do binário supera o ganho;
- Lógica de UI — wasm não acessa DOM; toda interação passeia pela fronteira JS.

**Onde brilhar** (Sletten, cap. 1/9/15/16): jogos, codecs, criptografia (libsodium), ML (TensorFlow), legacy C/C++ no browser, extensão de servidores (Istio/proxies), edge/serverless (Fastly, Cloudflare), IoT (Raspberry Pi, cf. Hoffman cap. 7), plataformas de plug-ins, aplicações descentralizadas (ewasm/Polkadot/IPFS).

---

### Ligações

- Fundamentos/API JS/Memória/Tabelas → [wasm-mdn-guide.md](wasm-mdn-guide.md)
- Rust/wasm-bindgen/wasm-pack → [wasm-with-rust.md](wasm-with-rust.md)
- Emscripten com projetos C/C++ e SDL → *Learn WebAssembly* (Mike Rourke, Packt): setup EMSDK, `emcc` flags `WASM=1`, `USE_SDL=2`, `MODULARIZE=1`, `ALLOW_MEMORY_GROWTH=1`, `SIDE_MODULE=1` (dynamic linking) e build com Makefile custom.
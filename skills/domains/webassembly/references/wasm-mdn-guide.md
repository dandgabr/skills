# WebAssembly — Guia de Referência MDN

Consolidado da documentação oficial do MDN Web Docs (developer.mozilla.org/pt-BR/docs/WebAssembly): Conceitos, API JavaScript (Módulo, Instância, Memória, Tabela, Global), compilação (C/C++, Rust, AssemblyScript), formato de texto (.wat) e JSPI.

---

## 1. Conceitos Fundamentais

**O que é**: linguagem de baixo nível tipo assembly com formato binário compacto (`.wasm`), executada com performance quase nativa em browsers modernos. **Não substitui o JavaScript** — complementa executando lado a lado na mesma VM.

**Objetivos (W3C WebAssembly CG)**:
1. Rápido, eficiente e portável (performance nativa em qualquer plataforma).
2. Legível e depurável (formato texto `.wat` com correspondência 1:1 ao binário).
3. Seguro — sandbox com mesma política de origem e permissões do browser.
4. Não quebrar a web (compatibilidade retroativa).

**Conceitos-chave (refletidos 1:1 na API JS)**:

| Conceito | Definição |
| :--- | :--- |
| **Module** | Binário compilado pelo browser em código executável. Sem estado; compartilhável entre janelas/workers via `postMessage()` como um `Blob`; declara imports/exports como um módulo ES2015. |
| **Memory** | `ArrayBuffer` **redimensionável** (ou `SharedArrayBuffer`) contendo array linear de bytes lidos/escritos por instruções de memória do wasm. |
| **Table** | Array **tipado e redimensionável** de referências (ex.: `funcref`) — não pode residir na memória linear por segurança/portabilidade. Base para ponteiros de função C/C++. |
| **Instance** | Module pareado com todo o estado de execução (Memory, Table, imports). Equivalente a módulo ES2015 carregado com um conjunto específico de imports. |

**Multiplicidade** (importante para vínculo dinâmico):
- Um Module pode ter **N** Instances.
- Uma Instance usa 0–1 Memory e 0–1 Table (futuro: 0–N).
- Uma Memory/Table pode ser compartilhada por 0–N Instances (espaço de endereço comum → dynamic linking).

## 2. Compilação — Pontos de Entrada

1. **Emscripten (C/C++)**: alimenta o código no clang+LLVM → transforma em `.wasm` + gera "código de cola" JS/HTML (implementa SDL, OpenGL, OpenAL, POSIX sobre Web APIs). O wasm **não acessa o DOM diretamente** — só chama JS, que faz as chamadas às APIs Web.
2. **Rust → Wasm**: via Rust Wasm Working Group (`wasm-pack`, gera pacote npm).
3. **AssemblyScript**: sintaxe tipo TypeScript → `.wasm`; bundle pequeno, performance um pouco inferior a C/Rust; ideal para devs web.
4. **Wasm direto (formato texto)**: escrever `.wat` e converter com ferramentas (WABT `wat2wasm`); playgrounds: WasmFiddle, WasmExplorer.

## 3. Formato Texto (.wat)

- Módulo, funções, imports com **namespace de dois níveis**:
  ```wat
  (module
    (func $i (import "imports" "imported_func") (param i32))
    (func (export "exported_func")
      i32.const 42
      call $i))
  ```
- S-expression; em debug, browsers expõem `wasm://` no painel Debugger (breakpoints, call stack, step sobre o texto).
- Conversão 1:1 `.wat` ↔ `.wasm` (WABT: `wat2wasm`, `wasm2wat`).

## 4. API JavaScript WebAssembly

### Métodos estáticos

| Método | Uso |
| :--- | :--- |
| `WebAssembly.instantiateStreaming(fetch(url), importObject)` | **Preferido**: compila+instancia direto do stream da resposta (`Response`), sem passar por `ArrayBuffer`. |
| `WebAssembly.compileStreaming(source)` | Compila apenas → `Promise<Module>`. |
| `WebAssembly.instantiate(bytes \| Module, importObject)` | Requer etapa extra `response.arrayBuffer()`. |
| `WebAssembly.compile(bytes)` | Compila de `ArrayBuffer`. |
| `WebAssembly.validate(bytes)` | Verifica se bytes são válido wasm (`boolean`). |
| `WebAssembly.promising(fn)` | **JSPI**: transforma função JS exportada do wasm em AsyncFunction (promise). |

### Exemplo canônico (streaming)

```javascript
const importObject = {
  imports: { imported_func: (arg) => console.log(arg) }, // namespace de 2 níveis
};

WebAssembly.instantiateStreaming(fetch("simple.wasm"), importObject).then(
  (obj) => obj.instance.exports.exported_func(),
);

// Sem streaming (fallback):
fetch("simple.wasm")
  .then((r) => r.arrayBuffer())
  .then((bytes) => WebAssembly.instantiate(bytes, importObject))
  .then(({ instance }) => instance.exports.exported_func());
```

### WebAssembly.Module
- `new WebAssembly.Module(bytes)` (síncrono); `Module.customSections()`, `Module.exports()`, `Module.imports()` (introspecção estática).
- Cacheável em **IndexedDB** e compartilhável com workers (grande ganho de startup).

### WebAssembly.Instance
- `instance.exports` → funções exportadas como funções JS normais (chamada síncrona).

### WebAssembly.Memory

```javascript
const memory = new WebAssembly.Memory({ initial: 10, maximum: 100 }); // páginas de 64KB
new Uint32Array(memory.buffer)[0] = 42;      // escrita
memory.grow(1);                              // +1 página (64KB)
```

- Unidades de `initial`/`maximum`/`grow()` = **páginas de 64 KB**.
- Ultrapassar `maximum` → `RangeError`. Declarar maximum permite pré-reserva eficiente.
- ⚠️ **Detached buffer**: após `grow()`, `memory.buffer` retorna **novo** `ArrayBuffer`; views antigas ficam inválidas ("desconectadas"). Sempre recriar `TypedArray` após grow.
- Memória pode ser importada (permite preencher conteúdo inicial via JS e compartilhar entre instâncias) ou exportada:
  ```javascript
  WebAssembly.instantiateStreaming(fetch("memory.wasm"), { js: { mem: memory } })
    .then(({ instance }) => {
      const i32 = new Uint32Array(memory.buffer);
      for (let i = 0; i < 10; i++) i32[i] = i;
      console.log(instance.exports.accumulate(0, 10));
    });
  ```
- **Memórias compartilhadas** (`shared: true`): `SharedArrayBuffer` transferível entre Window/Worker via `postMessage()` (usar com Atomics).

### WebAssembly.Table

- Array redimensionável de referências (element type: hoje limitado a `funcref`/`externref`); necessário para ponteiros de função C/C++ (índices ficam na memória linear; a referência fica na tabela com verificação de limites).
- Métodos: `set(index, ref)`, `get(index)`, `grow(n)`, `length`.
  ```javascript
  WebAssembly.instantiateStreaming(fetch("table.wasm")).then(({ instance }) => {
    const tbl = instance.exports.tbl;
    console.log(tbl.get(0)()); // 13  — dois parênteses: get() retorna a função
  });
  ```

### WebAssembly.Global

```javascript
const global = new WebAssembly.Global({ value: "i32", mutable: true }, 0);
global.value = 42;                       // set via JS
WebAssembly.instantiateStreaming(fetch("global.wasm"), { js: { global } })
  .then(({ instance }) => {
    instance.exports.getGlobal();        // 42
    instance.exports.incGlobal();        // wasm muta o global
    global.value;                        // 43
  });
```
- `value`: `i32`, `i64`, `f32`, `f64` (e referências). `mutable: boolean`.
- Bloco de construção para **vínculo dinâmico** entre múltiplos módulos.

### Exceções e JSPI

- `WebAssembly.Tag`, `WebAssembly.Exception` (`is()`, `getArg()`, `stack`): interop de exceções wasm↔JS; instruções `try_table`/`catch`/`throw` no wasm.
- `WebAssembly.Suspending()` + `WebAssembly.promising()`: **JSPI (JavaScript Promise Integration)** — suspender wasm durante Promises e retomar depois, sem bloquear a main thread.
- Erros: `CompileError`, `LinkError` (imports/exports incompatíveis), `RuntimeError` (ex.: `unreachable`), `SuspendError`.

## 5. Tipos de Valor

| Tipo | Descrição |
| :--- | :--- |
| `i32`, `i64` | Inteiros 32/64 bits (i64 cruza a fronteira JS como `BigInt`). |
| `f32`, `f64` | Ponto flutuante 32/64 bits. |
| `v128` | Vetor SIMD de 128 bits (instruções SIMD: splat, shuffle, extract_lane, load/store lane, trunc_sat, i8x16/i16x8/i32x4/f32x4/f64x2). |
| `funcref` | Referência a função (tabelas). |
| `externref` | Referência opaca a valores JS/(host). |
| `exnref` | Referência a exceção (EH propostas). |

## 6. Estruturas do Módulo (seções/definições)

- `func` (types), `data` (bytes em memória), `elem` (elementos de tabela), `global`, `memory`, `table`, `tag`.
- Instruções principais: control flow (`block`, `loop`, `if...else`, `br`, `br_if`, `br_table`, `call`, `return`, `unreachable`, `select`, `drop`, `nop`), variáveis (`local.get/set/tee`, `global.get/set`), memória (`load/store`, `grow`, `copy`, `fill`, `init`, `size`), numéricas (add/sub/mul/div/rem, bit operators, clz/ctz/popcnt, converts/reinterprets), SIMD.

## 7. Segurança e Boas Práticas

- **Sandbox**: mesmo origem/perm policy do browser; sem acesso direto a DOM/arquivo/rede — sempre via JS glue.
- **Validar imports/exports**: mismatches geram `LinkError`; use `WebAssembly.validate()` e `Module.imports()/exports()` para introspecção antes de instanciar.
- **Preferir streaming**: `instantiateStreaming` reduz latência de parse (bypass de `ArrayBuffer`).
- **Cache de módulos** grandes no IndexedDB (armazenar bytes compiláveis) para acelerar startup.
- **CORS/MIME**: servir `.wasm` com `Content-Type: application/wasm` (necessário para streaming compile).
- **Memory safety**: sempre recriar TypedArrays após `grow()`; usar `Atomics` em memórias compartilhadas entre threads.
- **Interações JS↔wasm síncronas**: evite glue quente demais (chamadas frequentes têm custo de fronteira); mova loops inteiros para dentro do wasm.
- **Debugging**: painel Debugger (Firefox 54+) mostra `wasm://` com representação texto, breakpoints e call stack.
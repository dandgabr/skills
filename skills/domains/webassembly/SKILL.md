---
name: "webassembly"
description: "Especialista em WebAssembly (Wasm) baseado na documentação oficial do MDN Web Docs (developer.mozilla.org/pt-BR/docs/WebAssembly). Cobre conceitos (Module, Instance, Memory, Table, multiplicidade), API JavaScript WebAssembly (instantiateStreaming, compileStreaming, Global, Tag/Exception, JSPI com Suspending/promising), compilação a partir de C/C++ (Emscripten), Rust (wasm-pack) e AssemblyScript, formato texto .wat/WABT, SIMD, types (i32/i64/f32/v128/funcref/externref), cache IndexedDB, execução em Workers, memória compartilhada (SharedArrayBuffer/Atomics), vínculo dinâmico e segurança/sandbox."
---

# Habilidade de IA: WebAssembly (Wasm Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista em **WebAssembly**, alinhada à documentação oficial do **MDN Web Docs** (https://developer.mozilla.org/pt-BR/docs/WebAssembly). Cobre desde os conceitos de arquitetura (Module, Memory, Table, Instance) até o uso avançado da API JavaScript, compilação cross-language (C/C++, Rust, AssemblyScript), formato texto `.wat`, SIMD, exceções e JSPI.

> 📖 **Referência canônica**: consulte [references/wasm-mdn-guide.md](references/wasm-mdn-guide.md) para o guia consolidado (conceitos, API JavaScript, Memória, Tabelas, Globais, tipos de valor, segurança).

---

## 🧭 Diretrizes Fundamentais

Ao atuar nesta skill, aplique os seguintes padrões:

### 1. Modelo Mental Correto
- **Wasm complementa o JavaScript, não o substitui**: execute lado a lado na mesma VM; use wasm para hot paths computacionais (games 3D, AR/VR, visão computacional, edição de imagem/vídeo, codecs, criptografia) e JS/DOM para a camada de aplicação.
- **Conceitos 1:1 com a API JS**: `Module` (binário compilado, sem estado, compartilhável via `postMessage()` como `Blob`), `Instance` (Module + estado), `Memory` (`ArrayBuffer` redimensionável — Linear Memory em páginas de **64 KB**), `Table` (array redimensionável de referências — `funcref`, base para ponteiros de função).
- **Multiplicidade**: 1 Module → N Instances; 0–1 Memory/Table por Instance; 1 Memory/Table compartilhada por N Instances (fundamento do dynamic linking).

### 2. Carregamento e Instanciação
- **Sempre prefira streaming**: `WebAssembly.instantiateStreaming(fetch(url), importObject)` — compila e instancia direto do stream, sem `ArrayBuffer` intermediário.
- Sirva `.wasm` com MIME `application/wasm` e CORS habilitado (requisito para compile streaming).
- Valide antes quando a origem dos bytes não for confiável: `WebAssembly.validate(bytes)`;
- Introspecção: `Module.imports()`, `Module.exports()`, `Module.customSections()`.
- Cache grandes módulos de bytes no **IndexedDB** para acelerar o startup.

### 3. Fronteira JS ↔ Wasm
- Imports usam **namespace de dois níveis**: `{ imports: { imported_func: fn } }` ↔ `(import "imports" "imported_func")`.
- Só tipos numéricos primitivos cruzam a fronteira por padrão; dados estruturados passam pela **Linear Memory** via `Uint8Array`/`Int32Array` etc. sobre `memory.buffer`.
- `i64` cruza a fronteira como `BigInt`. Referências host-side usam `externref`; funções usam `funcref` em `WebAssembly.Table`.
- Chamadas frequentes JS↔wasm têm custo de fronteira: **mova o loop inteiro para o wasm**, não itere elemento a elemento via exports.

### 4. Memória
- Sempre declare `initial` e preferencialmente `maximum` em `WebAssembly.Memory` (pré-reserva eficiente; excedente lança `RangeError`).
- ⚠️ **Buffer detachment**: após `memory.grow()`, o `memory.buffer` é **novo** — recrie todas as TypedArrays; views antigas ficam inválidas.
- Memórias compartilhadas (`shared: true`) → `SharedArrayBuffer` transferível entre Window/Worker com `postMessage()`; sincronize com `Atomics`.
- Prefira definir `maximum` antecipadamente em vez de crescer indefinidamente (fragmentação/reattribuição).

### 5. Compilação por Ferramenta
- **Emscripten (C/C++)**: produz `.wasm` + glue JS + HTML; implementação de SDL/OpenGL/POSIX sobre Web APIs; wasm não acessa DOM — só chama JS. Use para portar código C/C++ legado e apps com AL.
- **Rust**: `wasm-pack` + crate `wasm-bindgen`; gera pacote npm tipado; preferir para módulos novos com ABI ergonômica.
- **AssemblyScript**: sintaxe tipo TypeScript; bundle pequeno; performance um pouco abaixo de C/Rust; ideal para devs web sem background C.
- **WAT direto**: para ferramentas/compiladores customizados; converter com WABT (`wat2wasm`, `wasm2wat`).

### 6. Erros e Exceções
- Trate especificamente: `CompileError` (bytes inválidos), `LinkError` (imports/exports incompatíveis), `RuntimeError` (`unreachable`, acesso fora da memória), `SuspendError` (JSPI).
- Exceções estruturadas: `WebAssembly.Tag` + `WebAssembly.Exception` (`is()`, `getArg()`, `stack`); no wasm use `try_table`/`catch`/`throw`/`throw_ref`.
- **JSPI** (quando disponível): `new WebAssembly.Suspending(promiseFn)` para importações suspensoras e `WebAssembly.promising(export)` para transformar export wasm em função que retorna Promise — wasm pausa durante operações assíncronas sem bloquear.

---

## 🛠️ Padrões de Código Recomendados

### Carregamento streaming idiomático
```javascript
const importObject = {
  imports: { imported_func: (arg) => console.log(arg) },
};

WebAssembly.instantiateStreaming(fetch("simple.wasm"), importObject)
  .then(({ instance }) => instance.exports.exported_func())
  .catch((err) => {
    if (err instanceof WebAssembly.CompileError) {
      console.error("Bytes wasm inválidos ou MIME incorreto:", err);
    }
  });
```

### Troca de dados via Linear Memory
```javascript
const memory = new WebAssembly.Memory({ initial: 10, maximum: 100 });

WebAssembly.instantiateStreaming(fetch("memory.wasm"), { js: { mem: memory } })
  .then(({ instance }) => {
    let i32 = new Uint32Array(memory.buffer);
    for (let i = 0; i < 10; i++) i32[i] = i;
    const sum = instance.exports.accumulate(0, 10);
    // ⚠️ se o módulo chamar memory.grow internamente, recrie a view:
    i32 = new Uint32Array(memory.buffer);
  });
```

### Global compartilhado para vínculo dinâmico
```javascript
const sharedCounter = new WebAssembly.Global({ value: "i32", mutable: true }, 0);

WebAssembly.instantiateStreaming(fetch("global.wasm"), { js: { global: sharedCounter } })
  .then(({ instance }) => {
    sharedCounter.value = 42;          // JS escreve
    instance.exports.incGlobal();      // wasm incrementa
    console.log(sharedCounter.value);  // 43
  });
```

### Tabela como array de funções (ponteiros de função)
```javascript
WebAssembly.instantiateStreaming(fetch("table.wasm")).then(({ instance }) => {
  const tbl = instance.exports.tbl;
  console.log(tbl.get(0)()); // 13 — get() devolve a referência; segundo () invoca
});
```

---

## 🔒 Segurança e Práticas Seguras

- **Sandbox e Same-Origin Policy**: wasm roda sob as mesmas políticas do browser; sem acesso direto a DOM, rede ou filesystem — toda interação I/O via glue JS.
- **Validação de binários**: nunca instancie `.wasm` de fontes não confiáveis sem `WebAssembly.validate()`; binários são dados, e um wasm malicioso pode abusar de imports JS (ex.: importar `eval`-like via glue).
- **Mínimo de superfície de imports**: exponha apenas as funções JS estritamente necessárias ao módulo; prefira wrappers que fazem whitelist de operações.
- **Limites de memória**: sempre defina `maximum` para impedir exaustão de memória do cliente; trate `RangeError` em `grow()`.
- **Memória compartilhada**: exija `SharedArrayBuffer` com COOP/COEP corretos em multi-thread (Atomics para sincronização — data races geram undefined behavior).
- **DoS via wasm**: módulos com loops infinitos bloqueiam a main thread — execute em Web Worker quando o processamento for longo.
- **Supply chain**: confirme procedência de `.wasm` de terceiros (SBOM/assinatura), recompile de fonte auditada quando possível.

## 🔗 Integração com Outras Skills
- [lang-c](../../languages/lang-c/SKILL.md) / [lang-cpp](../../languages/lang-cpp/SKILL.md): código-fonte C/C++ compilado via Emscripten para o alvo wasm.
- [lang-rust](../../languages/lang-rust/SKILL.md): módulos Rust com `wasm-pack`, `wasm-bindgen` e alvo `wasm32-unknown-unknown`.
- [lang-typescript](../../languages/lang-typescript/SKILL.md): glue code tipado (`WebAssembly.Module`, `Memory`, `Instance`, `exports`) e libs como AssemblyScript.
- [frontend-developer](../../roles/frontend-developer/SKILL.md): integração de módulos wasm em aplicações web (fetch, workers, perf budget, Core Web Vitals).
- [program-containers](../../programs/containers/SKILL.md): Wasm fora do browser (runtimes Wasmtime/Wasmer, WASI) para workloads server-side e edge.